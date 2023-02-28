# 编译原理

<div class="badges">
<span class="badge cs-badge">CS 专业必修</span>
<span class="badge ai-badge">AI 专业三选一必修</span>
<span class="badge is-badge">IS 专业必修</span>
</div>

## 课程学习内容
首先简要介绍一下 “编译” 或者 “编译器” 这个更加广泛的方向，一般高级语言、面向通用 CPU 平台的编译器涉及的内容大致可以分为以下几个部分:

- 前端：指编译器读取我们文本文件的源代码，理解代码的结构和语义，生成 语法树（AST）
- 中端：根据语法树生成中间表示（IR），做一些 target independent optimization
- 后端：根据 IR 生成汇编，并做 target dependent optimization
- 其他：相关的运行时（Runtime）和语言设计等

由于一些“众所周知”的原因，编译原理课程基本只涉及前端，大部分时间会花在讲 tokenizer 和 parsing，这部分的一部分理论基础会在“计算理论”这门课学到。其他主要会很散的讲一点 Runtime 和 Memory 的问题。

书面作业一般是理论题目，通常是和上面这些算法相关的，一般不难。

Project 分两个小 lab 和一个大作业，小 lab 是用 flex 写 tokenzier 和用 bison 写 parser，非常简单。大作业（3人一组）是写一个完整的编译器，实现语言和被编译的语言不限，可以自己设计，验收是需要你用被编译的语言写解决 3 个 task 的代码（类似于程算的题目），用你写的编译器编译后根据输出检查正确性，对生成的代码质量没有要求。

期末考试可以带 cheating sheet，题目比较传统，选择和简答题。选择部分刁钻题还是有一些的，建议对一些概念和算法流程要比较清楚。

## 分数构成
书面作业（10%）+ 课堂 Quiz（10%）+ 期中考试（15%）+ Project（25%）+ 期末考试（40%），期末考斩杀线为 40 分。

## 相关书单
- *Compiler Contruction and Practice*, Kenneth C. Loudon（2022 春夏学期教材）
- *Compiler -- Principles, Techniques and Tools (2nd ed.)*, Aho, Sethi and Ullman（俗称“龙书”）
- *Modern Compiler Implementation in C (Java, ML)*, Andrew Appel（俗称“虎书”）
- *Engineering a Compiler (2nd/3rd ed.)*, Cooper, Keith D., Torczon, Linda（俗称“橡书”）
- *Advanced Compiler Design and Implementation*, Steven S.Muchnick（俗称“鲸书”）
- *Optimizing Compilers for Modern Architectures*, Allen
- *Parsing Techniques: A Practical Guide*， Grune, Jacobs

## 参考笔记
友情感谢  xyx 学长

- xyx 的语雀: https://www.yuque.com/xianyuxuan/coding/compiler

## 学习建议

编译原理的教材不固定，可能每几年轮换一次。

推荐初学者使用“橡书”，虽然讲的稍微泛一点，但是内容比较广和丰富；不太建议使用“龙书”，虽然享有盛名，但是讲的太繁琐了；不太建议看“虎书”，虽然有代码，但是内容涉及略少，而且虎书的代码对这门课用处不大；完全不建议看 Compiler Contruction and Practice，内容很老而且讲的不清楚。

由于这门课重点在 parser 有兴趣可以看 Parsing Techniques 这本书，这本书对 parsing 算法讲解比老师清晰很多。

如果对编译优化感兴趣，可以看“鲸书”，或者其他涉及程序分析、静态分析的书籍和论文。

这门课的 Project 设计非常不合理，小 lab 用的是很老的 flex 和 bison，虽然很简单，但是很多人写了之后形成了惯性，也用在大作业里面（然后就会发现面对复杂一点的语法就非常不好用，不灵活，很难调试）。大作业没有任何指导文档，但是要求能“跑起来”，大家要么使用类似 LLVM 的框架帮你生成汇编，要么直接使用 interpreter 解释执行 AST。前者对于不熟悉 LLVM、Linker、Loader 的人来说会相对困难，后者相对比较简单一点，建议大家提早开工，不要拖太久。

## 相关课程与书籍推荐

该部分仅面向认为课程内容过少，对编译领域感兴趣，想要深入学习相关技术的同学，只建议有余力的情况下学习:

- [THU Rust](https://lab.cs.tsinghua.edu.cn/rust/)，清华大学 Rust 程序设计课程。
- [CMU 15-745](https://www.cs.cmu.edu/afs/cs/academic/class/15745-s19/www/)，研究生课程，主要内容是使用 LLVM 编写优化 Pass，能够熟悉 LLVM 的架构，主要问题是近几年的 slides 和 materials 需要 CMU 教职工身份认证，没有资源的话可以看 19 年的。如果你有兴趣，可以提前在假期的时候先写一写，这样对付我们学校的大作业相对能比较从容。
- [LLVM 笔记](https://www.cnblogs.com/Five100Miles/)，LLVM 一些核心概念和重要源码的解读，熟悉 C++ 的同学初学 LLVM 可以先看这个。
- [Static Program Analysis - DC888](https://homepages.dcc.ufmg.br/~fernando/classes/dcc888/)，经典的面向编译器分析和编译优化的课程
- 中科大的编译原理课程，大作业是从中端和后端的几个 topic 中选一查阅资料加代码实现，似乎有给框架，涉及 SSA, Phi, RA, Optimize, Lowering 等话题，内容丰富，可参考他们的 [大作业展示](https://space.bilibili.com/273391839)。
- 北京大学熊老师的 [程序分析课程](https://xiongyingfei.github.io/SA/2022/main.htm)
- 相关延伸的和 AI 相关的如 [tvm](https://tvm.apache.org/)，需要有一定 HPC 经验。