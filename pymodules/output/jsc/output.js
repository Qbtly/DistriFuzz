
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
            


   let variableNames = ['i', 'propName', 'Object.getOwnPropertyDescriptor(obj,"x")', 'result', 'Reflect.defineProperty(proxy,"x",{enumerable:true,configurable:true,set:function(x){},})', 'theTarget', 'print(pDesc.enumerable===true)', 'pDesc', 'proxy', 'handler', 'called', 'b', 'obj', 'target', 'descriptor', 'x'];

/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = -1; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/
function print(b) {
    if (!b)
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



(function () {
    let target = {};
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 49; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    let called = false;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 59; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    let handler = {
        defineProperty: function(theTarget, propName, descriptor) {
            called = true;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 93; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            return Reflect.defineProperty(theTarget, propName, descriptor);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 110; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        }
    };
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 117; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


    let proxy = new Proxy(target, handler);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 136; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    for (let i = 0; i < 500; i++) {
        let result = Reflect.defineProperty(proxy, "x", {
            enumerable: true,
            configurable: true,
            get: function(){},
        });
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 211; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        print(result);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 218; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        print(called);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 225; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        called = false;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 233; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


        for (let obj of [target, proxy]) {
            let pDesc = Object.getOwnPropertyDescriptor(obj, "x");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 272; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(typeof pDesc.get === "function");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 287; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(typeof pDesc.set === "undefined");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 302; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(pDesc.get.toString() === (function(){}).toString());
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 329; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(pDesc.configurable === true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 342; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(pDesc.enumerable === true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 355; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        }
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 358; if (!points.has(point)) { let output = []; let a_v = [];
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

})();
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 367; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/



(function () {
    let target = {};
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 388; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    let called = false;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 398; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    let handler = {
        defineProperty: function(theTarget, propName, descriptor) {
            called = true;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 432; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            return Reflect.defineProperty(theTarget, propName, descriptor);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 449; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        }
    };
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 456; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


    let proxy = new Proxy(target, handler);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 475; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    for (let i = 0; i < 500; i++) {
        let result = Reflect.defineProperty(proxy, "x", {
            enumerable: true,
            configurable: true,
            set: function(x){},
        });
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 551; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        print(result);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 558; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        print(called);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 565; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        called = false;
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 573; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/


        for (let obj of [target, proxy]) {
            let pDesc = Object.getOwnPropertyDescriptor(obj, "x");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 612; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(typeof pDesc.get === "undefined");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 627; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(typeof pDesc.set === "function");
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 642; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(pDesc.set.toString() === (function(x){}).toString());
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 670; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(pDesc.configurable === true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 683; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

            print(pDesc.enumerable === true);
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 696; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

        }
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 699; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

    }
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 702; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

})();
/*----------------------------------------probe----------------------------------------*/
            ;(function() {let point = 708; if (!points.has(point)) { let output = []; let a_v = [];
                variableNames.forEach(varName => {try{
                    let typeInfo = DynamicReflection(varName, eval(varName)); a_v.push(varName);
                    if (typeInfo !== undefined) output.push(JSON.stringify(typeInfo, setReplacer, 2)
                );}catch(err){null;}}); my_print(a_v, point, output); points.add(point);} check_time(Date.now()); })();
/*----------------------------------------probe----------------------------------------*/

