arr1 = r'''

function isIterable(obj) {
    return obj != null && typeof obj[Symbol.iterator] === 'function';
}

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
    var iterable = isIterable(obj);
    return {'obj':objname, 'type':type, 'iterable':iterable, 'methods':methods, 'attrs':attrs};
};



/////////////////////////////////////////////////////////////////////////////////////
'''
arr2 = r'''
function setReplacer(key, value) {
  if (value instanceof Set) {
    return [...value];
  }
  return value;
}

let points = new Set()
var startTime = Date.now();
var timeout = 5000;

function check_time(now_time){
    if (now_time - startTime >= timeout) {
        print("Qbtly_timeout");
        quit(1);
     }
}

function my_print(a_v, point, output){
    print("qbtly_start&");
    print("qbtly_aviliable[" + a_v + "]qbtly_var");
    print("qbtly_point_start" + point + "qbtly_point_end");
    print("qbtly_dicts_start[" + output.join(",\n") + "]qbtly_dicts_end");
    print("&qbtly_end");
}
/////////////////////////////////////////////////////////////////////////////////////
            '''

arr3 = r''' if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();'''

head = "\n/*----------------------------------------probe----------------------------------------*/\n"

arr4 = r'''
let points = new Set()
var startTime = Date.now();
var timeout = 5000;

function probe(variableNames ,point){
    let isExecuted = points.has(point);
    if (!isExecuted) {
        let output = [];
        let a_v = [];
        variableNames.forEach(varName => {
        try{
            let varInstance = eval(varName);
            let typeInfo = DynamicReflection(varName, varInstance);
            //let typeInfo = DynamicReflection(varName.name, varName.instance);
            if (typeInfo !== undefined)
                output.push(JSON.stringify(typeInfo, setReplacer, 2));
                a_v.push(varName);
        }catch(err){
            null;
            }
        });
        print("qbtly_start&");
        print("qbtly_aviliable[" + a_v + "]qbtly_var");
        print("qbtly_point_start" + point + "qbtly_point_end");
        print("qbtly_dicts_start[" + output.join(",\n") + "]qbtly_dicts_end");
        print("&qbtly_end");
        points.add(point);
                }
     if (Date.now() - startTime >= timeout) {
        print("Function Run has been terminated due to timeout.");
        quit();
     }
}
/////////////////////////////////////////////////////////////////////////////////////
            '''
