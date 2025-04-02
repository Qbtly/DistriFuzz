
RootCause = {
    "A": "Incorrect Control Flow Handling",
    "B": "Incorrect Type Handling",
    "C": "Incorrect Data Structure Handling",
    "D": "Incorrect Optimization Algorithm",
    "E": "Incorrect Resource Management",
    "F": "Others"
}
# B.1 Type Conversion Errors
# B.2.1 Incorrect Type Consistency Assumption
# B.2.2 Incorrect Type Speculation
# B.3 Type Misuse
# C.1 Missing Accessibility Check / Validation
# C.2 Incorrect Range Speculation
# C.3 Incorrect Boundary Calculation
# C.4 Incorrect Structure Tracking
# C.5 Improper Synchronization of Shared Data Structures
# D. Incorrect Optimization Algorithm
# E.1 Improper Initialization
# E.2.1 Incorrect Reference Tracking
# E.2.2 Incorrect Mark-and-Sweep
# E.3 Incorrect Register Management
# F. Others

    

vul_patterns = [
    {
        "RootCause": RootCause["A"],
        "patterns": [
            {
                # "CVEs": ["CVE-2018-8279"],
                "rootc": "Incorrect Control Flow Handling",
                "vulp": '''
                    漏洞模式：类定义或默认参数中包含异步控制流，破坏语义边界
                    模式结构：
                        - 在类或函数默认参数中嵌入 async/await 表达式
                        - 搭配大规模对象创建或函数闭包喷射
                        - 导致控制权交错，作用域初始化失败或顺序错乱
                '''
            },
            {
                # "CVEs": ["CVE-2019-8672", "CVE-2019-5867"],
                "rootc": "Incorrect Control Flow Handling",
                "vulp": '''
                    漏洞模式：异常处理与递归或 eval 嵌套混用，控制流状态失衡
                    模式结构：
                        - 使用 try/catch 包裹函数递归或动态 eval
                        - 内部包含 TypedArray、Promise、slice.call 等 API 调用
                        - GC 或堆喷辅助打乱执行路径
                        - 导致异常捕获对象或上下文同步异常
                '''
            },
            {
                # "CVEs": ["CVE-2022-4262"],
                "rootc": "Incorrect Control Flow Handling",
                "vulp": '''
                    漏洞模式：函数参数解构 + 闭包绑定交错，引发作用域同步问题
                    模式结构：
                        - 使用 IIFE 或箭头函数 + 解构赋值语法（带计算属性）
                        - 解构过程中嵌套调用函数或 eval 动态语句
                        - 在特定条件或迭代触发堆栈同步失败
                '''
            },
            {
                # "CVEs": ["CVE-2021-38003"],
                "rootc": "Incorrect Control Flow Handling",
                "vulp": '''
                    漏洞模式：构造深层数组或对象链 + 异常回收失败
                    模式结构：
                        - 创建嵌套数组/对象并互相引用
                        - 使用 JSON.stringify、replace 等格式化接口触发异常
                        - 捕获异常对象（hole）并观察其泄露或属性异常
                '''
            },
            {
                # "CVEs": ["CVE-2017-11841", "CVE-2018-12387"],
                "rootc": "Incorrect Control Flow Handling",
                "vulp": '''
                    漏洞模式：构造函数或 call/apply 绑定执行链失衡
                    模式结构：
                        - 使用 call/apply/bind 调用构造函数或原型链方法
                        - 重复调用、inlined function、参数操作引起控制流不一致
                        - 特定数组操作（push、splice、slice）中出错
                '''
            },
        ]
    },
    {
        "RootCause": RootCause["B"],
        "patterns": [
            {
                # "CVEs": ["CVE-2018-6149"],
                "rootc": "Type Conversion Errors",
                "vulp": '''
                    漏洞模式：类数组对象类型混淆
                    操作特征：
                        - 使用 `String.prototype.split.call` 等原型方法调用非字符串类型对象（如超大数组）
                        - 利用类数组对象在内部转换为字符串时引发边界处理错误
                        - 构造异常对象形态（如超大数组）作为隐式类型转换的目标
                        - 触发路径：内建方法 + 非标准 this 对象组合 + 隐式类型转换链
                '''
            },
            {
                # "CVEs": ["CVE-2021-21220"],
                "rootc": "Type Conversion Errors",
                "vulp": '''
                    漏洞模式：TypedArray边界数值溢出
                    操作特征：
                        - 利用 `Uint32Array([2**31])` 构造高位整数数组，制造边界数值异常
                        - 算术运算导致内部数值溢出，改变实际计算语义或优化路径
                        - 利用重复调用诱导引擎优化（JIT）对数组内容或数值类型的错误假设
                        - 最终触发类型预测失败，导致访问越界或整数精度错误
                '''
            },
            {
                # "CVEs": ["CVE-2023-3079"],
                "rootc": "Type Conversion Errors",
                "vulp": '''
                    漏洞模式：Arguments对象与数组结构混淆
                    操作特征：
                        - 使用 `arguments` 对象模拟数组行为，并动态添加浮点属性
                        - 在循环中对 arguments 与标准数组频繁切换，打破类型稳定性
                        - 属性名（如 `a1`）与索引位置交替使用，混淆内部结构优化路径
                        - 在 JIT 优化后访问浮点属性位置，最终导致类型错误或内存越界
                '''
            },
            {
                # "CVEs": ["CVE-2021-4078"],
                "rootc": "Type Conversion Errors",
                "vulp": '''
                    漏洞模式：Promise构造与继承关系破坏
                    操作特征：
                        - 自定义类继承自 `Promise`，但构造行为非标准化（无 resolve/reject）
                        - 构造时传入非预期的函数或类对象作为参数，影响对象状态初始化
                        - 引擎在类型推导中假设 `super()` 后一定返回合法 Promise 实例，受到破坏
                        - 导致后续方法调用过程中触发内部类型转换异常
                '''
            },
            {
                # "CVEs": ["CVE-2023-1214"],
                "rootc": "Type Conversion Errors",
                "vulp": '''
                    漏洞模式：结构化克隆与浮点属性混合污染
                    操作特征：
                        - 构造包含浮点属性的对象，并混入至共享数组中
                        - 在 `postMessage` 传递过程中触发结构化克隆算法
                        - 克隆算法未正确处理对象中混杂的整数索引与浮点属性，导致类型转换错误
                        - 利用 `Worker` 多线程环境引发时序差异，加剧漏洞触发概率
                '''
            },
            {
                # "CVEs": ["CVE-2023-6702", "CVE-2021-4078"],
                "rootc": "Incorrect Type Consistency Assumption",
                "vulp": '''
                    漏洞模式：异步类型链破坏
                    操作特征：
                        - 非标准构造返回值：自定义类继承 Promise，但构造函数中返回非原生 Promise 类型对象（如 `{}`），破坏引擎类型一致性假设
                        - thenable 伪装链式调用：构造对象伪装 Promise 接口，诱导引擎在异步链中执行错误路径
                        - GC 等副作用干扰：在异步回调关键节点触发垃圾回收等操作，加剧对象生命周期与类型推导混乱
                        - 类型破坏路径高度依赖异步调度时序，常规静态分析难以覆盖
                '''
            },
            {
                # "CVEs": ["CVE-2019-9791", "CVE-2017-8729", "CVE-2017-8740"],
                "rootc": "Incorrect Type Consistency Assumption",
                "vulp": '''
                    漏洞模式：构造函数路径诱导类型退化
                    操作特征：
                        - 重复构造触发内联缓存，使 JIT 假设对象结构稳定
                        - 使用特定控制流（如空循环、条件判断）制造“假优化”路径
                        - 关键构造阶段引入不同类型字段（如从 float 到 string），打破类型一致性
                        - 最终构造出的对象形态在结构上与优化期推导结果不一致，引发内存或语义错误
                '''
            },
            {
                # "CVEs": ["CVE-2018-0835", "CVE-2019-8506", "CVE-2018-8384"],
                "rootc": "Incorrect Type Consistency Assumption",
                "vulp": '''
                    漏洞模式：原型链与数组结构错配污染
                    操作特征：
                        - 通过动态设置数组或对象的 `__proto__` 属性，影响属性查找路径
                        - 使用 `Object.defineProperty` 添加 getter，污染数组索引访问行为
                        - 在引擎内部创建数组优化结构后，破坏其“稀疏”与“紧凑”状态一致性
                        - 当访问越过某种阈值（如高索引或 OOL 结构），可诱发属性解析或缓存错误
                '''
            },
            {
                # "CVEs": ["CVE-2019-9813", "CVE-2017-8634", "CVE-2019-5877"],
                "rootc": "Incorrect Type Consistency Assumption",
                "vulp": '''
                    漏洞模式：TypedArray 与伪对象结构注入
                    操作特征：
                        - 构造类 TypedArray 对象（如 Uint8Array）或使用 Proxy 替代其构造路径
                        - 动态原型变更与字段注入：注入包含 `buffer` / `length` 等关键字段的 JS 对象
                        - 编译器在类型推导中对该对象假设其为原生结构，实际访问时触发结构错配
                        - 易触发越界访问、属性漂移或内存错读
                '''
            },
            {
                # "CVEs": ["CVE-2021-30632", "CVE-2021-38007", "CVE-2018-0838"],
                "rootc": "Incorrect Type Consistency Assumption",
                "vulp": '''
                    漏洞模式：JIT 优化路径与对象字段偏移错误
                    操作特征：
                        - 使用调优原语进行优化路径控制
                        - 在对象字段被写入与读取之间引入时序扰动（如赋值、删除或原型变更）
                        - 优化阶段 JIT 会对字段偏移和类型进行错误假设
                        - 函数被优化后读取到意料之外的结构或数据，造成越界或泄露
                '''
            },
            {
                # "CVEs": ["CVE-2017-0071", "CVE-2017-8548", "CVE-2017-8601", "CVE-2017-11802", "CVE-2018-0953", "CVE-2018-8467", "CVE-2018-8355", "CVE-2018-0840", "CVE-2018-0770", "CVE-2018-11840"],
                "rootc": "Incorrect Type Speculation",
                "vulp": '''
                    漏洞模式：对象字段类型重写误推断
                    操作特征：
                        - 初期大量设置对象字段为某一类型（如 double），诱导优化器产生稳定类型假设
                        - 在关键节点替换字段值为不同类型（如 object），打破引擎优化路径下的类型一致性
                        - 常与 `valueOf`、`toString` 等隐式类型转换方法结合使用，实现时序劫持
                        - 导致 JIT 编译器在内联访问或数组操作中访问错误偏移或解释错误数据
                '''
            },
            {
                # "CVEs": ["CVE-2018-0933", "CVE-2018-0934", "CVE-2018-0776", "CVE-2018-0837"],
                "rootc": "Incorrect Type Speculation",
                "vulp": '''
                    漏洞模式：参数逃逸与调用栈滥用触发类型错判
                    操作特征：
                        - 使用 `inlinee.arguments[0]` 等手段将栈对象逃逸为堆引用，诱导类型边界模糊
                        - 在逃逸对象上进行类型回写，导致优化器在“原地假设”下执行类型错误操作
                        - 通常通过高索引属性或函数调用传播，伪装正常数据流
                        - 优化器未能检测到逃逸路径与动态类型插入，最终发生越界或解释偏差
                '''
            },
            {
                # "CVEs": ["CVE-2019-0567", "CVE-2019-0539", "CVE-2019-11707", "CVE-2019-17026", "CVE-2019-8820", "CVE-2018-4233"],
                "rootc": "Incorrect Type Speculation",
                "vulp": '''
                    漏洞模式：原型链及构造路径干扰推导结果
                    操作特征：
                        - 构造函数、类继承、原型链变更影响对象实例的结构感知
                        - 诱导引擎在某个构造路径上缓存类型结构（如属性布局、偏移）
                        - 后续实例被强行替换原型或注入污染字段，引擎在优化路径上读取错误位置
                        - 常见于函数内联与对象分配合并的优化场景中
                '''
            },
            {
                # "CVEs": ["CVE-2018-8266", "CVE-2018-8288", "CVE-2018-0834", "CVE-2018-8617", "CVE-2018-0743", "CVE-2018-0931"],
                "rootc": "Incorrect Type Speculation",
                "vulp": '''
                    漏洞模式：数组与对象交错结构诱导类型漂移
                    操作特征：
                        - 在数组上动态切换索引类型（数值索引与字符串属性交替）
                        - 插入对象字段污染数组内部结构（如对象作为数组元素，或混入方法）
                        - 引擎对数组或数组-like 对象进行优化时未正确处理其混合结构
                        - 常通过 `concat`、`reverse`、getter/setter 等方式触发推测误导
                '''
            },
            {
                # "CVEs": ["CVE-2020-6418", "CVE-2023-3420", "CVE-2022-42856", "CVE-2020-15656", "CVE-2017-5115"],
                "rootc": "Incorrect Type Speculation",
                "vulp": '''
                    漏洞模式：优化路径指令乱序与副作用引发错判
                    操作特征：
                        - 使用 Proxy、Reflect、Function 构造等制造副作用路径
                        - 在引擎尚未识别副作用时已经进行关键变量推测（如 pop 前触发 proxy getter）
                        - JIT 编译器产生的指令乱序、失效缓存或类型检查缺失使得访问顺序错位
                        - 极易在 Reflect.construct、instanceof、Function 构建、getter 调用中触发
                '''
            },
            {
                # "CVEs": ["CVE-2021-30517"],
                "rootc": "Type Misuse",
                "vulp": '''
                    模式名称：跨原型链的 `super.property` 类型误用
                    抽象语义：
                        - 定义类 A，修改其原型链使 `super` 实际指向非类对象（如 Function）
                        - 在子类方法中访问 `super.prop`，依赖构造层级推导
                    误用特征：
                        - 原型链被替换为 Function 或非标准构造对象
                        - `super.prop` 实际返回结构不符类型，破坏引擎对 this/context 的推导
                '''
            },
            {
                # "CVEs": ["CVE-2017-11914"],
                "rootc": "Type Misuse",
                "vulp": '''
                    模式名称：Getter 劫持返回非法类型并触发不匹配调用
                    抽象语义：
                        - 使用 `__defineGetter__` 劫持某对象属性访问
                        - 在 getter 内获取 this 并存储/返回
                        - 后续将该 this 当函数使用进行调用
                    误用特征：
                        - this 实际为 Function/Object 等混用
                        - 调用时参数类型/结构不匹配，突破类型假设
                '''
            },
            {
                # "CVEs": ["CVE-2018-8291"],
                "rootc": "Type Misuse",
                "vulp": '''
                    模式名称：Setter 注入破坏属性类型推导
                    抽象语义：
                        - 通过大量属性污染构建稳定结构
                        - 向关键全局属性注册 setter，拦截后续访问
                        - 属性访问触发隐式函数，打破类型/行为一致性
                    误用特征：
                        - setter 与原属性类型不符
                        - 优化阶段对该属性假设为常量或纯值，实际触发动态行为
                '''
            },
            {
                # "CVEs": ["CVE-2021-38001"],
                "rootc": "Type Misuse",
                "vulp": '''
                    模式名称：类继承路径中返回非构造函数导致 super.xxx 类型漂移
                    抽象语义：
                        - 构造类 A 的子类 B，B 的父类通过函数动态返回对象（非 class）
                        - super.xxx 实际引用非 class 实例中的成员
                    误用特征：
                        - `super` 推导路径动态变更
                        - 类构造器中访问 `super.xxx` 时超出了 V8 对构造层次结构的假设
                '''
            },
        ]
    },
    {
        "RootCause": RootCause["C"],
        "patterns": [
            {
                # "CVEs": ["CVE-2018-6143", "CVE-2019-6215", "CVE-2023-42852"],
                "rootc": "Missing Accessibility Check / Validation",
                "vulp": '''
                    漏洞模式：RegExp 子类化匹配结果伪造访问
                    操作特征：
                        - 自定义类继承 RegExp，重写 `exec()` 方法返回非标准结构（如篡改 `length`）
                        - 或通过修改原型链使 `input` 等属性指向不安全对象
                        - 引擎使用匹配结果进行属性访问时未验证其结构完整性或类型合法性
                        - 可触发任意对象字段访问或空指针解引用
                '''
            },
            {
                # "CVEs": ["CVE-2020-6507", "CVE-2020-6395", "CVE-2019-5843"],
                "rootc": "Missing Accessibility Check / Validation",
                "vulp": '''
                    漏洞模式：数组拼接与构造路径绕过长度校验
                    操作特征：
                        - 构造超大数组并使用 `concat()`、`splice()` 等方法引发内部 `length` 字段偏移
                        - 利用 `Reflect.construct` + `Proxy` 伪造构造上下文，触发对象创建路径异常
                        - 引擎未对拼接后数组的长度或边界访问进行充分校验
                        - 可实现数组对象形态破坏或越界字段读取
                '''
            },
            {
                # "CVEs": ["CVE-2018-6142", "CVE-2017-11861"],
                "rootc": "Missing Accessibility Check / Validation",
                "vulp": '''
                    漏洞模式：类型转换后未验证结构合法性
                    操作特征：
                        - 执行 `Map` 或 `Set` 构造函数传入伪造或非法结构（如清空的 iterable）
                        - 引擎依赖输入对象的结构约定（如 [k,v] 对格式），但未实际校验其值类型
                        - 导致异常对象结构参与后续流程，可能泄露堆内浮点值或触发异常行为
                '''
            },
            {
                # "CVEs": ["CVE-2022-46700"],
                "rootc": "Missing Accessibility Check / Validation",
                "vulp": '''
                    漏洞模式：国际化 API 参数滥用触发访问错误
                    操作特征：
                        - 构造 Intl.Locale 等对象时传入非法结构（如无效配置项）
                        - 内部访问依赖 `option` 对象的可选字段，但缺乏类型与存在性校验
                        - 导致 `undefined` 被访问为对象、属性链断裂等异常访问错误
                '''
            },
            {
                # "CVEs": ["CVE-2020-6395", "CVE-2019-5843", "CVE-2020-6507"],
                "rootc": "Missing Accessibility Check / Validation",
                "vulp": '''
                    漏洞模式：构造函数/原型路径伪造绕过校验
                    操作特征：
                        - 使用 `Reflect.construct()` 配合 `Proxy` 修改类构造流程
                        - 或在函数执行前动态修改其 prototype，注入非法 getter/setter 行为
                        - 引擎在构造对象后未验证关键内部属性是否受污染或缺失
                        - 可引发类型困惑、构造失败或属性访问混乱
                '''
            },
            {
                # "CVEs": ["CVE-2021-21224", "CVE-2019-5755", "CVE-2020-6383"],
                "rootc": "Incorrect Range Speculation",
                "vulp": '''
                    漏洞模式：条件控制变量极值误推断
                    操作特征：
                        - 关键变量值受布尔或时间函数控制（如 `(trigger ? -0 : 0)`、`Date().getMilliseconds()`）
                        - 优化器在热点路径中推测变量永远落在某一值域内，忽略极端触发条件（如 `Infinity`、`-1`、`0xffffffff`）
                        - 反复调用诱导 JIT 编译假设输入范围，再利用稀有分支打破该假设
                        - 导致整数范围裁剪失效，进入非法分支或构造非法内存结构
                '''
            },
            {
                # "CVEs": ["CVE-2019-5782", "CVE-2018-0769", "CVE-2020-6383", "CVE-2019-13764"],
                "rootc": "Incorrect Range Speculation",
                "vulp": '''
                    漏洞模式：数组长度/偏移推导错误
                    操作特征：
                        - 根据输入参数、arguments.length 或 typed array size 推断数组索引安全范围
                        - 构造极大索引（如 `(x >> 16) * 0xf00000`、`j += 0x100000`）误导引擎推断“不会越界”
                        - 实际访问数组未被分配的元素，引发内存写入越界或未初始化读取
                        - JIT 忽略了稀有高位索引或数组类型的真实边界
                '''
            },
            {
                # "CVEs": ["CVE-2021-21230", "CVE-2023-38595"],
                "rootc": "Incorrect Range Speculation",
                "vulp": '''
                    漏洞模式：数学函数组合造成边界绕过
                    操作特征：
                        - 大量使用如 `Math.min` / `Math.max` / `|0` 等显式边界控制
                        - 优化器假设函数处理后的结果总处于安全值域
                        - 恶意构造输入或表达式组合打破这一假设（例如溢出、负数进入乘法等）
                        - 最终导致逻辑断言失效或值域逃逸至错误路径
                '''
            },
            {
                # "CVEs": ["CVE-2019-13764", "CVE-2018-0769"],
                "rootc": "Incorrect Range Speculation",
                "vulp": '''
                    漏洞模式：循环步长与终止条件逻辑错配
                    操作特征：
                        - 在循环中改变步长（如 `step = end - begin`），或依赖外部变量控制索引增量
                        - 配合无效起始值（如 `Infinity`、极小负数）干扰 JIT 判断是否越界
                        - 优化器误认为循环稳定、不会越界，导致越界访问视为合法
                        - 常配合 TypedArray、ArrayBuffer 等结构进行边界逃逸
                '''
            },
            {
                # "CVEs": ["CVE-2019-5755", "CVE-2023-38595", "CVE-2021-21224"],
                "rootc": "Incorrect Range Speculation",
                "vulp": '''
                    漏洞模式：逻辑位运算参与的范围裁剪偏移
                    操作特征：
                        - 构造 `(trigger ? -0 : 0) - 0`、`>>>`、`|0` 等行为特殊的逻辑位运算表达式
                        - 在特定分支中产生非法值（如 `-0`、高位符号截断），突破正常推导路径
                        - 优化器误将位运算结果假设为稳定范围，忽略了输入变化可能带来的值域跳跃
                        - 造成逻辑短路失效、算术值爆炸或类型自动转换异常
                '''
            },
            {
                # "CVEs": ["CVE-2017-2536", "CVE-2017-2464", "CVE-2019-5790", "CVE-2018-0758"],
                "rootc": "Incorrect Boundary Calculation",
                "vulp": '''
                    漏洞模式：数组展开与拼接长度误算
                    操作特征：
                        - 利用 `...spread`、`.concat()`、`.splice()` 等操作隐式触发边界扩展
                        - 在大数组或重复展开中，长度字段未正确更新，导致溢出或截断
                        - 多次拼接后构建超长数组或字符串，引发内存破坏或性能退化
                        - 可结合 `apply`、`fill`、或变长结构模拟变形边界
                '''
            },
            {
                # "CVEs": ["CVE-2023-28204", "CVE-2018-17478", "CVE-2022-4174"],
                "rootc": "Incorrect Boundary Calculation",
                "vulp": '''
                    漏洞模式：字符编码与正则边界缺陷
                    操作特征：
                        - 使用 `String.fromCodePoint()` 构造 emoji 等多字节字符组合
                        - 搭配正则表达式（如 lookahead、gmu 修饰符）进行字符串替换或匹配
                        - 引擎未正确处理 Unicode 字符边界与正则分组匹配之间的偏移
                        - 最终造成字符串替换错位、索引偏移或异常终止
                '''
            },
            {
                # "CVEs": ["CVE-2017-8671", "CVE-2018-8139", "CVE-2020-15965"],
                "rootc": "Incorrect Boundary Calculation",
                "vulp": '''
                    漏洞模式：构造函数与 Proxy 调用边界遗漏
                    操作特征：
                        - 利用 Proxy 包装内建函数（如 Function.prototype.call），篡改调用栈行为
                        - 或在 `Reflect.construct()` 中传入非法 bind 目标或参数组合
                        - JIT/运行时未正确计算函数 `length`、参数边界或目标合法性
                        - 可触发栈结构破坏或调用越界异常
                '''
            },
            {
                # "CVEs": ["CVE-2022-1638", "CVE-2019-5790", "CVE-2017-8636"],
                "rootc": "Incorrect Boundary Calculation",
                "vulp": '''
                    漏洞模式：极大输入导致边界截断或错算
                    操作特征：
                        - 构造极大字符串（如 `"a".repeat(0xAAAAAAA)`）或数组参数列表
                        - 输入被用于格式化、解析、构造对象等路径中
                        - 引擎对总长度计算或边界校验未做充分处理
                        - 可导致输入溢出、内存分配异常或解析失败
                '''
            },
            {
                # "CVEs": ["CVE-2020-15965", "CVE-2018-8139"],
                "rootc": "Incorrect Boundary Calculation",
                "vulp": '''
                    漏洞模式：JIT 条件分支下边界回写错误
                    操作特征：
                        - 构造变量（如 `v16213`, `v25608`）在不同条件下被赋予极端值（如 `-0x80000000`）
                        - 配合 `Math.sign()`、`Array()` 及 `.shift()` / `.unshift()` 操作造成边界结构突变
                        - JIT 编译假设特定条件下数组大小固定，实际出现动态突变未更新访问路径
                        - 可造成 OOB 写或对象结构错乱
                '''
            },
            {
                # "CVEs": ["CVE-2021-21225", "CVE-2016-1646", "CVE-2020-16009", "CVE-2018-4443", "CVE-2017-2447"],
                "rootc": "Incorrect Structure Tracking",
                "vulp": '''
                    漏洞模式：数组结构与原型链污染交叉干扰
                    操作特征：
                        - 动态修改 `__proto__` 或定义原型 getter/setter 干扰数组行为（如 concat、slice）
                        - 在访问数组元素过程中改变 `length` 或 prototype 元素，制造结构不一致
                        - 配合自定义 `Symbol.species`、代理、异步 GC 操作放大影响
                        - 可造成数组迭代结构错乱、越界访问或内存混淆
                '''
            },
            {
                # "CVEs": ["CVE-2020-16009", "CVE-2023-4427", "CVE-2023-41074", "CVE-2019-0568", "CVE-2017-8635"],
                "rootc": "Incorrect Structure Tracking",
                "vulp": '''
                    漏洞模式：对象形态演变导致 map 状态不一致
                    操作特征：
                        - 对象属性按不同顺序、条件、构造方式赋值，诱导生成结构 map 冲突
                        - 配合内联缓存（IC）机制或 Map 验证语义制造引擎结构跟踪混乱
                        - 对象结构或原型链在逻辑判断中突变，破坏优化器预期的稳定性
                        - 导致属性绑定错乱、IC 错误命中或字段漂移
                '''
            },
            {
                # "CVEs": ["CVE-2023-38600", "CVE-2018-16065", "CVE-2017-0236", "CVE-2020-26950"],
                "rootc": "Incorrect Structure Tracking",
                "vulp": '''
                    漏洞模式：TypedArray 与 ArrayBuffer 状态跟踪错误
                    操作特征：
                        - 利用 `ArrayBuffer.resize`、`neuter`、`postMessage transfer` 操作提前/中途破坏 Buffer 状态
                        - TypedArray 尝试在 buffer 状态异常时继续访问，造成引用失效或指针漂移
                        - 关键路径触发点常为 `valueOf` / `copyWithin` 等内联操作或跨线程行为
                        - 可导致越界读取、UAF、对象空洞引用等问题
                '''
            },
            {
                # "CVEs": ["CVE-2018-6106", "CVE-2023-4355", "CVE-2020-15965", "CVE-2017-5030"],
                "rootc": "Incorrect Structure Tracking",
                "vulp": '''
                    漏洞模式：异步调度与 GC 干扰造成结构伪装
                    操作特征：
                        - 在异步流程中注入结构性变更（如 promise.then、gen.next、setTimeout 回调）
                        - 回调中执行对象销毁、数组扩容、原型变更等影响结构状态操作
                        - 垃圾回收（GC）与优化器状态缓存冲突，造成对象结构信息丢失或误判
                        - 常见触发路径为：promise、async generator、数组合并、构造函数重入
                '''
            },
            {
                # "CVEs": ["CVE-2018-4441", "CVE-2016-4622", "CVE-2017-11764", "CVE-2018-0767", "CVE-2021-21195"],
                "rootc": "Incorrect Structure Tracking",
                "vulp": '''
                    漏洞模式：解释器与 JIT 对结构跟踪语义不一致
                    操作特征：
                        - 字节码执行路径与 JIT 编译路径对同一结构对象产生不同推导
                        - 使用 `splice`、`shift`、大步长索引等方式打乱数组结构标识
                        - 触发路径中通过异常、try-catch、eval 等方式逃逸结构状态
                        - 最终在 IC、访问优化中造成结构预测失败，触发 OOB 或对象错解
                '''
            },
            {
                # "CVEs": ["CVE-2024-2625"],
                "rootc": "Improper Synchronization of Shared Data Structures",
                "vulp": '''
                    漏洞模式：子类继承链中 super.method 的绑定对象同步异常
                    操作特征：
                        - 构造多层类继承链（如 A -> B -> C）
                        - 每层类通过 `super.getValue()` 引用父类方法
                        - 使用静态 `extend()` 生成类后实例化，访问 `super` 方法
                        - 引擎未正确同步 `super` 调用中 `this` 的绑定，导致跨类引用泄漏或访问异常
                '''
            },
            {
                # "CVEs": ["CVE-2022-1364"],
                "rootc": "Improper Synchronization of Shared Data Structures",
                "vulp": '''
                    漏洞模式：Error.prepareStackTrace 与调用帧对象共享状态同步失效
                    操作特征：
                        - 自定义 `Error.prepareStackTrace`，访问 `stack` 中的调用帧
                        - 修改回调行为导致 `getThis()` 返回内部对象
                        - 多次执行过程中访问帧数据，未正确同步引用状态，造成对象错误重用
                        - 可通过对比对象身份验证两个内部对象是否被错误复用
                '''
            },
            {
                # "CVEs": ["CVE-2022-3652"],
                "rootc": "Improper Synchronization of Shared Data Structures",
                "vulp": '''
                    漏洞模式：稀疏数组的结构重建与对象类型未同步
                    操作特征：
                        - 构造稀疏数组 `[1.1, 2.2, , 4.4]`
                        - 调用一次包含 JIT 逻辑的函数使数组进入优化路径
                        - 在特定调用中将元素写为 `{}`，打破原类型假设
                        - 同步不及时造成对象在访问某索引时仍按旧类型访问，导致内存破坏或类型错误
                '''
            },
            {
                # "CVEs": ["CVE-2019-5813"],
                "rootc": "Improper Synchronization of Shared Data Structures",
                "vulp": '''
                    漏洞模式：排序回调执行中数组结构发生变化引起同步异常
                    操作特征：
                        - 在 `.sort()` 回调中执行 `Array.prototype.shift` 等修改结构的操作
                        - 回调中嵌套调用其他函数（如 JSON.parse 或 splice）
                        - 多次触发时数组的内部长度、类型信息与外部访问结构不同步
                        - 可利用此差异访问越界元素或伪造属性对象
                '''
            },
            {
                # "CVEs": ["CVE-2021-37991"],
                "rootc": "Improper Synchronization of Shared Data Structures",
                "vulp": '''
                    漏洞模式：闭包与绑定对象状态不同步导致对象访问异常
                    操作特征：
                        - 在 JIT 环境下构造多个闭包、对象链与属性调用
                        - 函数体内定义大量无意义结构用于打乱分析
                        - 关键逻辑中操作全局属性（如 this.d），调用 `.delete` 过程造成同步丢失
                        - 可能导致对象属性状态在不同闭包中被意外更改或回收
                '''
            },
        ]
    },
    {
        "RootCause": RootCause["D"],
        "patterns": [
            {
                # "CVEs": ["CVE-2023-4352", "CVE-2023-41993", "CVE-2022-3723", "CVE-2022-4906", "CVE-2019-8765"],
                "rootc": "Incorrect Optimization Algorithm",
                "vulp": '''
                    漏洞模式：对象结构推理错误（Map Assumption Mismatch）
                    操作特征：
                        - 通过类继承、自定义 getter/setter、动态替换原型等操作，使对象结构在运行时发生变化
                        - 优化器假设对象具有稳定结构（Map），而实际结构发生了演化
                        - JIT 编译路径访问属性时结构偏移，导致字段读取错乱或非法指针解引用
                        - 常结合 `Object.defineProperty`、`Symbol.species`、类字段初始化等特性
                '''
            },
            {
                # "CVEs": ["CVE-2021-30513", "CVE-2021-30598", "CVE-2022-2295", "CVE-2020-9802", "CVE-2021-30599", "CVE-2021-21227"],
                "rootc": "Incorrect Optimization Algorithm",
                "vulp": '''
                    漏洞模式：布尔与位运算折叠错误（Incorrect Constant Folding）
                    操作特征：
                        - 使用 `&`, `|`, `>>>`, `<<`, `Object.is`, `NaN`、`-0` 等组合进行判断或返回
                        - 优化器错误地将表达式优化为固定常量，未考虑 JS 语义细节
                        - 常在条件分支极简场景或恒等判断中出现（如 `-0 === 0`）
                        - 可导致逻辑分支偏离或类型预测错误
                '''
            },
            {
                # "CVEs": ["CVE-2018-8137", "CVE-2018-0777", "CVE-2017-0234", "CVE-2018-0980", "CVE-2018-8145", "CVE-2020-16040"],
                "rootc": "Incorrect Optimization Algorithm",
                "vulp": '''
                    漏洞模式：数组边界错误与越界写入
                    操作特征：
                        - 使用优化器未识别的动态 `start`、`end` 或步长控制数组写入逻辑
                        - 在训练阶段保持安全访问，在触发阶段传入大范围值导致越界
                        - 常见构造包括 loop 中 `i += 0`, `if (i === 10)`, 控制流跳转等
                        - 也可能出现 length 被提前设为超大值，数组回写未检查边界
                '''
            },
            {
                # "CVEs": ["CVE-2018-0860", "CVE-2018-4442", "CVE-2017-11893", "CVE-2019-8622", "CVE-2018-8229", "CVE-2017-11918"],
                "rootc": "Incorrect Optimization Algorithm",
                "vulp": '''
                    漏洞模式：类型推导残留与堆对象错读
                    操作特征：
                        - 训练期间函数被认为只访问某类对象（如普通数组），触发阶段通过原型劫持或重定义注入特殊对象
                        - 优化器未检测结构变化，导致类型判断错误，错误读取对象/值
                        - 通常与原型污染、正则残留状态、属性 getter 有关
                        - 后果包括堆地址泄漏、对象错解、字段漂移等
                '''
            },
            {
                # "CVEs": ["CVE-2020-6382", "CVE-2017-11909", "CVE-2018-4442", "CVE-2020-6468", "CVE-2023-23496", "CVE-2023-35074", "CVE-2019-8518"],
                "rootc": "Incorrect Optimization Algorithm",
                "vulp": '''
                    漏洞模式：控制流预测失败导致路径污染
                    操作特征：
                        - 训练阶段优化器认为某分支永远不被执行（如死代码消除、条件恒真）
                        - 触发阶段通过稀有路径（异常、try-catch、eval）让该分支实际运行
                        - 可引起未初始化变量、空结构访问、未验证操作
                        - 典型症状是优化后某值为 `undefined/null`，但代码试图访问其属性
                '''
            },
        ]
    },
    {
        "RootCause": RootCause["E"],
        "patterns": [
            {
                # "CVEs": ["CVE-2017-7056", "CVE-2017-8640", "CVE-2017-8670", "CVE-2017-11809"],
                "rootc": "Improper allocation",
                "vulp": '''
                    漏洞模式：展开参数配合继承触发不当 arguments 分配
                    操作特征：
                        - 利用 `new Function()` 构造超长参数调用构造函数；
                        - 子类继承自函数或匿名构造器，触发 `super()` 或隐式构造逻辑；
                        - 通过 `arguments` 长度变化与优化时机干扰堆栈状态；
                        - 多轮调用混合 GC 与延迟插桩，诱导 JIT 错误行为。
                '''
            },
            {
                # "CVEs": ["CVE-2018-8298", "CVE-2017-6984", "CVE-2017-15396", "CVE-2022-32893"],
                "rootc": "Improper allocation",
                "vulp": '''
                    漏洞模式：Intl 多态接口中的错误类型分配
                    操作特征：
                        - 传入非标准对象（如空对象、原型污染对象）作为 Intl 方法的接收者；
                        - 利用 `apply()`、`call()` 或类数组结构模拟内部上下文；
                        - Intl 构造过程中未正确验证内部 slot 或执行路径，错误分配内部结构；
                        - 特定属性访问可导致未初始化对象字段泄漏或崩溃。
                '''
            },
            {
                # "CVEs": ["CVE-2019-13670"],
                "rootc": "Improper allocation",
                "vulp": '''
                    漏洞模式：过度嵌套正则引发分配异常
                    操作特征：
                        - 利用 `RegExp` 构造中存在大量命名捕获组（Named Groups）；
                        - 正则解析时分配未能正确计算对象或数组大小；
                        - 匹配调用（如 `.match()`）时访问未初始化槽位；
                        - 常与 `String.prototype.match()` 配合使用。
                '''
            },
            {
                # "CVEs": ["CVE-2020-16042"],
                "rootc": "Improper allocation",
                "vulp": '''
                    漏洞模式：BigInt 边界移位引发值错误与类型错配
                    操作特征：
                        - 通过大数值位移操作生成边界值；
                        - JIT 未正确判断运算后值是否越界；
                        - 触发意料之外的类型转换或结果状态，导致内部结构非预期分配。
                '''
            },
            {
                # "CVEs": ["CVE-2024-0517"],
                "rootc": "Improper allocation",
                "vulp": '''
                    漏洞模式：类继承中构造顺序错配
                    操作特征：
                        - 类 B 继承类 A，构造中访问 `new.target` 与 `super()` 顺序冲突；
                        - `new.target` 引发早期对象访问但尚未执行 `super()`；
                        - 内部对象尚未初始化，JIT 优化时错误推测其结构；
                        - 搭配优化函数易放大问题。
                '''
            },
            {
                # "CVEs": ["CVE-2022-1310", "CVE-2019-13696"],
                "rootc": "Incorrect Reference Tracking",
                "vulp": '''
                    漏洞模式：引用劫持与替换时序竞争
                    操作特征：
                        - 在 RegExp.prototype.exec 等核心方法中手动劫持执行逻辑
                        - 在重写或执行的中间阶段触发 GC 或动态删除/恢复方法引用
                        - 使用 Symbol.replace 等语义路径触发对象属性访问与替换
                        - 利用方法链断裂过程中的引用不一致，造成内部状态泄露或逻辑混乱
                '''
            },
            {
                # "CVEs": ["CVE-2022-2158"],
                "rootc": "Incorrect Reference Tracking",
                "vulp": '''
                    漏洞模式：FinalizationRegistry 异常注册与引用失效
                    操作特征：
                        - 使用 FinalizationRegistry 注册弱引用对象与 token
                        - 在未释放引用或未触发 GC 情况下尝试 unregister
                        - 利用 WASM Memory 等大内存对象诱导垃圾回收策略调整
                        - 导致 register 状态不一致，引擎无法正确追踪引用关系
                '''
            },
            {
                # "CVEs": ["CVE-2018-4416"],
                "rootc": "Incorrect Reference Tracking",
                "vulp": '''
                    漏洞模式：跨作用域原型链引用更新失效
                    操作特征：
                        - 使用 `__proto__` 在循环中动态变更对象原型
                        - 嵌套执行 GC 干扰原型结构写入顺序
                        - 被观察对象处于引用链中的非首层，导致结构跟踪出错
                        - 在访问对象属性时返回已失效或未更新的引用值
                '''
            },
            {
                # "CVEs": ["CVE-2019-8558"],
                "rootc": "Incorrect Reference Tracking",
                "vulp": '''
                    漏洞模式：正则替换中的引用重构失败
                    操作特征：
                        - 使用 `String.replace(regexp, function)` 方式对字符串进行替换
                        - 在替换回调中构造大量临时对象或 TypedArray，并持久化其原型引用
                        - 多次递归执行替换逻辑触发结构缓存失效
                        - 替换回调与全局作用域共享数据结构导致引用指向错乱
                '''
            },
            {
                # "CVEs": ["CVE-2019-8558", "CVE-2022-1310"],
                "rootc": "Incorrect Reference Tracking",
                "vulp": '''
                    漏洞模式：RegExp 引擎状态漂移导致引用同步失效
                    操作特征：
                        - 多次使用正则对象进行状态相关操作（如 `.test()` / `.exec()`）
                        - 引擎内部对状态对象如 lastIndex 处理存在引用跟踪逻辑
                        - 中途修改正则对象方法（如 RegExp.prototype.exec）导致内部引用错位
                        - 利用数组原型链修改造成 lastIndex 异常恢复，诱发下游逻辑漏洞
                '''
            },
            {
                # "CVEs": ["CVE-2021-37975"],
                "rootc": "Incorrect Mark-and-Sweep",
                "vulp": '''
                    漏洞模式：WeakMap 链式嵌套中的标记漂移
                    操作特征：
                        - 构造多级 WeakMap 嵌套关系，使用对象链进行键值级联绑定
                        - 中间层通过隐藏键定位深层 Map，并在底层 Map 结构上进行多次 set/get 嵌套
                        - 配合 GC 或大内存分配（如 ArrayBuffer）打乱标记位传播顺序
                        - 引擎在回收过程中错误标记活跃引用，导致可访问对象提前清除或标记失效
                '''
            },
            {
                # "CVEs": ["CVE-2017-2491"],
                "rootc": "Incorrect Mark-and-Sweep",
                "vulp": '''
                    漏洞模式：RegExp 替换回调中 arguments 逃逸与回收错误
                    操作特征：
                        - 构造特大正则表达式（如 40w+ 分组）与替换字符串组合进行压力测试
                        - 使用 replace + 回调函数访问替换参数（即 arguments）
                        - 借助 GC 压力使得部分 arguments 被错误回收，进而暴露未标记的原始引用
                        - 利用 typeof 检测存活状态泄露 GC 漏标对象
                '''
            },
            {
                # "CVEs": ["CVE-2021-30536"],
                "rootc": "Incorrect Mark-and-Sweep",
                "vulp": '''
                    漏洞模式：闭包绑定与 async 函数重入造成的引用追踪丢失
                    操作特征：
                        - 使用 `Function.prototype.bind(...args)` 延迟绑定大量参数形成函数快照
                        - 异步函数闭包中引用旧绑定的 arguments（或变量作用域）
                        - 绑定对象在后续执行中被替换（如 `var14 = var11`），但闭包中仍存在旧引用
                        - 引擎在 GC 时未能识别闭包中的延迟绑定引用，导致访问 UAF 对象或空引用异常
                '''
            },
        ]
    },
    # {
    #     "RootCause": RootCause["F"],
    #     "patterns": [
            
    #     ]
    # },
]