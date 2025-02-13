#!/usr/bin/env python
# encoding: utf-8

import requests
import time
import re
import config
import ast
import random
from call_function_with_timeout import SetTimeoutDecorator
import ollama


def extract(samples_text):
    # Regular expression to extract code samples between the markers
    pattern = re.compile(r'```javascript(.*?)```', re.DOTALL)

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


@SetTimeoutDecorator(timeout=1000)
def llm_mutate(origin_sample):
    messages = [
        {
            "role": "system",
            "content": "You are a JavaScript code mutator."
        },
        {
            "role": "user",
            "content": '''
                Sample:{}
                Please create 10 variations of this sample by mutating it.
                Mutation could involve:
                1. Insert a new statement that affects control flow  
                2. Inject an API call that interacts with an existing variable  
                3. Modify an existing function's return value  
                4. Alter a loop condition to increase/decrease iterations  
                5. Introduce a side-effect in an existing function  
                6. Replace an arithmetic operation with an equivalent but slightly different expression  
                7. Wrap an expression in an additional function call  
                8. Modify the object prototype of an existing object  
                9. Add an exception handling block around existing code  
                10. Change an object property access method (dot notation ↔ bracket notation)  
                11. Modify a function parameter's type or structure  
                12. Introduce an implicit type conversion in an expression  
                13. Replace an existing function call with a similar but different API call  
                14. Modify a logical condition to invert or adjust its evaluation  
                15. Alter the execution order of independent statements 
                Each mutation Choose one or two changes. 
                You should ensure each sample maintains some semblance of the original structure but introduces changes that could test different paths in JavaScript engines. 
                Output only the variant, don't output anything else. Do not add comments to variant.
                The output format:
                **Sample 1:**
                ```javascript
                fill in the first variant
                ```
                '''.format(origin_sample)
        }
    ]

    response = ollama.chat(model='deepseek-r1:70b', messages=messages) # deepseek-r1 codellama
    clean_response = re.sub(r"<.*?>", "", response['message']["content"])
    print(clean_response)
    return clean_response

samples = []

def parse(buf, add_buf, cur_id):
    # print('============================', cur_id, '============================')
    new_samples = []
    print(buf.decode())
    try:
        is_done, is_timeout, erro_message, samples_text = llm_mutate(buf.decode())
        if is_timeout:
            print("[Timeout]")
            print(erro_message)
        new_samples = extract(samples_text)
    except Exception as e:
        print("An error occurred:", e)
    for new_sample in new_samples:
        if new_sample not in config.new_samples:
            config.new_samples.append(new_sample)
            # samples.append(new_sample)
            if len(config.new_samples) > config.sample_size:
                return len(config.new_samples)
    print("Config.new_samples: ",len(config.new_samples))
    return len(config.new_samples)


def fuzz():
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


if __name__ == '__main__':
    js1 = '''
    function opt(a, b) {
        b[0] = 0;
        for (let i = 0; i < 1; i++)
            a[0] = 0;
        b[0] = 9.431092e-317;
    }
    let arr1 = new Array(1);
    arr1[0] = 'a';
    opt(arr1, [0]);
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
    
    length = 0
    for ii in range(0, 1):
        start_time = time.time()
        length = parse(js1.encode(), js2.encode(), ii)
        end_time = time.time()
        elapsed_time = end_time - start_time  # 计算时间差
        print(f"Function execution time: {elapsed_time:.4f} seconds")
        print("Mutation",ii,":",length, "| Total :", len(samples))

        with open("/home/lab/myh/Jungle/new_samples/mutation_log.txt", "a") as f:
            f.write(f"Function execution time: {elapsed_time:.4f} seconds\n")
            f.write(f"Mutation {ii}: {length} | Total: {len(samples)}\n")
    if length > 0:
        for i in range(0, length):
            with open("/home/lab/myh/Jungle/new_samples/"+str(i)+".js", "w") as f:
                f.write(fuzz().decode())
                f.close()
                # print(fuzz().decode())
                # print("=============================")

