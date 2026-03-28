

# 中华人民共和国国家标准

GB/T 45308—2025

# 轨道交通 机车车辆 网络时间同步技术要求

# Railway applications—Rolling stock—Technical requirements for network time synchronization

2025-02-28 发布

2025-09-01 实施

国家市场监督管理总局  

国家标准化管理委员会  

发布



## 目次

前言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 缩略语 …… 2    
5 技术要求 …… 3    
6 性能测试 …… 7    
参考文献 …… 10



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由国家铁路局提出。

本文件由全国轨道交通电气设备与系统标准化技术委员会(SAC/TC 278)归口。

本文件起草单位：中车株洲电力机车研究所有限公司、中铁检验认证株洲牵引电气设备检验站有限公司、中国铁道科学研究院集团有限公司机车车辆研究所、中车青岛四方机车车辆股份有限公司、中车株洲电力机车有限公司、中车唐山机车车辆有限公司。

本文件主要起草人：刘海涛、周学勋、申慧、郝波、蔡万银、叶鹏迪、马国栋、叶锋、冀云。



## 轨道交通 机车车辆

## 网络时间同步技术要求

## 1 范围

本文件规定了轨道交通机车车辆网络时间同步技术要求和性能测试。

本文件适用于轨道交通机车车辆列车通信网络(TCN)设备。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 17737.1 同轴通信电缆 第1部分：总规范 总则、定义和要求

GB/T 24338.4 轨道交通电磁兼容第3-2部分：机车车辆设备

GB/T 25119 轨道交通 机车车辆电子装置

GB/T 28029.1—2020 轨道交通电子设备 列车通信网络(TCN) 第1部分:基本结构

GB/T 28029.9—2020 轨道交通电子设备 列车通信网络(TCN) 第3-1部分:多功能车辆总线(MVB)

GB/T 28029.12—2020 轨道交通电子设备 列车通信网络（TCN） 第3-4部分：以太网编组网（ECN）

GB/T 37943—2019 北斗卫星授时终端测试方法

TB/T 1484.3—2017 机车车辆电缆 第 3 部分: 通信电缆

JJF(通信)018—2021 时间综合测试仪校准规范

## 3 术语和定义

GB/T 28029.1—2020 界定的以及下列术语和定义适用于本文件。

### 3.1 

时间基准 time reference

以北斗时作为时间初始基准，以原子时作为时间单元(s)基础的标准时间。

### 3.2 

时间准确度 time accuracy

在一定时间间隔内测量到的本地时钟与时间基准之间的一致性程度。

注：用时间偏差的绝对值表示。

### 3.3 

守时时间准确度 local time accuracy

守时状态下，在规定的时间间隔内测量到的本地时钟与时间基准之间的一致性程度。

注：用时间偏差的绝对值表示。

### 3.4 

## 授时时间准确度 correct time accuracy

授时状态下，授时时钟与被授时时钟之间的一致性程度。

注：用时间偏差的绝对值表示。

### 3.5 

## 时间稳定度 time stability

在 1 s 内,由于时钟的内在因素或环境影响而导致的时间准确度变化程度。

注：用时间偏差的标准差表示。

### 3.6 

## 时间同步装置 clock device

在网络上能发布或接收时间同步协议报文的设备。

### 3.7 

## 时钟源 clock source

能接收时间基准信号，并提供时间信息的设备。

### 3.8 

## 外部时钟源 external clock source

能接收北斗时间基准信号，并提供时间信息的设备。

注：如车载信号装置、中国机车远程监测与诊断系统、车载信息无线传输设备和独立授时设备等。

### 3.9 

## 主时钟 master clock

向从时钟发送时间同步协议报文的设备。

### 3.10 

## 从时钟 slave clock

采用主时钟的时间基准进行时间同步的设备。

### 3.11 

## 运行时钟 operational clock

时间同步装置的系统运行时钟。

注：也称软件时钟。

### 3.12 

本地时钟 local clock

时间同步装置的自有时钟。

注：也称硬件时钟。

### 3.13 

## 时钟域 clock domain

能按照相同的通信传输规范完成时间同步的装置的逻辑组合。

### 3.14 

## 时间同步 time synchronization

在某一时刻，使两台或多台时钟具有同一读数的操作过程。

## 4 缩略语

下列缩略语适用于本文件。

BDS:北斗卫星导航系统(BeiDou Navigation Satellite System)

CCU: 中央控制单元(Central Control Unit)

CMD: 中国机车远程监测与诊断系统 (Chinese locomotive remote Monitoring and Diagnosis system)

MVB: 多功能车辆总线(Multifunction Vehicle Bus)

TBN: 列车骨干网节点(Train Backbone Node)

TRDP: 列车实时数据协议 (Train Real Time Data Protocol)

WTD: 车载信息无线传输设备(Wireless Transformation Device)

1PPS: 秒脉冲 (1 Pulse Per Second)

## 5 技术要求

### 5.1 时间同步系统

#### 5.1.1 组成

时间同步系统由时间同步装置和传输介质组成，其中时间同步装置包含时钟源、主时钟和从时钟。

#### 5.1.2 分类

时间同步系统分为单层时间同步系统、多层时间同步系统和多域时间同步系统。

#### 5.1.3 单层时间同步系统

单层时间同步系统的典型示例见图 1。时钟源接收 BDS 时间基准信号、人工设置时间基准信号或地面无线时间基准信号，直接向本时钟域内的从时钟授时或向主时钟授时；主时钟接收时钟源的时间同步协议报文，处理后向本时钟域内的从时钟进行授时。

<div style="text-align: center;"><img src="imgs/img_in_image_box_233_925_968_1222.jpg" alt="Image" width="61%" /></div>


注：实线代表必要的；虚线代表可选的。

<div style="text-align: center;">图 1 单层时间同步系统典型示例</div>


#### 5.1.4 多层时间同步系统

多层时间同步系统的典型示例见图 2。时钟源接收 BDS 时间基准信号、人工设置时间基准信号或地面无线时间基准信号，并向一级主时钟授时；一级主时钟接收时钟源的时间同步协议报文，处理后向一级从时钟和二级主时钟授时；二级主时钟向二级从时钟授时。

注：一级主时钟指直接接收时钟源时间同步协议报文的主时钟，二级主时钟指从列车骨干网接收一级主时钟时间同步协议报文的主时钟。

<div style="text-align: center;"><img src="imgs/img_in_image_box_123_190_1048_405.jpg" alt="Image" width="77%" /></div>


注：实线代表必要的；虚线代表可选的。

<div style="text-align: center;">图 2 多层时间同步系统典型示例</div>


#### 5.1.5 多域时间同步系统

多域时间同步系统的典型示例见图 3。时钟源接收 BDS 时间基准信号、人工设置时间基准信号或地面无线时间基准信号，在本时钟域内采用单层时间同步系统或多层时间同步系统向从时钟授时。

<div style="text-align: center;"><img src="imgs/img_in_image_box_125_634_1047_817.jpg" alt="Image" width="77%" /></div>


注：实线代表必要的；虚线代表可选的。

<div style="text-align: center;">图 3 多域时间同步系统典型示例</div>


#### 5.1.6 系统配置

时间同步系统的配置要求如下：

a）在一个时钟域内，应至少有一个时钟源，时钟源宜为外部时钟源；

b) 在一个时钟域内，主时钟可采用热备冗余配置方式；

c）多域时间同步系统中，域内可采取单层时间同步系统或多层时间同步系统。

#### 5.1.7 运行方式

<div style="text-align: center;"><img src="imgs/img_in_image_box_724_1148_764_1183.jpg" alt="Image" width="3%" /></div>


时间同步系统的运行要求如下：

a） 主时钟及从时钟的运行时钟宜采用网络授时时间，当网络授时时间无效时，应采用本地时钟；



b）多层时间同步系统中，二级主时钟的运行时钟可根据其和一级主时钟间的链路延时进行相应时间补偿，二级主时钟运行时钟可基于补偿后的时间，补偿机制见 GB/T 25931—2010 中第 11 章；

c）多域时间同步系统中，应仅在域内进行时间同步，域与域之间不进行时间同步；

d）通过无线实现重联时，宜采用多域时间同步系统。

### 5.2 时间同步装置

#### 5.2.1 时钟源

时钟源基本结构示意图见图4。

<div style="text-align: center;"><img src="imgs/img_in_image_box_354_193_849_415.jpg" alt="Image" width="41%" /></div>


注：实线代表必要的；虚线代表可选的。

<div style="text-align: center;">图 4 时钟源基本结构示意图</div>


时钟源的技术要求如下：

a）宜采用 WTD、CMD、车载信号装置、独立时钟源或显示屏等作为时钟源，独立时钟源应为外部时钟源；

b) 应能从 BDS 接收时间信息或手动设置时间信息；

c）在上电未完全初始化阶段或运行异常时，不应发送时间同步协议报文或携带时间有效位信息；

d）在时间同步协议报文中宜附带 BDS 时间有效标志；

e） 应能正确处理闰秒，不应产生错误的时间信号。

#### 5.2.2 主时钟

主时钟基本结构示意图见图 5。

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_841_985_1092.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 5 主时钟基本结构示意图</div>


主时钟的技术要求如下：

a）应具备本地时钟；

b) 应具备从时钟源接收时间信息的通信接口；

c) 应判断时钟源发送时间信息的有效性，应能进行时间基准的选择；

d）在上电未完全初始化阶段或运行异常时，不宜发送时间同步协议报文；

e) 当失去外部时钟源时间信息或不启用外部时钟源时间信息时，主时钟应利用本地时钟进行守时并向从时钟发送时间同步协议报文；

f）设备运行时钟与网络授时时间偏差阈值应可设置，当偏差超出设置时应对运行时钟及本地时钟进行校正。

#### 5.2.3 从时钟

从时钟基本结构示意图见图6。

<div style="text-align: center;"><img src="imgs/img_in_image_box_367_195_803_473.jpg" alt="Image" width="36%" /></div>


注：实线代表必要的；虚线代表可选的。

<div style="text-align: center;">图 6 从时钟基本结构示意图</div>


从时钟的技术要求如下：

a）宜具备本地时钟；

b）设备运行时钟与网络授时时间偏差阈值应可设置，当偏差超出设置时应对运行时钟进行校正；若具备本地时钟，应对本地时钟进行校正。

### 5.3 传输介质

5.3.1 机车车辆网络通信电缆宜采用屏蔽双绞线、光纤等传输介质。屏蔽双绞线传输性能应符合TB/T 1484.3—2017的规定，光纤传输性能应符合GB/T 28029.9—2020中4.6.3的规定。

5.3.2 BDS 接收天线的传输介质宜采用同轴电缆，应符合 GB/T 17737.1 的规定。

### 5.4 信息传输

5.4.1 宜采用国际原子时、协调世界时或 UNIX 时间的时间数据格式。

5.4.2 时间同步协议报文可采用 TRDP 和/或 MVB 协议。

5.4.3 主时钟发送时间同步协议报文周期应可配置。

### 5.5 接口

#### 5.5.1 通信接口

通信接口应具有以下要求：

a）应支持 MVB 和/或以太网接口；

b）MVB接口应符合GB/T 28029.9—2020中4.5.7的规定；

c）以太网接口应符合 GB/T 28029.12—2020 中 4.9～4.10 的规定。

#### 5.5.2 BDS 信号输入接口

<div style="text-align: center;"><img src="imgs/img_in_image_box_67_1318_105_1353.jpg" alt="Image" width="3%" /></div>


外部时钟源应具备至少 1 路 BDS 信号接收端口，设备侧应采用 SMA 接口。

#### 5.5.3 1PPS 接口

时钟设备宜具备 1PPS 输出接口，应满足以下要求：

a）TTL电平；

b) 脉宽  $ 1 \, ms \sim 200 \, ms $ ;

c）上升沿不大于50 ns；

d）标称阻抗 50 Ω。

### 5.6 性能

#### 5.6.1 时间性能

在  $ 20^{\circ}C \sim 25^{\circ}C $  环境下，时钟源、主时钟、从时钟的时间准确度和稳定度满足以下要求：

——时钟源时间稳定度不应大于  $ 30 \times 10^{-6} $  s；

——时钟源 24 h 守时时间准确度不应大于 3 s，不宜大于 1 s；

——主时钟时间稳定度不应大于 $ 30\times10^{-6} $  s；

——主时钟授时时间准确度不大于1 s;

——主时钟 24 h 守时时间准确度不应大于 3 s，不宜大于 1 s；

——从时钟（若有本地时钟）24 h 守时时间准确度不应大于 3 s，不宜大于 1 s。

#### 5.6.2 BDS 信号性能

时钟源接收 BDS 时间信号性能应满足以下要求。

——灵敏度：捕获灵敏度小于或等于 $ -133\ dBm $ ，跟踪灵敏度小于或等于 $ -136\ dBm $ 。

——捕获时间：上电启动时小于2 min，热启动时小于1 min。

——接收中心频率：1 561.098 MHz/1 207.14 MHz/1 268.52 MHz/1 575.42 MHz/1 176.45 MHz。

#### 5.6.3 电磁兼容性

应符合 GB/T 24338.4 的规定。

#### 5.6.4 环境适应性

应符合 GB/T 25119 的规定。

## 6 性能测试

### 6.1 测试环境

测试环境条件要求如下：

——环境温度在  $ 20^{\circ}C \sim 25^{\circ}C $  内任选一点，温度变化不应超过  $ 2^{\circ}C $ ;

——相对湿度小于或等于80%;

——周围无影响仪器正常工作的电磁干扰和机械振动。

### 6.2 测试项目

测试项目见表1。

<div style="text-align: center;">表 1 时间同步装置测试项目</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>测试项目</td><td style='text-align: center;'>技术要求</td><td style='text-align: center;'>测试方法</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>时间同步装置时间稳定度测试</td><td style='text-align: center;'>5.6.1</td><td style='text-align: center;'>6.3.1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>时钟源守时时间准确度测试</td><td style='text-align: center;'>5.6.1</td><td style='text-align: center;'>6.3.2</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>主时钟守时时间准确度测试</td><td style='text-align: center;'>5.6.1</td><td style='text-align: center;'>6.3.3</td></tr></table>

<div style="text-align: center;">表 1 时间同步装置测试项目（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>测试项目</td><td style='text-align: center;'>技术要求</td><td style='text-align: center;'>测试方法</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>从时钟守时时间准确度测试</td><td style='text-align: center;'>5.6.1</td><td style='text-align: center;'>6.3.4</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>主时钟授时时间准确度测试</td><td style='text-align: center;'>5.6.1</td><td style='text-align: center;'>6.3.5</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>接收 BDS 信号性能测试</td><td style='text-align: center;'>5.6.2</td><td style='text-align: center;'>6.3.6</td></tr></table>

### 6.3 测试方法

#### 6.3.1 时间同步装置时间稳定度测试

若设备具备 1PPS 接口，时间稳定度按以下方法测试：

a) 按图 7 搭建测试拓扑；

b) 由时钟精度分析仪测量得到被测时钟与基准时间源 1 h 的时差数据（采样间隔 1 s），计算标准差，作为时间同步装置的时间稳定度，时钟精度分析仪性能应满足 JJF（通信）018—2015 的要求。



<div style="text-align: center;"><img src="imgs/img_in_image_box_164_604_1051_777.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 7 时间稳定度测试拓扑</div>


#### 6.3.2 时钟源守时时间准确度测试

时钟源守时时间准确度按以下方法进行测试。

a）按图 8 搭建测试拓扑。

b) 被测时钟源从北斗进行授时，并将获取到的基准时间设置到本地时钟后持续运行（在此期间不再重复设置本地时钟），持续运行24 h后通过软件接口分别获取BDS时间和本地时钟并计算其差值，取绝对值。按以上步骤测量3次，取最大值作为时钟源守时时间准确度。

<div style="text-align: center;"><img src="imgs/img_in_image_box_455_1065_715_1143.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 8 时钟源守时时间准确度测试拓扑</div>


#### 6.3.3 主时钟守时时间准确度测试

主时钟守时时间准确度按以下方法进行测试。

a）按图 9 搭建测试拓扑。

b) 陪测时钟源和被测主时钟运行时间同步协议，陪测时钟源从 BDS 获取基准时间，被测主时钟采集陪测时钟源的时间同步协议报文（采样间隔 1 s），基于报文中记录的陪试时钟源时间进行一次授时后，停止运行时间同步模块，并持续采集时间同步协议报文，持续运行 24 h 后，计算被测主时钟的本地时钟与陪测时钟源的时差数据，取绝对值。按以上步骤测量 3 次，取最大值作为主时钟守时时间准确度。

<div style="text-align: center;"><img src="imgs/img_in_image_box_304_194_900_278.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 9 主时钟守时时间准确度测试拓扑</div>


#### 6.3.4 从时钟守时时间准确度测试

从时钟守时时间准确度按以下方法进行测试。

a) 按图 10 搭建测试拓扑。

b) 陪测时钟源和被测从时钟运行时间同步协议，陪测时钟源从 BDS 获取时间基准，被测从时钟采集陪测时钟源的时间同步协议报文（采样间隔 1 s），基于报文中记录的陪试时钟源时间进行一次授时后，停止运行时间同步模块，并持续采集时间同步协议报文，持续运行 24 h 后，计算被测从时钟的本地时钟与陪测时钟源的时差数据，取绝对值。按以上步骤测量 3 次，取最大值作为从时钟守时时间准确度。

BDS时间基准 ___ 陪测时钟源 时间同步协议 被测从时钟



<div style="text-align: center;"><img src="imgs/img_in_image_box_282_627_928_723.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 10 从时钟守时时间准确度测试拓扑</div>


#### 6.3.5 主时钟授时时间准确度测试

若设备具备1PPS接口，主时钟授时时间准确度按以下方法进行测试：

a）按图 11 搭建测试拓扑；

b) 被测主时钟以 1 s 的周期向陪测从时钟发送时间同步协议报文，陪测从时钟每收到时间同步协议报文后，驱动 1PPS 信号有效，由时钟精度分析仪每秒采样 1 次陪测从时钟与被测主时钟 1PPS 信号的时差数据，剔除丢包情况下的最大偏差值，计算 1 h 内不丢包情况下的偏差最大值，取绝对值作为主时钟授时时间准确度。

<div style="text-align: center;"><img src="imgs/img_in_image_box_247_1045_955_1236.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 11 主时钟授时时间准确度测试拓扑</div>


#### 6.3.6 接收 BDS 信号性能测试

灵敏度测试按 GB/T 37943—2019 中 8.3.6 的规定进行。

捕获时间测试按 GB/T 37943—2019 中 8.3.8 的规定进行。

## 参 考 文 献

[1] GB/T 25931—2010 网络测量和控制系统的精确时钟同步协议

Powered by TCPDF (www.tcpdf.org)



