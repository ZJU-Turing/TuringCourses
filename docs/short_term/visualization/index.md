# 大数据可视化
<div class="badges">
<span class="badge cs-badge">大一短学期</span>
<span class="badge cs-badge">课程综合实践 Ⅰ</span>
</div>

## 课程学习内容

课程的目标是学习可视化的基本思想和主要方法，培养利用可视化技术分析数据的能力，具体就是学习如何使用 Tableau、Python 等工具进行数据处理和数据可视化，以及学习网页前端知识开发一个可视化系统（可选）。课程内容有：

- 上午的理论课程，包括可视化交互、空间数据可视化、高维数据可视化、时序数据可视化等，中文授课
- 中午的前沿讲座，由国内外知名学者分享前沿知识，上课和问答都用英文，**是国际化教学但不是国际化课程**
- 下午的实践课程，包括 Tableau 的基本用法以及 HTML、CSS、JavaScript、React 等前端知识，只是快速过一遍，对没有基础的人不太友好，不过如果不开发可视化系统的话也用不到

该课程的同时是国际暑期学校，授课对象除了线下上课的浙大学生，还包括数百位线上上课的外校学生。


### 先修要求

没有先修要求，但是对于想要追求高绩点的人来说，最好有网页前端开发基础，也推荐前端大佬选这门课。

如果没有前端基础的话，推荐在期末结束之后、短学期开始之前进行自学，简单了解一些 HTML、CSS、JavaScript 的基本知识。


## 任课教师

虽然课程挂名的是巫英才和陈为老师，但实际上是由十几位老师轮流上课，其中包括浙大的教授和国内外其他大学的教授。


## 分数构成

- 课程项目 1 (20%)
    - 个人作业：学习可视化分析工具的使用
    - 会给提供一份数据，比如 xlsx 文件，要求使用 Tableau 进行数据清洗和图表制作，然后写一份报告
- 课程项目 2 (50%)
    - 小组作业：使用可视分析工具（Python, Tableau, ...）做数据分析，或者自己设计并开发一个可视分析系统
    - 每组三人，自行组队，自由选题，需要提交报告和代码
- 课程项目 2 展示 (20%)
    - 在最后一节课（最后一天下午）展示，每个小组需要全员到场，没来视为缺考
    - 有 3 分钟的展示时间，展示内容至少需要包括分工、数据背景、可视系统设计+分析，重点是**基于数据和可视化，描述数据故事**
    - 助教和老师会坐在前排，在展示完毕后进行提问，问的问题基本不难，只要对自己的项目了如指掌就不会有问题
- 出勤 (10%)
- Bonus (5 points) 设计并开发一个可视分析系统


## 课程学习建议

### 课程项目 1

课程项目 1 的难度不大，报告也不需要卷，基本上只需要把每一步做什么和相应截图糊上去就好了，主要包括数据清洗的操作配置、前后的对比图、界面操作配置、可视化效果图等。提交截止时间是课程结束后两天，所以不会有太大压力。

需要注意的是 Tableau 的下载安装和使用都比较麻烦，很多操作逻辑需要靠猜，实践课程讲到这部分时最好听老师讲课。

### 课程项目 2

课程项目 2 的难度和工作量较大，主要任务是寻找数据、处理数据、分析数据、可视化数据，然后在报告和 PPT 中展示小组的工作成果。图灵的同学最好找上大佬一起参加，~~大佬对项目的高度很重要~~。最后提交的报告会写上每个人的分工，老师和助教会判断你的工作量给你相应的给分，~~想要高分不能只靠大佬带飞~~。

首先比较麻烦的是选题，选的数据最好既要有趣又能得出新颖的 insight。老师会在课上推荐几个数据集网站，其中个人最推荐的是 [Kaggle](https://www.kaggle.com/datasets)，上面有很多信息完整且内容有趣的数据集，有能力的还可以尝试用爬虫爬取数据。

数据处理方面，码力较弱的可以使用 Tableau 等 GUI 工具，不过个人更推荐使用 Python 脚本，因为它更加灵活，不仅本身的文本处理能力强大，还有着丰富的第三方库可以使用，比如 sqlite3 可以进行数据库操作，pandas 可以用于数据清洗、统计分析和可视化，sklearn 可以方便地完成聚类和降维等。不过数据处理并不是特别重要，重心应该放在可视化上。就实际情况来看，大多数人的数据处理只涉及数据清洗，最多再涉及列的加减乘除，连简单的聚类和降维都几乎见不到。

可视化方面，因为 Bonus 的存在，最好选择开发可视分析系统，也就是前端页面。小组内有前端大佬的话自然再好不过，没有的话其实自学起来也不是很难 ~~（maybe）~~，跟着 [Echarts](https://echarts.apache.org/handbook/zh/get-started/) 官方文档走一遍就足够了，只需要一点 HTML、CSS、JavaScript 的知识就可以看懂，~~就算不懂也应该能猜出来吧（？）~~。除此以外，还有 [D3.js](https://d3js.org/getting-started)、[Chart.js](https://www.chartjs.org/docs/latest/getting-started/) 等众多前端可视化工具可以使用，不过 Echarts 应该是最容易上手的，文档和中文社区也最丰富。

如果有余力的话，还可以学习 [Vue](https://cn.vuejs.org/guide/introduction.html)、[React](https://react.docschina.org/learn) 等前端框架，其中 Vue 对于小白来说更容易上手，官方中文文档更加友好，不过老师应该会更青睐于 React，实践课程教授的也是 React。如果想要做出更加好看的前端页面的话，还可以考虑使用 [Element UI](https://element-plus.org/zh-CN/#/zh-CN)、[Tailwind CSS](https://www.tailwindcss.cn/)、[Daisy UI](https://daisyui.com/) 等组件库，这些组件库都有着丰富的组件和模板，可以帮助你快速搭建一个漂亮的前端页面。



## 参考资料
- 前端开源可视化项目：
    - [VisChart](https://github.com/Zhroyn/VisChart)
- 前端开发框架：
    - [Vue](https://cn.vuejs.org/guide/introduction.html)
    - [React](https://react.docschina.org/learn)
- 前端数据可视化工具库：
    - [Echarts](https://echarts.apache.org/handbook/zh/get-started/)
    - [D3.js](https://d3js.org/getting-started)
    - [Chart.js](https://www.chartjs.org/docs/latest/getting-started/)
    - [AntV](https://antv.antgroup.com/zh)
    - [Highcharts](https://www.highcharts.com.cn)
- 前端组件库：
    - [Element UI](https://element-plus.org/zh-CN/#/zh-CN)
    - [Material UI](https://mui.com/material-ui)
    - [Ant Design](https://ant.design/docs/react/introduce-cn)
    - [Tailwind CSS](https://www.tailwindcss.cn)
    - [Daisy UI](https://daisyui.com/)

