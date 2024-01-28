
var varIntrospect = (objname, obj) => {
    var attrs = {};
    var methods = new Set();

    if(obj === undefined || obj === null){
        return;
    }
    var enumerableProperties = Array.isArray(obj) ? Object.keys(obj) : null;
    Object.getOwnPropertyNames(Object.getPrototypeOf(obj)).forEach((name) => {
        try{
        	//print(name);
        	//console.log(JSON.stringify(name, null, 2));
        	//console.log(name,obj[name]);
            //if (JSON.stringify(typeof obj[name], null, 2) == '"function"') {
            if (typeof obj[name] === 'function') {
                methods.add(name);
                //console.log(JSON.stringify([...methods], null, 2));
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

    var objtype = obj.constructor.name;
    if(objtype === 'String'){
        for(var index in attrs){
            var attr = attrs[index];
            if(!isNaN(parseInt(index)) && attr === 'String'){
                delete attrs[index];
            }
        }
    }
    return {'obj':objname, 'objtype':objtype, 'methods':methods, 'attrs':attrs};
};
function setReplacer(key, value) {
  if (value instanceof Set) {
    return [...value]; // 将 Set 转换为数组
  }
  return value;
}

let variableNames = ['foo','a','f']
function foo(glob, imp, b) {
    "use asm";
    var arr=new glob.Int8Array(b);
    return {};
  }
  a = new ArrayBuffer(64 * 1024);
  foo(this, null, a);
  function f(h, g) {
    //ensureNonInline(g);
  }
  f(Float64Array, a);


variableNames.forEach(varName => {
try{
	let varInstance = eval(varName);
	let typeInfo = varIntrospect(varName, varInstance);
	console.log(JSON.stringify(typeInfo, setReplacer, 2)); // 美化输出
}catch(err){
        console.log('error');
        }
});