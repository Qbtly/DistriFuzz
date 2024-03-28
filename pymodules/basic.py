all_bs = [
    'Array', 'String', 'Number', 'Object', 'Function', 'Boolean', 'Symbol', 'BigInt', 'RegExp', 'Error', 'EvalError',
    'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'URIError', 'ArrayBuffer',
    'SharedArrayBuffer', 'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array',
    'Float32Array', 'Float64Array', 'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'DataView', 'Date',
    'Promise', 'Proxy', 'Map', 'WeakMap', 'Set', 'WeakSet', 'WeakRef', 'FinalizationRegistry', 'Math', 'JSON', 'Reflect'
]

# obj['type']['copyWithin']['parameters']==>list[dict(name,type,valueRange,speciaValues,optional)]
methods2 = {
    'Array': {
        "constructor": [],
        "copyWithin": {
            "methodName": "Array.copyWithin",
            "parameters": [
                {
                    "name": "target",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["NaN", "Infinity", "-Infinity"],
                    "optional": False
                },
                {
                    "name": "start",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["NaN", "Infinity", "-Infinity"],
                    "optional": False
                },
                {
                    "name": "end",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["undefined", "NaN", "Infinity", "-Infinity"],
                    "optional": True
                }
            ],
            "changesVariableState": False
        },
        "at": {
            "methodName": "Array.at",
            "parameters": [
                {
                    "name": "index",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["NaN", "Infinity", "-Infinity"],
                    "optional": False
                }
            ],
            "changesVariableState": False
        },
        "concat": {
            "methodName": "Array.concat",
            "parameters": [
                {
                    "name": "arrays",
                    "type": "Array",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                }
            ],
            "changesVariableState": False
        },
        "fill": {
            "methodName": "Array.fill",
            "parameters": [
                {
                    "name": "value",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                },
                {
                    "name": "start",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["NaN", "Infinity", "-Infinity"],
                    "optional": True
                },
                {
                    "name": "end",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["NaN", "Infinity", "-Infinity"],
                    "optional": True
                }
            ],
            "changesVariableState": True
        },
        "find": {
            "methodName": "Array.find",
            "parameters": [
                {
                    "name": "callback",
                    "type": "Function",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                },
                {
                    "name": "thisArg",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": True
                }
            ],
            "changesVariableState": False
        },
        "findIndex": {
            "methodName": "Array.findIndex",
            "parameters": [
                {
                    "name": "callback",
                    "type": "Function",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                },
                {
                    "name": "thisArg",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": True
                }
            ],
            "changesVariableState": False
        },
        "findLast": {
            "methodName": "Array.findLast",
            "parameters": [
                {
                    "name": "callback",
                    "type": "Function",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                },
                {
                    "name": "thisArg",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": True
                }
            ],
            "changesVariableState": False
        },
        "findLastIndex": {
            "methodName": "Array.findLastIndex",
            "parameters": [
                {
                    "name": "callback",
                    "type": "Function",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                },
                {
                    "name": "thisArg",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": True
                }
            ],
            "changesVariableState": False
        },
        "lastIndexOf": {
            "methodName": "Array.lastIndexOf",
            "parameters": [
                {
                    "name": "searchElement",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": True
                },
                {
                    "name": "fromIndex",
                    "type": "number",
                    "valueRange": "integer",
                    "specialValues": ["NaN", "Infinity", "-Infinity"],
                    "optional": True
                }
            ],
            "changesVariableState": False
        },
        "pop": {
            "methodName": "Array.pop",
            "parameters": [],
            "changesVariableState": True
        },
        "push": {
            "methodName": "Array.push",
            "parameters": [
                {
                    "name": "element1",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": False
                },
                {
                    "name": "element2",
                    "type": "any",
                    "valueRange": "any",
                    "specialValues": [],
                    "optional": True
                }
            ],
            "changesVariableState": True
        },
        "reverse": {
            "methodName": "Array.reverse",
            "parameters": [],
            "changesVariableState": True
        },
        "shift": {
            "methodName": "Array.shift",
            "parameters": [],
            "changesVariableState": True
        }

    }
}

# 定义 JavaScript 方法及示例参数
methods = {
    'Array': {
        "constructor": [],
        "at": ["tmp_number"],
        "concat": ["tmp_array"],
        "copyWithin": ["tmp_number", "tmp_number"],
        "fill": ["tmp_string"],
        "find": ["element => element === 'example'"],
        "findIndex": ["element => element === 'example'"],
        "findLast": ["element => element === 'example'"],
        "findLastIndex": ["element => element === 'example'"],
        "lastIndexOf": ["tmp_string"],
        "pop": [],
        "push": ["tmp_string"],
        "reverse": [],
        "shift": [],
        "unshift": ["tmp_string"],
        "slice": ["tmp_number", "tmp_number"],
        "sort": [],
        "splice": ["tmp_number", "tmp_number"],
        "includes": ["tmp_string"],
        "indexOf": ["tmp_string"],
        "join": ["tmp_string"],
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
        "toSpliced": ["tmp_number", "tmp_number"],
        "with": ["tmp_number", "tmp_string"],
        "toLocaleString": [],
        "toString": []
    },

    'String': {
        "constructor": [],
        "anchor": ["tmp_string"],
        "at": ["tmp_number"],
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
        "charAt": ["tmp_number"],
        # "charAt": [
        #     {
        #         "name": "pos",
        #         "type": "integer",
        #         "values": ["NaN", "0", "Infinity", "-Infinity", "other integers"],
        #         "scopes": [],
        #         "conditions": ["pos < 0 or pos ≥ size"],
        #         "optional": False,
        #         "change": True
        #     }
        # ],
        "charCodeAt": ["tmp_number"],
        "codePointAt": ["tmp_number"],
        "concat": ["tmp_string"],
        "endsWith": ["tmp_string"],
        "fontcolor": ["tmp_string"],
        "fontsize": ["tmp_string"],
        "fixed": [],
        "includes": ["tmp_string"],
        "indexOf": ["tmp_string"],
        "isWellFormed": [],
        "italics": [],
        "lastIndexOf": ["tmp_string"],
        "link": ["'url'"],
        "localeCompare": ["tmp_string"],
        "match": ["/test/"],
        "matchAll": ["/test/g"],
        "normalize": ["tmp_string"],
        "padEnd": ["tmp_number", "tmp_string"],
        "padStart": ["tmp_number", "tmp_string"],
        "repeat": ["tmp_number"],
        "replace": ["/test/", "tmp_string"],
        "replaceAll": ["/test/g", "tmp_string"],
        "search": ["/test/"],
        "slice": ["tmp_number", "tmp_number"],
        "small": [],
        "split": ["' '", "tmp_number"],
        "strike": [],
        "sub": [],
        "substr": ["tmp_number", "tmp_number"],
        "substring": ["tmp_number", "tmp_number"],
        "sup": [],
        "startsWith": ["tmp_string"],
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
        "toExponential": ["tmp_number"],
        "toFixed": ["tmp_number"],
        "toPrecision": ["tmp_number"],
        "toString": ["tmp_number"],
        "valueOf": [],
        "toLocaleString": []
    },
    "Object": {
        "constructor": [],
        "__defineGetter__": ["tmp_string", "tmp_function"],
        "__defineSetter__": ["tmp_string", "tmp_function"],
        "hasOwnProperty": ["tmp_string"],
        "__lookupGetter__": ["tmp_string"],
        "__lookupSetter__": ["tmp_string"],
        "isPrototypeOf": ["tmp_object"],
        "propertyIsEnumerable": ["tmp_string"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": []
    },
    "Function": {
        "constructor": [],
        "apply": ["tmp_any", "tmp_array"],
        "bind": ["tmp_any", "tmp_any", "tmp_any", "..."],
        "call": ["tmp_any", "tmp_any", "tmp_any", "..."],
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
        "exec": ["tmp_string"],
        "compile": [],
        "toString": [],
        "test": []
    },
    "Error": {
        "constructor": [],
        "toString": [],
        "stack": ["tmp_string"]
    },
    "ArrayBuffer": {
        "constructor": [],
        "slice": ["tmp_number", "tmp_number"],
        "resize": ["tmp_number"],
        "transfer": ["destination", "tmp_number"],
        "transferToFixedLength": ["destination", "tmp_number", "tmp_number"]
    },
    "SharedArrayBuffer": {
        "constructor": [],
        "slice": ["tmp_number", "tmp_number"],
        "grow": ["tmp_number"],
    },
    "DataView": {
        "constructor": [],
        "getInt8": ["tmp_number"],
        "setInt8": ["tmp_number", "tmp_number"],
        "getUint8": ["tmp_number"],
        "setUint8": ["tmp_number", "tmp_number"],
        "getInt16": ["tmp_number"],
        "setInt16": ["tmp_number", "tmp_number"],
        "getUint16": ["tmp_number"],
        "setUint16": ["tmp_number", "tmp_number"],
        "getInt32": ["tmp_number"],
        "setInt32": ["tmp_number", "tmp_number"],
        "getUint32": ["tmp_number"],
        "setUint32": ["tmp_number", "tmp_number"],
        "getFloat32": ["tmp_number"],
        "setFloat32": ["tmp_number", "tmp_number"],
        "getFloat64": ["tmp_number"],
        "setFloat64": ["tmp_number", "tmp_number"],
        "getBigInt64": ["tmp_number"],
        "setBigInt64": ["tmp_number", "tmp_bigint"],
        "getBigUint64": ["tmp_number"],
        "setBigUint64": ["tmp_number", "tmp_bigint"]
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
        "setDate": ["tmp_number"],
        "getDay": [],
        "getFullYear": [],
        "setFullYear": ["tmp_number", "tmp_number"],
        "getHours": [],
        "setHours": ["tmp_number"],
        "getMilliseconds": [],
        "setMilliseconds": ["tmp_number"],
        "getMinutes": [],
        "setMinutes": ["tmp_number"],
        "getMonth": [],
        "setMonth": ["tmp_number"],
        "getSeconds": [],
        "setSeconds": ["tmp_number"],
        "getTime": [],
        "setTime": [],
        "getTimezoneOffset": [],
        "getUTCDate": [],
        "setUTCDate": ["tmp_number"],
        "getUTCDay": [],
        "getUTCFullYear": [],
        "setUTCFullYear": ["tmp_number", "tmp_number"],
        "getUTCHours": [],
        "setUTCHours": ["tmp_number"],
        "getUTCMilliseconds": [],
        "setUTCMilliseconds": ["tmp_number"],
        "getUTCMinutes": [],
        "setUTCMinutes": ["tmp_number"],
        "getUTCMonth": [],
        "setUTCMonth": ["tmp_number"],
        "getUTCSeconds": [],
        "setUTCSeconds": ["tmp_number"],
        "valueOf": [],
        "getYear": [],
        "setYear": ["tmp_number"],
        "toJSON": [],
        "toLocaleString": [],
        "toLocaleDateString": [],
        "toLocaleTimeString": []
    },
    "Promise": {
        "constructor": [],
        "then": ["tmp_function", "tmp_function"],
        "catch": ["tmp_function"],
        "finally": ["tmp_function"]
    },
    "Proxy": {
        "constructor": [],
        "__defineGetter__": ["tmp_string", "tmp_function"],
        "__defineSetter__": ["tmp_string", "tmp_function"],
        "hasOwnProperty": ["tmp_string"],
        "__lookupGetter__": ["tmp_string"],
        "__lookupSetter__": ["tmp_string"],
        "isPrototypeOf": ["tmp_object"],
        "propertyIsEnumerable": ["tmp_string"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": []
    },
    "Map": {
        "constructor": [],
        "get": ["tmp_any"],
        "set": ["tmp_any", "tmp_any"],
        "has": ["tmp_any"],
        "delete": ["tmp_any"],
        "clear": [],
        "entries": [],
        "forEach": ["tmp_function"],
        "keys": [],
        "values": []
    },
    "WeakMap": {
        "constructor": [],
        "delete": ["tmp_any"],
        "get": ["tmp_any"],
        "set": ["tmp_any", "tmp_any"],
        "has": ["tmp_any"]
    },
    "Set": {
        "constructor": [],
        "has": ["tmp_any"],
        "add": ["tmp_any"],
        "delete": ["tmp_any"],
        "clear": [],
        "entries": [],
        "forEach": ["tmp_function"],
        "values": [],
        "keys": [],
        "union": ["tmp_any"],
        "intersection": ["tmp_any"],
        "difference": ["tmp_any"],
        "symmetricDifference": ["tmp_any"],
        "isSubsetOf": ["tmp_any"],
        "isSupersetOf": ["tmp_any"],
        "isDisjointFrom": ["tmp_any"]
    },
    "WeakSet": {
        "constructor": [],
        "delete": ["tmp_any"],
        "has": ["tmp_any"],
        "add": ["tmp_any"]
    },
    "WeakRef": {
        "constructor": [],
        "deref": []
    },
    "FinalizationRegistry": {
        "constructor": [],
        "register": ["tmp_any", "tmp_any", "tmp_any"],
        "unregister": ["tmp_any"]
    },
    "Math": {
        "constructor": [],
        "__defineGetter__": ["tmp_string", "tmp_function"],
        "__defineSetter__": ["tmp_string", "tmp_function"],
        "hasOwnProperty": ["tmp_string"],
        "__lookupGetter__": ["tmp_string"],
        "__lookupSetter__": ["tmp_string"],
        "isPrototypeOf": ["tmp_object"],
        "propertyIsEnumerable": ["tmp_string"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": [],
        "abs": ["tmp_number"],
        "acos": ["tmp_number"],
        "acosh": ["tmp_number"],
        "asin": ["tmp_number"],
        "asinh": ["tmp_number"],
        "atan": ["tmp_number"],
        "atanh": ["tmp_number"],
        "atan2": ["tmp_number", "tmp_number"],
        "ceil": ["tmp_number"],
        "cbrt": ["tmp_number"],
        "expm1": ["tmp_number"],
        "clz32": ["tmp_number"],
        "cos": ["tmp_number"],
        "cosh": ["tmp_number"],
        "exp": ["tmp_number"],
        "floor": ["tmp_number"],
        "fround": ["tmp_number"],
        "hypot": ["tmp_number", "tmp_number"],
        "imul": ["tmp_number", "tmp_number"],
        "log": ["tmp_number"],
        "log1p": ["tmp_number"],
        "log2": ["tmp_number"],
        "log10": ["tmp_number"],
        "max": ["tmp_number", "tmp_number"],
        "min": ["tmp_number", "tmp_number"],
        "pow": ["tmp_number", "tmp_number"],
        "random": [],
        "round": ["tmp_number"],
        "sign": ["tmp_number"],
        "sin": ["tmp_number"],
        "sinh": ["tmp_number"],
        "sqrt": ["tmp_number"],
        "tan": ["tmp_number"],
        "tanh": ["tmp_number"],
        "trunc": ["tmp_number"]
    },
    "JSON": {
        "constructor": [],
        "__defineGetter__": ["tmp_string", "tmp_function"],
        "__defineSetter__": ["tmp_string", "tmp_function"],
        "hasOwnProperty": ["tmp_string"],
        "__lookupGetter__": ["tmp_string"],
        "__lookupSetter__": ["tmp_string"],
        "isPrototypeOf": ["tmp_object"],
        "propertyIsEnumerable": ["tmp_string"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": [],
        "parse": ["tmp_string", "tmp_function"],
        "stringify": ["tmp_json_value", "tmp_function | tmp_array", "tmp_string | tmp_number"],
        "rawJSON": ["tmp_json_value"],
        "isRawJSON": ["tmp_json_value"]
    },
    "Reflect": {
        "constructor": [],
        "__defineGetter__": ["tmp_string", "tmp_function"],
        "__defineSetter__": ["tmp_string", "tmp_function"],
        "hasOwnProperty": ["tmp_string"],
        "__lookupGetter__": ["tmp_string"],
        "__lookupSetter__": ["tmp_string"],
        "isPrototypeOf": ["tmp_object"],
        "propertyIsEnumerable": ["tmp_string"],
        "toString": [],
        "valueOf": [],
        "toLocaleString": [],
        "defineProperty": ["tmp_any", "tmp_string", "tmp_any"],
        "deleteProperty": ["tmp_any", "tmp_string"],
        "apply": ["tmp_any", "tmp_any", "tmp_array"],
        "construct": ["tmp_any", "tmp_array", "tmp_any"],
        "get": ["tmp_any", "tmp_any", "tmp_any"],
        "getOwnPropertyDescriptor": ["tmp_any", "tmp_any"],
        "getPrototypeOf": ["tmp_any"],
        "has": ["tmp_any", "tmp_any"],
        "isExtensible": ["tmp_any"],
        "ownKeys": ["tmp_any"],
        "preventExtensions": ["tmp_any"],
        "set": ["tmp_any", "tmp_any", "tmp_any", "tmp_any"],
        "setPrototypeOf": ["tmp_any", "tmp_any"]
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
        "stack": ["tmp_string"]
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
