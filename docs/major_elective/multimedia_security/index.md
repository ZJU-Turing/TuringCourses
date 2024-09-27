# 多媒体安全
<div class="badges">
<span class="badge is-badge">IS 专业选修</span>
</div>


## 课程学习内容

本课程旧名 "信息隐藏与数字水印", 是黄劲老师开设的课程。主要授课内容基本可以概括为 "水印" 和 "隐写" 两个部分。课程内容较多, 且十分理论,  包括

+ 水印和隐写的介绍和性质
+ 水印:
    + 水印模型
    + 多比特信息嵌入
    + ECC（校验编码）
    + 应用原图作为辅助增强
    + Dirty-paper code, Lattice Code
    + 鲁棒水印
    + Content Authentication, 也就是 erasable 水印
+ 隐写
    + 经典算法: LSB对DCT系数（JSteg），OutGuess，F3,F4,F5（矩阵编码）以及混淆方法（random walk）;
    + Wet Paper, 对隐写的检测与攻击
    + 使用 Sample pairs 进行隐写分析
+ 电子取证、利用指纹信息进行身份认证等。

老师会在最后一节课进行总复习。

## 任课教师

仅有黄劲老师一位。黄老师授课很有个性, 思维跳脱、富有热情, 很喜欢跟学生交流。但是本课程内容较多也较杂, 可能稍难跟上。不过课余时间老师比较亲和, 有任何问题都会耐心解答。

## 课程教材

Cox, I., Miller, M., Bloom, J., Fridrich, J., & Kalker, T. (2007). *Digital watermarking and steganography*. Morgan kaufmann. 一本十分厚的书, 本课程内容除了取证部分外基本都是基于课本展开。虽然此书叙述<del>啰嗦</del>细致, 但也有未能讲清楚的地方。

## 分数构成

一般来说分数构成为: lab 40%, 期末 40%, 课堂表现 20%, 可能有稍许浮动。

+ lab 为 4~5 次, 基本包括
    + E_BLIND/D_LC 水印系统实现
    + E_SIMPLE_8/D_SIMPLE_8 多位信息水印系统实现
    + E_BLK_8/D_BLK_8 + Hamming Code 或 Trellis Code 水印系统实现
    + F4, F5 隐写算法实现
    
lab 不限定编程语言。每次代码量约在数百行, 虽不算难但也对编程能力稍有要求。

+ 期末开卷, 包括少量选择、判断以及 8 道简答, 主要侧重课程内容的理解。要求英文作答。
+ 课堂表现分为两个部分:
    + 老师不会点名, 但会随堂 quiz 9 次之多 :-)
    + 每次课前会让两人一组进行一个简短的展示, 10 分钟左右; Topic 包括书中未讲到的部分, 也包括 lab 实现等。

## 参考资料

+ https://www.cc98.org/topic/5362725
+ https://github.com/QinJiuJiu/Information-hiding-and-digital-watermarking