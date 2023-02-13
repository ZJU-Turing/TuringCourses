# 认知神经科学导论

<div class="badges">
<span class="badge ai-badge">AI 专业必修</span>
</div>

## 课程学习内容

看起来像是生物课？放心，这只是门水课。大纲大概是这样的：

1. 神经生理学基础，主要是神经元的分子化学机制（讲的很浅，基本上就高中生物课本水平）；
2. 脑科学基础，也很基础，就是大脑的一些分区以及一些功能的介绍，不用背诵，别担心；
3. 计算神经科学基础（对，还是基础），关于神经元模型和神经信息编码，介绍的模型主要就是 LIF 模型，这个期末可能会考，ALIF，GLIF 和上课会提到的 H-H 模型应该都不要求；编码方式期末会考一道题，讲的不多，记一下就行；
4. 可塑性和学习机制，从这里开始基本上就和人工智能基础的内容有些重合了，主要面向的是深度学习，算法讲了 Tempotron, Surrogate Gradient 和 STDP，事实上期末考的是 ANN-SNN 之间的区别，具体算法一点没碰；
5. 记忆机制、脑成像机制等等杂七杂八的玩意，期末只靠概念，脑成像没考过，应该也是不考的。

会有几次作业，基本上都是 PPT 上的内容，2020 级的作业大概是每次四道题，都是论述题，不要求写代码。2019 级有一个 Project，但是因为反馈不好删掉了。

### 先修要求

无。LIF 的推导涉及一点点常微分方程，但是反正可以背诵，而且很简单。

## 任课老师

只有唐华锦老师。上课念中英夹杂的 PPT，而且不一定能念清楚，讲课讲的往往非常模糊，课件也很模糊，听不懂不要怀疑自己，大概是老师的问题。可以选择带上一份作业在教室后排摸鱼，而且没有点过名，大概也可以翘课，不过风险自负。

老师上课的时候有时候会走下来，下课期间也会和后排的同学聊天。感觉唐老师对自己讲的不清楚还是心知肚明的，毕竟他看到大家在后排摸鱼也都不会说什么。

给分情况笔者感觉比较一般，但也有同学得分不错，大概主要是期末考试给分。期末考试允许带两张 cheating sheet，考的主要是概念题，但是没有太多需要硬背诵的内容，把复习 PPT 过一遍去考问题其实就不会太大。最后一节复习课可以听一下，如果讲到了什么题，那大概率会有只换了数据的。

## 课程教材

无教材。

!!! warning "不建议不感兴趣的同学阅读任何一本参考书目"
    这门课虽然老师给出很多参考资料，但绝对不是必须的。下面的讨论仅限于对神经科学和类脑智能感兴趣的同学稍作了解，不感兴趣只是想通过考试拿个不太难看的成绩的话，只要看课件就足够了！

老师有很多推荐书目，不推荐 E. R. Kandel 的，毕竟神经科学原理一套跟砖头一样，咱啃了两年还没啃完。对于计算机系的学生，Abbott 和 Dayan 的 *Theoretical Neuroscience*，相对来讲更有计算机气息。其他书笔者没有看过，额外的推荐放在下面的专栏。

## 分数构成

老师似乎没讲，笔者也没在 PPT 中找到，如果有人知道或者问了欢迎补充。

## 推荐资料

- Coursera 有一份[关于计算神经科学的课程](https://www.coursera.org/learn/computational-neuroscience)，这份课程笔者看过，是比较推荐的；
- Thomas J. Anastasio *Tutorial on Neural Systems Modelling*，经典教材，主要讲的是怎么写代码，或许看着会更加亲切一点；
- Eliasmith, Chris; Anderson, Charles H. *Neural engineering: Representation, computation, and dynamics in neurobiological systems*，比较经典的课本；
- Michael A. Arbib; Shun-ichi Amari; Prudence H. Arbib *The Handbook of Brain Theory and Neural Networks*，手册，也是主要是计算神经科学有关的；
- Gerstner, W.; Kistler, W.; Naud, R.; Paninski, L. *Neuronal Dynamics*，神经动力学，需要一些数学基础；
- [Peter beim Graben, Changsong Zhou, Marco Thiel, Jürgen Kurths, *Lectures in Supercomputational Neuroscience*](https://link.springer.com/book/10.1007/978-3-540-73159-7)，主要是复杂系统（complex network）的视角，这个视角在笔者看来也是饶有兴味的；

因为笔者主要对计算神经科学和神经动力系统感兴趣，对神经生理学了解不多，如果有对相关资料了解比较多的可以继续补充。这方面相关的文献则非常多，篇幅有限故不在此叙述。只推荐一篇好玩的，对类脑智能感兴趣的同学可以一读：[Brooks, R.; Hassabis, D.; Bray, D.; Shashua, A. Turing centenary: Is the brain a good model for machine intelligence?](https://doi.org/10.1038%2F482462a)

关于类脑智能，推荐一篇引言性质的论文：

- [A. Mehonic, A. J. Kenyon, *Brain-inspired computing needs a master plan*](https://www.nature.com/articles/s41586-021-04362-w)

其他可以参考 BICA*AI 的会议记录，现在笔者暂时还没有见过系统性的教科书。

## 后续课程

唐老师的[《脑启发人工智能导论》](../major_elective/brain_inspired_ai)，内容和这门课差不多，合作的祁玉老师讲课水平不错，需要完成几个很简单的作业，作业的代码在 PPT 中几乎都已经给出。这门课是 AI 的选修课，事少给分好，建议选修。
