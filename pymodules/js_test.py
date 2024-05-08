js_code3 = '''
var a;

(a) = 1;

print(a === 1);
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
js_code4 = '''
function a(){}
class CustomPromise extends Promise{
 static resolve(){
  return{
   then(resolve, reject){
    Promise.resolve().then(BigInt).then(resolve, reject);
    reject();
   }
  };
 }
}
CustomPromise.any([1]);
'''