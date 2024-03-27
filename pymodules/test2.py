import os
import random
import json
import config
# from call_function_with_timeout import SetTimeoutDecorator
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.error.ErrorListener import ConsoleErrorListener
from JavaScriptLexer import JavaScriptLexer as JSL
from JavaScriptParser import JavaScriptParser as JSP
from JavaScriptParserVisitor import JavaScriptParserVisitor as JSV
from JavaScriptParserVisitor2 import JavaScriptParserVisitor2 as JSV2
import subprocess
import basic
import generator
import js, tools
from tools import set_timeout

engine = "/home/qbtly/Desktop/target/V8/v8/0124/d8"
IntervalEnd_Vardicts = {}
VariableNames = set()
obj_name8type = {}
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

    def visitStatement(self, ctx):
        interval = ctx.getSourceInterval()
        super().visitStatement(ctx)
        if interval[1] not in avaliableInterval:
            avaliableInterval.append(interval[1])
            IntervalEnd_VariableNames[interval[1]] = self.getVariablesAtIntervalEnd(interval)
        self.enterScope()
        super().visitBlock(ctx)
        self.exitScope()

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


def all_type_text():
    # print(IntervalEnd_VariableNames)
    for type in range(0, 86):
        if type == type:
            print(type, end=': ')
            for text in config.texts[type]:
                print(text, end="  |  ")
            print('\n')
            for interval in config.intervals[type]:
                print(interval, end="  |  ")
            print('\n')
    exit()


def init():
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


def Parse_ast(js_code):
    input_stream = InputStream(js_code.decode())
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
    for k in list(IntervalEnd_VariableNames.keys()):
        IntervalEnd_VariableNames[k] = list(VariableNames)
    print("IntervalEnd_VariableNames: ", IntervalEnd_VariableNames)
    return rewriter


def pre_process(js_code):
    init()
    rewriter = Parse_ast(js_code)
    return rewriter


def insertTamplate(rewriter):
    news = {}
    for interval_end in list(IntervalEnd_VariableNames.keys()):
        js_var = str(IntervalEnd_VariableNames[interval_end])
        head = "\n////////////////////probe/////////////////////////\n"
        js_id = "\n         let variableNames = " + str(js_var) + ";"  # 被调用过的
        get_type = r'''
                if (!isExecuted) {
                    let output = [];
                    variableNames.forEach(varName => {
                    try{
                        let varInstance = eval(varName);
                        let typeInfo = varIntrospect(varName, varInstance);
                        if (typeInfo !== undefined)
                            output.push(JSON.stringify(typeInfo, setReplacer, 2));
                            a_v.push(varName);
                    }catch(err){
                        null;
                        }
                    });
                    print("qbtly_aviliable[" + a_v + "]qbtly_var");
                    print("qbtly_start[" + output.join(",\n") + "]qbtly_end");
                    isExecuted = true; // 设置标志为 true，防止代码再次执行
                }
                    '''
        tmp = head + js_id + get_type + head
        # 插入
        rewriter.insertAfter(interval_end, tmp)
        new = rewriter.getDefaultText()
        news[interval_end] = new
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
    return news


def get_property(rewriter, engine_path):
    news = insertTamplate(rewriter)
    # print(news)
    with open("arr1.js", "r") as js_file1:
        js1 = js_file1.read()

    IntervalEnd_VariableNames_tmp = IntervalEnd_VariableNames
    keys = list(IntervalEnd_VariableNames_tmp.keys())
    for interval_end in keys:
        if len(IntervalEnd_VariableNames_tmp[interval_end]) <= 0:
            continue
        index = keys.index(interval_end)
        with open(f"output/output{index}.js", "w") as js_file:
            js_file.write(js1)
            js_file.write("\n\n")
            js_file.write(news[interval_end])
            # 执行 JavaScript 文件

        # cmd = [engine, "--allow-natives-syntax", "--expose-gc", f"output/output{index}.js"]
        cmd = [engine_path, f"output/output{index}.js"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        pattern1 = r'qbtly_aviliable(.*?)qbtly_var'
        # 去除首尾的方括号并按逗号分割字符串
        js_list = str(tools.extract(result.stdout, pattern1)).strip('[]').split(',')
        # 去除空格并转换为 Python 的列表
        IntervalEnd_VariableNames[interval_end] =  [item.strip() for item in js_list]

        pattern2 = r'qbtly_start(.*?)qbtly_end'
        extract_result = tools.extract(result.stdout, pattern2)
        var_dicts = []

        try:
            var_dicts = json.loads(extract_result)
            # print("提取成功！")
            # print("extract_result:", extract_result)
        except:
            # print("出错了！", index, result.stdout)
            # print("extract_result:", extract_result)
            IntervalEnd_VariableNames.pop(interval_end)
            continue
        # 丰富var_dicts
        # for var_dict in var_dicts:
        #     obj_type = var_dict['objtype']
        #     if obj_type not in list(obj_name8type.keys()):
        #         obj_name8type[obj_type] = []
        #     obj_name8type[obj_type].append(var_dict['obj'])
        #     var_dict['methods'] = get_call_statements(var_dict['methods'], obj_type)

        IntervalEnd_Vardicts[interval_end] = var_dicts

    print("IntervalEnd_Vardicts: ", IntervalEnd_Vardicts)
    print("IntervalEnd_VariableNames: ", IntervalEnd_VariableNames)
    return IntervalEnd_Vardicts

    # [
    #     {"obj": "v1",
    #     "objtype": "Array",
    #     "methods": [],
    #     "attrs": {"length": "number"}
    #     },
    # ]


def get_call_statements(methods, obj_type):
    # methods ==> var_dict["methods"]
    call_statements = []
    if obj_type in list(basic.methods.keys()):
        typed_methods = basic.methods[obj_type]
        all = list(typed_methods.items())
        b = list(typed_methods.keys())
        for a in all:
            args = ", ".join(a[1])
            call_statement = f"{a[0]}({args})"
            call_statements.append(call_statement)
        for method in methods:
            if method not in b:
                call_statements.append(f"{method}()")
                print(obj_type, method)
    # 输出生成的调用语句
    # for statement in call_statements:
    #     print(statement)
    return call_statements


def get_property_call(obj):
    # 新变量名
    new_var = tools.get_newname(VariableNames)

    # 选择obj
    var_name = obj['obj']

    # method or attr
    chosen_type = random.choice(["methods", "attrs"])
    if chosen_type == "methods":
        try:
            chosen_method = random.choice(obj["methods"])
            call_statement = f"\nlet {new_var} = {var_name}.{chosen_method};\n"
        except:
            call_statement = ""
    else:
        try:
            chosen_attr = random.choice(list(obj[chosen_type].keys()))
            call_statement = f"\nlet {new_var} = {var_name}.{chosen_attr};\n"
            call_statement += f"\n{var_name}.{chosen_attr} = {generator.random_generate(obj[chosen_type][chosen_attr])};\n"
        except:
            try:
                chosen_method = random.choice(obj["methods"])
                call_statement = f"\nlet {new_var} = {var_name}.{chosen_method};\n"
            except:
                call_statement = ""

    return call_statement


def generate(rewriter, intervalend_vardicts):
    interval_ends = list(intervalend_vardicts.keys())
    if len(interval_ends) > 0:
        # 确定插入位置
        interval_end = random.choice(interval_ends)
        # 确定可用变量
        objs = intervalend_vardicts[interval_end]
        if len(objs) > 0:
            obj = random.choice(objs)
            # 生成一条方法调用
            new_statement = get_property_call(obj)
            # 调整
            change_p = 1.0
            for n in range(3):
                ran = random.random()
                if "tmp_number" in new_statement:
                    # Number
                    try:
                        if ran < 0.8:
                            # new_arg = random.choice(obj_name8type['Number'])
                            new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_number()
                    except:
                        new_arg = generator.get_number()
                    # 替换
                    new_statement = new_statement.replace("tmp_number", str(new_arg))
                    pass
                elif "tmp_array" in new_statement:
                    # Array
                    try:
                        if ran < 0.8:
                            # new_array = random.choice(obj_name8type['Array'])
                            new_array = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_array = generator.get_array()
                    except:
                        new_array = generator.get_array()
                    # 替换
                    new_statement = new_statement.replace("tmp_array", str(new_array))
                elif "tmp_string" in new_statement:
                    # String
                    try:
                        if ran < 0.8:
                            # new_arg = random.choice(obj_name8type['String'])
                            new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_string()
                    except:
                        new_arg = generator.get_string()
                    # 替换
                    new_statement = new_statement.replace("tmp_string", new_arg)
                elif "tmp_object" in new_statement:
                    # Object
                    try:
                        if ran < 0.8:
                            new_arg = random.choice(obj_name8type['Object'])
                            # new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_string()
                    except:
                        if ran < 0.5:
                            new_arg = generator.get_string()
                        else:
                            new_arg = generator.get_number()
                    # 替换
                    new_statement = new_statement.replace("tmp_object", new_arg)
                elif "tmp_function" in new_statement:
                    # Function
                    try:
                        if ran < 0.8:
                            new_arg = random.choice(obj_name8type['Function'])
                            # new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_string()
                    except:
                        if ran < 0.5:
                            new_arg = generator.get_string()
                        else:
                            new_arg = generator.get_number()
                    # 替换
                    new_statement = new_statement.replace("tmp_function", new_arg)
                elif "tmp_any" in new_statement:
                    try:
                        new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                    except:
                        if ran < 0.5:
                            new_arg = generator.get_string()
                        else:
                            new_arg = generator.get_number()
                    # 替换
                    new_statement = new_statement.replace("tmp_any", new_arg)
                # 未完待续
            print(new_statement)
            # 插入
            rewriter.insertAfter(interval_end, new_statement)
    new_sample = rewriter.getDefaultText()
    # print(intervalend_vardicts)
    # print(new_sample)
    return new_sample


def insert(rewriter, all_type):
    pass


def change(rewriter, all_type):
    type = random.choice(all_type)
    if len(config.intervals[type]) > 0 and len(config.texts[type]) > 0:
        interval = random.choice(config.intervals[type])
        text = random.choice(config.texts[type])
        rewriter.replace("default", interval[0], interval[1], text.strip())
    new_sample = rewriter.getText("default", 0, 10000)
    # new_sample = rewriter.getDefaultText()
    print(new_sample)
    return new_sample


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


def after_timeout():  # 超时后的处理函数
    print("Timeout!")


# @set_timeout(20, after_timeout())  # 限时 2 秒
def parse(js_code, add_buf):
    engine_path = "/home/qbtly/Desktop/target/V8/v8/0207/d8"
    # engine_path = "/home/qbtly/Desktop/target/jerryscript/reeee/bin/jerry"
    rewriter = pre_process(js_code)
    # all_type_text()
    intervalend_vardicts = get_property(rewriter, engine_path)
    print("VariableNames:", VariableNames)
    exit()
    all_type = init2()
    for t in [65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81]:
        all_type.append(t)
    new_sample = ""
    count = 0
    change_p = 1.0
    while count < config.sample_size:
        count += 1  # 增加迭代计数
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
        ran = random.random()
        if ran < change_p:
            # 生成
            new_sample = generate(rewriter, intervalend_vardicts)
        elif change_p < ran < 1.0:
            # 更改
            new_sample = change(rewriter, all_type)
        else:
            # 插入
            new_sample = insert(rewriter, all_type)

        if new_sample not in config.new_samples:
            config.new_samples.append(new_sample)
            if len(config.new_samples) > config.sample_size:
                return len(config.new_samples)

    return len(config.new_samples)


if __name__ == '__main__':
    # 示例 JavaScript 代码
    js_code = js.js_code4
    js_code2 = js.js_code2
    length = parse(js_code.encode(), js_code2.encode())
    print("Total Samples: ", length)
    if length > 0:
        for i in range(0, length):
            with open("/home/qbtly/Desktop/aaaaa/b/" + str(i) + ".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
            # print(fuzz().decode())
    print("/home/qbtly/Desktop/aaaaa/b")
