import os
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
from antlr4 import *
import json
import subprocess

# 示例 JavaScript 代码
js_code = '''
function opt(a, b) {
    b[0] = 0;
    a.length;
    for (let i = 0; i < 1; i++)
        a[0] = 0;

    b[0] = 9.431092e-317;
}

let arr1 = new Array(1);
arr1[0] = 'a';
opt(arr1, [0]);

let arr2 = [0.1];
opt(arr2, arr2);
let xxx = 0;
let bbb = {
    c:1
};

opt(arr2, arr2);
arr2[0].x;
    '''

def all_type_text():
    for type in range(0, 86):
        print(type, end=': ')
        for text in config.texts[type]:
            print(text, end="  |  ")
        print('\n')

@SetTimeoutDecorator(timeout=10)
def Parse(js_sample):
    input_stream = InputStream(js_sample)
    lexer = JSL(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSP(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())
    tree = parser.program()
    return tree
def init():
    config.ids = []
    config.intervals = {}
    for type in range(0, 200):
        config.intervals[type] = []
    config.texts = {}
    for type in range(0, 200):
        config.texts[type] = []
    config.new_samples = []

def run(js_code, js_var):
    js_id = "let variableNames = " + str(js_var)  # 被调用过的
    js_type = '''
    variableNames.forEach(varName => {
    try{
    let varInstance = eval(varName);
    let typeInfo = varIntrospect(varName, varInstance);
    let fileName = `./output/${varName}.json`;  // 修改文件名以包含变量名
    fs.writeFileSync(fileName, JSON.stringify(typeInfo, replacerFunction, 2));
        console.log(typeInfo);
    }catch(err){
            null;}
    });
    '''
    # all_type_text()
    with open("arr.js", "r") as js_file1:
        js1 = js_file1.read()
    # 将 JavaScript 代码保存到一个 JavaScript 文件
    with open("output.js", "w") as js_file:
        js_file.write(js1)
        js_file.write(js_id)
        js_file.write(js_code)
        js_file.write(js_type)
    # 执行 JavaScript 文件
    subprocess.run(["node", "output.js"])


if __name__ == '__main__':
# 使用 ANTLR 解析 JavaScript 代码
    init()
    js_sample = js_code
    input_stream = InputStream(js_sample)
    lexer = JSL(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSP(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())
    tree = parser.program()

    VariableNames = set()
# 访问者类
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

    # 创建并使用访问者
    # visitor = JSV()
    visitor = MyVisitor()
    visitor.visit(tree)
    # all_type_text()
    # print(VariableNames)
    # os.mkdir('./output')
    # run(js_code, list(VariableNames))

    #let propertiesOnPrototypeToOverwrite = ["valueOf", "toString", "constructor"]



