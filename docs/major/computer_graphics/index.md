---
grave: https://zju-turing.github.io/TuringCoursesGrave/major_elective/computer_graphics/
---

# 计算机图形学

## 课程学习内容

主要讲述计算机图形学解决的基本问题，基础原则和方法，基础编程技能，但是不包含具体的编程指导和图像信息处理工具的使用，主要讲述了

- Rasterization
- Transform, view and Hidden Surface Removal
- Color, Surface, Materials and Textures
- Rendering
- Research(in Graphics and Vision)

还会介绍 OpenGL 和可编程管线，但是提到的 OpenGL 的实现是比较老的版本，如果这里作业使用老版本那么在后面的任务中可能会遇到一些问题。

总体而言讲的是比较 base 的图形学内容，而且吴鸿智老师的讲课偏向于 High-level 而不是细节，听课体验还是不错的。

## 任课教师

[吴鸿智](http://hongzhiwu.com/)，吴老师讲课比较好，会经常发问，对一些原理的东西也会比较深入地讲解

## 课程教材

- Computer Graphics with OpenGL, Fourth Edition, D. Hearn, M. P. Baker（电子工业出版社）
- Fundamentals of Computer Graphics, Peter Shirley, Steve Marschner, AK Peters
- 计算机图形学——原理、方法及应用，潘云鹤，董金祥，陈德人，2003
- OpenGL Programming Guide, Fourth Edition, Addison-Wesley, 2003,（OpenGL 编程指南，人民邮电出版社）
- OpenGL Distilled, Paul Martz, Addison-Wesley, Addison-WesleyProfessional; 1ST edition（OpenGL2.0 精髓，人民邮电出版社）
- [The NeHetutorials](http://nehe.gamedev.net)

## 分数构成

- Assignment(30%)

    课程一共有 9 次小的作业，分别是 opengl 绘制椭圆/绘制旗帜/书面作业 1（简单变换）/solar system/书面作业2（简单原理解释）/大作业组队 + proposal/dream car/给太阳系添加光源/给太阳系添加纹理

    小作业的设计基本上都是为了最后的课程项目准备的，里面用到的基本方法也都要求在最后的课程项目中体现，这么来看设计还是相对合理的。你需要的是从头开始学习 OpenGL 并理解他的逻辑，课程没有包含这一部分的指导，你需要通过网上的资料自己进行学习。这一部分主要是学习框架需要花费比较多的时间精力。这一部分的给分只要完成了基本要求都是满分，但是需要注意 deadline，有每天减一半的 late penalty。

- Course Project(40%)

    简单三维建模及真实感绘制（基础 90 分 + 高级 15 分）（以 2-3 人为一组实现，教师以给平均分的形式打分）。基本上是实现一个游戏，workload 并不小，在大三上众多专业课中也算是名列前茅。一方面要熟悉 OpenGL 的框架，另一方面也需要良好的 C++ 编程能力。

    单从最后的给分来说方差并不大，基础的部分中有很多要求是客观的，前面作业中用到的（75 分），完成了基础部分并且能让老师觉得你的游戏比较 awesome 就能拿到 88-89 分左右的分数，如果你对细节的设计更好，比如你设计了一个飞行导弹轨迹很好看或者爆炸效果很好，那你也许就能达到 92-93 的分数。当然高级要求中还有移动端和增强现实的加分，但是实现难度很大，很少有人去做。

    总而言之，这一部分的分数基本是是与你的投入成正比的，也是需要在最后一次课上进行展示的，你需要把你实现所有的酷炫的都展示给老师看。

- In-class Performance(30)

    课程会进行几次**不提前通知**的 Quiz，这是可能造成失分最多的地方。Quiz 可能与课程内容没有直接关系，允许携带一张 A4 作为 "Cheating" sheet。这一部分主要由于突击性而且题目也比较灵活，是可能造成失分的“重灾区”。当然吴鸿智老师在 24-25 秋冬降低了这一部分的比例 (23%)，更多的加到了作业里。

    另一部分是课堂的互动，这一部分并没有太多的分数，回答或者提问都是可以算入的，一般 2-3 次即可，每次 1 分

    24-25 秋冬的 Quiz 题是如何计算两条直线相交，Bezier 曲线的表示，Bezier 曲线的性质证明，brdf 光照模型反射相关。难度不算太大，但是 Quiz 时间比较有限一般 20 分钟就要完成。

## 学习建议

如果想要入门图形学的研究，或许 Games101 是更好的选择，这一门课更多是了解基本原理。对想要轻松并且获得高分数的同学，不建议选修这门课。这门课的 Workload 是比较大的，中间遇到问题很多也很折磨人，但是最后完成自己的 project 也是很有成就感的。理论的部分是需要好好理解的，Quiz 的扣分还是比较大的，需要重视。对实践的部分建议是从第一次开始就跟着 [LearnOpenGL](https://learnopengl.com/) 的教程配置环境，这样能很大程度的避免后期发现功能不支持带来的问题。而且这个教程相对而言也是比较详细的实践教程。
