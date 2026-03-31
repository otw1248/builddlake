

# 中华人民共和国国家标准

GB/T 39787—2021

# Coordinate system of BeiDou navigation satellite system

# 北斗卫星导航系统坐标系

2021-03-09 发布

2021-10-01 实施

## 目次

前言 …… I  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语、定义和缩略语 …… 1  
  
3.1 术语和定义 …… 1  
  
3.2 缩略语 …… 2  
  
4 坐标系定义 …… 2  
  
4.1 原点、尺度和定向 …… 2  
  
4.2 参考椭球 …… 3  
  
4.2.1 一般规定 …… 3  
  
4.2.2 定义常数 …… 3  
  
4.2.3 特殊应用常数 …… 3  
  
4.2.4 其他常数 …… 4  
  
4.3 相关主要模型和参数 …… 4  
  
5 北斗坐标系实现要求 …… 4  
  
5.1 一般概念 …… 4  
  
5.2 北斗参考站要求 …… 4  
  
5.3 北斗观测数据要求 …… 4  
  
5.4 数据处理要求 …… 5  
  
6 北斗参考框架维持与更新要求 …… 5  
  
6.1 北斗参考框架维持要求 …… 5  
  
6.1.1 一般概念 …… 5  
  
6.1.2 维持要求 …… 5  
  
6.2 北斗参考框架更新要求 …… 5  
  
6.2.1 一般概念 …… 5  
  
6.2.2 更新要求 …… 5  
  
7 坐标转换 …… 6  
  
7.1 转换类型 …… 6  
  
7.2 转换模型及要求 …… 6  
  
7.3 公共点选取 …… 6  
  
附录 A（规范性） 导出几何常数公式 …… 8  
  
附录 B（规范性） 导出物理常数公式 …… 10

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别这些专利的责任。

本文件由中央军委装备发展部提出。

本文件由全国北斗卫星导航标准化技术委员会(SAC/TC 544)归口。

本文件起草单位：西安测绘研究所、北京卫星导航中心。

本文件主要起草人：魏子卿、吴富梅、刘利、焦文海、刘莹、曾安敏、徐君毅、方柳、明锋、郭睿、李晓杰、王维嘉。

# 北斗卫星导航系统坐标系

## 1 范围

本文件规定了北斗卫星导航系统坐标系的定义、实现、维持与更新的要求，以及北斗卫星导航系统坐标系与其他地心坐标系的转换方法。

本文件适用于北斗卫星导航系统的建设、运行和应用。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 39267—2020 北斗卫星导航术语

## 3 术语、定义和缩略语

### 3.1 术语和定义

GB/T 39267—2020 界定的以及下列术语和定义适用于本文件。

#### 3.1.1 

国际地球参考框架 international terrestrial reference frame; ITRF

用于实现国际地球参考系的，一组全球分布的空间大地测量观测站的坐标和速度。

#### 3.1.2 

## 参考椭球 reference ellipsoid

大小和形状由赤道长半轴和扁率定义，代表地球体并经定位定向的旋转椭球体。

#### 3.1.3 

## 地球重力场 earth's gravity field

地球位、重力、大地水准面（或似大地水准面）、垂线偏差等的集合。

#### 3.1.4 

## 2000 中国大地坐标系统 China geodetic coordinate system 2000; CGCS2000

中国建立的大地坐标系。其坐标系的原点位于地球质心，Z轴指向国际地球自转服务组织（IERS）定义的参考极（IRP）方向，X轴为IERS定义的参考子午面（IRM）与通过原点且同Z轴正交的赤道面的交线，Y轴满足右手法则。

[来源:GB/T 39267—2020,2.2.5]

#### 3.1.5 

## 北斗坐标系 BeiDou coordinate system; BDCS

北斗卫星导航系统坐标系 coordinate system of BeiDou navigation satellite system

北斗卫星导航系统(BDS)采用的大地坐标系。BDCS的定义符合国际地球自转服务(IERS)规范，与CGCS2000的定义一致。

[来源:GB/T 39267—2020,2.2.6,有修改]

#### 3.1.6 

## 北斗参考站 BDCS reference stations

用于实现北斗坐标系的一组跟踪北斗卫星的北斗地面观测站。

注：包括北斗卫星定轨观测的主控站、监测站和注入站。

#### 3.1.7 

## 北斗参考框架 BDCS reference frame

体现北斗坐标系的北斗参考站的坐标和速度。

注：北斗参考框架的表示方法为：BDCS(YYYY.DOY)，YYYY代表年份，DOY代表年积日。BDCS(YYYY.DOY)

表示该框架从 YYYY 年第 DOY 天 UTC 0 时启用。

### 3.2 缩略语

下列缩略语适用于本文件。

BDS:北斗卫星导航系统(BeiDou Navigation Satellite System)

BIH: 国际时间局 (Bereau International del'Heure)

GNSS: 全球卫星导航系统 (Global Navigation Satellite System)

GLONASS: 格洛纳斯卫星导航系统 (Global Navigation Satellite System)

GPS: 全球定位系统(Global Positioning System)

GTRF:伽利略大地参考框架(Galileo Terrestrial Reference Frame)

PZ-90: PZ-90 坐标系 (Parameters of the Earth 1990 System)

TCG: 地心坐标时 (Geocentric Coordinate Time)

WGS84:1984 世界大地坐标系(World Geodetic System 1984)

## 4 坐标系定义

### 4.1 原点、尺度和定向

BDCS 的定义与 CGCS2000 的定义一致。原点、尺度、坐标轴的定向及其时间演变定义符合以下 IERS 定义：

a） 原点：位于包括海洋和大气的整个地球的质量中心；

b）尺度：长度单位为米(m)。这一尺度同地心局部框架的TCG时间坐标一致；

c）定向：在1984.0时初始定向与BIH的定向一致；

d）定向时间演变：定向随时间的演变相对于整个地球的水平构造运动无整体旋转。

BDCS 为一右手直角坐标系。原点位于地球质量中心，Z 轴指向 IERS 参考极方向，X 轴为 IERS 参考子午面与通过原点且同 Z 轴正交的赤道面的交线，Y 轴完成右手直角坐标系，见图 1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_326_201_883_548.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 1 北斗坐标系参考椭球</div>


### 4.2 参考椭球

#### 4.2.1 一般规定

BDCS 参考椭球与 CGCS2000 参考椭球一致，其几何中心与 BDCS 的原点重合，旋转轴与 BDCS 的 Z 轴一致。BDCS 参考椭球也是表面为正常重力场的等位面的正常椭球，由四个常数  $ (a, \mu, f, \omega) $  定义，几何常数和物理常数导出公式及数值应符合附录 A 和附录 B。

#### 4.2.2 定义常数

BDCS 参考椭球的定义常数如下：

a）长半轴： $ a = 6\,378\,137.0\,m $ ;

b）包含大气的地心引力常数 GM（亦可用  $ \mu $  表示）： $ \mu=3\ 986\ 004.418\times10^{8}\ m^{3}/s^{2} $ 

c) 扁率:  $ f=1:298.257\ 222\ 101 $ ;

d）地球自转角速度： $ w=7\ 292\ 115.0\times10^{-11}\ rad/s $ 。

#### 4.2.3 特殊应用常数

北斗坐标系采用的特殊应用常数见表1。

<div style="text-align: center;">表 1 特殊应用常数的值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>应用常数名称</td><td style='text-align: center;'>值</td></tr><tr><td style='text-align: center;'>不包括大气的地球引力常数 GM′/(m³/s²)</td><td style='text-align: center;'>GM′=3 986 000.9×10⁸</td></tr><tr><td style='text-align: center;'>地球大气的引力常数 GM_{A}/(m³/s²)</td><td style='text-align: center;'>GM_{A}=3.5×10⁸</td></tr><tr><td style='text-align: center;'>在进动参考架中地球角速度 ω*/(rad/s)</td><td style='text-align: center;'>ω*=7 292 115.855 3×10⁻¹¹+4.3×10⁻¹⁵T_{U} 式中: T_{U}——自J2000.0的儒略世纪数,T_{U}=d_{U}/36 525; d_{U}——自JD2451545.0 UT1的世界时(UT)的天数,取值 ±0.5,±1.5,±2.5…,d_{U}=JD-2451545。</td></tr></table>

#### 4.2.4 其他常数

北斗坐标系采用的其他常数见表2。

<div style="text-align: center;">表 2 其他常数的值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>其他常数名称</td><td style='text-align: center;'>值</td></tr><tr><td style='text-align: center;'>大地水准面的位W0/(m²/s²)</td><td style='text-align: center;'>W0=62 636 856.0±0.5</td></tr><tr><td style='text-align: center;'>地球位尺度因子R0/m</td><td style='text-align: center;'>R0=GM/W0=6 363 672.6±0.1</td></tr><tr><td style='text-align: center;'>动力学扁率H</td><td style='text-align: center;'>H=1/305.441 3</td></tr><tr><td style='text-align: center;'>地球的主惯性矩A、B、C/(kg·m²)</td><td style='text-align: center;'>A=8.009 102 9×1037B=8.009 255 9×1037C=8.035 487 2×1037</td></tr></table>

### 4.3 相关主要模型和参数

北斗坐标系宜采用 IERS 推荐的相关模型和参数，见表 3。

<div style="text-align: center;">表 3 BDCS 推荐的模型和参数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>模型种类</td><td style='text-align: center;'>模型名称</td></tr><tr><td style='text-align: center;'>地球重力场模型</td><td style='text-align: center;'>EGM2008 模型</td></tr><tr><td style='text-align: center;'>地球定向参数</td><td style='text-align: center;'>IERS 地球定向参数</td></tr><tr><td style='text-align: center;'>岁差—章动模型</td><td style='text-align: center;'>IAU 2000/2006 模型</td></tr><tr><td style='text-align: center;'>固体潮</td><td style='text-align: center;'>IERS 模型</td></tr><tr><td style='text-align: center;'>海潮模型</td><td style='text-align: center;'>FES2004 模型</td></tr><tr><td style='text-align: center;'>行星历表</td><td style='text-align: center;'>DE421</td></tr></table>

## 5 北斗坐标系实现要求

### 5.1 一般概念

北斗坐标系的实现应采用专用的软件、算法和模型通过处理分布在全球的北斗参考站观测数据，获得北斗参考站高精度的坐标，实现过程应符合北斗参考站、观测数据和数据处理等要求。

### 5.2 北斗参考站要求

北斗参考站建设应遵守如下要求：

a）参考站的观测墩建在稳固的基岩上，避开因地基不稳定而产生沉降和位移的地区；对无法建在基岩上的站点，应进行地基处理，保证点位稳定；

b）参考站宜尽量全球均匀分布。

### 5.3 北斗观测数据要求

北斗参考站观测数据应符合如下要求：

a）采用 BDS/GNSS 接收机连续观测；

b）参考站观测视场内障碍物高度角不超过 $ 15^{\circ} $ ; 参考站远离大功率发射源, 远离高压线和微波无线电信号传送通道及电磁场较强的地区; 避开雷击区及多路径效应严重的环境;

c） 观测仪器应强制对中。

### 5.4 数据处理要求

北斗坐标系实现的数据处理应遵守如下要求：

a）采用两套独立软件进行数据处理并比对；

b）从 ITRF 参考站中选取若干全球均匀分布、稳定、可靠、具有较长观测时间的参考站作为基准站（基准站一经选取宜尽量保持不变）；

c) 收集数据：北斗参考站观测数据、ITRF站观测数据；

d）构建包含北斗参考站和ITRF站的全球网；

e）采用松约束解算全球网，获得松弛解；

f) 采用通用基准约束方法，对全球网施加约束，实现与最新的 ITRF 框架对准，获得北斗参考站坐标；

g）精度评估。

## 6 北斗参考框架维持与更新要求

### 6.1 北斗参考框架维持要求

#### 6.1.1 一般概念

北斗参考框架维持是指对构建的全球网数据进行处理，分析北斗参考站坐标时间序列，研究坐标变化规律，获得精确的北斗参考站速度，并对坐标进行修正。

#### 6.1.2 维持要求

北斗参考框架的维持应遵守如下要求：

a）采用两套独立软件进行数据处理并比对；

b）收集数据：参考站历年坐标时间序列、当前参考站观测数据、当前ITRF站观测数据；

c) 采用松约束解算当前构建的全球网，获得松弛解；

d）采用通用基准约束方法，对当前全球网施加约束，实现与当前采用的 ITRF 框架对准，获得北斗参考站坐标；

e）合并参考站所有坐标时间序列并进行分析和处理，获得参考站速度；

h）精度评估；

f）利用解算获得的速度，获得参考站在不同解算历元的坐标。

### 6.2 北斗参考框架更新要求

#### 6.2.1 一般概念

北斗参考框架更新是指通过对历年北斗参考站数据进行处理，获得对准于最新的 ITRF 框架的北斗参考站坐标及其速度。

#### 6.2.2 更新要求

北斗参考框架更新应遵守如下要求：

a）采用两套独立软件进行数据处理并比对。

b）常规更新：每年更新一次，采用更新之后的参考站坐标及速度代替之前版本的结果。

c) 特殊更新：当通过维持解算得到的参考站（一个或者几个）坐标与当前使用的坐标分量超过限值 3 cm，即进行更新。

d）当模型或参数发生较大变化时的框架更新：

1）收集数据：参考站所有观测数据、国际ITRF站所有观测数据；

2）采用松约束解算所有全球网，获得松弛解；

3）采用通用基准约束方法，对全球网施加约束，实现与最新的ITRF框架对准，获得北斗参考站坐标；

4）对北斗参考站坐标时间序列进行分析，获得坐标及速度；

5）精度评估。

e） 当模型或参数未发生较大变化时的框架更新：

1）收集数据：参考站历年坐标时间序列、当前参考站观测数据、当前ITRF基准站观测数据；

2）采用松约束解算当前构建的全球网，获得松弛解；

3）采用国际通用基准约束方法，对所有全球网施加约束，实现与最新的ITRF框架对准，获得北斗参考站坐标；

4）对北斗参考站坐标时间序列进行分析，去除各种误差影响，获得参考站坐标及速度；

5）精度评估。

## 7 坐标转换

### 7.1 转换类型

北斗坐标系的坐标转换主要包括 BDCS 与其他地心坐标系(CGCS2000、WGS84、GTRF、PZ-90 等)之间的转换。

### 7.2 转换模型及要求

从坐标系 1 变换到坐标系 2，采用七参数模型，见公式(1)。

 $$ \begin{bmatrix}X\\ Y\\ Z\end{bmatrix}_{2}=\begin{bmatrix}X\\ Y\\ Z\end{bmatrix}_{1}+\begin{bmatrix}\Delta X\\ \Delta Y\\ \Delta Z\end{bmatrix}+\begin{bmatrix}m&-\varepsilon_{z}&\varepsilon_{y}\\ \varepsilon_{z}&m&-\varepsilon_{x}\\ -\varepsilon_{y}&\varepsilon_{x}&m\end{bmatrix}\begin{bmatrix}X\\ Y\\ Z\end{bmatrix}_{1} $$ 

式中：

 $ \Delta X $  、 $ \Delta Y $  、 $ \Delta Z $  ——平移参数，单位为米(m)；

 $ \varepsilon_{X} $ 、 $ \varepsilon_{Y} $ 、 $ \varepsilon_{Z} $  ——旋转参数，单位为弧度(rad)；

m ——尺度变化参数,无量纲。

七参数模型的适用范围，取决于坐标精度的一致性或者网的均匀性。如果变换的两个坐标系中各自坐标精度有很好的一致性，则全国范围可以用一组变换参数。否则，变换可按地区进行，不同地区用不同的转换参数。

### 7.3 公共点选取

公共点选取应满足如下要求：

a）优先选用具有两种坐标系下的高精度的地面点坐标作为公共点；

b）其次选用具有两种坐标系下的高精度卫星位置作为公共点；

c) 也可采用具有两种坐标系下的高精度精密星历解算的地面点作为公共点；

d）或可采用具有两种坐标系下的广播星历解算的地面点作为公共点。

## 附录 A

## (规范性)

## 导出几何常数公式

导出几何常数公式包括：

a) 子午椭圆第一偏心率: BDCS 参考椭球子午椭圆第一偏心率根据公式(A.1)采用迭代方式计算:

 $$ e^{2}=3J_{_{2}}+\frac{4}{15}\frac{\omega^{2}a^{3}}{GM}\frac{e^{3}}{2q_{0}} $$ 

式中：

 $ J_{2} $ ——地球重力场的2阶带谐系数

 $$ \begin{aligned}2q_{_{0}}=&\left(1+\frac{3}{e^{^{\prime}2}}\right)\tan^{-1}e^{^{\prime}}-\frac{3}{e^{^{\prime}}}\\&e^{^{\prime}}=e\left(1-e^{^{2}}\right)^{-1/2}\end{aligned} $$ 

b) 几何扁率: BDCS 参考椭球几何扁率根据公式 (A.2) 计算:

 $ f=1-(1-e^{2})^{1/2} $  或  $ f=(a-b)/a $  ……(A.2)

c）短半轴：BDCS参考椭球短半轴根据公式(A.3)计算：

 $$ b=a\left(1-e^{2}\right)^{1/2} $$ 

d) 线偏心率: BDC 参考椭球线偏心率根据公式 (A.4) 计算:

 $$ E=ae\quad 或 \quad E=(a^{2}-b^{2})^{1/2} $$ 

e）极曲率半径：BDCS参考椭球极曲率半径根据公式(A.5)计算：

 $$ c=a\left(1-e^{2}\right)^{-1/2}\quad 或 \quad c=a^{2}/b $$ 

f) 从赤道到极的子午圈弧长: BDCS 参考椭球从赤道到极的子午圈弧长根据如下公式 (A.6) 计算:

 $$ \begin{aligned}Q=&a\left(1-e^{2}\right)\int_{0}^{\pi/2}\frac{\mathrm{d}B}{\left(1-e^{2}\sin^{2}B\right)^{3/2}}\\=&a\left(1-e^{2}\right)\left(1+\frac{3}{4}e^{2}+\frac{45}{64}e^{4}+\frac{175}{256}e^{6}+\frac{11\ 025}{16\ 384}e^{8}+\frac{43\ 659}{65\ 536}e^{10}\right)\frac{\pi}{2}\end{aligned} $$ 

式中：

B——大地纬度。

g）椭球体积：BDCS参考椭球体积根据公式(A.7)计算：

 $$ V=\frac{4}{3}\pi a^{3}(1-e^{2})^{1/2}\quad 或 \quad V=\frac{4}{3}\pi a^{2}b $$ 

h) 椭球表面积: BDCS 参考椭球表面积根据公式 (A.8) 计算:

 $$ S=2\;\pi a^{2}\Big(1+\frac{1-e^{2}}{2e}\ln\frac{1+e}{1-e}\Big) $$ 

i) 算术平均半径: BDCS 参考椭球算术平均半径根据公式 (A.9) 计算:

 $$ \begin{aligned}R_{1}&=\left(a+a+b\right)/3\\&=a\left(1-f/3\right)\\&=a\left[2+\left(1-e^{2}\right)^{1/2}\right]/3\end{aligned} $$ 

i) 同面积之球半径：BDCS 参考椭球同面积之球半径根据公式 (A.10) 计算：

 $$ R_{2}=a\left(\frac{1}{2}+\frac{1-e^{2}}{4e}\ln\frac{1+e}{1-e}\right)^{1/2} $$ 

k）同体积之球半径：BDCS参考椭球同体积之球半径根据公式(A.11)计算：

 $$ R_{3}=a\left(1-e^{2}\right)^{1/6}\quad 或 \quad R_{3}=\left(a^{2}b\right)^{1/3} $$ 

根据上述公式和常数得到的 BDCS 参考椭球几何常数数值见表 A.1。

<div style="text-align: center;">表 A.1 北斗坐标系参考椭球的导出几何常数值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>常数名</td><td style='text-align: center;'>值</td><td style='text-align: center;'>常数名</td><td style='text-align: center;'>值</td></tr><tr><td style='text-align: center;'>短半轴b/m</td><td style='text-align: center;'>6 356 752.314 1</td><td style='text-align: center;'>扁率倒数1/f</td><td style='text-align: center;'>298.257 222 101</td></tr><tr><td style='text-align: center;'>线偏心率E/m</td><td style='text-align: center;'>521 854.009 7</td><td style='text-align: center;'>轴比b/a</td><td style='text-align: center;'>0.996 647 189 319</td></tr><tr><td style='text-align: center;'>极曲率半径c/m</td><td style='text-align: center;'>6 399 593.625 9</td><td style='text-align: center;'>子午圈一象限弧长Q/m</td><td style='text-align: center;'>10 001 965.7293</td></tr><tr><td style='text-align: center;'>第一偏心率e</td><td style='text-align: center;'>0.081 819 191 042 782</td><td style='text-align: center;'>椭球体积V/km³</td><td style='text-align: center;'>1 083 207 319 783.546</td></tr><tr><td style='text-align: center;'>第一偏心率平方e²</td><td style='text-align: center;'>0.006 694 380 022 90</td><td style='text-align: center;'>椭球表面积S/km²</td><td style='text-align: center;'>510 065 621.718</td></tr><tr><td style='text-align: center;'>第二偏心率e&#x27;</td><td style='text-align: center;'>0.082 094 438 151 912</td><td style='text-align: center;'>算术平均半径R₁/m</td><td style='text-align: center;'>6 371 008.771 4</td></tr><tr><td style='text-align: center;'>第二偏心率平方e&#x27;²</td><td style='text-align: center;'>0.006 739 496 775 48</td><td style='text-align: center;'>同面积之球的半径R₂/m</td><td style='text-align: center;'>6 371 007.180 9</td></tr><tr><td style='text-align: center;'>扁率f</td><td style='text-align: center;'>0.003 352 810 681 18</td><td style='text-align: center;'>同体积之球的半径R₃/m</td><td style='text-align: center;'>6 371 000.790 0</td></tr></table>

## 附录 B

## (规范性)

## 导出物理常数公式

导出物理常数公式包括：

a）参考椭球的正常位：BDCS参考椭球的正常位根据公式(B.1)计算：

 $$ U_{_{0}}=\frac{GM}{E}\tan^{-1}e^{\prime}+\frac{1}{3}\omega^{2}a^{2} $$ 

b）正常引力位(重力位 U 减去离心力位): BDCS 参考椭球正常引力位根据公式(B.2)计算：

 $$ V{=}\frac{\mathrm{G M}}{r}\Big(1{-}\sum_{n=1}^{\infty}J_{2n}\Big(\frac{a}{r}\Big)^{2n}P_{2n}\left(\cos\theta\right)\Big) $$ 

式中：

r ——向径,单位为米(m);

θ ——极距，单位为弧度(rad)；

 $ P_{2n} $ ——2n阶勒让德函数，用下式(B.3)递推：

 $$ P_{_{2n}}\left(\cos\theta\right)=\frac{1}{2^{2n}\left(2n\right)!}\frac{d^{2n}\left(\left(\cos\theta\right)^{2}-1\right)^{2n}}{d\left(\cos\theta\right)^{2n}} $$ 

 $ J_{2} $ ——地球重力场的2阶带谐系数，定义常数。2阶以上偶阶带谐系数用下式(B.4)递推：

 $$ J_{_{2n}}=\left(-1\right)^{n+1}\frac{3e^{2n}}{\left(2n+1\right)\left(2n+3\right)}\Big(1-n+5n\frac{J_{_{2}}}{e^{2}}\Big) $$ 

……(B.4)

c) 赤道正常重力和极正常重力: BDCS 参考椭球赤道正常重力  $ \gamma_{e} $  和极正常重力  $ \gamma_{p} $  根据公式(B.5)计算:

 $$ \begin{aligned}&\gamma_{\mathrm{e}}{=}\frac{\mathrm{G M}}{a b}\Big(1-m-\frac{m}{6}\frac{e^{\prime}q^{\prime}{}_{0}}{q_{0}}\Big)\\ &\gamma_{\mathrm{p}}{=}\frac{\mathrm{G M}}{a^{2}}\Big(1+\frac{m}{3}\frac{e^{\prime}q^{\prime}{}_{0}}{q_{0}}\Big)\\ \end{aligned} $$ 

式中：

 $$ \begin{aligned}q_{_{0}}^{\prime}=3\Big(1+\frac{1}{e^{\prime}^{2}}\Big)\Big(1-\frac{1}{e^{\prime}}\operatorname{tg}^{-1}e^{\prime}\Big)-1\\m=\frac{\omega^{2}a^{2}b}{GM}\end{aligned} $$ 

d）重力扁率：BDCS参考椭球重力扁率根据公式(B.6)计算：

 $$ f^{*}=\frac{\gamma_{\mathrm{p}}-\gamma_{\mathrm{e}}}{\gamma_{\mathrm{e}}} $$ 

e) 几何扁率和重力扁率满足的关系: BDCS 参考椭球几何扁率和重力扁率满足以下关系 (克莱劳定理), 见公式 (B.7):

 $$ f+f^{*}=\frac{\omega^{2}b}{\gamma_{\mathrm{e}}}\Big(1+\frac{e^{^{\prime}}q^{^{\prime}}{}_{0}}{2q_{0}}\Big) $$ 

f) 椭球面重力的平均值: BDCS 参考椭球面重力的平均值, 见公式(B.8) 和公式(B.9):

 $$ \begin{aligned}\overline{\gamma}=&\int_{0}^{\pi/2}\frac{\gamma\cos B\mathrm{d}B}{\left(1-e^{2}\sin^{2}B\right)^{2}}\div\int_{0}^{\pi/2}\frac{\cos B\mathrm{d}B}{\left(1-e^{2}\sin^{2}B\right)^{2}}\\=&\gamma_{\mathrm{e}}\Big(2+\frac{2}{3}k-\frac{4}{3}e^{2}\Big)\div\left[\sqrt{1-e^{2}}\Big(1+\frac{1-e^{2}}{2e}\ln\frac{1+e}{1-e}\Big)\right]\end{aligned} $$ 

式中：

 $$ k=\frac{b\gamma_{\mathrm{p}}}{a\gamma_{\mathrm{e}}}-1 $$ 

g）地球质量：BDCS参考椭球地球质量，见公式(B.10)：

 $$ M=GM/G $$ 

式中：

G——牛顿引力常数， $ G=6.672\ 59\times10^{-11}\ m^{3}/kg/s^{2} $ 

h）椭球对其短轴的转动惯量：BDCS参考椭球对其短轴的转动惯量，见公式(B.11)：

 $$ J_{\mathrm{~b~}}=\frac{2}{5}M a^{2} $$ 

……(B.11)

i) 椭球对其长轴的转动惯量：BDCS 参考椭球对其长轴的转动惯量，见公式(B.12)：

 $$ J_{\mathrm{a}}=\frac{1}{5}Ma^{2}\left(2-e^{2}\right) $$ 

根据上面公式和常数可得到 BDCS 参考椭球的物理常数数值，见表 B.1。

<div style="text-align: center;">表 B.1 北斗坐标系参考椭球的物理常数值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>常数名</td><td style='text-align: center;'>值</td><td style='text-align: center;'>常数名</td><td style='text-align: center;'>值</td></tr><tr><td style='text-align: center;'>椭球面正常位U0/(m²/s²)</td><td style='text-align: center;'>62 636 851.714 9</td><td style='text-align: center;'>极正常重力γp/(m/s²)</td><td style='text-align: center;'>9.832 184 940 2</td></tr><tr><td style='text-align: center;'>4阶带谐系数J4</td><td style='text-align: center;'>-0.237 091 125 614 0×10-5</td><td style='text-align: center;'>平均正常重力γ/(m/s²)</td><td style='text-align: center;'>9.797 643 222 4</td></tr><tr><td style='text-align: center;'>6阶带谐系数J6</td><td style='text-align: center;'>0.608 346 525 888 8×10-8</td><td style='text-align: center;'>重力扁率f*</td><td style='text-align: center;'>0.005 302 441 741 37</td></tr><tr><td style='text-align: center;'>8阶带谐系数J8</td><td style='text-align: center;'>-0.142 681 100 979 6×10-10</td><td style='text-align: center;'>k=bγp/aγc-1</td><td style='text-align: center;'>0.001 931 852 970 52</td></tr><tr><td style='text-align: center;'>10阶带谐系数J10</td><td style='text-align: center;'>0.121 439 338 333 7×10-13</td><td style='text-align: center;'>地球质量(包括大气)M/kg</td><td style='text-align: center;'>5.973 331 96×1024</td></tr><tr><td style='text-align: center;'>m=ω²a²b/GM</td><td style='text-align: center;'>0.003 449 786 506 76</td><td style='text-align: center;'>椭球对短轴的转动惯量Jb/(kg·m²)</td><td style='text-align: center;'>9.719 956 68×1037</td></tr><tr><td style='text-align: center;'>赤道正常重力γc/(m/s²)</td><td style='text-align: center;'>9.780 325 334 9</td><td style='text-align: center;'>椭球对长轴的转动惯量Ja/(kg·m²)</td><td style='text-align: center;'>9.687 422 13×1037</td></tr></table>