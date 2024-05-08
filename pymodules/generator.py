import string
import random
import basic
import tools

types = ['string', 'number', 'string', 'number', 'string', 'number', 'object', 'object', 'array']
types2 = ['string', 'number']


def get_newname(zdy, names):
    i = 0
    new_name = zdy + str(i)
    while new_name in names:
        i = random.randint(0, 1000)
        new_name = zdy + str(i)
    return new_name


# 定义一个函数来生成随机字符串
def get_string(p, variables, value_range, special_values):
    if p < 0.5:  # 变量
        if variables:
            return random.choice(variables)
    elif 0.5 < p < 1.0:  # 特殊值
        if special_values:
            return random.choice(special_values)
    else:  # 生成一个参数
        # ss = "'" + ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))) + "'"  # 生成一个随机字符串
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))


def get_string2(p):
    # ss = "'" + ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))) + "'"  # 生成一个随机字符串
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))

def get_number(p, variables, value_range, special_values):
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
        -1e-15, -1e12, -1e9, -1e6, -1e3,
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
    if p < 0.4:  # 可转换为number的变量
        if variables:
            return random.choice(variables)
    elif 0.4 < p < 0.6:  # 特殊值
        if special_values:
            return random.choice(special_values)
    elif 0.6 < p < 0.8:  # 特殊值集合
        return random.choice(numbers)
    else:  # 生成一个参数
        if value_range == 'integer':
            return random.randint(-100, 100)  # 随机生成一个整数值
        else:
            return random.uniform(-100, 100)  # 随机生成一个浮点数值


def get_number2(p):
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
        -1e-15, -1e12, -1e9, -1e6, -1e3,
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
    if p < 0.6:
        return random.choice(numbers)
    elif 0.6 < p < 0.8:
        return random.randint(-100, 100)  # 随机生成一个整数值
    else:
        return random.uniform(-100, 100)  # 随机生成一个浮点数值


# 生成一个随机数组
def get_array(p, variables, value_range, special_values, depth):
    if p < 0.5:  # 变量
        if variables:
            return random.choice(variables)
    elif 0.5 < p < 1.0:  # 特殊值
        if special_values:
            return random.choice(special_values)
    else:  # 生成一个数组参数
        array_length = random.randint(0, 10)  # 随机生成数组长度
        array_values = []
        for _ in range(array_length):
            value_type = random.choice(types)
            array_values.append(
                generate_parameter({'type': value_type, 'valueRange': value_range, 'specialValues': special_values},
                                   variables, depth=depth))
        return array_values


def get_array2(p, depth):
    # 生成一个数组参数
    array_length = random.randint(0, 10)  # 随机生成数组长度
    array_values = []
    for _ in range(array_length):
        value_type = random.choice(types)
        new_value = get_random_value(value_type, depth=depth)
        array_values.append(new_value)
    return array_values


def get_object(p, variables, value_range, special_values, depth):
    if p < 0.5:  # 变量
        if variables:
            return random.choice(variables)
    elif 0.5 < p < 1.0:  # 特殊值
        if special_values:
            return random.choice(special_values)
    else:  # 生成一个对象参数
        object_keys = random.choices(string.ascii_lowercase, k=random.randint(1, 5))  # 随机生成一组键
        object_values = [generate_parameter(
            {'type': random.choice(types), 'valueRange': value_range,
             'specialValues': special_values}, variables, depth=depth) for _ in object_keys]
        return dict(zip(object_keys, object_values))


def get_object2(p, depth):
    object_keys = random.choices(string.ascii_lowercase, k=random.randint(1, 5))  # 随机生成一组键
    value_type = random.choice(types)
    object_values = [get_random_value(value_type, depth=depth) for _ in object_keys]
    return dict(zip(object_keys, object_values))


def get_function(p, variables, value_range, special_values, depth):
    if p < 0.5:  # 变量
        return random.choice(variables)
    elif 0.5 < p < 0.5:  # 特殊值
        if special_values:
            return random.choice(special_values)
    else:  # 生成一个函数
        param_name = get_newname('zdy', variables)
        function_name = f'function_{param_name}'
        function_body = """
                var zdy_a = new Array(5);
                zdy_b = {};
                var zdy_c = [];
            """
        function_value = f'function {function_name}(zdy_b) {{ {function_body} }}'

        return function_value


def get_function2(p, variables):
    param_name = get_newname('zdy', variables)
    function_name = f'function_{param_name}'
    function_body = """
            var zdy_a = new Array(5);
            var zdy_b = {};
            var zdy_c = [];
        """
    function_value = f'function {function_name}(zdy_b) {{ {function_body} }}'

    return function_value


def get_random_value(type1, depth=3):
    result = None
    type1 = str(type1).lower()
    p = random.random()

    if depth <= 0:
        type1 = random.choice(types2)
        if type1 == 'string':
            result = get_string2(p)
        elif type1 == 'number':
            result = get_number2(p)
        return result  # 达到深度限制，返回空

    if type1 == 'any':
        type1 = random.choice(types)

    if type1 == 'string':
        result = get_string2(p)
    elif type1 == 'array':
        result = get_array2(p, depth=depth - 1)
    elif type1 == 'number':
        result = get_number2(p)
    elif type1 == 'object':
        result = get_object2(p, depth=depth - 1)

    return result


def generate_parameter(param_info, origin_variables, depth=3):
    param_name = param_info['name']
    param_type = param_info['type'].lower()
    value_range = param_info.get('valueRange', None)
    special_values = param_info.get('specialValues', [])
    optional = param_info.get('optional', False)

    if isinstance(origin_variables, dict):
        variables = origin_variables.get(param_type, [])
    else:
        variables = origin_variables

    p = random.random()
    if isinstance(optional, str):
        optional = tools.format_boolean(optional)

    if optional and p < 0.5:
        return None  # 参数是可选的且随机决定不生成该参数

    if param_type == 'number':
        return get_number(p, variables, value_range, special_values)
    elif param_type == 'string':
        return get_string(p, variables, value_range, special_values)
    elif param_type == 'array':
        return get_array(p, variables, value_range, special_values, depth=depth - 1)
    elif param_type == 'object':
        return get_object(p, variables, value_range, special_values, depth=depth - 1)
    elif param_type == 'function':
        return get_function(p, variables, value_range, special_values, depth=depth - 1)
    else:
        return random.choice(variables)


def generate_parameters(method_info, variables):
    parameters = method_info.get('parameters', [])
    generated_params = []
    for param_info in parameters:
        generated_param = generate_parameter(param_info, variables)
        if generated_param is not None:
            generated_params.append(generated_param)
    return generated_params


def generate_method_call(var_type, method_name, variables):
    method_info = basic.methods2.get(var_type, {}).get(method_name, {})
    parameters = generate_parameters(method_info, variables)
    return f"{method_name}({', '.join(map(str, parameters))})"


# obj['type']['copyWithin']['parameters']==>list[dict(name,type,valueRange,speciaValues,optional)]


def get_API_statement(obj_info, variables, new_name):
    # obj information
    var_name = obj_info['obj']
    var_type = obj_info['type']
    var_methods = obj_info.get('methods', [])
    var_attrs = obj_info.get('attrs', {})

    # method or attr
    chosen = random.choice(["methods", "methods", "attrs"])

    if chosen == "methods":
        try:
            method_name = random.choice(var_methods)
            method_call = generate_method_call(var_type, method_name, variables)
            call_statement = f"\nvar {new_name} = {var_name}.{method_call};\n"
        except:
            call_statement = ""
    else:
        try:
            attr, attr_type = random.choice(list(var_attrs.items()))
            call_statement = f"\nvar {new_name} = {var_name}.{attr};\n"
            call_statement += f"\n{var_name}.{attr} = {get_random_value(attr_type)};\n"
        except:
            try:
                method_name = random.choice(var_methods)
                method_call = generate_method_call(var_type, method_name, variables)
                call_statement = f"\nlet {new_name} = {var_name}.{method_call};\n"
            except:
                call_statement = ""
    print(call_statement)
    return call_statement


###################################################################
def adjust(new_statement, intervalend_varnames, interval_end):
    # 调整
    change_p = 0.5
    for n in range(3):
        # random.shuffle(intervalend_varnames[interval_end])
        ran = random.random()
        if "tmp_number" in new_statement:
            # Number
            try:
                if ran < change_p:
                    # new_arg = random.choice(obj_name8type['Number'])
                    new_arg = random.choice(intervalend_varnames[interval_end])
                else:
                    new_arg = get_random_value('number')
            except:
                new_arg = get_random_value('number')
            # 替换
            new_statement = new_statement.replace("tmp_number", str(new_arg), 1)
            pass
        elif "tmp_array" in new_statement:
            # Array
            try:
                if ran < change_p:
                    # new_array = random.choice(obj_name8type['Array'])
                    new_array = random.choice(intervalend_varnames[interval_end])
                else:
                    new_array = get_random_value('array')
            except:
                new_array = get_random_value('array')
            # 替换
            new_statement = new_statement.replace("tmp_array", str(new_array), 1)
        elif "tmp_string" in new_statement:
            # String
            try:
                if ran < change_p:
                    new_arg = random.choice(intervalend_varnames[interval_end])
                else:
                    new_arg = get_random_value('string')
            except:
                new_arg = get_random_value('string')
            # 替换
            new_statement = new_statement.replace("tmp_string", "'{}'".format(str(new_arg)), 1)
        elif "tmp_object" in new_statement:
            # Object
            try:
                if ran < change_p:
                    new_arg = random.choice(intervalend_varnames[interval_end])
                else:
                    new_arg = get_random_value('object')
            except:
                new_arg = get_random_value('object')
            # 替换
            new_statement = new_statement.replace("tmp_object", str(new_arg), 1)
        elif "tmp_function" in new_statement:
            # Function
            try:
                if ran < change_p:
                    new_arg = random.choice(intervalend_varnames[interval_end])
                else:
                    new_arg = get_function2(1, intervalend_varnames[interval_end])
            except:
                new_arg = get_function2(1, intervalend_varnames[interval_end])
            # 替换
            new_statement = new_statement.replace("tmp_function", str(new_arg), 1)
        elif "tmp_any" in new_statement:
            try:
                new_arg = random.choice(intervalend_varnames[interval_end])
            except:
                new_arg = get_random_value('any')
            # 替换
            new_statement = new_statement.replace("tmp_any", str(new_arg), 1)
        # 未完待续
    # print(new_statement)
    return new_statement


def get_property_call(new_var, obj):
    # 选择obj
    var_name = obj['obj']

    # method or attr
    member_type = random.choice(["methods", "methods", "methods", "methods", "attrs"])
    # member_type = random.choice(["methods"])
    if member_type == "methods":
        try:
            chosen_method = random.choice(obj["methods"])
            call_statement = f"\nlet {new_var} = {var_name}.{chosen_method};\n"
        except:
            call_statement = ""
    else:
        try:
            chosen_attr = random.choice(list(obj[member_type].keys()))
            call_statement = f"\nlet {new_var} = {var_name}.{chosen_attr};\n"
            type = obj[member_type][chosen_attr]
            value = get_random_value(obj[member_type][chosen_attr])
            if value:
                if type.lower() == 'string':
                    value = "'" + value + "'"
                call_statement += f"\n{var_name}.{chosen_attr} = {value};\n"
        except:
            try:
                chosen_method = random.choice(obj["methods"])
                call_statement = f"\nlet {new_var} = {var_name}.{chosen_method};\n"
            except:
                call_statement = ""

    return call_statement


def get_call_statements(methods, obj_type):
    # methods ==> var_dict["methods"]
    call_statements = []
    if obj_type in list(basic.methods.keys()):
        typed_methods = basic.methods[obj_type]
        items = list(typed_methods.items())
        b = list(typed_methods.keys())
        for a in items:
            args = ", ".join(a[1])
            call_statement = f"{a[0]}({args})"
            # call_statement = f"{a[0]}()"
            call_statements.append(call_statement)
        for method in methods:
            if method == 'crash' or method == 'oomTest':
                # print(method)
                continue
            if method not in b:
                call_statements.append(f"{method}()")
    else:
        call_statements.append(f"constructor()")
                # print(obj_type, method)
    # 输出生成的调用语句
    # for statement in call_statements:
    #     print(statement)
    return call_statements


def get_random_args(add_list):
    arg_type = add_list + ['tmp_number', 'tmp_string', 'tmp_object', 'tmp_any']
    arg_num = random.choice([0, 1, 2])
    args = ", ".join(random.sample(arg_type, arg_num))
    return args


def get_new_statement_obj(engine_name, new_var, obj):
    p = random.random()
    if engine_name == 'js' and p < 0.6:  # Spidermonkey
        args = get_random_args(basic.newglobal)
        if p < 0.3:
            sm_func = random.choice(basic.newglobal)
            new_statement = f"\nlet {new_var} = {sm_func}({args});\n"
        else:
            basic_methods = list(basic.methods.get(obj['type'], {"constructor": []}).keys())
            methods = basic_methods
            chosen_method = f"{str(random.choice(methods))}({args})"
            new_statement = f"\nlet {new_var} = {obj['obj']}.{chosen_method};\n"
    else:
        call_type = random.choice(['static', 'normal', 'normal', 'normal'])
        if call_type == 'static':
            member_type = random.choice(["methods", "methods", "attrs"])
            if member_type == "methods":
                static_method = random.choice(list(basic.static_methods.get(engine_name, {}).keys()))
                args = get_random_args([])
                new_statement = f"\nlet {new_var} = {static_method}({args});\n"
            else:
                static_attr = random.choice(list(basic.static_attrs.get(engine_name, {}).keys()))
                new_statement = f"\nlet {new_var} = {static_attr};\n"
                type = basic.static_attrs.get(engine_name, {}).get(static_attr, "")
                value = get_random_value(type)
                if value:
                    if type.lower() == 'string':
                        value = "'" + value + "'"
                    new_statement += f"\n{static_attr} = {value};\n"
        else:
            # need instance
            # 符合规范
            new_statement = get_property_call(new_var, obj)
    # print(new_statement)
    return new_statement


def get_new_statement(engine_name, new_var):  # 只能调用静态函数
    p = random.random()
    if engine_name == 'js' and p < 0.6:  # Spidermonkey
        args = get_random_args(basic.newglobal)
        sm_func = random.choice(basic.newglobal)
        new_statement = f"\nlet {new_var} = {sm_func}({args});\n"
    else:
        member_type = random.choice(["methods", "methods", "attrs"])
        if member_type == "methods":
            args = get_random_args([])
            static_method = random.choice(list(basic.static_methods.get(engine_name, {}).keys()))
            new_statement = f"\nlet {new_var} = {static_method}({args});\n"
        else:
            static_attr = random.choice(list(basic.static_attrs.get(engine_name, {}).keys()))
            new_statement = f"\nlet {new_var} = {static_attr};\n"
            type = basic.static_attrs.get(engine_name, {}).get(static_attr, "")
            value = get_random_value(type)
            if value:
                if type.lower() == 'string':
                    value = "'" + value + "'"
                new_statement += f"\n{static_attr} = {value};\n"
    # print(new_statement)
    return new_statement


if __name__ == '__main__':

    for n in range(2000):
        a = get_random_value('string', depth=3)
        print(a)
