# 优化基本理论与方法

<div class="badges">
<span class="badge cs-badge">CS 专业基础</span>
<span class="badge ai-badge">AI 专业基础</span>
<span class="badge is-badge">IS 专业基础</span>
</div>

## 课程学习内容

课程大部分内容可以概括为凸优化，但并不完全是凸优化，因此称为 “优化基本理论与方法” 也算是合理的。课本内容大概可以分为**黑箱优化**和**结构优化**，但是课程所讲的绝大部分内容都属于黑箱优化。简单概括课程大纲如下：

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

尽管看起来内容很多，但是你完全不需要学会，写作业只需要抄书，做 mid-term 和 final report 的时候再精准查查相关资料就行了 () 笔者表示根本没学会

### 先修要求

- 数学分析

应用了大量数学分析方法，对数学分析基础有较高的要求。

## 课程教材

* *Introductory Lectures on Convex Optimization A Basic Course*

作者 Yurii Nesterov，是凸优化领域的大佬。 PPT 大部分都抄自这里。

* *Lectures on Convex Optimization*

中文版书名《凸优化教程》，作者依然是 Yurii Nesterov，内容和上一本差不多，但是许多地方有改动。（记得似乎改正了旧版的一些错误，笔者学习时主要参考的书）

* *Convex Optimization*

作者 Boyd ，诸多大佬认为比 Yurii Nesterov 写得好的教材。由于不是教材，笔者没有看过，但是既然诸多大佬推荐，笔者也就在此放上。

## 分数构成

**考查**课，故没有考试。分数构成如下：

* 作业 (50%)

    包括 4 次普通作业和 1 次 mid-term，普通作业一次布置 3-6 道题目，大部分都能够在 PPT 或者书上找到答案。 Mid-term 则要求写代码、测试、写报告， 20 级的题目是用普通梯度下降法、拟牛顿法和共轭梯度法在小数据集上实现岭回归。注意作业和报告都是用 LaTeX 写的，会发 LaTeX 的模板，只要配好环境通过编译一关，修改对应的空处就可以快乐完成作业了。如果仔细研究所给的模板，还能学到很多 LaTeX 技巧。如果环境实在配不起来，可以考虑使用 [overleaf](https://www.overleaf.com/)。

* 报告 (50%)

    同样会给一个 LaTeX 报告模板，按照模板要求写就行了。会给几个研究方向，每个方向给一篇参考论文，选择一个研究方向写一篇报告即可。 20 级所给的三个方向是从 ODE / Geometry / Game Theory 的角度研究加速梯度下降。或许写成论文翻译，或许写成文献综述，也有真正的大佬疯狂推公式真的在做研究，看你想要做到什么程度。

## 任课教师

20 级的优化基本理论和方法只有钱徽一人开设。

钱徽是无情的 PPT reader，他会迅速地把他要讲的 PPT 讲下去，想要跟上其思路很难。他的声音毫无感情，虽然对该解释的地方也都会解释，甚至会温馨地画图，但总是毫无波澜，让人没有听的欲望。

可能会出现钱徽的研究生来讲课，声音颇有口音，但是比较洪亮，没有钱徽那么催眠。其讲课风格很有学生特色，相比钱徽容易听懂一些，但是口音听着很难受。

钱徽人非常 nice，也非常忙，可能是低调的隐藏强者，是 2022 年下半年疫情拉扯期各大课程老师中**唯一**准确判断本学期后续所有课程一直网课的老师。问他问题他总会抽时间耐心地解答（笔者问过几次问题，有的是 PPT 有错，有的是写得不清楚），但是考虑到他很忙，所以有的时候总是保持未读状态（但是一旦已读他一定会快速回复）。钱徽是 20 级大三秋冬专业课唯一给分之神，让几乎所有人都对成绩很满意，100 人的群收到的谢谢老师高达 70+ ，比很多 200+ 人的习概群的谢谢老师还要多。

## 参考资料

暂无

## 学习建议

可以迷迷糊糊地水过这门课，作业抄抄，代码糊糊，论文水水，也会得到钱徽的宽宥，得到还行的成绩。然而尽管神经网络是非凸的，这门课讲的很多方法也能应用于非凸问题（优化 “基本” 理论），比如梯度下降、Nesterov 加速梯度下降、镜像下降等。这门课给出的许多分析结论也很有意义，比如一阶局部黑箱优化理论最优的下降速率，还有光滑化的处理， “次梯度” 的引入也让人耳目一新。不过，志不在此的同学建议也就可以随便水水，毕竟要真的学会这门课要花的精力还是不少的，可能以后也用不到。但是想要踏踏实实做研究，想要明白其所以然的同学还是可以认真学一学（比如像大佬们一样放弃钱徽找别的资料大不自多也是一种思路）。
