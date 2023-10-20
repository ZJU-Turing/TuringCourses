# 汇编语言
<div class="badges">
<span class="badge is-badge">IS 专业必修</span>
<span class="badge cs-badge">CS 专业选修</span>
<span class="badge ai-badge">AI 专业选修</span>
</div>

## 课程学习内容
汇编语言这门课的主要内容就是学习较为古老的 8086 汇编、80386 的一小部分 32 位指令以及一小部分的 80386 保护模式基础知识。

!!! note "注意"
    除此之外还有一门课程叫 “汇编语言程序设计基础”（俗称长名汇编），是一门通识课，内容差不太多，但是作业和考试都要简单一些，只有短名的“汇编语言”是培养方案中写的 IS 专业必修、CS/AI 专业选修，选课时要注意一下。

## 任课教师
浙江大学《汇编语言》课程数十年来只有一位老师：**白洪欢**。

老师富有个性，上课硬核，擅长当黑客、逆向、密码学、拆东西。也是 AAA 战队的指导老师。白老师有自己的课程网站，会有学习汇编语言专用的虚拟机。虽然讲的内容很老，甚至可以说是过时的，但是小白老师也是少有的能将一门课讲清楚、讲透的老师。不过 22 年的汇编课可能由于考试有些难，普遍作业、考试完成的不够好，导致小白老师有些不满意，最后成绩普遍较低。

## 授课教材
这门课的教材是小白老师自己写的书，不过不是通过教务网来预订的，而是在上几周课后会发通知来买这本书。是 A4 纸印刷、装订的一本“书”，涵盖了本门课程的全部知识点，上课没跟上的可以好好看看书。

除此之外，每节课程小白老师都是通过 word 文档来讲授，这些文档都可以在他的主页 [cc.zju.edu.cn/bhh](http://cc.zju.edu.cn/bhh) 上找到。

## 分数构成
四次作业（40%）+期末考试（60%）

作业是用纯 8086 汇编来写程序，会逐次变难，最后一次相当于大作业，一般是写游戏（20 级推箱子，21 级走迷宫），不过后几次作业都会给对应的 C 语言源码，大概只需要翻译、调试。

期末考试是纯笔试，有判断、填空、阅读程序、补全程序等类型的题目。考试偏理论，需要好好复习一下，特别是 21 年保护模式考了很多，不复习的话根本不知道怎么答。以及课上讲的指令一定都要清楚作用是什么，否则可能所有程序都读不懂（因为每个程序都比较综合）。

## 推荐书单
- *《汇编语言》* 王爽，清华大学出版社（经典汇编课本，第一推荐）
- *《x86汇编语言-从实模式到保护模式》* 李忠，电子工业出版社（经典汇编课本）
- *《琢石成器》*罗云斌，32 位汇编
- *《软件调试》* 张银奎（各类底层硬件机制和调试方法）
- *《汇编语言程序设计》* 白洪欢，科学出版社（已绝版，就是老师自己印的那本）
- *《IBM-PC汇编语言程序设计》* 沈美明，清华大学出版社（比较老的中文教材）
- *《Windows汇编语言程序设计教程》* 谭毓安 ，电子工业出版社（比较老的中文教材）
- *Professional Assembly Language*, Richard Blum
- *The Art of Assembly Language*, Randall Hyde （不过这个系列使用的主要工具是 HLA，与一般的汇编差别较大）
- *The Art of 64-bit Assembly*, Randall Hyde
- *Assembly Language for x86 processors*, Kip R. Irvine（一本内容丰富的汇编书籍，电子工业出版社的黑皮系列里有。目前最新版是第 8 版）
- *Modern x86 Assembly Language Programming*, Daniel Kusswurm（少数能称得上 Modern 的汇编书）
- *Beginning X64 Assembly Programming*, Jo Van Hoey（不错的入门书, 64 位）
- *Assembly Language for Intel-Based Computers*, Kip Irvine（32 位）
- *Practical Malware Analysis*, Michael Sikorski,  Andrew Honig（二进制分析，病毒分析，逆向工程，侧重实战）
- [*Intel 80386 Programmer’s Manual*](https://pdos.csail.mit.edu/6.828/2018/readings/i386/toc.htm), 以及 *[Intel 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)* 
- *[Microsoft Macro Assembler reference](https://learn.microsoft.com/en-us/cpp/assembler/masm/microsoft-macro-assembler-reference?view=msvc-170)*

还有一些可以看的网课：

+ 华中科技大学：[汇编语言程序设计](https://www.bilibili.com/video/BV1Nt411V7fa)
+ 西安交通大学：[微机原理与接口技术](https://www.icourse163.org/course/xjtu-1001647001)（不全讲汇编，侧重硬件）
+ 清华大学：[汇编语言程序设计](https://www.xuetangx.com/course/THU08091000320/14767518)（推荐）

一些工具：

- [EMU8086-Microprocessor Emulator](https://emu8086-microprocessor-emulator.softonic.com/)
- [Godbolt Compiler Explorer](https://www.godbolt.org)
- [x86 Processor Information](https://www.sandpile.org)

## 参考笔记
- xg 的汇编笔记：https://note.tonycrane.cc/cs/pl/asm/
- https://www.cc98.org/topic/5239637

## 学长组课程学习建议

!!! abstract
    21 级学长组编写、22 级学长组修改后的学习建议。

本课程不需要额外教材，在几节课之后老师会让大家预定（一定不要忘了），是小白老师自己写的教材，看这本书足够应对这门课了。另外清华大学王爽《汇编语言》这本书也可以起到帮助。

小白老师上课知识点讲的很细，基本上结合例子来讲，但是也有不少人认为老师讲课不成体系。上课建议好好听，跟紧老师思路，最好要做笔记（比如笔记本上打开一个文档记下老师的操作）。老师对学生态度很好，在课前问问题会坐在你旁边手把手教你改代码。

一定要好好利用上课笔记、小白老师提供的笔记，98 上也能找到复习资料。据说上一届小白老师会在课程结束后删掉智云回放，不过这一届没有。但是这门两节课的课小白会在第一节课就明确地说会上三课时，也就是说最后一课时的内容在智云课堂上是没有回放的，因此建议上课认真听认真记笔记，特别是最后一课时。

课程的分数分为两部分：作业和考试。一共会有四次作业，代码量逐次提高，后两次是提供 C 语言代码，要将其翻译成汇编语言。作业都会比较耗时间，而且汇编语言调试起来比较麻烦，推荐留下作业后尽快完成，不要拖 ddl。最后一两次作业会花掉将近一周的时间，要有所准备。如果没能在 ddl 前完成也记得要把自己写了的东西交上去，而且最后一次作业应该会有补交的机会。上一届的最后一次作业是写推箱子游戏，汇编代码大概两三千行左右，这一届简单了很多，是写随机生成迷宫、走迷宫的程序，大概一千行左右，不知道你们这一届怎么样。

对于实验环境，小白会给一个 xp 虚拟机，里面是带有需要的软件的，不过整体还是很臃肿的。vscode 上有一个 dosbox 插件，也是可以用的，这样就不用在虚拟机里 debug 了（最后还是要在虚拟机里跑一下的，以免在老师那里出错）。

对于最后的考试，建议在考前好好看一看书，一些指令要记牢。考试内容是几个判断几个填空，程序填空和阅读程序填写结果。相信四次作业能完成的考试也不会差。只要理解了汇编语言、记住了指令，程序填空和阅读程序问题不大。判断填空会有一些基础的知识点，和一些保护模式的知识点，想要拿满的话要注意一下这些。复习/学习的时候可以参考一下 xg 的这篇笔记 https://note.tonycrane.cc/cs/pl/asm/，基本包含了这门课的所有知识点。
