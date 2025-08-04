---
abbrs: 
    - LLM 短学期
---

# 大模型应用与实践
<div class="badges">
<span class="badge is-badge">大二短学期</span>
<span class="badge is-badge">课程综合实践 Ⅱ</span>
</div>

## 课程学习内容

课程名是大模型应用与实践，但从课程内容上看，是偏向入门性质的课程。主要涉及的内容如下：

- 对 LLM 的基本介绍：包括发展历程、基本类型和原理以及特性和应用场景
- 提示词工程（Prompt Engineering）：涉及零样本和少样本提示(Zero-shot ＆ Few-shot)、上下文学习(ICL)、自注意力和多头注意力机制(Self-Attention ＆ Multi-Head Attention)等
- Transformer 架构：介绍了位置编码(Positional Encoding)、编码器（Encoder）和解码器（Decoder）、指令微调(Fine-Tuing)以及基于人类反馈的强化学习(RLHF)
- Agent 智能体：介绍了 Agent 智能体的基本概念、基于 LLM 的 Agent 智能体的设计、多 Agent 系统的设计以及检索增强型大语言模型(RA-LLM)

除此之外，课程还会请到清华、北航、百度等学校和公司的专家分享自己的研究经验和实践经验。

这些讲座分享的内容会分享科研界和工业界关于 LLM 的前沿技术，涉及的方向很多，包括但不限于：

- 视频生成 Video Generation
- 行为识别 Action Recognition

具体分享内容应该会随着每年请到的老师不同而变化。

总体而言，是一门适合入门和快速上手 LLM 的课程。

### 先修要求

理论上没有先修要求，但建议有基础的 Python 编程能力；如果有 AI 课程基础，在理解课堂知识上会事半功倍。

## 任课教师

本课程挂的是王文冠/朱霖潮两位老师的名字，但实际上课的只有朱霖潮一位老师。

[朱霖潮](https://person.zju.edu.cn/linchao)老师上课讲的很清楚，质量很好且有求必应。很照顾还没跟上进度的学生，并且手上还会随机刷新小零食，分给同学。下课前会做当堂课的内容总结，帮同学重新梳理思路。而且很喜欢同学问问题（“问题其实就是一种 Prompting”），跟他多多交流。


## 分数构成

本课程没有考勤分，不过朱老师会给多次出勤的同学小零食

- Assignment1(20%)：属于 Prompt Engineering 的作业，需要自己创建一个小的问题集，测试几个本地大模型的能力和性能
- Assignment2(60%)：属于 Agent 智能体的作业，需要使用本地大模型创建一个 Agent 智能体，完成一个数据分析和可视化的任务
- Lab1(10%)：在本地，使用小规模的莎士比亚文集数据上训练小型 GPT 模型，输出莎士比亚风格的文字
- Lab2(10%)：在本地实现Llama 2 7B模型的推理和量化，观察量化操作对模型推理性能的影响

Lab1 和 Lab2 都是认定型分数，只要验收通过就是满分。

## 参考资料

- 可以下载本地大模型的社区：https://huggingface.co/
- 可以用于运行本地大模型的工具：https://ollama.com/download
    - 对应的模型库：https://ollama.com/library  

下面是笔者在2024年短学期的资源：

- 该课程的笔记，可以用于参考大致的上课内容：[大模型应用与实践课程笔记](https://miraitowaves.github.io/notebook/Course/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8%E4%B8%8E%E5%AE%9E%E8%B7%B5/)
- Assignment2：https://github.com/miraitowaves/prompt-engineering