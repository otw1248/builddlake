

# 中华人民共和国国家标准

GB/T 31054—2014

# 机械产品计算机辅助工程 有限元数值计算 术语

# Computer aided engineering for mechanical products—Finite element numerical calculation—Terminology

2014-12-22 发布

2015-10-01 实施

## 目次

前言 …… I  
  
1 范围 …… 1  
  
2 一般术语 …… 1  
  
2.1 基本概念 …… 1  
  
2.2 前处理 …… 2  
  
2.3 单元 …… 4  
  
2.4 后处理 …… 5  
  
3 典型结构数值分析术语 …… 7  
  
3.1 结构静力学分析 …… 7  
  
3.2 结构动力学分析 …… 8  
  
3.3 结构热分析 …… 10  
  
3.4 结构耦合分析 …… 10  
  
3.5 结构优化设计 …… 11  
  
参考文献 …… 12  
  
索引 …… 13

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国技术产品文件标准化技术委员会(SAC/TC 146)提出并归口。

本标准起草单位:中国电子科技集团公司第三十八研究所、中机生产力促进中心、合肥瑞齐信息科技有限公司、北京科新纪元信息技术有限公司。

本标准主要起草人：张红旗、肖承翔、胡祥涛、陈帝江、张深广、李岱松、王云锋、高宏伟、杨东拜。

# 机械产品计算机辅助工程   有限元数值计算 术语

## 1 范围

本标准规定了机械产品计算机辅助工程有限元数值计算的常用术语和定义。

本标准适用于与机械产品有限元数值计算相关的研究、开发和应用。

## 2 一般术语

### 2.1 基本概念

#### 2.1.1 

## 计算机辅助工程 computer aided engineering(CAE)

运用计算机技术和数值分析技术(如有限单元法、有限差分法或离散元法等)获取物理系统的应力场、温度场或电磁场等物理场响应量的过程和方法，常用于评估系统功能和性能，优化结构、工艺或成本等目的。

#### 2.1.2 

## 有限单元法 finite element method(FEM)

## 有限元法

将连续的求解域离散为有限个单元，并在给定约束条件下，利用有限单元的近似解逼近真实物理系统的数值分析方法。

#### 2.1.3 

## 有限元分析 finite element analysis (FEA)

基于有限单元法的结构性能分析。

#### 2.1.4 

## 单元 element

具有几何、物理属性的最小求解域。

#### 2.1.5 

## 节点 node

单元之间的铰接点。

注：每个单元仅在节点处和相邻单元及外部发生联系。

#### 2.1.6 

## 前处理 preprocessing

几何模型处理、有限单元划分、物理参数设置和边界条件施加的过程。

#### 2.1.7 

## 求解 solve

设定求解环境(或条件)和寻求近似解的过程。

#### 2.1.8 

## 后处理 post-processing

对求解结果进行检查、分析和评估等处理的过程。

#### 2.1.9 

## 通用运动方程 general kinematics equation

描述载荷、惯性、阻尼和位移响应相互关系的方程，见式(1)：

 $$ M\ddot{u}+C\dot{u}+K u=F(t) $$ 

……(1)

式中：

M ——质量矩阵；

C —— 阻尼矩阵；

K ——刚度矩阵；

F ——载荷向量；

u ——位移响应；

t ——时间。

#### 2.1.10 

## 结构静力学分析 structural statics analysis

在静态或可近似静态载荷作用下，忽略惯性和阻尼效应的结构响应分析。

#### 2.1.11 

结构动力学分析 structural dynamics analysis

在时变载荷以及惯性和阻尼效应作用下,对结构动力学特性和响应的分析。

#### 2.1.12 

结构热分析 structural thermal analysis

对结构温度场及其他热物理参数的分析。

#### 2.1.13 

## 结构耦合分析 structural coupling analysis

在两个或多个物理场耦合作用下的结构响应分析。

#### 2.1.14 

## 优化设计 optimal design

用于确定结构几何、物理和工艺等设计参数，以满足最优性能、可靠性、重量和成本等要求。

#### 2.1.15 

## 设计模型 design model

侧重于产品几何描述的结构设计模型。

### 2.2 前处理

#### 2.2.1 

## 简化模型 simplified model

对机械产品设计模型中局部几何特征进行简化处理后的模型。

#### 2.2.2 

## 理想模型 ideal model

对机械产品物理特征进行理想化处理后的模型，如变形可以忽略不计的柔性体可理想化处理为刚体。

#### 2.2.3 

## 有限元模型 finite element model

以有限数量单元的组合逼近机械产品结构的模型，或更一般地物理系统结构的模型。

#### 2.2.4 

## 有限元建模 finite element modeling

构建有限元模型的过程，包括几何模型处理、有限单元设置和划分等步骤。

#### 2.2.5 

## 分析模型 analysis model

在有限元模型基础上，施加了材料性能和边界条件的模型。

#### 2.2.6 

## 工况 working conditions

机械产品在一定环境条件下的典型工作状况。

#### 2.2.7 

## 边界条件 boundary conditions

在给定工况下，求解域边界上的几何、物理条件，如力、温度、速度和位移等。

#### 2.2.8 

## 材料性能 material property

材料的力学、热学、电磁学等物理性能参数，如弹性模量、泊松比和密度等。

#### 2.2.9 

## 单元属性 element attribute

单元的几何、物理特性，如单元类型、材料性能和几何形状等。

#### 2.2.10 

## 自由度 degrees of freedom

力学系统中，完全确定一个机械结构形位所需的独立坐标个数。

#### 2.2.11 

## 约束 constraint

减少系统自由度的各种限制条件。

[GB/T 10853—2008, 定义 3.3.13]

#### 2.2.12 

## 位移 displacement

表征物体上一点相对于某参考系的位置变化的时间变量。

[GB/T 2298—2010, 定义 2.1]

#### 2.2.13 

## 节点位移 node displacement

节点相对于某参考系的位置变化的时间变量。

#### 2.2.14 

## 载荷 load

施加在物体或系统上的作用力系。

 $$  \text{[GB/T 10853—2008, 定义 5.2.58]}  $$ 

#### 2.2.15 

## 集中载荷 concentrated load

作用面积远小于物体表面尺寸，可近似作用于一点的载荷。

#### 2.2.16 

## 线载荷 line load

其作用点连续分布在给定线段上的载荷。

## GB/T 31054—2014

#### 2.2.17 

## 面载荷 surface load

其作用点连续分布在给定表面上的载荷。

#### 2.2.18 

## 体载荷 body load

其作用点连续分布在体积域或场域内的载荷,如重力。

#### 2.2.19 

## 内力 internal force

结构内部由于发生变形而产生的相互作用力。

#### 2.2.20 

## 惯性力 inertial force

质量被加速时产生的反作用力。

[GB/T 2298—2010, 定义 2.9]

#### 2.2.21 

## 载荷步 load step

人为设定的与真实时间无关的时间间隔。

注：载荷步一般用于离散时的变载荷，使其成为一系列静态载荷。

#### 2.2.22 

## 载荷子步 load substep

离散的载荷步时间节点，用于插值施加静态载荷。

注：载荷子步对求解效率和收敛性有明显影响。

#### 2.2.23 

## 收敛容限 convergence tolerance

判断收敛条件的阈值。

### 2.3 单元

#### 2.3.1 

## 形函数 shape function

## 插值函数

定义于单元内部的连续函数，描述单元内部任意点位移与节点位移插值关系。

#### 2.3.2 

## 单元阶次 element order

形函数的最高阶次。

#### 2.3.3 

## 等参单元 isoparametric element

采用同阶次同参数插值函数描述几何形状和位移场的单元。

#### 2.3.4 

## 超参单元 super-parameteric element

几何形状插值函数阶次高于位移场插值函数阶次的单元。

#### 2.3.5 

## 次参单元 sub-parameteric element

几何形状插值函数阶次低于位移场插值函数阶次的单元。

#### 2.3.6 

## 一 维单元 one dimensional element

表现形式为线段的单元。

#### 2 \.3\.7

## 二 维单元 two dimensional element

表现形式为面片的单元,如矩形单元、三角形单元等。

#### 2.3.8 

## 三 维单元 three dimensional element

表现形式为实体的单元，如四面体单元、六面体单元等。

#### 2.3.9 

## 接触单元 contact element

结构相互接触约束作用的单元。

#### 2.3.10 

## 弹簧单元 spring element

结构之间具有弹簧约束作用的单元。

#### 2.3.11 

## 质量单元 mass element

只具备质量属性的单元。

#### 2.3.12 

## 实常数 real constant

具有统一特征的几何或物理常数，用于补充描述单元属性。

### 2.4 后处理

#### 2.4.1 

应力 stress

结构某点受到的单位面积内力。

#### 2.4.2 

## 正应力 normal stress

垂直于给定平面的应力分量。

[GB/T 10623—2008, 定义 2.13.2]

#### 2.4.3 

剪应力 shear stress

平行于给定表面的应力分量。

#### 2.4.4 

## 单元应力 element stress

单元某点受到的单位面积内力。

#### 2.4.5 

节点应力 node stress

节点受到的单位面积内力。

注：在有限单元法中，单元应力由单元各节点位移决定，节点应力由相关联单元应力共同决定。

<div style="text-align: center;"><img src="imgs/img_in_image_box_921_1399_956_1433.jpg" alt="Image" width="2%" /></div>


#### 2.4.6 

## 主应力 principal stress

一类应力矢量，在以该应力矢量为法向的微面积元上，剪应力为0。

#### 2.4.7 

## 等效应力 equivalent stress

由强度准则计算的当量应力，一般采用第四强度准则，见式(2)：

 $$ \sigma_{\mathrm{e}}=\left[\frac{(\sigma_{1}-\sigma_{2})^{2}+(\sigma_{2}-\sigma_{3})^{2}+(\sigma_{1}-\sigma_{3})^{2}}{2}\right]^{\frac{1}{2}} $$ 

式中：

 $ \sigma_{e} $  ——等效应力；

 $ \sigma_{1} $  ——第一主应力；

 $ \sigma_{2} $  ——第二主应力；

 $ \sigma_{3} $  ——第三主应力。

#### 2.4.8 

## 变形 deformation

由外力引起的结构尺寸和形状的变化。

#### 2.4.9 

## 应变 strain

由外力引起的结构尺寸和形状的单位变化量，表示结构变形程度。

#### 2.4.10 

## 正应变 normal strain

在正应力作用下，通过结构某点的微线段元的单位长度变化量。

#### 2.4.11 

## 剪应变 shear strain

在剪应力作用下，通过结构某点的微直角元的形状变化量（角度变化量）。

#### 2.4.12 

## 主应变 principal strain

一类应变，在以该应变为法向的微面积元上，剪应变为0。

#### 2.4.13 

## 等效应变 equivalent strain

与等效应力对应的当量应变，由第四强度准则决定的等效应变，见式(3)：

 $$ \varepsilon_{\mathrm{e}}=\frac{1}{1+\nu}\Big[\frac{(\varepsilon_{1}-\varepsilon_{2})^{2}+(\varepsilon_{2}-\varepsilon_{3})^{2}+(\varepsilon_{1}-\varepsilon_{3})^{2}}{2}\Big]^{\frac{1}{2}} $$ 

式中：

 $ \varepsilon_{c} $  ——等效应变；

 $ \varepsilon_{1} $  ——第一主应变；

 $ \varepsilon_{2} $  ——第二主应变；

 $ \varepsilon_{3} $  ——第三主应变；

 $ ν $  ——泊松比。

#### 2.4.14 

## 弹性应变 elastic strain

在外力作用下，对应结构弹性变形部分的应变。

#### 2.4.15 

## 塑性应变 plastic strain

在外力作用下，对应结构塑性变形部分的应变。

#### 2.4.16 

## 时间历程曲线 curse of time history

有限元分析结果随载荷步或载荷子步变化的曲线。

#### 2.4.17 

## 等值线图 isoline map

利用等值线显示结构内任意一点计算结果的分布图。

#### 2.4.18 

## 云图 cloud map

利用色彩显示结构内任意一点计算结果的分布图。

#### 2.4.19 

## 矢量图 vector map

以带方向的线段显示结构内任意一点矢量结果的分布图。

#### 2.4.20 

## 应力集中 stress concentration

结构局部应力显著增大的现象。

## 3 典型结构数值分析术语

### 3.1 结构静力学分析

#### 3.1.1 

## 杆 bar

长度远大于其他方向尺寸的构件。

#### 3.1.2 

## 桁架 truss

由有限根杆通过铰相互连接而成的结构。

注：桁架包括平面桁架和空间桁架。

#### 3.1.3 

## 梁 beam

承受横向载荷，以弯曲变形为主的杆结构。

#### 3.1.4 

## 板壳 plane & shell

厚度方向尺寸远小于长度和宽度方向尺寸的结构。

注：表面为平面的称为板，表面为曲面的称为壳。

#### 3.1.5 

## 强度 strength

结构抵抗破坏的能力。

#### 3.1.6 

## 刚度 stiffness

结构抵抗变形的能力。

#### 3.1.7 

## 单元刚度 element stiffness

单元抵抗变形的能力。

## GB/T 31054—2014

#### 3.1.8 

## 稳定性 stability

结构保持原有平衡状态的能力。

#### 3.1.9 

## 节点自由度 node freedom

节点独立坐标的个数，通常每个节点具有6个自由度。

#### 3.1.10 

## 单元自由度 element freedom

单元独立坐标的个数。

#### 3 \.1\.11

## 结构自由度 structure freedom

结构独立坐标的个数。

#### 3 \.1\.12

## 平面应力问题 plane stress problem

应力只存在于平面内，沿厚度方向应力为 0 的结构静力学问题。

#### 3.1.13 

## 平面应变问题 plane strain problem

应变只存在于平面内，沿厚度方向应变为0的结构静力学问题。

#### 3 \.1\.14

## 轴对称问题 axisymmetric problem

几何形状和边界条件都对称于空间某一轴的结构静力学问题。

#### 3 \.1\.15

## 非线性静力学分析 nonlinear static analysis

考虑非线性因素的结构静力学分析，如大变形、塑形、蠕变等结构非线性分析。

#### 3 \.1\.16

## 状态非线性 state nonlinearity

系统刚度与结构状态相关的非线性行为。

#### 3 \.1\.17

## 材料非线性 material nonlinearity

非线性应力-应变关系引起的结构非线性行为。

#### 3 \.1\.18

## 几何非线性 geometry nonlinearity

因大变形引起结构几何形状变化的非线性行为。

#### 3.1.19 

## 屈曲分析 bulking analysis

用于预测屈曲强度和临界失稳载荷的结构分析。

注：含结构线性屈服分析和结构非线性屈曲分析。

### 3.2 结构动力学分析

#### 3.2.1 

## 模态 modal

结构固有振动特性，如固有频率和振型。

#### 3.2.2 

## 时域分析 time-domain analysis

在时间域中对结构进行的动力学响应分析。

#### 3.2.3 

## 频域分析 frequency-domain analysis

在频率域中对结构进行的动力学响应分析。

#### 3.2.4 

## 谱 spectrum

以频率或波长为变量的函数的量化描述。

[GB/T 2298—2010, 定义 2.61]

#### 3.2.5 

## 阻尼 damping

使能量随时间或距离发生耗散的物理参数。

#### 3.2.6 

## 临界阻尼比 critical damping ratio

实际阻尼系数与临界阻尼系数的比值。

#### 3.2.7 

## 结构阻尼 structural damping

由结构内的内部摩擦引起的结构内的能量耗散。

[GB/T 2298—2010, 定义 3.93]

#### 3.2.8 

## 模态分析 modal analysis

基于叠加原理的振动分析方法，用复杂结构系统自身的振动模态，即固有频率、模态阻尼和模态振型来表示其振动特性。

[GB/T 2298—2010, 定义 2.44]

#### 3.2.9 

## 谐响应分析 harmony response analysis

用于分析结构在正弦规律变化载荷作用下结构稳态响应的技术。

#### 3.2.10 

## 瞬态动力学分析 transient dynamic analysis

用于分析结构在随机载荷作用下结构动力学响应的技术，也称为时间历程分析。

#### 3.2.11 

## 谱分析 spectrum analysis

用于分析在含各种频率的瞬态激励下结构动力学响应的技术。

#### 3.2.12 

## 模态叠加 modal superposition

将结构振形加权叠加起来分析结构动力学响应的技术。

#### 3.2.13 

## 激励 excitation: stimulus

作用于系统的外力(或其他输入)，使系统以某种方式产生响应。

[GB/T 2298—2010, 定义 2.16]

#### 3.2.14 

共振 resonance

受迫振荡系统固有频率同激励频率一致时产生的振动状态。

### 3.3 结构热分析

#### 3.3.1 

稳态热分析 steady-state thermal analysis

用于分析稳定热载荷作用下系统温度场及其他热学参数的方法。

#### 3.3.2 

瞬态热分析 transient thermal analysis

用于分析时变热载荷作用下系统温度场及其他热学参数的方法。

#### 3.3.3 

热应力分析 thermal-stress analysis

用于热载荷引起的结构应力场的方法。

#### 3.3.4 

热载荷 thermal load

与热相关的载荷，包含温度、热流速率、热流密度、对流、辐射、绝热或热生成率等。

#### 3.3.5 

热流速率 heat flow rate

单位时间传递的热量 $ \left(\mathrm{d}Q/\mathrm{d}t\right) $ ，见式(4)，以W（瓦）表示：

 $$ Q=\int\frac{\mathrm{d}Q}{\mathrm{d}t}\mathrm{d}t $$ 

式中：

Q——热量。

[GB/T 6425—2008, 定义 3.5.6.3]

#### 3.3.6 

## 线膨胀系数 coefficient of linear thermal expansion

每单位长度单位温度变化材料长度的可逆增量。

[GB/T 6425—2008, 定义 3.5.10]

3.3.7

热流密度 heat flux density

单位时间内通过单位面积的热量。

### 3.4 结构耦合分析

#### 3.4.1 

热固耦合 thermo-solid coupling

温度场和应力场的相互耦合作用及影响。

3.4.2

流固耦合 fluid-solid coupling

流场和应力场的相互耦合作用及影响。

3.4.3

磁固耦合 magnetism-solid coupling

电磁场和应力场的相互耦合作用及影响。

#### 3.4.4 

热流固耦合 thermo-fluid-solid coupling

温度场、流场和应力场的相互耦合作用及影响。

#### 3.4.5 

顺序耦合方法 sequential coupling method

按照顺序进行两次或多次相关场分析的耦合场分析方法。

#### 3.4.6 

直接耦合方法 direct coupling method

利用耦合单元模型直接分析耦合场的分析方法。

### 3.5 结构优化设计

#### 3.5.1 

## 参数化模型 parameter model

在前处理时，将结构设计模型中的几何量、物理量或边界条件参数化的模型。

#### 3.5.2 

## 目标函数 objective function

描述结构优化设计的目标与设计变量及状态变量的映射关系。

#### 3.5.3 

设计变量 design variable

参数化的几何、物理或边界条件，属自变量。

#### 3.5.4 

状态变量 state variable

因结构设计变量的改变而引起结构状态变化的量，属因变量。

#### 3.5.5 

拓扑优化 topological optimization

以材料最佳利用为目标的结构形状优化。

#### 3.5.6 

可靠性优化 reliability optimization

以可靠度为目标或约束条件的结构优化。

## 参 考 文 献

[1] GB/T 2298—2010 机械振动、冲击与状态监测 词汇

[2] GB/T 6425—2008 热分析术语

[3] GB/T 10623—2008 金属材料 力学性能试验术语

[4] GB/T 10853—2008 机构与机器科学词汇

## 索引

## 汉语拼音索引

B  
  
板壳 …… 3.1.4  
边界条件 …… 2.2.7  
变形 …… 2.4.8  
  
C  
  
参数化模型 …… 3.5.1  
材料性能 …… 2.2.8  
材料非线性 …… 3.1.17  
超参单元 …… 2.3.4  
次参单元 …… 2.3.5  
磁固耦合 …… 3.4.3  
  
D  
  
单元 …… 2.1.4  
单元属性 …… 2.2.9  
单元阶次 …… 2.3.2  
单元自由度 …… 3.1.10  
单元刚度 …… 3.1.7  
单元应力 …… 2.4.4  
等参单元 …… 2.3.3  
等效应力 …… 2.4.7  
等效应变 …… 2.4.13  
等值线图 …… 2.4.17  
  
E  
  
二维单元 …… 2.3.7  
  
F  
  
非线性静力学分析 …… 3.1.15  
分析模型 …… 2.2.5  
  
G  
  
杆 …… 3.1.1  
刚度 …… 3.1.6  
工况 …… 2.2.6  
共振 …… 3.2.14

惯性力 …… 2.2.20  
H  
桁架 …… 3.1.2  
后处理 …… 2.1.8  
J  
集中载荷 …… 2.2.15  
激励 …… 3.2.13  
几何非线性 …… 3.1.18  
计算机辅助工程 …… 2.1.1  
结构静力学分析 …… 2.1.10  
结构动力学分析 …… 2.1.11  
结构热分析 …… 2.1.12  
结构耦合分析 …… 2.1.13  
结构自由度 …… 3.1.11  
结构阻尼 …… 3.2.7  
简化模型 …… 2.2.1  
节点 …… 2.1.5  
节点自由度 …… 3.1.9  
节点应力 …… 2.4.5  
节点位移 …… 2.2.13  
剪应力 …… 2.4.3  
剪应变 …… 2.4.11  
接触单元 …… 2.3.9  
K  
可靠性优化 …… 3.5.6  
L  
理想模型 …… 2.2.2  
梁 …… 3.1.3  
临界阻尼比 …… 3.2.6  
流固耦合 …… 3.4.2  
M  
面载荷 …… 2.2.17  
模态 …… 3.2.1

模态分析 …… 3.2.8    
模态叠加 …… 3.2.12    
目标函数 …… 3.5.2    
  
N    
内力 …… 2.2.19    
P    
平面应力问题 …… 3.1.12    
平面应变问题 …… 3.1.13    
频域分析 …… 3.2.3    
谱 …… 3.2.4    
谱分析 …… 3.2.11    
  
Q    
前处理 …… 2.1.6    
求解 …… 2.1.7    
强度 …… 3.1.5    
屈曲分析 …… 3.1.19    
  
R    
热固耦合 …… 3.4.1    
热流固耦合 …… 3.4.4    
热流速率 …… 3.3.5    
热应力分析 …… 3.3.3    
热载荷 …… 3.3.4    
热流密度 …… 3.3.7    
  
S    
三维单元 …… 2.3.8    
设计变量 …… 3.5.3    
设计模型 …… 2.1.15    
实常数 …… 2.3.12    
时间历程曲线 …… 2.4.16    
时域分析 …… 3.2.2    
矢量图 …… 2.4.19    
收敛容限 …… 2.2.23    
瞬态动力学分析 …… 3.2.10    
瞬态热分析 …… 3.3.2    
顺序耦合方法 …… 3.4.5    
塑性应变 …… 2.4.15    
  
T    
弹性应变 …… 2.4.14    
弹簧单元 …… 2.3.10

体载荷 …… 2.2.18    
通用运动方程 …… 2.1.9    
拓扑优化 …… 3.5.5    
  
W    
位移 …… 2.2.12    
稳定性 …… 3.1.8    
稳态热分析 …… 3.3.1    
  
X    
线载荷 …… 2.2.16    
线膨胀系数 …… 3.3.6    
谐响应分析 …… 3.2.9    
形函数 …… 2.3.1    
  
Y    
一维单元 …… 2.3.6    
应力 …… 2.4.1    
应力集中 …… 2.4.20    
应变 …… 2.4.9    
有限单元法 …… 2.1.2    
有限元法 …… 2.1.2    
有限元分析 …… 2.1.3    
有限元模型 …… 2.2.3    
有限元建模 …… 2.2.4    
优化设计 …… 2.1.14    
约束 …… 2.2.11    
云图 …… 2.4.18    
  
Z    
载荷 …… 2.2.14    
载荷步 …… 2.2.21    
载荷子步 …… 2.2.22    
正应力 …… 2.4.2    
正应变 …… 2.4.10    
质量单元 …… 2.3.11    
直接耦合方法 …… 3.4.6    
轴对称问题 …… 3.1.14    
主应力 …… 2.4.6    
主应变 …… 2.4.12    
状态非线性 …… 3.1.16    
状态变量 …… 3.5.4    
自由度 …… 2.2.10    
阻尼 …… 3.2.5

A  
  
axisymmetric problem 3.1.14  
analysis model 2.2.5  
B  
  
bar 3.1.1  
beam 3.1.3  
boundary conditions 2.2.7  
body load 2.2.18  
bulking analysis 3.1.19  
C  
  
cloud map 2.4.18  
coefficient of linear thermal expansion 3.3.6  
computer aided engineering 2.1.1  
constraint 2.2.11  
concentrated load 2.2.15  
convergence tolerance 2.2.23  
contact element 2.3.9  
critical damping ratio 3.2.6  
curse of time history 2.4.16  
D  
  
damping 3.2.5  
deformation 2.4.8  
degree of freedom 2.2.10  
design model 2.1.15  
design variable 3.5.3  
direct coupling method 3.4.6  
displacement 2.2.12  
E  
  
elastic strain 2.4.14  
element 2.1.4  
element attribute 2.2.9  
element order 2.3.2  
element stress 2.4.4  
element stiffness 3.1.7  
element freedom 3.1.10  
electrostatic field 3.4.7

equivalent stress 2.4.7  
equivalent strain 2.4.13  
excitation 3.2.13  
F  
fluid-solid coupling 3.4.2  
finite element method 2.1.2  
finite element analysis 2.1.3  
finite element model 2.2.3  
finite element modeling 2.2.4  
frequency-domain analysis 3.2.3  
G  
general kinematics equation 2.1.9  
geometry nonlinearity 3.1.18  
H  
harmony response analysis 3.2.9  
heat flow rate 3.3.5  
heat flux density 3.3.7  
I  
ideal model 2.2.2  
internal force 2.2.19  
inertial force 2.2.20  
isoparametric element 2.3.3  
isoline map 2.4.17  
L  
line load 2.2.16  
load 2.2.14  
load step 2.2.21  
load substep 2.2.22  
M  
magnetism-solid coupling 3.4.3  
material property 2.2.8  
material nonlinearity 3.1.17  
mass element 2.3.11  
modal 3.2.1  
modal analysis 3.2.8  
modal superposition 3.2.12

## N

node ..... 2.1.5  
node freedom ..... 3.1.9  
node stress ..... 2.4.5  
node displacement ..... 2.2.13  
nonlinear static analysis ..... 3.1.15  
normal strain ..... 2.4.10  
normal stress ..... 2.4.2  
  
O  
  
objective function ..... 3.5.2  
one dimensional element ..... 2.3.6  
optimal design ..... 2.1.14  
  
P  
  
parameter model ..... 3.5.1  
plastic strain ..... 2.4.15  
plane & shell ..... 3.1.4  
plane stress problem ..... 3.1.12  
plane strain problem ..... 3.1.13  
preprocessing ..... 2.1.6  
post-processing ..... 2.1.8  
principal stress ..... 2.4.6  
principal strain ..... 2.4.12  
  
R  
  
real constant ..... 2.3.12  
reliability optimization ..... 3.5.6  
resonance ..... 3.2.14  
  
S  
  
sequential coupling method ..... 3.4.5  
simplified model ..... 2.2.1  
shape function ..... 2.3.1  
shear strain ..... 2.4.11  
shear stress ..... 2.4.3  
solve ..... 2.1.7  
spring element ..... 2.3.10  
spectrum ..... 3.2.4  
spectrum analysis ..... 3.2.11  
stability ..... 3.1.8  
state nonlinearity ..... 3.1.16

state variable ..... 3.5.4  
strength ..... 3.1.5  
stiffness ..... 3.1.6  
structural statics analysis ..... 2.1.10  
structural dynamics analysis ..... 2.1.11  
structural thermal analysis ..... 2.1.12  
structural coupling analysis ..... 2.1.13  
structure freedom ..... 3.1.11  
structural damping ..... 3.2.7  
stress ..... 2.4.1  
stress concentration ..... 2.4.20  
strain ..... 2.4.9  
steady-state thermal analysis ..... 3.3.1  
stimulus ..... 3.2.13  
surface load ..... 2.2.17  
super-parametric element ..... 2.3.4  
sub-parametric element ..... 2.3.5  
T  
three dimensional element ..... 2.3.8  
thermal-stress analysis ..... 3.3.3  
thermal load ..... 3.3.4  
thermo-solid coupling ..... 3.4.1  
thermo-fluid-solid coupling ..... 3.4.4  
topological optimization ..... 3.5.5  
truss ..... 3.1.2  
time-domain analysis ..... 3.2.2  
transient dynamic analysis ..... 3.2.10  
transient thermal analysis ..... 3.3.2  
two dimensional element ..... 2.3.7  
V  
vector map ..... 2.4.19  
W  
working conditions ..... 2.2.6