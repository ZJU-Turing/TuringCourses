---
abbrs: 
    - Rust 开发实训
---

# <课程名称> 
<div class="badges">
<span class="badge is-badge">大二短学期</span>
<span class="badge is-badge">课程综合实践 Ⅱ</span>
</div>

## 课程学习内容

这门课内容非常之多，几乎把 Rust 从入门到实践开发都过了一遍，主要有下面的部分：

* Rust 语言基础
* Rust 高级特性（泛型、字符串、迭代器、智能指针、宏）
* Rust 异步系统（Future、async/await）
* Rust RPC 框架（主要是字节自研开发的 [volo 框架](https://github.com/cloudwego/volo)）
* Rust HTTP 框架使用

上课内容很多，但都是以很快的速度带过，~~做好心理准备~~。

### 先修要求

理论上没有先修要求，但是最好能掌握一门现代的面向对象的编程语言（如 C++/Java），对数据结构、操作系统、数据库系统有一定的了解。

## 任课教师

本课程挂的是张寅老师的名字，但张老师只负责最后登分，实际上的授课老师是来自字节跳动的 [CloudWeGo 团队](https://github.com/cloudwego) 的学长们，给分也是由他们完成。学长们都是在字节跳动从事相关开发工作，因此本身水平是很高的，人也很好，回答问题都很热情。不过大部分是第一次讲课，因此讲课水平参差不齐。此外虽然风格不同，但大家几乎都是翁恺老师所说 Nice to have 的践行者，上课的进度很快，需要课下自己消化。

虽然查老师上张寅老师的短学期课程评价不高，但是就 2023 年短学期的情况来看，给分相当慷慨。

## 分数构成

* 平时作业（50%）  
每节课都会布置与当堂课讲的内容相关的作业，基本上只有一两天时间。对于之前没有学过 Rust 的同学来说，后面几次作业难度大，大家基本上都是抄的 GitHub 上的开源代码。下面列出 2023 年短学期的课程作业：
    * 完成命令行搜索工具 myfind
    * 完成 Rust 高级特性的相关 Exercise（泛型、字符串、迭代器）
    * 完成 Rust 高级特性的相关 Exercise（智能指针、宏）
    * 完成一个简易多任务多线程的 Runtime（基于字节自研的 [volo 框架](https://github.com/cloudwego/volo)）
    * 完成一个简易的 Mini-Redis
    * 完成一个简易的 HTTP 服务器（利用 axum）  
    因为大作业时间紧张，这个作业最后变为了 bonus。
* 大作业（50%）  
三人一组，最后进行展示答辩，评委是字节团队的老师和学长。因为课程紧张，从作业布置到展示只有三天不到的时间。2023 年短学期的大作业是基于平时作业开发的 Mini-Redis 进行拓展，要求实现 AOF 持久化、Redis 主从架构、Redis Cluster。

字节跳动十分推崇开源，因此上述作业均要求公开上传到 GitHub 仓库。

## 参考资料

这里给出 2023 年短学期的[课前准备文档](https://bytedance.feishu.cn/docx/DX02deweRowa9xxsAEzcS122n1c)。

* [Rust 程序设计语言](https://www.rustwiki.org.cn/zh-CN/book/title-page.html)
* [Rust 圣经](https://course.rs/about-book.html)
* [rustlings](https://github.com/rust-lang/rustlings) 里面有很多 Rust 相关的小练习

下面是笔者 2023 年短学期的课程仓库：

* 平时作业：https://github.com/HobbitQia/Rust-2023-Homework
* 大作业：https://github.com/HobbitQia/Mini-Redis