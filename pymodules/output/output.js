var DynamicReflection = (objname, obj) => {
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

let mark = 0;

function probe(variableNames ,point){
    let isExecuted = mark === point;
    if (!isExecuted) {
        let output = [];
        let a_v = [];
        variableNames.forEach(varName => {
        try{
            let varInstance = eval(varName);
            let typeInfo = DynamicReflection(varName, varInstance);
            if (typeInfo !== undefined)
                output.push(JSON.stringify(typeInfo, setReplacer, 2));
                a_v.push(varName);
        }catch(err){
            null;
            }
        });
        print("qbtly_start&")
        print("qbtly_aviliable[" + a_v + "]qbtly_var");
        print("qbtly_point_start" + point + "qbtly_point_end")
        print("qbtly_dicts_start[" + output.join(",\n") + "]qbtly_dicts_end");
        print("&qbtly_end")
        mark = point; // 设置标志为 true，防止代码再次执行
                }
}

/////////////////////////////////////////////////////////////////////////////////////




   let variableNames = ['a', 'b', 'valueOf', 'i', 'push', 'length', 'a.length', 'c', 'slice'];

var a=[];
////////////////////probe/////////////////////////
   probe(variableNames,7);

////////////////////probe/////////////////////////

for(var i=0;i<100;i++){
    a.push(i+0.123);
////////////////////probe/////////////////////////
   probe(variableNames,35);

////////////////////probe/////////////////////////

}
////////////////////probe/////////////////////////
   probe(variableNames,37);

////////////////////probe/////////////////////////

let b={
    valueOf(){
        a.length=0;
////////////////////probe/////////////////////////
   probe(variableNames,57);

////////////////////probe/////////////////////////

        return 10;
////////////////////probe/////////////////////////
   probe(variableNames,63);

////////////////////probe/////////////////////////

    }
};
////////////////////probe/////////////////////////
   probe(variableNames,69);

////////////////////probe/////////////////////////

var c=a.slice(0,b);
////////////////////probe/////////////////////////
   probe(variableNames,83);

////////////////////probe/////////////////////////

