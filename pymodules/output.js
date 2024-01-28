console.log('function ArrayBuffer() { [native code] }'.includes('function'))
let methods = new Set();
methods.add("testMethod1");
methods.add("testMethod2");
console.log(methods);
console.log(JSON.stringify([...methods], null, 2));