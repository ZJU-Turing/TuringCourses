# 人工智能芯片与系统
<div class="badges">
<span class="badge is-badge">AI 专业必修</span>
</div>

## 学习内容

2024年人工智能芯片与系统内容如下（参考王则可老师课程大纲）

- Lec 1 - Lec 5 计算机体系结构相关内容（ROB、Tomasulo、Memory等）

- Lec 6 - Lec 8 GPU & GPU Optimization

- Lec 9 - Lec 10 Cache

- Lec 11 - Lec 13 AI Accelarator

- Lec 14 Parrallel Training

- Lec 15 - Lec 16 安排一次Guest Talk和一次课程复习

## 授课老师 

王则可老师。王则可老师上课相对细致，答疑也很耐心负责。虽然可能在授课过程中王老师难免有一些ppt reader的趋势，但是课程内容相对新颖也有不少收获。真正对AI系统和AI芯片感兴趣的同学相信可以在课上学到不少干货，若对这方面的兴趣不高，掌握基本的知识点并在考前认真复习也能够收获一个让自己满意的分数。

## 分数构成

+ 课堂表现（5%）
    - 上课开始前王老师表示会有点名和Quiz，但最终并没有落实，<del>这肯定是个好事</del>。24年就公布分数细节来看大家应该都给满了，但还是建议大家之后好好上课。

+ 实验（35%）
> 以下为24年AI芯片和系统课程的五个实验，按照王老师上课的描述，在之后的课程中会考虑再添加一个实验帮助大家更好理解GPU和CUDA
    - Lab 1 Pipeline CPU (包含forwarding, 不涉及 ROB 和 Tomasulo 算法，提供代码框架)
    - Lab 2 涵盖矩阵运算的Pipeline CPU
    - Lab 3 CUDA编程初步（NIDIA 教程）
    - Lab 4 CUDA加速（利用reduction和wrapping对求和进行加速，提供pipeline与baseline）
    - Lab 5 Ascend C 算子实现（基于ModelArts平台，提供代码框架）

+ 期末考（60%）
    - 半开卷考试，可以携带一张A4纸（打印手写均可）。考试内容涉及到上课讲过的所有内容，考试重点可以参考最后一节复习课。

## 学习建议

这门课的实验相对简单，也提供实验框架，对比计算机组成（系统 I II III）都轻松不少，建议大家对待实验不要当ddl战士，可以尽快完成。

像这样的系统课程需要记忆和理解的知识点也相对较多，比起直接硬背，建议大家可以多进行实操（多写写CUDA代码，在课程要求之上继续学习NVIDIA提供的教程），不仅有助于考试对CUDA的考察，更重要的是在后续的科研中可以对PyTorch的相关接口有更深入的理解。
