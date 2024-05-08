import datetime
import os
import random
import json
import shutil
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
import js_test
from pathlib import Path

IntervalEnd_Vardicts = {}
VariableNames = set()
obj_name8type = {}
IntervalEnd_VariableNames = {}  # 用于存储变量名和它们所在的行号
avaliableInterval = []
FunctionVarNames = {}

# class Scope:
#     def __init__(self, name='global', parent=None):
#         self.name = name
#         self.parent = parent
#         self.variables = {}


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
        # interval = ctx.getSourceInterval()
        # VariableNames.add(var_name)
        if var_name not in config.builtins:
            VariableNames.add(var_name)
        #     if var_name not in list(self.currentScope.variables.keys()):
        #         self.currentScope.variables[var_name] = interval[1]
        super().visitStatement(ctx)

    def visitStatement(self, ctx):
        interval = ctx.getSourceInterval()
        for b in ctx.getChildren():
            s_type = type(b).__name__
            # if s_type == 'BlockContext':
            # print(s_type,'+++++++++++++',b.getText())
            if s_type != "BlockContext":
                if interval[1] not in avaliableInterval:
                    avaliableInterval.append(interval[1])
                    IntervalEnd_VariableNames[interval[1]] = []
        super().visitStatement(ctx)

    def visitArgumentsExpression(self, ctx):
        FunctionVarNames[ctx.getChild(0).getText()] = ctx.getText()
        super().visitStatement(ctx)

def init():
    IntervalEnd_Vardicts.clear()
    VariableNames.clear()
    IntervalEnd_VariableNames.clear()
    avaliableInterval.clear()
    FunctionVarNames.clear()
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
    all_type2 = []
    for type in range(5, 86):
        if len(config.texts[type]) > 0:
            all_type2.append(type)
    return all_type2


def init3():
    all_type3 = []
    for type in range(0, 86):
        if len(config.texts[type]) > 0:
            all_type3.append(type)
    return all_type3


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
    for func_va_rname in list(FunctionVarNames.keys()):
        if not func_va_rname.startswith('('):
            VariableNames.add(FunctionVarNames[func_va_rname])
            func_va_rname_split = func_va_rname.split('.')
            for fc_name in list(VariableNames):
                if fc_name in func_va_rname_split:
                    # print(fc_name, func_va_rname)
                    VariableNames.remove(FunctionVarNames[func_va_rname])
                    break
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
    init()
    rewriter = Parse_ast1(buf)
    Parse_ast2(add_buf)
    return rewriter


def insertTamplate(rewriter, interval_ends):
    for interval_end in interval_ends:
        dr1 = f"            ;(function() {{let point = {interval_end};"
        dr = js.arr3
        tmp = js.head + dr1 + dr + js.head
        # 插入
        rewriter.insertAfter(interval_end, tmp)
    probed_sample = rewriter.getDefaultText()
    for interval_end in interval_ends:
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
    return probed_sample


def dynamic_reflection(rewriter, engine_path):
    engine_paths = engine_path.split(' ')
    engine_name = engine_paths[0].split('/')[-1]

    IntervalEnd_VariableNames[-1] = []
    interval_ends = list(IntervalEnd_VariableNames.keys())
    probed_sample = insertTamplate(rewriter, interval_ends)

    js0 = js.arr1
    js2 = js.arr2

    avaliableVar = "\n   let variableNames = " + str(list(VariableNames)) + ";\n"

    # with open(f"output/{engine_name}/output.js", "w") as js_file:
    try:
        with open(f"output/{engine_name}/output.js", "w") as js_file:
        # with open(f"pymodules/output/{engine_name}/output.js", "w") as js_file:
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
    cmd.append(f"output/{engine_name}/output.js")
    # cmd.append(f"pymodules/output/{engine_name}/output.js")

    result_text = ""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        result_text = result.stdout
    except subprocess.TimeoutExpired as e:
        print("The command timed out. Consider increasing the timeout or checking the command.")
        # print(e.stdout)
        if e.stdout:
            result_text = e.stdout.decode('utf-8')
        else:
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    
    # print(result_text)

    # 检查命令是否执行成功
    # if result.returncode == 0:
    #     print("Command executed successfully.")
    #     # print("Output:", result.stdout)
    # else:
    #     print("Error output:", result.stderr)

    pattern0 = r'qbtly_start&(.*?)&qbtly_end'
    outputs = tools.extract(result_text, pattern0)
    for output in outputs:
        # print(output)
        pattern2 = r'qbtly_point_start(.*?)qbtly_point_end'
        interval_end = int(tools.extract0(output, pattern2, 0))

        pattern1 = r'qbtly_aviliable(.*?)qbtly_var'
        js_list = str(tools.extract0(output, pattern1, [])).strip('[]')
        js_list = js_list.split(',') if js_list else []
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
            var_dict['methods'] = generator.get_call_statements(var_dict['methods'], obj_type)
            # var_dict["attrs"]
        IntervalEnd_Vardicts[interval_end] = dynamic_results

    # print("IntervalEnd_Vardicts: ", IntervalEnd_Vardicts, VariableNames)
    # print("IntervalEnd_VariableNames: ", IntervalEnd_VariableNames)
    return IntervalEnd_Vardicts


def generate(rewriter, intervalend_vardicts, engine_name):
    interval_ends = list(intervalend_vardicts.keys())
    if len(interval_ends) > 0:
        # 确定插入位置
        interval_end = random.choice(interval_ends)
        # 新变量名
        new_var = generator.get_newname('zdy', VariableNames)
        # 确定可用变量
        objs = intervalend_vardicts[interval_end]
        # print(objs)
        if len(objs) > 0:
            obj = random.choice(objs)  # obj-->dict
            new_statement = generator.get_new_statement_obj(engine_name, new_var, obj)
        else:
            new_statement = generator.get_new_statement(engine_name, new_var)
        if "BigFloat.parseFloat()" in new_statement:
            new_sample = rewriter.getDefaultText()
            return new_sample
        new_statement = generator.adjust(new_statement, IntervalEnd_VariableNames, interval_end)
        rewriter.insertAfter(interval_end, new_statement)
    new_sample = rewriter.getDefaultText()
    return new_sample


def insert(rewriter, all_type):
    pass


def change(rewriter, all_type2, all_type3):
    type2 = random.choice(all_type2)
    type3 = random.choice(all_type3)
    if len(config.intervals[type2]) > 0 and len(config.texts[type3]) > 0:
        interval = random.choice(config.intervals[type2])
        text = random.choice(config.texts[type3])
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

    # engine_path = "/home/qbtly/Desktop/target/WebKit/0422_debug/JSCOnly/Debug/bin/jsc"
    engine_path = "/home/qbtly/Desktop/target/gecko-dev/js/src/gcov/dist/bin/js"
    # engine_path = "/home/qbtly/Desktop/target/jerryscript/reeee/bin/jerry"
    # engine_path = "/home/qbtly/Desktop/target/V8/v8/0414_debug/d8 --allow-natives-syntax --expose-gc"

    # 获取输出路径
    # engine_path = str(os.environ.get('AFL_ENGINE'))
    engine_paths = engine_path.split(' ')
    engine_name = engine_paths[0].split('/')[-1]
    # print(engine_path)

    rewriter = pre_process(buf, add_buf)
    intervalend_vardicts = dynamic_reflection(rewriter, engine_path)
    print('=======================')
    all_type2 = init2()
    all_type3 = init3()
    for t in [65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81, 81, 81]:
        all_type2.append(t)

    new_sample = ""
    count = 0
    g_count = 0
    c_count = 0
    g_valid_count = 0
    c_valid_count = 0
    change_p = 0.6
    ran = 0
    
    while count < config.sample_size:
        # print("count:", count)
        # print("  g_count:", g_count)
        # print("  c_count:", c_count)
        count += 1  # 增加迭代计数
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")

        if not (intervalend_vardicts and count <= 500):
            ran = random.random()

        if ran < change_p and intervalend_vardicts:
            # 生成
            new_sample = generate(rewriter, intervalend_vardicts, engine_name)
            g_count += 1
            if new_sample not in config.new_samples:
                g_valid_count += 1
        else:
            # 更改
            new_sample = change(rewriter, all_type2, all_type3)
            c_count += 1
            if new_sample not in config.new_samples:
                c_valid_count += 1

        if new_sample not in config.new_samples:
            config.new_samples.append(new_sample)
            if len(config.new_samples) > config.sample_size:
                return len(config.new_samples)
            
    print("generate:", g_valid_count, "/", g_count)
    print("crossover:", c_valid_count, "/", c_count)
    return len(config.new_samples)


# def init(seed):
#     """
#     Called once when AFLFuzz starts up. Used to seed our RNG.

#     @type seed: int
#     @param seed: A 32-bit random value
#     """
#     random.seed(seed)


def deinit():
    pass


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


def parse(buf, add_buf):
    is_done2, is_timeout2, erro_message2, results2 = jungle(buf, add_buf)
    return len(config.new_samples)


if __name__ == '__main__':
    # 示例 JavaScript 代码
    # js_code = js_test.js_code3
    # js_code2 = js_test.js_code2
    # length = parse(js_code.encode(), js_code.encode())
    # print("Total Samples: ", length)
    # path = '/home/qbtly/Desktop/aaaaa/b/'
    # shutil.rmtree(path)
    # os.mkdir(path)
    # if length > 0:
    #     for i in range(0, length):
    #         with open(path + str(i) + ".js", "w") as f:
    #             f.write(fuzz().decode())
    #             f.close()
            # print(fuzz().decode())
    # print("/home/qbtly/Desktop/aaaaa/b")

    # poc_dir = "/home/qbtly/Desktop/PatchFuzz/js/js_poc/spidermonkey"
    poc_dir = "/home/qbtly/Desktop/PatchFuzz/js/seeds/jsc/queue"

    directory_path = Path(poc_dir)
    i = 1
    
    for file in directory_path.rglob('*'):
        if i < 0:
            i = i + 1
            continue
        if file.is_file():
            # bad_mark = bad
            try:
                with open(file, 'r') as f:
                    print('-----------------------------------------------------')
                    print(i, file)
                    js_content = f.read()
                    length = parse(js_content.encode(), js_content.encode())

                    print("Total Samples: ", length)
                    path = '/home/qbtly/Desktop/aaaaa/c/'
                    shutil.rmtree(path)
                    os.mkdir(path)
                    if length > 0:
                        for k in range(0, length):
                            with open(path + str(k) + ".js", "w") as f:
                                f.write(fuzz().decode())
                                f.close()
                    # print("--------------origin--------------")
                    # print(js_content)
                    # print("----------------------------------")
                    # tools.all_type_text()
                    # if bad_mark != bad:
                    #     print(i, file)
                    #     # print("--------------origin--------------")
                    #     # print(js_content)
                    #     # print("----------------------------------")
                    #     print(bad, '/', i)
    
            except Exception as e:
                print(i, file, e)
            # input('continue?')
            i = i + 1
