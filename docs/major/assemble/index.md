---
grave: https://zju-turing.github.io/TuringCoursesGrave/major_mandatory/assemble/
---

# 汇编语言程序设计与调试

## 课程学习内容

汇编语言程序设计与调试这门课的主要内容就是学习较为古老的 8086 汇编、80386 的一小部分 32 位指令以及其它一些安全相关的知识。25-26 春夏学期老师原本还计划讲保护模式的相关内容但没来得及讲，可能后面几届的课会涉及。

## 任课教师

从这门课的前身《汇编语言》到《汇编语言程序设计与调试》这门课，数十年来只有一位老师：**白洪欢**。

老师富有个性，上课硬核，擅长当黑客、逆向、密码学、拆东西。也是 AAA 战队的指导老师。白老师有自己的课程网站，会有学习汇编语言专用的虚拟机。虽然讲课速度较慢，讲的内容很老，甚至可以说是过时的，但是小白老师也是少有的能将一门课讲清楚、讲透的老师。

## 授课教材

这门课的教材是小白老师自己写的书《80x86 汇编语言程序设计基础》，涵盖了本门课程的大部分知识点，上课没跟上的可以好好看看书。

除此之外，每节课程小白老师都是通过 word 文档来讲授，这些文档都可以在他的主页 [cc.zju.edu.cn/bhh](http://cc.zju.edu.cn/bhh) 上找到。老师当节课的笔记和代码文件通常也会在课后发在钉钉群里，都是相当好的整理/复习材料。

## 分数构成

八次作业（30%）+ 两次小测（30%）+ 期末考试（40%）

25-26 春夏学期，由于白老师希望留更多时间来讲拓展内容，只有一次小测。

作业全部是程序填空题的形式，其实类似于程算的函数题或编程题，要自己写主要逻辑的汇编语言代码（8086 汇编和 80386 指令扩展）。作业难度会逐次提高。后面的作业很多都有 C 语言的对应代码，只需要翻译成汇编，也不会太难。

小测是两道程序填空题，与作业形式相同，但难度远低于作业。

期末考试分为理论考和实验考，类似程算也是两场连续进行。理论考有选择题和判断题，具体数量老师会在期末前说明。

## 推荐书单

- *《汇编语言》* 王爽，清华大学出版社（经典汇编课本，第一推荐）
- *《x86 汇编语言 - 从实模式到保护模式》* 李忠，电子工业出版社（经典汇编课本）
- *《琢石成器》*罗云斌，32 位汇编
- *《软件调试》* 张银奎（各类底层硬件机制和调试方法）
- *《汇编语言程序设计》* 白洪欢，科学出版社（已绝版，就是老师自己印的那本）
- *《IBM-PC 汇编语言程序设计》* 沈美明，清华大学出版社（比较老的中文教材）
- *《Windows 汇编语言程序设计教程》* 谭毓安，电子工业出版社（比较老的中文教材）
- *Professional Assembly Language*, Richard Blum
- *The Art of Assembly Language*, Randall Hyde（不过这个系列使用的主要工具是 HLA，与一般的汇编差别较大）
- *The Art of 64-bit Assembly*, Randall Hyde
- *Assembly Language for x86 processors*, Kip R. Irvine（一本内容丰富的汇编书籍，电子工业出版社的黑皮系列里有。目前最新版是第 8 版）
- *Modern x86 Assembly Language Programming*, Daniel Kusswurm（少数能称得上 Modern 的汇编书）
- *Beginning X64 Assembly Programming*, Jo Van Hoey（不错的入门书，64 位）
- *Assembly Language for Intel-Based Computers*, Kip Irvine（32 位）
- *Practical Malware Analysis*, Michael Sikorski,  Andrew Honig（二进制分析，病毒分析，逆向工程，侧重实战）
- [*Intel 80386 Programmer’s Manual*](https://pdos.csail.mit.edu/6.828/2018/readings/i386/toc.htm)，以及 *[Intel 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)*
- *[Microsoft Macro Assembler reference](https://learn.microsoft.com/en-us/cpp/assembler/masm/microsoft-macro-assembler-reference?view=msvc-170)*

还有一些可以看的网课：

- 华中科技大学：[汇编语言程序设计](https://www.bilibili.com/video/BV1Nt411V7fa)
- 西安交通大学：[微机原理与接口技术](https://www.icourse163.org/course/xjtu-1001647001)（不全讲汇编，侧重硬件）
- 清华大学：[汇编语言程序设计](https://www.xuetangx.com/course/THU08091000320/14767518)（推荐）

一些工具：

- [EMU8086-Microprocessor Emulator](https://emu8086-microprocessor-emulator.softonic.com/)
- [Godbolt Compiler Explorer](https://www.godbolt.org)
- [x86 Processor Information](https://www.sandpile.org)

## 参考笔记

- xg 的汇编笔记：<https://note.tonycrane.cc/cs/pl/asm/>
- <https://www.cc98.org/topic/5239637>

## 学长组课程学习建议

!!! abstract
    21 级学长组编写、22 级学长组和 25 级学长组修改后的学习建议。

老师对学生态度很好，在课前问问题会坐在你旁边手把手教你改代码，课前和课间喜欢放电影，课堂氛围是比较轻松的。

本课程的教材是小白老师自己写的，非常契合课程内容。但由于老师上课速度不快，且讲解基本都比较清晰，教材并不是不可或缺的。另外老师课后通常会把上课自己写的笔记和代码都发到钉钉群里，是用于课后整理和复习相当好的素材。

对于实验环境，小白会给一个 xp 虚拟机，还有一个由他自己修复的，带有 soft-ice 调试器的 bochs 虚拟机。xp 虚拟机整体比较臃肿，bochs 虚拟机操作又比较复杂。老师使用的 Editplus 是不必要的，可以自己选择喜欢的编辑器（比如 vscode）。vscode 上有一个 dosbox 插件，也是可以用的，这样就不用在虚拟机里 debug 了（最后还是要在虚拟机里跑一下的，以免在老师那里出错）。

最后会有一个月左右的时间完成最后一次作业，这段时间老师讲解了中断程序设计、溢出攻击、汇编与 C 语言混合编程、DOS 游戏逆向等内容，但不再布置相关作业。这部分没有在期末的实验考中考察，但在理论考部分有所涉及，也需要认真学习掌握。推荐最后的作业可以慢慢做，不然做完后会有一段时间缺乏编程练习，增大期末复习负担。

建议平时就整理汇编琐碎的知识点，复习可以直接看自己整理的笔记。理论考会有大量送分题，只要作业是自己写代码、自己调试的通常都能拿分，还有一些实际场景的分析，比如给调试器的截图，分析运行到某指令后某个寄存器的值，要注意复习理解那些缺乏作业练习的内容。实验考的难度是很低的，和作业的形式一致，基本上都能很快完成。复习/学习的时候可以参考一下 xg 的这篇笔记 <https://note.tonycrane.cc/cs/pl/asm/>，包含了这门课的大部分知识点。

通过这门课的学习，不仅能够学会 8086 汇编语法，同时也会对操作系统、程序运行原理等有更好的理解。尤其很多内容能够与（培养方案上同期的）计算机系统 I 中计算机组成部分的许多知识相互印证，学习 RISC-V 也能快速上手。另外，这门课的整体压力不高，如果平时认真跟上了进度，完成了作业，期末不必花太多的时间复习，成绩也会相当不错（25-26 春夏这门课的满绩率将近 40 %）。
