all_bs = [
    'Array', 'String', 'Number', 'Object', 'Function', 'Boolean', 'Symbol', 'BigInt', 'RegExp', 'Error', 'EvalError',
    'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'URIError', 'ArrayBuffer',
    'SharedArrayBuffer', 'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array',
    'Float32Array', 'Float64Array', 'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'DataView', 'Date',
    'Promise', 'Proxy', 'Map', 'WeakMap', 'Set', 'WeakSet', 'WeakRef', 'FinalizationRegistry', 'Math', 'JSON', 'Reflect'
]

# 定义 JavaScript 方法及示例参数
methods = {
    'Array': {
        "constructor": [],
        "at": ["tmp_num"],
        "concat": ["tmp_array"],
        "copyWithin": ["tmp_num", "tmp_num"],
        "fill": ["tmp_str"],
        "find": ["element => element === 'example'"],
        "findIndex": ["element => element === 'example'"],
        "findLast": ["element => element === 'example'"],
        "findLastIndex": ["element => element === 'example'"],
        "lastIndexOf": ["tmp_str"],
        "pop": [],
        "push": ["tmp_str"],
        "reverse": [],
        "shift": [],
        "unshift": ["tmp_str"],
        "slice": ["tmp_num", "tmp_num"],
        "sort": [],
        "splice": ["tmp_num", "tmp_num"],
        "includes": ["tmp_str"],
        "indexOf": ["tmp_str"],
        "join": ["tmp_str"],
        "keys": [],
        "entries": [],
        "values": [],
        "forEach": ["element => console.log(element)"],
        "filter": ["element => element.length > 4"],
        "flat": [],
        "flatMap": ["element => [element]"],
        "map": ["element => element.toUpperCase()"],
        "every": ["element => element.length > 4"],
        "some": ["element => element.length > 4"],
        "reduce": ["(accumulator, currentValue) => accumulator + currentValue"],
        "reduceRight": ["(accumulator, currentValue) => accumulator + currentValue"],
        "toReversed": [],
        "toSorted": [],
        "toSpliced": ["tmp_num", "tmp_num"],
        "with": ["tmp_num", "tmp_str"],
        "toLocaleString": [],
        "toString": []
    },
    # 'Array': {
    #     "constructor": [],
    #     "at": [
    #         {
    #             "name": "index",
    #             "type": "integer",
    #             "values": ["NaN", "0", "Infinity", "-Infinity"],
    #             "scopes": [],
    #             "conditions": ["index < 0 or index ≥ len"]
    #         }
    #     ],
    #     "concat": [
    #         {
    #             "name": "items",
    #             "type": "array",
    #             "values": ["Array", "Object", "Primitive"],
    #             "scopes": [],
    #             "conditions": [
    #                 "If an item is an Array and is concat spreadable, its elements are added individually.",
    #                 "If an item is an Array but not concat spreadable, or is an Object, it is added as a single item.",
    #                 "Primitive values are added as single items."
    #             ]
    #         }
    #     ],
    #     "copyWithin": [
    #         {
    #             "name": "target",
    #             "type": "integer",
    #             "values": ["NaN", "Infinity", "-Infinity"],
    #             "scopes": [0],
    #             "conditions": [
    #                 "if target is negative, it is treated as length + target where length is the length of the array"]
    #         },
    #         {
    #             "name": "start",
    #             "type": "integer",
    #             "values": ["NaN", "Infinity", "-Infinity"],
    #             "scopes": [0],
    #             "conditions": ["if start is negative, it is treated as length + start"]
    #         },
    #         {
    #             "name": "end",
    #             "type": "integer",
    #             "values": ["undefined", "NaN", "Infinity", "-Infinity"],
    #             "scopes": [],
    #             "conditions": ["if end is undefined, the length of this value is used",
    #                            "if end is negative, it is treated as length + end"],
    #             "optional": True
    #         }
    #     ],
    #     "fill": [
    #         {
    #             "name": "value",
    #             "type": "any",
    #             "values": ["Any value"],
    #             "scopes": [],
    #             "conditions": [],
    #             "optional": False
    #         },
    #         {
    #             "name": "start",
    #             "type": "integer",
    #             "values": ["0", "positive numbers", "negative numbers", "NaN", "undefined"],
    #             "scopes": [],
    #             "conditions": [
    #                 "if start is undefined, +0 is used",
    #                 "if start is negative, it is treated as length + start",
    #                 "if start is NaN, it is treated as 0"
    #             ],
    #             "optional": True
    #         },
    #         {
    #             "name": "end",
    #             "type": "integer",
    #             "values": ["undefined", "positive numbers", "negative numbers", "NaN"],
    #             "scopes": [],
    #             "conditions": [
    #                 "if end is undefined, the length of the array is used",
    #                 "if end is negative, it is treated as length + end",
    #                 "if end is NaN, it is treated as length"
    #             ],
    #             "optional": True
    #         }
    #     ],
    #     "find": [
    #         {
    #             "name": "predicate",
    #             "type": "function",
    #             "values": ["function"],
    #             "scopes": [],
    #             "conditions": [
    #                 "Called once for each element of the array, in ascending index order, until it finds one where predicate returns a value that coerces to true",
    #                 "If such an element is found, find immediately returns that element value, otherwise returns undefined"
    #             ],
    #             "optional": False
    #         },
    #         {
    #             "name": "thisArg",
    #             "type": "object",
    #             "values": ["any"],
    #             "scopes": [],
    #             "conditions": [
    #                 "Used as the 'this' value for each invocation of the predicate"
    #             ],
    #             "optional": True
    #         }
    #     ],
    #     "findIndex": ["tmp_func"],
    #     "findLast": ["tmp_func"],
    #     "findLastIndex": ["tmp_func"],
    #     "lastIndexOf": ["tmp_str"],
    #     "pop": [],
    #     "push": ["tmp_str"],
    #     "reverse": [],
    #     "shift": [],
    #     "unshift": ["tmp_str"],
    #     "slice": ["tmp_num", "tmp_num"],
    #     "sort": [],
    #     "splice": ["tmp_num", "tmp_num"],
    #     "includes": ["tmp_str"],
    #     "indexOf": ["tmp_str"],
    #     "join": ["tmp_str"],
    #     "keys": [],
    #     "entries": [],
    #     "values": [],
    #     "forEach": ["tmp_func"],
    #     "filter": ["tmp_func"],
    #     "flat": [],
    #     "flatMap": ["tmp_func"],
    #     "map": ["tmp_func"],
    #     "every": ["tmp_func"],
    #     "some": ["tmp_func"],
    #     "reduce": ["tmp_func"],
    #     "reduceRight": ["tmp_func"],
    #     "toReversed": [],
    #     "toSorted": [],
    #     "toSpliced": ["tmp_num", "tmp_num"],
    #     "with": ["tmp_num", "tmp_str"],
    #     "toLocaleString": [],
    #     "toString": []
    # },
    'String': {
        "constructor": [],
        "anchor": ["tmp_str"],
        "at": ["tmp_num"],
        # "at": [
        #     {
        #         "name": "index",
        #         "type": "integer",
        #         "values": ["NaN", "0", "Infinity", "-Infinity", "positive integers", "negative integers"],
        #         "scopes": [],
        #         "conditions": [
        #             "if index ≥ 0, then index is used directly",
        #             "if index < 0, then index is added to the string length"
        #         ]
        #     }
        # ],
        "big": [],
        "blink": [],
        "bold": [],
        "charAt": ["tmp_num"],
        "charAt": [
            {
                "name": "pos",
                "type": "integer",
                "values": ["NaN", "0", "Infinity", "-Infinity", "other integers"],
                "scopes": [],
                "conditions": ["pos < 0 or pos ≥ size"],
                "optional": False,
                "change": True
            }
        ],
        "charCodeAt": ["tmp_num"],
        "codePointAt": ["tmp_num"],
        "concat": ["tmp_str"],
        "endsWith": ["tmp_str"],
        "fontcolor": ["'color'"],
        "fontsize": ["'size'"],
        "fixed": [],
        "includes": ["tmp_str"],
        "indexOf": ["tmp_str"],
        "isWellFormed": [],
        "italics": [],
        "lastIndexOf": ["tmp_str"],
        "link": ["'url'"],
        "localeCompare": ["tmp_str"],
        "match": ["/test/"],
        "matchAll": ["/test/g"],
        "normalize": ["'NFC'"],
        "padEnd": ["tmp_num", "'0'"],
        "padStart": ["tmp_num", "'0'"],
        "repeat": ["tmp_num"],
        "replace": ["/test/", "'replace'"],
        "replaceAll": ["/test/g", "'replace'"],
        "search": ["/test/"],
        "slice": ["tmp_num", "tmp_num"],
        "small": [],
        "split": ["' '", "tmp_num"],
        "strike": [],
        "sub": [],
        "substr": ["tmp_num", "tmp_num"],
        "substring": ["tmp_num", "tmp_num"],
        "sup": [],
        "startsWith": ["tmp_str"],
        "toString": [],
        "toWellFormed": [],
        "trim": [],
        "trimStart": [],
        "trimLeft": [],
        "trimEnd": [],
        "trimRight": [],
        "toLocaleLowerCase": [],
        "toLocaleUpperCase": [],
        "toLowerCase": [],
        "toUpperCase": [],
        "valueOf": []
    },
    'Number': {
        "constructor": [],
        "toExponential": ["tmp_num"],
        "toFixed": ["tmp_num"],
        "toPrecision": ["tmp_num"],
        "toString": ["tmp_num"],
        "valueOf": [],
        "toLocaleString": []
    },
    'Object': {
        "constructor": [],
        "__defineGetter__": ["propName", "getterFunction"],
        "__defineSetter__": ["propName", "setterFunction"],
        "hasOwnProperty": ["propertyName"],
        "__lookupGetter__": ["propertyName"],
        "__lookupSetter__": ["propertyName"],
        "isPrototypeOf": ["object"],
        "propertyIsEnumerable": ["propertyName"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": []
    },
    'Function': {
        "constructor": [],
        "apply": ["thisArg", "argArray"],
        "bind": ["thisArg", "arg1", "arg2", "..."],
        "call": ["thisArg", "arg1", "arg2", "..."],
        "toString": []
    },
    'Boolean': {
        "constructor": [],
        "valueOf": [],
        "toLocaleString": []
    },
    "Symbol": {
        "constructor": [],
        "toString": [],
        "valueOf": []
    },
    "BigInt": {
        "constructor": [],
        "toLocaleString": [],
        "toString": [],
        "valueOf": []
    },
    "RegExp": {
        "constructor": [],
        "exec": ["tmp_str"],
        "compile": [],
        "toString": [],
        "test": []
    },
    "Error": {
        "constructor": [],
        "toString": [],
        "stack": ["tmp_str"]
    },
    "ArrayBuffer": {
        "constructor": [],
        "slice": ["tmp_num", "tmp_num"],
        "resize": ["tmp_num"],
        "transfer": ["destination", "tmp_num"],
        "transferToFixedLength": ["destination", "tmp_num", "tmp_num"]
    },
    "SharedArrayBuffer": {
        "constructor": [],
        "slice": ["tmp_num", "tmp_num"],
        "grow": ["tmp_num"],
    },
    "DataView": {
        "constructor": [],
        "getInt8": ["byteOffset"],
        "setInt8": ["byteOffset", "value"],
        "getUint8": ["byteOffset"],
        "setUint8": ["byteOffset", "value"],
        "getInt16": ["byteOffset"],
        "setInt16": ["byteOffset", "value"],
        "getUint16": ["byteOffset"],
        "setUint16": ["byteOffset", "value"],
        "getInt32": ["byteOffset"],
        "setInt32": ["byteOffset", "value"],
        "getUint32": ["byteOffset"],
        "setUint32": ["byteOffset", "value"],
        "getFloat32": ["byteOffset"],
        "setFloat32": ["byteOffset", "value"],
        "getFloat64": ["byteOffset"],
        "setFloat64": ["byteOffset", "value"],
        "getBigInt64": ["byteOffset"],
        "setBigInt64": ["byteOffset", "value"],
        "getBigUint64": ["byteOffset"],
        "setBigUint64": ["byteOffset", "value"]
    },
    "Date": {
        "constructor": [],
        "toString": [],
        "toDateString": [],
        "toTimeString": [],
        "toISOString": [],
        "toUTCString": [],
        "toGMTString": [],
        "getDate": [],
        "setDate": ["dayValue"],
        "getDay": [],
        "getFullYear": [],
        "setFullYear": ["yearValue", "monthValue"],
        "getHours": [],
        "setHours": ["hourValue"],
        "getMilliseconds": [],
        "setMilliseconds": ["millisecondValue"],
        "getMinutes": [],
        "setMinutes": ["minuteValue"],
        "getMonth": [],
        "setMonth": ["monthValue"],
        "getSeconds": [],
        "setSeconds": ["secondValue"],
        "getTime": [],
        "setTime": [],
        "getTimezoneOffset": [],
        "getUTCDate": [],
        "setUTCDate": ["dayValue"],
        "getUTCDay": [],
        "getUTCFullYear": [],
        "setUTCFullYear": ["yearValue", "monthValue"],
        "getUTCHours": [],
        "setUTCHours": ["hourValue"],
        "getUTCMilliseconds": [],
        "setUTCMilliseconds": ["millisecondValue"],
        "getUTCMinutes": [],
        "setUTCMinutes": ["minuteValue"],
        "getUTCMonth": [],
        "setUTCMonth": ["monthValue"],
        "getUTCSeconds": [],
        "setUTCSeconds": ["secondValue"],
        "valueOf": [],
        "getYear": [],
        "setYear": ["yearValue"],
        "toJSON": [],
        "toLocaleString": [],
        "toLocaleDateString": [],
        "toLocaleTimeString": []
    },
    "Promise": {
        "constructor": [],
        "then": ["onFulfilled", "onRejected"],
        "catch": ["onRejected"],
        "finally": ["onFinally"]
    },
    "Proxy": {
        "constructor": [],
        "__defineGetter__": ["prop", "getter"],
        "__defineSetter__": ["prop", "setter"],
        "hasOwnProperty": ["prop"],
        "__lookupGetter__": ["prop"],
        "__lookupSetter__": ["prop"],
        "isPrototypeOf": ["obj"],
        "propertyIsEnumerable": ["prop"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": []
    },
    "Map": {
        "constructor": [],
        "get": ["key"],
        "set": ["key", "value"],
        "has": ["key"],
        "delete": ["key"],
        "clear": [],
        "entries": [],
        "forEach": ["callback"],
        "keys": [],
        "values": []
    },
    "WeakMap": {
        "constructor": [],
        "delete": ["key"],
        "get": ["key"],
        "set": ["key", "value"],
        "has": ["key"]
    },
    "Set": {
        "constructor": [],
        "has": ["value"],
        "add": ["value"],
        "delete": ["value"],
        "clear": [],
        "entries": [],
        "forEach": ["callback"],
        "values": [],
        "keys": [],
        "union": ["iterable"],
        "intersection": ["iterable"],
        "difference": ["iterable"],
        "symmetricDifference": ["iterable"],
        "isSubsetOf": ["set"],
        "isSupersetOf": ["set"],
        "isDisjointFrom": ["set"]
    },
    "WeakSet": {
        "constructor": [],
        "delete": ["value"],
        "has": ["value"],
        "add": ["value"]
    },
    "WeakRef": {
        "constructor": [],
        "deref": []
    },
    "FinalizationRegistry": {
        "constructor": [],
        "register": ["target", "heldValue", "unregisterToken"],
        "unregister": ["unregisterToken"]
    },
    "Math": {
        "constructor": [],
        "__defineGetter__": ["prop", "getter"],
        "__defineSetter__": ["prop", "setter"],
        "hasOwnProperty": ["prop"],
        "__lookupGetter__": ["prop"],
        "__lookupSetter__": ["prop"],
        "isPrototypeOf": ["obj"],
        "propertyIsEnumerable": ["prop"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": [],
        "abs": ["x"],
        "acos": ["x"],
        "acosh": ["x"],
        "asin": ["x"],
        "asinh": ["x"],
        "atan": ["x"],
        "atanh": ["x"],
        "atan2": ["y", "x"],
        "ceil": ["x"],
        "cbrt": ["x"],
        "expm1": ["x"],
        "clz32": ["x"],
        "cos": ["x"],
        "cosh": ["x"],
        "exp": ["x"],
        "floor": ["x"],
        "fround": ["x"],
        "hypot": ["value1", "value2"],
        "imul": ["x", "y"],
        "log": ["x"],
        "log1p": ["x"],
        "log2": ["x"],
        "log10": ["x"],
        "max": ["value1", "value2"],
        "min": ["value1", "value2"],
        "pow": ["x", "y"],
        "random": [],
        "round": ["x"],
        "sign": ["x"],
        "sin": ["x"],
        "sinh": ["x"],
        "sqrt": ["x"],
        "tan": ["x"],
        "tanh": ["x"],
        "trunc": ["x"]
    },
    "JSON": {
        "constructor": [],
        "__defineGetter__": ["prop", "getter"],
        "__defineSetter__": ["prop", "setter"],
        "hasOwnProperty": ["prop"],
        "__lookupGetter__": ["prop"],
        "__lookupSetter__": ["prop"],
        "isPrototypeOf": ["obj"],
        "propertyIsEnumerable": ["prop"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": [],
        "parse": ["text", "reviver"],
        "stringify": ["value", "replacer", "space"],
        "rawJSON": ["rawValue"],
        "isRawJSON": ["value"]
    },
    "Reflect": {
        "constructor": [],
        "__defineGetter__": ["prop", "getter"],
        "__defineSetter__": ["prop", "setter"],
        "hasOwnProperty": ["prop"],
        "__lookupGetter__": ["prop"],
        "__lookupSetter__": ["prop"],
        "isPrototypeOf": ["obj"],
        "propertyIsEnumerable": ["prop"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": [],
        "defineProperty": ["target", "prop", "descriptor"],
        "deleteProperty": ["target", "prop"],
        "apply": ["target", "thisArg", "argArray"],
        "construct": ["target", "argArray", "newTarget"],
        "get": ["target", "prop", "receiver"],
        "getOwnPropertyDescriptor": ["target", "prop"],
        "getPrototypeOf": ["target"],
        "has": ["target", "prop"],
        "isExtensible": ["target"],
        "ownKeys": ["target"],
        "preventExtensions": ["target"],
        "set": ["target", "prop", "value", "receiver"],
        "setPrototypeOf": ["target", "proto"]
    },
    "SyntaxError": {
        "constructor": []
    },
    "EvalError": {
        "constructor": []
    },
    "TypeError": {
        "constructor": [],
    },
    "Int8Array": {
        "constructor": []
    },
    "Uint8Array": {
        "constructor": []
    },
    "RangeError": {
        "constructor": [],
    },
    "BigInt64Array": {
        "constructor": []
    },
    "Uint32Array": {
        "constructor": []
    },
    "ReferenceError": {
        "constructor": [],
    },
    "Int32Array": {
        "constructor": []
    },
    "Float64Array": {
        "constructor": []
    },
    "URIError": {
        "constructor": [],
        "stack": ["message"]
    },
    "Uint8ClampedArray": {
        "constructor": []
    },
    "Int16Array": {
        "constructor": []
    },
    "Float32Array": {
        "constructor": []
    },
    "Uint16Array": {
        "constructor": []
    },
    "BigUint64Array": {
        "constructor": []
    }

}

attrs = {
    "ArrayBuffer": {
        "byteLength": "undefined",
        "maxByteLength": "undefined",
        "resizable": "undefined",
        "detached": "undefined"
    },
}
