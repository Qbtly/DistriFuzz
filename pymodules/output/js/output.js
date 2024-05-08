
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
            


   let variableNames = ['Object.isFrozen(siteObject.raw)', 'expected', 'value', 'actual', 'elements', 'desc', 'siteObject', 'Object.getOwnPropertyDescriptor(siteObject,i)', 'shouldBe', 'i', 'count', 'tag'];

/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = -1; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/
function shouldBe(actual, expected) {
    if (actual !== expected)
        throw new Error('bad value: ' + actual);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 36; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

}
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 38; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


function tag(elements) {
    return function (siteObject) {
        shouldBe(siteObject instanceof Array, true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 73; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(Object.isFrozen(siteObject), true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 88; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(siteObject.raw instanceof Array, true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 104; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(Object.isFrozen(siteObject.raw), true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 121; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(siteObject.hasOwnProperty("raw"), true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 136; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(siteObject.propertyIsEnumerable("raw"), false);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 151; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(siteObject.length, arguments.length);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 165; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(siteObject.raw.length, arguments.length);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 181; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        var count = siteObject.length;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 193; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        for (var i = 0; i < count; ++i) {
            shouldBe(siteObject.hasOwnProperty(i), true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 234; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            var desc = Object.getOwnPropertyDescriptor(siteObject, i);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 252; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            shouldBe(desc.writable, false);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 264; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            shouldBe(desc.enumerable, true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 276; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            shouldBe(desc.configurable, false);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 288; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        }
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 291; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        shouldBe(siteObject.length, elements.length + 1);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 309; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        for (var i = 0; i < elements.length; ++i)
            shouldBe(arguments[i + 1], elements[i]);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 355; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    };
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 359; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

}
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 361; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


var value = {
    toString() {
        throw new Error('incorrect');
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 388; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    },
    valueOf() {
        throw new Error('incorrect');
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 410; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    }
};
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 416; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


tag([])``;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 426; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

tag([])`Hello`;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 440; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

tag([])`Hello World`;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 460; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

tag([value])`Hello ${value} World`;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 485; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

tag([value, value])`Hello ${value} OK, ${value}`;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 515; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

