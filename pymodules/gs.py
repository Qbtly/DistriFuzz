#!/usr/bin/env python
# encoding: utf-8
"""
Example Python Module for AFLFuzz

@author:     Christian Holler (:decoder)

@license:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

@contact:    choller@mozilla.com
"""

import requests
import vulmode
import time
import re
import config
import ast
import random
from call_function_with_timeout import SetTimeoutDecorator
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.error.ErrorListener import ConsoleErrorListener
from JavaScriptLexer import JavaScriptLexer as JSL
from JavaScriptParser import JavaScriptParser as JSP
from JavaScriptParserVisitor import JavaScriptParserVisitor as JSV
from JavaScriptParserVisitor2 import JavaScriptParserVisitor2 as JSV2
import tools,shutil,os

api_key = '0c2fecccc4224abcb5b80f6c69a52663'
url = "https://gpt4-j.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-06-01"
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}
operations = {
        'all': "100.Call the relevant API, pass special unexpected parameters to the API; Introduce outliers; Performing unexpected operations on variables;",
        'array':[
                 "1.Change the size of the array and try smaller or larger values;",
                 "2.Change the content of the array, single type or mixed type;",
                 "3.Explore different modes of memory allocation or array filling (sparse, dense);",
                 "4.Modify the array access mode;",
                 "5.Dynamically modify the state (length, type, content) of the array (by means of callback functions, etc.) during critical operations;",
                 "6.Assign a value to arr, and Give multiple different assignments to the same element; Insert statements that change the state of the array or operations on other elements of the array or operations on other parameters between multiple different assignments to the same element;"
                ],
        'function':[
                "1.Add conditional statements to functions so that different parameters can trigger different logic; Call the function with different parameters before and after optimization, and different logic in opt needs to be triggered by two calls to the parameters filled in.",
                "2.Perform unexpected operations on function parameters;",
                "3.Call the function with different parameters before and after optimization or elsewhere. The parameters filled in the two calls should be of different types or values, and different types of parameters that meet or do not meet expectations can be filled in separately;cc",
                "4.Change the timing of the function call; Change function call parameters (context-sensitive, interesting); Change the number of function calls (fill in the parameters of different states that meet expectations and do not meet expectations); Replace or remove function calls;",
                ],
        'class':[
                "1.Modify the inheritance structure: Add a new class hierarchy, change the inheritance chain, change the parent class;",
                "2.Add or subtract modify class attributes and methods;",
                "3.Dynamic class generation;",
                "4.Change the constructor logic, such as adding memory allocation operations, garbage collection, adding control flow statements, adding the use of super, etc.",
                "5.Overwrite a method, change the overwritten method logic;",
                "6.In the overridden method, change the expected state of the object or its own state, change the state of other variables or global variables; Instantiate the class and use instances to call methods or properties;"],
        'number':[
                "1.Use extreme values, boundary values, and illegal value variations frequently;"
            ],
        'object':[
                "1.Manipulating the prototype chain of objects (such as mixing objects with unexpected constructors and prototypes);",
                "2.Change the property type of more objects during loops or callbacks or critical operations, and dynamically modify the object structure;",
                "3.Create an object with a structure similar to or identical to the selected object (same attribute name);"
                ],
        'any':[
               "1.Randomly select mutation operation by oneself;",
               "2.Change the initialization state;",
                "3.Add statements that can trigger optimization operations such as constant folding and common subexpression elimination;",
                "4.Changing the value/type of the loop traversal during the loop by direct assignment or otherwise;",
                "5.Insert safety sensitive operation;",
                "6.Declare a new variable;",
]
# parameter
                }

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
    all_type2 = []
    for type in range(5, 86):
        if len(config.texts[type]) > 0:
            all_type2.append(type)
    for t in [2, 65, 73, 76, 80, 65, 73, 76, 80, 65, 73, 76, 80, 81, 81, 81]:
        all_type2.append(t)
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
    visitor = JSV()
    try:
        visitor.visit(tree)
    except RecursionError:
        return
    rewriter = TokenStreamRewriter(tokens=stream)
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
    return new_sample


def extract(samples_text):
    pattern = re.compile(r'```javascript_start(.*?)javascript_end```', re.DOTALL)

    samples = pattern.findall(samples_text)
    samples_return = []

    for i, sample in enumerate(samples, start=1):
        sample_content = sample.strip()
        samples_return.append(sample_content)
    return samples_return

def extract2(samples_text):
    pattern = re.compile(r'```javascript(.*?)```', re.DOTALL)

    samples = pattern.findall(samples_text)
    samples_return = []

    for i, sample in enumerate(samples, start=1):
        sample_content = sample.strip()
        samples_return.append(sample_content)
    return samples_return


def extract_content(s):
    if not s:
        print(s)
        return "[]"
    # 查找第一个'['的位置
    start_index = s.find('[')
    # 查找最后一个']'的位置
    end_index = s.rfind(']')
    
    # 如果找到了'['和']'，提取并返回这部分内容
    if start_index != -1 and end_index != -1:
        return s[start_index:end_index+1]
    else:
        return "[]"
    

@SetTimeoutDecorator(timeout=30)
def gpt_getvars(origin_sample):
    print("[gpt_getvars]")
    data1 = {
        "messages": [
            {
            "role": "user",
            "content": '''
                sample:{},
                The given sample is a PoC of historical vulnerabilities, identifying key variables and their corresponding types in the sample. 
                Note: Identify any type of variable, such as array, function, class, number, etc;
                Identification Criteria:
                    1. Variables involved in multiple operations;
                    2. Variables with frequently changing types, states, or values;
                    3. Variables whose changes directly affect the program's control flow;
                    4. Variables involving complex structures;
                    5. Variables involved in security-sensitive operations;
                Notes:
                    Variables with unknown types are given lower priority;
                    Loop variables that do not involve additional operations are given lower priority;
                    Variables that are only declared but never used are not considered key variables;
                    Functions that are only called once are not considered key variables;
                    Function parameters that are never used are not considered key variables;
                    Variables like e in 'catch (e)' is not considered key variables;
                    
                Output in dictionary array format[{{'Name of variable 1':'Type of variable 1'}},{{'Name of variable 2':'Type of variable 2'}},{{'Name of variable 3':'Type of variable 3'}},...,{{'Name of variable n':'Type of variable n'}}]。
                Sort by variable criticality priority, output only the array without any other content.
                    '''.format(origin_sample)
        }
        ],
        # "max_tokens": 100,
    }
    try:
        response_vars = requests.post(url, headers=headers, json=data1)
        response_vars_json = response_vars.json()
        vars_str = response_vars_json["choices"][0]["message"]["content"]
        with open('/js/output/gpt/var2.txt','a') as file:
            file.write(origin_sample + "\n")
            file.write(vars_str + "\n")

        vars_list = ast.literal_eval(vars_str)
        # print(vars_list)
    except Exception as e:
        vars_list = []
        print("An [gpt_mutate1] error occurred:", e)
    time.sleep(2)
    return vars_list


@SetTimeoutDecorator(timeout=60)
def gpt_mutate1(origin_sample, var_dict):
    print('[gpt_mutate1]')

    var_name = list(var_dict.keys())[0]
    var_type1 = var_dict[var_name].lower()
    if var_type1 == 'any':
        var_type = var_type1
    elif var_type1 == 'int':
        var_type = 'number'
    elif 'array' in var_type1:
        var_type = 'array'
    else:
        var_type = random.choice(['any',var_type1,var_type1,var_type1])
    ops = operations.get(var_type, operations['any'])
    ops_len = len(ops)
    ops_index = (ops_len // 2) + 1 if ops_len % 2 != 0 else ops_len // 2
    operation = random.sample(ops, ops_index)
    if var_name == 'anyone':
        var_name = "sample"
    else:
        var_name = " variable "+var_name

    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a JavaScript code mutator."
            },
            {
                "role": "user",
                "content": '''
                    {},
                    Perform mutation on {} to generate 10 different samples, with the following mutation operations available for each sample:
                    {};
                    {};
                    Note: 
                        Choose multiple mutation operations for a sample at will. 
                        Mutation should be diverse and meaningful with the goal of triggering vulnerabilities or increasing coverage. 
                        Ensure that a portion of the original sample's structure is preserved.
                    Attention: 
                        Do not output any content, only output the complete sample. 
                        Do not use meaningless statements such as console.log or print. 
                        Label the mutated variable, its type, and the order number of the selected mutation operation at the end of the sample.
                    Format requirements: 
                        Each mutated sample need to be annotated with '//GPT' using annotations, and each sample should be wrapped with " ```javascript_start " and " javascript_end``` "
                            '''.format(origin_sample, var_name, operation, operations['all'])
                                }
        ],
        # "max_tokens": 100,
    }
    # print("=====================================")
    time.sleep(3)
    new_samples = ""
    try:
        response_samples = requests.post(url, headers=headers, json=data)
        print(response_samples)
        response_samples_json = response_samples.json()
        # print(response_samples_json)
        new_samples = response_samples_json["choices"][0]["message"]["content"]
        # print(new_samples)
    except Exception as e:
            print("An [gpt_mutate1] error occurred:", e)
    # print("new_samples", len(config.new_samples))

    return new_samples


class Chat:
    def __init__(self, conversation_list=[]) -> None:
        modles = random.choice(vulmode.merged_vulnerability_patterns)
        
        self.conversation_list = [{'role':'system','content':f'''{vulmode.merged_vulnerability_patterns}
                                   The above content covers various vulnerability patterns. 
                                   Below, I will provide you with a sample. 
                                   After receiving the sample, you randomly select a vulnerability pattern and extract key variables that match the selected vulnerability pattern from the sample. 
                                   Output the names of key variables in array format and Wrap each variable name in single quotation marks.
                                   Do not output any other content besides the array.
                                   '''}]

    def show_conversation(self, msg_list):
        for msg in msg_list[-2:]:
            if msg['role'] == 'user': 
                pass
            else:  
                message = msg['content']
                print(f"\U0001f47D: {message}\n")
            print()

    @SetTimeoutDecorator(timeout=60)
    def ask(self, prompt, target='sample'):
        self.conversation_list.append({"role": "user", "content": prompt})
        messages = {"messages": self.conversation_list}
        response = requests.post(url, headers=headers, json=messages)
        time.sleep(5)
        response_json = response.json()
        try:
            content = response_json["choices"][0]["message"]["content"]
        except Exception as e:
            print("An error occurred:", e)
            print(response_json)
            exit()
        if target == 'var':
            self.conversation_list.append({"role": "assistant", "content": content})
        return content

        self.show_conversation(self.conversation_list)


def gpt(sample):
    talk = Chat()
    new_samples = []

    #get key vars
    words = sample.decode()
    try:
        is_done, is_timeout, erro_message, vars_str = talk.ask(words, 'var')
        if is_timeout:
            print("[Get Vars Timeout]")
        try:
            vars_list = ast.literal_eval(vars_str)
        except Exception as e0:
            vars_str = extract_content(vars_str)
            print("An Getvars0 error occurred:", e)
            print(vars_str)
            vars_list = ast.literal_eval(vars_str)
    except Exception as e:
        print("An Getvars error occurred:", e)
        print(vars_str)
        exit()
        return new_samples
    if not vars_list:
        vars_list.append("any variable")
    time.sleep(10)
    #get mutated sampels
    for var in vars_list:
        if vars_list.index(var) >= 2:
            break
        time.sleep(5)
        try:
            if var != 'any variable':
                var = 'the key variable ' + var
            words = '''
            Select a suitable vulnerability pattern for {} and mutate the sample according to the selected vulnerability pattern for that variable to generate 10 different samples. 
            Note: 
            1.Only provide the complete sample after mutation, annotate the mutation, and indicate the selected vulnerability pattern id at the beginning.
            2.Each mutated sample need to be annotated with '//GPT' using annotations and wrapped with " ```javascript_start " and " javascript_end```. 
            '''.format(var)
            is_done, is_timeout, erro_message, samples_text = talk.ask(words)
            if is_timeout:
                print("[GptMutate Timeout]")
                continue
            new_samples_son = extract(samples_text)
            if not new_samples_son:
                new_samples_son = extract2(samples_text)
                if not new_samples_son:
                    print(samples_text)

            for new_sample in new_samples_son:
                new_samples.append(new_sample)
            print("GPT sample:", len(new_samples))
        except Exception as e:
            print("An GptMutate error occurred:", e, "\n", erro_message)

    return new_samples



def gpt0(buf):
    new_samples = []
    try:
        is_done, is_timeout, erro_message, vars_list = gpt_getvars(buf.decode())
        if is_timeout:
            print("[Getvars Timeout]")
    except Exception as e:
        print("An Getvars error occurred:", e)
        # print(erro_message)
        return new_samples

    if not vars_list:
        vars_list.append({'anyone':'any'})

    var_num = len(vars_list)
    if var_num > 4:
        split_index = (var_num // 2) + 1 if var_num % 2 != 0 else var_num // 2
        # 分成前一半和后一半
        first_half = vars_list[:split_index]
        second_half = vars_list[split_index:]   

        selected_first_half = random.sample(first_half, 3)
        selected_second_half = random.sample(second_half, 2)
        vars_list = selected_first_half + selected_second_half
    
    for var_dict in vars_list:
        try:
            is_done, is_timeout, erro_message, samples_text = gpt_mutate1(buf.decode(), var_dict)
            if is_timeout:
                print("[GptMutate Timeout]")
                continue
            new_samples_son = extract(samples_text)
            if not new_samples_son:
                new_samples_son = extract2(samples_text)
                if not new_samples_son:
                    print(samples_text)

            for new_sample in new_samples_son:
                new_samples.append(new_sample)
            print("GPT sample:", len(new_samples))
        except Exception as e:
            print("An GptMutate error occurred:", e, "\n", erro_message)
        
    return new_samples


def gs(buf, add_buf, cur_id, queued_discovered):
    config.new_samples = []
    config.sample = buf
    new_discovered = queued_discovered - config.pre_queued_discovered
    config.pre_queued_discovered = queued_discovered
    if config.new_samples_len:
        result = (new_discovered / config.new_samples_len) * 100
    else:
        result = 0

    if config.use_gpt: #上一次用了gpt
        config.use_gpt = False
        result = f"{result:.2f}%"
        with open('/js/output/gpt/newidje3.txt','a') as file:
            file.write("==============================GPT START===============================\n")
            file.write("new_samples_len: " + str(config.new_samples_len) + "\n")
            file.write("new_discovered:  " + str(new_discovered) + "\n")
            file.write("new_discovered:  " + str(result) + "\n")
            file.write("===============================GPT END================================\n")
        is_done1, is_timeout1, erro_message1, results1 = checkParsetime(buf)
        if is_timeout1 is True:
            return len(config.new_samples)
        is_done2, is_timeout2, erro_message2, results2 = checkParsetime(add_buf)
        if is_timeout2 is True:
            return len(config.new_samples)
        
        rewriter = pre_process(buf, add_buf)
        all_type2 = init2()
        all_type3 = init3()

        new_sample = ""
        count = 0
        while count < config.sample_size:
            count += 1
            rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
            new_sample = change(rewriter, all_type2, all_type3)
            if new_sample not in config.new_samples:
                config.new_samples.append(new_sample)
                if len(config.new_samples) > config.sample_size:
                    print("count:", count)
                    return len(config.new_samples)  
        return len(config.new_samples)
    else: #上一次没用gpt
        result1 = f"{result:.2f}%"
        with open('/js/output/gpt/newidje3.txt','a') as file:
            file.write("---------------------------------------------------------------------\n")
            file.write("new_samples_len: " + str(config.new_samples_len) + "\n")
            file.write("new_discovered:  " + str(new_discovered) + "\n")
            file.write("new_discovered:  " + str(result1) + "\n")
            file.write("---------------------------------------------------------------------\n")
        if cur_id <= 100:
            if result < 2 and queued_discovered != 0:
                config.use_gpt = True
        elif 100 < cur_id <= 300:
            if result < 0.5 and queued_discovered != 0:
                config.use_gpt = True
        elif 300 < cur_id <= 10000:
            if result <= 0 and queued_discovered != 0:
                config.use_gpt = True
        else:
            if result <= 0 and queued_discovered != 0:
                config.use_gpt = True

        if config.use_gpt:
            # pass   
            # if cur_id >= 50:
            #         exit(0)
            # if (cur_id >= 50) and (cur_id % 10 == 0):
                print('============================ Run Times ', cur_id, ' Call GPT ============================')
                new_samples = []
                new_samples = gpt(buf)
                for new_sample in new_samples:
                    if new_sample not in config.new_samples:
                        config.new_samples.append(new_sample)
                        if len(config.new_samples) > config.sample_size:
                            print("new_samples", len(config.new_samples))
                            return len(config.new_samples)
                print('============================ GPT ', cur_id, ' DONE ============================')
                print("new_samples", len(config.new_samples))
                return len(config.new_samples)
        else:
            is_done1, is_timeout1, erro_message1, results1 = checkParsetime(buf)
            if is_timeout1 is True:
                return len(config.new_samples)
            is_done2, is_timeout2, erro_message2, results2 = checkParsetime(add_buf)
            if is_timeout2 is True:
                return len(config.new_samples)
            
            rewriter = pre_process(buf, add_buf)
            all_type2 = init2()
            all_type3 = init3()

            new_sample = ""
            count = 0
            while count < config.sample_size:
                count += 1
                rewriter.rollback(rewriter.lastRewriteTokenIndex(), "default")
                new_sample = change(rewriter, all_type2, all_type3)
                if new_sample not in config.new_samples:
                    config.new_samples.append(new_sample)
                    if len(config.new_samples) > config.sample_size:
                        print("count:", count)
                        return len(config.new_samples)  


    print('============================ Run Times ', cur_id, ' ============================')

    
    return len(config.new_samples)


def parse(buf, add_buf, cur_id, queued_discovered):
    gs(buf, add_buf, cur_id, queued_discovered)
    config.new_samples_len = len(config.new_samples)
    return len(config.new_samples)


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


if __name__ == '__main__':
    pass

