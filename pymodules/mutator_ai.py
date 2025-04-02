import easygui as g
import openai
import requests
import vulpattern


api_key = '0c2fecccc4224abcb5b80f6c69a52663'
url = "https://gpt4-j.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-06-01"
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

class Chat:
    def __init__(self, conversation_list=[]) -> None:
        self.conversation_list = [{'role':'system','content':f"可选漏洞模式：{vulpattern.vul_patterns}。下面你将收到一个样本，为其选取一个合适的漏洞模式，从样本中提取出符合所选漏洞模式的关键变量，以数组形式输出关键变量的名字，不要有任何其他内容。"}]
        self.costs_list = []  # 初始化聊天开销列表

    # 打印对话
    def show_conversation(self, msg_list):
        for msg in msg_list[-2:]:
            if msg['role'] == 'user':  # 如果是用户的话
                # print(f"\U0001f47b: {msg['content']}\n")
                pass
            else:  # 如果是机器人的话
                message = msg['content']
                print(f"\U0001f47D: {message}\n")
            print()

    # 调用chatgpt，并计算开销
    def ask(self, prompt):
        self.conversation_list.append({"role": "user", "content": prompt})
        messages = {"messages": self.conversation_list}
        response = requests.post(url, headers=headers, json=messages)
        response_json = response.json()
        # print(response_json)
        content = response_json["choices"][0]["message"]["content"]
        # print(content)
        # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.conversation_list)
        # response = openai.ChatCompletion.create(model="gpt-4", messages=self.conversation_list)
        # answer = response.choices[0].message['content']
        #把chatGPT的回答也添加到对话列表中，下一次问问题的时候就能形成上下文
        self.conversation_list.append({"role": "assistant", "content": content})
        self.show_conversation(self.conversation_list)

        cost = total_counts(response_json)
        self.costs_list.append(cost)
        print()


def total_counts(response):
    # 计算本次任务花了多少钱和多少tokens：
    tokens_nums = int(response['usage']['total_tokens'])  # 计算一下token的消耗
    price = 0.002 / 1000  # 根据openai的美元报价算出的token美元单价
    cost = '{:.5f}'.format(price * tokens_nums * 7.5)
    total = f'本次对话共消耗了{tokens_nums}个token，花了{cost}元（人民币）'
    print(total)

    return float(cost)


def main():
    talk = Chat()
    print()

    count = 0
    count_limit = 2#eval(input("你想要对话的次数是多少呢？\n(请输入数字即可)"))
    while count < count_limit:  
        if count < 1:
            words = '''
            function main() {
              function f0() {
                try {
                  var v0 = 9.137894809324841;
                } catch (v3) { }
                try {
                  var v1 = new Array(23);
                } catch (v4) { }
              }
              gc();
              f0();
            }
            main();
            main();
            main();
            '''
        else:
            words = "为关键变量v1选择一个合适的漏洞模式，按照所选漏洞模式针对变量v1对样本进行变异。只给出变异后的完整样本，用注释在样本中标明你所做的变异并在开头标明选取的漏洞模式,样本使用'''javascript_start 和 javascript_end'''包裹。"#input("您还可以继续与我交流，请您继续说：\n(请输入您的需求或问题)：")
        print()
        talk.ask(words)
        count += 1

    g.msgbox("对不起，您已达到使用次数的限额，欢迎您下次使用！")
    print(f'本轮聊天合计花费{sum(talk.costs_list)}元人民币。')


if __name__ == "__main__":
    main()