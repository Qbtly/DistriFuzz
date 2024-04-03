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



   let variableNames = ['from', 'define_property_holder', 'ReturnHolder', 'Trigger', 'new_value', 'print', 'ArrayBuffer', 'splice', 'old_space_array', 'to[0]', 'original_cow_object', 'i', 'MakeCopy', 'CopyElement', 'copy', 'Array', 'MakeCOW', 'concat', 'to', 'new_space_array', 'ForceGC'];
function ForceGC() { try { new ArrayBuffer(2 ** 34);   probe(variableNames,22);
 } catch { }   probe(variableNames,30);
 }   probe(variableNames,32);


old_space_array = Array(1, 2);   probe(variableNames,46);


function CopyElement(from, to) { to[0] = from[0];   probe(variableNames,72);
 }   probe(variableNames,74);

for (let i = 0; i < 10000; ++i) {
  CopyElement(old_space_array, old_space_array);   probe(variableNames,109);

}   probe(variableNames,111);


ForceGC();   probe(variableNames,117);


function MakeCOW() { return [0];   probe(variableNames,133);
 }   probe(variableNames,135);

original_cow_object = MakeCOW();   probe(variableNames,144);


function MakeCopy() {
  let copy = original_cow_object.concat();   probe(variableNames,167);

  copy.splice();   probe(variableNames,175);

  return copy;   probe(variableNames,181);

}   probe(variableNames,183);


new_value = 1;   probe(variableNames,191);

new_value = {};   probe(variableNames,199);


function ReturnHolder() { return define_property_holder   ;probe(variableNames,212);
 }   probe(variableNames,214);

class Trigger extends ReturnHolder { 0 = new_value; }   probe(variableNames,233);


for (let i = 0; i < 10000; ++i) {
  define_property_holder = MakeCopy();   probe(variableNames,269);

  new Trigger();   probe(variableNames,277);

}   probe(variableNames,279);


new_value = {};   probe(variableNames,288);

define_property_holder = MakeCOW();   probe(variableNames,297);

new Trigger();   probe(variableNames,304);


new_space_array = MakeCOW();   probe(variableNames,314);

new_space_array.splice();   probe(variableNames,321);


CopyElement(new_space_array, old_space_array);   probe(variableNames,331);


new_value = "";   probe(variableNames,339);

define_property_holder = MakeCOW();   probe(variableNames,348);

new Trigger();   probe(variableNames,355);


new_space_array = null;   probe(variableNames,363);

ForceGC();   probe(variableNames,368);


print(old_space_array[0][0]);   probe(variableNames,381);