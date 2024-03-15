js_code = '''
var a = [];
for (var e = 0; e < 100; e++) {a.push(e + 0.123);}
function call_back() {
    var k = 0;
    k = 1;
    a.length = 0; 
    return 10;
}
var b = a.slice(0, { valueOf: call_back });
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

get_type = r'''
        if (!isExecuted) {
            let output = [];
            variableNames.forEach(varName => {
            try{
                let varInstance = eval(varName);
                let typeInfo = varIntrospect(varName, varInstance);
                if (typeInfo !== undefined)
                    output.push(JSON.stringify(typeInfo, setReplacer, 2));
            }catch(err){
                null;
                }
            });
            console.log("qbtly_start[" + output.join(",\n") + "]qbtly_end");
            isExecuted = true; // 设置标志为 true，防止代码再次执行
        }
            '''