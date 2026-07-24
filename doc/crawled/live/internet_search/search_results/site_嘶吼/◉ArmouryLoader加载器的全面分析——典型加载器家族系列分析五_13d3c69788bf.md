# ◉ArmouryLoader加载器的全面分析——典型加载器家族系列分析五

### 来源信息
- **URL**: https://www.4hou.com/posts/xyE9
- **来源站点**: 嘶吼
- **页面抓取**: 成功

### 页面正文
引言
随着网络攻击技术的不断演变，恶意代码加载器逐渐成为恶意代码执行的关键组成部分。此类加载器是一种用于将各种恶意代码加载到受感染的系统中的恶意工具，通常负责绕过系统安全防护，将恶意代码注入内存中并执行，为后续的特洛伊木马类型恶意代码的部署奠定基础。加载器的核心功能包括持久性机制、无文件内存执行以及多层次规避技术。
安天CERT将近几年历史跟踪储备的典型恶意加载器家族有关信息汇总成专题报告，并持续追踪新的流行加载器家族。本项目专题将聚焦加载器技术细节，深入挖掘其在攻击链中的核心功能，包括其混淆技术、加密机制以及注入策略等。此外，我们也会不断完善自身安全产品能力，采取有效技术方案进一步提升针对加载器的识别率和准确率，帮助用户组织提前发现并阻止潜在威胁。
1 概述
ArmouryLoader加载器最早于2024年被发现，曾被用于投递SmokeLoader和CoffeeLoader等恶意代码家族。该加载器通过劫持华硕Armoury Crate系统管理软件的导出函数进行加载，因此被命名为ArmouryLoader。ArmouryLoader加载器具备提权、持久化以及投递目标载荷的功能，并具有一定对抗EDR（端点检测和响应）能力，使后续投递的载荷更容易突破系统防线。
ArmouryLoader在加载阶段会调用OpenCL解密载荷，需要运行环境具有GPU或32位CPU才能正常运行，能够起到规避沙箱和虚拟机环境的作用。ArmouryLoader在投递目标载荷时，还会利用系统中合法DLL的代码段来读取敏感内存、调用系统函数，并在此基础上伪造调用栈，隐藏系统调用的发起者，以此来规避EDR检测。通过以上手段，ArmouryLoader具有较强的隐蔽性，使其在沙箱和终端环境均难以被检测，提高了目标载荷投递的成功率，对用户的系统安全构成威胁。
该加载器详细信息参见安天病毒百科。
图 1‑1长按识别二维码查看HijackLoader加载器详细信息
2 ArmouryLoader加载器生存技术举例分析
2.1 混淆技术分析
ArmouryLoader具有三种混淆代码的方式，分别为增加无用指令、代码自解密和使用OpenCL解密。
其中ArmouryLoader在第一阶段和第三阶段拥有无用指令填充的混淆代码。
图 2‑1ArmouryLoader添加的无用指令
在第二、四和六阶段均有自解密代码以干扰分析。
图 2‑2Armoury自解密代码
此外ArmouryLoader在第三阶段还会用OpenCL解密代码，增加分析难度并增加了对运行环境设备的要求。
图 2‑3ArmouryLoader使用OpenCL解密代码
2.2 提权技术分析
ArmouryLoader在第五阶段会尝试使用CMSTPLUA COM组件进行提权，在提权时ArmouryLoader会将自身伪装成explorer.exe，随后调用提权函数获取Administrator权限。
图 2‑4ArmouryLoader使用COM组件进行提权
2.3 持久化技术分析
ArmouryLoader会通过计划任务实现持久化。根据版本不同，ArmouryLoader会使用系统工具schtasks或计划任务COM组件实现持久化。
无论持久化的方式如何，当具有管理员权限时，ArmouryLoader会选择通过用户登录触发并获取最高权限，否则ArmouryLoader将会以普通权限每隔30分钟执行一次。
图 2‑5以最高权限运行的计划任务
此外ArmouryLoader还会对持久化的文件加以系统、隐藏和只读属性，并修改ACL拒绝用户修改和删除文件。
图 2‑6ArmouryLoader设置文件属性
2.4 对抗技术分析
ArmouryLoader会通过合法DLL中的特殊gadget读取敏感位置内存。
图 2‑7ArmouryLoader通过gadget读取敏感内存数据
ArmouryLoader在第三阶段和第八阶段调用敏感函数时还会通过伪造调用栈避免检测。
图 2‑8ArmouryLoader伪造函数调用栈
ArmouryLoader还会通过Halo's Gate获取系统函数调用号，具有一定的反syscall hook能力，能够直接进行系统调用。
图 2‑9ArmouryLoader使用Halo's Gate技术搜索系统调用号
3 攻击流程
ArmouryLoader共具有八个阶段，每个阶段相对独立，分步完成最终载荷的投递工作。ArmouryLoader的一、三、五、七阶段负责完成特定的恶意行为，而二、四、六、八阶段负责加载下一阶段的PE载荷。
表 3‑1ArmouryLoader不同阶段恶意行为
| 加载阶段 | 恶意行为 | 
| 第一阶段 | 劫持Armoury Crate导出函数，运行第二阶段shellcode | 
| 第二阶段 | 解密并运行第三阶段PE文件 | 
| 第三阶段 | 通过OpenCL解密并运行第四阶段shellcode | 
| 第四阶段 | 解密并运行第五阶段PE文件 | 
| 第五阶段 | 进行提权及持久化，并运行第六阶段shellcode | 
| 第六阶段 | 解密并运行第七阶段PE文件 | 
| 第七阶段 | 将第八阶段的shellcode注入到64位dllhost.exe | 
| 第八阶段 | 加载并运行目标载荷 | 
4 样本分析
4.1 样本标签
表 4‑1ArmouryLoader样本标签
| 病毒名称 | Trojan/Win32.ArmouryLoader | 
| 原始文件名 | ArmouryA.dll | 
| MD5 | 5A31B05D53C39D4A19C4B2B66139972F | 
| 处理器架构 | x86 | 
| 文件大小 | 1.41 MB (1,480,552 字节) | 
| 文件格式 | BinExecute/Microsoft.EXE[:X86] | 
| 时间戳 | 2023-12-13 15:31:16 | 
| 数字签名 | ASUSTeK COMPUTER INC.（数字签名无效） | 
| 加壳类型 | 无 | 
| 编译语言 | Microsoft Visual C/C++(19.16.27049) | 
| VT首次上传时间 | 2024-09-12 18:34:23 | 
| VT检测结果 | 33/72 | 
4.2 ArmouryLoader加载器第一阶段
ArmouryA.dll是华硕Armoury Crate程序的一部分，ArmouryLoader加载器通过劫持ArmouryA.dll导出函数freeBuffer实现运行。
该函数中包含有大量无用代码以干扰安全人员对其分析，并最终会解密并执行第二阶段载荷。
图 4‑1ArmouryLoader解密并执行第二阶段代码
4.3 ArmouryLoader加载器第二阶段
在ArmouryLoader第二阶段，拥有大量自解密代码以阻碍静态分析。
图 4‑2ArmouryLoader自解密代码
在第二阶段，ArmouryLoader会通过PEB加载CreateThread函数，并创建一个新线程执行后续逻辑。
图 4‑3ArmouryLoader创建新线程执行后续逻辑
在新线程中，ArmouryLoader会从二阶段载荷中读取第三阶段的PE文件，并加载到内存中执行。
图 4‑4ArmouryLoader加载第三阶段PE文件
4.4 ArmouryLoader加载器第三阶段
在第三阶段，ArmouryLoader会加载OpenCL库，并通过OpenCL解密第四阶段载荷。该阶段会通过OpenCL库调用Nvidia、AMD或Intel设备进行shellcode解密。
图 4‑5ArmouryLoader寻找OpenCL可用设备
随后ArmouryLoader会将两个字符串异或生成解密密钥，再将密钥与密文传入OpenCL设备中进行异或解密，得到下一阶段的shellcode进而执行。
图 4‑6ArmouryLoader使用OpenCL设备解密shellcode
在后续的版本中，该阶段载荷增加了大量混淆，使其难以分析。
图 4‑7ArmouryLoader第三阶段混淆
在后续版本中，还对通过构造ROP链的方式对函数的帧栈进行伪造以对抗栈回溯。以程序调用GetModuleHandleW为例，该图中函数将会通过ret 4指令将EIP设置为GetModuleHandleW函数地址，随后再出栈四个字节。此时栈顶将留下GetModuleHandleW函数的返回地址RtlCreateMemoryBlockLookaside+88，以及函数的参数OpenCL.dll的字符串指针。其中RtlCreateMemoryBlockLookaside+88实际上为jmp [EBX]的汇编指令，当GetModuleHandleW函数返回时，将会从EBX地址中读取函数真正的返回值，并设置到EIP上，以归还程序的控制流。
图 4‑8ArmouryLoader构造ROP链对抗栈回溯
4.5 ArmouryLoader加载器第四阶段
在第四阶段，ArmouryLoader将解密并加载第五阶段PE文件并在内存中执行。
该阶段同样拥有自解密逻辑，但加密的层数较少，并使用loop指令控制循环而非第二阶段的jnz。
图 4‑9ArmouryLoader执行自解密逻辑
在完成解密后ArmouryLoader将会在内存中加载PE文件并执行。
图 4‑10ArmouryLoader加载PE文件到内存
4.6 ArmouryLoader加载器第五阶段
在第五阶段，ArmouryLoader会先检测程序是否具有提升权限或属于System用户组，并根据权限的不同选择不同的持久化位置。
图 4‑11ArmouryLoader检测进程权限
随后ArmouryLoader会复制自身到%PROGRAMDATA%或%LOCALAPPDATA%下，并设置文件系统、隐藏和只读属性。
图 4‑12ArmouryLoader移动自身到特定目录
之后ArmouryLoader还会添加文件的ACL列表来禁止用户删除或修改自身程序。
图 4‑13ArmouryLoader修改文件ACL列表
之后ArmouryLoader会通过schtasks创建一个名为AsusUpdateServiceUA每隔30分钟运行一次的计划任务来实现持久化。
图 4‑14ArmouryLoader通过schtasks创建计划任务实现持久化
如果具有管理员权限，ArmouryLoader则会在用户登录时以最高权限执行。
图 4‑15ArmouryLoader以最高权限运行计划任务
在较新的版本中，ArmouryLoader会尝试利用COM组件进行提权，此时ArmouryLoader会先修改PEB和LDR_DATA_TABLE_ENTRY中的进程信息。
图 4‑16ArmouryLoader修改进程信息
随后通过COM组件CMLuaUtil进行提权。
图 4‑17ArmouryLoader使用COM组件进行提权
在后续更新中，ArmouryLoader使用COM组件替代schtasks程序来创建计划任务。
图 4‑18ArmouryLoader使用COM组件创建计划任务
当不具有System权限时，计划任务将每10分钟触发一次。
图 4‑19ArmouryLoader设定每10分钟触发一次的计划任务
当具有System权限时，ArmouryLoader将设置以最高权限运行程序。
图 4‑20ArmouryLoader设置计划任务运行权限
此时ArmouryLoader计划任务将登录触发。
图 4‑21ArmouryLoader设置计划任务登录触发
随后运行shellcode执行下一阶段。
图 4‑22ArmouryLoader执行第六阶段载荷
4.7 ArmouryLoader加载器第六阶段
第六阶段与第四阶段样本功能相同，负责解密和加载下一阶段PE文件。
图 4‑23ArmouryLoader完成重定向工作并调用下一阶段PE文件入口点
4.8 ArmouryLoader加载器第七阶段
在第七阶段，ArmouryLoader将创建64位的dllhost.exe进程，并将shellcode注入其中，以将运行环境从32位更改为64位。
ArmouryLoader首先关闭文件重定向，并创建一个64位的dllhost.exe进程。
图 4‑24ArmouryLoader关闭文件重定向
随后ArmouryLoader会搜索一些64位的DLL以便劫持主进程，在该过程中ArmouryLoader将频繁使用天堂之门技术执行64位代码。
图 4‑25ArmouryLoader通过天堂之门执行64位代码
通过天堂之门，ArmouryLoader可以调用64位DLL中的函数。如图所示，ArmouryLoader通过get_dll64、get_func64和call_func64可以实现64位函数的搜索和调用。再对特定的函数进行封装以实现像调用普通函数一样调用64位函数。
图 4‑26ArmouryLoader对64位的NtGetContextThread进行封装
最后通过劫持主进程的方式在dllhost.exe中执行64位shellcode。
图 4‑27ArmouryLoader劫持64位dllhost.exe主进程
4.9 ArmouryLoader加载器第八阶段
在第八阶段，ArmouryLoader首先会获取ZwAddBootEntry、NtAllocateVirtualMemory和NtProtectVirtualMemory函数地址，并搜索对应的系统调用号。
图 4‑28Armoury搜索函数及系统调用号
在新版ArmouryLoader中，ArmouryLoader会在ntdll中搜索mov rax,[rax];ret;的gadget，并通过该gadget读取敏感内存区域，以欺骗EDR读取行为是由ntdll发出的。
图 4‑29ArmouryLoader通过gadget间接读取数据
ArmouryLoader会尝试在函数中搜索特定字节序列来获取调用号。
图 4‑30ArmouryLoader搜索系统调用号
如果目标函数被hook，则会导致ArmouryLoader搜索字节序列失败，进而导致无法获取系统调用号。此时ArmouryLoader会使用Halo's Gate技术进一步搜索系统调用号。该技术将搜索邻近的Zw函数，从中获取系统调用号。并根据搜索到的临近函数与目标函数之间的距离推算出目标函数的系统调用号。
图 4‑31ArmouryLoader使用Halo's Gate技术搜索系统调用号
在新版ArmouryLoader中，该算法进一步完善。ArmouryLoader不再假定Zw函数大小为32字节，而通过遍历函数导出表计算出最小的Zw函数间距，从而获取Zw函数大小。
图 4‑32ArmouryLoader计算Zw函数最小间距
在搜索完系统调用号后，ArmouryLoader会使用NtAllocateVirtualMemory和NtProtectVirtualMemory为最终的目标载荷申请内存空间。该过程中ArmouryLoader会先计算将会使用ZwAddBootEntry函数中的syscall配合系统调用号调用系统函数。并在这基础上伪造调用栈。
该过程将在kernel32.dll中搜索jmp [rbx]的gadget，用于在函数调用结束后返还控制流。
图 4‑33Armoury搜索jmp [rbx] gadget
随后ArmouryLoader通过.pdata节中的ExceptionDir获取函数对应的RUNTIME_FUNCTION信息，从而寻找函数的UnwindInfo，其中UnwindInfo包含了函数的帧栈大小信息。
图 4‑34ArmouryLoader搜索函数的RUNTIME_FUNCTION信息
之后ArmouryLoader通过UnwindInfo计算jmp [rbx] gadget所在函数以及BaseThreadInitThunk和RtlUserThreadStart的帧栈大小，用于后续的伪造。
图 4‑35ArmouryLoader计算函数栈大小
随后ArmouryLoader将jmp [rbx] gadget置于syscall的返回地址，而函数真正的返回地址的指针置于rbx寄存器中以实现返还控制流。并在后续的调用栈上将部署BaseThreadInitThunk和RtlUserThreadStart函数的帧栈，以欺骗EDR让其误以为syscall是从RtlUserThreadStart到BaseThreadInitThunk再经由kernel32中某个函数发出的。
图 4‑36ArmouryLoader伪造调用栈
在分配完内存空间后，ArmouryLoader将最终的目标载荷复制到指定内存区域，并完成重定向工作，调用程序入口点完成投递。根据最终的C2域名可知，ArmouryLoader投递的目标载荷为CoffeeLoader。
图 4‑37CoffeeLoader C2地址
5 IoCs
| IoCs | 
| 5A31B05D53C39D4A19C4B2B66139972F | 
| 90065F3DE8466055B59F5356789001BA | 
6 样本对应的ATT&CK映射图谱
图 6‑1技术特点对应ATT&CK的映射
具体ATT&CK技术行为描述表：
表 6‑1ATT&CK技术行为描述表
| ATT&CK阶段/类别 | 具体行为 | 注释 | 
| 持久化 | 利用计划任务/工作 | ArmouryLoader通过计划任务实现持久化 | 
| 滥用提升控制权限机制 | 滥用提升控制权限机制 | ArmouryLoader通过COM组件进行提权 | 
| 防御规避 | 反混淆/解码文件或信息 | ArmouryLoader拥有大量异或加密的代码段 | 
| ArmouryLoader通过OpenCL解密代码 | ||
| ArmouryLoader通过天堂之门执行64位代码 | ||
| 修改文件和目录权限 | ArmouryLoader通过添加ACL记录禁止用户更改和删除 | |
| 隐藏行为 | ArmouryLoader为持久化的文件添加隐藏、系统和只读属性 | |
| 间接执行命令 | ArmouryLoader通过系统DLL gadget读取目标内存 | |
| ArmouryLoader通过syscall直接调用系统函数 | ||
| ArmouryLoader伪造调用函数调用栈 | ||
| 仿冒 | ArmouryLoader伪装华硕系统管理软件，具有无效的数字签名 | |
| 混淆文件或信息 | ArmouryLoader代码具有混淆 | |
| ArmouryLoader通过哈希检索API | 
7 安天智甲助力用户防御加载器威胁
经过测试，安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀和防御本次发现病毒样本。
智甲可对本地磁盘进行实时监测，对新增文件自动化进行病毒检测。针对此次威胁，当用户通过接收邮件附件、微信传输、网络下载等方式将ArmouryLoader加载器存储至本地时，智甲会立即对该病毒进行告警并清除恶意文件，防止用户启动文件导致终端遭受攻击。
图 7‑1发现病毒时，智甲第一时间捕获并发送告警
智甲还为用户提供统一管理平台，管理员可通过平台集中查看网内威胁事件详情，并批量进行处置，提高终端安全运维效率。
图 7‑2智甲管理中心助力管理员实现高效的终端安全管理
附录：安天澜砥威胁检测分析垂直大模型自动化分析结
安天澜砥威胁检测分析垂直大模型能对样本进行自动化分析，部分解析内容如下：
根据提供的日志和分析结果，以下是详细的判定结论和解释：
1.判定结论
评估结果：可疑（准确度：约95%）
1.详细解释
2.特征匹配与判定依据：
恶意API调用：日志中多次出现与证书相关API的调用，如GetDeviceIndex、FreeEnvironmentStrings、CertGen等。这些API通常用于处理证书和安全相关的任务，恶意软件常利用这些API进行恶意操作，如绕过证书验证、获取私钥等。
字符串分析：日志中包含大量与证书相关的URL和字符串，例如crl3.digicert.com、ocsp.digicert、cacerts.digicert.com等。这些域名通常与数字证书相关的CA机构相关。
混淆与编码：日志中出现的混淆代码片段（如??表示未被选中作为特征使用）可能用于隐藏恶意行为，增加了检测的难度。
异常行为模式：日志中多处出现重复的字节模式（如04 81 AD 30 81 AA 30 53 A0 51 A0 4F 86 4D 68 74 74 70 3A 2F 2F 63 72 6C 33 2E 64 69 67 69 63 65 72 74 2E 63 6F 6D），可能用于数据填充或隐藏恶意代码。
·恶意代码特征：
证书相关操作：存在与证书相关的API调用，可能用于获取、验证或使用证书进行恶意通信。
混淆与加密：日志中包含大量混淆代码，增加了检测的复杂性，可能用于隐藏恶意行为。
异常字符串：出现多个与数字证书相关的域名和路径，可能用于绕过安全检测或进行恶意通信。
·评估准确度：
高可信度特征：日志中存在多个与恶意代码特征匹配的特征，增加了检测的准确性。
潜在的模糊性：部分特征（如??表示未被选中作为特征使用）可能隐藏了恶意行为，但整体特征仍显示出较高的可疑性。
·结论
根据上述分析，日志中包含多个与证书相关且可疑的API调用和字符串，这些特征符合恶意软件的典型行为模式。因此，分析工具判定该文件为Trojan.Win32.ShipCome（或类似的恶意软件家族）是合理的。
准确度评估：约95%
按照国标草案给出威胁分类为Trojan.Win32.SpyBind，自动提取特征生成的YARA规则如下：
rule Trojan.Win32.ShipCome:Trojan {
   meta:
      description = "这是一段由 VILLM V2 模型生成的 YARA 规则。用于检测Trojan.Win32.ShipCome"
   strings:
    $a = {f7 d3 4f 33 f8 c1 c6 17}
    $b = {c1 ce 17 33 f8 47 f7 d3}
    $c = {4e 33 c3 33 cf f7 d0 33 c5 c1 cf 17 4e 4b}
    $d = {f7 d0 f7 d0 87 c7 f7 d2}
    $e = {4b 33 cd 87 c1 ff e0}
   condition:
      all of them
}安天澜砥威胁检测分析垂直大模型是国内首个通过国家网信办备案的威胁检测生成式算法。模型基于安天赛博超脑20余年积累的海量样本特征工程数据训练而成，训练数据包括文件识别信息、判定信息、属性信息、结构信息、行为信息、主机环境信息、数据信息等，支持对不同场景下向量特征进行威胁判定和输出详实的知识理解，形成应用不同需求和场景的多形态的检测方式，提升后台隐蔽威胁判定能力，进一步为安全运营赋能。
图 8‑1安天澜砥威胁检测分析垂直大模型样本分析结果
参考资料
[1]. 安天.Trojan/Win32.ArmouryLoader病毒详解与防护-计算机病毒百科[R/OL].(2025-07-07)
 https://www.virusview.net/malware/Trojan/Win32/ArmouryLoader
发表评论

---
*爬取时间: 2026-07-24 21:55:23*
*来源: 直接站点爬取*
