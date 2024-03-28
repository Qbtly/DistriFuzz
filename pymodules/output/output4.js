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
            else if (Object.getPrototypeOf(obj).hasOwnProperty(name)) {
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
//    var allProps = Object.getOwnPropertyDescriptors(obj.constructor.prototype);
//    console.log(JSON.stringify(allProps))
//    for (const [name, descriptor] of Object.entries(allProps)) {
//        if (typeof descriptor.value === 'function') {
//            methods.add(name);
//        } else {
//            attrs[name] = typeof descriptor.value === 'object' && descriptor.value !== null
//                            ? descriptor.value.constructor.name
//                            : typeof descriptor.value;
//        }
//    }

    var type = obj.constructor.name;
    if(type === 'String' || type.includes('Array')){
        for(var index in attrs){
            var attr = attrs[index];
            if((!isNaN(parseInt(index)) && attr === 'String') || (!isNaN(parseInt(index)) && attr === 'string')||
            (!isNaN(parseInt(index)) && attr === 'Number') || (!isNaN(parseInt(index)) && attr === 'number')){
                delete attrs[index];
            }
        }
    }
    return {'obj':objname, 'type':type, 'methods':methods, 'attrs':attrs};
//    return {'obj':objname, 'type':type};
};
function setReplacer(key, value) {
  if (value instanceof Set) {
    return [...value];
  }
  return value;
}
//mark
let isExecuted = false;
let a_v = [];
/////////////////////////////////////////////////////////////////////////////////////



var a=[];
for(var i=0;i<100;i++){
    a.push(i+0.123);
}
let b={
    valueOf(){
        a.length=0;
        return 10;
////////////////////probe/////////////////////////

         let variableNames = ['c', 'a', 'i', 'b'];
                if (!isExecuted) {
                    let output = [];
                    variableNames.forEach(varName => {
                    try{
                        let varInstance = eval(varName);
                        let typeInfo = varIntrospect(varName, varInstance);
                        if (typeInfo !== undefined)
                            output.push(JSON.stringify(typeInfo, setReplacer, 2));
                            a_v.push(varName);
                    }catch(err){
                        null;
                        }
                    });
                    print("qbtly_aviliable[" + a_v + "]qbtly_var");
                    print("qbtly_start[" + output.join(",\n") + "]qbtly_end");
                    isExecuted = true; // 设置标志为 true，防止代码再次执行
                }
                    
////////////////////probe/////////////////////////

    }
};
var c=a.slice(0,b);
