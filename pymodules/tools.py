import os
import random
import shutil
import re
# coding=utf-8
import signal
import config


def extract_sample(samples_text):
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
    exit(1)


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


def remove_between(string, start, end):
    pattern = re.compile(re.escape(start) + '.*?' + re.escape(end))
    return re.sub(pattern, '', string, count=0)


def extract(text, pattern):
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return matches
    else:
        return ''


def extract0(text, pattern, default):
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return matches[0]
    else:
        return default


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


def format_boolean(optional):
    if optional == "False":
        return False
    elif optional == "True":
        return True
    return False


def classify(objs):
    # classify
    obj_name8type = {}
    for obj_info in objs:
        obj_type = obj_info['type'].lower()
        if obj_type not in list(obj_name8type.keys()):
            obj_name8type[obj_type] = set()
        obj_name8type[obj_type].add(obj_info['obj'])
    return obj_name8type




def select_random_files(directory, num_files=5):
    """
    Selects a random set of files from the specified directory.

    Args:
    directory (str): The path to the directory from which to select files.
    num_files (int): The number of random files to select.

    Returns:
    list: A list of selected file paths.
    """
    # Get a list of all files in the directory
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    
    # Check if the directory has enough files
    if len(files) < num_files:
        raise ValueError("Not enough files in the directory to select from.")
    
    # Randomly select files
    selected_files = random.sample(files, num_files)
    
    # Return the full paths of the selected files
    return [os.path.join(directory, file) for file in selected_files]


if __name__ == '__main__':
    names = ['zdy0', 'zdy1']
    for n in range(200):
        print(get_newname(names))
