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
import vulpattern

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
        # with open(f"output/{engine_name}/output.js", "w") as js_file:
        with open(f"pymodules/output/{engine_name}/output.js", "w") as js_file:
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
    # cmd.append(f"output/{engine_name}/output.js")
    cmd.append(f"pymodules/output/{engine_name}/output.js")

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

    pattern0 = r'qbtly_start&(.*?)&qbtly_end'
    outputs = tools.extract(result_text, pattern0)
    for output in outputs:
        # print(output)
        pattern2 = r'qbtly_point_start(.*?)qbtly_point_end'
        interval_end = int(tools.extract0(output, pattern2, 0))

        pattern1 = r'qbtly_aviliable(.*?)qbtly_var'
        js_list = str(tools.extract0(output, pattern1, []))
        js_list = js_list.split(" <qbav> ") if js_list else []
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
        if "BigFloat.parseFloat" in new_statement or "std.setenv" in new_statement or "os.chdir" in new_statement or "d8.quit" in new_statement or "enableShellAllocationMetadataBuilder" in new_statement or "recomputeWrappers" in new_statement:
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
    if random.random() > 0.2:
        type3 = random.choice(all_type3)
    else:
        type3 = type2
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

    # engine_path = "/jsc/fuzz/JSCOnly/Release/bin/jsc"
    # engine_path = "/home/qbtly/Desktop/target/gecko-dev/js/src/fuzz/dist/bin/js"
    # engine_path = "/home/qbtly/Desktop/target/jerryscript/reeee/bin/jerry"
    # 获取输出路径
    engine_path = str(os.environ.get('AFL_ENGINE'))
    engine_paths = engine_path.split(' ')
    engine_name = engine_paths[0].split('/')[-1]
    # print(engine_path)

    rewriter = pre_process(buf, add_buf)
    intervalend_vardicts = dynamic_reflection(rewriter, engine_path)
    # print('=======================')
    all_type2 = init2()
    all_type3 = init3()
    for t in [2, 65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81, 81, 81]:
        all_type2.append(t)

    new_sample = ""
    count = 0
    change_p = 0.6
    ran = 0
    while count < config.sample_size:
        count += 1  # 增加迭代计数
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")

        if not (intervalend_vardicts and count <= 500):
            ran = random.random()

        if ran < change_p and intervalend_vardicts:
            # 生成
            new_sample = generate(rewriter, intervalend_vardicts, engine_name)
        else:
            # 更改
            new_sample = change(rewriter, all_type2, all_type3)
        # else:
        #     # 插入
        #     new_sample = insert(rewriter, all_type)

        if new_sample not in config.new_samples:
            config.new_samples.append(new_sample)
            if len(config.new_samples) > config.sample_size:
                return len(config.new_samples)
    return len(config.new_samples)


api_key = ''
url = ""
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

@SetTimeoutDecorator(timeout=30)
def ai_keyvars(origin_sample, patterns):
    data = {
        "messages": [
            {
             "role": "system",
             "content": '''
                你的任务是对 JavaScript 引擎测试样本进行关键变量提取。
                请先为该样本选取一个合适的漏洞模式（从下面可选的漏洞模式中选择一个最适合的模式），
                然后从样本中提取出符合所选漏洞模式的关键变量,并为每个关键变量匹配最可能导致的漏洞根因(RootCause)。
                最后请以 JSON 数组形式输出，每个元素是一个对象，格式如下：
                {{
                    "var": "变量名称",
                    "rootc": "漏洞根因代号（例如 A, B, C, D, E, F)"
                }}

                可选漏洞模式：{}
                RootCause 定义：
                    A: Incorrect Control Flow Handling
                    B: Incorrect Type Handling
                    C: Incorrect Data Structure Handling
                    D: Incorrect Optimization Algorithm
                    E: Incorrect Resource Management

                请仅输出 JSON 数组，不要输出任何其他内容。
             '''.format(patterns)
            },
            {
            "role": "user",
            "content": '''
                样本：{},
                请根据上面的要求,先选取一个合适的漏洞模式,再从样本中提取出符合该模式的关键变量(不超过3个).
                为每个关键变量匹配其可能导致的漏洞根因，最后以 JSON 数组形式输出结果。
            '''.format(origin_sample)
        }
        ],
        # "max_tokens": 100,
        "temperature": 0.2
    }
    # print(data["messages"][0]["content"])
    # print(data["messages"][1]["content"])
    # return []
    try:
        time.sleep(5)
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        keyvars = ast.literal_eval(content)
        if isinstance(keyvars, list) and all(isinstance(kv, dict) and "var" in kv and "rootc" in kv for kv in keyvars):
            return keyvars
        else:
            return []
    except Exception as e:
        print("Error during key variable extraction:", e)
        return []

@SetTimeoutDecorator(timeout=30)
def ai_mutate(origin_sample, keyvar, patterns):
    data = {
        "messages": [
            {
                "role": "system",
                "content": '''
                你的任务是对 JavaScript 引擎测试样本进行代码变异。
                你将接收一个原始样本，以及一个关键变量和若干漏洞模式.
                请围绕该关键变量，结合最合适的几个漏洞模式进行结构化变异，以生成用于模糊测试的有效样本。
                '''
            },
            {
                "role": "user",
                "content": '''
                    样本代码：
                    {}

                    关键变量：{}

                    可选漏洞模式：
                    {}

                    生成10个变异样本,每个变异样本需保持原样本逻辑结构的可运行性和测试语义,并尽可能引入与关键变量及漏洞模式相关的变化。
                    注意：不要附加任何注释或说明,不使用console.log。
                    注意：每个变异样本都使用```javascript_start和```javascript_end包裹
                            '''.format(origin_sample, keyvar, patterns)
            }
        ],
        # "max_tokens": 100,
        "temperature": 0.7,
    }
    # print(data["messages"][0]["content"])
    # print(data["messages"][1]["content"])
    try:
        time.sleep(5)
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        mutated_samples = extract(content)
        if isinstance(mutated_samples, list):
            return mutated_samples
        else:
            return []
        return new_samples
    except Exception as e:
        print("AI变异出错：", e)
        return []

def AImutator(buf, add_buf):
    new_samples = []
    selected_patterns = tools.pick_random_pattern(vulpattern.vul_patterns)
    try:
        is_done, is_timeout, erro_message, vars_list = ai_keyvars(buf.decode(), selected_patterns)
    except Exception as e:
        print("An error occurred:", e)
        return len(config.new_samples)
    if not vars_list:
        print("No key variables extracted.")
        return len(config.new_samples)
    

    for var_entry in vars_list:
        var_name = var_entry.get("var")
        rootc_code = var_entry.get("rootc")
        if not var_name or not rootc_code:
            print("Invalid var_entry:", var_entry)
            continue
        # 根据根因类别获取相应的漏洞模式
        matching_patterns = []
        for root in vulpattern.vul_patterns:
            if root.get("RootCause") == vulpattern.RootCause[rootc_code]:
                matching_patterns = root.get("patterns", [])
                break

        if not matching_patterns:
            print(f"No patterns found for root cause {vulpattern.RootCause[rootc_code]}")
            continue
        try:
            is_done, is_timeout, error_message, samples_text = ai_mutate(
                buf.decode(), var_name, matching_patterns
            )
            if is_timeout:
                print("[Timeout]")
                print(erro_message)
            new_samples = tools.extract_sample(samples_text)
        except Exception as e:
            print("An error occurred:", e)
        for new_sample in new_samples:
            if new_sample not in config.new_samples:
                config.new_samples.append(new_sample)
                if len(config.new_samples) > config.sample_size:
                    return len(config.new_samples)
    # print(len(config.new_samples))
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


def parse(buf, add_buf, cur_id):
    print('============================', cur_id, '============================')
    if cur_id % 50 != 0:
        jungle(buf, add_buf)
    else:
        AImutator(buf, add_buf)
    return len(config.new_samples)


if __name__ == '__main__':
    # 示例 JavaScript 代码
    js_code = js_test.js_code3
    js_code2 = js_test.js_code2
    length = parse(js_code.encode(), js_code.encode())
    print("Total Samples: ", length)
    path = '/home/qbtly/Desktop/aaaaa/b/'
    shutil.rmtree(path)
    os.mkdir(path)
    if length > 0:
        for i in range(0, length):
            with open(path + str(i) + ".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
            # print(fuzz().decode())
    # print("/home/qbtly/Desktop/aaaaa/b")
