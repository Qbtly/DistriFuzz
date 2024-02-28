integer = [
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

b = [
   'Object', 'Array', 'Function', 'String', 'Boolean', 'Number', 'Symbol', 'BigInt', 'RegExp', 'Error', 'EvalError',
   'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'AggregateError', 'URIError', 'ArrayBuffer',
   'SharedArrayBuffer', 'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array',
   'Float32Array', 'Float64Array', 'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'DataView', 'Date',
   'Promise', 'Proxy', 'Map', 'WeakMap', 'Set', 'WeakSet', 'WeakRef', 'FinalizationRegistry', 'Math', 'JSON', 'Reflect',
   'isNaN', 'isFinite', 'eval', 'parseInt', 'parseFloat', 'globalThis', 'undefined', 'NaN', 'Infinity', 'decodeURI',
   'decodeURIComponent', 'encodeURI', 'encodeURIComponent', 'escap', 'unescape','__proto__', 'constructor', 'valueOf', 'toString'
]
all_bs = [
   'Object', 'Array', 'Function', 'String', 'Boolean', 'Number', 'Symbol', 'BigInt', 'RegExp', 'Error', 'EvalError',
   'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'AggregateError', 'URIError', 'ArrayBuffer',
   'SharedArrayBuffer', 'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array',
   'Float32Array', 'Float64Array', 'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'DataView', 'Date',
   'Promise', 'Proxy', 'Map', 'WeakMap', 'Set', 'WeakSet', 'WeakRef', 'FinalizationRegistry', 'Math', 'JSON', 'Reflect'
]

TypedArray = ["Uint8Array", "Int8Array", "Uint16Array", "Int16Array", "Uint32Array", "Int32Array", "Float32Array", "Float64Array", "Uint8ClampedArray", "BigInt64Array", "BigUint64Array"]
TypedArray_b = ['buffer', 'byteLength', 'byteOffset', 'length', 'copyWithin', 'entries', 'every', 'fill', 'find',
                   'findIndex', 'forEach', 'includes', 'indexOf', 'join', 'keys', 'lastIndexOf', 'reduce',
                   'reduceRight', 'reverse', 'set', 'some', 'sort', 'values', 'filter', 'map', 'slice', 'subarray',
                   'toString', 'toLocaleString']
Errors = ['EvalError', 'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'AggregateError', 'URIError']
Errors_b = ['message', 'cause', 'name', 'stack']

def all_builtins():
    all_builtin = {
        'RegExp': ['flags', 'dotAll', 'global', 'ignoreCase', 'multiline', 'source', 'sticky', 'unicode', 'compile', 'exec', 'test'],
        'DataView': ['buffer', 'byteLength', 'byteOffset', 'getInt8', 'getUint8', 'getInt16', 'getUint16', 'getInt32', 'getUint32', 'getFloat32', 'getFloat64', 'getBigInt64', 'setInt8', 'setUint8', 'setInt16', 'setUint16', 'setInt32', 'setUint32', 'setFloat32', 'setFloat64', 'setBigInt64'],
        'Proxy': [],
        'Map': ['size', 'clear', 'delete', 'entries', 'forEach', 'get', 'has', 'keys', 'set', 'values'],
        'WeakMap': ['delete', 'get', 'has', 'set'],
        'Set': ['size', 'add', 'clear', 'delete', 'entries', 'forEach', 'has', 'keys', 'values'],
        'WeakSet': ['add', 'delete', 'has'],
        'WeakRef': ['deref'],
        'FinalizationRegistry': ['register','unregister'],
        
        'Error': ['message', 'cause', 'name', 'stack'], 
        'Intl':['getCanonicalLocales', 'supportedValuesOf', 'Collator', 'DateTimeFormat', 'ListFormat', 'NumberFormat', 'PluralRules', 'RelativeTimeFormat', 'Segmenter'],

        'JSON': ['parse','stringify'],
        'Reflect': ['apply', 'construct', 'defineProperty', 'deleteProperty', 'get', 'getOwnPropertyDescriptor', 'getPrototypeOf', 'has', 'isExtensible', 'ownKeys', 'preventExtensions', 'set', 'setPrototypeOf'],
        'Math': ['E', 'LN2', 'LN10', 'LOG10E', 'LOG2E', 'PI', 'SQRT1_2', 'SQRT2', 'abs', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'atan2', 'cbrt', 'ceil', 'clz32',
                 'cos', 'cosh', 'exp', 'expm1', 'floor', 'fround', 'hypot', 'imul', 'log', 'log1p', 'log10', 'log2', 'max',
                 'min', 'pow', 'random', 'round', 'sign', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc'],
        
        'Function': ['length', 'arguments', 'caller', 'displayName', 'prototype', 'name', 'apply', 'call', 'bind'],
        'Object': ['assign', 'create', 'defineProperty', 'configurable', 'writable', 'enumerable', 'value', 'get', 'set', 'defineProperties', 'entries', 'freeze', 'fromEntries', 'getOwnPropertyDescriptor', 'getOwnPropertyDescriptors', 'getOwnPropertyNames', 'getOwnPropertySymbols', 'getPrototypeOf', 'groupBy', 'hasOwn', 'is', 'isExtensible', 'isFrozen', 'isSealed', 'keys', 'preventExtensions', 'seal', 'setPrototypeOf', 'values', 'prototype', 'hasOwnProperty', 'isPrototypeOf', 'propertyIsEnumerable', 'toLocaleString', '__lookupSetter__', '__lookupGetter__', '__defineSetter__', '__defineGetter__'],
        'Symbol': ['iterator', 'asyncIterator', 'match', 'matchAll', 'replace', 'search', 'split', 'hasInstance', 'isConcatSpreadable', 'unscopables', 'species', 'toPrimitive', 'toStringTag', 'for', 'keyFor', 'description'],
        'Boolean': ['prototype'],
        
        'Promise': ['resolve', 'reject', 'all', 'any', 'race', 'allSettled', 'catch', 'then', 'finally','prototype'],
        'Array': ['from', 'isArray', 'of', 'prototype', 'length', 'at', 'copyWithin', 'entries', 'every', 'fill', 'find', 'findIndex', 'forEach', 'includes', 'indexOf', 'join', 'keys', 'lastIndexOf', 'reduce', 'reduceRight', 'reverse', 'some', 'sort', 'values', 'pop', 'push', 'shift', 'splice', 'unshift', 'concat', 'filter', 'map', 'slice', 'flat', 'flatMap', 'toString', 'toLocaleString'],
        'String': ['fromCharCode', 'fromCodePoint', 'raw', 'prototype', 'length', 'charAt', 'charCodeAt', 'codePointAt', 'concat', 'includes', 'endsWith', 'indexOf', 'lastIndexOf', 'match', 'matchAll', 'normalize', 'padEnd', 'padStart', 'repeat', 'replace', 'replaceAll', 'search', 'slice', 'split', 'startsWith', 'substring', 'trim', 'trimStart', 'trimLeft', 'trimEnd', 'trimRight', 'toLowerCase', 'toUpperCase', 'localeCompare'],
        'BigInt': ['asIntN', 'asUintN', 'prototype', 'toString', 'toLocaleString', 'valueOf'],
        'Number': ['EPSILON', 'MAX_SAFE_INTEGER', 'MAX_VALUE', 'MIN_SAFE_INTEGER', 'MIN_VALUE', 'NaN', 'NEGATIVE_INFINITY', 'POSITIVE_INFINITY', 'isNaN', 'isFinite', 'isInteger', 'isSafeInteger', 'prototype', ],
        'Date': ['UTC', 'now', 'parse', 'prototype', 'toISOString', 'toDateString', 'toTimeString', 'toLocaleString', 'toLocaleDateString', 'toLocaleTimeString', 'getTime', 'getFullYear', 'getUTCFullYear', 'getMonth', 'getUTCMonth', 'getDate', 'getUTCDate', 'getDay', 'getUTCDay', 'getHours', 'getUTCHours', 'getMinutes', 'getUTCMinutes', 'getSeconds', 'getUTCSeconds', 'getMilliseconds', 'getUTCMilliseconds', 'getTimezoneOffset', 'getYear', 'now', 'setTime', 'setMilliseconds', 'setUTCMilliseconds', 'setSeconds', 'setUTCSeconds', 'setMinutes', 'setUTCMinutes', 'setHours', 'setUTCHours', 'setDate', 'setUTCDate', 'setMonth', 'setUTCMonth', 'setFullYear', 'setUTCFullYear', 'setYear', 'toJSON', 'toUTCString', 'toGMTString'],
        'ArrayBuffer': ['isView','prototype','byteLength', 'maxByteLength', 'resizable', 'resize', 'slice', 'transfer'],
        'SharedArrayBuffer': ['prototype','byteLength', 'maxByteLength', 'growable', 'grow', 'slice']
    }
    for t in TypedArray:
        all_builtin[t] = TypedArray_b
    for e in Errors:
        all_builtin[e] = Errors_b
    return all_builtin
        
        
huohu = {'InternalError': ['columnNumber', 'fileName', 'lineNumber']}

tongyong = ['globalThis', 'eval', 'isNaN', 'isFinite', 'parseInt', 'parseFloat', 'decodeURI', 'decodeURIComponent',
            'encodeURI', 'encodeURIComponent', 'escap', 'unescape', 'undefined', 'NaN', 'Infinity', '__proto__',
            'constructor', 'valueOf', 'toString', 'toLocaleString', 'Object', 'Array', 'Function', 'String',
            'Boolean', 'Number', 'Symbol', 'BigInt', 'RegExp', 'Error', 'EvalError', 'RangeError', 'ReferenceError',
            'SyntaxError', 'TypeError', 'AggregateError', 'URIError', 'ArrayBuffer', 'SharedArrayBuffer', 'Uint8Array',
            'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array', 'Float32Array', 'Float64Array',
            'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'DataView', 'Date', 'Promise', 'Proxy', 'Map',
            'WeakMap', 'Set', 'WeakSet', 'WeakRef', 'FinalizationRegistry', 'Math', 'JSON', 'Reflect']

constructors = ['Math', 'Function', 'Object', 'Symbol', 'Boolean', 'Promise', 'Array', 'String', 'BigInt', 'Number', 'Date', 'ArrayBuffer', 'SharedArrayBuffer']

statement = [
    "var t = new Array(1,2,3);",
    "var a = new ArrayBuffer(8);",
    "var buffer = new ArrayBuffer(0x10000);",
    "var n = new Number(a[item]);",
    "var q = new Intl.NumberFormat(['en']);",
    "var q = new Intl.Collator();"
"(Array.prototype[('X') + (5)]) = true;",
    "let call = new Proxy(Function.prototype.call, {}); ",
    "new Function(code)();"

]
se = ["() => {}",]