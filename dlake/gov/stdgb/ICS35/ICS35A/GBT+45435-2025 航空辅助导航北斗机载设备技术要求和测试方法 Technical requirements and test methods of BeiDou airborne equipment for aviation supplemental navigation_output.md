

# 中华人民共和国国家标准

GB/T 45435—2025

# 航空辅助导航北斗机载设备技术要求和测试方法

# Technical requirements and test methods of BeiDou airborne equipment for aviation supplemental navigation

2025-03-28 发布

2025-03-28 实施

国家市场监督管理总局  

国家标准化管理委员会  

发布



## 目次

前言 …… III    
引言 …… IV    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语、定义和缩略语 …… 1    
3.1 术语和定义 …… 1    
3.2 缩略语 …… 2    
4 系统组成 …… 2    
5 要求 …… 3    
5.1 功能要求 …… 3    
5.2 性能要求 …… 3    
5.3 接口要求 …… 5    
5.4 可靠性 …… 5    
6 测试方法 …… 5    
6.1 测试环境 …… 5    
6.2 测试设备 …… 6    
6.3 测试项目 …… 6    
6.4 功能测试 …… 7    
6.5 性能测试 …… 9    
6.6 接口测试 …… 21    
6.7 可靠性测试 …… 21    
附录 A（规范性） 标准接收信号和干扰环境 …… 22    
附录 B（规范性） 定位精度分析方法 …… 26    
附录 C（规范性） 一般最小二乘解和对流层修正算法中的权重 …… 27    
附录 D（规范性） 接收机自主完好性方法 …… 31    
参考文献 …… 33



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由中央军委装备发展部提出。

本文件由全国卫星导航标准化技术委员会(SAC/TC 544)归口。

本文件起草单位:航天恒星科技有限公司、中国商飞北京民用飞机技术研究中心、中国民航大学、中国卫星导航工程中心、中国航天标准化研究所。

本文件主要起草人：周中华、岳富占、张展、马振洋、刘莹、李泽明、蒋可心、孟斌、李申阳、李铁帅、金志威、王维嘉、王鹏、朱兵。

## 引言

航空辅助导航北斗机载设备，是根据民用航空行业用户在运输飞机、通航飞机使用北斗卫星导航系统B1C频点进行辅助导航的实际应用需求，为目标飞行器在航路阶段使用的机载专用型终端。

本文件中规定的北斗机载设备预期为其他机载终端设备提供位置/速度/时间（PVT）等信息，因功能失效而引起错误性信息为轻微失效状态，功能丧失为无安全影响失效状态。

北斗机载导航设备参考我国民航的相关技术标准规定，一般将北斗机载设备分为两种类型，分别为Beta类设备和Gamma类设备，其中Beta类设备由独立的北斗机载设备构成，该类设备预期为其他终端设备提供位置/速度/时间（PVT）等信息，Beta类设备因功能失效而引起错误性信息为轻微失效状态，功能丧失为无安全影响失效状态；Gamma类设备由北斗机载设备和显控装置构成，并具备航路导航能力和显示功能的设备，Gamma类设备没有标准的最低失效状态类别。在设备设计时记录其功能丧失和故障的失效状态类别。

为了保持航空辅助导航北斗机载设备与民航相关标准的符合性，本文件中关于北斗机载设备的功能要求、性能要求与Beta类设备保持一致，并适用于在民用航空器上使用。

# 航空辅助导航北斗机载设备技术要求和测试方法

## 1 范围

本文件规定了使用北斗 B1C 信号的航空辅助导航北斗机载设备的技术要求，描述了相应测试方法。

本文件适用于航空辅助导航北斗机载设备（以下简称北斗机载设备）的研制、生产、测试和验收。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 5080.7 设备可靠性试验 恒定失效率假设下的失效率与平均无故障时间的验证试验方案

GB/T 39267 北斗卫星导航术语

GB/T 39413 北斗卫星导航系统信号模拟器性能要求及测试方法

GB/T 39414.1—2020 北斗卫星导航系统空间信号接口规范 第1部分：公开服务信号 B1C

## 3 术语、定义和缩略语

### 3.1 术语和定义

GB/T 39267 界定的以及下列术语和定义适用于本文件。

3.1.1

## 告警时间 time to alert

从定位故障开始时刻到设备发出告警时刻所经历的时间。

[来源:GB/T 42833—2023,3.1.22]

3.1.2

## 定位失效 positioning failure

真实位置与定位解算值之间的差异超过相应的水平保护级。

#### 3.1.3 

水平品质因数 horizontal figure of merit; HFOM

以真实位置为中心，以95%概率包含水平定位位置的圆形水平区域的半径。

3.1.4

水平排除级别 horizontal exclusion level; HEL

在故障检测及排除功能可用时，以真实位置为中心且满足漏警及排除失败要求的圆的半径。

GB/T 45435—2025

#### 3.1.5 

## 漏警 missed alert

定位失效发生但在要求的告警时间内没有指示告警。

#### 3.1.6 

## 虚警 false alert

定位失效未发生却指示告警。

### 3.2 缩略语

下列缩略语适用于本文件。

BDS: 北斗卫星导航系统(BeiDou Navigation Satellite System)

CW: 连续波 (Continuous Wave)

FD: 故障检测(Fault Detection)

FDE: 故障检测与排除(Fault Detection and Exclusion)

GDOP: 几何精度因子(Geometric Dilution of Precision)

GNSS: 全球卫星导航系统 (Global Navigation Satellite System)

HAL: 水平告警限值 (Horizontal Alert Limit)

HDOP: 水平精度因子 (Horizontal Dilution of Precision)

HPL: 水平保护级(Horizontal Protection Level)

MSL: 平均海平面 (Mean Sea Level)

MTBF: 平均故障间隔时间(Mean Time Between Failure)

MTTR: 平均修复时间 (Mean Time to Repair)

PRN:伪随机噪声码(Pseudo-Random Noise)

RAIM: 接收机自主完好性监测 (Receiver Autonomous Integrity Monitoring)

SISA: 空间信号精度 (Singal in Space Accuracy)

SISAI: 空间信号精度指数 (Singal in Space Accuracy Index)

## 4 系统组成

航空辅助导航北斗机载系统作为选装系统，仅用于在航路阶段提供基于北斗的备份导航信息显示，系统不向已有机载系统输出信号，本系统因功能失效而引起错误性信息为轻微失效状态，功能丧失为无安全影响失效状态。

航空辅助导航北斗机载系统通常由天线、北斗机载设备和显控装置三部分组成，如图1所示。本文件主要涉及北斗机载设备的技术要求和测试方法。

<div style="text-align: center;"><img src="imgs/img_in_image_box_241_193_961_478.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">图 1 航空辅助导航北斗机载系统组成框图</div>


## 5 要求

### 5.1 功能要求

#### 5.1.1 基本功能

北斗机载设备应具备独立接收和使用北斗 B1C 信号进行工作的能力，至少应能输出时间、位置、速度、HFOM 和 HPL 等。北斗公开服务信号 B1C 信号的接口要求符合 GB/T 39414.1—2020 的规定。

#### 5.1.2 自检功能

北斗机载设备应具备自检功能，当设备发生故障时能通过指示灯或其他方式进行故障指示。

#### 5.1.3 卫星选择功能

北斗机载设备应具有以下能力：

a）识别卫星健康状态，能指示每颗北斗卫星/信号是“健康的”“不健康的”或是“边缘的”；

b）能自动选择健康的北斗卫星/信号用于位置解算和完好性计算；

c） 能使用同一组卫星进行位置解算和完好性监测；

d）当选择卫星组发生改变时，能在5.2.4规定的告警时间内完成更改。

#### 5.1.4 导航告警

北斗机载设备应在下列任何情况出现后1 s内提供导航能力丧失的告警指示：

a） 设备故障；

b）由于可用卫星数量不足（小于4颗），导致持续5 s或更长的时间无法进行定位解算；

c）由于可用卫星数量不足(小于6颗)，导致完好性无法剔除检测到的故障卫星；

d）FDE 未在 8 s 内排除检测到的故障。

在上述情况终止后，设备应能立即恢复正常运行状态。

### 5.2 性能要求

#### 5.2.1 定位精度

水平定位精度应优于  $ 23 \, m $  (95% 置信度)。

#### 5.2.2 捕获时间

##### 5.2.2.1 初始捕获时间

在没有时间、位置和历书数据等信息的情况下，设备从上电到输出第一次有效位置（定位精度和完好性均满足要求）的时间间隔应不超过300 s。

##### 5.2.2.2 卫星捕获时间

在持续输出有效位置  $ 60 \, s $  后，设备应能在  $ 62 \, s $  内将新的北斗卫星信号并入定位解算，并输出有效位置。

##### 5.2.2.3 卫星重捕获时间

当卫星信号中断时间 $ \leqslant30\ s $  且其余卫星的GDOP $ \leqslant6 $  时，设备应在重新接收到该卫星信号后的20 s 内重新捕获该卫星。

#### 5.2.3 灵敏度和动态范围

本条规定了使用有源天线的相关要求，有源天线包含一个前置放大器和无源天线。灵敏度和动态范围应在图1规定的天线端口处测量，要求为：

a）捕获灵敏度应优于-134.5 dBm；

b）可接收北斗 B1C 卫星信号的功率范围至少为  $ \left[-134.5\ dBm, -118.5\ dBm\right] $ 。

注：天线制造商需在天线安装说明中对前置放大器的最小和最大增益以及相应的最小和最大安装损耗进行定义。

#### 5.2.4 完好性

##### 5.2.4.1 阶跃

北斗机载设备应能检测出任何用于定位解算的卫星上的大于  $ 700 \, m $  的伪距阶跃跳变，包括能造成小于  $ 10 \, s $  失锁的阶跃跳变。

##### 5.2.4.2 由 FDE 提供的完好性

在航路/洋区飞行阶段，完好性要求应按表1的规定。

<div style="text-align: center;">表 1 完好性性能要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>飞行阶段</td><td style='text-align: center;'>水平告警限值</td><td style='text-align: center;'>虚警率</td><td style='text-align: center;'>告警时间</td><td style='text-align: center;'>漏警率</td><td style='text-align: center;'>排除失败率</td><td style='text-align: center;'>检测可用性</td><td style='text-align: center;'>排除可用性</td></tr><tr><td style='text-align: center;'>航路/洋区</td><td style='text-align: center;'>2.0 nm</td><td style='text-align: center;'>$ 3.33 \times 10^{-7} $ /采样</td><td style='text-align: center;'>8 s</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>99.95%</td><td style='text-align: center;'>99.30%</td></tr></table>

##### 5.2.4.3 存在干扰时的完好性

当干扰信号功率高于附录 A 中的要求时，对于可能输出误导信息的情况，设备应在告警时间内提供相应的完好性保障。当干扰信号恢复到附录 A 中要求且满足初始捕获条件时，设备应在 300 s 内自动恢复到稳态运行状态。

#### 5.2.5 动态性能

##### 5.2.5.1 正常机动

当航空器在进行正常机动时，设备应满足本文件规定的精度要求、卫星捕获时间要求和卫星重捕获要求，航空器正常机动条件下的动态要求应按表2的规定。

<div style="text-align: center;">表 2 正常飞行动态要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>最大地速</td><td style='text-align: center;'>最大水平加速度</td><td style='text-align: center;'>最大垂直加速度</td><td style='text-align: center;'>最大加加速度</td></tr><tr><td style='text-align: center;'>取值</td><td style='text-align: center;'>800 kt</td><td style='text-align: center;'>0.58g</td><td style='text-align: center;'>0.5g</td><td style='text-align: center;'>0.25g/s</td></tr><tr><td colspan="5">注: 1 kt(节) = 1 n mile/h = 0.514 444 m/s, 重力加速度 g = 9.8 m/s²。</td></tr></table>

##### 5.2.5.2 异常机动

在异常机动情况下，设备应不输出误导性信息，定位和完好性监测功能按规定运行。当航空器从异常机动恢复到正常机动时，北斗机载设备满足本文件规定的卫星重捕要求。航空器异常机动条件下的动态要求应按表3的规定。

<div style="text-align: center;">表 3 异常飞行动态要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>最大地速</td><td style='text-align: center;'>最大水平加速度</td><td style='text-align: center;'>最大垂直加速度</td><td style='text-align: center;'>最大加加速度</td></tr><tr><td style='text-align: center;'>取值</td><td style='text-align: center;'>800 kt</td><td style='text-align: center;'>2g</td><td style='text-align: center;'>1.5g</td><td style='text-align: center;'>0.74g/s</td></tr><tr><td colspan="5">注: 1 kt(节) = 1 n mile/h = 0.514 444 m/s, 重力加速度 g = 9.8 m/s $ ^{2} $ 。</td></tr></table>

#### 5.2.6 位置数据输出更新率

位置数据输出的最小更新率应为  $ 1 \, Hz $ 。

### 5.3 接口要求

北斗机载设备接口要求应按如下规定：

a）北斗机载设备具有串行通信接口 RS-232、RS-422、RS-485、ARINC429 总线接口、USB 接口或网络接口等的一种或多种通用通信接口；

b) 机载天线与北斗机载设备射频接口通过同轴型  $ 50 \Omega $  的电连接器连接。

### 5.4 可靠性

设备应符合预期航空平台的使用要求，其可靠性至少应满足以下要求：

a） 平均故障间隔时间(MTBF):  $ \geq $ 2 000 h;

b) 平均修复时间（MTTR） $ \leq $ 20 min。

## 6 测试方法

### 6.1 测试环境

除另有规定外，按照下列试验环境进行试验。

a） 温度： $ 15^{\circ}C \sim 35^{\circ}C $ 

b）相对湿度：20%~80%。

c）气压：86 kPa～106 kPa。

### 6.2 测试设备

北斗机载设备测试设备具体要求如下，测试仪器见表4。

a）测试用仪器设备经过计量部门检定合格，并在有效期内。

b）测试用仪器、设备有足够的分辨力、准确度和稳定性，其性能应满足被测性能指标的要求。其精度至少高于被测指标精度的三分之一。

<div style="text-align: center;">表 4 测试仪器</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>仪器名称</td><td style='text-align: center;'>仪器性能指标要求</td><td style='text-align: center;'>数量</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>GNSS模拟器</td><td style='text-align: center;'>a) 能模拟北斗B1C公开服务信号；b) 能完成卫星星座仿真、大气传播仿真、用户轨迹仿真、多径仿真和特殊事件仿真(卫星故障、卫星伪距跳变)；c) 信号通道数≥12；d) 速度分辨力：≤0.01m/s；e) 最大速度：≥8000m/s；f) 最大加速度：≥900m/s²；g) 最大加速度分辨力：≤0.01m/s²；h) 最大加速度：≥900m/s²；i) 伪距误差：≤0.05m；j) 其他指标要求按GB/T39413</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>干扰信号源</td><td style='text-align: center;'>a) 频率范围：至少支持1GHz～2GHz；b) 最小信号频率分辨率优于20kHz，输出功率至少支持20dBm，最小输出功率分辨率优于0.1dB；c) 频率稳定度优于5×10⁻⁷；d) 能模拟连续波干扰、脉冲干扰和外部宽带干扰噪声</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>合路器</td><td style='text-align: center;'>a) 频率：至少支持1GHz～2GHz；b) 阻抗：50Ω；c) 插损：≤3.5dB；d) 驻波：≤2.0；e) 相位平衡度：≤5°；f) 幅度平衡度：≤0.3dB</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>低噪声放大器</td><td style='text-align: center;'>a) 频率：至少支持1575.42MHz±16MHz；b) 阻抗：50Ω；c) 增益：≥26.5dB</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>数据分析设备</td><td style='text-align: center;'>能对北斗机载设备输出数据进行统计、分析和存储的设备</td><td style='text-align: center;'>1</td></tr></table>

### 6.3 测试项目

北斗机载设备测试项目如表5所示，室内GNSS模拟器和信号干扰源测试环境见图2。

<div style="text-align: center;">表 5 测试项目索引</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>测试项目</td><td style='text-align: center;'>要求章条号</td><td style='text-align: center;'>测试方法章条号</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>基本功能</td><td style='text-align: center;'>5.1.1</td><td style='text-align: center;'>6.4.1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>自检功能</td><td style='text-align: center;'>5.1.2</td><td style='text-align: center;'>6.4.2</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>卫星选择功能</td><td style='text-align: center;'>5.1.3</td><td style='text-align: center;'>6.4.3</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>导航告警</td><td style='text-align: center;'>5.1.4</td><td style='text-align: center;'>6.4.4</td></tr><tr><td rowspan="2">5</td><td rowspan="2">定位精度</td><td rowspan="2">5.2.1</td><td style='text-align: center;'>6.5.1</td></tr><tr><td style='text-align: center;'>6.5.2</td></tr><tr><td rowspan="2">6</td><td rowspan="2">初始捕获时间</td><td rowspan="2">5.2.2.1</td><td style='text-align: center;'>6.5.3</td></tr><tr><td style='text-align: center;'>6.5.4</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>卫星捕获时间</td><td style='text-align: center;'>5.2.2.2</td><td style='text-align: center;'>6.5.5</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>卫星重捕获时间</td><td style='text-align: center;'>5.2.2.3</td><td style='text-align: center;'>6.5.6</td></tr><tr><td rowspan="4">9</td><td rowspan="4">灵敏度和动态范围</td><td rowspan="4">5.2.3</td><td style='text-align: center;'>6.5.3</td></tr><tr><td style='text-align: center;'>6.5.4</td></tr><tr><td style='text-align: center;'>6.5.6</td></tr><tr><td style='text-align: center;'>6.5.9</td></tr><tr><td rowspan="2">10</td><td rowspan="2">完好性</td><td rowspan="2">5.2.4</td><td style='text-align: center;'>6.5.7</td></tr><tr><td style='text-align: center;'>6.5.8</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>动态性能</td><td style='text-align: center;'>5.2.5</td><td style='text-align: center;'>6.5.9</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>位置数据输出更新率</td><td style='text-align: center;'>5.2.6</td><td style='text-align: center;'>6.5.10</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>接口要求</td><td style='text-align: center;'>5.3</td><td style='text-align: center;'>6.6</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>可靠性</td><td style='text-align: center;'>5.4</td><td style='text-align: center;'>6.7</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_1088_894_1283.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 2 室内 GNSS 模拟器和信号干扰源测试环境框图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_366_1350_405_1383.jpg" alt="Image" width="3%" /></div>


### 6.4 功能测试

#### 6.4.1 基本功能测试

基本功能测试可验证北斗机载设备是否具备独立接收和使用北斗 B1C 信号进行工作的能力。测试步骤为：

a）按图 2 连接测试设备；

b) 操作 GNSS 模拟器，设置满足 5.2.5.1 正常飞行动态要求的场景，输出北斗卫星导航系统 B1C 频点信号；

c) 北斗机载设备上电并正常工作，将时间、位置、速度、水平位置品质因数（HFOM）和水平保护级（HPL）等数据输出到数据分析设备上，检查是否符合5.1.1的要求。

#### 6.4.2 自检功能测试

自检功能用于检测北斗机载设备的硬件和软件是否存在异常或错误。

测试步骤为：

a）北斗机载设备加电；

b）根据被测设备的产品规范/使用说明书，检查其状态显示或指示是否正确。

#### 6.4.3 卫星选择功能测试

北斗机载设备应自动选择健康的卫星用于位置解算和完好性计算。

测试步骤为：

a）按图 2 连接测试设备；

b) 操作 GNSS 模拟器，设置相应的城市位置，并输出北斗卫星导航系统 B1C 频点信号；

c）北斗机载设备加电并正常工作，操作 GNSS 模拟器，模拟卫星电文出现下列情况，检查被测设备是否未选择下列情况的卫星用于定位解算。

1）1 bit 的“DIF”表示空间信号播发的电文参数误差超出播发的空间信号精度 SISA 值时；

2）空间信号精度指数 SISAI 值超出范围；

3）2 bit 的“HS”表示整星不健康时；

4）1 bit 的“SIF”表示信号不正常时。

#### 6.4.4 导航告警功能测试

导航告警功能用于检测设备的告警指示功能。

测试步骤为：

a）按图 2 连接测试设备；

b) 操作 GNSS 模拟器正常输出信号，播发 5 颗北斗卫星信号；

c) 被测设备加电并稳定工作后，确认北斗机载设备用于定位解算的卫星号，操作 GNSS 模拟器关闭其中两颗导航卫星并持续至少 5 s；

d) 检测被测设备是否在 1 s 内给出告警指示；

e) 操作 GNSS 模拟器正常输出信号，播发 5 颗北斗卫星信号；

f) 被测设备加电并稳定工作后，确认北斗机载设备用于定位解算的卫星号，操作 GNSS 模拟器使其中一颗导航卫星出现 700 m 阶跃故障；

g）检测被测设备是否在8 s内给出告警指示；

h）操作 GNSS 模拟器正常输出信号，播发至少 6 颗北斗卫星信号；

i) 待被测设备稳定工作后，确认设备用于定位解算的卫星号，然后操作 GNSS 模拟器使其中一颗导航卫星出现 700 m 阶跃故障；

i) 检测被测设备是否排除故障卫星并给出指示。

### 6.5 性能测试

#### 6.5.1 定位精度测试

##### 6.5.1.1 测试目的

定位精度测试的目的是验证设备在规定的条件下是否满足5.2.1定位精度的要求。

##### 6.5.1.2 测试场景

精度测试框图见图 2。信号模拟器及其干扰条件要求如下。

a）对于所有测试场景，应模拟宽带 GNSS 测试噪声 $ (I_{\mathrm{GNSS,Test}}) $ 和热噪声 $ (N_{\mathrm{sky,antenna}}) $ 。干扰测试场景共有三组：宽带外部干扰噪声、连续波干扰和脉冲干扰：

1）天线端口处的宽带外部干扰噪声 $ (IE_{xt,Test}) $ 的功率谱密度等于-170.5 dBm/Hz;

2）连续波干扰 CW 功率和频率见表 6；

3）对于脉冲干扰测试，使用1 575.42 MHz的脉冲调制载波，信号带宽为1 MHz，峰值载波功率为+10 dBm，脉冲宽度为125  $ \mu $ s，占空比为1%。

b) 宽带 GNSS 测试噪声 $ (I_{\mathrm{GNSS,Test}}) $ ：在天线端口处功率谱密度等于 -172.3 dBm/Hz，该噪声密度已去除模拟卫星的贡献。

c) 热( $ N_{sky,antenna} $ )噪声：-172.5 dBm/Hz。

d）信号模拟器播发场景：按照公认模型提供对流层、电离层等相关信息，HDOP≤4，设置一颗卫星为最大功率-118.5 dBm，一颗卫星为最小功率-134.5 dBm，其余卫星为-131.5 dBm。

e）动态场景：恒速 800 kt，从 5 000 ft(MSL) 开始，执行  $ 3^{\circ} $  的爬升。

注：1 ft=0.304 8 m。

<div style="text-align: center;">表 6 稳态精度测试 CW 连续波功率和频率</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>频率/MHz</td><td style='text-align: center;'>功率/dBm</td><td style='text-align: center;'>干信比/dB</td></tr><tr><td style='text-align: center;'>1 525.0</td><td style='text-align: center;'>-12.0</td><td style='text-align: center;'>122.0</td></tr><tr><td style='text-align: center;'>1 555.42</td><td style='text-align: center;'>-89.5</td><td style='text-align: center;'>44.5</td></tr><tr><td style='text-align: center;'>1 575.42a</td><td style='text-align: center;'>-120.5</td><td style='text-align: center;'>13.5</td></tr><tr><td style='text-align: center;'>1 595.42</td><td style='text-align: center;'>-89.5</td><td style='text-align: center;'>44.5</td></tr><tr><td style='text-align: center;'>1 610.0</td><td style='text-align: center;'>-30</td><td style='text-align: center;'>104.0</td></tr><tr><td style='text-align: center;'>1 618.0</td><td style='text-align: center;'>-12</td><td style='text-align: center;'>122.0</td></tr><tr><td style='text-align: center;'>1 626.0b</td><td style='text-align: center;'>8</td><td style='text-align: center;'>142.0</td></tr><tr><td colspan="3">注: 表中规定了天线端口的连续波干扰(CWI)功率。</td></tr><tr><td colspan="3">a CWI 应与提供的卫星信号同步。但在整个试验过程中, 应保持精确的频率关系。b 仅适用于装配有卫星通信(SATCOM)的飞机。</td></tr></table>

##### 6.5.1.3 测试步骤

精度测试步骤如下所示：

a）按图 2 连接测试设备；

b）北斗机载设备加电正常工作，并获得被测场景的有效历书；

c）北斗机载设备进入稳定工作状态后，将干扰施加于被测设备，且将信号和干扰功率调至要求的电平；

d）被测设备稳定工作后，将时间、位置、速度、HFOM 和 HPL 等数据输出至数据分析设备上并进行存储；

e） 被测设备采集 30 min 数据后，将设备断电；

f） 分析其精度和完好性数据是否满足要求。

##### 6.5.1.4 测试判据

定位精度满足 5.2.1 定位精度要求，完好性数据满足 5.2.4 完好性要求。

#### 6.5.2 基于真实卫星信号的  $ 7 \times 24 $  h 精度测试

##### 6.5.2.1 测试目的

基于真实卫星信号的  $ 7 \times 24 $  h 精度测试用于评估北斗机载设备静态定位精度和长时间的连续工作稳定性。

##### 6.5.2.2 测试场景

基于真实卫星信号的  $ 7 \times 24 $  h 精度测试框图见图 3。

<div style="text-align: center;"><img src="imgs/img_in_image_box_333_737_838_972.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图 3 真实卫星信号的  $ 7 \times 24 $  h 精度测试框图</div>


##### 6.5.2.3 测试步骤

 $ 7 \times 24 $  h 精度测试步骤如下所示：

a）将天线部署于室外位置已知的标准点，从天线顶到水平面以上 $ 10^{\circ} $ 的仰角空间范围内对卫星的视野清晰，且天线周围200 m无大功率无线电发射源；

b) 按图 3 连接测试设备；

c） 被测设备正常工作，并将时间、位置、速度、HFOM 和 HPL 等数据输出到数据分析设备上进行存储；

d）分析被测设备  $ 7 \times 24 $  h 的测试数据，检查其精度和完好性是否满足要求。

##### 6.5.2.4 测试判据

定位精度满足 5.2.1 定位精度要求，完好性数据满足 5.2.4 完好性要求。

#### 6.5.3 初始捕获时间测试

##### 6.5.3.1 测试目的

用于验证北斗机载设备存在干扰情况下的卫星初始捕获能力。

##### 6.5.3.2 测试场景

初始捕获测试框图见图 2。信号模拟器及其干扰条件要求如下。

a）5 颗北斗卫星发射的 B1C 信号。

b) 宽带 GNSS 测试噪声 $ (I_{\mathrm{GNSS,Test}}) $ ：在天线端口处功率谱密度等于 -172.3 dBm/Hz，该噪声密度已去除模拟卫星的贡献。

c) 宽带外界干扰噪声( $ IE_{xt,Test} $ ): 在天线端口功率谱密度等于-176.5 dBm/Hz。

d）热噪声 $ (N_{\text{sky,antenna}}) $ : -172.5 dBm/Hz。

e) 一颗卫星为最大功率 -118.5  dBm，一颗卫星为最小功率 -134.5  dBm，其余卫星为 -131.5  dBm。

f) 平台动态：恒速 800 kt，从 5 000 ft(MSL) 开始，执行  $ 3^{\circ} $  的爬升。

##### 6.5.3.3 测试步骤

初始捕获时间测试步骤如下：

a）按图 2 连接测试设备；

b) 操作 GNSS 模拟器和信号干扰源，模拟宽带 GNSS 测试噪声，宽带外界干扰噪声和热噪声；

c) 被测设备上电并初始化到相对于信号模拟器的起始位置总径向误差等于  $ 60 \, n mile $  的位置，同时相对于信号模拟器的时间基准时间误差在  $ 1 \, min $  内 ( $ 60 \, s $ )。被测设备需在进行测试之前获得有效历书；

d) 检查北斗机载设备从上电开始到输出第一个有效位置(HPL可用)的时间是否满足要求，并记录接下来至少60 s的连续定位（至少60个数据点）数据，分析测试数据并检查定位精度是否满足要求；

e）在每次测试后清除设备的星历或使其无效；

f）转到步骤b)，按附录B中表B.1要求重复。

##### 6.5.3.4 测试判据

初始捕获时间应满足 5.2.2.1 的要求，定位精度应满足 5.2.1 的要求。

#### 6.5.4 异常干扰后的初始捕获时间测试

##### 6.5.4.1 测试目的

用于验证北斗机载设备在异常干扰情况下的卫星初始捕获能力。

##### 6.5.4.2 测试场景

异常干扰后的初始捕获时间测试框图见图2。信号模拟器及其干扰条件要求如下。

a）5 颗北斗卫星发射的 B1C 信号。

b) 宽带 GNSS 测试噪声 $ (I_{\mathrm{GNSS,Test}}) $ ：在天线端口处功率谱密度等于 -172.3 dBm/Hz，该噪声密度已去除模拟卫星的贡献。

c) 宽带外界干扰噪声( $ IE_{xt,Test} $ ): 在天线端口功率谱密度等于-176.5 dBm/Hz。

d）热噪声 $ (N_{\text{sky,antenna}}) $ : -172.5 dBm/Hz。

e）信号模拟器播发场景：卫星 HDOP 值  $ \leqslant 4 $ ，一颗卫星为最大功率 -118.5 dBm，一颗卫星为最小功率 -134.5 dBm，其余卫星为 -131.5 dBm。

f) 平台动态: 恒速 800 kt, 在恒定的高度上。

g）被测设备上电或信号模拟器开始运行之前，GNSS 和外部干扰应施加到被测设备上。

##### 6.5.4.3 测试步骤

异常干扰后的初始捕获时间测试步骤如下。

a）按图 2 连接测试设备。

b）操作 GNSS 模拟器和信号干扰源，模拟宽带 GNSS 测试噪声，宽带外界干扰噪声和热噪声，设置异常 CW 干扰频率为 1575.42 MHz。

c) 被测设备上电并初始化到相对于信号模拟器的起始位置总径向误差等于  $ 60 \, n mile $  的位置，同时相对于信号模拟器的时间基准时间误差在  $ 1 \, min $  内（ $ 60 \, s $ ）。被测设备需在测试之前获得有效历书。

d）在北斗机载设备输出有效位置1 min前，可将模拟器输出卫星信号功率调高，或将宽带噪声调低。

e）在北斗机载设备连续1 min输出有效位置之后，施加异常连续波干扰。在第一轮测试中，施加1 min后去除异常干扰；第二轮试验施加2 min，以此类推，第十轮试验施加10 min。测试过程中设备无需清除星历数据。

f) 检查北斗机载设备从异常 CW 干扰消除到输出第一个有效位置（定位精度和完好性满足要求）的时间是否满足要求，并记录接下来至少 60 s 的连续定位（至少 60 个数据点）数据，分析测试数据并检查定位精度是否满足要求。

g）在(重复)试验之间重新初始化时，不需要清除星历数据。

h）转到步骤b)，按附录B中表B.1要求重复。

##### 6.5.4.4 测试判据

异常干扰后的初始捕获时间应满足5.2.2.1的要求，定位精度应满足5.2.1的要求。

#### 6.5.5 卫星捕获时间测试

##### 6.5.5.1 测试目的

用于验证北斗机载设备在稳定定位情况下对新出现的卫星捕获能力。

##### 6.5.5.2 测试场景

卫星捕获时间测试框图见图 2。信号模拟器及其干扰条件要求如下。

a）宽带 GNSS 测试噪声 $ (I_{\mathrm{GNSS,Test}}) $ ：在天线端口处功率谱密度等于 -172.3 dBm/Hz，该噪声密度已去除模拟卫星的贡献。

b) 热噪声(Nsky,antenna): -172.5 dBm/Hz.

c) 宽带外界干扰噪声 $ (IE_{\mathrm{xt,Test}}) $ ：在天线端口功率谱密度等于-170.5 dBm/Hz。

d）平台动态：恒速800 kt，从5 000 ft（平均海平面MSL）开始并执行3°爬升。

e）任意数量的任意功率的北斗卫星，直到被测设备进入稳定导航模式。

f) 一颗卫星为最大功率 -118.5  dBm，一颗卫星为最小功率 -134.5  dBm，其余卫星为 -131.5  dBm。

g）以最小功率开启新增的待捕获北斗卫星信号。

##### 6.5.5.3 测试步骤

卫星捕获时间测试步骤为：

a）按图 2 连接测试设备；

b）操作 GNSS 模拟器和信号干扰源，模拟宽带 GNSS 测试噪声，宽带外界干扰噪声和热噪声；

c) 被测设备上电。北斗机载设备需在进行测试之前获得对仿真器场景有效的历书用以测试；

d）在打开待捕获的卫星之前，被测设备应处于稳态导航，一旦进入稳态导航，仿真卫星和宽带噪声应被置为相应的稳态功率电平；

e） GNSS 信号模拟器上播发新增的待捕获卫星信号；

f) 记录从待测卫星信号播发到卫星被加入定位解算并输出第一个有效位置的时间，并记录接下来至少 60 s 的定位结果，分析定位精度是否要求；

g）重置场景（包括信号和噪声功率电平），转到步骤b)，按附录B中表B.1要求重复测试。

##### 6.5.5.4 测试判据

卫星捕获时间应满足5.2.2.2的要求，定位精度应满足5.2.1的要求。

#### 6.5.6 卫星重捕获时间测试

##### 6.5.6.1 测试目的

用于验证北斗机载设备接收卫星信号中断后的重捕获能力。

##### 6.5.6.2 测试场景

卫星重捕获时间测试框图见图 2。信号模拟器及其干扰条件要求如下。

a）宽带 GNSS 测试噪声 $ (I_{\mathrm{GNSS,Test}}) $ ：在天线端口处功率谱密度等于 -172.3 dBm/Hz，该噪声密度已去除模拟卫星的贡献。

b) 热噪声(Nsky,antenna): -172.5 dBm/Hz.

c) 宽带外界干扰噪声( $ IE_{xt,Test} $ ): 在天线端口功率谱密度等于-170.5 dBm/Hz。

d）平台动态：恒速800 kt，从5 000 ft(MSL)开始并执行3°爬升。

e）任意数量的任意功率的北斗卫星，直到被测设备进入稳定导航模式。

f) 一颗卫星为最大功率 -118.5  dBm，一颗卫星为最小功率 -134.5  dBm，其余卫星为 -131.5  dBm。

##### 6.5.6.3 测试步骤

卫星重捕获时间测试步骤为如下。

a）按图 2 连接测试设备。

b）操作 GNSS 模拟器和信号干扰源，模拟宽带 GNSS 测试噪声，宽带外界干扰噪声和热噪声。

c）被测设备上电。北斗机载设备需在进行测试之前获得对仿真器场景有效的历书用以测试。

d）在打开或关闭待重捕的卫星之前，被测设备应处于正常定位状态。一旦进入稳态导航，设置仿真卫星和宽带噪声为相应的稳态功率电平。

e）在 GNSS 信号模拟器上关闭最小功率卫星信号（应确保剩余卫星  $ GDOP \leq 6 $ ），直到被测设备对这颗卫星的信号进入失锁状态，并将这颗卫星从定位解算中移除，然后在 30 s 内以最小功率重新播发这颗卫星信号。

f) 记录从待测卫星信号播发到卫星被加入定位解算并输出第一个有效位置的时间，并记录接下来至少60 s的定位结果，分析定位精度是否满足要求。

g）重置场景（包括信号和噪声功率电平），转到步骤b)，按附录B中表B.1要求重复测试。

##### 6.5.6.4 测试判据

卫星重捕获时间应满足 5.2.2.3 的要求，定位精度应满足 5.2.1 的要求。

#### 6.5.7 抗干扰能力测试

##### 6.5.7.1 测试目的

用于验证北斗机载设备在带内连续波干扰条件下的性能。

##### 6.5.7.2 测试场景

抗干扰测试框图见图 2。信号模拟器及其干扰条件应符合下列要求。

a）指定一颗仿真环境中的可见卫星为最小功率，其余处于高功率电平。

b）初始 CW 功率为 -120.5 dBm（在初始捕获期间可降低）。干信比将根据测试程序而变化。在整个测试过程中保持准确的频率关系。该场景包括最小功率的卫星。

注：此评估方法基于实现加权最小二乘定位算法且使用基线完好性算法。如果使用不同形式的定位或完好性方法，这种评估方法可能不合适。

##### 6.5.7.3 测试步骤

抗干扰测试步骤如下。

a）按图 2 连接测试设备。

b）操作 GNSS 模拟器和信号干扰源，打开 CW 干扰，在初始捕获期间的 CW 干扰功率应低于稳态运行时的功率。

c）被测设备上电。设备应在进行测试之前获得对仿真器场景有效的历书。

d）待被测设备进入稳定状态后，将 CW 干扰功率调整为 -120.5 dBm。

e）在被测设备精度达到稳态前，CW干扰功率保持不变。在此期间内应记录所有卫星的伪距测量和伪距有效性指示（例如，隔离位）。

f) 设置 CW 干扰信号的功率增加 1 dB 并保持 200 s。在此期间，记录所有卫星的伪距观测量和伪距有效性指示（例如，隔离位）。

g) 转到步骤 f) 并重复，直到最小功率卫星从导航解算中被排除。将 CW 干扰信号再增加 3 dB，并验证最小功率卫星仍能被排除。需要确保 PRN 24 被排除时的仰角始终大于卫星仰角。

##### 6.5.7.4 测试判据

对于每个采样点，当 PRN24 伪距有效时，使用公式(1)误差评估准则：

 $$ Z_{j}\leqslant\mathrm{TH}_{j} $$ 

其中：

 $$ \mathrm{T H}_{j}=5.33\times\left[\left(N_{j}-1\right)/N_{j}\right]\sigma_{\mathrm{n o i s e},\mathrm{P R N24},j} $$ 

 $$ Z_{j}=P R_{\mathrm{P R N24},j}-R_{\mathrm{P R N24},j}-(c\Delta t)_{j} $$ 

 $$ (c\Delta t)_{j}=(1/N_{j})\sum_{i=1}^{N_{j}}(PR_{i,j}-R_{i,j}) $$ 

式中：

 $ PR_{i,j} $  —— j 时刻 i 卫星的伪距；

 $ R_{i,j} $  ——j 时刻 i 卫星的真实距离（包括外推法）；

 $ N_{i} $  ——i 时刻的卫星个数；

 $ \sigma_{noise,i,j} $  ——设备输出或者等价值（按照附录 C 规定的方法），i 时刻 i 卫星的接收机噪声。

如果伪距误差 $ Z_{i} $ 在10 s告警时间内超过阈值TH，则测试失败。

#### 6.5.8 完好性测试

##### 6.5.8.1 测试目的

对北斗机载设备 RAIM 算法的测试评估包括阶跃检测测试、可用性测试、漏警和排除失败率测试、虚警率测试、在线行为测试五个测试。其中：

a）阶跃检测测试用于验证设备的完好性功能测试；

b) 可用性测试用于测试北斗星座在全球范围内进行故障检测可用性和故障排除可用性；

c) 漏警和排除失败率测试用于评估 RAIM 算法(计算方法按照附录 D)在有故障情况下的告警和排除情况；

d) 虚警率测试用于评估 RAIM 算法无故障情况下进行告警的概率是否满足要求；

e) 在线行为测试使用 GNSS 模拟器测试，用于检测设备中使用的 RAIM 算法与离线测试中使用的算法性能相同。

注：可用性测试、漏警和排除失败率测试、虚警率测试为离线软件训练模型测试。

##### 6.5.8.2 测试场景

阶跃检测测试需要在四个场景下完成。如果制造商通过检测能证明其设备的阶跃检测机制对阶跃类型（导航数据的变化或编码相位突然变化）不敏感，那么只有一种类型阶跃需要被测试，典型的卫星信号功率可在这些测试中使用。其测试框图见图4。

<div style="text-align: center;"><img src="imgs/img_in_image_box_368_841_836_1036.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">图 4 阶跃检测测试框图</div>


##### 6.5.8.3 阶跃检测测试

###### 6.5.8.3.1 不能执行排除能力的测试

####### 6.5.8.3.1.1 测试步骤

不能执行排除能力的测试连接框图见图4，测试步骤如下：

a） 设置 GNSS 模拟器仅播发 5 颗卫星并可见；

b）北斗机载设备使用5颗卫星定位解算并稳定工作；

c) 设置 GNSS 模拟器在北斗机载设备定位解算中使用的最难检测到的卫星上，通过改变卫星电文，模拟 700 m 的阶跃故障；

d）记录设备完好性输出数据，使用附录 B 中公式(B.1)分析定位精度；

e）重复步骤 a)～步骤 b);

f) 设置 GNSS 模拟器在北斗机载设备定位解算中使用的最难检测到的卫星上，通过改变卫星的码相位，模拟 700 m 的阶跃故障；

g）记录北斗机载设备完好性输出数据，使用附录 B 中公式(B.1)分析定位精度。

####### 6.5.8.3.1.2 测试判据

北斗机载设备通过该项测试，需要满足以下要求：

a）定位误差在整个测试中不超过200 m；

b）HPL 不可用，完好性监测指示失效。

注：通过改变广播星历数据引入一个阶跃时，伪距阶跃直到收到第二组广播星历之后才会发生。

###### 6.5.8.3.2 无干扰故障检测的测试

####### 6 \.5\.8\.3\.2\.1 测试步骤

无干扰故障检测的测试连接框图见图4，测试步骤如下：

a） 设置 GNSS 模拟器仅播发 5 颗卫星并可见；

b）设置北斗机载设备 HPL 小于 0.3 n mile，使用 5 颗卫星定位解算并稳定工作；

c) 设置 GNSS 模拟器在北斗机载设备定位解算中使用的最难检测到的卫星上，通过改变卫星伪距，模拟  $ 10 \, m/s $  的斜坡故障；

d） 记录北斗机载设备完好性输出数据。

####### 6.5.8.3.2.2 测试判据

北斗机载设备通过该项测试，满足以下要求：

a）在任何时候都不应有卫星被排除；

b）北斗机载设备应在定位故障发生后指示出定位故障，且该时间在告警时间范围之内。

###### 6.5.8.3.3 可执行排除能力的测试

####### 6 \.5\.8\.3\.3\.1 测试步骤

可执行排除能力的测试连接框图见图4，测试步骤如下：

a） GNSS 模拟器模拟 6 颗及以上卫星可见；

b) 设置北斗机载设备 HPL 小于 0.3 n mile，使用 6 颗及以上卫星定位解算并稳定工作；

c) 设置 GNSS 模拟器在北斗机载设备定位解算中使用的最难检测到的卫星上，通过改变卫星电文模拟 750 m 的阶跃故障；

d）记录北斗机载设备完好性输出数据，分析定位精度；

e) 重复步骤 a)～步骤 b) 测试；

f) 通过改变 GNSS 模拟器的码相位，模拟 750 m 的阶跃故障；

g）记录北斗机载设备完好性输出数据，分析定位精度。

####### 6.5.8.3.3.2 测试判据

北斗机载设备通过该项测试，满足以下要求：

a）应在引入伪距阶跃之后的 10 s 内将故障卫星从定位解算中移除；

b）定位误差在整个测试中不超过200 m；

c）HPL值发生变化。

注：通过改变广播星历数据引入一个阶跃时，伪距阶跃直到收到第二组广播星历之后才会发生。

###### 6.5.8.3.4 无干扰故障检测与排除的测试

####### 6.5.8.3.4.1 测试步骤

无干扰故障检测与排除的测试连接框图见图4，测试步骤如下：

a） GNSS 模拟器模拟 6 颗及以上卫星可见；

b) 设置北斗机载设备 HPL 小于 0.3 n mile，使用 6 颗及以上卫星定位解算并稳定工作；

c) 设置 GNSS 模拟器在北斗机载设备定位解算中使用的最难检测到的卫星上，通过改变卫星伪距，模拟  $ 10 \, m/s $  的斜坡故障；

d）记录完好性输出数据。

####### 6.5.8.3.4.2 测试判据

北斗机载设备通过该项测试，满足：排除功能应正常运行，能排除定位失效导致的错误。

##### 6.5.8.4 可用性测试

###### 6.5.8.4.1 测试步骤

针对不同的卫星星座几何分布，需要分别计算每个场景的检测和排除可用性，可用性测试采用离线模拟测试，具体测试步骤如下。

a）确定分析网格：从北纬 $ 0^{\circ} $ ～北纬 $ 90^{\circ} $ 共计2353个网格点。具体方法为纬度间隔三度采样一个点，每个纬度圈的点在经度上均匀分布，具体划分方法如公式(5)所示：

 $$  long_{-}step=\frac{360}{ROUND(\frac{360}{MIN[3/\cos(latitude),360]}} $$ 

b）根据北斗卫星运行一圈时间，确定从00:00:00～12:00:00采样 $ 7\times24 $  h，每5 min采样一次，共产生2016个时间点。

c）根据时间点和空间点，共产生4 743 648个测试场景。

d）对于确定场景，所有卫星对于航路水平告警限值和告警时间要求，检测功能满足漏警和虚警要求，检测功能定义为可用；同样，对于确定场景，RAIM算法满足排除失败要求，并防止定位故障或完好性监测功能丧失的迹象发生，排除功能定义为可用。按照检测功能可用和排除功能可用的定义，计算每个场景的检测和排除是否可用，并统计检测可用和排除可用的场景总数。

e）计算 RAIM 算法的检测可用性和排除可用性。检测功能可用性由检测可用场景总数  $ N_{d} $  确定，排除功能可用性由排除可用总数  $ N_{a} $  确定，具体如公式（6）和公式（7）所示：

 $$ N_{\mathrm{d}}/4\ 743\ 648 $$ 

 $$ N_{\mathrm{a}}/4\ 743\ 648 $$ 

式中：

 $ N_{d} $ ——规定检测可用总数；

 $ N_{a} $ ——规定排除可用总数。

###### 6.5.8.4.2 测试判据

设备通过该项测试，满足以下要求：

a）检测可用性≥99.95%；

b） 排除可用性≥99.30%。

##### 6.5.8.5 漏警和排除失败率测试

###### 6.5.8.5.1 测试步骤

漏警和排除失败率测试采用离线仿真测试，具体测试步骤如下。

a）设置采样间隔时间 1 s，同时为每颗卫星添加不同的噪声样本，并在每次测试中均生成新的噪声，噪声模型采用高斯分布模型；卫星几何分布位置固定，且卫星速度为 0，以保证 HPL 在测试过程中不会改变。

b）进行测试集合选择，在可用性测试中的4 743 648个场景中，根据计算的保护级选择测试集合1和测试集合2，共40个几何分布。其中集合1中的20个几何分布，HPLFD从0.1 nm到设备支持的最大HAL，近似均匀分布，用于测试漏警率和误警率，集合2中20个几何分布，HELFD从0.1 nm到设备支持的最大HAL，近似均匀分布，用于测试漏报、错误警报和失败排除。

c) 对于步骤 b) 中的 40 个几何分布，每一种分布引入速度为  $ 5 \, m/s $  的斜坡型故障。其中，集合 1 在最难探测的卫星中引入故障，集合 2 在最难排除的卫星中引入故障。

d）针对集合1，分别执行RAIM算法，直到以下三个条件中任意一个发生：

1）正确排除：位置误差超过  $ HPL_{FD} $  并在超过警报时间之前，故障的卫星被正确排除；

2）排除失败：检测到定位故障（故障无法排除导致的故障）输出导航警报；

3）漏警：在没有导航告警的情况下，位置误差超过 $ HPL_{FD} $ 的时间超过告警时间。

e）针对集合2，分别执行RAIM算法，直到以下三个条件中任意一个发生：

1）正确排除：当位置误差超过  $ HEL_{FD} $  的时间超过告警时间 8 s 之前，故障的卫星被正确排除；

2）排除失败：当位置误差超过  $ HEL_{FD} $  的时间超过最长告警时间 8 s，输出导航告警；

3）漏警：在没有导航告警的情况下，位置误差超过 $ HPL_{FD} $ 的时间超过告警时间8s。

f）对于上述 40 个几何分布，每一个几何分布需要进行 1 650 次离线试验，记录每次试验结果及定位跟踪和警报状态。

g）统计失败排除和漏警的次数，与通过测试标准对比，确定是否满足 RAIM 漏警率和失败排除率。

###### 6.5.8.5.2 测试判据

设备通过该项测试，满足以下要求：

a）集合1的每个卫星分布，漏警次数总数应小于或等于47；

b）集合2的每个卫星分布，失败排除和漏警次数总数应小于或等于47；

##### 6.5.8.6 虚警率测试

###### 6.5.8.6.1 快照算法虚警率测试

####### 6.5.8.6.1.1 测试步骤

快照型算法实现方法按照附录 D 进行，该方法适用于电离层误差或接收机噪声的单个样本以简单高斯分布建模的情况。采用离线仿真测试，具体测试步骤如下：

a） 虚警率测试使用漏警率测试中筛选出的 40 个几何分布集合，单个样本电离层误差或接收机噪声采用简单的高斯分布建模；

b）对于40个几何分布，每个几何分布模拟2 475 000次独立样本执行RAIM算法，记录每个分

布试验结果过及告警状态；

c）对于每个几何分布，统计虚警的数量，确定 RAIM 算法是否满足虚警率要求。

####### 6.5.8.6.1.2 测试判据

北斗机载设备通过该项测试，满足以下要求：

a）所有可接受的几何分布上的告警数应 $ \leqslant47 $ ；

b）对于每个几何分布上的告警数应 $ \leqslant3 $ 。

###### 6.5.8.6.2 非快照算法虚警率测试

####### 6.5.8.6.2.1 测试步骤

非快照型算法适用于电离层误差和接收机噪声为相关时间函数的情况。采用离线仿真测试，具体测试步骤如下。

a）虚警率测试使用漏警率测试中筛选出的40个几何分布集合，电离层误差和接收机噪声为相关时间的函数。

b）对于40个几何分布，每个几何分布模拟82 500 h的执行时间。记录每个分布试验结果过及警报状态。在每次82 500 h的模拟运行期间，将卫星速度设置为0，卫星位置将被冻结在所选的边缘几何值上，确保HAL/HPL在运行期间不发生变化。

c）对于每个几何分布，统计虚警的数量，确定 RAIM 算法是否满足虚警率要求。

####### 6.5.8.6.2.2 测试判据

北斗机载设备通过该项测试，满足以下要求：

a）所有可接受的几何分布上的告警总数应 $ \leqslant47 $ ；

b）对于每个几何分布，告警数应 $ \leqslant3 $ 。

##### 6.5.8.7 在线测试

###### 6.5.8.7.1 测试步骤

在线验证测试的目的是确保离线算法和在北斗机载设备上实现的算法在功能、性能和计算结果上是一致的。该部分测试分为目标计算测试和在线行为测试。

目标计算测试属于离线仿真测试，具体测试步骤如下：

a）根据筛选出的40个几何分布场景，在每个场景中，生成5 m/s斜坡故障，执行RAIM算法；

b）记录测试结果，包括水平检测保护级、水平排除保护级、水平径向位置误差、告警标识等；

c）将测试数据复制到机载设备中，执行 RAIM 算法，记录执行结果；

d）将目标计算结果和离线结果进行对比。

北斗机载设备通过该项测试，需要满足：目标软件测试输出的算术变量值和离线输出算术变量值相差在0.1 m以内，逻辑变量严格一致。

在线行为测试通过 GNSS 模拟器进行测试，测试步骤如下：

a）按照图 4 测试框图连接设备；

b）根据 40 个几何分布，从中选择 5 个几何分布，分别配置 GNSS 信号模拟器；

c) 在 GNSS 模拟器的相应卫星添加 5 m/s 斜坡故障；

d）被测设备正常工作并执行 RAIM 算法；

e）记录定位结果和 HPL $ _{FD} $  值；

f）统计定位结果精度和 $ HPL_{FD} $ 值偏差结果，判断算法是否满足RAIM性能要求。

###### 6.5.8.7.2 测试判据

北斗机载设备通过该项测试，需要满足以下要求：

1）设备在线仿真测试和目标计算测试的定位结果差异超过5 m的时间应在2 s内；

2）设备在线仿真测试和目标计算测试的 HPL $ _{FD} $  差异超过 50 m 的时间应在 10 s 内。

#### 6.5.9 动态性能测试

##### 6.5.9.1 测试目的

用于验证北斗机载设备在飞行过程中的动态性能。

##### 6.5.9.2 测试场景

动态性能测试框图见图2。

##### 6.5.9.3 测试步骤

动态性能测试分为正常机动测试和异常机动测试，其中正常机动测试包括动态场景一～动态场景四，异常机动测试为动态场景五，测试步骤如下。

a）设置 GNSS 模拟器，分别仿真以下动态用户轨迹，同时储存用户轨迹数据：

1）动态场景一：水平加速度 0.58g，最大地速不超过 800 kt，然后加速度降低到 0；

2）动态场景二：180°转弯飞行，直到1.3倍的标准速率（水平加速度不超过0.58g），最大地速不超过800 kt，然后加速度降低到0；

3）动态场景三：垂直加速度 0.5g，最大地速不超过 800 kt，然后加速度降低到 0；

4）动态场景四：垂直加速度-0.5g，最大地速不超过800 kt，然后加速度降低到0；

5）动态场景五：水平加速度2g，垂直加速度1.5g，最大地速不超过800 kt，然后加速度降低到0。

b） 被测设备上电并记录定位数据。

##### 6.5.9.4 测试判据

设备通过该项测试，应满足以下要求：

a）正常机动飞行过程中，非加速后10 s内定位数据应满足5.2.1精度要求。

b）异常机动飞行过程中，非加速后60 s内定位数据应满足5.2.1精度要求。

#### 6.5.10 位置数据输出更新率测试

##### 6.5.10.1 测试目的

用于验证北斗机载设备的位置数据输出更新率。

##### 6.5.10.2 测试场景

数据更新率测试框图见图2。

##### 6.5.10.3 测试步骤

测试步骤如下：

a）按图 2 连接测试设备；

b) 操作 GNSS 模拟器，设置满足 5.2.5.1 正常飞行动态要求的场景，输出北斗卫星导航系统 B1C

频点信号；

c）北斗机载设备正常工作，并至少记录10 min时间、位置、速度、HFOM和HPL等数据。

##### 6.5.10.4 测试判据

设备相邻两条定位数据输出的时间间隔应不大于1 s。

### 6.6 接口测试

接口测试步骤为：

a）目视检查电气接口类型，使用万用表笔测量阻值；

b）将北斗机载设备与测试设备连接，检查其接口通信是否正常；

c）试连接同轴连接器接插件，以检验其连接性。

### 6.7 可靠性测试

北斗机载设备定型时，应进行可靠性试验，验证产品是否达到规定的可靠性要求，测试方法依据GB/T 5080.7中的定时（定数）截尾试验方案。

在北斗机载设备批量生产验收且不需要估计MTBF的真值时，应以预定的判决风险率 $ (\alpha,\beta) $ ，对规定的MTBF值作合格与否的判断。测试方法依据GB/T5080.7中的截尾序贯试验方案。

# 附录 A

(规范性)

## 标准接收信号和干扰环境

### A.1 概述

本附录规定了航空辅助导航北斗机载设备在 B1C 频段带内及其带外的射频干扰环境。描述了标准天线的频率选择要求。

所有信号电平均以天线端口处测得的 dBm 为单位。就本设备的技术要求而言：

a）带内和近带频率定义在1 575.42 MHz±20 MHz的范围内；

b）带外频率定义为在带内和近带频率范围之外。

### A.2 干扰环境

#### A.2.1 概述

干扰电平的参考基准为天线端口，与天线辐射方向图无关。图 A.1 显示了运行干扰环境，包括带内和近带干扰，天线口面总干扰功率与接收带宽的函数关系如图 A.2 所示。最低标准天线的频率选择性如图 A.3 所示，用于定义使用这种天线的设备的工作环境。

#### A.2.2 带外干扰

在天线端口处进行测量，带外连续波(CW)干扰信号可能达到图 A.1 和表 A.1 的水平。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_300_902_885_1359.jpg" alt="Image" width="49%" /></div>


频率/MHz

<div style="text-align: center;">图 A.1 天线端口处的干扰功率</div>


<div style="text-align: center;">表 A.1 稳态导航 CW 干扰门限</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>干扰信号频率范围(f1)MHz</td><td style='text-align: center;'>干扰电平dBm</td></tr><tr><td style='text-align: center;'>1 315&lt;f1&gt;从-9 dBm线性增加至-1.5 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 525&lt;f1&gt;从-1.5 dBm线性降低至-4 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 531&lt;f1&gt;从-4 dBm线性降低至-35 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 536&lt;f1&gt;从-35 dBm线性降低至-120.5 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 565.42&lt;f1&gt;120.5 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 585.42&lt;f1&gt;120.5 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 610&lt;f1&gt;从-120.5 dBm线性增加至-30 dBm</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 618&lt;f1&gt;从-30 dBm线性增加至-12 dBm*</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 618&lt;f1&gt;从-12 dBm线性增加至21.5 dBm*</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 618&lt;f1&gt;从-30 dBm线性增加至8 dBm*</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 626.5&lt;f1&gt;从8 dBm线性增加至21.5 dBm*</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>f1&gt;2 000</td><td style='text-align: center;'>21.5 dBm</td></tr><tr><td colspan="2">a适用于没有机载卫星通信的飞行器。b适用于有机载卫星通信的飞行器。</td></tr></table>

所有飞行阶段运行的设备进入稳态导航后，可在上述规定的带外频率范围内承受脉冲干扰。其述特性见表 A.2。

<div style="text-align: center;">表 A.2 带外脉冲干扰</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>卫星导航系统</td><td style='text-align: center;'>BDS</td></tr><tr><td style='text-align: center;'>峰值功率</td><td style='text-align: center;'>+30 dBm</td></tr><tr><td style='text-align: center;'>脉宽</td><td style='text-align: center;'>$ \leq $ 125  $ \mu $ s</td></tr><tr><td style='text-align: center;'>占空比</td><td style='text-align: center;'>$ \leq $ 1%</td></tr></table>

#### A.2.3 带内和近带干扰

带内和近带干扰环境适用于稳态导航。建立稳态导航后，对于B1C信号的初始捕获，其带内和近带干扰电平比稳态导航低6 dB。干扰带宽为3 dB。

稳态导航建立后，设备可承受频率范围为1575.42 MHz ± BW_{1}/2 MHz 的干扰信号，该信号与表A.3中规定的电平一样高，是干扰信号带宽(BW_{1})的函数。

<div style="text-align: center;">表 A.3 带内和近带干扰带宽定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>带宽 BW1</td><td style='text-align: center;'>干扰电平 dBm</td></tr><tr><td style='text-align: center;'>0≤BW1≤700 Hz</td><td style='text-align: center;'>-120.5 dBm</td></tr><tr><td style='text-align: center;'>700 Hz&lt;BW1&gt;10 kHz</td><td style='text-align: center;'>从-120.5 dBm线性增加至-113.5 dBm</td></tr></table>

<div style="text-align: center;">表 A.3 带内和近带干扰带宽定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>带宽 BW1</td><td style='text-align: center;'>干扰电平 dBm</td></tr><tr><td style='text-align: center;'>10 kHz&lt;BW1≤100 kHz</td><td style='text-align: center;'>从-113.5 dBm线性增加至-110.5 dBm</td></tr><tr><td style='text-align: center;'>100 kHz&lt;BW1≤1 MHz</td><td style='text-align: center;'>-110.5 dBm</td></tr><tr><td style='text-align: center;'>1 MHz&lt;BW1≤20 MHz</td><td style='text-align: center;'>从-110.5 dBm线性增加至-97.5 dBm*</td></tr><tr><td style='text-align: center;'>20 MHz&lt;BW1≤30 MHz</td><td style='text-align: center;'>从-97.5 dBm线性增加至-91.1 dBm*</td></tr><tr><td style='text-align: center;'>30 MHz&lt;BW1 I≤40 MHz</td><td style='text-align: center;'>从-91.1 dBm线性增加至-89.5 dBm*</td></tr><tr><td style='text-align: center;'>40 MHz&lt;BW1</td><td style='text-align: center;'>-89.5 dBm*</td></tr><tr><td colspan="2">* 在1 575.42 MHz±10 MHz的频率范围内,干扰电平不应超过-110.5 dBm/MHz。</td></tr></table>

表 A.3 中干扰电平作为带宽的函数，如图 A.2 所示。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_310_638_862_1070.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 A.2 带内和近带干扰环境</div>


稳态导航建立后，在所有飞行阶段运行的设备可在上述规定的带内和近带频率范围内承受脉冲干扰，其特性见表 A.4。

<div style="text-align: center;">表 A.4 带内和近带脉冲干扰</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>峰值功率</td><td style='text-align: center;'>脉宽</td><td style='text-align: center;'>占空比</td><td style='text-align: center;'>信号带宽</td></tr><tr><td style='text-align: center;'>+10 dBm</td><td style='text-align: center;'>125  $ \mu $ s</td><td style='text-align: center;'>1%</td><td style='text-align: center;'>1 MHz</td></tr></table>

#### A.2.4 GNSS 噪声

GNSS 噪声是一种宽带噪声，其频谱密度对设备的影响相当于 GNSS 环境的总功率。由于不同的信号耦合和操作要求，表 A.5 指定了不同接收机功能的值。

<div style="text-align: center;">表 A.5 所有 GNSS 源的有效噪声密度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接收机功能</td><td style='text-align: center;'>有效噪声密度dBm/Hz</td></tr><tr><td style='text-align: center;'>北斗信号初始捕获</td><td style='text-align: center;'>-172.2</td></tr><tr><td style='text-align: center;'>北斗信号跟踪和重捕获</td><td style='text-align: center;'>-171.9</td></tr></table>

### A.3 天线频率选择性最低标准

当使用最低标准天线接收时，干扰信号至少会根据表 A.6 和图 A.3 中的频率衰减特性。

<div style="text-align: center;">表 A.6 频率选择性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>频率fMHz</td><td style='text-align: center;'>选择性dB</td></tr><tr><td style='text-align: center;'>1 315 MHz≤f&lt;1 504.42 MHz</td><td style='text-align: center;'>-50 dB</td></tr><tr><td style='text-align: center;'>1 504.42 MHz≤f&lt;1 554.42 MHz</td><td style='text-align: center;'>从-50 dB线性增加到-5 dB</td></tr><tr><td style='text-align: center;'>1 554.42 MHz≤f&lt;1 558.42 MHz</td><td style='text-align: center;'>从-5 dB线性增加</td></tr><tr><td style='text-align: center;'>1 558.42 MHz≤f&lt;1 591.92 MHz</td><td style='text-align: center;'>0 dB</td></tr><tr><td style='text-align: center;'>1 591.92 MHz&lt;fcel从-25.35 dB线性下降到-25 dB</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 605.42 MHz&lt;fcel从-25.35 dB线性下降到-50 dB</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1 625.42 MHz&lt;fcel-50 dB</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_334_924_867_1364.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 A.3 频率选择性</div>


## 附录 B

(规范性)

## 定位精度分析方法

定位精度分析可按本附录给出的方法进行数据处理。

精度计算使用  $ 2d_{rms} $  公式计算，计算公式(B.1)如下：

 $$ 2d_{\mathrm{r m s}}=2\sqrt{\left[\sum_{i=1}^{N}\left(1.5d_{i}/\mathrm{H D O P}_{i}\right)^{2}\right]/N} $$ 

……(B.1)

式中：

 $ 2d_{rms} $  —— 两倍的距离，（误差）均方根；

 $ d_{i} $  ——瞬时二维水平位置误差，单位为米(m)；

N ——(试验中)纳入考虑的采样点数;

HDOP_{i}——(第 i 个采样时刻的)瞬时水平精度因子。

在单次测试中，若北斗机载设备在数据统计时间内输出有效位置，则测试失败。

总计最多进行三组测试，每组可进行10次测试。如在第一组的前10次试验中没有发生故障，则为测试成功，如出现1次失败，则进行下一组的10次试验，如出现2次及以上失败，则判定为测试失败，以此类推。具体见表B.1。

<div style="text-align: center;">表 B.1 分级采样通过/失败准则</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验</td><td style='text-align: center;'>在指定时间内的累计失败数</td><td style='text-align: center;'>测试配置</td></tr><tr><td style='text-align: center;'>前十(10)次试验</td><td style='text-align: center;'>0次1次≥2次</td><td style='text-align: center;'>通过再进行10次或更多失败</td></tr><tr><td style='text-align: center;'>第二组十(10)次试验</td><td style='text-align: center;'>0次1次或2次≥3次</td><td style='text-align: center;'>通过再进行10次或更多失败</td></tr><tr><td style='text-align: center;'>第三组十(10)次试验</td><td style='text-align: center;'>0次≥1次</td><td style='text-align: center;'>通过失败</td></tr></table>

## 附录 C

## (规范性)

## 一 般最小二乘解和对流层修正算法中的权重

### C.1 权重

BDS 伪距测量加权最小二乘定位解算和 FDE 中按公式(C.1)和公式(C.2)计算权重。

 $$ \sigma_{i}^{2}=\mathrm{URA}_{i}^{2}+\sigma_{i,\mathrm{UIRE}}^{2}+\sigma_{i,\mathrm{air}}^{2}+\sigma_{i,\mathrm{tropo}}^{2} $$ 

 $$ w_{i}=1/\sigma_{i}^{2} $$ 

### C.2 电离层延迟方差

下面模型描述了基于 BDS 电离层改正有关的电离层误差，见公式(C.3)～公式(C.5)：

 $$ \sigma_{i,\mathrm{UIRE}}^{2}=\mathrm{MAX}\left\{\left(\frac{c\ T_{\mathrm{iono}}}{5}\right)^{2},(F_{\mathrm{PP}}\cdot\tau_{\mathrm{vert}})^{2}\right\} $$ 

 $$ \tau_{vert}=\left\{\begin{aligned}&9m,0\leqslant\left|\phi_{m}\right|\leqslant20\\ &4.5m,20<\left|\phi_{m}\right|\leqslant55\\ &6m,55<\left|\phi_{m}\right|\end{aligned}\right. $$ 

式中：

c ——光速,  $ 2.99792458 \times 10^{8} $  m/s;

 $ T_{iono} $  ——电离层改正数，计算方法参照 GB/T 39414.1—2020 中 8.8.2；

 $ F_{PP} $  ——倾斜因子；

 $ \phi_{m} $  ——地理伪距。

 $$ F_{\mathrm{PP}}=1/\sqrt{1-\left(\frac{R_{\mathrm{e}}\cos E}{R_{\mathrm{e}}+h_{\mathrm{I}}}\right)^{2}} $$ 

式中：

 $ R_{e} $ ——取值为6 378 000.0 m；

 $ h_{1} $  ——取值为400 000.0 m。

### C.3 机载接收机误差方差

参数 $ \sigma_{i,air}^{2} $ 有两种计算模型。

误差模型1：设备没有进行载波平滑伪距，机载接收机误差方法见公式（C.6）：

 $$ \sigma_{i,air}^{2}=25\ m^{2} $$ 

注1：对于模型1的 $ \sigma_{i,air}^{2} $ 多路径误差sigma模型基于航路、进近和着陆操作的数据采集。

误差模型 2: 设备进行载波平滑伪距, 机载接收机误差方法见公式(C.7):

 $$ \sigma_{i,\mathrm{air}}^{2}=\sigma_{i,\mathrm{noise}}^{2}+\sigma_{i,\mathrm{multipath}}^{2}+\sigma_{i,\mathrm{divg}}^{2} $$ 

机载设备的多径误差用分布  $ N(0, \sigma_{\text{multipath}}^{2}) $  描述，见公式(C.8)：

 $$ \sigma_{i,\mathrm{m u l t i p a t h}}=0.13+0.53\mathrm{e}^{(-\theta_{i}/10)} $$ 

式中：

 $ \theta_{i} $  —— 卫星 i 的高度角，单位为度( $ ^{\circ} $ )。

注2：高度角大于 $ 2^{\circ} $ 时，多路径误差sigma有效。

注3：对于$\mathrm{HAL}>560\ \mathrm{m}$，码测量的载波平滑引起的误差忽略不计，假定为零。如果制造商选择使用$\mathrm{HAL}<556\ \mathrm{m}$的载波平滑设备，制造商宜考虑载波平滑引起的误差。

注4：如果机载设备平滑滤波器相比标准滤波器收敛到一个不同的稳态偏差，稳态误差仍然存在时，宜考虑 $ \sigma_{divg} $ 。

 $ \sigma_{i,noise} $  为一个正态分布的标准差，该正态分布界定了 GNSS 接收机与卫星 i 相关的分布尾部误差，包括接收机噪声、热噪声、干扰、信道间偏差、外推、平滑滤波器初始化时间以及处理误差。

 $ \sigma_{i,noise} $  根据不同信号条件是可变的。例如，由于干扰导致的系统精度下降需要在警报时间内计算保护级别使用的RMS $ _{pr\_air} $ 。

注5：6.5.1的测试程序足以表明符合5.2.1的精度要求和完好性的 $ \sigma_{noise} $ 要求。通过这些测试验证 $ \sigma_{noise} $ 能用作正态分布的标准差，其限制了与接收机跟踪性能有关的误差分布的尾部。

### C.4 对流层改正模型

由于对流层折射是一种局部现象,所有用户都将计算自己的对流层延迟校正。建议的对流层校正模式描述如下。

卫星 i 的对流层延迟修正 TC 采用公式(C.9)形式：

 $$ \mathrm{TC}_{i}=-\left(d_{\mathrm{hyd}}+d_{\mathrm{wet}}\right)\bullet m\left(\mathrm{El}_{i}\right) $$ 

式中：

 $ \left[d_{hyd}, d_{wet}\right] $ ——由流体静力平衡中的大气气体和水蒸气引起的卫星 $ 90^{\circ} $ 仰角估计距离延迟；

 $ m(\mathrm{El}_{i}) $  ——一个无量纲的映射函数，用于将延迟缩放到实际的卫星仰角  $ E l_{i} $  方向。

 $ \left[d_{hyd}, d_{wet}\right] $  的计算根据接收机的高度和 5 个气象参数的估算：压力 P [单位为毫巴 (mbar)]，温度 T [单位为卡尔文 (K)]，水汽压力 eP [单位为毫巴 (mbar)]，温度递减率  $ \beta $  [单位为卡尔文/毫巴 (K/mbar)] 和水汽“递减率”  $ \lambda $ 。

注：1 mbar=100 Pa。

适用于接收纬度  $ \phi $  和年份 D（从 1 月 1 日开始）的 5 个气象参数的每个值都是根据表 C.1 中给出的平均值和季节变化值计算出来的。每个参数值  $ \xi $  计算见公式（C.10）：

 $$ \xi(\phi,D)=\xi_{0}(\phi)-\Delta\xi(\phi)\cdot\cos\left[\frac{2\pi(D-D_{\min})}{365.25}\right] $$ 

式中：

 $ D_{min} $  ——北纬为28，南纬为211；

 $ \xi_{0} $  ——接收机所在纬度的特定参数的平均值；

△ξ——接收机所在纬度的季节变化值。对于 $ |\phi|\leqslant15^{\circ} $ 和 $ |\phi|\geqslant75^{\circ} $ 的纬度， $ \xi_{0} $ 和 $ \Delta\xi $ 的值直接取自表C.1。对于 $ 15^{\circ}<|\phi|<75^{\circ} $ 范围内的纬度，在接收机纬度处的 $ \xi_{0} $ 和 $ \Delta\xi $ 的值分别通过表C.1中最接近的两个纬度 $ \left[\phi_{i},\phi_{i+1}\right] $ 的值之间的线性插值计算出来，见公式(C.11)和公式(C.12)：

 $$ \hat{\xi}_{0}\left(\phi\right)=\hat{\xi}_{0}\left(\phi_{i}\right)+\left[\hat{\xi}_{0}\left(\phi_{i+1}\right)-\hat{\xi}_{0}\left(\phi_{i}\right)\right]\bullet\frac{\left(\phi-\phi_{i}\right)}{\left(\phi_{i+1}-\phi_{i}\right)} $$ 

 $$ \Delta\xi(\phi)=\Delta\xi(\phi_{i})+\left[\Delta\xi(\phi_{i+1})-\Delta\xi(\phi_{i})\right]\cdot\frac{(\phi-\phi_{i})}{(\phi_{i+1}-\phi_{i})} $$ 

<div style="text-align: center;">表 C.1 对流层延迟的气象参数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">纬度</td><td colspan="5">均值</td></tr><tr><td style='text-align: center;'>$ P_{0}/\mathrm{mbar} $</td><td style='text-align: center;'>$ T_{0}/\mathrm{K} $</td><td style='text-align: center;'>$ e_{0}/\mathrm{mbar} $</td><td style='text-align: center;'>$ \beta_{0}/(\mathrm{K}/\mathrm{m}) $</td><td style='text-align: center;'>$ \lambda_{0} $</td></tr><tr><td style='text-align: center;'>&lt;15°</td><td style='text-align: center;'>1 013.25</td><td style='text-align: center;'>299.65</td><td style='text-align: center;'>26.31</td><td style='text-align: center;'>6.3e-3</td><td style='text-align: center;'>2.77</td></tr><tr><td style='text-align: center;'>30°</td><td style='text-align: center;'>1 017.25</td><td style='text-align: center;'>294.15</td><td style='text-align: center;'>21.79</td><td style='text-align: center;'>6.05e-3</td><td style='text-align: center;'>3.15</td></tr><tr><td style='text-align: center;'>45°</td><td style='text-align: center;'>1 015.75</td><td style='text-align: center;'>283.15</td><td style='text-align: center;'>11.66</td><td style='text-align: center;'>5.58e-3</td><td style='text-align: center;'>2.57</td></tr></table>

<div style="text-align: center;">表 C.1 对流层延迟的气象参数（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">纬度</td><td colspan="5">均值</td></tr><tr><td style='text-align: center;'>$ P_{0}/\mathrm{mbar} $</td><td style='text-align: center;'>$ T_{0}/\mathrm{K} $</td><td style='text-align: center;'>$ e_{0}/\mathrm{mbar} $</td><td style='text-align: center;'>$ \beta_{0}/(\mathrm{K}/\mathrm{m}) $</td><td style='text-align: center;'>$ \lambda_{0} $</td></tr><tr><td style='text-align: center;'>60°</td><td style='text-align: center;'>1 011.75</td><td style='text-align: center;'>272.15</td><td style='text-align: center;'>6.78</td><td style='text-align: center;'>5.39e-3</td><td style='text-align: center;'>1.81</td></tr><tr><td style='text-align: center;'>&gt;75°</td><td style='text-align: center;'>1 013.00</td><td style='text-align: center;'>263.65</td><td style='text-align: center;'>4.11</td><td style='text-align: center;'>4.53e-3</td><td style='text-align: center;'>1.55</td></tr><tr><td rowspan="2">纬度</td><td colspan="5">季节变化</td></tr><tr><td style='text-align: center;'>$ \Delta P/\mathrm{mbar} $</td><td style='text-align: center;'>$ \Delta T/\mathrm{K} $</td><td style='text-align: center;'>$ \Delta e/\mathrm{mbar} $</td><td style='text-align: center;'>$ \Delta \beta/(\mathrm{K}/\mathrm{m}) $</td><td style='text-align: center;'>$ \Delta \lambda $</td></tr><tr><td style='text-align: center;'>&lt;15°</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00e-3</td><td style='text-align: center;'>0.00</td></tr><tr><td style='text-align: center;'>30°</td><td style='text-align: center;'>-3.75</td><td style='text-align: center;'>7.00</td><td style='text-align: center;'>8.85</td><td style='text-align: center;'>0.25e-3</td><td style='text-align: center;'>0.33</td></tr><tr><td style='text-align: center;'>45°</td><td style='text-align: center;'>-2.25</td><td style='text-align: center;'>11.00</td><td style='text-align: center;'>7.24</td><td style='text-align: center;'>0.32e-3</td><td style='text-align: center;'>0.46</td></tr><tr><td style='text-align: center;'>60°</td><td style='text-align: center;'>-1.75</td><td style='text-align: center;'>15.00</td><td style='text-align: center;'>5.26</td><td style='text-align: center;'>0.81e-3</td><td style='text-align: center;'>0.74</td></tr><tr><td style='text-align: center;'>&gt;75°</td><td style='text-align: center;'>-0.50</td><td style='text-align: center;'>14.50</td><td style='text-align: center;'>3.39</td><td style='text-align: center;'>0.62e-3</td><td style='text-align: center;'>0.30</td></tr></table>

零高度天顶延迟项 $ \left[z_{\mathrm{hyd}}, z_{\mathrm{wet}}(m)\right] $ 计算见公式(C.13)和公式(C.14):

 $$ z_{\mathrm{hyd}}=\frac{10^{-6}\ k_{\mathrm{l}}\ R_{\mathrm{d}}P}{g_{\mathrm{m}}} $$ 

 $$ z_{\mathrm{w e t}}=\frac{10^{-6}k_{2}R_{\mathrm{d}}}{g_{\mathrm{m}}(\lambda+1)-\beta R_{\mathrm{d}}}\cdot\frac{e}{T} $$ 

式中：

 $ k_{1} $  ——大气折射常数，77.604 K/mbar；

 $ k_{2} $  ——大气折射常数，382 000 K^{2}/mbar；

 $ R_{d} $ ——大气干分量常数，287.054 J/(kg·K)；

 $ g_{m} $ ——重力加速度，9.784 m/s $ ^{2} $ 。

 $ \left[d_{hyd}, d_{wet}\right] $  计算见公式(C.15)和公式(C.16):

 $$ d_{\mathrm{hyd}}=\left(1-\frac{\beta H}{T}\right)^{\mathrm{g}/R\mathrm{d}\beta}\bullet z_{\mathrm{hyd}} $$ 

 $$ d_{\mathrm{w e t}}=\left(1-\frac{\beta H}{T}\right)^{(\left(\lambda+1\right)g/R\mathrm{d}\beta)-1}\cdot z_{\mathrm{w e t}} $$ 

式中：

g ——重力加速度,9.806 65 m/s $ ^{2} $ ;

H——接收机的高度，表示平均海平面以上，单位为米(m)。

卫星高程的对流层校正映射函数  $ m(\mathrm{El}_{i}) $  是通过以下两种方式之一计算出来的：

高度角大于 $ 4^{\circ} $ ，m简化计算见公式(C.17):

 $$ \mathrm{m}(\mathrm{El}_{i})=\frac{1.001}{\sqrt{0.002\ 001+\sin^{2}(\mathrm{El}_{i})}} $$ 

对于卫星高度角大于 $ 2^{\circ} $ ，m的计算见公式(C.18):

 $$ \mathrm{m}(\mathrm{El}_{i})=\left(\frac{1.001}{\sqrt{0.002\ 001+\sin^{2}(\mathrm{El}_{i})}}\right)\bullet\left\{1+0.015\bullet\left(\operatorname{MAX}\left[\begin{aligned}0\\ (4^{\circ}-\mathrm{El}_{i})\end{aligned}\right]\right)^{2}\right\} $$ 

对于不适用上述对流层模型的设备，该设备应包括一个超过罕见对流层延迟的残余误差模型。

### C.5 对流层误差模型标准方差

对流层延迟残差是基于对流层误差的评估。在 C.4 对流层改正模型的基础上，卫星 i 对流层延迟校正的残差参数  $ \sigma_{i,trop} $  见公式 (C.19)：

 $$ \sigma_{i,\mathrm{t r o p}}=\left[\sigma_{\mathrm{V T E}}\bullet\mathrm{m}(\mathrm{E l}_{i})\right] $$ 

式中：

 $ \sigma_{VTE} $  —— 对流层垂直误差，取值为 0.12 m。

## 附录 D

## (规范性)

## 接收机自主完好性方法

检测效果较好的 RAIM 算法是基于当前伪距观测量的快照(Snapshot)方法，伪距比较法、最小二乘残差法和奇偶矢量法三种方法对于单卫星故障检测都有较好的效果，三种方法的本质是一样的。其中奇偶矢量法计算相对比较简单，被普遍采用。

在 BDS 导航系统下,不考虑观测噪声时,其伪距观测方程如公式(D.1)所示:

 $$ y=\mathbf{G}x $$ 

其中，G 见公式(D.2):

 $$ \boldsymbol{G}=\left[\begin{array}{cccc}{{{\cos\mathrm{El}_{1}\cos A z_{1}}}}&{{{\cos\mathrm{El}_{1}\sin A z_{1}}}}&{{{\sin\mathrm{EI}_{1}}}}&{{{\cdots}}}&{{{1}}} \\{{{\vdots}}}&{{{\vdots}}}&{{{\vdots}}}&{{{\vdots}}}&{{{\vdots}}} \\{{{\cos\mathrm{El}_{N}\cos A z_{N}}}}&{{{\cos\mathrm{El}_{N}\sin A z_{N}}}}&{{{\sin\mathrm{EI}_{N}}}}&{{{\cdots}}}&{{{1}}}\end{array}\right] $$ 

式中：

N ——表示可见星的数量,单位为个;

El ——表示卫星高度角，单位为度( $ ^{\circ} $ )；

 $ A_{z} $  ——表示卫星方位角，单位为度( $ ^{\circ} $ )；

G ——表示方向余弦矩阵，前三列由东北天方向的方向余弦组成，最后一列由导航系统的时钟参数组成；

X —— $ 4 \times 1 $  维误差参数矢量，包括 3 个用户位置误差参数和 1 个接收机钟差参数；

Y ——由 N 颗可见星的伪距构成的  $ N \times 1 $  矢量。

对方向余弦矩阵 G 进行 QR 分解得：

 $$ G=Q R $$ 

其中 Q 是  $ N \times N $  维正交矩阵，R 是  $ N \times 4 $  维的上三角矩阵。将公式(D.3)代入公式(D.1)中，同时左乘  $ Q^{T} $  得：

 $$ \boldsymbol{Q}^{\mathrm{T}}\boldsymbol{y}=\boldsymbol{R}\boldsymbol{x} $$ 

 $ Q^{T} $  和 R 可表示为公式(D.5):

 $$ \boldsymbol{Q}^{\mathrm{T}}=\begin{bmatrix}Q_{x}\\ Q_{\mathrm{p}}\end{bmatrix},\boldsymbol{R}=\begin{bmatrix}R_{x}\\ 0\end{bmatrix} $$ 

其中 $ Q_{x} $ 为 $ Q^{T} $ 的前4行， $ Q_{p} $ 为其余的N-4行， $ R_{x} $ 为R的前4行，则公式(D.3)可表示为公式(D.6)：

 $$ \begin{bmatrix}Q_{x}\\ Q_{\mathrm{p}}\end{bmatrix}y=\begin{bmatrix}R_{x}\\ 0\end{bmatrix}x $$ 

可得 x 的最小二乘解为公式(D.7):

 $$ \hat{x}=R_{x}Q_{x}y $$ 

同时， $ Q_{p}y=0 $ 。此时，若考虑伪距观测噪声  $ \varepsilon $  和伪距偏差 b，其中  $ \varepsilon $  为  $ N\times1 $  量测噪声，认为观测噪声服从均值为零，方差为  $ \sigma^{2} $  的高斯分布，即  $ \varepsilon\sim N(0,\sigma^{2}) $ 。当不存在伪距偏差时，b 为  $ N\times1 $  阶零矩阵。定义奇偶矢量见公式(D.8)：

 $$ \boldsymbol{p}=Q_{\mathrm{p}}\boldsymbol{\varepsilon}+Q_{\mathrm{p}}\boldsymbol{b} $$ 

从奇偶矢量 p 的表达式可看出奇偶矢量只与卫星的几何分布和观测误差量有关。

定义奇偶矢量的数量积为检验统计量，进行故障的检测与识别，即公式(D.9):

 $$ T_{\mathrm{s}}^{2}=p^{\mathrm{T}}p/\sigma^{2} $$ 

当所有可见星中不含有故障卫星时， $ T_{s}^{2} $  服从自由度为 N-5 的  $ \chi^{2} $  分布，即  $ T_{s}^{2} \sim \chi^{2}(N-4) $ ；当可见

星中含有故障卫星时， $ T_{s}^{2} $  服从自由度为 N-4 的非中心化的  $ \chi^{2} $  分布，即  $ T_{\mathrm{s}}^{2} \sim \chi^{2}(N-4, \lambda) $ ，其中  $ \lambda $  为非中心化参数。

如果系统中不存在故障卫星，而系统给出了告警，称为虚警。在满足一定的条件下，给定虚警概率 $ P_{FA} $ ，可由下式确定检测门限值 $ T^{2} $ 见公式(D.10)：

 $$ P_{r}(T_{\mathrm{s}}^{2}<T^{2})=\int_{0}^{T^{2}}f_{\chi^{2}(N-5)}(x)\mathrm{d}x=1-P_{\mathrm{F A}} $$ 

若 $ T_{s}>T $ ，则存在故障卫星，需要进行故障识别；反之，则无故障卫星，不需要进行故障识别。

若存在故障卫星，构造故障识别量见公式(D.11):

 $$ r_{_{i}}=\frac{\mid p^{\mathrm{T}}Q_{\mathrm{p},i}\mid}{\mid Q_{\mathrm{p},i}\mid} $$ 

其中， $ Q_{p,i} $  为  $ Q_{p} $  的第 i 列。求出所有可见星的故障识别量的大小，并且认为故障识别量最大值所对应的可见星为故障卫星。

## 参 考 文 献

[1] GB/T 42833—2023 北斗星基增强系统单频增强服务机载设备最低性能规范