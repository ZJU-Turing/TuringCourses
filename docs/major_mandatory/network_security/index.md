---
abbrs:
    - 网络安全
---

# 网络安全原理与实践

<div class="badges">
<span class="badge is-badge">IS 专业必修</span>
</div>

## 课程学习内容

本课程主要介绍基本的网络安全攻防手段，具体内容为：

1. DDoS 攻击与防御：介绍了大量的对称与非对称 DDoS 攻击以及防御手段
2. 安全路由：在回顾计算机网络中学习的路由算法和协议的基础上，基于路由算法的弱点介绍相应的攻击和防御方案
3. 匿名通信：介绍通过代理节点实现匿名通信的方式，特别是洋葱路由的核心算法，以及相应的攻击手段
4. Web 安全：介绍 web 基础、SQL 注入、同源策略、跨站攻击等常见的 web 安全问题
5. 邮件安全：介绍邮件传输相关的认证算法，核心是邮件的公钥认证体系中的整体架构和关键算法
6. 流量分析：介绍防火墙、入侵检测系统（IDS）、入侵防御系统（IPS）的原理
7. 回溯：介绍如何回溯攻击者的身份，如 IP Traceback，Link Testing，Logging-based Traceback 和 Bloom Filter 等方法的原理
8. 网络保护：回顾前面章节介绍的防火墙、入侵检测系统（IDS）等内容，同时也介绍负载均衡、用户认证、访问控制等内容

这门课算得上是信息安全专业最早开设的安全类课程之一，因此一开始这门课还会讲授物联网安全、区块链安全等主题，但后来这些内容都被单独开设的新课程取代，保留下来了以上内容。

### 预修要求

* 计算机网络
* 密码学

## 任课教师

=== "卜凯"

    卜凯老师算得上最早一批来到网安学院的老师，研究方向也与网络安全有很大的关联，因此也是这门课最合适的授课人选，信安专业每年也都会预置卜凯老师。特别注意的是，卜凯老师的课程是国际化课程，因此授课是英文的，整体而言比较清晰，部分时候可能有些迷糊，但老师也会经常切换成中文来进行一些总结和讨论来有助于大家理解。

    卜凯老师为人非常有亲和力，就像个大哥哥一样，我们亲切称呼他为 kg。kg 有一个 QQ 大群，是从他第一次给 2016 级体系结构开课开始一直沿用至今的大群。里面会偶尔讨论一些升学相关的问题，kg 也会经常冒泡水群（kg 独特的水群方式感染了一届又一届的计院学子）。

    kg 上课互动性比较强，会经常有讨论的环节，也有两次 quiz 记为平时分，平时也可能有随机的点名。除此之外实验课不管讲不讲实验也必须到场，还专门挑不讲实验的实验课点名，当然是一个一个走到你旁边签字，然后顺带认识一下你。当然最终的给分 kg 也是相当慷慨的，査老师的均绩非常真实。

=== "林峰"

    林峰老师讲课不像卜凯老师那样热情，比较平淡，当然也能将课程内容讲清楚。林峰老师有一次 quiz 当签到，相对而言互动会比 kg 少很多，如果跨专业同学选不到 kg 也可以考虑选择林峰老师，但林峰老师的课程不是国际化，中文授课，这点需要注意。

## 课程教材

无指定教材，老师课前会发布 PPT，考试内容都在 PPT 上。卜凯老师上课也倒苦水说这门课没有合适的教材，因此内容的选取也是耗费了不少的精力。

## 分数构成

这门课分数由三个部分构成:

* 作业（10%）

    有一次较大的作业，大约 30-40 个简答题，kg 说只要完成度到达一定层次即可给满分。当然这 10% 除了作业之外还包括两次 quiz 和点名，quiz 难度不大，都是上课讲的重点内容。

* 实验（40%）：共 3 次实验，内容和分数占比分别为：
    - 抓包（10%）：利用 Burp Suite 进行抓包实现一系列的攻击
    - 伪冒攻击（10%）：利用 ARP Spoofing 实现 DNS Spoofing
    - Web 安全（20%）：一个靶场的简单难度，包括 SQL 注入、XSS、CSRF等所有常见的基础攻击实验
    
    这门课的实验设计比较完整，事实上几乎所有的步骤助教都会完整演示，因此不必担心无法完成。并且这门课的实验也是很有趣的，总体而言体验是很好的。需要提醒的是，实验可以用科研导向的 project 替代，但暂时并没有听说谁这么做，如果对网络安全研究非常感兴趣的同学可以尝试。

* 期末考试（50%）

    这门课考试采取半开卷的形式，允许带一张手写 A4 纸。考试题型是单选题、判断和简答。由于是国际化课程考试内容都是英文的，答题也要求用英文，当然实在不会写也可以偶尔几个词用中文。在 CC98 可以找到历年卷，大致的风格是一致的，内容因为三年不能重复因此参考价值有限。但实际上 kg 也承认这门课能考的点也就那么多，并且两个班最后都有复习课（kg 复习课会关话筒，所以可以提前准备录音设备），信息量 2020 级来看 kg 班明显大于林峰班，但以往林峰老师班也有一定信息量，所以还是建议都参考一下。这门课考试难度并不大，核心就是 A4 纸一定要按重点抄完整即可，最后的给分也非常慷慨。