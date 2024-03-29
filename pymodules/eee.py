import datetime
import os
import random
import json
import time

import config
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.error.ErrorListener import ConsoleErrorListener
from JavaScriptLexer import JavaScriptLexer as JSL
from JavaScriptParser import JavaScriptParser as JSP
from JavaScriptParserVisitor import JavaScriptParserVisitor as JSV
from JavaScriptParserVisitor2 import JavaScriptParserVisitor2 as JSV2
from call_function_with_timeout import SetTimeoutDecorator
import subprocess
import basic
import generator
import js
import tools

IntervalEnd_Vardicts = {}
VariableNames = set()
IntervalEnd_VariableNames = {}  # 用于存储变量名和它们所在的行号
avaliableInterval = []


class Scope:
    def __init__(self, name='global', parent=None):
        self.name = name
        self.parent = parent
        self.variables = {}


class MyVisitor(JSV):
    def __init__(self):
        super().__init__()
        self.globalScope = Scope()
        self.scopeCounter = 0
        self.currentScope = self.globalScope
        self.scopes = [self.globalScope]  # 用于跟踪作用域层级

    def enterScope(self, name=None):
        if name is None:
            name = f"block_{self.scopeCounter}"
            self.scopeCounter += 1
        # 进入新的作用域
        self.currentScope = Scope(name=name, parent=self.currentScope)
        self.scopes.append(self.currentScope)

    def exitScope(self):
        # 离开当前作用域
        self.scopes.pop()
        self.currentScope = self.scopes[-1] if self.scopes else self.globalScope

    # def visitExpressionStatement(self, ctx):
    #     # 使用expressionSequence代替之前假定的expression方法
    #     expressionSequence = ctx.expressionSequence()
    #     for expression in expressionSequence.getChildren():
    #         # print(type(expression).__name__)
    #         if 'AssignmentOperatorExpressionContext' in str(type(expression).__name__):
    #             name = expression.getText()
    #             VariableNames.add(name)
    #     #         print(f"找到表达式: {expression.getText()}")
    #     super().visitExpressionStatement(ctx)
    #
    def visitAssignmentExpression(self, ctx):
        left = ctx.singleExpression(0).getText()
        right = ctx.singleExpression(1).getText()
        VariableNames.add(left)
        # print(left, right)
        super().visitExpressionStatement(ctx)

    def visitFunctionDeclaration(self, ctx):
        function_name = ctx.identifier().getText()
        VariableNames.add(function_name)
        interval = ctx.getSourceInterval()
        if function_name not in list(self.currentScope.variables.keys()):
            self.currentScope.variables[function_name] = interval[1]

        self.enterScope(function_name)
        super().visitFunctionDeclaration(ctx)
        self.exitScope()

    def visitClassDeclaration(self, ctx):
        class_name = ctx.identifier().getText()
        VariableNames.add(class_name)
        interval = ctx.getSourceInterval()
        if class_name not in list(self.currentScope.variables.keys()):
            self.currentScope.variables[class_name] = interval[1]

        self.enterScope(class_name)
        super().visitFunctionDeclaration(ctx)
        self.exitScope()

    def visitBlock(self, ctx):
        self.enterScope()
        super().visitBlock(ctx)
        self.exitScope()

    def visitVariableDeclaration(self, ctx):
        var_name = ctx.assignable().getText()
        VariableNames.add(var_name)
        interval = ctx.getSourceInterval()
        if var_name not in list(self.currentScope.variables.keys()):
            self.currentScope.variables[var_name] = interval[1]
        # print(var_name, interval)
        # print(self.currentScope.variables, self.currentScope.name)
        super().visitVariableDeclaration(ctx)

    def visitIdentifier(self, ctx):
        var_name = ctx.getText()
        interval = ctx.getSourceInterval()
        VariableNames.add(var_name)
        # if var_name not in config.builtins:
        #     VariableNames.add(var_name)
        #     if var_name not in list(self.currentScope.variables.keys()):
        #         self.currentScope.variables[var_name] = interval[1]
        super().visitStatement(ctx)

    def visitStatement(self, ctx):
        interval = ctx.getSourceInterval()
        super().visitStatement(ctx)
        if interval[1] not in avaliableInterval:
            avaliableInterval.append(interval[1])
            IntervalEnd_VariableNames[interval[1]] = []
        super().visitStatement(ctx)

    def getVariablesAtIntervalEnd(self, interval):
        # 假设 interval 是一个 (start, end) 元组
        _, interval_end = interval
        available_variables = set()
        scope = self.currentScope
        # 遍历所有作用域，从当前作用域开始，向上直到全局作用域
        while scope is not None:
            for var_name, var_interval in scope.variables.items():
                var_declaration_line = var_interval
                if var_declaration_line <= interval_end:
                    available_variables.add(var_name)
            scope = scope.parent  # 移动到父作用域

        return list(available_variables)


def init():
    IntervalEnd_Vardicts = {}
    VariableNames = set()
    obj_name8type = {}
    IntervalEnd_VariableNames = {}  # 用于存储变量名和它们所在的行号
    avaliableInterval = []
    config.ids = []
    config.intervals = {}
    for type in range(0, 200):
        config.intervals[type] = []
    config.texts = {}
    for type in range(0, 200):
        config.texts[type] = []
    config.new_samples = []
    config.intervals[1].append((0, 0))


def init2():
    all_type = []
    for type in range(5, 86):
        if len(config.texts[type]) > 0:
            all_type.append(type)
    return all_type


@SetTimeoutDecorator(timeout=10)
def checkParsetime(buf0):
    js_sample0 = buf0.decode()
    input_stream0 = InputStream(js_sample0)
    lexer0 = JSL(input_stream0)
    stream0 = CommonTokenStream(lexer0)
    parser0 = JSP(stream0)
    parser0.removeErrorListeners()
    parser0.addErrorListener(ConsoleErrorListener())
    tree0 = parser0.program()
    return True


def Parse_ast1(buf):
    input_stream = InputStream(buf.decode('utf-8', 'ignore'))
    lexer = JSL(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSP(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())
    tree = parser.program()
    visitor = MyVisitor()
    try:
        visitor.visit(tree)
    except RecursionError:
        return
    rewriter = TokenStreamRewriter(tokens=stream)
    # print("IntervalEnd_VariableNames: ", IntervalEnd_VariableNames)
    return rewriter


@SetTimeoutDecorator(timeout=10)
def Parse_ast2(add_buf):
    input_stream2 = InputStream(add_buf.decode('utf-8', 'ignore'))
    lexer2 = JSL(input_stream2)
    stream2 = CommonTokenStream(lexer2)
    parser2 = JSP(stream2)
    tree2 = parser2.program()
    visitor2 = JSV2()
    try:
        visitor2.visit(tree2)
    except RecursionError:
        pass


def pre_process(buf, add_buf):
    init()
    rewriter = Parse_ast1(buf)
    Parse_ast2(add_buf)
    return rewriter


def insertTamplate(rewriter, interval_ends):
    for interval_end in interval_ends:
        head = "\n////////////////////probe/////////////////////////\n"
        # point = "\n   let point = " + str(interval_end) + ";\n"
        dr = f"   probe(variableNames,{interval_end});\n"
        tmp = head + dr + head
        # 插入
        rewriter.insertAfter(interval_end, tmp)
    probed_sample = rewriter.getDefaultText()
    for interval_end in interval_ends:
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
    return probed_sample


def Dynamic_Reflection(rewriter, engine_path):
    engine_paths = engine_path.split(' ')
    engine_name = engine_paths[0].split('/')[-1]

    interval_ends = list(IntervalEnd_VariableNames.keys())
    probed_sample = insertTamplate(rewriter, interval_ends)
    with open("pymodules/arr1.js", "r", encoding='utf-8') as js_file1:
        # with open("arr1.js", "r", encoding='utf-8') as js_file1:
        js1 = js_file1.read()

    avaliableVar = "\n   let variableNames = " + str(list(VariableNames)) + ";\n"
    with open(f"pymodules/output/{engine_name}/output.js", "w") as js_file:
        js_file.write(js1)
        js_file.write("\n\n")
        js_file.write(avaliableVar)
        js_file.write(probed_sample)

        # 执行 JavaScript Samples
        cmd = []
        for item in engine_paths:
            cmd.append(item)
        cmd.append(f"pymodules/output/{engine_name}/output.js")

        # cmd = ["/home/qbtly/Desktop/target/V8/v8/0124/d8", "--allow-natives-syntax", "--expose-gc", f"output/output{index}.js"]

        result = subprocess.run(cmd, capture_output=True, text=True)
        # print(result.stdout)

        pattern0 = r'qbtly_start&(.*?)&qbtly_end'
        outputs = tools.extract(result.stdout, pattern0)
        for output in outputs:
            # print(output)
            pattern2 = r'qbtly_point_start(.*?)qbtly_point_end'
            interval_end = int(tools.extract0(output, pattern2, 0))

            pattern1 = r'qbtly_aviliable(.*?)qbtly_var'
            js_list = str(tools.extract0(output, pattern1, [])).strip('[]').split(',')
            IntervalEnd_VariableNames[interval_end] = [item.strip() for item in js_list]

            pattern3 = r'qbtly_dicts_start(.*?)qbtly_dicts_end'
            extract_result = tools.extract0(output, pattern3, [])

            dynamic_results = []

            try:
                dynamic_results = json.loads(extract_result)
            except:
                IntervalEnd_VariableNames.pop(interval_end)
                continue

        IntervalEnd_Vardicts[interval_end] = dynamic_results
    # print("IntervalEnd_Vardicts: ", IntervalEnd_Vardicts)
    # print("IntervalEnd_VariableNames: ", IntervalEnd_VariableNames)
    return IntervalEnd_Vardicts


def generate(rewriter, dynamic_results):
    interval_ends = list(dynamic_results.keys())
    if len(interval_ends) > 0:
        # point
        interval_end = random.choice(interval_ends)
        # available variable
        variables = IntervalEnd_VariableNames[interval_end]
        # available variable classify
        classified_variables = tools.classify(dynamic_results[interval_end])
        # available variable information
        objs = dynamic_results[interval_end]
        if len(objs) > 0:
            # choose one variable
            obj_info = random.choice(objs)
            # new variable name
            new_name = tools.get_newname(VariableNames)
            # generate API statement
            new_statement = generator.get_API_statement(obj_info, variables, new_name)
            # insert into sample
            rewriter.insertAfter(interval_end, new_statement)
    new_sample = rewriter.getDefaultText()
    return new_sample


def chang_API(rewriter, all_type):
    pass


def change_parameter(rewriter, all_type):
    type = random.choice(all_type)
    if len(config.intervals[type]) > 0 and len(config.texts[type]) > 0:
        interval = random.choice(config.intervals[type])
        text = random.choice(config.texts[type])
        rewriter.replace("default", interval[0], interval[1], text.strip())
    new_sample = rewriter.getText("default", 0, 10000)
    # new_sample = rewriter.getDefaultText()
    # print(new_sample)
    return new_sample


@SetTimeoutDecorator(timeout=30)
def jungle(buf, add_buf):
    # check timeout
    is_done1, is_timeout1, error_message1, results1 = checkParsetime(buf)
    is_done2, is_timeout2, error_message2, results2 = checkParsetime(add_buf)
    if is_timeout1 is True or is_timeout2 is True:
        return len(config.new_samples)

    # engine
    engine_path = str(os.environ.get('AFL_ENGINE'))

    # pre-process
    rewriter = pre_process(buf, add_buf)

    # dynamic reflection
    dynamic_results = Dynamic_Reflection(rewriter, engine_path)

    # RULE_singleExpression = 65
    # RULE_literal = 73
    # RULE_numericLiteral = 76
    # RULE_identifierName = 80
    # RULE_identifier = 81
    all_type = init2()
    for t in [65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81]:
        all_type.append(t)

    # mutation
    count = 0
    change_p = 0.7
    while count < config.sample_size:
        count += 1
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
        ran = random.random()
        if ran < change_p:
            # 生成
            new_sample = generate(rewriter, dynamic_results)
        elif change_p < ran < 1.0:
            # 更改参数
            new_sample = change_parameter(rewriter, all_type)
        else:
            # 更改API
            new_sample = chang_API(rewriter, all_type)

        if new_sample not in config.new_samples:
            config.new_samples.append(new_sample)
            if len(config.new_samples) > config.sample_size:
                return len(config.new_samples)
    return len(config.new_samples)


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


def parse(buf, add_buf):
    jungle(buf, add_buf)
    return len(config.new_samples)


if __name__ == '__main__':
    # 示例 JavaScript 代码
    js_code = js.js_code4
    js_code2 = js.js_code2
    length = parse(js_code.encode(), js_code.encode())
    print("Total Samples: ", length)
    if length > 0:
        for i in range(0, length):
            with open("/home/qbtly/Desktop/aaaaa/b/" + str(i) + ".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
            # print(fuzz().decode())
    print("/home/qbtly/Desktop/aaaaa/b")
