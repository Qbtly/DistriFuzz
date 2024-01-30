import os
import random
import json
import config
import re
import config
from call_function_with_timeout import SetTimeoutDecorator
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
VariableNames = set()


class MyVisitor(JSV):
    def __init__(self):
        super().__init__()
        self.isGlobalScope = True  # 标记当前是否在全局作用域

    # 访问函数声明
    def visitFunctionDeclaration(self, ctx):
        # 在访问函数时，标记不再处于全局作用域
        self.isGlobalScope = False
        self.visitChildren(ctx)  # 继续遍历子节点
        self.isGlobalScope = True  # 恢复全局作用域标记

    # 访问变量声明
    def visitVariableDeclaration(self, ctx):
        if self.isGlobalScope:
            # 如果当前处于全局作用域，则处理变量声明
            var_name = ctx.assignable().getText()
            VariableNames.add(var_name)
        self.visitChildren(ctx)  # 继续遍历子节点


def all_type_text():
    for type in range(0, 86):
        print(type, end=': ')
        for text in config.texts[type]:
            print(text, end="  |  ")
        print('\n')


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

def Parse(js_code):
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
    return rewriter


def pre_process(js_code):
    init()
    rewriter = Parse(js_code)
    return rewriter


def get_property(js_code, js_var):
    js_id = "\nlet variableNames = " + str(js_var)  # 被调用过的
    js_type = r'''
variableNames.forEach(varName => {
try{
    let varInstance = eval(varName);
    let typeInfo = varIntrospect(varName, varInstance);
    output.push(JSON.stringify(typeInfo, setReplacer, 2));
}catch(err){
    console.log('error');
    }
});
console.log("[" + output.join(",\n") + "]");
    '''
    # all_type_text()
    with open("arr1.js", "r") as js_file1:
        js1 = js_file1.read()
    # 将 JavaScript 代码保存到一个 JavaScript 文件
    with open("output.js", "w") as js_file:
        js_file.write(js1)
        js_file.write(js_id)
        js_file.write(js_code)
        js_file.write(js_type)
    # 执行 JavaScript 文件
    cmd = ["/home/qbtly/Desktop/target/V8/v8/0124/d8", "output.js"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    var_dict = json.loads(result.stdout)
    print(result.stdout)
    # [
    # {"obj": "v1",
    # "objtype": "Array",
    # "methods": [],
    # "attrs": {"length": "number"}
    # },
    # ]
    return var_dict


def get_call_statements(array_methods):
    call_statements = []
    for method in array_methods:
        if method in basic.array_methods.keys():
            chosen_variable = random.choice(variables)
            chosen_type = random.choice(["methods", "attrs"])
            chosen_method_or_attr = random.choice(list(chosen_variable[chosen_type].items()))

            # 构造调用语句
            if chosen_type == "methods":
                args_string = ", ".join(chosen_method_or_attr[1])
                js_call_snippet = f"{chosen_variable['name']}.{chosen_method_or_attr[0]}({args_string});"
            else:
                js_call_snippet = f"{chosen_variable['name']}.{chosen_method_or_attr[0]};"

        #     # 这些方法通常需要一个回调函数作为参数
        #     call_statements.append(f"{method}(element => element > 0)")
        # elif method in ["push", "unshift"]:
        #     # push 和 unshift 方法通常需要添加元素作为参数
        #     call_statements.append(f"{method}(newElement)")
        # elif method in ["indexOf", "lastIndexOf", "includes"]:
        #     # 这些方法通常需要一个要搜索的元素作为参数
        #     call_statements.append(f"{method}(searchElement)")
        # elif method in ["slice", "splice"]:
        #     # slice 和 splice 方法通常需要索引作为参数
        #     call_statements.append(f"{method}(start, end)")
        # elif method == "join":
        #     # join 方法通常需要一个字符串作为参数
        #     call_statements.append(f"{method}(', ')")
        # elif method == "sort":
        #     # sort 方法可以带有一个比较函数作为参数
        #     call_statements.append(f"{method}((a, b) => a - b)")
        else:
            # 对于其他方法，我们暂时不添加特定参数
            call_statements.append(f"{method}()")
    # 输出生成的调用语句
    # for statement in call_statements:
    #     print(statement)
    return call_statements

def get_property_call(var_dicts):
    # 新变量名
    new_var = "var"
    i = 1
    while new_var + str(i) in VariableNames:
        i += 1
    new_var = new_var + str(i)

    chosen_obj = random.choice(var_dicts)

    chosen_feature_type = random.choice(["methods", "attrs"])

    if chosen_feature_type == "methods":
        call_statement = random.choice(chosen_obj["methods"])
        call_statement = f"\nlet {new_var} = {chosen_obj['obj']}.{call_statement};\n"
    else:
        chosen_attr = random.choice(list(chosen_obj[chosen_feature_type].keys()))
        call_statement = f"\nlet {new_var} = {chosen_obj['obj']}.{chosen_attr};\n"

    return chosen_obj['obj'], call_statement


def mutate(rewriter, var_dict):
    # 生成一条方法调用

    var_name, new_statement = get_property_call(var_dict)

    #位置
    prefix = ""
    interval = (0, 0)
    count = 0
    while (var_name not in prefix) and count < 100:
        interval = random.choice(config.intervals[1])
        prefix = new_sample = rewriter.getText("", 0, interval[1])
        count += 1  # 增加迭代计数
        # 检查是否达到最大迭代次数
        if count >= 100:
            break

    # 插入
    rewriter.insertAfter(interval[1], new_statement)
    new_sample = rewriter.getDefaultText()
    return new_sample


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


def parse(js_code, add_buf):
    rewriter = pre_process(js_code.encode())
    var_dicts = get_property(js_code, list(VariableNames))
    exit(0)
    for var_dict in var_dicts:
        var_dict["methods"] = get_call_statements(var_dict["methods"])
        # var_dict["attrs"]

    all_type = init2()
    # for t in [65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81]:
    #     all_type.append(t)
    count = 0
    change_p = 0.9
    new_sample = ""

    while count < config.sample_size:
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
        ran = random.random()
        if ran < change_p:
            # 生成
            new_sample = mutate(rewriter, var_dicts)

        elif change_p < ran < 1.0:
            pass
        else:
            pass

        if new_sample not in config.new_samples:
            config.new_samples.append(new_sample)
            if len(config.new_samples) > config.sample_size:
                return len(config.new_samples)
        count += 1  # 增加迭代计数
        # print('===========================')
        # new_sample = rewriter.getDefaultText()
        # print(new_sample)
        #
        # print('88888888888888888888888888')
        # now = rewriter.getText("", 0, 10000)
        # print(now)

    # while count < config.sample_size:
    #     ran = random.random()
    #     type = random.choice(all_type)
    #     if len(config.intervals[type]) > 0 and len(config.texts[type]) > 0:
    #         count += 1
    #         if ran < change_p:
    #             #替换
    #             interval = random.choice(config.intervals[type])
    #             text = random.choice(config.texts[type])
    #             change(text, interval, rewriter)
    #         elif change_p < ran < 1.0:
    #             # 删除
    #             interval = random.choice(config.intervals[type])
    #             text = ''
    #             change(text, interval, rewriter)
    #         else:
    #             # 插入
    #             if len(config.intervals[1]) > 0:
    #                 interval = random.choice(config.intervals[1])
    #                 text = rewriter.getText("", interval[0], interval[1]) + random.choice(kkk.statement)
    #                 change(text, interval, rewriter)

    return len(config.new_samples)


if __name__ == '__main__':
    # 示例 JavaScript 代码
    js_code = '''
    const v1 = ["Apple", "Banana"];
    const v3 = "A string primitive";
    '''
    js_code2 = '''
    
    const v2 = new Array(2);
    const v4 = new String("A String object");
    '''
    length = parse(js_code2, js_code2)
    # length = parse(js1.encode(), js2.encode())
    print(length)
    if length > 0:
        for i in range(0, length):
            with open("/home/qbtly/Desktop/aaaaa/b" + str(i) + ".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
            # print(fuzz().decode())
            # print("=============================")
