---
abbrs:
    - 计算机系统 II
    - 计算机系统Ⅱ
grave: https://zju-turing.github.io/TuringCoursesGrave/major_basic/computer_system2/
---

# 计算机系统 Ⅱ

## 课程学习内容

系统贯通系列的第二门课程，主要包括计组（一点体系结构）、操作系统两个部分，也称为硬件和软件两个部分。具体内容是，硬件部分重点为 RISC-V 流水线 CPU，还有一些其他的硬件优化技术介绍等；软件部分从操作系统基础讲起，包括操作系统调用、进程线程、调度、同步等内容。

!!! note "课程大纲"
    来自 24 级卢立申文博老师班

    - Instruction Classification and Design Principle ~ 1 week
    - Concept, Category, Architecture and Design of Pipeline CPU ~ 1.5 weeks
    - Hazard of Pipeline CPU ~ 2 weeks
    - Software/Hardware Interfaces ~ 1 week
    - Introduction of OS ~ 2 weeks
    - Interrupt ~ 2 weeks
    - Process and Thread ~ 2 weeks 
    - Scheduling, Synchronization and Deadlock ~ 2.5 weeks
    - Final Review ~ 1 week

## 任课教师

24 级图灵班该课程预置的是卢立老师和申文博老师，没有必要更换预置。应硬件部分由卢立老师教授，软件部分由申文博老师教授。卢立老师上课稍微有点催眠，但大部分时候还是讲得比较清楚的，课上互动不多，听课比较轻松。申文博老师上课则比较活跃，讲得非常不错，唯一的缺点就是比较注重学生的 participation，24 级常做的操作是从后排开始开火车让同学回答问题，并且不定时的会把课上提的问题让同学们写在纸上记名上交，记为平时点名的分数，采取严格的准出计数，基本上不存在本人未到还能签上到的情况。

这门课的助教也很重要，无论是实验指导还是课后答疑，负责的助教都会有很大的帮助。

## 分数构成

=== "21 级"
    课堂参与（5%）+ 作业（10%）+ 实验（55%）+ 期末考试（30%）

=== "23 级"
    === "卢立、申文博老师班"
        作业（10%）（实则最后没有这部分，应该是换成了签到）+ 实验（60%）+ 期末考试（30%）

=== "24 级"
    作业（10%）+ 实验（60%）+ 期末考试（30%）

## 学习建议

关于作业，留的次数不一定，21 级只有硬件课留了两次作业，24 级卢立申文博老师班也是这种情况，23 级卢立申文博老师班则完全没有作业。同样实验是重头，期末半开卷，难度不高。注意和某些计院专业课一样，这门课也参与了计院的朋辈辅学项目，期末时可以跟着学长的复习课过一遍可能出的大题题型。

24 级的系统二有 7 个平时实验、1 个综合实验和 1 个 Bonus 实验：

- lab0: 系统 I 的单周期 CPU
- lab1: 基础五级流水线 CPU
- lab2: 竞争处理及 AXI4-lite 总线内存模型
- lab3: 卷积加速器
- lab4: RISC-V 64 内核引导
- lab5: RISC-V 64 时钟中断处理
- lab6: RISC-V 64 内核线程调度
- Bonus lab: ARM 架构下 Linux 内核的编译与 QEMU 仿真
- lab7: 综合实验

其中 lab0 到 lab3 以及综合实验属于硬件实验，调试起来比较困难，建议留足时间；lab4 到 lab6 及 Bonus 属于软件实验，会让同学们根据给定的框架一步一步实现操作系统的功能，较为简单，遇到不会的问题可以参考 Linux 的源码或者问大模型解决。具体内容可以参考[实验文档](https://zju-sys.pages.zjusct.io/sys2/sys2-fa25/)，如果文档不存在可以访问[仓库](https://git.zju.edu.cn/zju-sys/sys2/sys2-fa25)查看源码或按照指引本地渲染文档。

系统二是计算机系统三门课中最好拿分的一门，实验不拖 ddl 全部认真完成，期末复习一下，成绩完全不用担心。

## 参考书目

- *《计算机组成与设计：硬件/软件接口》Computer Organization and Design: The Hardware/Software Interface, RISC-V Edition*  
    同系统一，这里也有流水线 CPU 部分的知识，和课上讲的也很类似，可以看看。
- *Operating System Concepts, 10th Edition*  
    软件部分的教材，但是基本也不会用到，21 级说作业从这上面出，但后来软件部分其实并没留作业。
- *Operating Systems: Three Easy Pieces*  
    即 OSTEP，老师和各学长都强烈推荐的一本操作系统书，是完全免费的，网站是 <https://pages.cs.wisc.edu/~remzi/OSTEP/>。
- *《深入理解计算机系统》Computer System: A Programmer’s Perspective*  

## 参考笔记

- xg 的系统 Ⅱ 笔记：<https://note.tonycrane.cc/cs/system/cs2/>  
    这回所有内容基本上都记了，可以参考
- shrike505 的系统 Ⅱ 笔记：<https://nest.shrike505.cc/notes/ComputerScience/ComputerSystem2/>  
    考虑到这可能是大二上较为简单的主课，所以记得很详细

## 历年卷

- [2024-2025 秋冬](https://www.cc98.org/topic/6089253)
