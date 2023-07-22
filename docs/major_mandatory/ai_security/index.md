# 人工智能安全
<div class="badges">
<span class="badge is-badge">IS 专业必修</span>
</div>

!!! warning "不要与 AI 专业的人工智能伦理与安全混淆"

## 课程学习内容

上课内容包括：

+ 概论，进行总的介绍，以及 AI 安全问题的分类
+ 人工智能基本概念
+ 对抗样本攻击，及其检测与防御
+ 数据投毒攻击及防御
+ 后门攻击及防御
+ 人工智能隐私性，隐私攻击与防御
+ 人工智能公平性
+ 人工智能可解释性

每个专题都会首先讲解主要概念，并对四五个相关论文的工作进行详细介绍，带人深入了解。论文以 2017 年到 2021 年这一时期的为主，因此不少还是很新颖的工作（这一点我很喜欢）。总的来说，可以学到人工智能安全主流方向与研究进展，了解多种安全技术，是一门不错的课程。

> 这门课挺好的，任务不多，有4次自己上网搜集资料，整理回答，不算难，然后实验课就是跑通两次代码写报告，最后复现一次大作业就好了，虽然看着很多，但是他学分也多啊（乐），总之上课体验良好，没有特别卷，老师讲的也很好，一个这方面的小白都了解了这块内容，实验也不难，可以选的。
>
> —— CC98 上一位同学的评价，<https://www.cc98.org/topic/5646762>

这门课的作业包括（看起来很多但事实上并不多）：

+ 大概三四次平时作业，都是几道思考题的形式，根据上课内容以及自己简单查些文献基本都能做出来，内容并不多；
+ 一篇综述的报告。22-23 春夏学期读的综述是关于对抗样本攻击的， Yuan, X., He, P., Zhu, Q., & Li, X. (2017). Adversarial Examples: Attacks and Defenses for Deep Learning. [https://arxiv.org/abs/1712.07107](https://arxiv.org/abs/1712.07107)；
+ 三次实验，22-23 春夏学期中，第一次实验是配环境（送分的），第二次是对抗样本攻击，第三次是联邦学习；实验课要求线下到课，需要写实验报告；
+ 一次大作业。大作业为小组完成，1-2人一组，共同提交一份报告。内容是复现或自己提出一种 AI 安全特定方向的相关技术，并至少在一个目标模型和一个目标数据集上完成相应测试。23 年留的是公平性和成员推断攻防；在这之前留的是对抗样本攻击。

实验课春学期不上，夏学期是每两周一次。不上实验课的那周，会请蚂蚁专家来进行线上讲座，这个个人认为讲得有些过于商业了，不是很能听进去 :-)

没有期末考试。

## 先修要求

最好对基本数学知识、神经网络、一些常见 AI 算法和模型有基本了解（安利 [Stanford University CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/)）。但如果没有基础也是可以的的，因为老师上课都会把需要了解的相关内容的讲一遍，也有一节课专门介绍 AI 基本概念。

当然基本的 Python 和 Pytorch 知识还是要有的，毕竟有实验和大作业。  

## 任课教师

有王志波、杨子祺两位老师。两位老师都可以选，至少他们都是对这一方向很了解的（不过笔者认为杨讲得更清楚一些）。

两位老师都会随机点名。给分都不错，査老师上均绩都 > 4.5。


## 分数构成

课堂出勤（10%）+ 平时作业（30%）+ 实验上机（20%）+ 期末大作业（40%）。

## 推荐书目

AI 安全的书并不多，而且很多技术比较前沿。可以一看的有

+ 腾讯安全朱雀实验室 (2022)，《AI安全：技术与实战》，电子工业出版社
+ Christoph Molnar (2023)，Interpretable Machine Learning: A Guide for Making Black Box Models Explainable, [https://christophm.github.io/interpretable-ml-book/](https://christophm.github.io/interpretable-ml-book/)
+ Yevgeniy Vorobeychik , Murat Kantarcioglu (2020), Adversarial Machine Learning, [https://link.springer.com/book/10.1007/978-3-031-01580-9](https://link.springer.com/book/10.1007/978-3-031-01580-9) （中文名：对抗机器学习：机器学习系统中的攻击和防御，机械工业出版社）
+ 论文
  + Ian J. Goodfellow, Jonathon Shlens, Christian Szegedy. (2014). Explaining and Harnessing Adversarial Examples 
  + Kurakin, A., Goodfellow, I.J., & Bengio, S. (2016). Adversarial examples in the physical world. *ArXiv, abs/1607.02533*.
+ [书单 | 做好AI安全，不可错过的精品好书！ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/634680147)

## 参考笔记

- [金鱼马的人工智能安全笔记](https://www.zhihu.com/column/c_1633936906831552512)
