import ollama
import re
import requests
import json, time

origin_sample = '''
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

messages = [
        {
            "role": "system",
            "content": "You are a JavaScript code mutator."
        },
        {
            "role": "user",
            "content": '''
                Do not output your thought process.
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
                11. Modify a function parameter’s type or structure  
                12. Introduce an implicit type conversion in an expression  
                13. Replace an existing function call with a similar but different API call  
                14. Modify a logical condition to invert or adjust its evaluation  
                15. Alter the execution order of independent statements 
                Each mutation Choose one or two changes. 
                You should ensure each sample maintains some semblance of the original structure but introduces changes that could test different paths in JavaScript engines. 
                Output only the variant, don't output anything else (including your thought process). 
                Finally, tell me how long it took you to answer.
                The output format:
                **Sample 1:**
                ```javascript_start
                fill in the first variat
                ```javascript_end
                '''.format(origin_sample)
        }
    ]

def extract(samples_text):
    pattern = re.compile(r'```javascript_start(.*?)```javascript_end', re.DOTALL)

    # Extract all samples
    samples = pattern.findall(samples_text)
    samples_return = []
    # Print each extracted sample
    for i, sample in enumerate(samples, start=1):
        sample_content = sample.strip()
        samples_return.append(sample_content)
        print("--------------sample {}-------------".format(i))
        print(sample_content)
        print()
    return samples_return


def llm():
    # 14d6c3c5.r16.cpolar.top
    API_URL = "http://172.17.0.1:11434/api/chat"  # 11434 是 Ollama 默认端口
    response = requests.post(API_URL, json={"model": "deepseek-r1:70b", "messages": messages}, stream=True)
    # deepseek-r1 codellama
    # print(response['message']["content"])

    # clean_response = re.sub(r"<.*?>", "", response['message']["content"])
    # print(response)
    # return response
    # 存储完整的回答
    full_response = ""
    print(response)

    for line in response.iter_lines():
        if line:  
            json_obj = line.decode("utf-8")  
            # print(json_obj)
            try:
                parsed_data = json.loads(json_obj)  
                # print(parsed_data)
                content = parsed_data.get("message", {}).get("content", "")
                full_response += content  
            except Exception as e:
                print("Response Error:", e)

    # print("最终回答:", full_response)
    return full_response


start_time = time.time()
clean_response = llm()
end_time = time.time()
elapsed_time = end_time - start_time  # 计算时间差

print(f"Function execution time: {elapsed_time:.4f} seconds")
extract(clean_response)
print(f"Function execution time: {elapsed_time:.4f} seconds")