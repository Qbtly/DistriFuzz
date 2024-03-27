js_code3 = '''
function main() {
    const v1 = [2020, 2020];
    function v3(v4, v5, v6, v7) {
        for (const obj18 = obj16++; v11 < 7; v11++) {
            for (let v16 = 0; v16 != 100; v16++) {
            }
            for (let v18 = -0.0; v18 < 7; v18 = v18 || 13.37) {
                const v21 = Math.max(-339, v18);
                const v22 = v1.fill();
                const v23 = v7 % v21;
            }
        }
    }
    const v24 = v3();
}

main();

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
            print("qbtly_start[" + output.join(",\n") + "]qbtly_end");
            isExecuted = true; // 设置标志为 true，防止代码再次执行
        }
            '''