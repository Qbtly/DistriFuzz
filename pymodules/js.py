js_code3 = '''
var a;

(a) = 1;

print(a === 1);

'''
js_code = '''
var a=[];
for(var i=0;i<100;i++){
    a.push(i+0.123);
}
let b={
    valueOf(){
        a.length=0;
        return 10;
    }
};
var c=a.slice(0,b);
'''

js_code2 = '''


const ab = new ArrayBuffer(0x1000, { "maxByteLength": 0x4000 });
const u8 = new Uint8Array(ab);

let callback = {
    valueOf() {
        ab.resize(0);
        return 0;
    }
};

u8.copyWithin(0x20, callback);

'''
js_code4 = '''
class CustomPromise extends Promise{
 static resolve(){
  return{
   then(resolve, reject){
    Promise.resolve().then(BigInt).then(resolve, reject);
    reject();
   }
  };
 }
}
CustomPromise.any([1]);
'''

arr1 = r'''
var DynamicReflection = (objname, obj) => {
    var attrs = {};
    var methods = new Set();
    if(obj === undefined || obj === null){
        return;
    }
    var enumerableProperties = Array.isArray(obj) ? Object.keys(obj) : null;
    Object.getOwnPropertyNames(Object.getPrototypeOf(obj)).forEach((name) => {
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
    Object.getOwnPropertyNames(obj).forEach((name) => {
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
};
function setReplacer(key, value) {
  if (value instanceof Set) {
    return [...value];
  }
  return value;
}
/////////////////////////////////////////////////////////////////////////////////////
'''
arr2 = r'''
let points = new Set()
function probe(variableNames ,point){

    let isExecuted = points.has(point);
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
        points.add(point)
                }
}
/////////////////////////////////////////////////////////////////////////////////////
            '''