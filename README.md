# WasmFuzzer

This is a grammar-aware Wasm compilers fuzzer based on AFL.

## compile on Ubuntu

```
CFLAGS="-DUSE_PYTHON -I/usr/include/python3.10" LDFLAGS="-lpython3.10" make clean all
```

## compile and fuzz webkit on Ubuntu

```
git clone https://github.com/WebKit/WebKit.git --depth 1
cd Webkit
export CC=/home/b/wasm_fuzzer/afl-clang
export CXX=/home/b/wasm_fuzzer/afl-clang++
export AFL_HARDEN=1
export AFL_INST_RATIO=100
./Tools/Scripts/build-jsc --jsc-only --build-dir=1212/

sudo apt install ruby
sudo apt install libicu-dev

export AFL_SKIP_CRASHES=1

AFL_PYTHON_MODULE="mutator" PYTHONPATH=./pymodules/ ./afl-fuzz -S jsc -m 4G -t 800+ -i /home/b/js_poc/jsc/ -o /home/b/jsc_out/ /home/b/WebKit/1212/JSCOnly/Release/bin/jsc @@
```

## get and compile v8 on Ubuntu
```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=$PATH:~/zhunki/depot_tools
mkdir v8
cd v8
gclient config https://chromium.googlesource.com/v8/v8
gclient sync
cd v8
export AFL_HARDEN=1
export AFL_INST_RATIO=100
export AFL_CC_VERBOSE=1
gn gen 0907 --args='is_debug=false use_afl=true' --check
ninja -C 0907/

AFL_PYTHON_MODULE="mutator" PYTHONPATH=./pymodules/ ./afl-fuzz -S jsc -m 4G -t 800+ -i /home/b/js_poc/v8/ -o /home/b/v8_out/ /home/b/v8/v8/d8 @@
```