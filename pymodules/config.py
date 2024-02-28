builtins = ["Array", "ArrayBuffer", "AggregateError", "apply", "abs", "acos", "acosh", "asin", "asinh", 
"atan", "atan2", "atanh", "arguments", "at", "add", "asyncIterator", "anchor", "and", "asIntN", 
"asUintN", "Atomics", "all", "allSettled", "any", "assign", "AsyncFunction", "AsyncGeneratorFunction",

"bind", "Boolean", "byteOffset", "BYTES_PER_ELEMENT", "byteLength", "BigInt64Array", "BigUInt64Array",
"buffer", "big", "blink", "bold",

"constructor", "configurable", "copyWithin", "call", "charAt", "charCodeAt", "concat", "caller", 
"ceil", "cos", "cosh", "Collator", "codePointAt", "clz32", "cbrt", "compile", "cause", "columnNumber",
"compareExchange", "catch", "create", "clear", "construct", "callee",

"Date", "DataView", "defineProperty", "deleteProperty", "decodeURIComponent", "DateTimeFormat", 
"decodeURI", "defineProperties", "DisplayNames", "DisplayName", "dotAll", "delete", "deref", "description",

"endsWith", "Error", "eval", "enumerable", "exec", "entries", "every", "encodeURI", "encodeURIComponent",
"exp", "expm1", "exchange", "evalError", "escape", "EPSILON",

"fill", "Function", "Float32Array", "Float64Array", "filter", "find", "fromCodePoint", "fromCharCode", 
"freeze", "floor", "fround", "findIndex", "findLast", "findLastIndex", "forEach", "from", "flags", 
"fileName", "for", "fixed", "fontcolor", "fontsize", "flat", "flatMap", "finally", "fromEntries",

"get", "getOwnPropertyDescriptor", "getPrototypeOf", "getReader", "getDate", "getDay", "getFullYear", 
"getHours", "getMilliseconds", "getMinutes", "getMonth", "getSeconds", "getTime", "getTimezoneOffset", 
"getUTCDate", "getUTCDay", "getUTCFullYear", "getUTCHours", "getUTCMilliseconds", "getUTCMinutes", 
"getUTCMonth", "getUTCSeconds", "getYear", "global", "group", "groupToMap",
"getOwnPropertyDescriptors", "getCanonicalLocales", "getOwnPropertySymbols", "getOwnPropertyNames",
"getBigInt64", "getFloat64", "getFloat32", "getInt64", "getInt32", "getInt16", "getInt8",
"getBigUint64", "getUint64", "getUint32", "getUint16", "getUint8", "globalThis", "GeneratorFunction",

"hasOwnProperty", "hasInstance", "hypot", "has", "hasOwn",

"isNaN", "Int32Array", "isExtensible", "Int16Array", "Infinity", "isFoxyinite", "isFrozen", "isSealed", 
"InternalError", "Intl", "isConcatSpreadable", "includes", "Int8Array", "indexOf", "isArray", "imul",
"isView", "ignoreCase", "input", "iterator", "italics", "isLockFree", "isPrototypeOf", "isInteger",
"isSafeInteger", "is",

"JSON", "join",

"keys", "keyFor",

"length", "lastIndexOf", "lastParen", "leftContext", "LN2", "LN10", "LOG10E", "LOG2E", "lastIndex",
"log", "log10", "log1p", "log2", "lastMatch", "lineNumber", "link", "localeCompare", "load",
"ListFormat", "Locale",

"Math", "match", "matchAll", "MIN_SAFE_INTEGER", "MAX_SAFE_INTEGER", "MAX_VALUE", "MIN_VALUE", 
"Map", "max", "min", "multiline", "message", 

"NaN", "NEGATIVE_INFINITY", "next", "Number", "normalize", "NumberFormat", "name", "now",
"notify",

"Object", "ownKeys", "of", "or",

"pop", "push", "print", "prototype", "Promise", "POSITIVE_INFINITY", "parseInt", "parseFloat", 
"Proxy", "preventExtensions", "padEnd", "padStart", "propertyIsEnumerable", "PI", "pow", "parse",
"PluralRules",


"repeat", "ReferenceError", "Reflect", "round", "ReadableStream", "reverse", "random", "RegExp", 
"replace", "rightContext", "RangeError", "revocable", "replaceAll", "reduce", "reduceRight", 
"raw", "resolve", "race", "reject", "return", "RelativeTimeFormat",

"set", "split", "slice", "String", "splice", "sort", "shift", "Symbol", "species", "setPrototypeOf", 
"search", "setUTCHours", "setUTCFullYear", "setUTCDate", "setTime", "setSeconds", "setMonth", 
"setMinutes", "setFullYear", "setHours", "setMilliseconds", "setYear", "SyntaxError", "Set", 
"substring", "startsWith", "setBigInt64", "setFloat64", "setFloat32", "setInt64", "setInt32", 
"setInt16", "setInt8","setBigUint64", "setUint64", "setUint32", "setUint16", "setUint8",
"SQRT2", "SQRT1_2", "sign", "sin", "sinh", "sqrt", "some", "subarray", "setDate",
"setUTCMilliseconds", "setUTCMinutes", "setUTCMonth", "setUTCSeconds", "source", "sticky",
"stack", "small", "strike", "sub", "substr", "sup", "SharedArrayBuffer", "store", "stringify",
"seal", "size", "supportedValuesOf", "Segmenter",

"toString", "toLocaleString", "then", "toLocaleLowerCase", "toLocaleUpperCase", "toLowerCase", 
"toUpperCase", "toTimeString", "toUTCString", "TypeError", "toPrimitive", "toISOString", "toJSON",
"tan", "tanh", "trunc", "TypedArray", "toDateString", "toGMTString", "toLocaleDateString", 
"toLocaleTimeString", "test", "toStringTag", "trim", "trimEnd", "trimStart", "toExponential", 
"toFixed", "toPrecision", "throw",


"Uint8Array", "Uint32Array", "unshift", "Uint8ClampedArray", "Uint16Array", "UTC", "unicode",
"URIError", "unscopables", "undefined", "unescape",

"valueOf", "values",

"writable", "WebAssembly", "WeakMap", "WeakSet", "WeakRef", "wait", "waitAsync",

"xor",

"__proto__", "__defineGetter__", "__defineSetter__", "__lookupGetter__", "__lookupSetter__",
"$_", "$&", "$+", "$`", "$'", "$1", "$2", "$3", "$4", "$5", "$6", "$7", "$8", "$9",
"%PrepareFunctionForOptimization", "%OptimizeFunctionOnNextCall", "%OptimizeMaglevOnNextCall", "%OptimizeOsr", "%GetOptimizationStatus", "%DeoptimizeNow", "%DeoptimizeFunction", "%NeverOptimizeFunction",
"%HasHoleyElements", "%HasObjectElements", "%HasSmiElements", "%HasDoubleElements", "%HasDictionaryElements", "%HasSloppyArgumentsElements", "%HasFastElements",
"%HaveSameMap", "%HeapObjectVerify", "%HasFastProperties", "%HasProperty",
"%DebugPrint", "%SystemBreak", "%ScheduleBreak", "%Typeof", "%CollectGarbage","%ClearFunctionFeedback", "%ArrayBufferDetach", "%AbortJS",
"%CompileBaseline", "%BaselineOsr", "%BenchTurbofan", "%DisassembleFunction", "%TraceExit","%IsSmi", "%LiveEditPatchScript","%Call",
"%EnsureFeedbackVectorForFunction", "%CreatePrivateSymbol", "%CreatePrivateNameSymbol", "%GetUndetectable",
"%RunningInSimulator", "%IsAsmWasmCode", "%CheckIsOnCentralStack", "%IsArray", "%CheckTypeOf", "%CheckTurboshaftTypeOf",
"%DeleteProperty", "%DefineAccessorPropertyUnchecked","%GetProperty","%SetKeyedProperty","%SetNamedProperty",
"%StringParseInt", "%DisableOptimizationFinalization", "%PerformMicrotaskCheckpoint", "%IsDictPropertyConstTrackingEnabled",
"%SetAllocationTimeout", "%SimulateNewspaceFull", "%WaitForBackgroundOptimization", "%StringAdd", "%_DeoptimizeNow",
"%HasOwnConstDataProperty", "%OptimizeObjectForAddingMultipleProperties", "%TryMigrateInstance", "%MaxSmi", "%ToLength",
"%CompleteInobjectSlackTracking", "%NotifyContextDisposed", "%ArrayBufferMaxByteLength", "%DebugToggleBlockCoverage", "%ForceFlush",
"%StringMaxLength", "%StringLessThan", "%_CreateDataProperty", "%ConstructConsString", "%DebugGetLoadedScriptIds", "%ToFastProperties",
"%FunctionGetInferredName", "%HandleDebuggerStatement", "%InLargeObjectSpace", "%EnqueueMicrotask", "%NormalizeElements",
"%FinalizeOptimization", "%ThrowStackOverflow", "%SetForceSlowPath", "%AllocateHeapNumber", "%InternalizeString", "%LoadLookupSlot",
"%IsBeingInterpreted", "%IsWasmCode", "%SerializeWasmModule", "%DeserializeWasmModule", "%EnableCodeLoggingForTesting", "%IsThreadInWasm",
"%WasmTierUpFunction", "%IsLiftoffFunction"]

token_size = 200
sample_size = 10000
train = False

ids = []
intervals = {}
texts = {}
new_samples = []

# train_file_path = "/home/b/zhunki/crossover/pymodules/train.txt"
# last_original = ""
# last_replace = ""
# last_original_sample = ""