import string
import random


# 定义一个函数来生成随机字符串
def get_string():
    length = random.randint(0, 15)
    # string.ascii_letters 包含所有字母(大写和小写)，string.digits 包含所有数字字符
    characters = string.ascii_letters + string.digits
    # 使用 random.choices 从所有字符中随机选取，形成指定长度的列表，然后使用 ''.join 将列表连接成字符串
    random_string = ''.join(random.choices(characters, k=length))
    random_string = repr(random_string)
    return random_string


def get_number():
    numbers = [
        -9223372036854775808, -9223372036854775807,
        -9007199254740992, -9007199254740991, -9007199254740990,
        -4294967297, -4294967296, -4294967295,
        -2147483649, -2147483648, -2147483647,
        -1073741824, -536870912, -268435456,
        -65537, -65536, -65535,
        -4096, -1024, -256, -128,
        -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 64,
        127, 128, 129,
        255, 256, 257,
        512, 1000, 1024, 4096, 10000,
        65535, 65536, 65537,
        268435439, 268435440, 268435441,
        536870887, 536870888, 536870889,
        268435456, 536870912, 1073741824,
        1073741823, 1073741824, 1073741825,
        2147483647, 2147483648, 2147483649,
        4294967295, 4294967296, 4294967297,
        9007199254740990, 9007199254740991, 9007199254740992,
        9223372036854775807,
    -1e-15,-1e12, -1e9, -1e6, -1e3,
    -5.0, -4.0, -3.0, -2.0, -1.0,
    -0.0, 0.0,
    1.0, 2.0, 3.0, 4.0, 5.0,
    1e3, 1e6, 1e9, 1e12, 1e-15,
    '-Infinity',
    'Number.MIN_SAFE_INTEGER - 1',
    '-Number.EPSILON',
    '-Number.MIN_VALUE',
    'Number.MIN_VALUE',
    'Number.EPSILON',
    'Number.MAX_SAFE_INTEGER + 1',
    'Infinity',
    'NaN'
    ]
    random_number = random.choice(numbers)
    return random_number


# 生成一个包含数字、字符串等的随机数组
def get_array():
    int_array = [1, 1, 1, 1, 1]
    float_array = [3.14, 1.0]
    str_array = ["Hello"]
    # 定义一个样本数组，包含不同类型的元素
    sample_elements = [int_array, str_array, float_array]
    # 从样本数组中随机选择元素来生成随机数组
    random_array = random.choices(sample_elements)
    return random_array
