# 面向对象程序设计

<div class="badges">
<span class="badge cs-badge">CS 专业基础</span>
<span class="badge ai-badge">AI 专业基础</span>
<span class="badge is-badge">IS 专业基础</span>
</div>

## 课程学习内容

以 C++ 语言为例学习面向对象语言的特点。课程一部分学习 C++ 的语法，一部分学习 C++ 实现封装、继承和多态的方式。

### 先修要求

- 数据结构基础
- 掌握 C 语言

（个人认为 C++ 0 基础来上课是没问题的，想准备可以提前了解下相关语法和特性。）

## 任课教师

=== "翁恺"

   翁恺老师授课毫无疑问还是最有水平的，除了上课的时候闲扯时间可能比较长。老师的实验题必须在实验当天完成，或者你有情况需要点进题目集（PTA 的奇怪设定）后与翁恺老师说明情况然后第二天会补开。这门课难度不是特别大，但期末考试考纲不定，每个老师教的东西也不定，翁恺老师讲的很多比较难的都不在考察范围（上课基本只会讲到 C++98 标准，仅涉及少量 C++11 标准）。翁恺老师给分还是值得信赖的，有补分集可以补满平时分。老师会有少数查重，20 级有一次。点名在 20 级有一次突击小测（时间和题目都与 19 级一致，因此可以参考往年录播），小测后一次发卷子也是通过一个一个念名字的方式进行。当然有一个小的雷点就是 oop 部分他的编程题描述不清或者有一些奇怪的测试点，经常会搞人心态。

## 课程教材

* *《C++ 程序设计》Intruduction to Programming with C++ (Third Edition)* [美] Y. Daniel Liang（梁勇）

    课程组指定教材，~~但没有什么用处~~ 比较基础、简单易懂

* *《C++ 编程思想》Thinking in C++* [美] Bruce Eckel

    一本比较经典的 C++ 教材，作者 Bruce Eckel 是著名的编程教育家。翁恺老师的大部分课件都是按照这本书内容编排。当然这本书有很多考试不考察的内容，如果时间不够可以只看老师 PPT 涉及内容对应的部分。

## 参考阅读

读万卷书，行万里路。

* *C++ Primer* (5th edition), [美] Stanley B. Lippman / [美] Josée Lajoie / [美] Barbara E. Moo

    经典 C++ 教材，有十分详尽的语法讲解。不过整本书看起来像是语法字典，可能并不容易读，建议用到某一特性再去找。第五版教材包括了 C++11 标准。

* *C++ Primer Plus* (6th edition)，[美] Stephen Prata

    傻瓜式的、从 0 开始的 C++ 教材，有人觉得很面面俱到，个人觉得啰里啰嗦。

* *Essential C++*, [美] Stanley B·Lippman
    
    比较基础，分四个部分讲解 C++ 的本质，也可以用作入门读物。比较老了，只到 C++98 标准。

* C++ 之父 Bjanre Stroustrup 的几本书：
    * [*Programming: Principles and Practice using C++*](https://link.zhihu.com/?target=https%3A//www.stroustrup.com/programming.html)（《C++ 程序设计原理与实践》）
        
        “适合以前没有编程经验或者已经学完另一种语言，并且希望对现代 C++ 有一个相对温和的介绍的人”，BS 给大一学生写的教材。覆盖 C++11 和 C++14 标准。

    * [*The C++ Programming Language* (4th edition)](https://link.zhihu.com/?target=https%3A//www.stroustrup.com/4th.html)（《C++程序设计语言》）
    
        “面向已经了解 C++ 或至少是经验丰富的程序员的人”。覆盖 C++11 标准。

    * 如果你想知道为什么 C++ 的历史，请看 [*The Design and Evolution of C++*](https://link.zhihu.com/?target=https%3A//www.stroustrup.com/dne.html)（《C++语言的设计与演化》）。[*Thriving in a Crowded and Changing World: C++ 2006-2020*](https://link.zhihu.com/?target=https%3A//dl.acm.org/doi/pdf/10.1145/3386320) 可以被视为 D&E 的最新后续。
    * [*A Tour of C++* (second edition)](https://link.zhihu.com/?target=https%3A//www.stroustrup.com/tour2.html)（《C++语言导学》）
    
        适合去快速了解 C++ 所提供的功能。这本书以 200 页的篇幅介绍了 C++ 及其标准库的主要特性，且覆盖 C++17 标准（及少量 C++20 标准），对于了解新标准特性也不错。

* 关于 C++ 的 STL（标准模板库），想要了解其内部实现细节，可参考侯捷老师《STL源码剖析》，但侯捷老师这本书不适合初学者，而且标准比较老，后面几章有些已经用不上了。另外也可以看 Scott Meyers, *Effective STL*。
* *Effective C++*, [美] Scott Meyers
    
    讲解一些实际套路和原理，结合具体情况教你如何写程序，写了很多 C++ 各种容易踩坑的点。有些很有帮助，后面有些可能有点难。这本书还有后作 *More Effective C++*，更高深了（×。两本书都只涉及 C++98/03 标准，少量内容有些过时。

* *C++ Without Fear*, Brian Overland

    比较老（指 C++98 标准）的入门书籍。

* *Functional Programming in C++*, Ivan Cukic
    
    （给老司机们）了解 C++ 函数式编程

* （给老司机们）进一步探索现代 C++：
    * *Modern Effective C++*, [美] Scott Meyers
        
        教你怎么用 C++11 和 C++14，既有语法也有实例讲解，带你走向现代 C++。后面有点难。

    * [《现代 C++ 快速上手 (Modern C++ Tutoral)》](https://github.com/changkun/modern-cpp-tutorial)》，Ou Changkun，字面意思，快速上手。
    * *C++ Templates* (2nd edition)，[美] David Vandevoorde / [德] Nicolai M.Josuttis / [美] Douglas Gregor 
    
        深入了解模板<del>的奇技淫巧</del>。

    * 其他，如：《深入探索 C++14（Discovering Modern C++)》《现代 C++ 语言核心特性解析》《C++20 高级编程》等

* 可参考 [The Definitive C++ Book Guide and List](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)，Stack Overflow 上整理的书单。也可以逛逛 [Quora](https://www.quora.com/What-is-the-best-C-book-for-a-beginner)。
* C++ 之父 Bjanre Stroustrup 的 [FAQ](https://www.stroustrup.com/bs_faq.html) 很有意思，值得一看！此外他还有 [C++ Style and Technique FAQ](https://www.stroustrup.com/bs_faq2.html) 。
* 一些 C++ 书籍的**电子版资源**：https://www.aliyundrive.com/s/z5hLRAELpPP

## 参考资料
- RyanFcr 整理的笔记和历年卷：[:material-github: RyanFcr/ZJU_Course:大二春夏/面向对象程序设计OOP](https://github.com/RyanFcr/ZJU_Course/tree/main/%E5%A4%A7%E4%BA%8C%E6%98%A5%E5%A4%8F/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1OOP)
- Stanford CS106L 课程：https://www.cc98.org/topic/5401931
- 贺老师的专栏：https://www.zhihu.com/column/c_1561843704159232000
- Isshiki 的课堂笔记：[📔 \[大一寒假\] ZJU Object-Oriented Programing Using C++ (yuque.com)](https://www.yuque.com/isshikixiu/codes/wk_oop)
- 咸鱼暄学长的 [C++ Weekly Tips](https://www.yuque.com/xianyuxuan/saltfish_shop/weekly017) 和[快速入门 C++ 写题](https://xuan-insr.github.io/cpp/cpp_for_contests/)
- zjj 提供的作业题整理：[oop-mid-review](https://zhoutimemachine.github.io/2022/07/07/2022/oop-mid-review/)、[oop-final-review](https://zhoutimemachine.github.io/2022/07/07/2022/oop-final-review/)（如果链接失效可以在 [blog主页](https://zhoutimemachine.github.io/) 看看）

## 分数构成

=== "翁恺"
    - quiz 5%
    - Homework 10%
    - 七个 Labs（一次上机期中考试） 15%
    - 一个大 Project 15% team work（2 人一组）
        - MUD 游戏
        - 日记本
        - 也可以是自己的题目
        - 每个月都要上交进度报告，进度报告一般给 100，结题报告按实际情况给分，四次报告取平均
    - 期中 5%
    - 期末 50%

    除此之外还会有补分集（3分），很多同学的平时分都是满分。

期末复习可以参考这个[课程资料仓库](https://github.com/RyanFcr/ZJU_Course/tree/main/%E5%A4%A7%E4%BA%8C%E6%98%A5%E5%A4%8F/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1OOP)。这门课期末考试不是很友好，除了之前说的大纲不确定外，部分老师命题水平实在有限，也有部分老师出题审核不严格出现漏洞。另外，C++ 语言本身就很复杂，而且考试可能会考到一些很细的语言特性，可能需要平时多注意。

并且自从 2019 级春夏出现大量编译错误后人工批阅的情况后，接下来的学期都采取主观题形式写代码，然后由老师人工批阅。个人认为平常写代码是认真写的，然后特别注意部分地方的语法（例如 virtual 等）分数都不会差。当然不得不承认的一点是，数据库系统大作业 minisql 是一个复习 oop 的很好的练习。
