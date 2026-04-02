

# 中华人民共和国国家标准

GB/T 43851—2024

# 制造物流系统互联互通通用要求

# General requirements for interconnection of manufacturing logistics system

2024-04-25 发布

2024-11-01 实施



## 目次

前言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 缩略语 …… 1    
5 集成架构 …… 1    
6 基本要求 …… 2    
6.1 总体要求 …… 2    
6.2 通信接口要求 …… 2    
6.3 数据格式要求 …… 2    
6.4 信息交换要求 …… 2    
7 接口参考模型 …… 3    
7.1 总则 …… 3    
7.2 业务组件 …… 3    
7.3 业务组件接口 …… 3    
附录 A（资料性） 制造物流系统互联互通典型接口示例 …… 6    
A.1 应用场景 …… 6    
A.2 接口实现 …… 6    
附录 B（资料性） 制造物流系统互联互通服务流程 …… 7    
B.1 概述 …… 7    
B.2 集成设计 …… 7    
B.3 集成实施 …… 7    
B.4 流程管理 …… 7    
附录 C（资料性） 制造物流系统业务数据 …… 8    
C.1 基础数据管理相关业务数据 …… 8    
C.2 采购管理相关业务数据 …… 9    
C.3 仓储管理相关业务数据 …… 9    
C.4 制造管理相关业务数据 …… 10    
C.5 配送管理相关业务数据 …… 10    
C.6 销售管理相关业务数据 …… 10    
C.7 设备管理相关业务数据 …… 11    
C.8 质量管理相关业务数据 …… 11    
C.9 运输管理相关业务数据 …… 12    
参考文献 …… 13



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

本文件由中国机械工业联合会提出。

本文件由全国自动化系统与集成标准化技术委员会(SAC/TC 159)归口。

本文件起草单位：北自所（北京）科技发展股份有限公司、北京机械工业自动化研究所有限公司、江苏长江智能制造研究院有限责任公司、杭州海康机器人股份有限公司、北京起重运输机械设计研究院有限公司、北京理工大学、湖州德奥机械设备有限公司、浙江省自动化学会、北京众驰自动化设备有限公司、深圳路辉物流设备有限公司、深圳市九天中创自动化设备有限公司、赛那德科技有限公司、深圳市高捷力科技有限公司、中轻长泰（长沙）智能科技股份有限公司、临沂临工智能信息科技有限公司、深圳市海柔创新科技有限公司、昆山同日工业自动化有限公司、南京有多利科技发展有限公司、浙江中烟工业有限责任公司。

本文件主要起草人：王勇、徐慧、刘新、饶丰、唐聪、蔡苗、万英和、吴永海、林树茂、孙洁香、杨秋影、柴森春、张荣卫、吴华朋、张驰、潘艳飞、杜已超、薛静婉、渠晶、柴润祺、田贵磊、张利强、司佳顺、高静、赵钊、吴璇、钟霄、刘晓虹、曹峰、周非、李华、施灿、陈博、屈辉现、程宏、孔哲、姚万军、傅明东、谢晓波、高扬华。

Powered by TCPDF (www.tcpdf.org)

# 制造物流系统互联互通通用要求

## 1 范围

本文件规定了制造物流系统与企业资源计划（ERP）、制造执行系统（MES）互联互通的集成架构、基本要求、接口参考模型等通用要求。

本文件适用于指导企业制造物流系统与企业资源计划、制造执行系统互联互通服务的实践应用。

## 2 规范性引用文件

本文件没有规范性引用文件。

## 3 术语和定义

下列术语和定义适用于本文件。

<div style="text-align: center;"><img src="imgs/img_in_image_box_99_756_135_797.jpg" alt="Image" width="3%" /></div>


### 3.1 

## 制造物流系统 manufacturing logistics system

制造企业内部实现原材料、在制品、半成品、成品的输送、存储、配送等各实体流动环节中用于信息获取、处理、传递和利用的系统。

### 3.2 

## 互联互通 interconnection

制造物流系统与企业资源计划、制造执行系统之间通信协议能够兼容并且能相互理解对方信息资源的语义，进行系统间的数据交换。

## 4 缩略语

下列缩略语适用于本文件。

ERP: 企业资源计划 (Enterprise Resource Planning)

MES: 制造执行系统 (Manufacturing Execution System)

TMS: 运输管理系统 (Transportation Management System)

WCS: 仓储控制系统 (Warehouse Control System)

WMS: 仓库管理系统 (Warehouse Management System)

## 5 集成架构

在制造物流系统中，互联互通的主体指与制造物流相关的各信息系统，包括：ERP等企业管理层信息系统，MES等车间管控层信息系统，WMS、WCS、TMS等物流执行层信息系统。

物流执行系统与企业资源计划通过企业管理层-物流执行层接口实现互联互通，物流执行系统与制造执行系统通过制造执行层-物流执行层接口实现互联互通。其应用场景和接口实现见附录A。

各信息系统互联互通集成架构如图 1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_209_1001_742.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 1 制造物流系统互联互通集成架构</div>


## 6 基本要求

### 6.1 总体要求

实现制造物流系统与企业资源计划、制造执行系统之间的互联互通，构建数据资源共享。制造物流系统与企业资源计划、制造执行系统之间在进行信息交互时所产生的负荷不应导致双方系统自身显著变慢，出现停滞、卡顿、事务回滚等故障。双方信息交互时限应保证双方实时业务操作，不应影响对方生产作业。

### 6.2 通信接口要求

制造物流系统与企业资源计划、制造执行系统之间的通信接口应满足以下要求：

a）制造物流系统互联互通的链路层保证其数据帧传输延迟低于收发双方对延迟的最长允许时间要求，并具有适当的冗余；

b）通信双方在可信安全环境下直接进行数据传输交换，数据传输所采用的通信协议根据双方实际业务需求和技术发展情况协商确定。

### 6.3 数据格式要求

制造物流系统与企业资源计划、制造执行系统之间互联互通的数据格式可由交换双方协商确定，宜采用安全可靠的数据交换格式。

### 6.4 信息交换要求

#### 6.4.1 原则

制造物流系统与企业资源计划、制造执行系统之间互联互通的信息交换应遵循合法性、规范性、安

全性、真实性、可靠性、有效性、时效性等原则。

宜遵循高内聚、低耦合、精分解的设计原则，尽量降低各系统间、系统内各模块间的耦合度，降低操作复杂度，保证实现的通用性，提高系统的重用性和扩展性，具体原则如下：

a） 使用简单、快捷，通用性好，可靠性高；

b）充分考虑接口所涉及系统的应用扩展，灵活支撑需求变化；

c）保证接口数据在接口所涉及的各个系统间的一致性；

d）在数据交换过程中，应具有传送和接收后的确认过程。

#### 6.4.2 信息交换方式

制造物流系统与企业资源计划、制造执行系统之间互联互通的信息交换方式可由交换双方协商确定，宜采用安全可靠的信息交换方式。如：Web Service、TCP/IP Socket。

#### 6.4.3 信息交换安全

交换双方应采取约束、检查、加密、校验和认证等安全措施，确保交换数据的正确性、完整性、一致性、可靠性和抗抵赖性。各类安全措施宜采用国内商用密码技术实现。

## 7 接口参考模型

### 7.1 总则

接口参考模型描述了制造物流执行系统与企业资源计划/制造执行系统业务子功能间的业务活动，是对系统互联互通接口需求的描述。接口参考模型采用业务组件、组件间互联互通活动的分级表述方式。制造物流执行系统与企业资源计划/制造执行系统互联互通服务流程见附录 B。

### 7.2 业务组件

业务组件是基于制造物流全过程涉及各环节确定的。各业务组件所包含的业务数据见附录 C。与制造物流系统相关的各信息系统应包括但不限于以下业务组件：

a）基础数据管理：完成各类基础数据的维护；

b）采购管理：完成采购需求获取、采购订单制定及处理的过程；

c）仓储管理：完成企业内部各种物料的保管及流转过程；

d）制造管理：完成企业产品制造计划制定、制造过程的控制；

e) 配送管理：实现产品制造过程中所需各种物料的配送过程控制；

f) 销售管理：完成客户需求获取、客户订单制定及处理的过程；

g） 设备管理：完成企业设备全生命周期管理、维修维护过程控制；

h）质量管理：完成质量控制的过程管理、物料及产品质量检测的过程；

i) 运输管理：完成企业物流运输的调度和控制。

### 7.3 业务组件接口

#### 7.3.1 基础数据管理组件

基础数据管理是完成各类基础数据维护的业务活动。基础数据管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与制造管理：发送各类基础数据；

b）与仓储管理：发送各类基础数据。

#### 7.3.2 采购管理组件

##### 7.3.2.1 采购计划

采购计划是安排企业日常制造过程所需原辅料等生产资料采购事务的活动。采购计划与其他业务组件间可能的跨系统物流信息交换活动有：

a）与仓储管理：查询实时库存，发送采购计划；

b）与运输管理：发送采购计划。

##### 7.3.2.2 到货管理

到货管理是采购物资出入库应履行的业务程序。到货管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与仓储管理：发送采购到货通知，下达接收/退货指令，接收收货/退货反馈；

b) 与质量管理：接收物料质检报告；

c）与运输管理：接收卸货完成信息。

#### 7.3.3 仓储管理组件

##### 7.3.3.1 库存管理

库存管理是完成维护库存状态的业务活动，包括记录和维护库存数据、发布库存信息等功能。库存管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与质量管理：接收质检规则，接收质量检验报告，反馈更新库存结果；

b）与采购管理、制造管理：发布实时库存数据。

##### 7.3.3.2 库存调度

库存调度是完成库存地点内物资移动的业务活动，包括接收请求、生成作业、反馈执行结果等功能。库存调度与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与采购管理：接收采购到货通知，反馈采购入库执行结果，接收物料退货通知，反馈物料退货入库执行结果；

b）与销售系统：接收发货订单，反馈发货订单执行结果，接收退货通知，反馈退货入库执行结果；

c) 与制造管理：接收生产物料需求，反馈生产物料出库结果，接收半成品/成品入库信息，反馈半成品/成品入库执行结果；

d）与质量管理：接收质检出库单据，反馈质检出库执行结果。

#### 7.3.4 制造管理组件

##### 7.3.4.1 生产计划编制

生产计划编制是完成生产计划编制的业务活动，包括请求库存及质量数据、接收库存及质量数据等功能。生产计划编制与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与仓储管理：查询物料库存状态，接收实时库存信息；

b）与质量管理：查询物料质量报告，接收物料质量信息。

##### 7.3.4.2 生产计划执行

生产计划执行是按照生产计划进行执行调度的业务活动，包括发送物料需求和产品下线信息、接收

物料配送结果和产品入库信息等功能。生产计划执行与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与仓储管理：发送生产物料需求，接收生产物料出库结果，发送半成品/成品入库信息，接收半成品/成品入库结果，发送物料退货信息，接收物料退货入库结果；

b）与质量管理：发送产品生产报告，接收产品质量信息。

#### 7.3.5 配送管理组件

配送管理是完成物料配送到生产线的业务活动。配送管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与制造管理：发送物料配送信息，接收配送完成确认；

b）与仓储管理：接收物料配送信息，反馈配送完成信息。

#### 7.3.6 销售管理组件

##### 7.3.6.1 销售计划

销售计划是完成企业产品销售计划制定的业务活动。销售计划与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与仓储管理：查询产品库存状态，接收实时库存信息；

b）与运输管理：发送销售计划。

##### 7.3.6.2 发货管理

发货管理是按销售计划及客户要求安排产品出库的业务活动。发货管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与仓储管理：下发销售计划，接收销售计划执行结果，发送产品退货通知，接收产品退货入库执行结果；

b) 与运输管理：接收装车完成信息。

#### 7.3.7 设备管理组件

设备管理是物流设备运行状态作业数据的跟踪及设备维护管理活动。设备管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：与制造管理组件发送设备运行参数，接收设备维护计划，反馈设备维护结果。

#### 7.3.8 质量管理组件

质量管理是物流过程中与质量检验相关的活动。质量管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与采购管理：接收物料到货信息，提供物料质量报告；

b）与仓储管理：发送质检出库单据，接收质检出库执行结果，提供物料质量报告。

#### 7.3.9 运输管理组件

运输管理是物流过程中与外来车辆运输相关的活动。运输管理与其他业务组件间跨系统物流信息交换活动应包括但不限于：

a）与采购管理：接收物料到货信息，反馈卸货完成信息；

b）与销售管理：接收销售计划，反馈装车完成信息。

# 附录 A

# (资料性)

# 制造物流系统互联互通典型接口示例

### A.1 应用场景

制造物流系统互联互通典型应用场景一般包括以下情形：

a）物流执行层（WMS、WCS、TMS等系统）与企业管理层（ERP等系统）进行互联互通；

b）物流执行层（WMS、WCS、TMS等系统）与车间管控层（MES等系统）进行互联互通。

### A.2 接口实现

制造物流系统互联互通典型接口实现一般包括以下内容。

a）物流执行层的 WMS 与企业管理层的 ERP 有关基础数据的接口应包含但不限于以下内容：

1）物料信息：物料编码、物料名称、物料描述和规格等；

2）供应商信息：供应商编码、供应商名称、供应商简称、供应商地址和供应商联系人等；

3）客户信息：客户编码、客户名称、客户简称、客户地址和客户联系人等；

4）业务类型信息：业务类型编码、业务类型名称等。

基础数据由 ERP 进行维护, 发送给 WMS.

b）物流执行层的 WMS 与企业管理层的 ERP 有关采购管理接口有：采购计划、采购到货通知单、退换货通知单。ERP 将采购计划、采购到货通知单、退换货通知单下发给 WMS，WMS 执行完毕将结果反馈给 ERP。

c）物流执行层的 WMS 与企业管理层的质量管理系统有关质量管理接口有：质检申请单、质检报告。WMS 接收质检申请单执行出库，接收质检报告更新库存状态。

d）物流执行层的 WMS 与车间管控层的 MES 有关制造管理接口有：生产物料需求、半成品/成品入库信息、物料退货信息。MES 将生产物料需求发给 WMS，WMS 执行出库后，将出库结果反馈给 MES；MES 发起半成品/成品入库请求、物料退货请求，WMS 执行入库完成后，将入库结果反馈给 MES。

e) 物流执行层的 WMS 与企业管理层的 ERP 有关销售管理接口有：销售计划、产品退货通知单。ERP 将销售计划发给 WMS，WMS 执行出库后，将出库结果反馈给 ERP。ERP 将产品退货通知单发给 WMS，WMS 执行入库后，将入库结果反馈给 ERP。

f) 物流执行层的 WCS 与车间管控层的 MES 有关设备管理接口有：设备维护计划。MES 将设备维护计划下发给 WCS，WCS 执行完毕将执行结果反馈给 MES。

g）物流执行层的 TMS 与企业管理层的 ERP 有关运输管理接口有：采购物料到货信息、销售计划出库信息。ERP 将采购物料到货信息、销售计划出库信息下发给 TMS，TMS 执行完装卸货作业后，将执行结果反馈给 ERP。

# 附录 B

(资料性)

## 制造物流系统互联互通服务流程

### B.1 概述

制造物流系统与企业资源计划、制造执行系统之间互联互通的服务流程包括但不限于：集成设计、集成实施、流程管理三个方面。旨在根据制造业的行业特点和具体制造场景对智能制造服务进行全局规划，明确各阶段目标，采取一系列措施实现目标。

### B.2 集成设计

集成设计的活动包含但不限于以下内容。

a）需求调研：制造物流系统与企业资源计划、制造执行系统双方各自的项目团队应就企业现状及企业的战略目标，进行详细调查，熟悉企业业务流程，充分了解企业管理的信息需求。

b) 系统分析：根据企业需求确定逻辑模型，即确定做什么。

c）系统设计：在系统分析的基础上确定物流模型，即确定实现这些需求，怎么做。进行概要设计、详细设计，形成系统之间互联互通的详细设计说明书。

d）系统评审：制造物流系统与企业资源计划、制造执行系统双方及企业相关干系人针对详细设计说明书进行评审，形成最终可实施的详细设计说明书。

### B.3 集成实施

集成实施的活动包含但不限于以下内容：

a）计算机等设备的购置、安装和调试；

b) 程序的编写和调试；

c） 人员培训；

d） 数据文件转换；

e）系统调试与转换；

f）记录运行情况、进行必要的修改；

g）评价系统的工作质量和经济效益。

### B.4 流程管理

供方可按计划的时间间隔对服务进行管理评审，确保服务的适用性、充分性和有效性，具体方法见GB/T 19001—2016。管理评审内容包括但不限于以下内容：

a）以往管理评审所采取措施的实施情况；

b）供方内部和外部的因素变化；

c） 内部审核结果；

d) 持续改进的机会；

e）需方和其他相关方的满意程度；

f）纠正、创新、风险评估成果和措施。

## 附录 C

(资料性)

制造物流系统业务数据

### C.1 基础数据管理相关业务数据

与制造物流系统相关的基础数据主要包括物料基础数据、供应商基础数据、客户基础数据、业务类型基础数据。包含的关键业务字段见表 C.1～表 C.4。

<div style="text-align: center;">表 C.1 物料基础数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>SkuID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>物料代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>SkuName</td><td style='text-align: center;'>VarChar</td><td style='text-align: center;'>物料名称</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>SkuDesc</td><td style='text-align: center;'>VarChar</td><td style='text-align: center;'>物料描述</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Speci</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>规格</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>mUnit</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>计量单位</td><td style='text-align: center;'>基础参数</td></tr></table>

<div style="text-align: center;">表 C.2 供应商基础数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>VendorID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>供应商代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>VendorName</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>供应商名称</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>VendorDesc</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>供应商简称</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>VendorAddr</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>供应商地址</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>VendorContact</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>供应商联系人</td><td style='text-align: center;'>基础参数</td></tr></table>

<div style="text-align: center;">表 C.3 客户基础数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>CustomerID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>客户代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CustomerName</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>客户名称</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CustomerDesc</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>客户简称</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CustomerAddr</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>客户地址</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CustomerContact</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>客户联系人</td><td style='text-align: center;'>基础参数</td></tr></table>

<div style="text-align: center;">表 C.4 业务类型基础数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>IOCLassID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>业务类型代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>IOCLassName</td><td style='text-align: center;'>VarChar</td><td style='text-align: center;'>业务类型名称</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>TranType</td><td style='text-align: center;'>VarChar</td><td style='text-align: center;'>业务类型</td><td style='text-align: center;'>关键参数</td></tr></table>

### C.2 采购管理相关业务数据

与制造物流系统相关的采购管理信息主要包括采购计划数据。包含的关键业务字段见表C.5。

<div style="text-align: center;">表 C.5 采购计划数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>BillID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>采购订单号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>IOCLassID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>业务类型代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>VendorID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>供应商代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>ArrivalTime</td><td style='text-align: center;'>datetime</td><td style='text-align: center;'>物料到货时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateTime</td><td style='text-align: center;'>datetime</td><td style='text-align: center;'>单据的创建时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CreateUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>单据的创建人</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>SkuID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>物料 ID</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LotNO</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>批号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Speci</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>规格</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Num</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>数量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Weight</td><td style='text-align: center;'>Decimal</td><td style='text-align: center;'>质量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>OwnerID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>货主</td><td style='text-align: center;'>基础参数</td></tr></table>

### C.3 仓储管理相关业务数据

与制造物流系统相关的仓储管理信息主要包括库存数据。包含的关键业务字段见表C.6。

<div style="text-align: center;">表 C.6 库存数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>StoreDefID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>库房代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>货位地址</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>PalletID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>托盘号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>SkuID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>物料 ID</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LotNO</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>批号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Speci</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>规格</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Num</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>数量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Weight</td><td style='text-align: center;'>Decimal</td><td style='text-align: center;'>质量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>OwnerID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>货主</td><td style='text-align: center;'>基础参数</td></tr></table>

### C.4 制造管理相关业务数据

与制造物流系统相关的制造管理信息主要包括生产计划数据。包含的关键业务字段见表C.7。

<div style="text-align: center;">表 C.7 生产计划数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>PLanID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>计划号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>计划创建时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CreateUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>创建人</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>RunTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>计划执行时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>FinishTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>计划完成时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>MachineID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>机台号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Mid</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>产成品代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LotNO</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>批号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Num</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>计划生产数量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>FinishNum</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>完工数量</td><td style='text-align: center;'>关键参数</td></tr></table>

### C.5 配送管理相关业务数据

与制造物流系统相关的配送管理信息主要包括配送计划数据。包含的关键业务字段见表C.8。

<div style="text-align: center;">表 C.8 配送计划数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>PLanID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>计划号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>计划创建时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CreateUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>创建人</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>RunTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>计划执行时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>FinishTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>计划完成时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>StartStation</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>起始工位</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>EndStation</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>目的工位</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>SKUID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>物料代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Num</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>配送数量</td><td style='text-align: center;'>关键参数</td></tr></table>

### C.6 销售管理相关业务数据

与制造物流系统相关的销售管理信息主要包括销售订单数据。包含的关键业务字段见表C.9。

<div style="text-align: center;">表 C.9 销售订单数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>BillID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>销售订单号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>IOCLassID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>业务类型代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CustomerID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>客户</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>MachineID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>机台号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Mid</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>产成品代码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LotNO</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>批号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Num</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>单据出库数量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>FinishNum</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>实际出库数量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>创建时间</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CreateUserId</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>创建人</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>FinishTime</td><td style='text-align: center;'>DateTime</td><td style='text-align: center;'>完成时间</td><td style='text-align: center;'>基础参数</td></tr></table>

### C.7 设备管理相关业务数据

与制造物流系统相关的设备管理信息主要包括设备维护计划数据。包含的关键业务字段见表 C.10。

<div style="text-align: center;">表 C.10 设备维护计划数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>PLanID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>计划号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>DevNO</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>设备号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>创建时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>创建人</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Maintaintime</td><td style='text-align: center;'>datetime</td><td style='text-align: center;'>维护时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Maintainer</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>维护人</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>MainTainItem</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>维护项目</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>FinishTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>完成时间</td><td style='text-align: center;'>关键参数</td></tr></table>

### C.8 质量管理相关业务数据

与制造物流系统相关的质量管理信息主要包括质检计划数据、质检报告数据。包含的关键业务字段见表 C.11、表 C.12。

<div style="text-align: center;">表 C.11 质检计划数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>BillID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>质检计划单号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>SkuID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>物料编码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LotNO</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>批号</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Num</td><td style='text-align: center;'>Int</td><td style='text-align: center;'>质检数量</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CheckTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>质检时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>UserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>送检人</td><td style='text-align: center;'>关键参数</td></tr></table>

<div style="text-align: center;">表 C.12 质检报告数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>BillID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>质检报告单号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>SkuID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>物料编码</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>MStatus</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>质检状态</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Reason</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>不合格原因</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>CheckTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>质检时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CheckUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>质检人</td><td style='text-align: center;'>关键参数</td></tr></table>

### C.9 运输管理相关业务数据

与制造物流系统相关的运输管理信息主要包括运输计划数据。包含的关键业务字段见表C.13。

<div style="text-align: center;">表 C.13 运输计划数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>类型</td><td colspan="2">说明</td></tr><tr><td style='text-align: center;'>PLanID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>计划号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>创建时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>CreateUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>创建人</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LoaderType</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>装卸车类型</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>NumberPlate</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>车牌号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Driver</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>司机</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Phone</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>联系电话</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>Platform</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>月台号</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>PlanTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>计划装卸车时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LoadTime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>装卸时间</td><td style='text-align: center;'>关键参数</td></tr><tr><td style='text-align: center;'>LoadUserID</td><td style='text-align: center;'>Varchar</td><td style='text-align: center;'>装卸人</td><td style='text-align: center;'>基础参数</td></tr><tr><td style='text-align: center;'>Finishtime</td><td style='text-align: center;'>Datetime</td><td style='text-align: center;'>完成时间</td><td style='text-align: center;'>关键参数</td></tr></table>

# 參 考 文 献

[1] GB/T 19001—2016 质量管理体系 要求







