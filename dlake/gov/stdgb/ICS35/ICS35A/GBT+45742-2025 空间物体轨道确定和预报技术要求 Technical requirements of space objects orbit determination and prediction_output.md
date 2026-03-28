

# 中华人民共和国国家标准

GB/T 45742—2025

# 空间物体轨道确定和预报技术要求

# Technical requirements of space objects orbit determination and prediction

2025-05-30 发布

2025-09-01 实施

Powered by TCPDF (www.tcpdf.org)

## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 轨道动力学模型要求 …… 2  
  
4.1 概述 …… 2  
  
4.2 轨道动力学模型的时间和坐标系统要求 …… 2  
  
4.3 轨道动力学模型 …… 2  
  
4.4 轨道动力学模型设置要求 …… 3  
  
5 轨道预报技术要求 …… 3  
  
5.1 概述 …… 3  
  
5.2 输入数据要求 …… 4  
  
5.3 轨道预报技术流程 …… 4  
  
6 轨道确定技术要求 …… 6  
  
6.1 概述 …… 6  
  
6.2 输入数据要求 …… 6  
  
6.3 初轨确定技术要求 …… 7  
  
6.4 批处理精密定轨技术要求 …… 7  
  
6.5 序贯处理精密定轨技术要求 …… 9  
  
6.6 输出数据要求 …… 11  
  
附录 A（资料性） 一种轨道动力学模型的摄动加速度计算方法 …… 12  
  
A.1 地球非球形引力摄动 …… 12  
  
A.2 地球潮汐形变摄动 …… 12  
  
A.3 第三体引力摄动 …… 13  
  
A.4 后牛顿效应摄动 …… 13  
  
A.5 大气阻力摄动 …… 14  
  
A.6 太阳光压摄动 …… 14  
  
附录 B（资料性） 不同类型轨道和轨道预报精度要求下的摄动加速度模型设置 …… 15  
  
附录 C（资料性） 基于线性化理论的轨道运动参数修正和协方差预报方法 …… 18  
  
C.1 基于最小二乘估计的轨道运动参数修正值计算方法 …… 18  
  
C.2 状态转移矩阵计算方法 …… 18  
  
C.3 轨道运动参数协方差矩阵的线性预报方法 …… 19  
  
参考文献 …… 20



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国宇航技术及其应用标准化技术委员会(SAC/TC 425)提出并归口。

本文件起草单位：中国科学院国家天文台、南京大学、西安卫星测控中心、北京航天飞行控制中心、中国航天标准化研究所。

本文件主要起草人：刘静、程昊文、汤靖师、王彦荣、曹建峰、郑峰椿、李大卫、杨旭、张耀、甘庆波、李杨、江海、泉浩芳、赵南英。



# 空间物体轨道确定和预报技术要求

## 1 范围

本文件规定了绕地球运动空间物体轨道确定和预报中的主要力模型、输入输出和技术流程。

本文件适用于在自然力作用下绕地球运动空间物体测量、编目和预警中涉及的空间物体轨道数据生成、轨道运动状态预测及其应用。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 45621 航天术语 空间碎片

## 3 术语和定义

GB/T 45621 界定的以及下列术语和定义适用于本文件。

### 3.1 

#### J2000.0 参考系 J2000.0 reference system

以地球质心为原点，历元 J2000.0 平赤道为 XY 平面，历元 J2000.0 平春分点为 X 轴指向的右手参考系。

注：历元 J2000.0 是指地球时(Terrestrial Time)2000 年 1 月 1 日 12 时 0 分 0 秒。

### 3.2 

## 地心天球参考系 geocentric celestial reference system

以地球质心为原点，由2000年国际天文学联合会(IAU)决议B1.3定义的右手参考系。

注：GCRS坐标轴指向与J2000.0参考系靠近，相差约为0.02。

### 3.3 

## 轨道运动参数 orbital motion parameters

空间物体轨道运动状态参数，用空间物体位置和速度矢量或可等价转换为位置和速度矢量的参数表示；在轨道确定中轨道运动参数也可包含轨道动力学模型参数。

注：轨道动力学模型参数包括大气阻力系数、太阳光压系数等。

### 3.4 

## 轨道测量数据 orbital measurement data

直接或间接反映空间物体轨道运动状态的测量数据。

注：轨道测量数据包括测角、测距、测速、三维位置等。

### 3.5 

## 测量方程 measurement equations

表示空间物体轨道测量数据值与轨道运动参数之间关系的方程组。

### 3.6 

## 测量矩阵 measurement matrix

基于测量方程得到的空间物体轨道测量数据值对轨道运动参数的偏导数矩阵。

### 3.7 

动力学方程 dynamical equations

空间物体轨道运动参数随时间变化的微分方程组。

### 3.8 

## 轨道确定 orbit determination

基于动力学方程，利用空间物体轨道测量数据确定在某一时刻空间物体轨道运动参数的过程。

注 $ ^{1} $ ：轨道确定分为初轨确定和精密定轨两类。

注2：轨道确定理论上也能够确定测量模型参数，但并不在本文件的范围内。

### 3.9 

## 轨道预报 orbit prediction

利用某时刻轨道运动参数，基于动力学方程，计算过去或未来某时刻轨道运动参数的过程。

## 4 轨道动力学模型要求

### 4.1 概述

轨道动力学模型是指在一个或多个力作用下，空间物体轨道运动所符合的模型，以轨道运动参数满足的动力学方程表示。轨道动力学模型是空间物体轨道确定和预报的基础。

### 4.2 轨道动力学模型的时间和坐标系统要求

轨道动力学模型的时间系统应采用地球时。

轨道动力学模型的坐标系统，在空间物体轨道动力学模型精度需求优于10 m时应采用地心天球参考系，否则可选择J2000.0参考系或地心天球参考系。

### 4.3 轨道动力学模型

#### 4.3.1 动力学方程

轨道动力学模型满足的动力学方程表示为式(1):

 $$ \ddot{\vec{r}}=-\mu\frac{\vec{r}}{r^{3}}+\vec{F}_{\varepsilon}(\vec{r},\dot{\vec{r}},t) $$ 

式中：

 $ \vec{r} $  ——空间物体位置矢量；

 $ \dot{\vec{r}} $  ——空间物体速度矢量；

 $ \dot{\vec{r}} $  ——空间物体加速度矢量；

r ——空间物体地心距离；

 $$ \frac{\mu}{\rightarrow}F. $$ 

 $ \mu $  ——地球引力常数；

 $ \overrightarrow{F}_{\varepsilon} $  ——各摄动加速度矢量的和；

t ——时间。





#### 4.3.2 地球质点引力加速度

将地球简化为同等质量的质点所产生的引力加速度,采用式(1)中的 $ -\mu\frac{\vec{r}}{r^{3}} $ 计算。

#### 4.3.3 摄动加速度

摄动加速度模型包括地球非球形引力摄动、地球潮汐形变摄动、第三体引力摄动、后牛顿效应、大气阻力摄动和太阳光压摄动。

a) 地球非球形引力摄动：不考虑除地球以外天体引力作用，地球实际质量分布产生的引力加速度与等质量质点引力加速度之差。地球非球形引力摄动加速度表示为球谐函数级数形式，各级球谐系数由地球引力场模型给出，级数的截止阶次越高，地球非球形引力摄动加速度的计算精度越高。附录 A 中的 A.1 提供了一种计算地球非球形引力摄动加速度的方法。

b) 地球潮汐形变摄动：地球受外部天体引力作用产生形变，并因此对空间物体产生的摄动加速度。地球潮汐形变摄动是因地球形变引起的加速度，表示为对地球引力场模型的修正。修正的引力场模型阶次越高，地球潮汐形变摄动加速度的计算精度越高。A.2 提供了一种计算地球潮汐形变摄动加速度的方法。

c) 第三体引力摄动：除地球以外的天体对空间物体的引力效应所产生的加速度之和。在本文件适用范围内，只涉及太阳和月球对空间物体产生的引力加速度计算，对太阳和月球位置计算精度越高，第三体引力摄动加速度的计算精度越高。A.3 提供了一种计算第三体引力摄动加速度的方法。

d）后牛顿效应：现代引力理论相对于牛顿力学的修正效应所产生的加速度。A.4 提供了一种计算后牛顿效应加速度的方法。

e) 大气阻力摄动：空间物体相对于大气分子高速运动受到的阻力效应产生的加速度。大气阻力摄动加速度与地球大气密度有关，也与空间物体等效大气阻力截面积与其质量之比有关。A.5 提供了一种计算大气阻力摄动加速度的方法。

f) 太阳光压摄动：太阳辐射的光子作用于空间物体表面发生动量交换所产生的加速度。当空间物体被太阳照射时，太阳光压摄动加速度与空间物体表面反照率有关，也与空间物体等效太阳光压截面积与其质量之比有关；当空间物体在地球阴影中时，太阳光压摄动加速度为零。A.6 提供了一种计算太阳光压摄动加速度的方法。

### 4.4 轨道动力学模型设置要求

#### 4.4.1 轨道动力学模型一致性要求

空间物体轨道预报设置的轨道动力学模型应与生成轨道运动参数初始值的轨道确定中所采用的轨道动力学模型一致。

#### 4.4.2 摄动加速度模型设置要求

对不同类型的轨道，在不同摄动加速度模型设置下，能够实现的轨道动力学模型精度有所不同。附录 B 给出了不同类型轨道和轨道预报精度要求下的摄动加速度模型设置。

## 5 轨道预报技术要求

### 5.1 概述

空间物体轨道预报是求解动力学方程式(1)的过程,根据预报起始时刻 $ t_{start} $ 的轨道运动参数初值,计算得到预报结束时刻 $ t_{end} $ 的轨道运动参数预报值,求解方法分为数值法和解析法。

在一般应用场景下，数值法轨道预报相对于解析法轨道预报容易实现高精度，但预报速度较慢。

### 5.2 输入数据要求

轨道预报应输入空间物体在预报起始时刻的轨道运动参数。数据的内容和格式宜采用 GB/T 43223—2023 的要求。轨道预报还应明确预报结束时刻。

### 5.3 轨道预报技术流程

#### 5.3.1 数值法轨道预报技术流程

数值法轨道预报的技术流程是以预报起始时刻  $ t_{start} $  的轨道运动参数为初值，循环利用积分器和轨道动力学模型，计算下个时刻的轨道运动参数，直至预报结束时刻  $ t_{end} $  。数值法轨道预报的技术流程如图1所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_446_536_733_1117.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">图 1 数值法轨道预报的技术流程图</div>


一类典型的积分器为单步法积分器，能够实现根据当前时刻 $ t_{i} $ 的轨道运动参数 $ \vec{x}_{i} $ 计算下个时刻 $ t_{i+1} $ 的轨道运动参数 $ \vec{x}_{i+1} $ 的功能，可以表达为式(2)：

 $$ \vec{x}_{i+1}=N_{\mathrm{i n t g}}(t_{i},\vec{x}_{i},h) $$ 

式中：

 $ \vec{x}_{i+1} $  ——  $ t_{i+1} $  时刻轨道运动参数；

 $ N_{intg} $  ——从 $ t_{i} $ 时刻轨道运动参数到 $ t_{i+1} $ 时刻轨道运动参数的映射函数；

 $ \vec{x}_{i} $  —— $ t_{i} $  时刻轨道运动参数；

h ——积分步长，取值 $ t_{i+1}-t_{i} $ 。

注：在不考虑计算机舍入误差的前提下，积分步长越小，数值法预报精度越高。

利用单步法积分器实现数值法轨道预报的技术流程如图 2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_329_203_873_704.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图 2 单步法积分器实现数值法轨道预报的技术流程图</div>


#### 5.3.2 解析法轨道预报技术流程

解析法轨道预报的技术流程是通过求解动力学方程，得到由预报起始时刻 $ t_{start} $ 的轨道运动参数初值计算预报结束时刻 $ t_{end} $ 的轨道运动参数值的解析公式，实现轨道预报。解析法轨道预报的技术流程如图3所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_473_945_730_1356.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 3 解析法轨道预报的技术流程图</div>


一类典型的解析法计算预报结束时刻 $ t_{end} $ 的轨道运动参数的方法为：首先将 $ t_{start} $ 时刻轨道运动参数初值转换为 $ t_{start} $ 时刻平均根数，再计算 $ t_{end} $ 时刻平均根数，最后将 $ t_{end} $ 时刻平均根数转换为 $ t_{end} $ 时刻的轨道运动参数预报值，利用平均根数实现解析法轨道预报的技术流程如图4所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_431_203_743_1057.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">图 4 利用平均根数实现解析法轨道预报的技术流程图</div>


## 6 轨道确定技术要求

### 6.1 概述

轨道确定分为初轨确定和精密定轨。初轨确定相较于精密定轨精度较低。精密定轨分为批处理精密定轨和序贯处理精密定轨。序贯处理精密定轨相较于批处理精密定轨速度更快。

### 6.2 输入数据要求

#### 6.2.1 轨道测量数据要求

轨道确定输入的轨道测量数据应包含测量设备位置坐标，除非已明确测量数据以某个绝对位置（如坐标系原点）为基准。

初轨确定中，输入的轨道测量数据个数不能少于需要确定的轨道运动参数个数。

轨道测量数据内容和格式宜采用 GB/T 44316—2024 的要求。

#### 6.2.2 初始轨道运动参数要求

精密定轨应输入初始轨道运动参数。数据的内容和格式宜采用 GB/T 43223—2023 的要求。

#### 6.2.3 协方差数据要求

初轨确定宜输入轨道测量数据的协方差数据。

批处理精密定轨宜输入初始轨道运动参数的协方差数据和轨道测量数据的协方差数据。

序贯处理精密定轨应输入初始轨道运动参数的协方差数据和轨道测量数据的协方差数据。

### 6.3 初轨确定技术要求

初轨确定的技术流程如图 5 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_500_581_703_1084.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 5 初轨确定的技术流程图</div>


初轨确定方法中，计算轨道运动参数随时间的变化，应符合轨道动力学模型。

初轨确定输出应为确定时刻的轨道运动参数。

### 6.4 批处理精密定轨技术要求

#### 6.4.1 技术流程

批处理精密定轨是指利用累积的一批轨道测量数据（通常产生于不同测量时刻和不同测量设备），通过迭代逐步修正轨道运动参数初值的过程。批处理精密定轨的技术流程如图6所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_184_200_985_1146.jpg" alt="Image" width="67%" /></div>


 $ ^{a} $  最常用超出 3 倍测量量残差均方根作为判断测量量野值的标准。

<div style="text-align: center;">图 6 批处理精密定轨的技术流程图</div>


#### 6.4.2 轨道预报

以初始轨道运动参数或上一次迭代修正后的轨道运动参数为初值，求解动力学方程，计算每个测量时刻的轨道运动参数。具体技术要求见第5章。

#### 6.4.3 计算测量量理论值

根据轨道预报得到的每个测量时刻的轨道运动参数,通过测量方程,计算每个测量时刻的测量量的理论值。

#### 6.4.4 计算测量量残差

将每个测量时刻的实际测量值与测量量的理论值相减，得到每个测量时刻的测量量残差。

#### 6.4.5 剔除测量量野值

剔除测量量残差异常值，被剔除的测量量残差所对应的轨道测量数据不应用于精密定轨。通常情况下，被剔除的测量量残差大小明显超过了先验的或者估计的测量误差大小。

#### 6.4.6 判断残差统计值小于阈值

计算测量量残差的统计值(如均方根)，判断是否小于阈值或判断迭代次数是否大于预先设定的最大迭代次数。如果判断为是，当迭代次数超过设定上限，则批处理精密定轨失败，否则精密定轨成功，输出最后一次修正后的轨道运动参数。

注：阈值的设定一般与轨道确定精度相当。

#### 6.4.7 计算轨道运动参数修正值并修正轨道运动参数

利用测量量残差,计算轨道运动参数修正值。附录 C 中的 C.1 提供了一种计算轨道运动参数修正值的方法。

将轨道运动参数上一次迭代值(如果是第一次迭代则为初值)加上轨道运动参数修正值,得到修正后的轨道运动参数。

### 6.5 序贯处理精密定轨技术要求

#### 6.5.1 技术流程

序贯处理精密定轨是指将轨道测量数据按时间顺序分组处理进行精密定轨的过程。序贯处理精密定轨的技术流程如图7所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_283_203_890_1420.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 7 序贯处理精密定轨的技术流程图</div>


#### 6.5.2 轨道预报

以初始轨道运动参数或上一次修正后的轨道运动参数为初值，求解动力学方程，计算新的一组轨道测量数据测量时刻的轨道运动参数。具体技术要求见第5章。

#### 6.5.3 预报轨道运动参数协方差矩阵

以最新的轨道运动参数协方差矩阵为初值，计算新的一组轨道测量数据测量时刻的轨道运动参数协方差矩阵。C.3 提供了一种轨道运动参数协方差矩阵的计算方法。

#### 6.5.4 计算测量量理论值

根据轨道预报得到的测量时刻的轨道运动参数，通过测量方程，计算测量时刻的测量量的理论值。

#### 6.5.5 计算测量量残差

将测量时刻的实际测量值与测量量的理论值相减，得到测量时刻的测量量残差。

#### 6.5.6 剔除测量数据

剔除测量量残差异常值，被剔除的测量量残差所对应的轨道测量数据不应用于轨道运动参数修正和协方差矩阵修正。通常情况下，剔除测量量残差大小明显超过了先验的或者估计的测量误差大小。

#### 6.5.7 修正轨道运动参数及其协方差矩阵

根据测量量残差、测量量协方差修正轨道运动参数及其协方差矩阵。

### 6.6 输出数据要求

初轨确定、批处理精密定轨和序贯处理精密定轨的输出结果应包含轨道运动参数和轨道运动参数的协方差矩阵，宜采用 GB/T 43223—2023 的要求。宜输出测量量残差均方根、轨道测量数据利用率等作为评估轨道确定结果质量的参考。

## 附录 A

(资料性)

一种轨道动力学模型的摄动加速度计算方法

### A.1 地球非球形引力摄动

计算公式见式(A.1)~式(A.5):

 $$ \vec{F}_{\mathrm{grav}}=\mathbf{H}(\vec{F}_{\mathrm{zonal}}+\vec{F}_{\mathrm{tesseral}}) $$ 

 $$ \overrightarrow{F}_{zonal}=-\sum_{l\geqslant2}\overrightarrow{C}_{l,0}\frac{\mu a_{e}^{l}}{r^{l+3}}\{\left[(l+1)\;\overline{P}_{l,0}+\sin\varphi\;\overline{P^{\prime}}_{l,0}\right]\overrightarrow{R}-r\;\overline{P^{\prime}}_{l,0}\overrightarrow{k}\} $$ 

 $$ \overrightarrow{F}_{tesseral}=-\sum_{l\geqslant2}\sum_{m=1}^{l}\left\{\frac{\mu a_{e}^{l}}{r^{l+3}}\big[((l+1)\overline{P}_{l,m}+\sin\varphi\overline{P^{\prime}}_{l,m})\overrightarrow{R}-r\overline{P^{\prime}}_{l,m}\overrightarrow{k}\big]A_{lm}\right. $$ 

 $$ \left.+\frac{m}{\left(x^{2}+y^{2}\right)^{1/2}}\frac{\mu a_{\mathrm{e}}^{l}}{r^{l+1}}\overline{P}_{l,m}B_{l m}\overrightarrow{G}\right\} $$ 

 $$ A_{l m}=\overline{{C}}_{l,m}\cos m\lambda_{G}+\overline{{S}}_{l,m}\sin m\lambda_{G} $$ 

 $$ B_{l m}=\overline{{C}}_{l,m}\sin m\lambda_{G}-\overline{{S}}_{l,m}\cos m\lambda_{G} $$ 

式中：

 $ \vec{F}_{grav} $  ——地球非球形引力摄动加速度；

 $ \vec{F}_{zonal} $  ——地固坐标系中地球非球形引力摄动加速度带谐项部分；

 $ \vec{F}_{tesseral} $  ——地固坐标系中地球非球形引力摄动加速度田谐项部分；

H ——三维矢量由地固坐标系转到轨道动力学模型所采用坐标系的转换矩阵；

 $ \mu $  ——地球引力常数；

r ——空间物体地心距离；

 $ a_{e} $  ——地球赤道平均半径；

 $ \overline{P}_{l,m} $  ——归一化的连带勒让德多项式 $ \overline{P}_{l,m}(\sin\varphi) $ ， $ m=0,1,2\cdots l $ ；

 $ \overline{P}_{l,m}^{\prime} $  ——归一化的连带勒让德多项式的导数 $ \overline{P}_{l,m}^{\prime}(\sin\varphi) $ ， $ m=0,1,2\cdots l $ ；

 $ \overrightarrow{R} $  ——空间物体在地固坐标系中的位置矢量；

x ——空间物体在地固坐标系中的位置矢量的 x 轴分量；

y ——空间物体在地固坐标系中的位置矢量的 y 轴分量；

 $ \vec{k} $  ——矢量 $ (0\ 0\ 1)^{T} $ ;

 $ \overrightarrow{G} $  ——矢量 $ (- \sin \lambda_{G}\quad \cos \lambda_{G}\quad 0)^{T} $ ;

 $ \overline{C}_{l,m} $  ——地球引力场模型归一化球谐系数；

 $ \overline{S}_{l,m} $  ——地球引力场模型归一化球谐系数；

 $ \lambda_{G} $  ——空间物体在地固坐标系中的地心经度；

 $ \varphi $  ——空间物体在地固坐标系中的地心纬度。

### A.2 地球潮汐形变摄动

地球的潮汐形变是在太阳、月球等天体作用下，固体地球、海洋等对引潮力的响应而产生的形变。形变导致的质量重新分布会对空间物体的轨道运动产生影响。考虑地球自转平极和瞬时极的差异，地球自转导致的形变也会产生极潮。

潮汐形变会造成地球引力场模型归一化球谐系数变化。将加入了变化的归一化球谐系数代入到式(A.1)～式(A.3)，得到反映潮汐形变摄动的地球非球形引力摄动。二阶固体潮对应的球谐系数修正计算公式为式(A.6)：

 $$ \Delta\overline{C}_{2,m}-i\Delta\overline{S}_{2,m}=\frac{k_{2,m}}{5}\sum_{j}\frac{\mu_{j}}{\mu}\left(\frac{a_{\mathrm{e}}}{r_{j}}\right)^{3}\overline{P}_{2,m}\left(\sin\varphi_{j}\right)\mathrm{e}^{-i m\lambda_{j}} $$ 

式中：

 $ \Delta\overline{C}_{2,m} $  ——归一化引力场球谐系数 $ \overline{C}_{2,m} $  的二阶固体潮修正量；

i ——虚数单位；

 $ \Delta\overline{S}_{2,m} $  ——归一化引力场球谐系数 $ \overline{S}_{2,m} $  的二阶固体潮修正量；

 $ k_{2,m} $  ——二阶 m 次勒夫数；

 $ \sum $  ——对所有需要考虑的第三体产生的潮汐形变摄动加速度求和；

 $ \mu_{i} $  ——日、月等第三体的引力常数；

 $ \mu $  ——地球引力常数；

 $ a_{e} $  ——地球赤道平均半径；

 $ r_{i} $  ——日、月等第三体的地心距离；

 $ \overline{P}_{2,m} $  ——归一化的二阶 m 次连带勒让德多项式；

 $ \varphi_{i} $  ——日、月等第三体在地固坐标系中的地心纬度；

 $ \lambda_{i} $  ——日、月等第三体在地固坐标系中的地心经度。

考虑高精度的潮汐摄动，尤其需要注意地球非球形引力场系数中是否已经包含永久潮汐项。

### A.3 第三体引力摄动

计算公式为式(A.7):

 $$ \vec{F}_{3body}=-\sum_{j}\mu_{j}\left(\frac{\vec{\Delta}_{j}}{\Delta_{j}^{3}}+\frac{\vec{r}_{j}}{r_{j}^{3}}\right) $$ 

式中：

 $ \vec{F}_{3body} $ ——第三体引力摄动加速度；

 $ \sum $  ——对所有需要考虑的第三体产生的摄动加速度求和；

 $ \mu_{j} $  ——第三体的引力常数；

 $ \vec{r}_{i} $  ——第三体在和轨道动力学模型一致的坐标系中的地心位置矢量；

 $ r_{i} $  ——第三体的地心距离；

 $ \vec{\Delta}_{j} $  ——空间物体相对于第三体在和轨道动力学模型一致的坐标系中的位置矢量。

### A.4 后牛顿效应摄动

计算公式为式(A.8):

 $$ \vec{F}_{\mathrm{p N}}=\frac{\mu}{c^{2}r^{3}}\bigg[\bigg(\frac{4\mu}{r}-v^{2}\bigg)\vec{r}+4(\vec{r}\bullet\dot{\vec{r}})\dot{\vec{r}}\bigg] $$ 

式中：

 $ \overrightarrow{F}_{pN} $  ——由后牛顿效应引起的摄动加速度；

 $ \mu $  ——地球引力常数；

c ——真空中的光速；

r ——空间物体地心距离；

v ——空间物体在惯性坐标系下的速率；

 $ \vec{r} $  ——空间物体在和轨道动力学模型一致的坐标系中的位置矢量；

 $ \vec{r} $  ——空间物体在和轨道动力学模型一致的坐标系中的速度矢量。

### A.5 大气阻力摄动

计算公式为式(A.9):

 $$ \overrightarrow{F}_{\mathrm{D}}=-\frac{1}{2}C_{\mathrm{D}}\bigg(\frac{S_{\mathrm{D}}}{m}\bigg)\rho V\overrightarrow{V} $$ 

式中：

 $ \vec{F}_{D} $  ——大气阻力摄动加速度；

 $ C_{D} $  ——大气阻力系数；

 $ S_{D}/m $  ——空间物体等效大气阻力面积质量比；

ρ ——大气密度；

V ——空间物体相对大气的速率；

 $ \vec{V} $  ——空间物体相对大气的运动速度矢量。

### A.6 太阳光压摄动

计算公式为式(A.10):

 $$ \vec{F}_{\mathrm{SRP}}=\nu(1+\eta)\left(\frac{S_{R}}{m}\right)\left(\rho_{s}\frac{\Delta_{s}^{2}}{\Delta^{2}}\right)\hat{\Delta} $$ 

式中：

 $ \vec{F}_{SRP} $  ——太阳光压摄动加速度；

——表示地影因子，当空间物体位于地球阴影内时取值 0，当空间物体位于地球阴影以外时取值 1；

 $ \eta $  ——空间物体的表面反射系数；

 $ S_{R}/m $  ——空间物体等效太阳光压面积质量比；

 $ \rho_{s} $  ——距离太阳 $ \Delta_{s} $ 处受到的太阳光压强度；

 $ \Delta_{s} $  ——1个天文单位对应的距离；

△——空间物体到太阳的距离；

 $ \hat{\Delta} $  ——空间物体相对太阳位置的单位矢量。

## 附录 B

(资料性)

不同类型轨道和轨道预报精度要求下的摄动加速度模型设置

空间物体运动于不同近地点高度 $ (h) $ 和偏心率 $ (e) $ 的轨道情况下，在初始时刻，由轨道运动参数初值预报未来或过去24 h内的轨道运动参数，达到不同平均精度需求下对摄动加速度模型的配置要求如下。

注：因为大气阻力和太阳光压摄动受到空间物体和空间环境特性的影响存在不确定性，对轨道动力学模型精度造成的影响可能超过配置要求里给定的精度，因此这里给出的是达到相应精度要求时的必要配置，并非达到精度要求的充分条件。

a）轨道类型1:  $ 200\ km \leq h < 1\ 500\ km $  且  $ 0 \leq e < 0.1 $ ，见表B.1。

<div style="text-align: center;">表 B.1 轨道类型 1 在不同平均精度需求下的摄动加速度模型设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">摄动加速度模型</td><td colspan="4">轨道预报精度需求/m</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1 000</td></tr><tr><td style='text-align: center;'>非球形引力场阶次</td><td style='text-align: center;'>25～90</td><td style='text-align: center;'>15～80</td><td style='text-align: center;'>10～40</td><td style='text-align: center;'>5～20</td></tr><tr><td style='text-align: center;'>第三体位置精度</td><td style='text-align: center;'>L</td><td style='text-align: center;'>L</td><td style='text-align: center;'>L</td><td style='text-align: center;'>L</td></tr><tr><td style='text-align: center;'>潮汐形变摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>后牛顿效应</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>大气阻力摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>太阳光压摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td colspan="5">注1：L表示第三体位置精度低于第三体与地球平均距离的千分之一。注2：✓表示考虑其影响，✗表示不考虑其影响。</td></tr></table>

细分近地点高度下的非球形引力场阶次设置，见表 B.2。

<div style="text-align: center;">表 B.2 对轨道类型 1 细分近地点高度下对不同平均精度需求的非球形引力场阶次设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">近地点高度范围/km</td><td colspan="4">轨道预报精度需求/m</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1 000</td></tr><tr><td style='text-align: center;'>[200°～300)</td><td style='text-align: center;'>90</td><td style='text-align: center;'>80</td><td style='text-align: center;'>40</td><td style='text-align: center;'>20</td></tr><tr><td style='text-align: center;'>[300～400)</td><td style='text-align: center;'>80</td><td style='text-align: center;'>70</td><td style='text-align: center;'>30</td><td style='text-align: center;'>15</td></tr><tr><td style='text-align: center;'>[400～500)</td><td style='text-align: center;'>70</td><td style='text-align: center;'>50</td><td style='text-align: center;'>20</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>[500～600)</td><td style='text-align: center;'>65</td><td style='text-align: center;'>40</td><td style='text-align: center;'>20</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>[600～700)</td><td style='text-align: center;'>60</td><td style='text-align: center;'>40</td><td style='text-align: center;'>15</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>[700～800)</td><td style='text-align: center;'>55</td><td style='text-align: center;'>30</td><td style='text-align: center;'>15</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>[800～900)</td><td style='text-align: center;'>45</td><td style='text-align: center;'>30</td><td style='text-align: center;'>15</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>[900～1 000)</td><td style='text-align: center;'>40</td><td style='text-align: center;'>25</td><td style='text-align: center;'>15</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>[1 000～1 100)</td><td style='text-align: center;'>35</td><td style='text-align: center;'>25</td><td style='text-align: center;'>15</td><td style='text-align: center;'>5</td></tr></table>

<div style="text-align: center;">表 B.2 对轨道类型 1 细分近地点高度下对不同平均精度需求的非球形引力场阶次设置（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">近地点高度范围/km</td><td colspan="4">轨道预报精度需求/m</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1 000</td></tr><tr><td style='text-align: center;'>[1 100～1 200)</td><td style='text-align: center;'>30</td><td style='text-align: center;'>20</td><td style='text-align: center;'>10</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>[1 200～1 300)</td><td style='text-align: center;'>30</td><td style='text-align: center;'>20</td><td style='text-align: center;'>10</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>[1 300～1 400)</td><td style='text-align: center;'>30</td><td style='text-align: center;'>20</td><td style='text-align: center;'>10</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>[1 400～1 500)</td><td style='text-align: center;'>25</td><td style='text-align: center;'>15</td><td style='text-align: center;'>10</td><td style='text-align: center;'>5</td></tr><tr><td colspan="5">$ ^{*} $ 对于近地点高度小于200 km的轨道，也可以按照此配置设定非球形引力场阶次。</td></tr></table>

b）轨道类型2:1 500 km≤h<30 000 km 且 0≤e<0.1，见表B.3。

<div style="text-align: center;">表 B.3 轨道类型 2 在不同平均精度需求下的摄动加速度模型设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">摄动加速度模型</td><td colspan="4">轨道预报精度需求/m</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1 000</td></tr><tr><td style='text-align: center;'>非球形引力场阶次</td><td style='text-align: center;'>20</td><td style='text-align: center;'>15</td><td style='text-align: center;'>10</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>第三体位置精度</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>L</td><td style='text-align: center;'>L</td></tr><tr><td style='text-align: center;'>潮汐形变摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>后牛顿效应</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>大气阻力摄动</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>太阳光压摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td></tr><tr><td colspan="5">注1：L表示第三体位置精度低于第三体与地球平均距离的千分之一；H表示第三体位置精度高于第三体与地球平均距离的千分之一。注2：✓表示考虑其影响，✗表示不考虑其影响。</td></tr></table>

c）轨道类型 3:30 000 km≤h＜40 000 km 且 0≤e＜0.1，见表 B.4。

<div style="text-align: center;">表 B.4 轨道类型 3 在不同平均精度需求下的摄动加速度模型设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">摄动加速度模型</td><td colspan="4">轨道预报精度需求/m</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1 000</td></tr><tr><td style='text-align: center;'>非球形引力场阶次</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>第三体位置精度</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>L</td><td style='text-align: center;'>L</td></tr><tr><td style='text-align: center;'>潮汐形变摄动</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td></tr><tr><td style='text-align: center;'>后牛顿效应</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td></tr><tr><td style='text-align: center;'>大气阻力摄动</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td></tr><tr><td style='text-align: center;'>太阳光压摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>×</td></tr><tr><td colspan="5">注1: L 表示第三体位置精度低于第三体与地球平均距离的千分之一; H 表示第三体位置精度高于第三体与地球平均距离的千分之一。注2: ✓ 表示考虑其影响, × 表示不考虑其影响。</td></tr></table>

d）轨道类型4:  $ 200\ km \leqslant h < 40\ 000\ km $  且  $ 0.1 \leqslant e < 1 $ ，见表 B.5。

<div style="text-align: center;">表 B.5 轨道类型 4 在不同平均精度需求下的摄动加速度模型设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">摄动加速度模型</td><td colspan="4">轨道预报精度需求/m</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1 000</td></tr><tr><td style='text-align: center;'>非球形引力场阶次</td><td style='text-align: center;'>50</td><td style='text-align: center;'>40</td><td style='text-align: center;'>20</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>第三体位置精度</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>L</td><td style='text-align: center;'>L</td></tr><tr><td style='text-align: center;'>潮汐形变摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>后牛顿效应</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>大气阻力摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>太阳光压摄动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✗</td></tr><tr><td colspan="5">注1：L表示第三体位置精度低于第三体与地球平均距离的千分之一；H表示第三体位置精度高于第三体与地球平均距离的千分之一。注2：✓表示考虑其影响，✗表示不考虑其影响。</td></tr></table>

## 附录 C

(资料性)

基于线性化理论的轨道运动参数修正和协方差预报方法

### C.1 基于最小二乘估计的轨道运动参数修正值计算方法

基于最小二乘估计理论，计算轨道运动参数修正值的方法的具体步骤如下。

a）计算每个测量时刻 $ t_{i} $ 的状态转移矩阵 $ \Phi_{i} $ 。状态转移矩阵的计算方法可以是数值法、解析法和差分法等，见C.2。

b）计算每个测量时刻 $ t_{i} $ 的测量矩阵 $ Y_{i} $ 

c）计算矩阵为式(C.1):

 $$ \boldsymbol{P}=\sum_{i=1}^{n}\mathbf{\Psi}\left(\mathbf{Y}_{i}\boldsymbol{\Phi}_{i}\right)^{T}\mathbf{W}_{i}\left(\mathbf{Y}_{i}\boldsymbol{\Phi}_{i}\right) $$ 

式中：

 $ W_{i} $ ——批处理精密定轨中测量时刻 $ t_{i} $ 的轨道测量数据的权重矩阵；

 $ Y_{i} $  ——测量时刻 $ t_{i} $ 的测量矩阵；

 $ \Phi_{i} $ ——测量时刻 $ t_{i} $ 的状态转移矩阵。

 $$ \boldsymbol{Q}=\sum_{i=1}^{n}\left(\boldsymbol{Y}_{i}\boldsymbol{\Phi}_{i}\right)^{T}\boldsymbol{W}_{i}\boldsymbol{y}_{i} $$ 

式中：

 $ y_{i} $  ——测量时刻 $ t_{i} $ 的测量量残差；

 $ W_{i} $ ——批处理精密定轨中测量时刻 $ t_{i} $ 的轨道测量数据的权重矩阵；

 $ Y_{i} $  ——测量时刻 $ t_{i} $ 的测量矩阵；

 $ \Phi_{i} $ ——测量时刻 $ t_{i} $ 的状态转移矩阵。

用户可自定义加权方法，例如将 $ W_{i} $ 设置为 $ t_{i} $ 时刻的轨道测量数据协方差矩阵的逆矩阵。

d）计算轨道运动参数修正值 $ d_{x} $ 

 $$ \boldsymbol{d}_{x}=\boldsymbol{P}^{-1}\boldsymbol{Q} $$ 

式中：

 $ P^{-1} $ ——P 矩阵的逆矩阵。

### C.2 状态转移矩阵计算方法

状态转移矩阵  $ \boldsymbol{\Phi}(t) $  表示任意 t 时刻轨道运动参数  $ \boldsymbol{X}(t) $  对初始  $ t_{0} $  时刻轨道运动参数  $ \boldsymbol{X}(t_{0}) $  的偏导数矩阵，可用来计算线性意义下初始时刻轨道运动参数的偏差随时间的演化，状态转移矩阵可表示为式(C.4)：

 $$ \mathbf{\Phi}(t)=\frac{\partial\mathbf{X}(t)}{\partial\mathbf{X}(t_{0})} $$ 

式中：

 $ \Phi(t) $  —— t 时刻的状态转移矩阵；

 $  \mathbf{X}(t)  $  —— t 时刻轨道运动参数；

 $  \mathbf{X}(t_{0})  $  ——初始 $ t_{0} $ 时刻轨道运动参数。

精密定轨中，已知初始时刻的轨道运动参数  $ \mathbf{X}(t_{0}) $  ，计算状态转移矩阵通常有三种方法。

a）根据轨道运动参数随时间变化的解析公式  $ X[t;X(t_{0})] $ ，按照式(C.4)推导  $ \Phi(t) $  的解析表达；

b)  $ \Phi(t) $  的数值解通过积分，按式(C.5)～式(C.6)计算：

 $$ \left\{\begin{aligned}\dot{\boldsymbol{\Phi}}(t)=&\boldsymbol{A}\boldsymbol{\Phi}(t)\\ \boldsymbol{\Phi}(t_{0})=I\end{aligned}\right. $$ 

 $$ \boldsymbol{A}=\frac{\partial(\dot{\vec{r}},\ddot{\vec{r}},\dot{\beta})}{\partial(\vec{r},\dot{\vec{r}},\beta)} $$ 

式中：

 $ \Phi(t) $  —— t 时刻的状态转移矩阵变率；

 $ \Phi(t) $  —— t 时刻的状态转移矩阵；

 $ \Phi(t_{0}) $  —— $ t_{0} $  时刻的状态转移矩阵；

I ——单位矩阵；

 $ \dot{\vec{r}} $  —— t 时刻空间物体速度矢量；

 $ \dot{\vec{r}} $  —— t 时刻空间物体加速度矢量；

 $ \vec{r} $  —— t 时刻空间物体位置矢量；

 $ \beta $  ——轨道运动参数中的轨道动力学模型参数的变率；

 $ \beta $  ——轨道运动参数中的轨道动力学模型参数。

c) 根据  $ \Phi(t) $  的含义，分别在每个轨道运动参数上添加“小偏差”，然后将加入了偏差的轨道及原轨道均预报至 t 时刻，利用偏差的轨道预报值相对于原轨道预报值的差分结果计算  $ \Phi(t) $  的近似值。

### C.3 轨道运动参数协方差矩阵的线性预报方法

利用初始轨道运动参数协方差矩阵  $ \boldsymbol{P}(t_{0}) $ ，采用式(C.7)以线性预报方法计算任意时刻的协方差矩阵  $ \boldsymbol{P}(t) $ ：

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_960_151_993.jpg" alt="Image" width="3%" /></div>


 $$ \mathbf{P}(t)=\mathbf{\Phi}(t)\mathbf{P}(t_{0})\mathbf{\Phi}^{T}(t) $$ 

式中：

 $ P(t) $  —— t 时刻的协方差矩阵；

 $ \Phi(t) $  —— t 时刻的状态转移矩阵；

 $ P(t_{0}) $  ——初始轨道运动参数协方差矩阵。

## 参 考 文 献

[1] GB/T 43223—2023 空间物体轨道数据规范

[2] GB/T 44316—2024 空间物体监测数据规范

[3] ISO Space Systems—Orbit Determination and Estimation—Process for Describing Techniques. 2013.

[4] Astronautics, American Institute of Aeronautics and. Astrodynamics—Propagation Specifications, Technical Definitions, and Recommended Practices. AIAA:2010.

[5] IAU resolutions. adopted at the 24th general assembly. 2000.

[6] Gérard Petit and Brian Luzum. IERS Conventions 2010 (IERS Technical Note 36). Frankfurt am Main: Verlag des Bundesamts für Kartographie und Geodäsie, 2010.

