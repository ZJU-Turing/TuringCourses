# 电子工程训练
<div class="badges">
<span class="badge cross-badge">跨专业课程</span>
<span class="badge labor-badge">劳育认定</span>
</div>

电子工程训练是信息与电子工程学院开设的专业课程，分为[电子工程训练（甲）](#course_1)和[电子工程训练（乙）](#course_2)，甲是信电学院专业的专业基础课，乙是信电学院开给能源工程学院车辆工程专业的专业实践课。

---

## 电子工程训练（甲） {#course_1}

### 课程学习内容

电子工程训练（甲）的课程学习基本如下：

* 电子工程训练初步，占时五周左右，训练内容包括：
    - 认识电子元器件，如电阻器、二极管、集成电路等
    - 学会使用常用的电子仪器，如示波器、信号发生器、万用表等
    - 了解焊接工艺，进行手工焊接训练
    - 学会调试焊接好后的电路板，如流水灯、幸运转盘等
* 电子工程训练提高，占时十一周左右，训练内容包括：
    - 了解并学习 [Arduino IDE](https://www.arduino.cc/en/software)，学会使用 Arduino 完成相应任务
    - 学会结合各种技术开发硬件系统，如智能插座、智能 WiFi 机器人小车

电子工程训练（甲）的课程要求比电子工程训练（乙）更高，其差别主要体现 Arduino 上，除此以外区别不大，因此可以随便从中选一个，没必要为此多等一个学期。

本课程需要两人小组合作，没有期末考试，但需要完成实验报告。虽然实验难度不大，但任务较多，如果不预习的话，上课时基本上没有摸鱼时间。不过课程本身十分有趣，跟着学下来可以基本掌握焊接、Arduino 硬件编程等实用技能，收获很大，给分也相当不错，非常值得一学。

本课程同时算作劳育课和跨专业课，不过学分只有 1.5 分，因此更推荐缺劳育的同学选这门课。

#### 先修要求

本课程和普物实验、计逻一样涉及电子仪器的使用，不过会有详细的教学，~~可以当作普物实验和计逻的先修课~~，不用担心。

如果是“施红军、叶险峰、邓靖靖”班的话，在进行 Arduino 基础实验时，还会和计逻一样涉及寄存器、电平跳变、串行并行等知识，不过课程对此要求不高，不需要深入了解这些知识就可以完成实验，如果没有先修也不用担心。

### 任课教师

本课程主要分为两个班，老师评分都很高，人都很好，选择任意一个都行。

=== "施红军、叶险峰、邓靖靖"

    在电子工程训练提高部分，会先进行 Arduino 基础实验，然后进行智能 WiFi 小车实验，各需完成一份报告。

    Arduino 基础实验占时四周左右，共二十四个例程，主要包括：

    - Arduino 入门、LED 显示、按键控制 LED
    - 模拟量读取、PWN 调光、蜂鸣器发声、传感器使用
    - 接口扩展、点阵显示、数码管显示、LCD 屏显示
    - 电机控制、红外遥控、超声波测距、继电器使用

    智能小车实验需要用到 Arduino Uno 开发板控制小车，与 Arduino 基础实验一样，需要修改提供的代码以实现各种功能。

=== "马洪庆、金向东、李培弘"

    在电子工程训练提高部分，会先进行智能插座工程实践，然后进行智能 WiFi 机器人小车设计实验，其中后者只需验收不用写报告。
    
    智能插座占时四周左右，涉及使用 Arduino，需要修改 Arduino 代码调试智能插座。智能 WiFi 小车则不需要用到 Arduino，开发所使用的是老师提供的 APP。

### 分数构成

!!! warning "未找到具体的分数比例，以下为大致的分数构成，具体任务可能会有变化"

=== "施红军、叶险峰、邓靖靖"

    - 出勤
    - 实验样品的验收
    - 调试演示的验收
    - 实验报告
    - 桌面整理与卫生、套件整理、小车安装规范、操作规范等

    作业只包括线下验收和线下提交纸质版实验报告，不需要用到学在浙大。

=== "马洪庆、金向东、李培弘"

    除了出勤、验收和报告以外，还包括：

    - 预习作业
    - 互评作业
    - 课程总结
    - 照片、视频、总体表现等

    作业提交主要在学在浙大上进行，实验报告只需电子版。

### 学习建议

因为每节课的课程内容很多，老师讲解的速度会比较快，需要认真听讲才能跟上，其中有些内容对于完成实验并不是必要的，可以当作扩展知识；还有些内容可以帮助你更好地理解电路或代码，不清楚的话可能在课上茫然无措、效率低下，因此若感到跟不上老师节奏最好提前预习。但总的来说，大部分实验的电路图和代码都在 PPT 中，即使完全不懂，照着做也能完成。不过最好还是要对原理有所了解，这样不仅能快速完成本节课的实验，对之后写实验报告、做新的实验也更有帮助。

在熟练了以后，很多内容不需要老师的讲解就能看懂，尤其是 Arduino 相关部分。建议提前预习 PPT 并敲好代码，这样上课时只需要连接电路，可以快速完成实验，空余的时间就可以用来写报告。不过需要注意的是，"马洪庆、金向东、李培弘"班的智能小车 PPT 省略较多，听课之后才能知道怎么做，上课讲到这部分时需要格外认真，不然可能一不小心就把老师说要怎么改代码给忘了。

---

## 电子工程训练（乙） {#course_2}

### 课程学习内容

电子工程训练（乙）在课程内容上和甲班接近但是相对更加简单，课程进度和甲班基本一致，可以参考电子工程训练（甲）的相关内容，但是在智能插座制作过程中对 Arduino 没有过多要求，仅仅有一个写函数控制 GPIO 口的 bonus，当然也比甲班多了一些调试测量工作，总体还是轻松的。

#### 先修要求

由于是乙班。并未对代码有过多的要求。所以没有任何先修要求。当然，对开发板、集成电路有一定了解的同学上起来会更加容易一些。

### 任课教师

我所在的班级任课教师为马洪庆、金向东、李培弘，这三位老师也开设了绝大多数的平行班。三位都是工程师，人非常好，会耐心地解决同学们遇到的各种奇奇怪怪的问题，给分也非常好。

### 分数构成

老师没有公布具体的给分比例，但是总体来说只要认真完成都会获得非常不错的分数，下面是一些影响因素：

- 出勤，尤其记得下课的时候钉钉要记得签退
- 基础部分电路板的验收，包括功能实现和焊接技术，当然总体给分都很好，但是还是尽量在如剪短管脚之类的地方做规范一些（
- 调试演示的验收视频，如智能机器人小车的循迹
- 实验报告，初步部分需个人完成实验报告，后面的部分为二人小组共同完成报告，还是比较轻松
- 桌面整理、操作规范

### 学习建议

课程难度总体不大，一下是几点小建议：

- 装配过程中，一定要先确定好元件正确安装后再焊接（不然可能在拆元件上浪费很多很多时间）
- 在使用可调电源等设备时，一定注意极性和电压（说来容易，实际操作中经常出各种奇奇怪怪的事情），不然可能导致设备损坏，给自己和他人带来不便
- 遇到无法解决的问题时及时寻求老师帮助（注意，应当事先自行寻求解决方案并进行尝试），因为给到的元器件本身可能存在问题
- 在作业前应当认真阅读老师给的材料并对整个流程有一个认识，不然可能会导致不断返工
- 在调试过程中要有充足的耐心，不然课程可能会艰难
