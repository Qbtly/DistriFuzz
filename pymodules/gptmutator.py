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
import time
import re
import config
import ast
import random
import vulpattern
from call_function_with_timeout import SetTimeoutDecorator

api_key = '0c2fecccc4224abcb5b80f6c69a52663'
url = "https://gpt4-j.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-06-01"
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}
operations = {
        'array':['1. 改变数组的大小，尝试更小或更大的值;. 变更数组的内容，单一类型/混合类型;3. 更改数据类型，大小不变;4. 调用涉及到对内存操作的API,给API传递非预期的参数;5. 更改样本中调用的API;6. 对变量进行非预期的操作，如对数组访问不存在的下标或对数组设置属性值等',
                 '1. 填充数组（稠密数组或稀疏数组）;2. 调用相关的API 或 样本中的函数，将数组作为其实例或参数;3. 声明一个回调函数（可以通过重写一个对象的valueOf或toString方法来实现 ，也可以使用其他方法 ），在回调函数中修改数组的状态（清空数组、更改属性、更改类型等） ;4. 回调函数作为被调API或函数的参数使用',
                 '1. 对变量进行赋值，对同一元素进行多次不同赋值; 2. 在对同一元素的多次不同赋值中间插入改变数组状态的语句/对数组其他元素的操作/对其他参数的操作',
                ],
        'function':['1. 调用函数两次，分别填入符合预期与不符合预期的不同类型的参数;2. 参数需与上下文有关联（元素从上下文中选择）或者有趣',
                    '1. 函数中添加条件语句，使不同参数能够触发不同的逻辑; 2. 优化前后分别以不同参数调用函数，两次调用填入的参数需要触发函数中的不同逻辑',
                    '1. 优化前后分别以不同参数调用函数，两次调用填入的参数类型或数值不同; 2. 改变函数调用参数、位置、次数',
                ],
        'class':['1. 更改父类，更改被重写的方法;2. 在重写的方法中，改变对象的预期状态或本身的状态（如修改数组长度或元素类型）;3. 调用重写的方法',
                 '1. 更改构造函数行为，如添加内存分配操作、垃圾回收、添加控制流语句等; 2. 操纵对象的原型链（如将对象与非预期的构造函数和原型混合）;3. 对类进行实例化，并使用实例'
                ],
        'number':['1. 添加能够引发常量折叠、公共子表达式消除的语句; 2.在循环过程中以直接赋值或其他方式改变循环遍历的值/类型;'],
        'any':['1. 自由发挥; 2. 修改控制流逻辑; 3. 多使用极值、边界值、非法值变异; 4. 对数据类型的API（成员函数、属性）进行变异 ，添加API、删除API、修改API、参数变异、调用次数变异等; 5. 加入与样本中使用的数据类型相关联类型的操作,组合不同的数据类型,增加类型转换操作; 6.增加变量声明和赋值,增加变量之间的嵌套关系,适当做一些不合乎语法的变异']

                }

def extract(samples_text):
    # Regular expression to extract code samples between the markers
    pattern = re.compile(r'```javascript_start(.*?)```javascript_end', re.DOTALL)

    # Extract all samples
    samples = pattern.findall(samples_text)
    samples_return = []
    # Print each extracted sample
    for i, sample in enumerate(samples, start=1):
        sample_content = sample.strip()
        samples_return.append(sample_content)
        # print("--------------sample {}-------------".format(i))
        # print(sample_content)
        # print()
    return samples_return

def pick_random_pattern(patterns):
    selected_patterns = []

    for group in patterns:
        patterns = group.get("patterns", [])
        if patterns:
            selected = random.sample(patterns, min(3, len(patterns)))
            selected_patterns.extend(selected)
    return selected_patterns


@SetTimeoutDecorator(timeout=30)
def get_keyvars(origin_sample, patterns):
    data = {
        "messages": [
            {
             "role": "system",
             "content": '''
                你的任务是对 JavaScript 引擎测试样本进行关键变量提取。
                请先为该样本选取一个合适的漏洞模式（从下面可选的漏洞模式中选择一个最适合的模式），
                然后从样本中提取出符合所选漏洞模式的关键变量，并为每个关键变量匹配最可能导致的漏洞根因（RootCause）。
                最后请以 JSON 数组形式输出，每个元素是一个对象，格式如下：
                {{
                    "var": "变量名称",
                    "rootc": "漏洞根因代号（例如 A, B, C, D, E, F）"
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
                样本：{}，
                请根据上面的要求，先选取一个合适的漏洞模式，再从样本中提取出符合该模式的关键变量（不超过3个），并为每个关键变量匹配其可能导致的漏洞根因，最后以 JSON 数组形式输出结果。
            '''.format(origin_sample)
        }
        ],
        # "max_tokens": 100,
        "temperature": 0.2
    }
    print(data["messages"][0]["content"])
    print(data["messages"][1]["content"])
    return []
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
def gpt_getvars(origin_sample):
    print("[gpt_getvars]")
    data1 = {
        "messages": [
            {
             "role": "system",
             "content": "你是一个代码变量提取器"
            },
            {
            "role": "user",
            "content": '''
                样本：{}，
                给定的样本是历史漏洞的PoC, 识别样本中的关键变量
                注意：要识别出任何类型的变量, array、function、class、number等等类型的变量;
                以字典数组形式输出[{{'变量1名':'变量类型'}},{{'变量2名':'变量类型'}},{{'变量3名':'变量类型'}},...,{{'变量n名':'变量类型'}}]。
                按变量关键性大小排序，只输出数组不要任何其他内容。
                    '''.format(origin_sample)
        }
        ],
        # "max_tokens": 100,
    }
    response_vars = requests.post(url, headers=headers, json=data1)
    response_vars_json = response_vars.json()
    vars_str = response_vars_json["choices"][0]["message"]["content"]
    try:
        vars_list = ast.literal_eval(vars_str)
        print(vars_list)
    except:
        vars_list = []
    time.sleep(2)
    return vars_list



@SetTimeoutDecorator(timeout=30)
def ai_mutate(origin_sample, keyvar, patterns):
    data = {
        "messages": [
            {
                "role": "system",
                "content": "你的任务是对 JavaScript 引擎测试样本进行代码变异。你将接收一个原始样本，以及一个关键变量和若干漏洞模式，请围绕该关键变量，结合最合适的几个漏洞模式进行结构化变异，以生成用于模糊测试的有效样本。"
            },
            {
                "role": "user",
                "content": '''
                    样本代码：
                    {}

                    关键变量：{}

                    可选漏洞模式：
                    {}

                    生成10个变异样本，每个变异样本需保持原样本逻辑结构的可运行性和测试语义，并尽可能引入与关键变量及漏洞模式相关的变化。
                    注意：不要附加任何注释或说明,不使用console.log。
                    注意：每个变异样本都使用```javascript_start和```javascript_end包裹
                            '''.format(origin_sample, keyvar, patterns)
            }
        ],
        # "max_tokens": 100,
        "temperature": 0.7,
    }
    print(data["messages"][0]["content"])
    print(data["messages"][1]["content"])
    return []
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



@SetTimeoutDecorator(timeout=30)
def gpt_mutate1(origin_sample, var_dict):
    print('[gpt_mutate1]')

    var_name = list(var_dict.keys())[0]
    var_type1 = var_dict[var_name].lower()
    if var_type1 == 'any':
        var_type = var_type1
    else:
        var_type = random.choice(['any',var_type1,var_type1,var_type1])
    # print(var_name,var_type1,var_type)
    operation = random.choice(operations[var_type])

    if var_name == 'anyone':
        var_name = "样本"
    else:
        var_name = "变量"+var_name

    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a JavaScript code mutator."
            },
            {
                "role": "user",
                "content": '''
                    样本：{}，
                    对{}进行变异生成10个不同的样本,每个样本可选的变异操作如下：
                    {}
                    注意：对于一个样本任意选择多个变异操作使用。变异要多样化有意义以触发漏洞或提高覆盖率为目标。要保证原样本的一部分结构。
                    注意：不要输出任何内容，只输出完整的样本,不使用console.log。
                    注意：每个变异后的样本要完整，每一个样本都使用```javascript_start和```javascript_end包裹
                            '''.format(origin_sample, var_name, operation)
                                }
        ],
        # "max_tokens": 100,
    }
    print("=====================================")
    time.sleep(5)
    response_samples = requests.post(url, headers=headers, json=data)
    response_samples_json = response_samples.json()
    new_samples = response_samples_json["choices"][0]["message"]["content"]
    print("new_samples", len(config.new_samples))

    return new_samples

@SetTimeoutDecorator(timeout=30)
def gpt_mutate(origin_sample):
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a JavaScript code mutator."
            },
            {
                "role": "user",
                "content": '''
                    样本：{}
                    所给样本为历史漏洞的PoC或是可以触发新覆盖率的样本，你需要对它进行变异，给出12个不同的变异样本。
                    具体做法：
                    1.对于变量（包括函数、类等各种变量）：识别样本中的关键变量，参考变量的关键性，对变量进行变异操作（所有变量都要变异到，关键性高的变异次数多，关键性低的变异次数少）：
                    1.1为变量调用相关的API（调用相关方法或修改变量属性）
                    1.2为API填入容易触发漏洞的参数（有趣、多样、与上下文有联系、边界值）
                    2.对于函数变量，使用不同参数调用，在不同位置调用
                    2.1调用相关的API（调用相关方法或修改变量属性）
                    3.对于子类变量，可修改其父类类型，重写其方法
                    3.1调用相关的API（调用相关方法或修改变量属性）
                    4. 自由发挥，可以修改控制流逻辑，可修改数据类型
                    注意：对于一个样本任意选择多个变异操作使用。变异要多样化有意义以触发漏洞或提高覆盖率为目标。
                    注意：不要输出任何内容，最好不要改变样本中的其他变量，只输出完整的样本。
                    注意：每个变异后的样本要完整，每一个样本都使用```javascript_start和```javascript_end包裹
                            '''.format(origin_sample)
                                }
        ],
        # "max_tokens": 100,
    }

    time.sleep(10)
    response_samples = requests.post(url, headers=headers, json=data)
    response_samples_json = response_samples.json()
    new_samples = response_samples_json["choices"][0]["message"]["content"]
    print("new_samples", len(config.new_samples))

    return new_samples

def parse1(buf, add_buf, cur_id):
    print('============================', cur_id, '============================')
    new_samples = []
    try:
        is_done, is_timeout, erro_message, vars_list = gpt_getvars(buf.decode())
    except Exception as e:
        print("An error occurred:", e)
        return len(config.new_samples)
    # vars_list = []
    if not vars_list:
        vars_list.append({'anyone':'any'})
    # print(vars_list)
    for var_dict in vars_list:
        if vars_list.index(var_dict) > 3:
            break
        try:
            is_done, is_timeout, erro_message, samples_text = gpt_mutate1(buf.decode(), var_dict)
            if is_timeout:
                print("[Timeout]")
                print(erro_message)
            new_samples = extract(samples_text)
        except Exception as e:
            print("An error occurred:", e)
        for new_sample in new_samples:
            if new_sample not in config.new_samples:
                config.new_samples.append(new_sample)
                if len(config.new_samples) > config.sample_size:
                    return len(config.new_samples)
    print(len(config.new_samples))
    return len(config.new_samples)



def parse(buf, add_buf, cur_id):
    print('============================', cur_id, '============================')
    
    new_samples = []
    selected_patterns = pick_random_pattern(vulpattern.vul_patterns)
    try:
        is_done, is_timeout, erro_message, vars_list = get_keyvars(buf.decode(), selected_patterns)
        vars_list = [
    {
        "var": "obj",
        "rootc": "D"
    },
    {
        "var": "foo",
        "rootc": "E"
    }
]

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
            new_samples = extract(samples_text)
        except Exception as e:
            print("An error occurred:", e)
        for new_sample in new_samples:
            if new_sample not in config.new_samples:
                config.new_samples.append(new_sample)
                if len(config.new_samples) > config.sample_size:
                    return len(config.new_samples)
    # print(len(config.new_samples))
    return len(config.new_samples)

def fuzz():
    """
    Called per fuzzing iteration.

    @type buf: bytearray
    @param buf: The buffer that should be mutated.

    @type add_buf: bytearray
    @param add_buf: A second buffer that can be used as mutation source.

    @type max_size: int
    @param max_size: Maximum size of the mutated output. The mutation must not
        produce data larger than max_size.

    @rtype: bytearray
    @return: A new bytearray containing the mutated data
    """
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


if __name__ == '__main__':
    js1 = '''
    let obj = {};
Object.defineProperty(obj, "foo", {
    get: () => { return {}; } 
});
    '''
    js2 = '''
    class Base {
        constructor() {
            this.x = 1;
        }
    }
    class Derived extends Base {
        constructor() {
            super();
        }
    }
    let bound = Object.bind();
    Reflect.construct(Derived, [], bound);
    %OptimizeFunctionOnNextCall(Derived);
    new Derived();
    '''
    length = parse(js1.encode(), js2.encode(),1)
    print(length)
    # if length > 0:
    #     for i in range(0, length):
    #         with open("/home/b/crossover/custom_mutators/examples/new_samples/"+str(i)+".js", "w") as f:
    #             f.write(fuzz().decode())
    #             f.close()
            # print(fuzz().decode())
            # print("=============================")


