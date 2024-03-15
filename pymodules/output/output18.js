var varIntrospect = (objname, obj) => {
    var attrs = {};
    var methods = new Set();

    if(obj === undefined || obj === null){
        return;
    }
    var enumerableProperties = Array.isArray(obj) ? Object.keys(obj) : null;
//    var enumerableProperties = Array.isArray(obj) ? Object.getOwnPropertyDescriptor(obj) : null;
//    console.log(enumerableProperties)
    // 获取对象原型链上的属性和方法
//    console.log(1)
    Object.getOwnPropertyNames(Object.getPrototypeOf(obj)).forEach((name) => {
//    console.log(name)
        try{
            if (typeof obj[name] === 'function') {
                methods.add(name);
            }
            else if (obj.hasOwnProperty(name)) {
                attrs[name] = typeof obj[name] === 'object' && obj[name] !== null
                             ? obj[name].constructor.name
                             : typeof obj[name];
            }
        }catch(err){
            null;
        }
    });
    // 获取对象自身的属性和方法
//    console.log(2)
    Object.getOwnPropertyNames(obj).forEach((name) => {
//    console.log(name)
        try{
            if (enumerableProperties !== null && enumerableProperties.indexOf(name) !== -1) {
                return;
            }
            if (typeof obj[name] === 'function') {
                methods.add(name);
            }
            else if (obj.hasOwnProperty(name)) {
                attrs[name] = typeof obj[name] === 'object' && obj[name] !== null
                             ? obj[name].constructor.name
                             : typeof obj[name];
            }
        }catch(err){
            null;
        }
    });
////    console.log(3)
//    // 获取对象的构造函数的属性和方法
//    Object.getOwnPropertyNames(obj.constructor).forEach((name) => {
////        console.log(name)
////        console.log(obj.constructor.hasOwnProperty(name))
//        try{
//            if (typeof obj.constructor[name] === 'function') {
//                methods.add(name);
//            }
//            else if (obj.constructor.hasOwnProperty(name)) {
//                attrs[name] = typeof obj.constructor[name] === 'object' && obj.constructor[name] !== null
//                             ? obj.constructor[name].constructor.name
//                             : typeof obj.constructor[name];
//            }
//        }catch(err){
//            null;
//        }
//    });

    // 使用Object.getOwnPropertyDescriptors获取所有自有属性描述符
    var allProps = Object.getOwnPropertyDescriptors(obj.constructor.prototype);
//    console.log(JSON.stringify(allProps))
    for (const [name, descriptor] of Object.entries(allProps)) {
        if (typeof descriptor.value === 'function') {
            methods.add(name);
        } else {
            attrs[name] = typeof descriptor.value === 'object' && descriptor.value !== null
                            ? descriptor.value.constructor.name
                            : typeof descriptor.value;
        }
    }
    var objtype = obj.constructor.name;
    if(objtype === 'String'){
        for(var index in attrs){
            var attr = attrs[index];
            if((!isNaN(parseInt(index)) && attr === 'String') || (!isNaN(parseInt(index)) && attr === 'string')){
                delete attrs[index];
            }
        }
    }
    return {'obj':objname, 'objtype':objtype, 'methods':methods, 'attrs':attrs};
};
function setReplacer(key, value) {
  if (value instanceof Set) {
    return [...value];
  }
  return value;
}
//mark
let isExecuted = false;
/////////////////////////////////////////////////////////////////////////////////////


function opt(opt_param){
const v2 = new Float64Array(752);
const v5 = [];
const v6 = v2.values;
const v7 = Reflect.apply(v6,v2,v5);
switch (v7) {
    case Float64Array:
        let v8 = 1;
        do {
            function* v10(v11,v12) {
                for (const v13 of v5) {
                    const v14 = v13 >>> v8;
                }
                const v15 = yield v10;
                return 752;
            }
            const v16 = v8++;
        } while (v8 < 2);
        break;
}
return v5;
}
let jit_a0 = opt(false);
opt(true);
////////////////////probe/////////////////////////

         let variableNames = ['opt', 'jit_a0'];
        if (!isExecuted) {
            let output = [];
            variableNames.forEach(varName => {
            try{
                let varInstance = eval(varName);
                let typeInfo = varIntrospect(varName, varInstance);
                if (typeInfo !== undefined)
                    output.push(JSON.stringify(typeInfo, setReplacer, 2));
            }catch(err){
                null;
                }
            });
            console.log("qbtly_start[" + output.join(",\n") + "]qbtly_end");
            isExecuted = true; // 设置标志为 true，防止代码再次执行
        }
            
////////////////////probe/////////////////////////

let jit_a0_0 = opt(false);
%PrepareFunctionForOptimization(opt);
let jit_a1 = opt(true);
%OptimizeFunctionOnNextCall(opt);
let jit_a2 = opt(false);
print(jit_a0);
print(jit_a2);
//--allow-natives-syntax --fuzzing
