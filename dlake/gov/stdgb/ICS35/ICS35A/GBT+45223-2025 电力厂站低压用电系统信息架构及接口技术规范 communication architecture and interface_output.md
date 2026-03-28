

# 中华人民共和国国家标准

GB/T 45223—2025

# 电力厂站低压用电系统信息架构及接口 技术规范

# Technical specification for communication architecture and interface of low voltage auxiliary power systems for electric power stations and substations

2025-01-24 发布

2025-08-01 实施



## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 缩略语 …… 1  
  
5 架构 …… 2  
  
5.1 系统结构 …… 2  
  
5.2 网络架构 …… 2  
  
5.3 信息交互 …… 5  
  
5.4 模型要求 …… 5  
  
5.5 接口要求 …… 5  
  
6 模型 …… 5  
  
6.1 功能分解 …… 5  
  
6.2 建模通则 …… 7  
  
6.3 信息建模 …… 7  
  
7 接口 …… 10  
  
7.1 基本功能 …… 10  
  
7.2 技术参数 …… 11  
  
7.3 品质与时标 …… 11  
  
7.4 网络接口 …… 11  
  
8 测试 …… 11  
  
8.1 一致性测试 …… 11  
  
8.2 应用测试 …… 12  
  
附录 A（规范性） 电力厂站低压用电系统的设备模型 …… 13  
  
A.1 概述 …… 13  
  
A.2 交流进线 ZACI …… 13  
  
A.3 直流进线 ZDCI …… 15  
  
A.4 交流母线 ZACB …… 15  
  
A.5 交流支路 ZABR …… 17  
  
A.6 直流母线 ZDCB …… 18  
  
A.7 直流支路 ZDBR …… 20  
  
A.8 交流自动切换装置 ZDAC …… 21  
  
A.9 通用双投开关装置 ZDPS …… 22

A.10 充电装置 ZDUG …… 23  
A.11 充电模块 ZDUS …… 24  
A.12 蓄电池组 ZBTG …… 24  
A.13 单只蓄电池 ZBTS …… 26  
A.14 硅链降压装置 ZSRS …… 26  
A.15 整组交流不间断电源装置/逆变电源装置 ZUIG …… 27  
A.16 交流不间断电源装置/逆变电源装置的模块 ZUIS …… 27  
A.17 交流保安电源 ZACP …… 28  
附录 B（资料性） 电力厂站低压用电系统的通信服务 …… 31

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国电力系统厂站低压用电标准化工作组(SAC/SWG 21)提出并归口。

本文件起草单位：国网四川省电力公司电力科学研究院、南京南瑞继保电气有限公司、深圳奥特迅电力设备股份有限公司、浙江科畅电子股份有限公司、广东仟舜科技有限公司、国网四川省电力公司、国电南京自动化股份有限公司、中国电力工程顾问集团华北电力设计院有限公司、中国电力科学研究院有限公司、智洋创新科技股份有限公司、安徽南瑞继远电网技术有限公司、北京四方继保自动化股份有限公司、国网四川综合能源服务有限公司、河北创科电子科技有限公司、大连市旅顺电力电子设备有限公司、国网辽宁省电力有限公司电力科学研究院、深圳市泰昂能源科技股份有限公司、广州优维电子科技有限公司、施耐德电气（中国）有限公司、四川电力设计咨询有限责任公司、国网河北省电力有限公司电力科学研究院、深圳供电局有限公司、国网冀北电力有限公司张家口供电公司、贵州电网有限责任公司电力科学研究院、山东泰开自动化有限公司、许继电源有限公司。

本文件主要起草人：董汉彬、李晶、罗洋、代小翔、胡绍谦、王凤仁、许昭德、李淑琦、张振乾、方源、汪金礼、陈书欣、徐玉凤、钱莉莉、范松海、羊静、赵梦欣、向博、张宗喜、马小敏、杨玥坪、陈实、刘黎、王洪梅、熊晓丹、刘国永、李永祥、张武洋、马延强、赵砚青、王亚莉、周广渊、刘忠祥、赵应龙、李秉宇、杨忠亮、刘斌、王洪、李迎春、徐伟、罗治军。



# 电力厂站低压用电系统信息架构及接口 技术规范

## 1 范围

本文件规定了电力厂站低压用电系统信息的架构、模型和接口的相关技术要求，描述了相应的测试方法。

本文件适用于发电厂、变电站等电力工程低压交直流用电系统中，监控信息通信的研发、设计及制造。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2900.1 电工术语 基本术语

GB/T 2900.33 电工术语 电力电子技术

GB/T 32890 继电保护 IEC 61850 工程应用模型

GB/T 36572 电力监控系统网络安全防护导则

DL/T 860（所有部分）电力自动化通信网络和系统

DL/T 860.74 电力自动化通信网络和系统 第 7-4 部分: 基本通信结构 兼容逻辑节点类和数据类

DL/T 1146 DL/T 860 实施技术规范

## 3 术语和定义

GB/T 2900.1、GB/T 2900.33 和 DL/T 860（所有部分）界定的以及下列术语和定义适用于本文件。

电力厂站低压用电系统 low voltage auxiliary power system for electric power stations and substations: APS

在正常或事故情况下，为发电厂、变电站等电力工程的低压设备和相关通信设备提供电源的系统。

## 4 缩略语

下列缩略语适用于本文件。

ATSE: 自动转换开关装置(Automatic Transfer Switching Equipment)

IED: 智能电子设备 (Intelligent Electronic Device)

INV: 逆变电源装置(Inverter)

LLN0: 逻辑节点零 (Logical Node Zero)

LN:逻辑节点(Logical Node)

LPHD: 物理设备信息的逻辑节点 (Logical Node of Physical Device Information)

UPS: 不间断电源装置 (Uninterruptible Power Supply)

## 5 架构

### 5.1 系统结构

APS 的结构如图 1 所示，包含：交流电源、直流电源、交流保安电源、交流不间断电源、直流变换电源和逆变电源。

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_428_992_1242.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 1 APS 结构示意图</div>


### 5.2 网络架构

#### 5.2.1 拓扑结构

网络拓扑结构应满足以下要求：

a）选用工作可靠、结构简单和易于维护的网络结构；

b）重要节点设备采用冗余配置，交流保安电源通过独立 IED 就地接入网络；

c）APS 内任一信息设备或组件发生故障时应自动隔离，不影响正常设备或组件的工作；

d）根据工程特点和技术经济条件，设备组网在集中式、分层集中式和分布式三种结构中选取。

#### 5.2.2 集中式

APS 的设备主要通过一个或非常少量的 IED 接入站控层网络，与各个设备之间宜采用串行通信等通用标准交换信息。集中式结构的 IED 采用冗余配置，双机互为热备用，结构示意图见图 2。

<div style="text-align: center;"><img src="imgs/img_in_image_box_232_358_975_787.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2 集中式结构示意图</div>


#### 5.2.3 分层集中式

为了较高的经济性、适用性和一定的互操作性，APS中各类电源中的设备通过独立的电源 IED 接入站控层网络，其结构示意图见图 3。

<div style="text-align: center;"><img src="imgs/img_in_image_box_282_988_920_1300.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 3 分层集中式结构示意图</div>


#### 5.2.4 分布式

为使设备（如充电装置、馈线柜及蓄电池检测等）具备互操作性和互换性，可采用分布式结构通过各自独立的 IED 接入站控层网络，其结构示意图见图 4。

<div style="text-align: center;"><img src="imgs/img_in_image_box_315_350_859_1416.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图 4 分布式结构示意图</div>


### 5.3 信息交互

信息的交流互动应满足以下要求：

a）APS 内各采集、监视、告警、控制、人机接口和存储等功能模块（设备）的信息交互；

b）与监控、集控、调度、生产信息管理系统等其他系统的信息交互；

c) APS 的信息分级处理、分层存储，实现运行数据、动作信息、告警信息、控制命令等业务数据汇聚和处理；

d）在站控层网络失效的情况下，设备独立完成就地监控；

e）按照 GB/T 36572 规定的网络安全防护要求。

### 5.4 模型要求

信息模型应满足以下要求：

a）符合 DL/T 860（所有部分）的建模原则；

b）具备兼容电源设备已有和新增信息模型的能力；

c）逻辑设备用于区分不同类型电源；

d）逻辑节点反映各类电源的逻辑功能；

e) 逻辑功能建模应优先选择 DL/T 860（所有部分）、DL/T 1146 和 GB/T 32890 确立的逻辑节点；

f) 按照 DL/T 860（所有部分）扩展原则创建新的逻辑节点模型，不宜采用通用输入输出（GGIO）、自动过程控制（GAPC）等通用逻辑节点作为逻辑功能模型。

### 5.5 接口要求

在架构上接口应满足以下要求：

a）接入电力监控系统时遵照“安全分区、网络专用、横向隔离、纵向认证”；

b) 代码全面可控，避免各类中间件引起的安全漏洞；

c) 支持信息交互的全面、高效、实时和安全；

d）支持运行数据、动作信息、告警信息、控制命令及状态监测等实时信息的汇集；

e）支持实时信息采集、装置控制和系统管理等监控数据类型的交互；

f）适应嵌入式装置交互的需求；

g）重要节点设备接口按冗余设计。

## 6 模型

### 6.1 功能分解

依据 APS 不同类型电源包含的不同逻辑功能，各电源及其逻辑功能的分解见图 5。信息模型按照图 5 所示的电源类型和逻辑功能组织。

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_199_953_1447.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 5 APS 的电源及功能分解图</div>


### 6.2 建模通则

6.2.1 系统的信息应在 IED 上创建模型。每个 IED 对应一个物理设备。物理设备仅包含一个服务对象。该服务对象应包含反映电源信息的逻辑设备。

6.2.2 按照 APS 实际组网结构，每个 IED 的模型可包含一个或多个反映不同类型电源信息的逻辑设备。例如在 IED 集中式网络结构中，IED 模型包括多个逻辑设备，分别反映不同类型电源信息模型；在 IED 分布式网络结构中，每个 IED 仅包含一个反映一种电源信息的逻辑设备。

6.2.3 逻辑设备按照 APS 的电源类型应分类为：

a）交流电源类逻辑设备，inst名为“ACPS”；

b）直流电源类逻辑设备，inst名为“DCPS”；

c）交流不间断电源类逻辑设备，inst名为“UPSS”；

d）直流变换电源类逻辑设备，inst名为“DDPS”；

e）逆变电源逻辑类逻辑设备，inst名为“INVS”；

f）交流保安电源类逻辑设备，inst名为“ACSPS”。

注：“inst”智能电子设备内逻辑设备的标识，其值不能是空字符串。

6.2.4 IED 模型包含多个同类型逻辑设备时，其 inst 名应在该类型电源逻辑设备 inst 名后添加两位数字组成。例如两个交流电源逻辑设备，其名称分别为 ACPS01、ACPS02。

6.2.5 各类电源的逻辑功能模型对应的逻辑节点应按附录 A 中所列选取。

### 6.3 信息建模

#### 6.3.1 模型结构

IED 每个逻辑设备模型应由其对应类型电源的公用信息模型和逻辑功能信息模型组成。公用信息模型由 LLN0 和 LPHD 逻辑节点实例组成，其数据集和控制块应由 LLN0 创建。逻辑功能信息模型应由反映电源全部逻辑功能的逻辑节点实例组成。对于同一种逻辑节点，其逻辑节点前缀表示逻辑功能的应用类别，例如 cheZPUS 和 chmZPUS 分别表示充电装置监测功能和充电模块监测功能；其逻辑节点实例号用于区分同类逻辑功能的不同实例，例如 aciMMXU1、aciMMXU2。

#### 6.3.2 交流电源

交流电源信息模型包括：交流进线测量及状态检测、电能计量监测、交流自动切换、交流母线测量及状态检测、交流馈线状态检测及控制等，其对应的逻辑节点实例见表1。

<div style="text-align: center;">表 1 交流电源信息模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>交流进线测量及状态检测</td><td style='text-align: center;'>aci</td><td style='text-align: center;'>ZACI</td><td style='text-align: center;'>交流输入电压、电流、频率；交流缺相、避雷器故障、电流电压故障告警</td></tr><tr><td rowspan="2">电能计量监测</td><td style='text-align: center;'>—</td><td style='text-align: center;'>MMTR</td><td style='text-align: center;'>交流进线电能计量</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>MHAI</td><td style='text-align: center;'>交流进线谐波和间谐波测量</td></tr><tr><td rowspan="2">交流自动切换</td><td style='text-align: center;'>aas</td><td style='text-align: center;'>ZDAC</td><td style='text-align: center;'>交流自动切换，管理 ATSE 运行状态。如自动/手动设置，主备状态</td></tr><tr><td style='text-align: center;'>gds</td><td style='text-align: center;'>ZDPS</td><td style='text-align: center;'>通用双投开关，控制双投开关的合闸位置，检测开关位置及脱扣报警或熔断器报警</td></tr></table>

<div style="text-align: center;">表 1 交流电源信息模型（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>交流母线测量及状态检测</td><td style='text-align: center;'>acb</td><td style='text-align: center;'>ZACB</td><td style='text-align: center;'>交流母线电压、电流、频率、电阻等测量信息，以及对应的缺相、绝缘等告警</td></tr><tr><td style='text-align: center;'>交流馈线状态检测及控制</td><td style='text-align: center;'>fms</td><td style='text-align: center;'>ZABR</td><td style='text-align: center;'>交流馈线电压、电流、功率、电阻等测量信息；馈线开关位置状态信息；馈线脱扣、熔断、绝缘等告警信息</td></tr></table>

#### 6.3.3 直流电源

直流电源信息模型包括：交流进线测量及状态检测、交流自动切换、充电装置运行状态检测及控制、蓄电池组检测、直流母线状态检测、直流馈线状态检测及控制、硅降压装置状态检测等，其对应的逻辑节点实例见表2。

<div style="text-align: center;">表 2 直流电源信息模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>交流进线测量及状态检测</td><td style='text-align: center;'>aci</td><td style='text-align: center;'>ZACI</td><td style='text-align: center;'>检测交流缺相、防雷器故障、零序电流及运行状态</td></tr><tr><td rowspan="2">交流自动切换</td><td style='text-align: center;'>aas</td><td style='text-align: center;'>ZDAC</td><td style='text-align: center;'>交流自动切换，管理 ATSE 运行状态。如自动/手动设置，主备状态</td></tr><tr><td style='text-align: center;'>gds</td><td style='text-align: center;'>ZDPS</td><td style='text-align: center;'>通用双投开关，控制双投开关的合闸位置，检测开关位置及脱扣报警或熔断器报警</td></tr><tr><td rowspan="2">充电装置运行状态检测及控制</td><td style='text-align: center;'>che</td><td style='text-align: center;'>ZDUG</td><td style='text-align: center;'>充电装置检测，检测直流电压、电流、绝缘电阻、运行状态</td></tr><tr><td style='text-align: center;'>chm</td><td style='text-align: center;'>ZDUS</td><td style='text-align: center;'>充电模块检测，检测充电模块输出电压、电流、运行状态，控制模块开关机、均浮充</td></tr><tr><td rowspan="2">蓄电池组检测</td><td style='text-align: center;'>btg</td><td style='text-align: center;'>ZBTG</td><td style='text-align: center;'>蓄电池组测量，检测蓄电池组电压、电流、环境温度及运行状态</td></tr><tr><td style='text-align: center;'>bts</td><td style='text-align: center;'>ZBTS</td><td style='text-align: center;'>蓄电池组单只电池，检测单只电池温度、电压、内阻、连接电阻及运行状态</td></tr><tr><td style='text-align: center;'>直流母线状态检测</td><td style='text-align: center;'>dbm</td><td style='text-align: center;'>ZDCB</td><td style='text-align: center;'>直流母线测量及其告警信息</td></tr><tr><td style='text-align: center;'>直流馈线状态检测及控制</td><td style='text-align: center;'>fms</td><td style='text-align: center;'>ZDBR</td><td style='text-align: center;'>直流馈线测量信息、开关位置状态信息，以及相关告警信息</td></tr><tr><td style='text-align: center;'>硅降压装置状态检测</td><td style='text-align: center;'>srs</td><td style='text-align: center;'>ZSRS</td><td style='text-align: center;'>硅降压，检测硅降压装置硅链投入节数、断硅位置、运行方式、断硅报警及运行状态</td></tr></table>

#### 6.3.4 交流不间断电源

交流不间断电源信息模型包括：交流进线测量及状态检测、交流旁路进线状态检测、交流自动切换、直流进线状态检测、UPS运行状态检测及控制、交流母线状态检测、交流馈线状态检测及控制等，其对应的逻辑节点实例见表3。

<div style="text-align: center;">表 3 交流不间断电源信息模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>交流进线测量及状态检测</td><td style='text-align: center;'>aci</td><td style='text-align: center;'>ZACI</td><td style='text-align: center;'>检测交流缺相、避雷器故障、运行状态</td></tr><tr><td style='text-align: center;'>交流旁路进线状态检测</td><td style='text-align: center;'>aci</td><td style='text-align: center;'>ZACI</td><td style='text-align: center;'>检测交流缺相、避雷器故障、运行状态</td></tr><tr><td rowspan="2">交流自动切换</td><td style='text-align: center;'>aas</td><td style='text-align: center;'>ZDAC</td><td style='text-align: center;'>交流自动切换，管理 ATSE 运行状态。如自动/手动设置，主备状态</td></tr><tr><td style='text-align: center;'>gds</td><td style='text-align: center;'>ZDPS</td><td style='text-align: center;'>通用双投开关，控制双投开关的合闸位置，检测开关位置及脱扣报警或熔断器报警</td></tr><tr><td style='text-align: center;'>直流进线状态检测</td><td style='text-align: center;'>dim</td><td style='text-align: center;'>ZDCI</td><td style='text-align: center;'>直流进线开关位置状态</td></tr><tr><td rowspan="2">UPS 运行状态检测及控制</td><td style='text-align: center;'>ups</td><td style='text-align: center;'>ZUIG</td><td style='text-align: center;'>UPS 检测，检测 UPS 输出电压、电流、频率、均流不均衡度、运行状态，控制开关机</td></tr><tr><td style='text-align: center;'>umd</td><td style='text-align: center;'>ZUIS</td><td style='text-align: center;'>UPS 模块检测，检测 UPS 模块输出电压、电流、运行状态，控制开关机</td></tr><tr><td style='text-align: center;'>交流母线测量及状态</td><td style='text-align: center;'>acb</td><td style='text-align: center;'>ZACB</td><td style='text-align: center;'>交流母线监测</td></tr><tr><td style='text-align: center;'>交流馈线状态检测及控制</td><td style='text-align: center;'>fms</td><td style='text-align: center;'>ZABR</td><td style='text-align: center;'>交流馈线电压、电流、功率等测量信息；馈线开关位置状态信息；馈线脱扣、熔断、绝缘等告警信息</td></tr></table>

#### 6.3.5 直流变换电源

直流变换电源信息模型包括：直流进线测量及状态检测、直流变换运行状态检测及控制、直流母线状态检测、直流馈线状态检测及控制等，其对应的逻辑节点实例见表4。

<div style="text-align: center;">表 4 直流变换电源信息模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>直流进线测量及状态检测</td><td style='text-align: center;'>dim</td><td style='text-align: center;'>ZDCI</td><td style='text-align: center;'>直流进线开关位置状态</td></tr><tr><td rowspan="2">直流变换电源装置运行状态检测及控制</td><td style='text-align: center;'>dis</td><td style='text-align: center;'>ZDUG</td><td style='text-align: center;'>直流变换电源装置检测，检测直流电压、电流、运行状态</td></tr><tr><td style='text-align: center;'>dis</td><td style='text-align: center;'>ZDUS</td><td style='text-align: center;'>直流变换电源检测，检测直流变换模块输出电压、电流、运行状态，控制模块开关机</td></tr><tr><td style='text-align: center;'>直流母线状态检测</td><td style='text-align: center;'>dbm</td><td style='text-align: center;'>ZDCB</td><td style='text-align: center;'>直流母线监测</td></tr><tr><td style='text-align: center;'>直流馈线状态检测及控制</td><td style='text-align: center;'>fms</td><td style='text-align: center;'>ZDBR</td><td style='text-align: center;'>直流馈线测量信息、开关位置状态信息，以及相关告警信息</td></tr></table>

#### 6.3.6 逆变电源

逆变电源信息模型包括：交流旁路进线测量及状态检测、交流自动切换、直流进线状态检测、逆变电源装置运行状态检测及控制、交流母线状态检测、交流馈线状态检测及控制等，其对应的逻辑节点实例见表5。

<div style="text-align: center;">表 5 逆变电源信息模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>交流旁路进线测量及状态检测</td><td style='text-align: center;'>acbi</td><td style='text-align: center;'>ZACI</td><td style='text-align: center;'>检测交流旁路缺相、避雷器故障、零序电流、运行状态</td></tr><tr><td style='text-align: center;'>直流进线状态检测</td><td style='text-align: center;'>dim</td><td style='text-align: center;'>ZDCI</td><td style='text-align: center;'>直流进线开关位置状态</td></tr><tr><td rowspan="2">INV运行状态检测及控制</td><td style='text-align: center;'>ups</td><td style='text-align: center;'>ZUIG</td><td style='text-align: center;'>INV检测，检测INV输出电压、电流、频率、均流不均衡度、运行状态，控制开关机</td></tr><tr><td style='text-align: center;'>umd</td><td style='text-align: center;'>ZUIS</td><td style='text-align: center;'>INV模块检测，检测INV模块输出电压、电流、运行状态，控制开关机</td></tr><tr><td style='text-align: center;'>交流母线状态检测</td><td style='text-align: center;'>acb</td><td style='text-align: center;'>ZACB</td><td style='text-align: center;'>交流母线监测</td></tr><tr><td style='text-align: center;'>交流馈线状态检测及控制</td><td style='text-align: center;'>fms</td><td style='text-align: center;'>ZABR</td><td style='text-align: center;'>交流馈线电压、电流、功率等测量信息；馈线开关位置状态信息；馈线脱扣、熔断、绝缘等告警信息</td></tr></table>

#### 6.3.7 交流保安电源

交流保安电源信息模型可包括：交流进线测量及状态检测、发电机状态检测及控制、交流自动切换、交流母线状态检测、交流馈线状态检测及控制等，其对应的逻辑节点实例见表6。

<div style="text-align: center;">表 6 交流保安电源信息模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>逻辑功能</td><td style='text-align: center;'>逻辑节点前缀</td><td style='text-align: center;'>逻辑节点</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>交流进线测量及状态检测</td><td style='text-align: center;'>acbi</td><td style='text-align: center;'>ZACI</td><td style='text-align: center;'>检测交流旁路缺相、避雷器故障、运行状态</td></tr><tr><td style='text-align: center;'>发电机状态检测及控制</td><td style='text-align: center;'>gn</td><td style='text-align: center;'>ZACP</td><td style='text-align: center;'>发电机保安电源测量、告警</td></tr><tr><td rowspan="2">交流自动切换</td><td style='text-align: center;'>aas</td><td style='text-align: center;'>ZDAC</td><td style='text-align: center;'>交流自动切换，管理 ATSE 运行状态。如自动/手动设置，主备状态</td></tr><tr><td style='text-align: center;'>gds</td><td style='text-align: center;'>ZDPS</td><td style='text-align: center;'>通用双投开关，控制双投开关的合闸位置，检测开关位置及脱扣报警或熔断器报警</td></tr><tr><td style='text-align: center;'>交流母线状态检测</td><td style='text-align: center;'>acb</td><td style='text-align: center;'>ZACB</td><td style='text-align: center;'>交流母线电压、电流、频率等测量信息，以及对应的缺相、绝缘等告警</td></tr><tr><td style='text-align: center;'>交流馈线状态检测及控制</td><td style='text-align: center;'>fms</td><td style='text-align: center;'>ZABR</td><td style='text-align: center;'>交流馈线电压、电流、功率等测量信息；馈线开关位置状态信息；馈线脱扣、熔断、绝缘等告警信息</td></tr></table>

## 7 接口

### 7.1 基本功能

信息接口应具备以下功能：

a）在加密及身份认证等安全防护措施下，与多个其他系统同时进行数据交互；

b）模拟量和状态量的数据主动上送其他系统；

c）其他系统读取、修改参数或定值；

d）APS 设备装置的本地控制或远方控制；

e）文件获取、下载和删除；

f）远程倒闸、远程核对性放电等远方操控；

g）蓄电池在线监测、绝缘监测、剩余电流监测等历史数据读取。

### 7.2 技术参数

信息接口应满足以下技术指标：

a）IED 报文应与设备实际状态同步，实时动态数据延迟应不超过 200 ms；

b）数据交互支持不少于16个客户端的并发通信；

c）对使用编码对时的设备，应优先使用未经幅度调制的串行时间交换码 $$ IRIG-B(DC) $$ 对时方式；

d）接入站控层的网络宜采用双10 M/100 M。

### 7.3 品质与时标

IED 模型中数据品质和时标应源于数据采集设备，当其未标注品质或时标时，按以下方法处理：

a）当采集设备不具备标注品质时，在 IED 与其通信正常则品质标注为有效，通信异常则品质标注为无效或可疑；

b）当 IED 获取的数据未标注时标，则 IED 以获取数据的时刻作为时标标注。

### 7.4 网络接口

7.4.1 IED 应配备 2 个及以上 RJ45 网口，支持站控层的冗余网络通信。

7.4.2 适用 APS 接口的 DL/T 860（所有部分）通信服务见附录 B。

## 8 测试

### 8.1 一致性测试

一致性测试内容根据设备情况，按照 DL/T 860（所有部分）规定选择相关功能项进行测试。测试项目见表 7 所列，其中有“✓”的项目应选择并完成测试。

<div style="text-align: center;">表 7 一致性测试内容</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>测试项目</td><td style='text-align: center;'>测试标号</td><td style='text-align: center;'>必测项</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>文档和版本控制检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>配置文件检测</td><td style='text-align: center;'>sCnf6</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>数据模型检验 $ ^{a} $</td><td style='text-align: center;'>sMd113</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4</td><td colspan="3">抽象通信服务接口(ACSI)模型和服务的映射检验</td></tr><tr><td style='text-align: center;'>4.1</td><td style='text-align: center;'>应用关联检验</td><td style='text-align: center;'>sAss3, sAssN2, sAssN3, sAssN4, sAssN5</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.2</td><td style='text-align: center;'>服务器/逻辑设备/逻辑节点和数据模型检验</td><td style='text-align: center;'>sSrv5, sSrv7, sSrv9, sSrv10</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.3</td><td style='text-align: center;'>数据集模型检验</td><td style='text-align: center;'>sDs10, sDsN1</td><td style='text-align: center;'>✓</td></tr></table>

<div style="text-align: center;">表 7 一致性测试内容（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>测试项目</td><td style='text-align: center;'>测试标号</td><td style='text-align: center;'>必测项</td></tr><tr><td style='text-align: center;'>4.4</td><td style='text-align: center;'>取代模型检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>定值组控制模型检验</td><td style='text-align: center;'>sSgN4</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.6</td><td style='text-align: center;'>非缓存报告模型检验</td><td style='text-align: center;'>sRp1, sRp2, sRp3, sRp8, sRpN4</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.7</td><td style='text-align: center;'>缓存报告模型检验</td><td style='text-align: center;'>sBr1, sBr2, sBr3, sBr8, sBrN4</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.8</td><td style='text-align: center;'>日志类模型检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.9</td><td colspan="3">控制模型检验</td></tr><tr><td style='text-align: center;'>4.9.1</td><td style='text-align: center;'>通用控制检验</td><td style='text-align: center;'>sCtl1, sCtl6, sCtl8, sCtl9, sCtl10, sCtl11, sCtl15, sCtl30</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.9.2</td><td style='text-align: center;'>DOns控制模式检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.9.3</td><td style='text-align: center;'>SBOns控制模式检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.9.4</td><td style='text-align: center;'>DOes控制模式检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.9.5</td><td style='text-align: center;'>SBOes控制模式检验</td><td style='text-align: center;'>sSBOes1, sSBOes6, sSBOes8</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4.10</td><td style='text-align: center;'>时间和时间同步模型检验</td><td style='text-align: center;'>sTm1, sTm2, sTmN1</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.11</td><td style='text-align: center;'>文件传输检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4.12</td><td style='text-align: center;'>服务跟踪模型检验</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td colspan="4">注: 必测项中“✓”表示应选择的项目,“—”表示可选择的项目。</td></tr><tr><td colspan="4">a 数据模型检验应满足DL/T 860(所有部分)和第6章的要求。</td></tr></table>

### 8.2 应用测试

8.2.1 一致性测试不能代替工程特定的有关系统的测试，特定工程所制造或集成的系统应对实际系统通过工厂测试确认通信功能满足设计要求。

8.2.2 应用测试应根据系统配置情况来测试具体的服务器/逻辑设备/逻辑节点和数据模型、数据集模型、定值组控制模型（如果有）、控制模型（如果有）。

## 附录 A

(规范性)

电力厂站低压用电系统的设备模型

### A.1 概述

本附录列出了按照 DL/T 860.74 扩展原则定义的各类电源设备功能模型对应逻辑节点类。每个逻辑节点类均省略了所含通用逻辑节点（Common LN）的强制数据对象，实际设备模型的逻辑节点类首先需要包含这些强制数据对象，其中，DL/T 860.74 已定义的数据对象中强制数据用 M 表示，可选数据用 O 表示。本文件扩展的条件强制数据对象用 C 表示，扩展的可选数据对象用 E 表示。

### A.2 交流进线 ZACI

依据各电源的逻辑功能分解，含交流进线的有交流电源、直流电流、交流不间断电源、逆变电源和交流保安电源，其状态、测量及定值信息见表 A.1。

<div style="text-align: center;">表 A.1 交流进线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACI类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>AcInErr</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线故障(总故障)</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInArresF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>避雷器故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInVHiA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线A相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVHiB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线B相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVHiC</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线C相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInVLoA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线A相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVLoB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线B相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVLoC</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线C相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInAHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线过载</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInAHiA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线A相过载</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInAHiB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线B相过载</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInAHiC</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线C相过载</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInPhLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线缺相</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInPhLosA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线A相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInPhLosB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线B相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInPhLosC</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线C相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线监测装置通信故障</td><td style='text-align: center;'>C</td></tr></table>

<div style="text-align: center;">表 A.1 交流进线（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACI类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>AcInVAComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线A相电压表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVBComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线B相电压表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVCComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线C相电压表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInAAComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线A相电流表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInABComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线B相电流表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInACComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线C相电流表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInEMComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流进线电能表通信故障</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>AcInVoltAB</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线AB电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVoltBC</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线BC电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVoltCA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线CA电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVoltA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线A相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInVoltB</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线B相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInVoltC</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线C相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInCurrA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线A相电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInCurrB</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线B相电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInCurrC</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线C相电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInFreq</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线频率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInPow</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线电能</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInWattA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线A相有功功率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInWattB</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线B相有功功率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInWattC</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线C相有功功率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVArA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线A相无功功率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVArB</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线B相无功功率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInVArC</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流进线C相无功功率</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>AcInOVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>交流进线过压报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInOVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>交流进线过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInUVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>交流进线欠压报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInUVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>交流进线欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInOLSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>交流进线过载报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AcInOLRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>交流进线过载回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>SmpProd</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>采样间隔</td><td style='text-align: center;'>E</td></tr></table>

### A.3 直流进线 ZDCI

依据各电源的逻辑功能分解，含直流进线的有交流不间断电源、直流变换电源和逆变电源，其状态、测量及定值信息见表 A.2。

<div style="text-align: center;">表 A.2 直流进线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDCI类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>DcInErr</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流进线故障(总故障)</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DcInOvVol</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流进线过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DcInUnVol</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流进线欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DcInOvCur</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流进线过流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DcInComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流进线监测设备通信故障</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>DcInVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>直流进线电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DcInCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>直流进线电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>AcInWatt</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>直流进线功率</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>DcInOVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>直流进线过压报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DcInOVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>直流进线过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DcInUVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>直流进线欠压报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DcInUVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>直流进线欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DcInOASet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>直流进线过流报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DcInOARSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>直流进线过流回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>SMPProd</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>采样间隔</td><td style='text-align: center;'>E</td></tr></table>

### A.4 交流母线 ZACB

依据各电源的逻辑功能分解，含交流母线的有交流电源、交流不间断电源、逆变电源和交流保安电源，其状态、测量及定值信息见表A.3。

<div style="text-align: center;">表 A.3 交流母线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACB类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>VExp</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线电压异常</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VHiA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线A相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VHiB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线B相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VHiC</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线C相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VLoA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线A相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VLoB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线B相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VLoC</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线C相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>PhLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线缺相</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>PhsALos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线A相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>PhsBLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线B相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>PhsCLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线C相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>RLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线绝缘接地电阻低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线监测设备通信故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VMAComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线A相电压表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VMBComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线B相电压表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VMCComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线C相电压表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AMAComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线A相电流表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AMBComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线B相电流表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>AMCComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流母线C相电流表通信故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>绝缘监测设备通信故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsDevExp</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>绝缘监测设备异常</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>ACPhsABVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线AB电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsBCVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线BC电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsCBVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线CA电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsAVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线A相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsBVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线B相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsCVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线C相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsACur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线A相电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACPhsBCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线B相电流</td><td style='text-align: center;'>C</td></tr></table>

<div style="text-align: center;">表 A.3 交流母线（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACB类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>ACPhsCCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线C相电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACBusHz</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线频率</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>BusGInsRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>母线对地绝缘电阻</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>ACBOvVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线过压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACBOvVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACBUnVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线欠压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACBUnVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BusRLoSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地绝缘电阻过低报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BusRLoRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地绝缘电阻过低回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>SMPProd</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>采样间隔</td><td style='text-align: center;'>E</td></tr></table>

### A.5 交流支路 ZABR

依据各电源的逻辑功能分解，含交流支路的有交流电源中的交流进线、交流馈线，直流电源中的交流进线，交流不间断电源中的交流进线、交流旁路进线、交流馈线，逆变电源中的交流进线、交流馈线，交流保安电源中的交流进线、交流馈线。交流支路不包含交流自动切换装置和通用双投开关装置，其状态、测量及控制信息见表A.4。

<div style="text-align: center;">表 A.4 交流支路</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZABR类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>TripAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>脱扣报警或熔断器报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>SwiPos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>开关位置:1表示合;0表示分</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>BpPhLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路缺相</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>BpPhsALos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路A相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BpPhsBLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路B相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BpPhsCLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路C相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsRisLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>绝缘电阻降低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ResCurF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>剩余电流过大</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsMDComF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>绝缘监测装置通信故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsMDAbn</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>绝缘监测装置异常</td><td style='text-align: center;'>C</td></tr></table>

<div style="text-align: center;">表 A.4 交流支路（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZABR类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>ACPhsABVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 AB 电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsBCVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 BC 电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsCBVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 CA 电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsAVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 A 相电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsBVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 B 相电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsCVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 C 相电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsACur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 A 相电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsBCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 B 相电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACPhsCCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流母线 C 相电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>En</td><td style='text-align: center;'>DEL</td><td style='text-align: center;'>电能</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>Watt</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>有功功率</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>VAr</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>无功功率</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>GndInsRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>对地绝缘电阻</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>ResA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>剩余电流</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>SwiCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>开关分合控制:1 表示合;0 表示分</td><td style='text-align: center;'>E</td></tr></table>

### A.6 直流母线 ZDCB

依据各电源的逻辑功能分解，含直流母线的有直流电源和直流变换电源，其状态、测量、定值及控制信息见表 A.5。

<div style="text-align: center;">表 A.5 直流母线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDCB类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>HMVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>合闸母线过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>HMVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>合闸母线欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>PosHMVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>正合闸母线对地电压过低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>NegHMVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>负合闸母线对地电压过低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>KMVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>控制母线过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>KMVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>控制母线欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>PosKMVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>正合闸母线对地电压过低</td><td style='text-align: center;'>E</td></tr></table>

<div style="text-align: center;">表 A.5 直流母线（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDCB类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>NegKMVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>负合闸母线对地电压过低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>绝缘降低</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsPClsBLA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>正合闸母线对地绝缘降低报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsNClsBLA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>负合闸母线对地绝缘降低报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsPClsBLW</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>正合闸母线对地绝缘降低预警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsNClsBLW</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>负合闸母线对地绝缘降低预警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsPCtlBLA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>正控制母线对地绝缘降低报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNCtlBLA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>负控制母线对地绝缘降低报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsPCtlBLW</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>正控制母线对地绝缘降低预警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNCtlBLW</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>负控制母线对地绝缘降低预警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsACVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流窜入电压高报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GndDifVAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>对地压差告警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DCBinAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流互串告警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsTrGnd</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>瞬间接地报警</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>ClsBusVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>合闸母线电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CtlBusVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>控制母线电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsPClsBV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>正合闸母线对地电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsNClsBV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>负合闸母线对地电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsPCtlBV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>正控制母线对地电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNCtlBV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>负控制母线对地电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsPClsBR</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>正合闸母线对地电阻</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsNClsBR</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>负合闸母线对地电阻</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsPCtlBR</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>正控制母线对地电阻</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNCtlBR</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>负控制母线对地电阻</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsCBGnACV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>窜入交流电压</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>CBOVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线过压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CBOVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CBUVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线欠压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CBUVSetRD</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsUVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地电压欠压报警值</td><td style='text-align: center;'>C</td></tr></table>

<div style="text-align: center;">表 A.5 直流母线（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDCB类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>InsUVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地电压欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsACUSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地串入交流电压欠压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsACURSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地串入交流电压欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsGOVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地电压过压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsGOVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地电压过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsRLASet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地绝缘降低报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsRLARSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地绝缘降低报警回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsRLWSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地绝缘降低预警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsRLWRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>母线对地绝缘降低预警回差值</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>StrNBTest</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>启动不平衡桥测量:1表示启动;0表示无操作</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>StopNBTest</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>停止不平衡桥测量:1表示停止;0表示无操作</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">注:负合闸母线对地电压、负合闸母线对地电阻对应于共正母线情况。</td></tr></table>

### A.7 直流支路 ZDBR

依据各电源的逻辑功能分解，含直流支路的有直流电源中的充电装置输出、直流馈线，直流变换电源中的直流变换电源装置输入、输出、直流馈线，交流不间断电源装置和逆变电源装置中直流输入，其状态、测量及控制信息见表A.6。

注：直流支路不包含通用双投开关装置，但包含直流母联开关、蓄电池回路开关或断路器。

<div style="text-align: center;">表 A.6 直流支路</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDBR 类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>TripAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>脱扣报警或熔断器报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>SwiPos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>开关位置:1 表示合;0 表示分</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsPRLAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路正对地绝缘降低报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsPRLWrn</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路正对地绝缘降低预警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNRLAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路负对地绝缘降低报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNRLWrn</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路负对地绝缘降低预警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsACIn</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路交流串入报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsDCCross</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>直流互串报警</td><td style='text-align: center;'>C</td></tr></table>

<div style="text-align: center;">表 A.6 直流支路（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDBR 类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>InsTrGnd</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>瞬间接地报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>SampDevF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>支路监测模块故障</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>InsPosRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路正对地绝缘电阻</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsNegRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路负对地绝缘电阻</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsTrPRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路正对地瞬间绝缘电阻</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsTrNRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路负对地瞬间绝缘电阻</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>BpVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BpLodCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路负载电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BpWatt</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>支路功率</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>SwiCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>开关分合控制:1表示合;0表示分</td><td style='text-align: center;'>E</td></tr></table>

### A.8 交流自动切换装置 ZDAC

依据各电源的逻辑功能分解，含交流自动切换装置的有交流电源、直流电源、交流不间断电源、逆变电源、交流保安电源，其状态、测量及控制信息见表A.7。

<div style="text-align: center;">表 A.7 交流自动切换装置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDAC 类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>ActStat</td><td style='text-align: center;'>ENS</td><td style='text-align: center;'>主用状态:取值范围 1~3。1 表示 1 号主用;2 表示 2 号主用;3 表示互备</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>MAStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>自动切换的状态:1 表示手动;0 表示自动</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InOvVol</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsAOV</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>A 相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsBOvV</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>B 相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsCOvV</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>C 相过压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InUnVol</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsAUnV</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>A 相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsBUnV</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>B 相欠压</td><td style='text-align: center;'>E</td></tr></table>

<div style="text-align: center;">表 A.7 交流自动切换装置（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDAC类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>InPhsCUnV</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>C相欠压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsALosA</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>A相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsBLosB</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>B相缺相</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsCLos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>C相缺相</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>InPhsAVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>A相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InPhsBVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>B相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InPhsCVolt</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>C相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InPhsACur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>A相电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsBCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>B相电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InPhsCCur</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>C相电流</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InHz</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>频率</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>ActStatCtl</td><td style='text-align: center;'>ENC</td><td style='text-align: center;'>主用状态,取值范围:1~4。1表示1号主用;2表示2号主用;3表示互备;4表示分列运行</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>MACtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>控制模式:1表示手动控制;0表示自动控制</td><td style='text-align: center;'>E</td></tr></table>

### A.9 通用双投开关装置 ZDPS

通用双投开关装置的状态及控制信息见表 A.8。

<div style="text-align: center;">表 A.8 通用双投开关装置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDPS类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>TripAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>双投开关报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ISwiPos</td><td style='text-align: center;'>IPS</td><td style='text-align: center;'>双投开关位置：0表示OFF；1表示I位闭合；2表示Ⅱ位闭合</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>ISwiCtl</td><td style='text-align: center;'>INC</td><td style='text-align: center;'>双投开关分合控制；0表示OFF；1表示I位闭合；2表示Ⅱ位闭合</td><td style='text-align: center;'>E</td></tr></table>

### A.10 充电装置 ZDUG

依据各电源的逻辑功能分解，含充电装置仅有直流电源，充电装置包含整组充电装置的信息和单个充电模块的信息，整组充电装置的状态、测量及控制信息见表A.9。

<div style="text-align: center;">表 A.9 充电装置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDUG类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>ChaFltAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置总故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ChaRunStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置开关状态:1表示开机;0表示关机</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ChaECStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>均充状态:1表示均充;0表示浮充</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ChaEquASta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>均流状态:1表示已均流;0表示不均流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ChaConBat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置关联蓄电池状态:1表示关联;0表示未关联</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACInFlt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInFltPhs</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入缺相</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置输出欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置输出过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>FbdCvtRson</td><td style='text-align: center;'>INC</td><td style='text-align: center;'>禁止转均充原因:取值范围1~3。1表示蓄电池室环境过温;2表示蓄电池单只过压;3表示监测装置等其他异常</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>FCvtBRson</td><td style='text-align: center;'>INC</td><td style='text-align: center;'>浮充转均充原因:取值范围1~4。1表示手动启动;2表示自动定时启动;3表示单体欠压;4表示远程启动</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BCvtFRson</td><td style='text-align: center;'>INC</td><td style='text-align: center;'>均充转浮充原因:取值范围1~13。1表示手动终止均充;2表示充满电自动终止均充;3表示蓄电池过温;4表示蓄电池单只过压;5表示监测装置等其他异常;6表示远程控制</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>DCOutV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>充电装置输出电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>充电装置输出电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutRip</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>充电装置输出波纹电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DCOutCpImb</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>充电装置输出电流不均衡度</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>DevCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>开关机控制:0表示关机控制;1表示开机控制</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ECCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>均充控制:0表示停止均充;1表示启动均充</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>LocCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>本地/远程控制:0表示本地操作,不允许远程开关和均充控制;1表示允许远程开关机和均充控制</td><td style='text-align: center;'>E</td></tr></table>

### A.11 充电模块 ZDUS

依据各电源的逻辑功能分解，含充电装置仅有直流电源，充电装置包含整组充电装置整流充电模块组的信息和单个充电模块的信息，充电模块的状态、测量及控制信息见表 A.10。

<div style="text-align: center;">表 A.10 充电模块</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZDUS类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>ChaFltAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>整流充电模块故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ChaRunStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>整流充电模块开关状态:1表示开机;0表示关机</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACInFlt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACInVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInFltPhs</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入缺相</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置输出欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>充电装置输出过压</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>DCOutV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>充电装置输出电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DCOutA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>充电装置输出电流</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>DevCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>开关机控制:1表示开机控制;0表示关机控制</td><td style='text-align: center;'>E</td></tr></table>

### A.12 蓄电池组 ZBTG

依据各电源的逻辑功能分解，含蓄电池组仅有直流电源，蓄电池组包含蓄电池整组的信息和单只蓄电池的信息，蓄电池组的状态、测量、定值及控制信息见表 A.11。

<div style="text-align: center;">表 A.11 蓄电池组</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZBTG类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>ChaSta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池充电状态：1表示充电；0表示非充电</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>DisSta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池放电报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>TmpHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池室环境温度过高</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池组电压过高</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池组电压过低</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ConStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池离线状态（含内部开路）</td><td style='text-align: center;'>E</td></tr></table>

<div style="text-align: center;">表 A.11 蓄电池组（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZBTG类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>BatImb</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>电池电压均衡状态:1表示均衡;0表示不均衡</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CapSta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池容量异常状态</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CoreSta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>电池核容状态:1表示正在核容</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InsSta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池绝缘降低状态</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InsFltNo</td><td style='text-align: center;'>INS</td><td style='text-align: center;'>单只蓄电池绝缘故障位置号</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CelTmpHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池极柱温度过高(总)</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CelInRHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池内阻过高(总)</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CelVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池电压过高(总)</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CelVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池电压过低(总)</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>TmpSamF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>温度采集故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CommFlt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>监测装置通信故障</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>BtgV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>蓄电池组电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>BtgA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>蓄电池组充放电电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>Tmp</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>环境温度</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GndRis</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>接地电阻</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>VHiSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池组电压过压报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VHiSetRD</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池组电压过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VLoSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池组电压欠压报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VLoSetRD</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池组电压欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>TmpHiSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>环境温度过高报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>TmpHiSetRD</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>环境温度过高回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CapLoSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池组容量报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VImbSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池不均衡度值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CelOvVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>单体蓄电池电压过压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CelOvVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>单体蓄电池电压过压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CelUnVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>单体蓄电池电压欠压报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CelUnVRSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>单体蓄电池电压欠压回差值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CelOvTSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池极柱温度过高报警值</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CelORisSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池内阻过高报警值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DisCurSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池放电限流值</td><td style='text-align: center;'>E</td></tr></table>

<div style="text-align: center;">表 A.11 蓄电池组（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZBTG类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">定值信息</td></tr><tr><td style='text-align: center;'>StopDisTm</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池终止放电时间值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>StopDVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池终止放电电压值</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>StopDCVSet</td><td style='text-align: center;'>ASG</td><td style='text-align: center;'>蓄电池终止放电单体电压值</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>InnRTest</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>启动电池内阻测试:1表示启动内阻测试;0表示停止内阻测试</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>StrCCTest</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>启动核容测试:1表示启动核容测试;0表示停止核容测试</td><td style='text-align: center;'>E</td></tr></table>

### A.13 单只蓄电池 ZBTS

依据各电源的逻辑功能分解，含蓄电池组仅有直流电源，蓄电池组包含蓄电池整组的信息和单只蓄电池的信息，单只蓄电池的状态及测量信息见表 A.12。

<div style="text-align: center;">表 A.12 单只蓄电池</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZBTS类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>TmpHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池极柱温度过高</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>InRHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池内阻过高</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池电压过高</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>VLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池电压过低</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ConnF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池开路</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>TmpSamF</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>温度采集故障</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ComFlt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池监测装置通信故障</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>Vol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>蓄电池单体电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>InnR</td><td style='text-align: center;'>SVC</td><td style='text-align: center;'>蓄电池内阻</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ConnR</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>连接条电阻</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>PoleTmp</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>极柱温度</td><td style='text-align: center;'>E</td></tr></table>

### A.14 硅链降压装置 ZSRS

依据各电源的逻辑功能分解，含硅链降压装置仅有直流电源，其状态信息见表A.13。

<div style="text-align: center;">表 A.13 硅链降压装置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZSRS 类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>SiEnaNum</td><td style='text-align: center;'>INS</td><td style='text-align: center;'>硅链投入节数</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BrkSiPos</td><td style='text-align: center;'>INS</td><td style='text-align: center;'>断硅位置</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>RunSta</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>自动运行状态:1 表示自动;0 表示手动</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BrkSiAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>断硅报警</td><td style='text-align: center;'>C</td></tr></table>

### A.15 整组交流不间断电源装置/逆变电源装置 ZUIG

依据各电源的逻辑功能分解，交流不间断电源装置/逆变电源装置含装置信息和单模块信息（模块并联结构的装置），装置的状态、测量及控制信息见表A.14。

<div style="text-align: center;">表 A.14 整组交流不间断电源装置/逆变电源装置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZUIG类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>DevStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>开关机状态:1表示开机;0表示关机</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>Flt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>故障</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>ASStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>运行状态:1表示异常;0表示正常</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>RunMod</td><td style='text-align: center;'>INS</td><td style='text-align: center;'>运行模式:取值范围1~3。1表示交流输入逆变输出;2表示直流输入逆变输出;3表示旁路输出</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入电压高</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入电压低</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACBysVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流旁路输入电压高</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACBysVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流旁路输入电压低</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>OutPhV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>输出电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>OutA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>输出电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>OutFreq</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>输出频率</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>OutAImd</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>并机均流不平衡度</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>DevCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>开关机控制:1表示开机控制;0表示关机控制</td><td style='text-align: center;'>E</td></tr></table>

### A.16 交流不间断电源装置/逆变电源装置的模块 ZUIS

依据各电源的逻辑功能分解,交流不间断电源装置/逆变电源装置含装置的信息和单个模块的信息

（模块并联结构的装置），模块的状态、测量及控制信息见表A.15。

<div style="text-align: center;">表 A.15 交流不间断电源装置/逆变电源装置的模块 ZUIS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZUIS类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>FltAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>模块故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>RunStat</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>开关状态:1表示开机;0表示关机</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInFlt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入故障</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入欠压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInVHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入过压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACInFltPhs</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>交流输入缺相</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>ACOutV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>输出电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACOutA</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>输出电流</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">控制信息</td></tr><tr><td style='text-align: center;'>DevCtl</td><td style='text-align: center;'>SPC</td><td style='text-align: center;'>开关机控制;1表示开机控制;0表示关机控制</td><td style='text-align: center;'>E</td></tr></table>

### A.17 交流保安电源 ZACP

依据逻辑功能分解，交流保安电源除前述表中的逻辑节点类外，其快速启动柴油发电机的状态及测量信息见表 A.16。

<div style="text-align: center;">表 A.16 交流保安电源</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACP 类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>GnCCBPos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机控制开关状态:1 表示合;0 表示分</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnCCBAPos</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机控制开关模式:1 表示自动;0 表示手动</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnAMSel</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机自动/手动运行位</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnRStrEna</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机远程启动允许</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnCtlAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机控制报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>UrgHalt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>紧急停机</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnFltHalt</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机故障停机</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>SysSynPrg</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>同步系统正在同步</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>SynSysAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>同步系统报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>CoTmpHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>冷却水温度高</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CoTmpLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>冷却水温度低</td><td style='text-align: center;'>E</td></tr></table>

<div style="text-align: center;">表 A.16 交流保安电源（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACP类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">状态信息</td></tr><tr><td style='text-align: center;'>OilTmpHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>润滑油温度高</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>OilTmpLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>润滑油压力低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CoTmpHiShD</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>机头油箱油位低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>OiPrsLoShD</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>机组超速</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>StrFail</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>启动失败报警</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnDifOp</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机差动保护动作</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnOvCurOp</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机过流动作</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>GnRvPwrOp</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机逆功率保护动作</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>GnWdTmpHi</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机绕组温度高</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>GnRotSpdLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机转速低</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>BatLo</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>蓄电池电压低</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnTestPrg</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>发电机处于试验运行位</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>HzLoAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>频率低报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>HzHiAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>频率高报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VolLoAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>电压低报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>VolHiAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>电压高报警</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>TolAHiAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>总电流过大</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>SglAHiAlm</td><td style='text-align: center;'>SPS</td><td style='text-align: center;'>单相电流过大</td><td style='text-align: center;'>E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>GnPPV</td><td style='text-align: center;'>DEL</td><td style='text-align: center;'>发电机线电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnPhV</td><td style='text-align: center;'>WYE</td><td style='text-align: center;'>发电机相电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnA</td><td style='text-align: center;'>WYE</td><td style='text-align: center;'>发电机电流</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnHz</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机频率</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnTotPF</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机功率因数(P/S)</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnTotW</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机有功功率</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnFldVol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机励磁电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>GnFldAmp</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机励磁电流</td><td style='text-align: center;'>C</td></tr></table>

<div style="text-align: center;">表 A.16 交流保安电源（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">ZACP类</td></tr><tr><td style='text-align: center;'>数据对象名</td><td style='text-align: center;'>公共数据类</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>M/O/C/E</td></tr><tr><td colspan="4">测量信息</td></tr><tr><td style='text-align: center;'>GnSpd</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机转速</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>OilPres</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>润滑油压力</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>OilTmp</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>润滑油温度</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>CoTmp</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>冷却水温度</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>Vol</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>电池电压</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>DifAngClc</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>发电机与同期母线相位差</td><td style='text-align: center;'>E</td></tr><tr><td style='text-align: center;'>ACSecBusV</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流保安母线电压</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>ACSecBusHz</td><td style='text-align: center;'>MV</td><td style='text-align: center;'>交流保安母线频率</td><td style='text-align: center;'>C</td></tr><tr><td colspan="4">注:表中的发电机为柴油发电机。</td></tr></table>

## 附录 B

(资料性)

电力厂站低压用电系统的通信服务

采用 DL/T 860（所有部分）作为系统模型通信服务时，表 B.1 列举了适用于 APS 接口的通信服务。

<div style="text-align: center;">表 B.1 适用 APS 接口的 DL/T 860（所有部分）通信服务</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口</td><td style='text-align: center;'>通信服务</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="3">数据交互初始化</td><td style='text-align: center;'>Associate</td><td style='text-align: center;'>关联</td></tr><tr><td style='text-align: center;'>Abort</td><td style='text-align: center;'>异常中止</td></tr><tr><td style='text-align: center;'>Release</td><td style='text-align: center;'>释放</td></tr><tr><td rowspan="5">数据主动上送</td><td style='text-align: center;'>Report</td><td style='text-align: center;'>报告</td></tr><tr><td style='text-align: center;'>GetBRCBValues</td><td style='text-align: center;'>读缓存报告控制块值</td></tr><tr><td style='text-align: center;'>SetBRCBValues</td><td style='text-align: center;'>设置缓存报告控制块值</td></tr><tr><td style='text-align: center;'>GetURCBValues</td><td style='text-align: center;'>读非缓存报告控制块值</td></tr><tr><td style='text-align: center;'>SetURCBValues</td><td style='text-align: center;'>设置非缓存报告控制块值</td></tr><tr><td rowspan="13">读/写参数</td><td style='text-align: center;'>GetServerDirectory</td><td style='text-align: center;'>服务器目录</td></tr><tr><td style='text-align: center;'>GetLogicalDeviceDirectory</td><td style='text-align: center;'>逻辑设备目录</td></tr><tr><td style='text-align: center;'>GetLogicalNodeDirectory</td><td style='text-align: center;'>逻辑节点目录</td></tr><tr><td style='text-align: center;'>GetDataDirectory</td><td style='text-align: center;'>读数据目录</td></tr><tr><td style='text-align: center;'>GetDataDefinition</td><td style='text-align: center;'>读数据定义</td></tr><tr><td style='text-align: center;'>GetDataValues</td><td style='text-align: center;'>读数据值</td></tr><tr><td style='text-align: center;'>GetDataSetDirectory</td><td style='text-align: center;'>读数据集定义</td></tr><tr><td style='text-align: center;'>GetDataSetValues</td><td style='text-align: center;'>读数据集值</td></tr><tr><td style='text-align: center;'>GetDataDirectory</td><td style='text-align: center;'>读数据目录</td></tr><tr><td style='text-align: center;'>GetDataDefinition</td><td style='text-align: center;'>读数据定义</td></tr><tr><td style='text-align: center;'>GetDataValues</td><td style='text-align: center;'>读数据值</td></tr><tr><td style='text-align: center;'>SetDataValues</td><td style='text-align: center;'>设置数据值</td></tr><tr><td style='text-align: center;'>SetDataSetValues</td><td style='text-align: center;'>设置数据集值</td></tr><tr><td rowspan="6">读/写定值</td><td style='text-align: center;'>GetSGCBValues</td><td style='text-align: center;'>获取定值块属性值</td></tr><tr><td style='text-align: center;'>SelectEditSG</td><td style='text-align: center;'>选择编辑定值组</td></tr><tr><td style='text-align: center;'>SelectActiveSG</td><td style='text-align: center;'>选择激活定值组</td></tr><tr><td style='text-align: center;'>GetSGValues</td><td style='text-align: center;'>获取定值组值</td></tr><tr><td style='text-align: center;'>SetSGValues</td><td style='text-align: center;'>设置定值组值</td></tr><tr><td style='text-align: center;'>ConfirmEditSGValues</td><td style='text-align: center;'>确认编辑定值组值</td></tr></table>

<div style="text-align: center;">表 B.1 适用 APS 接口的 DL/T 860（所有部分）通信服务（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口</td><td style='text-align: center;'>通信服务</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="4">控制、远程操作</td><td style='text-align: center;'>SelectWithValue</td><td style='text-align: center;'>带值选择</td></tr><tr><td style='text-align: center;'>Cancel</td><td style='text-align: center;'>取消</td></tr><tr><td style='text-align: center;'>Operate</td><td style='text-align: center;'>执行</td></tr><tr><td style='text-align: center;'>CommandTermination</td><td style='text-align: center;'>命令终止</td></tr><tr><td rowspan="4">文件传输</td><td style='text-align: center;'>GetFile</td><td style='text-align: center;'>获取文件</td></tr><tr><td style='text-align: center;'>GetFileAttributeValues</td><td style='text-align: center;'>获取文件属性</td></tr><tr><td style='text-align: center;'>SetFile</td><td style='text-align: center;'>设置文件</td></tr><tr><td style='text-align: center;'>DeleteFile</td><td style='text-align: center;'>删除文件</td></tr><tr><td rowspan="5">历史数据读取</td><td style='text-align: center;'>GetLCBValues</td><td style='text-align: center;'>获取日志控制块属性值</td></tr><tr><td style='text-align: center;'>SetLCBValues</td><td style='text-align: center;'>设置日志控制块属性值</td></tr><tr><td style='text-align: center;'>GetLogStatusValues</td><td style='text-align: center;'>获取日志状态</td></tr><tr><td style='text-align: center;'>QueryLogbyTime</td><td style='text-align: center;'>按时间查询日志</td></tr><tr><td style='text-align: center;'>QueryLogAfter</td><td style='text-align: center;'>查询日志</td></tr></table>

