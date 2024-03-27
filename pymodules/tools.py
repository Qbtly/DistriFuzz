import os
import random
import shutil
import re
# coding=utf-8
import signal
import config


def all_type_text():
    for type in range(0, 86):
        if type == type:
            print(type, end=': ')
            for text in config.texts[type]:
                print(text, end="  |  ")
            print('\n')
            for interval in config.intervals[type]:
                print(interval, end="  |  ")
            print('\n')


def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(num)  # 设置 num 秒的闹钟
                print
                'start alarm signal.'
                r = func(*args, **kwargs)
                print
                'close alarm signal.'
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap

def extract(text, pattern):
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return matches[0]
    else:
        return []


def del_file(path_data):
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "/" + i  # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)

# 函数定义：根据指定的obj名字选择字典
def select_by_objname(data, obj, obj_name):
    dict_list = [item for item in data if item[obj] == obj_name]
    try:
        return dict_list[0]
    except:
        return {}

def select_by_obj_name(data, obj, obj_name):
    dict_list = [item for item in data if item[obj] == obj_name]
    try:
        return dict_list[0]
    except:
        return {}

def get_newname(names):
    new_name = "zdy"
    i = 0
    while new_name + str(i) in names:
        i += 1
        if i > 30:
            i = random.randint(31, 1000)
            break
    new_name = new_name + str(i)
    return new_name