# 计算机视觉

<div class="badges">
<span class="badge cs-badge">CS 专业选修</span>
</div>

<!-- include custom css -->
<link rel="stylesheet" type="text/css" href="custom.css">

## 课程学习内容

本课程主要涉及图像处理等基本思想和方法，包括：

- 视觉方面的基础理论
- 对图像和视频进行处理
    - low-level 层面：处理形状、颜色等
    - high-level 层面：识别具体的物体是（语义理解）
- 对三维世界进行解构（更多是几何方面的内容）

### 先修要求

无先修要求，只要会基本的 C 和 Python 语法即可。老师的课堂/实验会从基本的 OpenCV 使用与图像处理开始，比较容易上手，包括之后的 CNN 处的实验也是很经典的。不过本课程和 [图像信息处理](../digital_image_processing) 有相通之处，在修习完图像信息处理之后（特别是后半段内容）再修习本课程会有一定的帮助。

## 任课教师

=== "潘纲"

    全中文授课，课件以往年的形成的<font class="heimu" title="你知道的太多了">杂交</font>课件为主，但是也会夹杂着一些随时事 <font class="heimu" title="你知道的太多了">OpenAI</font> 更新的课件（Transformer）。因为潘老师原本就是 CV 方向的，所以对于课程的讲解也是很有深度的。不过从 21 年开始，潘老师的实验开始改革，相比宋老师班会难很多，同时也会邀请实验做的比较好的同学对自己的实验进行讲解，有一定的 Bonus（但没公布比例），原则上一人一次。2023 年冬没有点名的情况。

=== "宋明黎" 

    来自潘老师班的说法：据说宋老师上课和图像信息处理很相近。  
    TODO：待完善

## 课程教材

整体课程以课程讲义为主，没有指定教材，相关的原理可以查询维基或者 OpenCV 等库的说明。不过潘老师课件中有给出一些关于 OpenCV 的书籍，如：

- *Learning OpenCV：Computer Vision with the OpenCVLibrary*, Gary Bradski, Adrian Kaebler
- 《OpenCV教程—基础篇》，刘瑞祯、于仕琪

不过并不是特别需要，使用的相关文档可以直接参考 OpenCV 的 [Documents](https://docs.opencv.org/4.x/d1/dfb/intro.html)。

## 分数构成

=== "潘纲"

    - 平时编程作业（50%）
        - Canny Edge Detection
        - Image Stitching
        - Eigenface
        - Learning CNN
            - LeNet-5, U-Net
        - Learning CNN++
            - 公开数据集 [Pokemon Image Dataset](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types/data) 上的精灵宝可梦类型预测任务
        - 其他说明
            - 若迟交，最高得分上限 80%
            - 在班级整体完成度不好的情况下，会对作业进行延期，甚至可以变成考试周大作业
            - 若完成度好，通过进行展示可以得到一定 Bonus，比例未知，从个人得分上感觉没有溢出到期末
    - 期末考试（50%）
        - 两班历年来都统一由潘老师出题
        - 期末考试闭卷，全中文，全问答题
        - 充分参考老师提供的提纲进行复习即可

=== "宋明黎" 

    TODO：待完善
