
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
            


   let variableNames = ['print(einstanceofRangeError)', 'e', 'v', 'radix', 'a', 'testInvalidRadix'];

/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = -1; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/
function print(a) {
    if (!a)
        throw new Error("Bad assertion");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 26; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

}
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 28; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


let v = 10n;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 38; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString() === "10");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 52; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(2) === "1010");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 67; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(3) === "101");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 82; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(8) === "12");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 97; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(16) === "a");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 112; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(32) === "a");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 127; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


v = 191561942608236107294793378393788647952342390272950271n;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 135; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString() === "191561942608236107294793378393788647952342390272950271");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 149; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(2) === "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 164; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(3) === "2002122121011101220102010210020102000210011100122221002112102021022221102202020101221000021200201121121100121121");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 179; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(8) === "77777777777777777777777777777777777777777777777777777777777");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 194; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(16) === "1ffffffffffffffffffffffffffffffffffffffffffff");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 209; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(32) === "3vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 224; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


v = -10n;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 233; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString() === "-10");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 247; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(2) === "-1010");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 262; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(3) === "-101");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 277; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(8) === "-12");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 292; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(16) === "-a");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 307; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(32) === "-a");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 322; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


v = -191561942608236107294793378393788647952342390272950271n;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 331; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString() === "-191561942608236107294793378393788647952342390272950271");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 345; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(2) === "-111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 360; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(3) === "-2002122121011101220102010210020102000210011100122221002112102021022221102202020101221000021200201121121100121121");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 375; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(8) === "-77777777777777777777777777777777777777777777777777777777777");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 390; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(16) === "-1ffffffffffffffffffffffffffffffffffffffffffff");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 405; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

print(v.toString(32) === "-3vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 420; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/




function testInvalidRadix(radix) {
    try {
        v.toString(radix);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 446; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        print(false);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 453; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    } catch(e) {
        print(e instanceof RangeError);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 474; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    }
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 477; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

}
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 479; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


testInvalidRadix(-10);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 487; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

testInvalidRadix(-1);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 494; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

testInvalidRadix(0);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 500; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

testInvalidRadix(1);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 506; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

testInvalidRadix(37);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 512; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

testInvalidRadix(4294967312);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 518; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


