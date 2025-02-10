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
def gpt_mutate1(origin_sample, var_dict):
    print('[gpt_mutate1]')

    var_name = list(var_dict.keys())[0]
    # print("==================1===================")
    var_type1 = var_dict[var_name].lower()
    # print("==================2===================")
    if var_type1 == 'any':
        var_type = var_type1
    else:
        var_type = random.choice(['any',var_type1,var_type1,var_type1])
    # print("==================3===================")
    print(var_name,var_type1,var_type)
    operation = random.choice(operations[var_type])
    # print("==================4===================")
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

def parse(buf, add_buf, cur_id):
    print('============================', cur_id, '============================')
    new_samples = []
    # print(buf)
    print(buf.decode())
    # try:
    #     is_done, is_timeout, erro_message, samples_text = gpt_mutate(buf)
    #     if is_timeout:
    #         print("[Timeout]")
    #         print(erro_message)
    #     new_samples = extract(samples_text)
    # except Exception as e:
    #     print("An error occurred:", e)
    # for new_sample in new_samples:
    #     if new_sample not in config.new_samples:
    #         config.new_samples.append(new_sample)
    #         if len(config.new_samples) > config.sample_size:
    #             return len(config.new_samples)
    
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
        time.sleep(1)
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

    %OptimizeFunctionOnNextCall(opt);

    opt(arr2, arr2);
    arr2[0].x;
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
    length = parse(js1.encode(), js2.encode())
    print(length)
    if length > 0:
        for i in range(0, length):
            with open("/home/b/crossover/custom_mutators/examples/new_samples/"+str(i)+".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
            # print(fuzz().decode())
            # print("=============================")


# Uncomment and implement the following methods if you want to use a custom
# trimming algorithm. See also the documentation for a better API description.

# def init_trim(buf):
#     '''
#     Called per trimming iteration.
#
#     @type buf: bytearray
#     @param buf: The buffer that should be trimmed.
#
#     @rtype: int
#     @return: The maximum number of trimming steps.
#     '''
#     global ...
#
#     # Initialize global variables
#
#     # Figure out how many trimming steps are possible.
#     # If this is not possible for your trimming, you can
#     # return 1 instead and always return 0 in post_trim
#     # until you are done (then you return 1).
#
#     return steps
#
# def trim():
#     '''
#     Called per trimming iteration.
#
#     @rtype: bytearray
#     @return: A new bytearray containing the trimmed data.
#     '''
#     global ...
#
#     # Implement the actual trimming here
#
#     return bytearray(...)
#
# def post_trim(success):
#     '''
#     Called after each trimming operation.
#
#     @type success: bool
#     @param success: Indicates if the last trim operation was successful.
#
#     @rtype: int
#     @return: The next trim index (0 to max number of steps) where max
#              number of steps indicates the trimming is done.
#     '''
#     global ...
#
#     if not success:
#         # Restore last known successful input, determine next index
#     else:
#         # Just determine the next index, based on what was successfully
#         # removed in the last step
#
#     return next_index
#
# def post_process(buf):
#     '''
#     Called just before the execution to write the test case in the format
#     expected by the target
#
#     @type buf: bytearray
#     @param buf: The buffer containing the test case to be executed
#
#     @rtype: bytearray
#     @return: The buffer containing the test case after
#     '''
#     return buf
#
# def havoc_mutation(buf, max_size):
#     '''
#     Perform a single custom mutation on a given input.
#
#     @type buf: bytearray
#     @param buf: The buffer that should be mutated.
#
#     @type max_size: int
#     @param max_size: Maximum size of the mutated output. The mutation must not
#         produce data larger than max_size.
#
#     @rtype: bytearray
#     @return: A new bytearray containing the mutated data
#     '''
#     return mutated_buf
#
# def havoc_mutation_probability():
#     '''
#     Called for each `havoc_mutation`. Return the probability (in percentage)
#     that `havoc_mutation` is called in havoc. Be default it is 6%.
#
#     @rtype: int
#     @return: The probability (0-100)
#     '''
#     return prob
#
# def queue_get(filename):
#     '''
#     Called at the beginning of each fuzz iteration to determine whether the
#     test case should be fuzzed
#
#     @type filename: str
#     @param filename: File name of the test case in the current queue entry
#
#     @rtype: bool
#     @return: Return True if the custom mutator decides to fuzz the test case,
#         and False otherwise
#     '''
#     return True
#
# def queue_new_entry(filename_new_queue, filename_orig_queue):
#     '''
#     Called after adding a new test case to the queue
#
#     @type filename_new_queue: str
#     @param filename_new_queue: File name of the new queue entry
#
#     @type filename_orig_queue: str
#     @param filename_orig_queue: File name of the original queue entry
#     '''
#     pass
