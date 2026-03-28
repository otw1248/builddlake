

# 中华人民共和国国家标准

GB/T 38614—2020

# 基于柔性铰链机构和压电陶瓷驱动器的 纳米定位与扫描平台测量方法

# Measurement method for nano positioning and scanning stage based on flexure hinge mechanism and piezo actuator

2020-04-28 发布

2020-11-01 实施

国家市场监督管理总局  

国家标准化管理委员会  

发布

## 目次

前言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 测量条件 …… 1    
5 测量仪器 …… 1    
6 测量方法 …… 1    
6.1 轴向行程 …… 1    
6.2 准确度 …… 2    
6.3 单向重复定位精度 …… 2    
6.4 双向重复定位精度 …… 3    
6.5 迟滞误差 …… 4    
6.6 线性度 …… 5    
6.7 位移分辨力 …… 6    
6.8 角摆偏差 …… 6    
6.9 直线度 …… 8    
6.10 平面度 …… 9    
6.11 正交误差 …… 10

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国电子测量仪器标准化技术委员会(SAC/TC 153)提出并归口。

本标准起草单位：沈阳建筑大学、三英精控（天津）仪器设备有限公司、广东工业大学、中国计量科学研究院、苏州昊通仪器科技有限公司、沈阳理工大学。

本标准主要起草人：须颖、戴敬、邵萌、安冬、施玉书、贾静、戴超、文杰、石怀涛。

# 基于柔性铰链机构和压电陶瓷驱动器的纳米定位与扫描平台测量方法

## 1 范围

本标准规定了基于柔性铰链机构和压电陶瓷驱动器的纳米定位与扫描平台（以下简称为平台）的测量条件、测量系统和测量方法。

本标准适用于平台的研究、设计、生产、检测及使用。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 11336—2004 直线度误差检测

GB/T 38616—2020 纳米定位与扫描平台术语

## 3 术语和定义

GB/T 38616—2020 界定的术语和定义适用于本文件。

## 4 测量条件

平台的测量应满足如下条件：

a）测量场地应无影响测量精度的灰尘、振动、气流扰动和较强磁场；

b）测量时的环境温度为 $ 20\pm1 $ ℃，其变化应不大于 $ 0.5\;^{\circ}C/h $ ;

c) 测量时的环境相对湿度为 $ 50\pm5\% $ ;

d）测量前应确认平台无影响测量正确性实施和测量结果的外观缺陷；

e） 测量时平台处于正常工作状态。

## 5 测量仪器

本标准中推荐使用激光干涉仪（以下简称干涉仪），角摆偏差也可使用自准直仪，测量仪器精度应满足测量要求。

## 6 测量方法

### 6.1 轴向行程

#### 6.1.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行轴向行程测量：

a）将平台移动至行程反向极限位置，干涉仪测量读数清零；

b）将平台移动至行程正向极限位置，记录干涉仪测量值；

c）重复步骤 a) 和步骤 b) 不应少于 3 次。

#### 6.1.2 计算

轴向行程 T，按式(1)计算：

 $$ T=\frac{1}{n}\sum_{j=1}^{n}T_{j} $$ 

式中：

 $ T_{i} $  ——平台第 i 次轴向行程测量值；

n ——测量次数, $ n \geqslant 3 $ 。

### 6.2 准确度

#### 6.2.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行准确度测量：

a）按图1所示，在全行程平均分布11个测量位置，分别为 $ p_{i}(i=1,2,\cdots,11) $ ，其中 $ p_{1} $ 为行程反向极限位置， $ p_{11} $ 为行程正向极限位置；

b）将平台移动至第1个测量位置 $ p_{1} $ ，干涉仪测量读数清零；

c）将平台从  $ p_{1} $  开始依次定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，在每个位置稳定后记录该位置的干涉仪测量值；

d）重复步骤 b) 和步骤 c) 不应少于 5 次。

 $$ \begin{array}{l}\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\longrightarrow\left|\longrightarrow\right|\end{array} $$ 

<div style="text-align: center;">图 1 单向测量位置行程示意图</div>


#### 6.2.2 计算

第 i 个测量位置的准确度  $ A_{i} $ ，按式(2)计算：

 $$ A_{i}=\left|\frac{\sum\limits_{j=1}^{n}P_{ij}}{n}-P_{i}\right|\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{ij} $  ——平台第 i 个测量位置的第 j 次测量值；

 $ P_{i} $  ——平台第 i 个测量位置的目标值；

n ——测量次数, $ n \geqslant 5 $ 。

取  $ A=\max(A_{i}) $  为平台被测轴的准确度。

### 6.3 单向重复定位精度

#### 6.3.1 测量步骤

单向重复定位精度测量步骤同6.2.1，其中步骤d)的重复步骤b)和步骤c)不应少于10次。

#### 6.3.2 计算

单向重复定位精度计算过程如下：

a）按式(3)确定第i个测量位置的正向平均测量值 $ \overline{P}_{i} $ 

 $$ \overline{P}_{i}\uparrow=\frac{\sum_{j=1}^{n}P_{ij}\uparrow}{n}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{ij} $ ↑——平台第i个测量位置的第j次正向测量值；

n ——测量次数, $ n \geqslant 10 $ 。

b）第 i 个测量位置的正向重复定位精度  $ R_{i} $  ↑，按式(4)计算：

 $$ R_{i}\uparrow=\sqrt{\frac{\sum_{j=1}^{n}(P_{ij}\uparrow-\overline{P}_{i}\uparrow)^{2}}{n-1}}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{ij} $ ↑——平台第i个测量位置的第j次正向测量值；

 $ \overline{P}_{i} $  ↑ ——平台第 i 个测量位置的正向平均测量值  $ \overline{P}_{i} $  ↑；

n ——测量次数, $ n \geqslant 10 $ 。

取  $ R \uparrow = \max(R_{i} \uparrow) $  为平台被测轴的正向重复定位精度。

注：本标准中仅规定了正向重复定位精度的测量方法，反向重复定位精度的测量方法参照正向重复定位精度。

### 6.4 双向重复定位精度

#### 6.4.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行双向重复定位精度测量：

a）按图2所示，在全行程平均分布11个测量位置，分别为 $ p_{i}(i=1,2,\cdots,11) $ ，其中 $ p_{1} $ 为行程反向极限位置， $ p_{11} $ 为行程正向极限位置；

b) 将平台移动至第 1 个测量位置  $ p_{1} $ ，干涉仪测量读数清零；

c) 将平台从  $ p_{1} $  开始依次正向定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，再从  $ p_{11} $  开始依次反向定位到  $ p_{10}, p_{9}, \cdots, p_{1} $ ，在每个位置稳定后记录该位置的干涉仪测量值；

d）重复步骤 c) 不应少于 6 次。

<div style="text-align: center;"><img src="imgs/img_in_image_box_385_1120_824_1217.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图 2 双向测量位置行程示意图</div>


#### 6.4.2 计算

双向重复定位精度计算过程如下：

a）由于第一次测量误差较大，在进行双向重复定位精度数据处理时将第一次测量数据去掉，取m=n-1，其中n为测量次数。

b) 按式(5)确定第 i 个测量位置的双向平均测量值  $ \overline{P}_{i} $  :

 $$ \overline{P}_{i}=\frac{\overline{P}_{i}\uparrow+\overline{P}_{i}\downarrow}{2}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ \overline{P}_{i} $ ↑——平台第i个测量位置的正向平均测量值；

 $ \overline{P}_{i}\downarrow $  ——平台第 i 个测量位置的反向平均测量值。

c）第 i 个测量位置的正向重复定位精度  $ R_{i} \uparrow $ ，按式(6)计算：

 $$ R_{i}\uparrow=\sqrt{\frac{\sum_{j=2}^{n}(P_{ij}\uparrow-\overline{P}_{i})^{2}}{m-1}}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{ij} $ ↑——平台第i个测量位置的第j次正向测量值；

 $ \overline{P}_{i} $  ——平台第 i 个测量位置的双向平均测量值；

m ——测量次数  $ n-1, m \geqslant 5 $ 。

d) 第 i 个测量位置的反向重复定位精度  $ R_{i} \downarrow $ ，按式(7)计算：

 $$ R_{i}\downarrow=\sqrt{\frac{\sum_{j=2}^{n}(P_{ij}\downarrow-\overline{P}_{i})^{2}}{m-1}}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{ij}\downarrow $  ——平台第 i 个测量位置的第 j 次反向测量值；

 $ \overline{P}_{i} $  ——平台第 i 个测量位置的双向平均测量值；

m ——测量次数  $ n-1, m \geqslant 5 $ 。

取  $  R = \max(R_{i} \uparrow, R_{i} \downarrow)  $  为平台被测轴的双向重复定位精度。

### 6.5 迟滞误差

#### 6.5.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行迟滞误差测量：

a）按图2所示，在全行程平均分布11个测量位置，分别为 $ p_{i}(i=1,2,\cdots,11) $ ，其中 $ p_{1} $ 为行程反向极限位置， $ p_{11} $ 为行程正向极限位置；

b）将平台移动至第1个测量位置，干涉仪测量读数清零；

c) 将平台从  $ p_{1} $  开始依次正向定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，再从  $ p_{11} $  开始依次反向定位到  $ p_{10}, p_{9}, \cdots, p_{1} $ ，在每个位置稳定后记录该位置的干涉仪测量值；

d）重复步骤 b) 和步骤 c) 不应少于 5 次。

#### 6.5.2 计算

迟滞误差计算过程如下：

a）按式(8)计算第i个测量位置的反向差值 $ B_{i} $ ：

 $$ B_{i}=\overline{P}_{i}\uparrow-\overline{P}_{i}\downarrow\quad(i=1,2,\cdots,11) $$ 

式中：

 $ \overline{P}_{i} $  ——平台第 i 个测量位置的正向平均测量值；

 $ \overline{P}_{i}\downarrow $  ——平台第 i 个测量位置的反向平均测量值。

b）取测量位置反向差值绝对值的最大值  $ \max(|B_{i}|) $  为平台的轴向反向差值 B，即： $ B=\max(|B_{i}|) $ 。

c) 迟滞误差  $ \delta_{H} $ ，按式(9)计算：

 $$ \delta_{\mathrm{H}}=B/T\times100\% $$ 

式中：

T ——平台轴向行程；

B ——轴向反向差值。

### 6.6 线性度

#### 6.6.1 测量步骤

线性度测量步骤同6.2.1。

#### 6.6.2 计算

线性度计算过程如下：

a）按式(3)确定第i个测量位置的正向平均测量值 $ \overline{P}_{i} $ 

b) 按图3所示，以指令 $ p_{i} $ 为横坐标， $ \overline{P}_{i}\uparrow $ 为纵坐标建立直角坐标系，对 $ \overline{P}_{i}\uparrow(i=1,2,\cdots,11) $ 进行最小二乘线性拟合，计算出 $ \overline{P}_{i}\uparrow $ 与其对应的拟合点 $ \overline{P}_{i}^{\prime}\uparrow $ 之间最大偏差值的绝对值 $ \Delta P_{\max} $ ；

c) 线性度  $ \delta_{L} $ ，按式(10)计算：

 $$ \delta_{\mathrm{L}}=\Delta P_{\max}/T\times100\% $$ 

式中：

T ——平台轴向行程；

 $ \Delta P_{max} $  ——最大偏差值的绝对值。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_309_818_869_1321.jpg" alt="Image" width="47%" /></div>


注1：·——第i个测量位置的平均测量值 $ \overline{P}_{i} $ ↑。

注 2： $ \circ $ ——与  $ \overline{P}_{i} $  ↑ 对应的最小二乘拟合点  $ \overline{P}_{i}^{\prime} $  ↑。

<div style="text-align: center;">图 3  $ \Delta P_{max} $  求解示意图</div>


### 6.7 位移分辨力

#### 6.7.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行位移分辨力测量：

a）按图 4 所示，将全行程十等分，依据平台的有效带宽设置合适的采样频率，使得采集的数据信息覆盖平台的有效带宽；

b）将平台移动至反向极限位置，干涉仪测量读数清零；

c）将平台按照图4所示的台阶波运动，每个台阶待系统稳定后记录干涉仪测量值。

注 $ ^{1} $ ：采样频率的设置要高于平台系统工作频带宽度的2倍。

注2：系统稳定时间取系统阶跃响应稳定时间的2倍。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_234_543_941_989.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 4 行程为  $ 100 \mu m $  的平台位移分辨力测量示意图</div>


#### 6.7.2 计算

位移分辨力计算过程如下：

a）将每个台阶波测量数据平均分成3段，分别计算3段数据的标准偏差值，取3段数据标准偏差值的平均值作为相应台阶的位移分辨力 $ \varepsilon_{i}(i=1,2,\cdots,10) $ ;

b) 取  $ \varepsilon=\max(\varepsilon_{i}) $  为平台的轴向位移分辨力。

### 6.8 角摆偏差

#### 6.8.1 测量步骤

##### 6.8.1.1 干涉仪法

将干涉仪严格对准平台，按照以下步骤进行角摆偏差测量：

a）按图1所示，在全行程平均分布11个测量位置，分别为 $ p_{i}(i=1,2,\cdots,11) $ ，其中 $ p_{1} $ 为行程反向极限位置， $ p_{11} $ 为行程正向极限位置；

b）将平台移动至第1个测量位置 $ p_{1} $ ，干涉仪测量读数清零；

c) 将平台从  $ p_{1} $  开始依次定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，在每个位置稳定后记录该位置偏摆角  $ \delta\phi_{i} $ ，俯仰角  $ \delta\theta_{i} $  和滚转角  $ \delta\gamma_{i} $  的干涉仪测量值；

d）重复步骤b)和步骤c)不应少于5次；

e） 此方法为仲裁方法。

##### 6.8.1.2 自准直仪法

将自准仪严格对准平台，按照以下步骤进行角摆偏差测量：

a）按图1所示，在全行程平均分布11个测量位置，分别为 $ p_{i}(i=1,2,\cdots,11) $ ，其中 $ p_{1} $ 为行程反向极限位置， $ p_{11} $ 为行程正向极限位置；

b) 偏摆角  $ \delta\phi_{i} $  和俯仰角  $ \delta\theta_{i} $  的测量设置如图 5 所示，将平台移动至第 1 个测量位置  $ p_{1} $ ，自准直仪测量读数清零；

c) 将平台从  $ p_{1} $  开始依次定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，在每个位置稳定后记录该位置偏摆角  $ \delta\phi_{i} $  和俯仰角  $ \delta\theta_{i} $  的自准直仪测量值；

d）重复步骤b)和步骤c)不应少于5次；

e) 滚转角  $ \delta\gamma_{i} $  的测量设置如图 6 所示，将平台移动至第 1 个测量位置  $ p_{1} $ ，自准直仪测量读数清零；

f) 将平台从  $ p_{1} $  开始依次定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，在每个位置稳定后记录该位置滚转角  $ \delta\gamma_{i} $  的自准直仪测量值；

g）重复步骤 e) 和步骤 f) 不应少于 5 次。

<div style="text-align: center;"><img src="imgs/img_in_image_box_364_802_840_975.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">图 5 自准直仪测量偏摆角  $ \delta\phi_{i} $  和俯仰角  $ \delta\theta_{i} $  示意图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_357_1043_848_1229.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 6 自准直仪测量滚转角  $ \delta\gamma_{i} $  示意图</div>


#### 6.8.2 计算

角摆偏差计算过程如下：

a）分别按式(11)、式(12)、式(13)确定第i个测量位置的角摆偏差平均值 $ \delta\overline{\phi}_{i},\delta\overline{\theta}_{i},\delta\overline{\gamma}_{i} $ 

 $$ \delta\overline{{\phi}}_{i}=\frac{\sum_{j=1}^{n}\delta\phi_{ij}}{n}\quad(i=1,2,\cdots,11) $$ 

 $$ \delta\overline{\theta}_{i}=\frac{\sum\limits_{j=1}^{n}\delta\theta_{ij}}{n}\quad(i=1,2,\cdots,11) $$ 

 $$ \delta\overline{\gamma}_{i}=\frac{\sum_{j=1}^{n}\delta\gamma_{ij}}{n}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ \delta\phi_{ij} $  ——平台第 i 个测量位置的第 j 次偏摆角测量值；

 $ \delta\theta_{ij} $  ——平台第 i 个测量位置的第 j 次俯仰角测量值；

 $ \delta\gamma_{ij} $  ——平台第 i 个测量位置的第 j 次滚转角测量值；

n ——测量次数, $ n \geqslant 5 $ 。

b) 取  $ \delta\phi=\max(\delta\phi_{i}) $  为平台运动轴向的偏摆角。

取  $ \delta\theta=\max(\delta\overline{\theta}_{i}) $  为平台运动轴向的俯仰角。

取  $ \delta\gamma=\max(\delta\overline{\gamma}_{i}) $  为平台运动轴向的滚转角。

### 6.9 直线度

#### 6.9.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行直线度测量：

a）以 X 轴作为被测轴为例，建立空间直角坐标系 XYZ；在全行程平均分布 11 个测量位置，分别为  $ p_{i}(i=1,2,\cdots,11) $ ，其中  $ p_{1} $  为行程反向极限位置， $ p_{11} $  为行程正向极限位置；

b）将平台移动至第1个测量位置 $ p_{1} $ ，Y轴干涉仪和Z轴干涉仪测量读数清零；

c）将平台从  $ p_{1} $  开始依次定位到  $ p_{2}, p_{3}, \cdots, p_{11} $ ，在每个位置稳定后记录该位置的干涉仪测量值；

d）记录Y轴干涉仪第i个测量位置的值为 $ P_{yi}(i=1,2,\cdots,11) $ ; Z轴干涉仪第i个测量位置的值为 $ P_{zi}(i=1,2,\cdots,11) $ ;

e）重复步骤b)～步骤d)不应少于5次。

#### 6.9.2 计算

直线度计算过程如下：

a）按式(14)确定 Y 方向第 i 个测量位置的单向平均测量值  $ \overline{P}_{yi} $ 

 $$ \overline{P}_{_{yi}}\uparrow=\frac{\sum_{j=1}^{n}P_{_{yij}}}{n}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{yij} $  ——平台第 i 个测量位置的 Y 轴干涉仪第 j 次测量值；

n ——测量次数, $ n \geqslant 5 $ 。

b) 按式(15)确定 Z 方向第 i 个测量位置的单向平均测量值  $ \overline{P}_{zi} $  ↑:

 $$ \overline{P}_{zi}\uparrow=\frac{\sum\limits_{j=1}^{n}P_{zij}}{n}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ P_{zij} $  ——平台第 i 个测量位置的 Z 轴干涉仪第 j 次测量值；

n ——测量次数, $ n \geqslant 5 $ 。

c) 按式(16)确定第 i 个测量位置的测量矢量合成值  $ \overline{P}_{xi} $  ↑:

 $$ \overline{P}_{xi}\uparrow=\sqrt{\overline{P}_{yi}\uparrow^{2}+\overline{P}_{zi}\uparrow^{2}}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ \overline{P}_{yi} $ ↑——Y方向第i个测量位置的单向平均测量值；

 $ \overline{P}_{zi} $ ↑——Z方向第i个测量位置的单向平均测量值。

d) 按图7所示，对 $ \overline{P}_{xi}\uparrow(i=1,2,\cdots,11) $ 进行最小二乘拟合，得到最小二乘拟合直线 $ l_{LS} $ ，分别计算出 $ \overline{P}_{xi}\uparrow(i=1,2,\cdots,11) $ 到 $ l_{LS} $ 的垂直距离，取其中的最大值 $ \Delta P_{xi-\max} $ ，计算方法按照GB/T 11336—2004；

e) X 轴运动时的直线度误差  $ L_{x} $ ，按式(17)计算：

 $$ L_{x}=2\Delta P_{xi\max} $$ 

式中：

 $ \Delta P_{xi-\max} $  —— X 方向，第 i 个测量位置单向最大测量值。

注：Y 轴、Z 轴直线度误差测量方法参照 X 轴测量方法。

<div style="text-align: center;"><img src="imgs/img_in_image_box_286_680_840_950.jpg" alt="Image" width="46%" /></div>


注 $ ^{1} $ ：○——第i个测量位置的测量矢量合成值。

注 2： $ l_{1,s} $  ——最小二乘中线。

<div style="text-align: center;">图 7  $ \Delta P_{xi-max} $  求解示意图</div>


### 6.10 平面度

#### 6.10.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行平面度测量：

a）平台在 XY 平面内运动的平面度测量，按图 8 所示，建立空间直角坐标系 XYZ，被测平面为 X 轴和 Y 轴所建立的平面，在平面范围内，沿 X 轴和 Y 轴平均分布  $ 11 \times 11 $  个测量位置，记为  $ p(i,j) $ ；

b）将平台移动至第一个测量位置  $ p(1,1) $ ，Z 轴干涉仪测量读数清零；

c) 将平台从  $ p(1,1) $  开始按图 8 所示蛇形网格布点形式沿各条测量线逐点顺序定位，直至定位到  $ p(11,11) $ ，在每个位置稳定后记录该位置的 Z 轴干涉仪测量值  $ Z_{(i,j)} $ ；

d）重复步骤b)和步骤c)不应少于5次。

<div style="text-align: center;"><img src="imgs/img_in_image_box_406_228_766_576.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">图 8 11×11 个测量位置行程示意图</div>


#### 6.10.2 计算

平面度计算过程如下：

a）按式(18)确定第 $ p(i,j) $ 个测量位置的Z轴干涉仪平均测量值 $ \overline{Z}_{(i,j)} $ ：

 $$ \overline{Z}_{(i,j)}=\frac{\sum\limits_{k=1}^{n}Z_{(i,j)k}}{n}\quad(i=1,2,\cdots,11;j=1,2,\cdots,11)\cdots\cdots\cdots\cdots\cdots\cdots\cdots(18) $$ 

式中：

 $ Z_{(i,j)k} $  ——测量位置  $ p(i,j) $  的 Z 轴干涉仪第 k 次测量值；

n ——测量次数, $ n \geqslant 5 $ 。

b）在空间直角坐标系 XYZ 中，由  $ \overline{Z}_{(i,j)}\left(i=1,2,\cdots,11;j=1,2,\cdots,11\right) $  进行最小二乘平面拟合，计算出最小二乘平面上各点坐标值  $ \overline{Z}'_{(i,j)} $ 。

c) 分别计算出各测量点  $ p(i,j) $  的平均测量值  $ \overline{Z}_{(i,j)} $  相对于最小二乘平面上拟合点  $ \overline{Z}'_{(i,j)} $  的差值  $ \Delta Z_{(i,j)} $ 。

d）平面度误差 F，按式(19)计算：

 $$ F=\max(\Delta Z_{(i,j)})-\min(\Delta Z_{(i,j)}) $$ 

式中：

 $ \Delta Z_{(i,j)} $  ——各测量点的平均测量值相对于最小二乘平面上拟合点的差值。

注：其他平面内的平面度测量，其方法参照 XY 平面测量方法。

### 6.11 正交误差

#### 6.11.1 测量步骤

将干涉仪严格对准平台，按照以下步骤进行正交误差测量：

a）按图9a)所示，在Y轴全行程平均分布11个测量位置，分别为 $ p_{yi}(i=1,2,\cdots,11) $ ，其中 $ p_{y1} $ 为行程反向极限位置， $ p_{y11} $ 为行程正向极限位置；

b）将平台在 X 轴方向归零，沿 Y 轴移动至第 1 个测量位置  $ p_{y1} $ ，X 轴干涉仪测量读数清零。

c）将平台从  $ p_{y1} $  开始依次定位到  $ p_{y2}, p_{y3}, \cdots, p_{y11} $ ，在每个位置稳定后记录该位置的 X 轴干涉仪

测量值：

d) 按图 9 b) 所示，在 X 轴全行程平均分布 11 个测量位置，分别为  $ p_{xi}(i=1,2,\cdots,11) $ ，其中  $ p_{x1} $  为行程反向极限位置， $ p_{x11} $  为行程正向极限位置；

e）将平台在 Y 轴方向归零，沿 X 轴移动至第 1 个测量位置  $ p_{x1} $ ，Y 轴干涉仪测量读数清零；

f) 将平台从  $ p_{x1} $  开始依次定位到  $ p_{x2}, p_{x3}, \cdots, p_{x11} $ ，在每个位置稳定后记录该位置的 Y 轴干涉仪测量值；

g）重复步骤b)～步骤f)不应少于5次。

<div style="text-align: center;"><img src="imgs/img_in_image_box_376_426_826_476.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">a）Y 轴单向测量位置行程示意图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_376_523_828_574.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">b) X 轴单向测量位置行程示意图</div>


<div style="text-align: center;">图 9 Y 轴和 X 轴单向测量位置行程示意图</div>


#### 6.11.2 计算

正交误差计算过程如下：

a）按式(20)确定平台沿Y轴方向运动时，第i个测量位置的X轴干涉仪平均测量值 $ \overline{X}_{yi} $ 

 $$ \overline{X}_{yi}=\frac{\sum\limits_{j=1}^{n}X_{yij}}{n}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ X_{yij} $  —— Y 轴运动时第 i 个测量位置的 X 轴干涉仪第 j 次测量值；

n ——测量次数, $ n \geqslant 5 $ 。

b) 按式(21)确定平台沿 X 轴方向运动时，第 i 个测量位置的 Y 轴干涉仪平均测量值  $ \overline{Y}_{xi} $ 

 $$ \overline{Y}_{xi}=\frac{\sum\limits_{j=1}^{n}Y_{xij}}{n}\quad(i=1,2,\cdots,11) $$ 

式中：

 $ Y_{xij} $  —— X 轴运动时第 i 个测量位置的 Y 轴干涉仪第 j 次测量值；

n ——测量次数, $ n \geqslant 5 $ 。

c) 以 Y 轴方向上指令  $ p_{yi} $  为横坐标， $ \overline{X}_{yi} $  为纵坐标建立直角坐标系，由  $ \overline{X}_{yi}(i=1,2,\cdots,11) $  进行最小二乘拟合，计算出拟合直线的斜率  $ K_{Y'} $ ，确定与斜率相对应的拟合直线倾斜角，即实际运动轨迹  $ Y' $  轴与目标 Y 轴之间的偏差角  $ \varphi_{1} $ （如图 10 所示）。

d) 以 X 轴方向上指令  $ p_{xi} $  为横坐标， $ \overline{Y}_{xi} $  为纵坐标建立直角坐标系，由  $ \overline{Y}_{xi}(i=1,2,\cdots,11) $  进行最小二乘拟合，计算出拟合直线的斜率  $ K_{X'} $ ，确定与斜率相对应的拟合直线倾斜角，即实际运动轨迹  $ X' $  轴与目标 X 轴之间的偏差角  $ \varphi_{2} $ （如图 10 所示）。

e）正交性误差  $ \delta\phi_{orth} $ ，按式(22)计算：

 $$ \delta\phi_{\mathrm{o r t h}}=\varphi_{2}-\varphi_{1} $$ 

式中：

 $ \varphi_{2} $  ——实际运动轨迹  $ X^{\prime} $  轴与目标 X 轴之间的偏差角；

 $ \varphi_{1} $  ——实际运动轨迹  $ Y' $  轴与目标 Y 轴之间的偏差角。

<div style="text-align: center;"><img src="imgs/img_in_image_box_472_206_696_426.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">图 10 正交误差示意图</div>
