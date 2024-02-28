import os
import random
import json
import config
import re
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

VariableNames = set()
obj_name8type = {}


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
    return rewriter


def pre_process(js_code):
    init()
    rewriter = Parse_ast(js_code)
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
    # print(result.stdout)
    # [
    # {"obj": "v1",
    # "objtype": "Array",
    # "methods": [],
    # "attrs": {"length": "number"}
    # },
    # ]
    return var_dict


def get_call_statements(methods, obj_type):
    # methods ==> var_dict["methods"]
    call_statements = []
    typed_methods = basic.methods[obj_type]
    all = list(typed_methods.items())
    b = list(typed_methods.keys())
    for a in all:
        args = ", ".join(a[1])
        call_statement = f"{a[0]}({args});"
        call_statements.append(call_statement)
    for method in methods:
        if method not in b:
            call_statements.append(f"{method}()")
            print(method)

    # 输出生成的调用语句
    # for statement in call_statements:
    #     print(statement)
    return call_statements


def get_property_call(var_dicts):
    # 新变量名
    new_var = "zdy"
    i = 1
    while new_var + str(i) in VariableNames:
        i += 1
    new_var = new_var + str(i)

    chosen_obj = random.choice(var_dicts)
    chosen_type = random.choice(["methods", "attrs"])
    if chosen_type == "methods":
        chosen_method = random.choice(chosen_obj["methods"])
        call_statement = f"\nlet {new_var} = {chosen_obj['obj']}.{chosen_method};\n"
    else:
        chosen_attr = random.choice(list(chosen_obj[chosen_type].keys()))
        call_statement = f"\nlet {new_var} = {chosen_obj['obj']}.{chosen_attr};\n"

    return chosen_obj['obj'], call_statement


def generate(rewriter, var_dicts):
    # 生成一条方法调用
    var_name, new_statement = get_property_call(var_dicts)

    change_p = 1.0
    for n in range(3):
        ran = random.random()
        if "tmp_num" in new_statement:
            # Number
            try:
                if ran < 0.8:
                    new_num = random.choice(obj_name8type['Number'])
                else:
                    new_num = generator.get_number()
            except:
                new_num = generator.get_number()
            # 替换
            new_statement = new_statement.replace("tmp_num", str(new_num))
            pass
        elif "tmp_array" in new_statement:
            # Array
            try:
                if ran < 0.8:
                    new_array = random.choice(obj_name8type['Array'])
                else:
                    new_array = generator.get_array()
            except:
                new_array = generator.get_array()
            # 替换
            new_statement = new_statement.replace("tmp_array", str(new_array))
        elif "tmp_str" in new_statement:
            # String
            try:
                if ran < 0.8:
                    new_str = random.choice(obj_name8type['String'])
                else:
                    new_str = generator.get_string()
            except:
                new_str = generator.get_string()
            # 替换
            new_statement = new_statement.replace("tmp_str", new_str)
        # 未完待续

    # 确定插入位置
    prefix = ""
    interval = (0, 0)  # 从头
    count = 0
    while (var_name not in prefix) and count < 100:
        interval = random.choice(config.intervals[1])
        prefix = rewriter.getText("", 0, interval[1])
        count += 1  # 增加迭代计数
        # 检查是否达到最大迭代次数
        if count >= 100:
            break

    # 插入
    rewriter.insertAfter(interval[1], new_statement)
    new_sample = rewriter.getDefaultText()
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


def parse(js_code, add_buf):
    rewriter = pre_process(js_code.encode())
    var_dicts = get_property(js_code, list(VariableNames))

    # 丰富var_dicts
    for var_dict in var_dicts:
        obj_type = var_dict['objtype']
        if obj_type not in list(obj_name8type.keys()):
            obj_name8type[obj_type] = []
        obj_name8type[obj_type].append(var_dict['obj'])

        var_dict['methods'] = get_call_statements(var_dict['methods'], obj_type)
        # var_dict["attrs"]
    print(var_dicts)

    all_type = init2()
    for t in [65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81]:
        all_type.append(t)
    new_sample = ""

    count = 0
    change_p = 0.8
    while count < config.sample_size:
        count += 1  # 增加迭代计数
        rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
        ran = random.random()
        if ran < change_p:
            # 生成
            new_sample = generate(rewriter, var_dicts)
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
    js_code = '''
    const v1 = ["Apple", "Banana"];
    const v3 = "A string primitive";
    '''
    js_code2 = '''
    const v2 = new Array(2);
    const v4 = new String("A String object");
    '''
    length = parse(js_code, js_code)
    # length = parse(js1.encode(), js2.encode())
    print(length)
    if length > 0:
        for i in range(0, length):
            with open("/home/qbtly/Desktop/aaaaa/b/" + str(i) + ".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
            # print(fuzz().decode())
    print("/home/qbtly/Desktop/aaaaa/b")

# [{
#   "obj": "v2",
#   "objtype": "Array",
#   "methods": [
#     "constructor",
#     "at",
#     "concat",
#     "copyWithin",
#     "fill",
#     "find",
#     "findIndex",
#     "findLast",
#     "findLastIndex",
#     "lastIndexOf",
#     "pop",
#     "push",
#     "reverse",
#     "shift",
#     "unshift",
#     "slice",
#     "sort",
#     "splice",
#     "includes",
#     "indexOf",
#     "join",
#     "keys",
#     "entries",
#     "values",
#     "forEach",
#     "filter",
#     "flat",
#     "flatMap",
#     "map",
#     "every",
#     "some",
#     "reduce",
#     "reduceRight",
#     "toReversed",
#     "toSorted",
#     "toSpliced",
#     "with",
#     "toLocaleString",
#     "toString"
#   ],
#   "attrs": {
#     "length": "number"
#   }
# },
# {
#   "obj": "v4",
#   "objtype": "String",
#   "methods": [
#     "constructor",
#     "anchor",
#     "at",
#     "big",
#     "blink",
#     "bold",
#     "charAt",
#     "charCodeAt",
#     "codePointAt",
#     "concat",
#     "endsWith",
#     "fontcolor",
#     "fontsize",
#     "fixed",
#     "includes",
#     "indexOf",
#     "isWellFormed",
#     "italics",
#     "lastIndexOf",
#     "link",
#     "localeCompare",
#     "match",
#     "matchAll",
#     "normalize",
#     "padEnd",
#     "padStart",
#     "repeat",
#     "replace",
#     "replaceAll",
#     "search",
#     "slice",
#     "small",
#     "split",
#     "strike",
#     "sub",
#     "substr",
#     "substring",
#     "sup",
#     "startsWith",
#     "toString",
#     "toWellFormed",
#     "trim",
#     "trimStart",
#     "trimLeft",
#     "trimEnd",
#     "trimRight",
#     "toLocaleLowerCase",
#     "toLocaleUpperCase",
#     "toLowerCase",
#     "toUpperCase",
#     "valueOf"
#   ],
#   "attrs": {
#     "length": "number"
#   }
# }]
