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

    def visitAssignmentExpression(self, ctx):
        left = ctx.singleExpression(0).getText()
        right = ctx.singleExpression(1).getText()
        VariableNames.add(left)
        # print(left, right)
        super().visitExpressionStatement(ctx)

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

        if interval[1] not in avaliableInterval:
            avaliableInterval.append(interval[1])
            IntervalEnd_VariableNames[interval[1]] = []
        super().visitStatement(ctx)


def init1():
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
    # for k in list(IntervalEnd_VariableNames.keys()):
    #     IntervalEnd_VariableNames[k] = list(VariableNames)
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
    init1()
    rewriter = Parse_ast1(buf)
    Parse_ast2(add_buf)
    return rewriter


def insertTamplate(rewriter, interval_ends):
    for interval_end in interval_ends:
        head = "\n////////////////////probe/////////////////////////\n"
        dr = f"   ;probe(variableNames,{interval_end});\n"
        # tmp = head + dr + head
        tmp = dr
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
    # with open("arr1.js", "r", encoding='utf-8') as js_file1:
    #     # with open("arr1.js", "r", encoding='utf-8') as js_file1:
    #     js1 = js_file1.read()
    #     js_file1.close()
    js0 = js.arr1
    js2 = js.arr2

    avaliableVar = "\n   let variableNames = " + str(list(VariableNames)) + ";\n"

    # with open(f"output/{engine_name}/output.js", "w") as js_file:
    try:
        with open(f"custom_mutators/examples/output/{engine_name}/output.js", "w") as js_file:
            js_file.write(js0)
            js_file.write(js2)
            js_file.write("\n\n")
            js_file.write(avaliableVar)
            js_file.write(probed_sample)
    except Exception as e:
        print(f"Error occurred: {e}")

    # 执行 JavaScript Samples
    cmd = []
    for item in engine_paths:
        if item:
            cmd.append(item)
    cmd.append(f"custom_mutators/examples/output/{engine_name}/output.js")
    # cmd.append(f"output/{engine_name}/output.js")

    # cmd = ["/home/qbtly/Desktop/target/V8/v8/0124/d8", "--allow-natives-syntax", "--expose-gc", f"output/output{index}.js"]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    # print(cmd, result.stdout)

    # 检查命令是否执行成功
    if result.returncode == 0:
        print("Command executed successfully.")
        # print("Output:", result.stdout)
    else:
        print("Command failed with return code", result.returncode)
        print("Error output:", result.stderr)

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

        # 丰富var_dicts
        for var_dict in dynamic_results:
            obj_type = var_dict['type']
            if obj_type not in list(obj_name8type.keys()):
                obj_name8type[obj_type] = []
            obj_name8type[obj_type].append(var_dict['obj'])
            var_dict['methods'] = get_call_statements(var_dict['methods'], obj_type)
            # var_dict["attrs"]
        IntervalEnd_Vardicts[interval_end] = dynamic_results

    # print("IntervalEnd_Vardicts: ", IntervalEnd_Vardicts, VariableNames)
    # print("IntervalEnd_VariableNames: ", IntervalEnd_VariableNames)
    return IntervalEnd_Vardicts


def get_call_statements(methods, obj_type):
    # methods ==> var_dict["methods"]
    call_statements = []
    if obj_type in list(basic.methods.keys()):
        typed_methods = basic.methods[obj_type]
        items = list(typed_methods.items())
        b = list(typed_methods.keys())
        for a in items:
            args = ", ".join(a[1])
            call_statement = f"{a[0]}({args})"
            call_statements.append(call_statement)
        for method in methods:
            if method not in b:
                call_statements.append(f"{method}()")
                # print(obj_type, method)
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
    # chosen_type = random.choice(["methods"])
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
            call_statement += f"\n{var_name}.{chosen_attr} = {generator.get_random_value(obj[chosen_type][chosen_attr])};\n"
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
            # print(interval_end,obj)
            # 生成一条方法调用
            new_statement = get_property_call(obj)
            # 调整
            change_p = 0.5
            for n in range(3):
                # random.shuffle(IntervalEnd_VariableNames[interval_end])
                ran = random.random()
                if "tmp_number" in new_statement:
                    # Number
                    try:
                        if ran < change_p:
                            # new_arg = random.choice(obj_name8type['Number'])
                            new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_random_value('number')
                    except:
                        new_arg = generator.get_random_value('number')
                    # 替换
                    new_statement = new_statement.replace("tmp_number", str(new_arg), 1)
                    pass
                elif "tmp_array" in new_statement:
                    # Array
                    try:
                        if ran < change_p:
                            # new_array = random.choice(obj_name8type['Array'])
                            new_array = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_array = generator.get_random_value('array')
                    except:
                        new_array = generator.get_random_value('array')
                    # 替换
                    new_statement = new_statement.replace("tmp_array", str(new_array), 1)
                elif "tmp_string" in new_statement:
                    # String
                    try:
                        if ran < change_p:
                            new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_random_value('string')
                    except:
                        new_arg = generator.get_random_value('string')
                    # 替换
                    new_statement = new_statement.replace("tmp_string", str(new_arg), 1)
                elif "tmp_object" in new_statement:
                    # Object
                    try:
                        if ran < change_p:
                            new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_random_value('object')
                    except:
                        new_arg = generator.get_random_value('object')
                    # 替换
                    new_statement = new_statement.replace("tmp_object", str(new_arg), 1)
                elif "tmp_function" in new_statement:
                    # Function
                    try:
                        if ran < change_p:
                            new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                        else:
                            new_arg = generator.get_function2(1, IntervalEnd_VariableNames[interval_end])
                    except:
                        new_arg = generator.get_function2(1, IntervalEnd_VariableNames[interval_end])
                    # 替换
                    new_statement = new_statement.replace("tmp_function", str(new_arg), 1)
                elif "tmp_any" in new_statement:
                    try:
                        new_arg = random.choice(IntervalEnd_VariableNames[interval_end])
                    except:
                        new_arg = generator.get_random_value('any')
                    # 替换
                    new_statement = new_statement.replace("tmp_any", str(new_arg), 1)
                # 未完待续
                # print(new_statement)
            # 插入
            rewriter.insertAfter(interval_end, new_statement)
            # print(new_statement)
    new_sample = rewriter.getDefaultText()

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
    # print(new_sample)
    return new_sample


@SetTimeoutDecorator(timeout=30)
def jungle(buf, add_buf):
    is_done1, is_timeout1, erro_message1, results1 = checkParsetime(buf)
    is_done2, is_timeout2, erro_message2, results2 = checkParsetime(add_buf)
    if is_timeout1 is True or is_timeout2 is True:
        return len(config.new_samples)

    # 获取输出路径
    engine_path = str(os.environ.get('AFL_ENGINE'))
    # print(engine_path)
    # engine_path = "/jsc/fuzz/JSCOnly/Release/bin/jsc"
    # engine_path = "/gecko-dev/js/src/0402/dist/bin/js"
    # engine_path = "/home/qbtly/Desktop/target/jerryscript/reeee/bin/jerry"
    rewriter = pre_process(buf, add_buf)
    intervalend_vardicts = Dynamic_Reflection(rewriter, engine_path)
    # print('=======================')
    all_type = init2()
    for t in [65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81]:
        all_type.append(t)
    new_sample = ""
    count = 0
    change_p = 0.8
    ran = 0
    while count < config.sample_size:
        count += 1  # 增加迭代计数
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")

        if count > 1000:
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


def init(seed):
    """
    Called once when AFLFuzz starts up. Used to seed our RNG.

    @type seed: int
    @param seed: A 32-bit random value
    """
    random.seed(seed)


def deinit():
    pass


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


def fuzz_count(buf, add_buf):
    jungle(buf, add_buf)
    return len(config.new_samples)


if __name__ == '__main__':
    # 示例 JavaScript 代码
    js_code = js.js_code4
    js_code2 = js.js_code2
    length = fuzz_count(js_code.encode(), js_code.encode())
    print("Total Samples: ", length)
    # if length > 0:
    #     for i in range(0, length):
    #         with open("/home/qbtly/Desktop/aaaaa/b/" + str(i) + ".js", "w") as f:
    #             f.write(fuzz().decode())
    #             f.close()
    #         # print(fuzz().decode())
    # print("/home/qbtly/Desktop/aaaaa/b")
