
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

/////////////////////////////////////////////////////////////////////////////////////

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
            


   let variableNames = ['x', 'print(x.toString(16))', 'i', 'j'];

/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = -1; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/
for (let i = 0, j = 0; i < 1_000_000; ++i) {
    let x = (-0xffffffffffffffff_ffffffffffffffffn >> 0x40n);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 47; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    if (x != -0x10000000000000000n) {
        print(x.toString(16));
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 73; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        if (++j == 10) break;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 88; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    }
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 91; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

}
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 93; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/
