---
grave: https://zju-turing.github.io/TuringCoursesGrave/major_basic/computer_system2/
---

# 计算机系统 Ⅱ

## 课程学习内容
系统贯通系列的第二门课程，主要包括计组（一点体系结构）、操作系统两个部分，也称为硬件和软件两个部分。具体内容是，硬件部分重点为 RISC-V 流水线 CPU，还有一些其他的硬件优化技术介绍等；软件部分从操作系统基础讲起，包括操作系统调用、进程线程、调度、同步等内容。

!!! note "课程大纲"
    来自 23 级卢立申文博老师班

    - Instruction Classification and Design Principle ~ 1.5 week
    - Concept, Category, Architecture and Design of Pipeline CPU ~ 1.5 weeks
    - Hazard of Pipeline CPU ~ 2 weeks
    - Software/Hardware Interfaces ~ 1 week
    - Introduction of OS ~ 2 weeks
    - Interrupt ~ 2 week
    - Process and Thread ~ 2 weeks 
    - Scheduling, Synchronization and Deadlock ~ 3 weeks
    - Final Review ~ 1 week

## 任课教师
硬件部分还是由系统一的卢立老师继续教授。软件部分 20 级为申文博老师，21 级为周亚金老师，都很 nice 的。随着系统逐渐成为计院软硬件课程的主流，必修这门课的同学也越来越多，之后会有更多老师开班。

这门课的助教也很重要，无论是实验指导还是课后答疑，负责的助教都会有很大的帮助。

## 分数构成
=== "21 级"
    课堂参与（5%）+ 作业（10%）+ 实验（55%）+ 期末考试（30%）

=== "23 级"
    === "卢立、申文博老师班"
        作业（10%）（实则最后没有这部分，应该是换成了签到）+ 实验（60%）+ 期末考试（30%）

## 学习建议
硬件课有可能老师会在课上让做一下小题最后上交答题纸来记录课堂参与度。作业次数不一定，21 级只有硬件课留了两次作业，23 级卢立申文博老师班则完全没有作业。同样实验是重头，期末半开卷，难度不高。注意和某些计院专业课一样，这门课也参与了计院的朋辈辅学项目，期末时可以跟着学长的复习课过一遍可能出的大题题型。

关于实验，硬件部分应该有三个，第一个是上学期的单周期 CPU，照顾一下当时没完成的同学，第二个就是流水线 CPU，第三个是冒险的处理（Forwarding 模块 & Axi 总线模型）。硬件实验还是有些麻烦的，调试不太容易，出问题勤问助教就好。软件部分实验和其他专业的 os 实验差不多，第一个实验是编译、调试 Linux 内核，第二个实验开始根据框架一步一步实现操作系统的功能。面对给的框架可能不知道从何入手，这时候可以参考 Linux 的源码。最后一个实验是综合性实验，但实际来说就是硬件实验，需要在之前的流水线 CPU 上添加 RISC-V 特权模式的一小部分功能，来跑起来一个简化的小 kernel。

和系统一一样，这门课也是相当好拿分的，甚至 20 级的均绩都达到了 4.8 分。实验不拖 ddl 全部认真完成，期末简单复习一下，成绩完全不用担心。

## 参考书目
- *《计算机组成与设计：硬件/软件接口》Computer Organization and Design: The Hardware/Software Interface, RISC-V Edition*  
    同系统一，这里也有流水线 CPU 部分的知识，和课上讲的也很类似，可以看看。
- *Operating System Concepts, 10th Edition*  
    软件部分的教材，但是基本也不会用到，21 级说作业从这上面出，但后来软件部分其实并没留作业。
- *Operating Systems: Three Easy Pieces*  
    即 OSTEP，老师和各学长都强烈推荐的一本操作系统书，是完全免费的，网站是 https://pages.cs.wisc.edu/~remzi/OSTEP/。
- *《深入理解计算机系统》Computer System: A Programmer’s Perspective*  

## 参考笔记
- xg 的系统 Ⅱ 笔记：https://note.tonycrane.cc/cs/system/cs2/  
    这回所有内容基本上都记了，可以参考
- shrike505 的系统 Ⅱ 笔记：https://nest.shrike505.cc/notes/ComputerScience/ComputerSystem2/  
    考虑到这可能是大二上较为简单的主课（普通物理学.jpg），所以记得很详细:)

## 历年卷

- [2024-2025 秋冬](https://www.cc98.org/topic/6089253)