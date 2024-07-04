# 优化基本理论与方法

<div class="badges">
<span class="badge cs-badge">CS 专业基础</span>
<span class="badge ai-badge">AI 专业基础</span>
<span class="badge is-badge">IS 专业基础</span>
</div>

## 课程学习内容

课程大部分内容可以概括为凸优化，但并不完全是凸优化，因此称为 “优化基本理论与方法” 也是合理的。课本内容大概可以分为**黑箱优化**和**结构优化**，但是课程所讲的绝大部分内容都属于黑箱优化。简单概括课程大纲如下：

* Introduction
    - 优化问题的范式，基本概念和与机器学习的联系
* 光滑优化基础
    - (一阶、二阶)近似，可微函数类
    - 凸/强凸的定义，凸/强凸函数类，光滑凸/强凸函数类
* 下降方法
    - 梯度下降法
    - 牛顿法，共轭梯度法
* 加速方法
    - 基于光滑凸/强凸函数类的一阶局部黑箱优化的下降速率极限
    - Nesterov 加速梯度下降方法 (最优算法) 及其性能分析
* 一般凸问题
    - 一般凸函数，闭凸性/连续性/可微性
    - 分离定理，次梯度 (Subgradient)
    - 次梯度下降，Frank-Wolfe 算法
* 结构优化
    - 近端梯度下降 (Proximal Gradient Descent)，Douglas-Rachford 分离 
    - 对偶，Lagrange 对偶以及 Fenchel 共轭
    - 光滑化方法，基于 Bregman 散度的镜像下降 (Mirror Descent)
* 随机梯度下降
    - 随机取样，随机梯度下降 (Stochastic Gradient Descent)
    - 改进随机梯度下降，随机镜像下降，SVRG / SARAH

~~尽管看起来内容很多，但是你完全不需要学会，写作业只需要抄书，做 mid-term 和 final report 的时候再精准查查相关资料就行了 () 笔者表示根本没学会~~

### 先修要求

- 数学分析+线性代数

应用了大量分析方法，对分析学基础有一些要求；此外这门课研究的都是向量值函数，因此经常涉及向量和矩阵运算，需要具备基础线性代数知识。

这门课也涉及少量概率统计（主要是最后两节课）和机器学习等内容，不过不了解也没啥问题。

## 课程教材

* Yurii Nesterov. (2014). *Introductory Lectures on Convex Optimization: A Basic Course.* Springer.

作者是凸优化领域的巨擘。前半学期的内容大部分都来自这里。（不要相信书名中的 “basic” :-)

* Yurii Nesterov. (2018). *Lectures on Convex Optimization.* Springer.

第二本书是第一本的修正和扩充，但是许多地方有改动（改正了旧版的一些错误，笔者学习时主要参考的书）。作者的出发视角很高，且极具理论性，这使得本书与其它优化书籍有截然不同的内容，但是其内容也因此有些晦涩抽象，尤其第二本书越到后面越如此。同时，在某种程度上，本书缺少清晰的脉络，定理也缺乏直观解释或者例题说明，笔者认为初学者都不应该使用这本书自学。

## 分数构成

**考查**课，故没有考试。分数构成如下：

* 作业 (50%)

    包括 4 次普通作业和 1 次 mid-term，普通作业一次布置 3-6 道题目，大部分都能够在 PPT 或者书上找到答案。 Mid-term 则要求写代码、测试、写报告， 20 级的题目是用普通梯度下降法、拟牛顿法和共轭梯度法在小数据集上实现岭回归。注意作业和报告都是用 LaTeX 写的，会发 LaTeX 的模板，只要配好环境通过编译一关，修改对应的空处就可以快乐完成作业了。如果仔细研究所给的模板，还能学到很多 LaTeX 技巧。如果环境实在配不起来，可以考虑使用 [overleaf](https://www.overleaf.com/)。

* 报告 (50%)

    同样会给一个 LaTeX 报告模板，按照模板要求写就行了。会给几个研究方向，每个方向给一篇参考论文，选择一个研究方向写一篇报告即可。 20 级所给的三个方向是从 ODE / Geometry / Game Theory 的角度研究 Nesterov 加速梯度下降。或许写成论文翻译，或许写成文献综述，也有真正的大佬疯狂推公式真的在做研究，看你想要做到什么程度。

## 任课教师

20 级的优化基本理论和方法只有钱徽一人开设。

钱徽是无情的 PPT reader，他会迅速地把他要讲的 PPT 讲下去，想要跟上其思路很难。他的声音毫无感情，虽然对该解释的地方也都会解释，甚至会温馨地画图，但总是毫无波澜，让人没有听的欲望。

可能会出现钱徽的研究生来讲课，声音颇有口音，但是比较洪亮，没有钱徽那么催眠。其讲课风格很有学生特色，相比钱徽容易听懂一些，但是口音听着很难受。

钱徽人非常 nice，也非常忙，可能是低调的隐藏强者，是 2022 年下半年疫情拉扯期各大课程老师中**唯一**准确判断本学期后续所有课程一直网课的老师。问他问题他总会抽时间耐心地解答（笔者问过几次问题，有的是 PPT 有错，有的是写得不清楚），但是考虑到他很忙，所以有的时候总是保持未读状态（但是一旦已读他一定会快速回复）。钱徽是 20 级大三秋冬专业课唯一给分之神，让几乎所有人都对成绩很满意，100 人的群收到的谢谢老师高达 70+ ，比很多 200+ 人的习概群的谢谢老师还要多。

## 参考资料

### 书籍

* Boyd, S.P., & Vandenberghe, L. (2005). *Convex Optimization*. Journal of the American Statistical Association, 100, 1097 - 1097. 

    作者是优化领域另一著名大佬 Stephen Boyd，这本书是极其经典的凸优化教材，侧重凸分析的基础，一本相当厚的大部头。花了非常长的篇幅介绍函数的凸性、对偶等，不过有人认为介绍的算法非常有限。作者在自己主页挂了这本书的电子版：[https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)。清华大学出版社翻译了本书，名字就叫《凸优化》。

    这本书也是斯坦福大学 [EE364a](https://web.stanford.edu/class/ee364a/)、 [EE364b](https://web.stanford.edu/class/ee364b/) 课程教材。

* Dimitri P. Bertsekas. (2009). *Convex Optimization Theory*. Athena Scientific.

    中文名《凸优化理论》，清华大学出版社; 并不厚, 个人觉得相之于前面的好读很多。

* Sra, Nowozin, Wright. (2011). *Optimization for Machine Learning*. MIT Press.

* R. T. Rockafellar. (1970). *Convex Analysis*. Princeton.

    Rockafellar 是优化领域绕不开的祖师级人物，不过他的文章有些太难了。本书包含了对凸集、凸函数、凸几何、约束凸优化的详尽理论推导。他的这本《凸分析》还有《变分分析（Variational Analysis）》等书感觉更适合数学专业的看……

* Giuseppe C. Calafiore, \& Laurent El Ghaoui (2014), *Optimization Models*, Cambridge University Press. 据说难度适中, 包含了许多应用举例和分析：[https://people.eecs.berkeley.edu/~elghaoui/optmodbook.html](https://people.eecs.berkeley.edu/~elghaoui/optmodbook.html)
* 这个领域有很多人喜欢直接把自己写的书挂在 arxiv 上，下面几个都是不错的资料：
    + Sébastien Bubeck, *Convex Optimization: Algorithms and Complexity*, [https://arxiv.org/abs/1405.4980](https://arxiv.org/abs/1405.4980)；
    + Léon Bottou et al., *Optimization Methods for Large-Scale Machine Learning*,  [https://arxiv.org/abs/1606.04838](https://arxiv.org/abs/1606.04838)；
    + Francesco Orabona, *A Modern Introduction to Online Learning*, [https://arxiv.org/abs/1912.13213](https://arxiv.org/abs/1912.13213).

就中文书而言，笔者知道的有：

+ 袁亚湘, & 孙文瑜. (1997).最优化理论与方法. 科学出版社. （基本都是算法的纯数学分析和证明）
+ 陈宝林. (2005).最优化理论与算法. 清华大学出版社. （教材）

近年，北京大学文再文老师课题组编写了两本教材：

+ （详细版） 刘浩洋, 户将, 李勇锋，文再文，最优化：建模、算法与理论, 高教出版社；
+ （简化版）刘浩洋, 户将, 李勇锋，文再文，最优化计算方法，高教出版社；
介绍了的最优化的基本概念、典型案例、基本算法和理论，内容紧凑，理论充实（美中不足的缺点可能是印刷质量有点差 :-）网页：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook.html。

### 课程

* CMU 课程 Convex Optimization. 深入浅出的优秀课程：<https://www.stat.cmu.edu/~ryantibs/convexopt/>
* EPFL Course - Optimization for Machine Learning - CS-439，[https://github.com/epfml/OptML_course](https://github.com/epfml/OptML_course)
* 中科大凌青老师的最优化理论课程：<https://www.bilibili.com/video/BV19M411T7S7>
* CSE 535, Theory of Optimization and Continuous Algorithms. <https://yintat.com/teaching/cse535-spring21/>
* ELE522: Large-Scale Optimization for Data Science. 钱老师的授课内容有所参考：<https://yuxinchen2020.github.io/ele522_optimization/>
* IE 598: Big Data Optimization. 钱老师的授课内容有所参考：<https://github.com/niaohe/Big-Data-Optimization-Course>

除此之外，如果仅是为了机器学习和深度学习的工作，其实并不一定要深入了解凸优化，一些基本优化算法在深度学习教材或者课程里都会提及。

### 笔记

* 20 级的金鱼马同学为这门课总结了详细的笔记：[https://www.zhihu.com/column/c_1676006565717573634](https://www.zhihu.com/column/c_1676006565717573634)，如果你发现笔记有错误，请联系他指出问题
    * 在写笔记的过程中，金鱼马同学也发现知乎上也有不少关于优化的文章，例如：
        + <https://www.zhihu.com/column/convex>
        + <https://www.zhihu.com/column/c_119426147>
        + <https://www.zhihu.com/column/c_1263999612412952576>

## 学习建议

可以迷迷糊糊地水过这门课，作业抄抄，代码糊糊，论文水水，也会得到钱徽的宽宥，得到还行的成绩。

这门课的知识和机器学习、数据分析和建模等很多学科领域紧密相关，比如梯度下降、随机方法等都可以用于机器学习模型的训练。许多分析结论也很有意义，比如一阶局部黑箱优化理论最优的下降速率，还有光滑化的处理， “次梯度” 的引入也让人耳目一新。

不过，志不在此的同学建议也可以水一些，毕竟要真的学会这门课要花的精力还是不少的，可能以后也用不到。但是想要踏踏实实做研究，想要明白其所以然的同学还是可以认真学一学。
