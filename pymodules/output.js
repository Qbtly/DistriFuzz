
var varIntrospect = (objname, obj) => {
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
            if((!isNaN(parseInt(index)) && attr === 'String') || (!isNaN(parseInt(index)) && attr === 'string')){
                delete attrs[index];
            }
        }
    }
    return {'obj':objname, 'objtype':objtype, 'methods':methods, 'attrs':attrs};
};
function setReplacer(key, value) {
  if (value instanceof Set) {
    return [...value];
  }
  return value;
}
let output = [];
/////////////////////////////////////////////////////////////////////////////////////
let variableNames = ['v4', 'v2']
    
    const v2 = new Array(2);
    const v4 = new String("A String object");
    
variableNames.forEach(varName => {
try{
    let varInstance = eval(varName);
    let typeInfo = varIntrospect(varName, varInstance);
    output.push(JSON.stringify(typeInfo, setReplacer, 2));
}catch(err){
    console.log('error');
    }
});
console.log("[" + output.join(",\n") + "]");
    