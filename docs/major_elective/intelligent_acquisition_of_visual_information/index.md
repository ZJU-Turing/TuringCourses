# 智能视觉信息采集
<div class="badges">
<span class="badge ai-badge">AI 专业选修</span>
</div>

## 课程学习内容

本课程分为理论部分和实验部分。理论课为全英文授课，难度较大，内容上与 AI 专业必修课《计算机视觉导论》有一定重合，但是更偏重摄影学，主要介绍视觉信息、相机模型、表面与体积采集等等；同时，课程并不会过多介绍 OpenCV, OpenGL, Tensorflow 等编程技术，在实验/大作业用到时需要自行查阅资料。理论课包含以下章节：

- Modern Camera Systems
- Lightfields & Image Relighting
- Measuring Depths
- Volumetric Acquisition
- Appearance Capture
- Advanced Topics

实验部分主要包含四次组队实验，在最后完成并展示大作业（见“分数构成”章节）。

## 任课教师

[吴鸿智](https://svbrdf.github.io/) 吴老师对待学术非常认真严谨，同时品味也很高。他的课堂偏重引导学生思考“为什么”而非一味灌输知识，讲课逻辑清晰，英语也比较流利。吴老师也很欢迎学生与他交流包含专业理论、大作业选题与科研方向在内的任何问题。

## 参考书目

- Computer Vision: Algorithms and Applications, 2nd Ed, 2021. Szeliski, Richard. Springer.
- Deep Learning, 2016. Goodfellow et al. MIT Press.
- Physically Based Rendering: From Theory to Implementation, 3rd Ed, 2018. Pharr et al. Morgan Kaufmann.
- Elements of Information Theory, 2nd Ed, 2006. Cover, Thomas & Thomas, Joy. Wiley.

## 分数构成

课堂表现 20% + 实验 40% + 大作业 40%

=== "课堂表现"

    课堂表现由 Q&A 和 Quiz 两部分构成：

    - Q&A (2%): 老师会在课堂上提问，自由举手回答，一次正确回答加 1 分（可以中文回答）。
    - Quiz (18%): 课前小测，共三次，不会提前通知。每次小测只有一道比较开放的简答题，不会直接出自课堂内容，但可以用课上知识回答，更加考查对知识的理解（可以中文作答）。

=== "实验"

    本课程实验均为三人组队完成，每组每次实验需要上交一份全英文撰写的实验报告。课程为每一组提供两台 Basler daA2500-14uc 相机与一台投影仪用于完成实验。五次实验分别为：

    1. Image Acquisition (6%): Basler 相机与 Pylon Viewer 的使用（含 Bonus 25%）
    2. Project Proposal (2%): 大作业选题与方案（无实验）
    3. Single Camera Calibration with OpenCV (9%): 相机标定与单目视觉（含 Bonus 10%）
    4. Passive Two-view Stereo (11%): 基于双目视觉的深度估计
    5. Projector-Camera-Based Stereo Vision (12%): 基于结构光的深度估计

=== "大作业"

    大作业也是三人组队完成，自主选题，内容上要有动手实践的内容，比较重视实验设计，同时鼓励软硬件结合开发。评判标准如下：

    - Novelty (30%)
    - Experimental Evaluation (30%)
    - Technical Depth (20%)
    - Completeness (10%)
    - Presentation (10%)

    可以借用实验室的相机与投影仪，也可以申请小额器材的报销。关于优秀课程项目可以参考[这个视频](https://www.bilibili.com/video/BV1oK4y1D7kW)。值得一提的是，在大作业获得最高分的队伍可以得到吴鸿智老师的奖励（24-25 秋冬是《塞尔达传说：王国之泪》的手办）。

## 学习建议

《智能视觉信息采集》这门课为 2.5 学分却是单学期课程，加上吴鸿智老师对教学的相对高要求，可想而知 workload 不会小。上课体验而言，吴老师的英语比较流畅，适应之后可以跟上课程节奏；但是最后几周随着课程难度增大，想听懂全部内容比较困难。个人认为吴老师的“启发式”授课在整个计算机学院中称得上一股清流，注重结论产生的过程又触及本质，即便是全英语也可以把知识讲得清楚。如果想在课堂表现上获得不错分数，尽量不要错过举手回答问题的机会，同时每周上课前可适当复习上周 slides 以免突然出现 quiz 时头脑一片空白。

对于实验部分，本课程的实验压力并不小，基本每周都有实验，需要当堂完成数据收集并在一周时间内上交报告；这门课虽然“不会直接讲授编程内容”，但实验与大作业对代码能力有一定要求，包括 OpenCV 在内的一些开源库需要自行检索资料学习。值得一提的是，前两次实验有 Bonus，非常建议在时间宽裕的情况下完成。

关于大作业，其实最后用于大作业的时间并不长，Lab5 到期末展示不过一周多的时间，最好是在第三周前多与老师交流，将大作业的结构框定在可控的范围内。从课程展示的点评环节看，老师本人更加青睐精巧的实验设计，不过如果手头有现成项目进行改编也未尝不可。

总而言之，这门课从里至外渗透着吴鸿智老师一以贯之的教学追求：贴近本质、重视应用与 high-level。如果你有一定的知识储备与代码能力，或是较强的自主学习驱动力，那么选这门课能收获不错的体验；但是，如果单纯为了水选修学分，这门课的庞大工作量与最后或将不及预期的分数可能比较劝退，属于事多给分还行的范畴。
