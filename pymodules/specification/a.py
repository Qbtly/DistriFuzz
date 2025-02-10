    #     // Possible return values of the 'typeof' operator.
    # public static let jsTypeNames = ["undefined", "boolean", "number", "string", "symbol", "function", "object", "bigint"]

    # static let wellKnownSymbols = ["iterator", "asyncIterator", "match", "matchAll", "replace", "search", "split", "hasInstance", "isConcatSpreadable", "unscopables", "species", "toPrimitive", "toStringTag"]

    # public let interestingIntegers = InterestingIntegers

    # // Double values that are more likely to trigger edge-cases.
    # public let interestingFloats = [-Double.infinity, -Double.greatestFiniteMagnitude, -1e-15, -1e12, -1e9, -1e6, -1e3, -5.0, -4.0, -3.0, -2.0, -1.0, -Double.ulpOfOne, -Double.leastNormalMagnitude, -0.0, 0.0, Double.leastNormalMagnitude, Double.ulpOfOne, 1.0, 2.0, 3.0, 4.0, 5.0, 1e3, 1e6, 1e9, 1e12, 1e-15, Double.greatestFiniteMagnitude, Double.infinity, Double.nan]

    # public let interestingStrings = jsTypeNames
    # public let interestingRegExpQuantifiers = ["*", "+", "?"]

    # public let intType = ILType.integer
    # public let bigIntType = ILType.bigint
    # public let floatType = ILType.float
    # public let booleanType = ILType.boolean
    # public let regExpType = ILType.jsRegExp
    # public let stringType = ILType.jsString
    # public let emptyObjectType = ILType.object()
    # public let arrayType = ILType.jsArray
    # public let argumentsType = ILType.jsArguments
    # public let generatorType = ILType.jsGenerator
    # public let promiseType = ILType.jsPromise

    # /// Identifiers that should be used for custom properties and methods.
    # public static let CustomPropertyNames = ["a", "b", "c", "d", "e", "f", "g", "h"]
    # public static let CustomMethodNames = ["m", "n", "o", "p", "valueOf", "toString"]

    # public private(set) var builtins = Set<String>()
    # public let customProperties = Set<String>(CustomPropertyNames)
    # public let customMethods = Set<String>(CustomMethodNames)
    # public private(set) var builtinProperties = Set<String>()
    # public private(set) var builtinMethods = Set<String>()

    # private var builtinTypes: [String: ILType] = [:]

all_bs = [
    'Array', 'String', 'Number', 'Object', 'Function', 'Boolean', 'Symbol', 'BigInt', 'RegExp', 'Error', 'EvalError',
    'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'URIError', 'ArrayBuffer',
    'SharedArrayBuffer', 'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array',
    'Float32Array', 'Float64Array', 'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'DataView', 'Date',
    'Promise', 'Proxy', 'Map', 'WeakMap', 'Set', 'WeakSet', 'WeakRef', 'FinalizationRegistry', 'Math', 'JSON', 'Reflect'
]

#type
anything = "jsanything"
function = "jsfunction"
object = "jsobject"
iterable = "jsiterable"
number = "jsnumber"
string = "jsstring"

undefined = "undefined"
infinity = "Infinity"
_infinity = "-Infinity"

# negative = "negative"
# integer = ".integer"
length = "length"


builtin_objects = {
    # 23.1 Array Objects
    # 23.2 TypedArray Objects
    "Array":{
        "constructor":{
            "new Array":[
                {
                    "name": "element",   #element or arrayLength
                    "type": number,
                    "value": [anything],
                    "optional": True,
                    "...": True   
                }
            ],
            "Array":[
                {
                    "name": "arrayLength",
                    "type": number,
                    "value": [anything],
                    "optional": True,
                    "...": True   
                }
            ],
        },
        "static_methods":{
            # ( items [ , mapfn [ , thisArg ] ] )
            "Array.from": [
                {
                    "name": "items",
                    "type": anything,
                    "value": [anything],
                },
                {
                    "name": "mapfn",
                    "type": function,
                    "value": [function],
                    "boundary": [undefined],
                    "optional": True
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "Array.fromAsync": [
                {
                    "name": "items",
                    "type": anything,
                    "value": [anything],
                },
                {
                    "name": "mapfn",
                    "type": function,
                    "value": [function],
                    "boundary": [undefined],
                    "optional": True
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "Array.isArray": [
                {
                    "name": "value",
                    "type": anything,
                    "value": [anything]
                }
            ],
            "Array.of": [
                {
                    "name": "items",
                    "type": anything,
                    "value": [anything],
                    # "boundary": ["Array(2**53 - 1)"],
                    "...": True
                }
            ],
        },
        "static_properties":{},
        "instance_methods":{
            "at"             : [
                {
                    "name": "index",
                    "type": number,
                    "value": [anything], #ToIntegerOrInfinity(index).
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, infinity]
                }
            ],
            "concat"         : [
                {
                    "name": "value",
                    "type": anything,
                    "value": [anything],
                    "...": True
                }
            ],
            "copyWithin"     : [
                {
                    "name": "target",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, infinity],
                },
                {
                    "name": "start",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, infinity],
                },
                {
                    "name": "end",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, infinity, undefined],
                    "optional": True
                },
            ],
            # "every"          : [.function(), .opt(.object())],
            "every"          : [
                {
                    "name": "callbackFn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "fill"           : [
                {
                    "name": "value",
                    "type": anything,
                    "value": [anything],
                },
                {
                    "name": "start",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1"],
                    "optional": True
                },
                {
                    "name": "end",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1"],
                    "optional": True
                }
            ],
            # "filter"         : [.function(), .opt(.object())],
            "filter"         : [
                {
                    "name": "callbackfn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            # "find"           : [.function(), .opt(.object())],
            "find"           : [
                {
                    "name": "predicate",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "findIndex"      : [
                {
                    "name": "predicate",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "findLast"      : [
                {
                    "name": "predicate",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "findLastIndex"      : [
                {
                    "name": "predicate",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "flat"           : [
                {
                    "name": "depth",
                    "type": number,
                    "value": [anything],
                    "boundary": ["0", undefined],
                    "optional": True
                }
            ],
            # "flatMap"        : [.function(), .opt(.anything)],
            "flatMap"        : [
                {
                    "name": "mapperFunction",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            # "forEach"        : [.function(), .opt(.object())],
            "forEach"        : [
                {
                    "name": "callbackFn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "includes"       : [
                {
                    "name": "searchElement",
                    "type": anything,
                    "value": [anything],
                },
                {
                    "name": "fromIndex",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, infinity],
                    "optional": True
                }
            ],
            "indexOf"        : [
                {
                    "name": "searchElement",
                    "type": anything,
                    "value": [anything],
                },
                {
                    "name": "fromIndex",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, infinity, undefined],
                    "optional": True
                }
            ],
            "join"           : [
                {
                    "name": "separator",
                    "type": string,
                    "value": [anything], #ToString(separator)
                    "boundary": ["undefined", "''"],
                }
            ],
            "lastIndexOf"    : [
                {
                    "name": "searchElement",
                    "type": anything,
                    "value": [anything],
                },
                {
                    "name": "fromIndex",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, undefined],
                    "optional": True
                }
            ],
            "map"            : [
                {
                    "name": "callbackfn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            # "push"           : [.anything...], ...items   2**53 items
            "push"           : [
                {
                    "name": "items",
                    "type": anything,
                    "value": [anything],
                    # "boundary": ["Array(2**53 - 1)"],
                    "...": True
                }
            ], 
            # "reduce"         : [.function(), .opt(.anything)], ( callbackfn [ , initialValue ] )
            "reduce"         : [
                {
                    "name": "callbackfn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "initialValue",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],

            # "reduceRight"    : [.function(), .opt(.anything)], ( callbackfn [ , initialValue ] )
            "reduceRight"    : [
                {
                    "name": "callbackfn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "initialValue",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "slice"          : [
                {
                    "name": "start",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity],
                    "optional": True
                },
                {
                    "name": "end",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, undefined],
                    "optional": True
                }
            ],
            # "some"           : [.function(), .opt(.anything)],
            "some"           : [
                {
                    "name": "callbackfn",
                    "type": function,
                    "value": [function],
                },
                {
                    "name": "thisArg",
                    "type": anything,
                    "value": [anything],
                    "optional": True
                }
            ],
            "sort"           : [
                {
                    "name": "comparefn",
                    "type": function,
                    "value": [function],
                    "optional": True
                }
            ],
            # "splice"         : [.integer, .opt(.integer), .anything...],  ( start, deleteCount, ...items )
            "splice"         : [
                {
                    "name": "start",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, undefined],
                },
                {
                    "name": "deleteCount",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, undefined],
                    "optional": True
                },
                {
                    "name": "items",
                    "type": anything,
                    "value": [],
                    # "boundary": ["Array(2**53 - 1)"],
                    "...": True
                }
            ],
            # "toLocaleString" : [.opt(.string), .opt(.object())],
            "toLocaleString" : [
                {
                    "name": "locales",
                    "type": string,
                    "value": [anything],
                    "boundary": [],
                    "optional": True
                },
                {
                    "name": "options",
                    "type": object,
                    "value": [object],
                    "boundary": [],
                    "optional": True
                }
            ],
            # "toSpliced"      : [.integer, .opt(.integer), .anything...],
            "toSpliced"      : [
                {
                    "name": "start",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, undefined],
                },
                {
                    "name": "skipCount",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1", "length", "length+1", _infinity, undefined],
                    "optional": True
                },
                {
                    "name": "items",
                    "type": anything,
                    "value": [anything],
                    "optional": True,
                    "...": True
                },
            ],
            # "toSorted"       : [.opt(.function())],
            "toSorted"       : [
                {
                    "name": " comparefn",
                    "type": function,
                    "value": [function],
                    "boundary": [undefined],
                    "optional": True
                }
            ],
            "unshift"        : [
                {
                    "name": "items",
                    "type": anything,
                    "value": [anything],
                    "optional": True,
                    "...": True
                }
            ],
            "with"           : [
                {
                    "name": "index",
                    "type": number,
                    "value": [anything],
                    "boundary": ["-length-1", "-length", "-1", "-0", "+0", "length-1"],
                },
                {
                    "name": "value",
                    "type": anything,
                    "value": [anything],
                }
            ],
            "entries"        : [],
            "keys"           : [],          # returns an array iterator
            "reverse"        : [],
            "values"         : [],
            "pop"            : [],
            "shift"          : [],
            "toString"       : [],
            "toReversed"     : [],
        },
        "instance_properties":{}
    },
    "ArrayBuffer": {
        "constructor": {
            "new ArrayBuffer":[
                {
                    "name": "length", 
                    "type": number,
                    "value": [anything], 
                },
                {
                    "name": "options",  
                    "type": object,
                    "value": [anything],
                    "optional": True,
                    "args": [
                        {
                            "name": "maxByteLength",
                            "type": number,
                            "value": [anything],
                            "optional": True,
                        }
                    ],  
                }
            ],
        },
        "static_methods":{
            "ArrayBuffer.isView": []
        },
        "static_properties":{},
        "instance_methods":{
            "slice": ["tmp_number", "tmp_number"],
            "resize": ["tmp_number"],
            "transfer": ["tmp_any", "tmp_number"],
            "transferToFixedLength": ["tmp_any", "tmp_number", "tmp_number"]
        },
        "instance_properties":{
            "byteLength": [],
            "detached": [],
            "maxByteLength": [],
            "resizable": [],
        },
    },
# 24 Keyed Collections
    # 24.1 Map Objects
    # 24.2 Set Objects
    # 24.3 WeakMap Objects
    # 24.4 WeakSet Objects
    "Map": {
        "constructor": {
            "new Map":[
                {
                    "name": "iterable",
                    "type": iterable,
                    "value": [iterable],
                    "optional": True,
                }
            ]
        },
        "static_methods":{},
        "static_properties":{
            # "Map.groupBy" : [.anything, .function()],
            "Map.groupBy" : [
                {
                    "name": "items",
                    "type": iterable,
                    "value": [iterable],
                },
                {
                    "name": "callbackfn",
                    "type": function,
                    "value": [function],
                    "args": [
                        {
                            "name": "element",
                            "type": iterable,
                            "value": [iterable],
                        },
                        {
                            "name": "index",
                            "type": iterable,
                            "value": [iterable],
                        }
                    ],
                }
            ]
        },
        "instance_methods":{
            # "clear"   : [] => .undefined,
            # "delete"  : [.anything] => .boolean,
            # "entries" : [] => .object(),
            # "forEach" : [.function(), .opt(.object())] => .undefined,
            # "get"     : [.anything] => .anything,
            # "has"     : [.anything] => .boolean,
            # "keys"    : [] => .object(),
            # "set"     : [.anything, .anything] => .jsMap,
            # "values"  : [] => .object(),
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
        "instance_properties":{
            # "size"      : .integer
        },
        
    },
    "Set": {
        "constructor": {
            "new Error":[],
            "Error":[]
        },
        "static_methods":{},
        "static_properties":{},
        "instance_methods":{
            # "add"     : [.anything] => .jsSet,
            # "clear"   : [] => .undefined,
            # "delete"  : [.anything] => .boolean,
            # "entries" : [] => .object(),
            # "forEach" : [.function(), .opt(.object())] => .undefined,
            # "has"     : [.anything] => .boolean,
            # "keys"    : [] => .object(),
            # "values"  : [] => .object(),
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
        "instance_properties":{
            # "size"      : .integer
        },
    },
    "WeakMap": {
        "constructor": {
            "":[
                
            ],
        },
        "static_methods":{},
        "static_properties":{},
        "instance_methods":{
            "delete": ["tmp_any"],
            "get": ["tmp_any"],
            "set": ["tmp_any", "tmp_any"],
            "has": ["tmp_any"]
            # "delete" : [.anything] => .boolean,
            # "get"    : [.anything] => .anything,
            # "has"    : [.anything] => .boolean,
            # "set"    : [.anything, .anything] => .jsWeakMap,
        },
        "instance_properties":{},
        
    },
    "WeakSet": {
        "constructor": {
            "new Error":[],
            "Error":[]
        },
        "static_methods":{},
        "static_properties":{},
        "instance_methods":{
            # "add"    : [.anything] => .jsWeakSet,
            # "delete" : [.anything] => .boolean,
            # "has"    : [.anything] => .boolean,
            "delete": ["tmp_any"],
            "has": ["tmp_any"],
            "add": ["tmp_any"]
        },
        "instance_properties":{},
        
    },
    "String":{},
    "Object":{},
    # 27 Control Abstraction Objects
    # 27.1 Iteration
    # 27.2 Promise Objects
    # 27.3 GeneratorFunction Objects
    # 27.4 AsyncGeneratorFunction Objects
    # 27.5 Generator Objects
    # 27.6 AsyncGenerator Objects
    # 27.7 AsyncFunction Objects
    "Promise": {
        "constructor": {
            "new Promise":[
                {
                    "name": "executor",
                    "type": function,
                    "value": [function],
                    "args": [
                        {
                            "name": "resolveFunc",
                            "type": function,
                            "value": [function],
                        },
                        {
                            "name": "rejectFunc",
                            "type": function,
                            "value": [function],
                        }
                    ],
                }
            ],
        },
        "static_methods":{
            # "all"        : [.jsPromise...] => .jsPromise,
            "Promise.all"        : [
                {
                    "name": "iterable",
                    "type": iterable,
                    "value": [iterable],
                }
            ],
            # "allSettled" : [.jsPromise...] => .jsPromise,
            "Promise.allSettled" : [
                {
                    "name": "iterable",
                    "type": iterable,
                    "value": [iterable],
                }
            ],
            # "any"        : [.jsPromise...] => .jsPromise,
            "Promise.any"        : [
                {
                    "name": "iterable",
                    "type": iterable,
                    "value": [iterable],
                }
            ],
            # "race"       : [.jsPromise...] => .jsPromise,
            "Promise.race"       : [
                {
                    "name": "iterable",
                    "type": iterable,
                    "value": [iterable],
                }
            ],
            # "reject"     : [.anything] => .jsPromise,
            "Promise.reject"     : [
                {
                    "name": "reason",
                    "type": anything,
                    "value": [anything],
                }
            ],
            # "resolve"    : [.anything] => .jsPromise,
            "Promise.resolve"    : [
                {
                    "name": "value",
                    "type": anything,
                    "value": [anything],
                }
            ],
            # "withResolvers" : [] => .object(withProperties: ["promise", "resolve", "reject"]),
            "Promise.withResolvers" : [],
        },
        "static_properties":{
            "Promise.prototype" : object
        },
        "instance_methods":{
            # "catch"   : [.function()] => .jsPromise,
            "catch": [
                {
                    "name": "onRejected",
                    "type": function,
                    "value": [function],
                    "args": [
                        {
                            "name": "reason",
                            "type": anything,
                            "value": [anything],
                        }
                    ],
                }
            ],
            # "finally" : [.function()] => .jsPromise, 
            "finally": [
                {
                    "name": "onFinally",
                    "type": function,   #no arguments
                    "value": [function],
                    "boundary": ["() => {}"],
                }
            ],
            # "then"    : [.function()] => .jsPromise,
            "then": [
                {
                    "name": "onFulfilled",
                    "type": function,
                    "value": [function],
                    "args": [
                        {
                            "name": "value",
                            "type": anything,
                            "value": [anything],
                        }
                    ],
                },
                {
                    "name": "onRejected",
                    "type": function,
                    "value": [function],
                    "args": [
                        {
                            "name": "reason",
                            "type": anything,
                            "value": [anything],
                        }
                    ],
                    "optional": True
                }
            ],
        },
        "instance_properties":{},        
    },
    #https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#parameters
    "Int8Array": {
        "constructor": {
            "new Int8Array":[],
        }
    },
    "Uint8Array": {
        "constructor": {
            "new Uint8Array":[],
        }
    },
    "Uint8ClampedArray": {
        "constructor": {
            "new Uint8ClampedArray":[],
        }
    },
    "Int16Array": {
        "constructor": {
            "new Int16Array":[],
        }
    },
    "Uint16Array": {
        "constructor": {
            "new Uint16Array":[],
        }
    },
    "Int32Array": {
        "constructor": {
            "new Int32Array":[],
        }
    },
    "Uint32Array": {
        "constructor": {
            "new Uint32Array":[],
        }
    },
    "Float32Array": {
        "constructor": {
            "new Float32Array":[],
        }
    },
    "BigInt64Array": {
        "constructor": {
            "new BigInt64Array":[],
        }
    },
    "Float64Array": {
        "constructor": {
            "new Float64Array":[],
        }
    },
    "BigUint64Array": {
        "constructor": {
            "new BigUint64Array":[],
        }
    },
    "Error": {
        "constructor": {
            "new Error":[],
            "Error":[]
        },
        "static_methods":{},
        "static_properties":{},
        "instance_methods":{
            "toString": [],
            "stack": ["tmp_string"]
        },
        "instance_properties":{},
    },
    "AggregateError":{
        "constructor": {
            "new AggregateError":[],
            "AggregateError":[]
        }
    },
    "EvalError": {
        "constructor": {
            "new EvalError":[],
            "EvalError":[]
        }
    },
    "RangeError": {
        "constructor": {
            "new RangeError":[],
            "RangeError":[]
        }
    },
    "ReferenceError": {
        "constructor": {
            "new ReferenceError":[],
            "ReferenceError":[]
        }
    },
    "SyntaxError": {
        "constructor": {
            "new SyntaxError":[],
            "SyntaxError":[]
        }
    },
    "TypeError": {
        "constructor": {
            "new TypeError":[],
            "TypeError":[]
        }
    },
    "URIError": {
        "constructor": {
            "new URIError":[],
            "URIError":[]
        }
    },
}



f =             {
                    "name": "",
                    "type": anything,
                    "value": [],
                    "boundary": [],
                    "optional": True,
                    "...": True
                }

{
    "Error": {
        "constructor": {
            "new Error":[],
            "Error":[]
        },
        "static_methods":{},
        "static_properties":{},
        "instance_methods":{},
        "instance_properties":{},
    }
}