# 计算机系统概论
<div class="badges">
<span class="badge cs-badge">大一短学期</span>
</div>

## 课程学习内容

**计算机系统概论**（*Introducion to Computing Systems*, 以下简称 **ICS** 或者**计概**）从计算机最底层的逻辑门一直到各种数字逻辑结构，再到冯·诺伊曼架构、LC-3 汇编语言，最后到高级语言 C。

课程以 LC-3 这种精简的汇编语言为载体，覆盖了我们后续课程 **数字逻辑设计/计算机逻辑设计基础+计算机组成/计算机组成与设计** 的主体内容。

22 以及 23 年的实验内容包括:

* Lab1：LC-3 机器码实现简单功能
* Lab2：LC-3 汇编
* Lab3：实现双端队列
* Lab4：中断
* Lab5：递归
* Lab6：高级语言实现 LC-3 汇编器/执行器

其中 Lab6 一般是固定的题目（在PTA上布置），在学完了 LC-3 的指令集、数据通路等知识之后就可以开始着手准备了。

值得一提的是，计概本身价值 4 学分，学好计概可以为后续课程打下良好基础。同时还有四课分+国际化学分（需要留意在期限内自己申请）。

### 先修要求

无任何先修要求，~~你甚至不需要掌握 C 语言。~~

按照 Patt 教授的说法，这门课应该是给刚入学的计算机专业学生们上的。

## 任课教师

=== "Yale N. Patt"

    Patt 是美国计算机界泰斗级教授。84 岁高龄的他仍然活跃在教学界和学术界（据说还在带学生）。他用英语授课，但是口音不重，而且语速适中，讲课也非常清晰，会认真详细地回答所有学生的问题。（以上内容仅作参考，笔者没有好好听过课，这实在是种遗憾）

=== "姜晓红（Prof.Jiang）"

    姜老师（也称为姜女士）是 Patt 教授的老搭档了（乐）。她自己本身教授计算机组成、计算机体系结构课程，对这门课的内容也算是比较熟悉。但是她的英语比较令人捉急，上课和 Patt 交流存在一定障碍。同时老师的惯例是要求实验验收一次通过，第二次会扣除 10% 的分数。如果你想了解姜女士更多的故事，欢迎查看查老师热门评论（雾）。

在 2024 年以前的课程安排中，同学们会被分成若干个小教学班，有对应的助教，前两周均是由 Patt 教授上/下午授课，配合下/上午各个助教的 TA Session（复习前一节课的内容 + 实验讲解或验收），而最后几天则是由姜老师进行 C 语言相关内容的讲解（计算机专业的同学应该都已经学过了）以及前两周主题内容的简要复习。所有小班都不得不遵守姜老师的规矩。

而在 2023 短学期中姜老师说明年开始不请 Patt 教授来上课了（据说是因为身体原因），**所以 2024 短学期是否有这门课以及如果有这门课的话该怎么上，还未确定**。

## 课程教材

*Introduction to Computing Systems: From Bits and Gates to C and Beyond 3rd, Yale N. Patt*

Patt 教授及其学生执笔的教材。上课基本按照教材内容，作业也是来自教材的课后习题。个人认为教材写的挺好，认真读课本可以代替听课。注意使用第三版教材。 

## 分数构成

Homework(20%) + Lab(40%) + Final(40%)

* Homework 均为教材习题，网上有答案，由助教批改。去年为了控制平时分，作业批改较严。
* Lab: lab1(5%) + lab2(5%) + lab3(7%) + lab4(7%) + lab5(8%) + lab6(8%), 实验内容见课程学习内容部分。
    * 其中前五个实验需要验收，第六个实验可以在整个暑假时间内完成，开学前截止且不用验收。实验均需要实验报告。
    * 每个实验都有查重，查到了会扣掉该次实验所有分数并扣除 10% 的总评。
    * 第一次没验收成功则验收最高得分 90, 超过验收期限也会有 penalty. 
    * 2022 年实验的要求可见[仓库](https://github.com/HobbitQia/ZJU-Courses-Resources/tree/master/ICS)，2023 年实验要求可见[仓库](https://github.com/Frankoxer/ZJU-ICS-2023-Labs)
* Final 是纸质统一考试，没有 cheating sheet, 一般是开学第一周周五（是的，隔了一个暑假）有斩杀线（据说是 50）

## 学习建议

你可能会看到很多人吐槽这门课难，那是因为这门课是面向全校同学开课的，课程班级中也有一部分非计算机相关专业的学生。身为图灵班的学生，你基本不需要太过担心。如果你已经学完了汇编语言课程或者电工学相关课程或者预习了计逻知识或者有过 ICS 相关课程/书籍的学习，完全不用担心，你甚至可以不听课（只需要听助教讲课就行）。下载 LC-3 模拟器之后多去玩玩，它的内容也并不复杂。就算不会的话也可以去问助教。

由于秋学期开学需要进行期末考试，建议暑假末期对计概的基础知识过一遍，并重点关注有关数据通路、中断以及递归等方面的细节知识。好好做 Lab6 中的 LC-3 执行器也会对理解相关知识有帮助。

这里给出一些学长的笔记：

* [QJJ 的计概笔记](https://note.hobbitqia.cc/ICS/)
* [修佬的计概笔记](https://www.yuque.com/isshikixiu/codes/ics)

## 相关课程

这里贴出其他学校比较有名的 ICS 课程及其资源：

* [CMU 15-213](http://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)  
教材是计算机界的“圣经” [CSAPP](http://csapp.cs.cmu.edu/3e/home.html), 即 *Computer Systems: A Programmer's Perspective*
* [南京大学 ICS 课程实验 - PA](https://nju-projectn.github.io/ics-pa-gitbook/ics2022/)

上述资源的难度、深度、广度均远大于计概，仅供各位参考。