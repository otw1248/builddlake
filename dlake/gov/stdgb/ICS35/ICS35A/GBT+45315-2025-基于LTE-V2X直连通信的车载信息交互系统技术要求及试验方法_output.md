

# 中华人民共和国国家标准

GB/T 45315—2025

# 基于 LTE-V2X 直连通信的车载信息交互系统技术要求及试验方法

# Technical requirements and test methods of vehicular information interactive systems based on LTE-V2X direct communication

2025-02-28 发布

2025-02-28 实施

国家市场监督管理总局  

国家标准化管理委员会  

发布



## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义、符号和缩略语 …… 1  
  
4 系统描述 …… 3  
  
5 车规环境要求 …… 4  
  
6 定位授时要求 …… 8  
  
7 功能要求 …… 9  
  
8 通信性能要求 …… 33  
  
9 试验方法 …… 34  
  
附录 A（资料性） LTE-V2X 系统电磁兼容性技术要求及试验方法 …… 57  
  
附录 B（资料性） 关键事件触发 BSM 消息发送 …… 59  
  
附录 C（资料性） 拥塞控制机制 …… 60  
  
附录 D（规范性） 车辆基本类型及编号 …… 64  
  
附录 E（资料性） 车辆历史轨迹与预测路线参考设计 …… 67  
  
附录 F（规范性） 车辆方位区域划分 …… 69  
  
附录 G（资料性） 耐久性试验 …… 71  
  
附录 H（资料性） 车辆天线性能测试场地要求 …… 72  
  
参考文献 …… 75



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由中华人民共和国工业和信息化部提出。

本文件由全国汽车标准化技术委员会(SAC/TC 114)归口。

本文件起草单位：中国汽车技术研究中心有限公司、中国信息通信研究院、国汽（北京）智能网联汽车研究院有限公司、中国信息通信科技集团有限公司、华为技术有限公司、安徽江淮汽车集团股份有限公司、上汽大众汽车有限公司、重庆长安汽车股份有限公司、高通无线通信技术（中国）有限公司、中国第一汽车集团有限公司、中国软件评测中心（工业和信息化部软件与集成电路促进中心）、东软集团股份有限公司、长城汽车股份有限公司、东风汽车集团股份有限公司、福特汽车（中国）有限公司、金龙联合汽车工业（苏州）有限公司、北京百度智行科技有限公司、泛亚汽车技术中心有限公司、宝马中国（服务）有限公司、梅赛德斯—奔驰（中国）投资有限公司、江铃汽车股份有限公司、大众汽车（中国）投资有限公司、丰田汽车（中国）投资有限公司、北京星云互联科技有限公司、沃尔沃汽车（亚太）投资控股有限公司。

本文件主要起草人：孙航、王兆、葛雨明、刘建行、李春、吴飞燕、房家奕、杨淼、朱陈伟、梁睿、牛雷、殷悦、孙博逊、李明超、王荣、周欣如、刁立凯、赵奕铭、公维洁、吴建飞、姜国凯、聂石启、彭伟、陈岭、张洁、张图南、刘帆、明经洪、于润东、杨行、姜美尧、王易之、汝正阳。



# 基于 LTE-V2X 直连通信的车载信息交互系统技术要求及试验方法

## 1 范围

本文件规定了基于长期演进的车用无线通信技术(LTE-V2X)支持直连通信的车载信息交互系统的系统描述、车规环境要求、定位授时要求、功能要求、通信性能要求以及试验方法。

本文件适用于 M 类、N 类车辆。

注：在不引起歧义的情况下，本文件将基于 LTE-V2X 直连通信的车载信息交互系统简称为 LTE-V2X 系统。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 28046.2—2019 道路车辆 电气及电子设备的环境条件和试验 第2部分：电气负荷

GB/T 28046.3—2011 道路车辆 电气及电子设备的环境条件和试验 第3部分：机械负荷

GB/T 28046.4—2011 道路车辆 电气及电子设备的环境条件和试验 第4部分：气候负荷

GB/T 30038—2013 道路车辆 电气电子设备防护等级(IP 代码)

GB 34660—2017 道路车辆 电磁兼容性要求和试验方法

YD/T 3340—2018 基于 LTE 的车联网无线通信技术 空中接口技术要求

YD/T 3707—2020 基于 LTE 的车联网无线通信技术 网络层技术要求

YD/T 3709—2020 基于 LTE 的车联网无线通信技术 消息层技术要求

YD/T 3756—2024 基于 LTE 的车联网无线通信技术支持直连通信的车载终端设备技术要求

YD/T 3848—2021 基于 LTE 的车联网无线通信技术支持直连通信的车载终端设备测试方法

YD/T 3957—2021 基于 LTE 的车联网无线通信技术 安全证书管理系统技术要求

## 3 术语和定义、符号和缩略语

### 3.1 术语和定义

下列术语和定义适用于本文件。

3.1.1

V2X vehicle to everything

一种车辆与外界通信的技术。

注：“外界”指车外的车辆、行人、云端、基础设施等。

[来源:GB/T 44373—2024,4.8]

3.1.2

基于长期演进的车用无线通信技术 long term evolution vehicle to everything; LTE-V2X 一种基于长期演进的车辆与外界通信的技术。

#### 3.1.3 

## 直连通信 direct communication

无线电设备通过无线电传输方式直接进行通信。

注：本文件指车辆通过 LTE-V2X 直连通信接口与其他设备之间的信息交换。

#### 3.1.4 

试验电压 test voltage

在试验期间施加到被测设备上的电压。

[来源:GB/T 28046.1—2011,3.5,有修改]

### 3.2 符号和缩略语

下列符号和缩略语适用于本文件。

ABS: 制动防抱死系统 (Antilock Brake System)

AID: 应用标识 (Application ID)

BDS:北斗卫星导航系统(BeiDou Navigation Satellite System)

BSM: 车辆基本安全消息 (Basic Safety Message)

CBR:信道忙碌率(Channel Busy Ratio)

DE: 数据元素 (Data Element)

DF: 数据帧(Data Frame)

DSM: 专用短消息 (Dedicated Short Message)

DSMP: 专用短消息协议 (Dedicated Short Message Protocol)

DUT: 被测装置 (Device Under Test)

<div style="text-align: center;"><img src="imgs/img_in_image_box_849_933_883_968.jpg" alt="Image" width="2%" /></div>


GALILEO:伽利略卫星导航系统(Galileo Navigation Satellite System)

GLONASS:格洛纳斯卫星导航系统(Global Navigation Satellite System)

GNSS: 全球导航卫星系统 (Global Navigation Satellite System)

GPS: 全球定位系统(Global Positioning System)

HDOP: 水平精度因子 (Horizontal Dilution of Precision)

ID: 身份标识号码(Identity)

LTE: 长期演进技术(Long Term Evolution)

LTE-V2X:基于长期演进的车用无线通信技术(LTE Vehicle to Everything)

MAC: 媒体访问控制地址 (Media Access Control Address)

PC5:邻近通信接口 5(ProSe Communication 5)

PDB: 数据包时延预算(Packet Delay Budget)

PDCP: 分组数据汇聚协议 (Packet Data Convergence Protocol)

PH:历史轨迹(Path History)

PPPP:邻近服务逐包优先级(ProSe Per-Packet Priority)

RLC: 无线链路控制 (Radio Link Control)

SN: 序列号(Sequence Number)

SPDU: 安全协议数据单元(Secured Protocol Data Unit)

 $ T_{min} $ : 最低工作温度

 $ T_{max} $ : 最高工作温度

TCS:牵引力控制系统(Traction Control System)

 $ U_{Smax} $ : 最高工作电压

 $ U_{Smin} $ : 最低工作电压

 $ U_{t} $ : 试验电压

UTC: 协调世界时 (Coordinated Universal Time)

## 4 系统描述

### 4.1 系统构成

LTE-V2X 系统对外可通过 LTE-V2X 直连通信技术和其他车辆、路侧基础设施、弱势交通参与者等进行实时信息交互，对内可采集电子电气系统信息并与其进行信息交互。两种常用的 LTE-V2X 系统功能模块示意图见图 1，图 1 a) 是车载定位子系统内置的 LTE-V2X 系统功能模块示意图，图 1 b) 是车载定位子系统外置的 LTE-V2X 系统功能模块示意图。

注：弱势交通参与者包括行人、自行车、电动自行车等。

<div style="text-align: center;"><img src="imgs/img_in_image_box_169_825_528_1221.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">a）车载定位子系统内置的 LTE-V2X 系统功能模块示意图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_678_826_1039_1221.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">b）车载定位子系统外置的 LTE-V2X 系统功能模块示意图</div>


<div style="text-align: center;">图 1 LTE-V2X 系统功能模块示意图</div>


### 4.2 工作模式

根据试验对象所处的工作条件，将其工作模式分为4种，见表1。

<div style="text-align: center;">表 1 工作模式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验对象</td><td style='text-align: center;'>工作条件</td><td style='text-align: center;'>工作模式</td></tr><tr><td rowspan="2">LTE-V2X系统</td><td style='text-align: center;'>具备LTE-V2X直连通信功能的最小功能模块不上电</td><td style='text-align: center;'>工作模式1</td></tr><tr><td style='text-align: center;'>具备LTE-V2X直连通信功能的最小功能模块上电且正常工作</td><td style='text-align: center;'>工作模式2</td></tr><tr><td rowspan="2">车辆</td><td style='text-align: center;'>车辆启动并保持静止，LTE-V2X系统正常广播BSM</td><td style='text-align: center;'>工作模式3</td></tr><tr><td style='text-align: center;'>车辆启动并以一定速度运动，LTE-V2X系统正常广播BSM</td><td style='text-align: center;'>工作模式4</td></tr><tr><td colspan="3">注：最小功能模块是指包含图1所示的无线通信子系统的最小零部件。</td></tr></table>

示例 1：图 1 a) 所示，最小功能模块包括车载定位子系统、无线通信子系统、车载设备处理单元、LTE-V2X 天线、GNSS 天线。

示例 2：图 1 b) 所示，最小功能模块包括无线通信子系统、车载设备处理单元、LTE-V2X 天线。

## 5 车规环境要求

### 5.1 功能等级划分

LTE-V2X系统的功能等级分为以下4级：

a）等级 A: 试验中和试验后 LTE-V2X 系统功能满足第 7 章的要求；

b）等级 B：试验中 LTE-V2X 系统功能不满足第 7 章的要求，但试验后 LTE-V2X 系统功能自动恢复至满足第 7 章的要求；

c) 等级 C: 试验中 LTE-V2X 系统功能不满足第 7 章的要求，且试验后 LTE-V2X 系统功能不能自动恢复至满足第 7 章的要求，需对 LTE-V2X 系统进行简单操作重新激活系统功能；

d）等级 D：试验中 LTE-V2X 系统功能不满足第 7 章的要求，且试验后不能自动恢复至满足第 7 章的要求，需对 LTE-V2X 系统进行维修或更换。

注：“功能”是指 LTE-V2X 系统发送 BSM 必选数据的功能。

### 5.2 电气性能

#### 5.2.1 直流供电电压

LTE-V2X系统的直流供电电压范围见表2，在 $ U_{Smin}\sim U_{Smax} $ 范围内，按照9.1.2.1进行试验，LTE-V2X系统功能状态应满足5.1等级A的要求。

<div style="text-align: center;">表 2 直流供电电压范围</div>


单位为伏特


<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">额定电压</td><td colspan="3">供电电压范围</td></tr><tr><td style='text-align: center;'>$ U_{Smin} $</td><td style='text-align: center;'>$ U_{Smax} $</td><td style='text-align: center;'>供电电压</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>9</td><td style='text-align: center;'>16</td><td style='text-align: center;'>12±0.2</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>16</td><td style='text-align: center;'>32</td><td style='text-align: center;'>24±0.2</td></tr></table>

#### 5.2.2 过电压

##### 5.2.2.1 $ T_{max}-20^{\circ}C $  条件下

按照 9.1.2.2.1 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

##### 5.2.2.2 室温条件下

按照 9.1.2.2.2 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.2.3 供电电压缓降和缓升

按照 9.1.2.3 进行试验，当供电电压由  $ U_{Smin} $  降到 0 V，然后由 0 V 升到  $ U_{Smin} $  时，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.2.4 叠加交流电压

按照 9.1.2.4 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.2.5 反向电压

按照 9.1.2.5 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.2.6 供电电压瞬态变化

##### 5.2.6.1 供电电压瞬时下降

按照 9.1.2.6 a) 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

##### 5.2.6.2 复位特性

按照 9.1.2.6 b) 进行试验，电压恢复到  $ U_{Smin} $  后，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

##### 5.2.6.3 启动特性

按照 9.1.2.6 c) 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.2.7 参考接地和供电偏移

按照 9.1.2.7 进行试验，对于多点接地的 LTE-V2X 系统，其功能状态应满足 5.1 等级 A 的要求。

#### 5.2.8 抛负载

按照 9.1.2.8 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

注：本条仅适用于有低压交流发电机的车辆。

#### 5.2.9 开路

按照 9.1.2.9 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.2.10 短路保护

按照 9.1.2.10 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.2.11 绝缘电阻

按照 9.1.2.11 进行试验，LTE-V2X 系统绝缘电阻应大于  $ 10 \, M\Omega $ 。

### 5.3 环境耐候性

#### 5.3.1 温湿度范围

LTE-V2X系统的贮存环境温度范围和工作环境温湿度范围应符合表3的规定。

<div style="text-align: center;">表 3 温湿度范围</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>汽车上安装位置</td><td style='text-align: center;'>贮存环境温度℃</td><td style='text-align: center;'>工作环境温度(Tmin～Tmax)℃</td><td style='text-align: center;'>工作环境相对湿度%</td></tr><tr><td style='text-align: center;'>乘客舱太阳直射处a</td><td style='text-align: center;'>-40～95</td><td style='text-align: center;'>-40～90</td><td style='text-align: center;'>25～75</td></tr><tr><td style='text-align: center;'>其他位置</td><td style='text-align: center;'>-40～90</td><td style='text-align: center;'>-40～85</td><td style='text-align: center;'>25～75</td></tr><tr><td colspan="4">a安装在车顶处的智能天线终端产品温湿度范围按照乘客舱太阳直射处温湿度要求执行,Tmax应不低于90℃。</td></tr></table>

#### 5.3.2 低温贮存

按照 9.1.3.1 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.3.3 低温工作

按照 9.1.3.2 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.3.4 高温贮存

按照 9.1.3.3 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.3.5 高温工作

按照 9.1.3.4 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.3.6 温度梯度

按照 9.1.3.5 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.3.7 规定转换时间的温度快速变化

按照 9.1.3.6 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 B 的要求。

#### 5.3.8 规定变化率的温度循环

按照 9.1.3.7 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.3.9 湿热循环

按照 9.1.3.8 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.3.10 稳态湿热

按照 9.1.3.9 进行试验，LTE-V2X 系统功能状态应满足 5.1 等级 A 的要求。

#### 5.3.11 耐盐雾

按照 9.1.3.10 进行试验，检查 LTE-V2X 系统外观，应密封完好，标志和标签应清晰可见，其功能状态应满足 5.1 等级 B 的要求。

### 5.4 外壳防护

按照 GB/T 28046.4—2011 表 A.1 的要求，按照 9.1.4 进行试验，LTE-V2X 系统功能应满足 5.1 等级 B 的要求。

### 5.5 机械性能

#### 5.5.1 机械振动

按照 9.1.5.1 进行试验，LTE-V2X 系统不应有物理损坏，其功能状态应满足 5.1 等级 A 的要求。

#### 5.5.2 机械冲击

按照 9.1.5.2 进行试验，LTE-V2X 系统不应有物理损坏，其功能状态应满足 5.1 等级 A 的要求。

#### 5.5.3 自由跌落

按照 9.1.5.3 进行试验，LTE-V2X 系统不应有隐形损坏，在不影响 LTE-V2X 系统性能的情况下允许外壳有微小损坏，其功能状态应满足 5.1 等级 B 的要求。

### 5.6 耐久性

按照 9.1.6 进行试验，LTE-V2X 系统不应有物理损坏，其寿命应不低于 10 年。

### 5.7 电磁兼容性

#### 5.7.1 车辆电磁兼容性

##### 5.7.1.1 宽带辐射发射

按照 9.1.7.1.4.1 进行试验，车辆应符合 GB 34660—2017 中 4.2 的要求。

##### 5.7.1.2 窄带辐射发射

按照 9.1.7.1.4.2 进行试验，车辆应符合 GB 34660—2017 中 4.3 的要求。

##### 5.7.1.3 对电磁辐射的抗扰

按照 9.1.7.1.4.3 进行试验，试验中及试验后，车辆在连续测试时间 t（单位为秒）内，V2X PC5 消息接收仪表接收到的 BSM 数据包的数量应不低于 round $ (t \times 10 \times 95\%) $ 。

注：round 表示取整数。

#### 5.7.2 系统电磁兼容性

LTE-V2X 系统电磁兼容性要求见附录 A。

## 6 定位授时要求

### 6.1 定位

按照 9.2.3 进行试验，LTE-V2X 系统应支持北斗独立定位，若支持北斗单模定位也视为满足要求。

按照 9.2.4 进行试验，车载定位子系统应以 10 Hz 频率输出位置坐标，在开阔天空环境下精度达到 1.5 m [置信概率为 CEP(68%)]，且应提供对应的 UTC 时间。

注：精确度要求是假设典型的最小道路宽度为3 m。

### 6.2 车辆位置参考点与坐标系统

车辆位置参考点为车辆投影至道路平面上的包络矩形的中心，此矩形覆盖车辆的最前端和最后端，以及左侧边到右侧边的点，包含外部后视镜等原始设备。车辆位置参考点及坐标系见图2。

<div style="text-align: center;"><img src="imgs/img_in_image_box_355_638_756_864.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_218_916_950_1166.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 2 BSM 中的车辆位置参考点及坐标系</div>


### 6.3 车载定位子系统时间

车载定位子系统中应包含一个同步到 UTC 的参考时钟，其精度值为 1 ms。车载定位子系统每次输出位置时应同时包含对应的 UTC 时间。

## 7 功能要求

### 7.1 接入层配置要求

#### 7.1.1 PC5 接口通用要求

系统应将预配置参数设置为 YD/T 3756—2024 表 A.1、表 A.2、表 A.3 及表 A.4 对应取值。

若 LTE-V2X 系统预配置了 YD/T 3340—2018 中的同步偏移指示 1(syncOffsetIndicator1-r14)、同步偏移指示 2(syncOffsetIndicator2-r14)或同步偏移指示 3(syncOffsetIndicator3-r14)，这 3 个参数不应生效。

#### 7.1.2 PC5 接口发送端要求

7.1.2.1 LTE-V2X 系统应采用广播方式发送业务数据。

7.1.2.2 LTE-V2X 系统应支持采用传输模式 4 进行数据发送。在发送业务数据时，宜采用感知加半持续调度的资源选择方式。

注：传输模式4指终端（用户设备）自主资源选择，终端通过侦听的方式感知占用PC5资源。

7.1.2.3 PDCP 头的 3 bit SDU(业务数据单元)类型应设为 011，应采用 16 bit 的 PDCP SN。PGK(邻近服务群组密钥)标识、PTK(邻近服务业务密钥)标识和 PDCP SN 应设为 0。

7.1.2.4 LTE-V2X 系统在使用 PC5 发送业务数据时应采用 RLC UM（无确认模式），并采用 5 bit 的 RLC SN。

7.1.2.5 MAC 头的 4 bit V 域应设为 0011。

### 7.2 网络层配置要求

#### 7.2.1 PC5 接口发送端要求

数据包发送行为应符合如下要求。

a）适配层在 $$ 0x010001,0xFFFFFE $$ 范围内随机产生并维持24bit Source_Layer-2 ID。若ADAPTATION-LAYER.request中出现Application layer ID changed参数，适配层在 $$ 0x010001,0xFFFFFE $$ 范围内重新随机产生并维持24bit Source_Layer-2 ID。适配层在数据包发送时将维持24bit Source_Layer-2 ID指示给接入层。

b）适配层按照表4将AID参数映射为24bit Destination Layer-2 ID并指示给接入层。

c）适配层根据 YD/T 3756—2024 表 A.2，将发送数据包的 Priority 参数映射为 PPPP 并指示给接入层。

d）当上层提供业务周期 Traffic Period 参数时，网络层将其指示给接入层。

e）针对 YD/T 3707—2020 表 1 定义的 DSMP 数据帧格式，DSMP 版本填写为 0，预留域全填写为 0。

<div style="text-align: center;">表 4 AID 与 Destination Layer-2 ID 映射表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>AID 参数取值(十六进制紧凑编码)</td><td style='text-align: center;'>Destination_Layer-2 ID 参数取值(十六进制)</td></tr><tr><td style='text-align: center;'>0p6f</td><td style='text-align: center;'>0x000001</td></tr><tr><td style='text-align: center;'>0p70</td><td style='text-align: center;'>0x000002</td></tr></table>

<div style="text-align: center;">表 4 AID 与 Destination Layer-2 ID 映射表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>AID 参数取值(十六进制紧凑编码)</td><td style='text-align: center;'>Destination_Layer-2 ID 参数取值(十六进制)</td></tr><tr><td style='text-align: center;'>0p71</td><td style='text-align: center;'>0x000003</td></tr><tr><td style='text-align: center;'>0p72</td><td style='text-align: center;'>0x000004</td></tr></table>

#### 7.2.2 PC5 接口接收端要求

数据包接收行为应满足如下要求：

a）适配层按照 YD/T 3756—2024 表 A.3，将接收数据包的 PPPP 映射为 Priority 并指示给上层；

b）当下层提供 CBR 或 Max data rate 参数时，网络层将其指示给上层。

### 7.3 应用层要求

#### 7.3.1 BSM 消息发送

##### 7.3.1.1 消息内容

LTE-V2X 系统发送的 BSM 的数据结构及编码应符合 YD/T 3709—2020，且不应携带表 5 未提及的其他数据单元。当 LTE-V2X 系统接收 BSM 时，应能忽略除表 6 之外的数据元素。BSM 内容见表 5，BSM 中的数据帧及数据元素定义见 7.3.2。

<div style="text-align: center;">表 5 BSM 内容</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>BSM字段内容</td><td style='text-align: center;'>定义</td></tr><tr><td style='text-align: center;'>DE_MsgCount</td><td style='text-align: center;'>消息编号</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>车辆临时ID号</td></tr><tr><td style='text-align: center;'>DE_Dsecond</td><td style='text-align: center;'>时间</td></tr><tr><td style='text-align: center;'>DE_TimeConfidence</td><td style='text-align: center;'>时间置信度</td></tr><tr><td style='text-align: center;'>DF_Position3D</td><td style='text-align: center;'>车辆位置</td></tr><tr><td style='text-align: center;'>DF_PositionalAccuracy</td><td style='text-align: center;'>车辆位置精度</td></tr><tr><td style='text-align: center;'>DF_PositionConfidenceSet</td><td style='text-align: center;'>车辆位置综合精度</td></tr><tr><td style='text-align: center;'>DE_TransmissionState</td><td style='text-align: center;'>车辆挡位状态</td></tr><tr><td style='text-align: center;'>DE_Speed</td><td style='text-align: center;'>车辆速度</td></tr><tr><td style='text-align: center;'>DE_Heading</td><td style='text-align: center;'>车辆航向角</td></tr><tr><td style='text-align: center;'>DE_SteeringWheelAngle</td><td style='text-align: center;'>车辆方向盘转角</td></tr><tr><td style='text-align: center;'>DF_MotionConfidenceSet</td><td style='text-align: center;'>车辆运行状态精度</td></tr><tr><td style='text-align: center;'>DF_AccelerationSet4Way</td><td style='text-align: center;'>车辆四轴加速度</td></tr><tr><td style='text-align: center;'>DF_BrakeSystemStatus</td><td style='text-align: center;'>车辆制动系统状态</td></tr><tr><td style='text-align: center;'>DF_VehicleSize</td><td style='text-align: center;'>车辆尺寸</td></tr><tr><td style='text-align: center;'>DF_VehicleClassification</td><td style='text-align: center;'>车辆的基本类型</td></tr><tr><td style='text-align: center;'>DF_VehicleSafetyExtensions</td><td style='text-align: center;'>车辆安全辅助信息集合</td></tr><tr><td style='text-align: center;'>DF_VehicleEmergencyExtensions</td><td style='text-align: center;'>紧急车辆当前状态的集合</td></tr></table>

##### 7.3.1.2 数据发送准则

当满足表 6 规定的数据发送要求时，LTE-V2X 系统应发送 BSM；当必选字段或满足发送条件的条件性必选字段无法进行填充且该字段不存在无效值时，LTE-V2X 系统应停止发送 BSM，直到 LTE-V2X 系统重新满足表 6 规定的数据发送要求时再次发送 BSM。

数据发送要求规定了 4 种类型数据单元的发送要求：

——必选：LTE-V2X 系统应发送该数据；

——条件性必选：当条件满足时，LTE-V2X系统应发送该数据，具体条件见7.3.2；

——可选：LTE-V2X 系统可自主选择是否发送该数据；

——不选：LTE-V2X 系统不应发送该数据。

<div style="text-align: center;">表 6 数据发送要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元/字段</td><td style='text-align: center;'>数据单元类型(必选/条件性必选/可选/不选)</td><td style='text-align: center;'>内容所在章条</td></tr><tr><td style='text-align: center;'>DE_MsgCount</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.1</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.2</td></tr><tr><td style='text-align: center;'>DE_DSecond</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.3</td></tr><tr><td style='text-align: center;'>DE_TimeConfidence</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.4</td></tr><tr><td colspan="3">DF_Position3D(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_Latitude</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.5</td></tr><tr><td style='text-align: center;'>&gt;DE_Longitude</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.5</td></tr><tr><td style='text-align: center;'>&gt;DE_Elevation</td><td style='text-align: center;'>不选</td><td style='text-align: center;'>7.3.2.5</td></tr><tr><td colspan="3">DF_PositionalAccuracy(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_SemiMajorAxisAccuracy</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.6</td></tr><tr><td style='text-align: center;'>&gt;DE_SemiMinorAxisAccuracy</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.6</td></tr><tr><td style='text-align: center;'>&gt;DE_SemiMajorAxisOrientation</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.6</td></tr><tr><td colspan="3">DF_PositionConfidenceSet(可选)</td></tr><tr><td style='text-align: center;'>&gt;DE_PositionConfidence</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.7</td></tr><tr><td style='text-align: center;'>&gt;DE_ElevationConfidence</td><td style='text-align: center;'>不选</td><td style='text-align: center;'>7.3.2.7</td></tr><tr><td style='text-align: center;'>DE_TransmissionState</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.8</td></tr><tr><td style='text-align: center;'>DE_Speed</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.9</td></tr><tr><td style='text-align: center;'>DE_Heading</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.10</td></tr><tr><td style='text-align: center;'>DE_SteeringWheelAngle</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.11</td></tr><tr><td colspan="3">DF_MotionConfidenceSet(可选)</td></tr><tr><td style='text-align: center;'>&gt;DE_SpeedConfidence</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.12</td></tr><tr><td style='text-align: center;'>&gt;DE_HeadingConfidence</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.12</td></tr><tr><td style='text-align: center;'>&gt;DE_SteeringWheelAngleConfidence</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.12</td></tr></table>

<div style="text-align: center;">表 6 数据发送要求（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元/字段</td><td style='text-align: center;'>数据单元类型(必选/条件性必选/可选/不选)</td><td style='text-align: center;'>内容所在章条</td></tr><tr><td colspan="3">DF_AccelerationSet4Way(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_Acceleration(Longitudinal)</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td style='text-align: center;'>&gt;DE_Acceleration(Lateral)</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td style='text-align: center;'>&gt;DE_VerticalAcceleration</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td style='text-align: center;'>&gt;DE_YawRate</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td colspan="3">DF_BrakeSystemStatus(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_BrakePedalStatus</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_BrakeAppliedStatus</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_TractionControlStatus</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_AntiLockBrakeStatus</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_StabilityControlStatus</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_BrakeBoostApplied</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_AuxiliaryBrakeStatus</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td colspan="3">DF_VehicleSize(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleWidth</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.15</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleLength</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.15</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleHeight</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.15</td></tr><tr><td colspan="3">DF_VehicleClassification(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_BasicVehicleClass</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.16</td></tr><tr><td style='text-align: center;'>&gt;DE_FuelType</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.17</td></tr><tr><td colspan="3">DF_VehicleSafetyExtensions(必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleEventFlags</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>7.3.2.18.2</td></tr><tr><td style='text-align: center;'>&gt;DF_PathHistory</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DE_GNSSstatus</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_PathHistoryPointList</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_PathHistoryPoint</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_PositionOffsetLLV</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_PositionOffsetLL</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_VerticalOffset</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_TimeOffset</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_Speed</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_PositionConfidenceSet</td><td style='text-align: center;'>不选</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_CoarseHeading</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>7.3.2.18.3</td></tr></table>

<div style="text-align: center;">表 6 数据发送要求（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元/字段</td><td style='text-align: center;'>数据单元类型（必选/条件性必选/可选/不选）</td><td style='text-align: center;'>内容所在章条</td></tr><tr><td style='text-align: center;'>&gt;DF_PathPrediction</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.4</td></tr><tr><td style='text-align: center;'>&gt;&gt;DE_RadiusOfCurvature</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.4</td></tr><tr><td style='text-align: center;'>&gt;&gt;DE_Confidence</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>7.3.2.18.4</td></tr><tr><td style='text-align: center;'>&gt;DE_ExteriorLights</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>7.3.2.18.5</td></tr><tr><td colspan="3">DF_VehicleEmergencyExtensions(条件性必选)</td></tr><tr><td style='text-align: center;'>&gt;DE_ResponseType</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>7.3.2.19</td></tr><tr><td style='text-align: center;'>&gt;DE_SirenInUse</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>7.3.2.19</td></tr><tr><td style='text-align: center;'>&gt;DE_LightBarInUse</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>7.3.2.19</td></tr><tr><td colspan="3">注1：“&gt;”表示处于BSM数据包中的第一个层级，“&gt;”表示处于BSM数据包中的第二个层级，依此类推。注2：当YD/T 3709—2020的可选(optional)数据元素在本文件中被要求为必选、条件性必选或不选时，以本文件的填充要求为准。</td></tr></table>

##### 7.3.1.3 拥塞控制与消息生成周期

LTE-V2X 系统发送的 BSM 分为两类，一类为不携带表 26 列举的关键事件标志的常规 BSM，另一类为携带表 26 列举的关键事件标志的关键事件触发 BSM。

常规 BSM 应为周期性生成，默认生成周期应为 100 ms。LTE-V2X 系统每次正常工作后发送的第一个常规 BSM，应在满足数据发送准则后的 0 ms～100 ms 内生成。

关键事件触发 BSM 应在某个触发条件首次满足后立刻生成，并取消原 BSM 的发送，该条 BSM 应包含截止到数据封装时刻的所有有效关键事件标志。在触发条件有效期间，应以上述首个关键事件触发 BSM 的生成时刻为起点，持续按照 100 ms 的生成周期生成关键事件触发 BSM。在一个具体触发条件无效后，应取消 BSM 中携带的相应关键事件标志。

注：关键事件触发 BSM 的发送示例见附录 B。

LTE-V2X 系统的应用层应对常规 BSM 进行拥塞控制，拥塞控制机制见附录 C。

##### 7.3.1.4 优先级设置

当发送常规 BSM 时，LTE-V2X 系统应将网络层 DSM.request 原语中的优先级参数 Priority 设置为 112。

当发送关键事件触发 BSM 时，LTE-V2X 系统应将网络层 DSM.request 原语中的优先级参数 Priority 设置为 208。

##### 7.3.1.5 包延迟预算(PDB)设置

对于常规 BSM 的传输，PDB 宜设置为 100 ms；对于关键事件触发 BSM 的传输，PDB 宜设置为 50 ms。

##### 7.3.1.6 调用底层传输服务

LTE-V2X 系统应调用网络层 DSM.request 原语发送 BSM，并满足如下要求：

a）应使用广播方式发送；

b) 应按照表 7 设置 AID 参数；

c） 应设置 Network ProtocolType 参数为 4；

d）应按照7.3.1.4设置Priority参数；

e） 可设置业务周期 Traffic Period 参数为应用层当前的 BSM 生成周期；

f）按照 7.4.5.2 要求更换假名证书时，应设置 Application layer ID changed 参数。

<div style="text-align: center;">表 7 AID 取值及条件</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>AID取值(十六进制紧凑编码)</td><td style='text-align: center;'>AID取值(十进制)</td><td style='text-align: center;'>条件</td></tr><tr><td style='text-align: center;'>0p6f</td><td style='text-align: center;'>111</td><td style='text-align: center;'>普通车辆发送的常规BSM</td></tr><tr><td style='text-align: center;'>0p70</td><td style='text-align: center;'>112</td><td style='text-align: center;'>普通车辆发送的关键事件触发BSM</td></tr><tr><td style='text-align: center;'>0p71</td><td style='text-align: center;'>113</td><td style='text-align: center;'>当紧急车辆满足7.3.2.19c)时发送的常规BSM</td></tr><tr><td style='text-align: center;'>0p72</td><td style='text-align: center;'>114</td><td style='text-align: center;'>当紧急车辆满足7.3.2.19c)时发送的关键事件触发BSM</td></tr></table>

#### 7.3.2 数据单元

##### 7.3.2.1 消息编号

LTE-V2X 系统设备启动后发送第一条 BSM 时，应将消息编号 DE_MsgCount 初始化为一个随机整数，其范围为 $$ 0,127 $$ ，DE_MsgCount 的具体描述见表 8。

若发送上一条 BSM 之后，更换了用于签名 BSM 的证书，则 LTE-V2X 系统在发送下一条 BSM 之前应将 DE_MsgCount 重新初始化为一个随机整数。

如果用于签名 BSM 的证书自从发送上一条 BSM 之后无变更，则 LTE-V2X 系统应将 DE_MsgCount 设置为发送前一条 BSM 所用的值加 1；若编号达到 127，则下一条 BSM 中的 DE_MsgCount 值回到 0。

<div style="text-align: center;">表 8 消息编号数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_MsgCount</td><td style='text-align: center;'>消息编号</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,127]</td><td style='text-align: center;'>LTE-V2X系统对发送的BSM依次进行编号</td><td style='text-align: center;'>1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.2 车辆临时 ID 号

LTE-V2X 系统应将启动后生成的第一条 BSM 的 id 初始化为随机值，id 的具体描述见表 9。

若发送上一条 BSM 之后，更换了用于签名 BSM 的证书，则 LTE-V2X 系统在发送下一条 BSM 之前应将 id 重新初始化为随机值。如果证书无变更，则 LTE-V2X 系统不应改变 id。

<div style="text-align: center;">表 9 车辆临时 ID 号数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>车辆临时ID号</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>长度为8 byte的字节序列</td><td style='text-align: center;'>7.3.2.2 文字描述</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.3 时间

LTE-V2X 系统应以 UTC 作为参考时间设置 DE_DSecond。

DE_DSecond 的数值表示的时间是本条 BSM 中的车辆位置数据(DF_Position3D)所对应的时刻。DE_DSecond 的具体描述见表 10。

DE_DSecond 的数值所表示的时间与本条 BSM 的生成时间之间的偏差应小于 150 ms。

注：上述要求使得 BSM 不包含任何早于生成该 BSM 的 UTC 减去 150 ms 时间点的信息。

<div style="text-align: center;">表 10 时间数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_DSecond</td><td style='text-align: center;'>1 min内的毫秒级时刻</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,60 999]</td><td style='text-align: center;'>7.3.2.3 文字描述</td><td style='text-align: center;'>1 ms</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.4 时间置信度

LTE-V2X 系统应将 DE_TimeConfidence 设置为 DE_Dsecond 的时间精度，其置信度水平为 95%。DE_TimeConfidence 的具体描述见表 11。

<div style="text-align: center;">表 11 时间置信度数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_TimeConfidence</td><td style='text-align: center;'>时间置信度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>数值0～39，数值定义参照YD/T 3709—2020的5.2.4.74</td><td style='text-align: center;'>数值描述了95%置信水平的时间精度</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.5 车辆位置

LTE-V2X 系统应按如下要求设置自车的纬度(DE Latitude)和经度(DE Longitude)坐标：

a）由车载定位子系统输出；

b) 定位参考点满足 6.2 的要求；

c）满足国家地理信息相关管理要求。

数据帧 DF_Position3D 的各个数据单元描述见表 12。

<div style="text-align: center;">表 12 车辆位置数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_Latitude</td><td style='text-align: center;'>纬度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-900 000 000, 900 000 000]</td><td style='text-align: center;'>北纬为正,南纬为负;填充值在正负90°范围之内</td><td style='text-align: center;'>10-7</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_Longitude</td><td style='text-align: center;'>经度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-1 799 999 999, 1 800 000 000]</td><td style='text-align: center;'>东经为正,西经为负;填充值在正负180°范围之内</td><td style='text-align: center;'>10-7</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_Elevation</td><td style='text-align: center;'>车辆海拔高程</td><td style='text-align: center;'>不选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.6 车辆位置精度

LTE-V2X 系统应使用 DF_PositionalAccuracy 来表示车辆位置的实际精度。

DF_PositionalAccuracy 应能提供 DE_SemiMajorAxisAccuracy、DE_SemiMinorAxisAccuracy、DE_SemiMajorAxisOrientation 3 个数据元素，其具体描述见表 13。这 3 个数据元素至少应从 GNSS 接收机中获得。

<div style="text-align: center;">表 13 车辆位置精度数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_SemiMajorAxisAccuracy</td><td style='text-align: center;'>表示车辆位置精度误差椭圆的长半轴</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,255]</td><td style='text-align: center;'>表示范围0m～12.7m；数值等于或大于12.7m，应填写为254</td><td style='text-align: center;'>0.05m</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>255</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_SemiMinorAxisAccuracy</td><td style='text-align: center;'>表示车辆位置精度误差椭圆的短半轴</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,255]</td><td style='text-align: center;'>表示范围0m～12.7m；数值等于或大于12.7m，应填写为254</td><td style='text-align: center;'>0.05m</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>255</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_SemiMajorAxisOrientation</td><td style='text-align: center;'>表示车辆位置精度误差椭圆的长轴和正北方向的夹角</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,65535]</td><td style='text-align: center;'>表示相对正北方向0°～359.9945078786°</td><td style='text-align: center;'>0.0054932479°</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>65535</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

##### 7.3.2.7 车辆位置综合精度

LTE-V2X 系统应以综合位置精度 DF_PositionConfidenceSet 描述定位置信区间与定位能力。车

辆位置综合精度数据帧的具体描述见表14。

<div style="text-align: center;">表 14 车辆位置综合精度数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_PositionConfidence</td><td style='text-align: center;'>车辆位置综合精度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>枚举值(0)～(15)</td><td style='text-align: center;'>(0):无效值(1):500 m(2):200 m(3):100 m(4):50 m(5):20 m(6):10 m(7):5 m(8):2 m(9):1 m(10):0.5 m(11):0.2 m(12):0.1 m(13):0.05 m(14):0.02 m(15):0.01 m</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_ElevationConfidence</td><td style='text-align: center;'>其数值描述了95%置信水平的车辆高程精度</td><td style='text-align: center;'>不选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.8 车辆挡位状态

DE TransmissionState 应能反映车辆的实际挡位状态，其具体描述见表 15。

注：前进挡(forwardGears)包含自动挡车辆前进挡、手动挡车辆用于前进的各挡位等。

<div style="text-align: center;">表 15 车辆挡位状态数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_TransmissionState</td><td style='text-align: center;'>车辆挡位信息</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>枚举值(0)～(7)</td><td style='text-align: center;'>(0):Neutral(空挡)(1):Park(停止挡)(2):ForwardGears(前进挡)(3):ReverseGears(倒挡)(4):(6):保留位(7):Unavailable(无效值)</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>7</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

##### 7.3.2.9 车辆速度

LTE-V2X 系统应基于车辆的实时速度填写 BSM 中的车辆速度数据单元，具体要求见表 16。

<div style="text-align: center;">表 16 车辆速度数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_Speed</td><td style='text-align: center;'>车辆速度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,8191]</td><td style='text-align: center;'>车辆实时速度标量</td><td style='text-align: center;'>0.02 m/s</td><td style='text-align: center;'>$ \pm $ 0.28 m/s (68%置信度)</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.10 车辆航向角

DE_Heading 描述车辆运动方向，其值以正北方向为  $ 0^{\circ} $ ，按顺时针方向增加，具体描述见表 17。车辆航向角应满足以下要求：

a）当车速不超过  $ 45 \, km/h $  时，DE_Heading 相对车辆的实际航向角的差距在  $ 3^{\circ} $  之内（68% 置信度）；

b）当车速超过45 km/h时，DE_Heading相对车辆的实际航向角的差距在2°之内（68%置信度）。注：车辆运动方向为车辆运动轨迹的变化率方向。

<div style="text-align: center;">表 17 车辆航向角数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_Heading</td><td style='text-align: center;'>车辆航向角</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,28 800]</td><td style='text-align: center;'>车辆运动方向与正北方向的顺时针夹角，表示范围 0°～359.9875°</td><td style='text-align: center;'>0.0125°</td><td style='text-align: center;'>7.3.2.10文字描述</td><td style='text-align: center;'>是</td><td style='text-align: center;'>28 800</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

##### 7.3.2.11 车辆方向盘转角

车辆方向盘转角的具体描述见表 18。

<div style="text-align: center;">表 18 车辆方向盘转角数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_SteeringWheelAngle</td><td style='text-align: center;'>车辆方向盘转角</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-126,127]</td><td style='text-align: center;'>向右为正，向左为负。表示范围-189°到189°。方向盘转角超过189°，将其值置为126；方向盘转角小于-189°，将其值置为-126</td><td style='text-align: center;'>1.5°</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>127</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

##### 7.3.2.12 车辆运行状态精度

车辆运行状态 DF_MotionConfidenceSet 精度包括车速精度(DE_SpeedConfidence)、航向精度(DE_HeadingConfidence)和方向盘转角精度(DE_SteeringWheelAngleConfidence)。数据帧 DF_MotionConfidenceSet 的各个数据单元描述见表 19。

<div style="text-align: center;">表 19 车速运行状态精度数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_SpeedConfidence</td><td style='text-align: center;'>数值描述了95%置信水平的车速精度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(7)</td><td style='text-align: center;'>(0):无效值(1):100 m/s(2):10 m/s(3):5 m/s(4):1 m/s(5):0.1 m/s(6):0.05 m/s(7):0.01 m/s</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_HeadingConfidence</td><td style='text-align: center;'>数值描述了95%置信水平的车辆航向精度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(7)</td><td style='text-align: center;'>(0):无效值(1):10°(2):5°(3):1°(4):0.1°(5):0.05°(6):0.01°(7):0.0125°</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

<div style="text-align: center;">表 19 车速运行状态精度数据帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_SteeringWheelAngleConfidence</td><td style='text-align: center;'>数值描述了95%置信水平的方向盘转角精度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值（0）～（3）</td><td style='text-align: center;'>(0):无效值(1):2°(2):1°(3):0.02°</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

##### 7.3.2.13 车辆四轴加速度

DF_AccelerationSet4Way 包含车辆纵向加速度 $$ DE_Acceleration(Longitudinal) $$ 、车辆横向加速度 $$ DE_Acceleration(Lateral) $$ 、车辆垂直加速度 $$ DE_VerticalAcceleration $$ 和车辆横摆角速度 $$ DE_YawRate $$ 。LTE-V2X 系统应按照 6.2 设置坐标系。此数据帧的各数据单元描述见表 20。

<div style="text-align: center;">表 20 车辆四轴加速度数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_Acceleration(Longitudinal)</td><td style='text-align: center;'>车辆纵向加速度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-2 000, 2 001]</td><td style='text-align: center;'>车头方向为正,车头反向为负。加速度大于或等于20 m/s²,将其值置为2 000;加速度小于或等于-20 m/s²,将其值置为-2 000</td><td style='text-align: center;'>0.01 m/s²</td><td style='text-align: center;'>±0.3 m/s²(68%置信度)</td><td style='text-align: center;'>是</td><td style='text-align: center;'>2001</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_Acceleration(Lateral)</td><td style='text-align: center;'>车辆横向加速度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-2 000, 2 001]</td><td style='text-align: center;'>向右加速为正,向左加速为负。加速度大于或等于20 m/s²,将其值置为2 000;加速度小于或等于-20 m/s²,将其值置为-2 000</td><td style='text-align: center;'>0.01 m/s²</td><td style='text-align: center;'>±0.3 m/s²(68%置信度)</td><td style='text-align: center;'>是</td><td style='text-align: center;'>2001</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

<div style="text-align: center;">表 20 车辆四轴加速度数据帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_Vertical Acceleration</td><td style='text-align: center;'>垂直方向的加速度大小</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-127,127]</td><td style='text-align: center;'>Z轴方向竖直向下，沿着Z轴方向为正，反向为负。当车辆纵向无加速运动时，取值为0；加速度大于或等于25.4m/s²，将其值置为127；加速度小于或等于-25.2m/s²，将其值置为-126</td><td style='text-align: center;'>0.02g，g为重力加速度，取值为9.80665m/s²</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>-127</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_YawRate</td><td style='text-align: center;'>车辆横摆角速度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-32,767,32,767]</td><td style='text-align: center;'>车辆绕垂直轴的偏转，顺时针旋转为正，逆时针为负</td><td style='text-align: center;'>0.01(°)/s</td><td style='text-align: center;'>±0.5(°)/s（68%置信度）</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.14 车辆制动系统状态

当可以获得车辆制动系统状态时，LTE-V2X系统应将车辆总线用作DF_BrakeSystemStatus的数据来源。数据帧DF_BrakeSystemStatus的各个数据单元描述见表21。

对于 DF_BrakeSystemStatus 中的数据元素 DE_BrakeAppliedStatus，其填充规则应满足如下要求：

a）当各个车轮的制动状态可用时，LTE-V2X系统基于相应车轮的制动状态将DE_BrakeAppliedStatus的各个比特设置为1（=true）或0（=false），并将DE_BrakeAppliedStatus的unavailable对应比特设置为0（=false）；

b) 如果仅车辆制动状态指示可用（单个车轮状态不可用），LTE-V2X 系统基于车辆的制动状态将 DE_BrakeAppliedStatus 中 4 个车轮对应比特统一设置为 1（=true）或 0（=false），并将 DE_BrakeAppliedStatus 的 unavailable 对应比特设置为 0（=false）；

c) 当无可用的制动状态时，LTE-V2X 系统将 DE_BrakeAppliedStatus 的 unavailable 对应比特设置为 1(=true)。

注：车轮的制动状态触发时将 DE_BrakeAppliedStatus 的各个比特设置为  $ 1(\text{=true}) $ ，不触发时设置为  $ 0(\text{=false}) $ 。

<div style="text-align: center;">表 21 车辆制动系统状态数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_BrakePedalStatus</td><td style='text-align: center;'>指示制动踏板状态是否处于被踩下状态</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>枚举值(0)～(2)</td><td style='text-align: center;'>(0):无效值(1):制动踏板未踩下(2):制动踏板踩下</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

<div style="text-align: center;">表 21 车辆制动系统状态数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_BrakeAppliedStatus</td><td style='text-align: center;'>四轮分别的制动状态</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>5位数值B&#x27;00000～B&#x27;11111</td><td style='text-align: center;'>7.3.2.14第二段描述。从左向右数，第1个比特代表未装备/未知/不可用，第2个比特代表左前轮状态，第3个比特代表左后轮状态，第4个比特代表右前轮状态，第5个比特代表右后轮状态。当车辆某一组轮胎由多个组成时，将其状态等效为一个数值</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>B&#x27;00000</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_TractionControlStatus</td><td style='text-align: center;'>定义牵引力控制系统TCS实时状态</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>枚举值(0)～(3)</td><td style='text-align: center;'>(0):无效值(1):系统处于关闭状态(2):系统处于开启状态，但未触发(3):系统被触发，处于作用状态</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_AntiLockBrakeStatus</td><td style='text-align: center;'>定义ABS状态</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(3)</td><td style='text-align: center;'>(0):无效值(1):LTE-V2X系统处于关闭状态(2):LTE-V2X系统处于开启状态，但未触发(3):LTE-V2X系统被触发，处于作用状态</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_StabilityControlStatus</td><td style='text-align: center;'>车辆动态稳定控制系统状态</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(3)</td><td style='text-align: center;'>(0):无效值(1):系统处于关闭状态(2):系统处于开启状态，但未触发(3):系统被触发，处于作用状态</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_BrakeBoostApplied</td><td style='text-align: center;'>制动助力系统的状态</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(2)</td><td style='text-align: center;'>(0):无效值(1):制动助力系统关闭(2):制动助力系统开启</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_AuxiliaryBrakeStatus</td><td style='text-align: center;'>指示制动辅助系统状态</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(3)</td><td style='text-align: center;'>(0)B&#x27;00:无效值(1)B&#x27;01:制动辅助系统关闭(2)B&#x27;10:制动辅助系统开启(3)B&#x27;11:保留位</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号、LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

##### 7.3.2.15 车辆尺寸

车辆尺寸 DF_VehicleSize 包含车辆车身宽度（DE_VehicleWidth）、车辆车身长度（DE_VehicleLength）和车辆车身高度（DE_VehicleHeight）。数据帧 DF_VehicleSize 的各个数据单元描述见表 22。

<div style="text-align: center;">表 22 车辆尺寸数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_VehicleWidth</td><td style='text-align: center;'>车身宽度(包含外部后视镜等原始设备)</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,1023]</td><td style='text-align: center;'>能够描述的最大车身宽度为10.23 m</td><td style='text-align: center;'>0.01 m</td><td style='text-align: center;'>0.2 m</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_VehicleLength</td><td style='text-align: center;'>车身长度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,4095]</td><td style='text-align: center;'>能够描述的最长车身长度为40.95 m</td><td style='text-align: center;'>0.01 m</td><td style='text-align: center;'>0.2 m</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_VehicleHeight</td><td style='text-align: center;'>车身高度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>[0,127]</td><td style='text-align: center;'>能够描述的最高车身高度为6.35 m</td><td style='text-align: center;'>0.05 m</td><td style='text-align: center;'>0.2 m</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.16 车辆基本类型

车辆基本类型 DF_VehicleClassification 数据单元描述见表 23，车辆基本类型及编号应符合附录 D 的规定。

<div style="text-align: center;">表 23 车辆基本类型数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_BasicVehicleClass</td><td style='text-align: center;'>车辆基本类型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0,255]</td><td style='text-align: center;'>以对应车辆类型编号进行填充</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.17 燃料类型

车辆燃料动力类型描述见表 24。

<div style="text-align: center;">表 24 燃料动力类型数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_Fuel Type</td><td style='text-align: center;'>燃料动力类型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>枚举值(0)～(15)</td><td style='text-align: center;'>(0): 未知燃料动力类型(1): 汽油(2): 甲醇(3): 柴油(4): 纯电动(5): 混合动力(6): 氢动力(含燃料电池电动)(7): 气体燃料(8): 双燃料(9): 两用燃料(10): 保留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.18 车辆安全辅助信息集合

###### 7.3.2.18.1 车辆安全辅助信息集合数据帧

车辆安全辅助信息集合 DF_VehicleSafetyExtensions 是 BSM 中基础安全数据的补充，包括车辆事件标志（DE_VehicleEventFlags）、车辆历史轨迹（DF_PathHistory）、车辆预测路线（DF_PathPrediction）、车身灯光状态（DE_ExteriorLights）。

###### 7.3.2.18.2 车辆事件标志位

关键事件条件刚被满足的时刻与生成包含对应的 DE_VehicleEventFlags 比特集合的第一条 BSM 的时刻之间的时间差应小于 250 ms。当有另一个关键事件正在进行时，应仍然满足该要求。

当关键事件条件被满足时，LTE-V2X系统应设置该事件标志。如果信息可用，LTE-V2X系统在表26中关键事件条件发生时设置相应的关键事件标志，且能支持其他事件标志。车辆事件标志数据单元具体描述见表25。

<div style="text-align: center;">表 25 车辆事件标志数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_VehicleEventFlags</td><td style='text-align: center;'>车辆的特殊状态</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>13位数值B&#x27;0000000000000～B&#x27;111111111111</td><td style='text-align: center;'>如果数据某一位被置1，表示车辆处于该位对应的状态。当至少有一种对应状态被激活或者从激活状态恢复，该标志数值才应被设置。(1)、(5)、(6)、(8)、(9)可不发送。从左向右数，各个数据位表示内容如下：(0)第1个比特表示Hazard Lights:危险信号灯亮起；(1)第2个比特表示StopLineViolation:车辆在到达路口前预测自己无法及时制动而越过停止线；(2)第3个比特表示ABS:ABS系统被触发并超过100ms；(3)第4个比特表示Traction Control:电子系统控制牵引力被触发并超过100ms；(4)第5个比特表示Stability Control:车身稳定控制被触发并超过100ms；(5)第6个比特表示Hazardous Materials:危险品运输车；(6)第7个比特表示Reserved1:保留位；(7)第8个比特表示Hard Braking:车辆紧急制动，并且减速度大于4m/s²；(8)第9个比特表示Lights Changed:过去2s内，车灯状态改变；(9)第10个比特表示Wipers Changed:过去2s内，车辆雨刷(前窗或后窗)状态改变；(10)第11个比特表示Flat tire:单个或多个轮胎欠压报警；(11)第12个比特表示Disabled Vehicle:除上述所列的导致车辆无法正常行驶的安全故障；(12)第13个比特表示Air Bag Deployment:至少1个安全气囊从正常状态变为弹出状态</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

关键事件触发类 BSM 对应的关键事件见表 26。当表 26 中关键事件触发且车辆能获取此项事件对应的触发状态信号时，应发送对应关键事件触发消息。

<div style="text-align: center;">表 26 关键事件标志位及对应触发状态</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>车辆关键事件标志位</td><td style='text-align: center;'>关键事件及对应的触发状态</td></tr><tr><td style='text-align: center;'>(0):Hazard Lights</td><td style='text-align: center;'>车辆危险信号灯亮起</td></tr><tr><td style='text-align: center;'>(1):eventABSactivated</td><td style='text-align: center;'>ABS系统被触发并超过100 ms</td></tr><tr><td style='text-align: center;'>(2):eventTractionControlLoss</td><td style='text-align: center;'>电子牵引力控制系统被触发并超过100 ms</td></tr><tr><td style='text-align: center;'>(3):eventStabilityControlactivated</td><td style='text-align: center;'>车身稳定控制被触发并超过100 ms</td></tr><tr><td style='text-align: center;'>(4):eventHardBraking</td><td style='text-align: center;'>车辆紧急制动</td></tr><tr><td style='text-align: center;'>(5):eventFlatTire</td><td style='text-align: center;'>单个或多个轮胎欠压报警(参考GB 26149—2017)</td></tr><tr><td style='text-align: center;'>(6):eventDisabledVehicle</td><td style='text-align: center;'>由上述之外的行车安全故障导致的无法正常行驶</td></tr><tr><td style='text-align: center;'>(7):eventAirBagDeployment</td><td style='text-align: center;'>当至少1个安全气囊从正常状态变为弹出状态时，在车辆蓄电池可以持续正常供电且LTE-V2X系统可以正常工作的情况下，LTE-V2X系统发送BSM至少10 min</td></tr></table>

###### 7.3.2.18.3 车辆历史轨迹

LTE-V2X 系统应按如下所述填充 BSM 中 DF_VehicleSafetyExtensions 数据帧中的 DF_PathHistoryPointList。车辆历史轨迹包含了过去一段时间内的车辆的位置序列。DF_PathHistory 和 DF_PathHistoryPoint 不应包含 BSM 中已经存在的信息。位置坐标系应满足 6.2 的要求。

在 DF_PathHistoryPointList 中，填充 DF_PathHistoryPoint 数据帧，应使用最小比特长度的数据帧发送数据，不应使用较大数据帧发送较小的偏差数值（例如不得使用 DF_Position-LL-28B 表达小于 0.0002047° 的偏差数值）。

当假名证书变更时，LTE-V2X系统应清空历史轨迹数据相应的存储区。

除以下 PH 距离可以小于 200 m 的情况外，LTE-V2X 系统应以 PH 点填充 DF_PathHistory，使得所表示的 PH 距离（即沿车辆轨迹的第一个和最后一个 PH 点之间的距离）至少为 200 m 且不超过 400 m：

a）车辆使用当前假名证书所行驶的物理距离小于200 m（例如初始态或假名证书更换）；

b) 历史位置不可用, PH 小于 200 m;

c）LTE-V2X系统携带的PH点的数目超过15，但是车辆行驶的物理距离小于200 m。

注：基于广泛的测试，DF_PathHistory 以 91.3% 的概率包含 5 个点或更少（在非对齐压缩编码规则编码之前小于或等于 40 bytes）。

LTE-V2X 系统应维护一条车辆轨迹以表征车辆近期运动，该轨迹由车载定位子系统输出的数据元素组成，可按周期性时间间隔（典型情况为与 BSM 发送频率相同）采样。

LTE-V2X 系统应以 PH 点填充 DF_PathHistory，使得车辆轨迹上任意一点，到其相邻两 PH 点之间连线，或其相邻的 BSM 当前位置点（DF_Position3D）与第 1 个 PH 点之间连线的垂直距离小于 1 m，见附录 E。

LTE-V2X 系统应从可用的车辆轨迹位置数据中选择一个子集，以最少数目的 PH 点填充 DF_PathHistory，以满足上述 1 m 和 200 m 的相关要求。

LTE-V2X 系统应以按照时间排序的 PH 点填充 DF_PathHistory，其中第一个 PH 点在时间上与

当前的 UTC 时间最接近。

如果满足本节前述要求所需的 PH 点数目超过了 15，LTE-V2X 系统应以计算出的点集内不超过 15 数目的点填充 DF_PathHistory。

每一个 PH 点的位置偏移值应以所在 BSM 中的当前位置(DF_Position3D)为基准。每一个 PH 点的时间偏移值应以所在 BSM 中的 DE_DSecond 为基准。

数据帧 DF_PathHistory 的具体描述见表 27。

<div style="text-align: center;">表 27 车辆历史轨迹数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DF_PathHistory</td><td style='text-align: center;'>利用一个参考轨迹点信息，以及一系列基于该参考信息的PH点，给出车辆一段PH</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>PH 应降频发送，PathHistory的默认发送间隔为500 ms。距离上一次发送PH信息500 ms后的第一个BSM应包含PathHistory</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_GNSSstatus</td><td style='text-align: center;'>包括设备工作状态、锁星情况和修正信息等。GNSS系统可以是GPS、BDS等相关系统和设备</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>长度为8的比特序列</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DF_PathHistoryPointList</td><td style='text-align: center;'>PH点的集合，定义车辆的历史轨迹</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DF_PathHistoryPoint</td><td style='text-align: center;'>车辆的历史轨迹点</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DF_PositionOffsetLLV</td><td style='text-align: center;'>车辆三维相对位置（相对经度、相对纬度和相对高度）。偏差值等于真实值减去参考值</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>见7.3.2.18.3文字描述</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DF_PositionOffsetLL</td><td style='text-align: center;'>经纬度偏差，描述一个坐标点的相对位置</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>DF_Position-LL-24BDF_Position-LL-28BDF_Position-LL-32BDF_Position-LL-36B</td><td style='text-align: center;'>偏差值等于真实值减去参考值</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

<div style="text-align: center;">表 27 车辆历史轨迹数据帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DF_Vertical Offset</td><td style='text-align: center;'>定义垂直方向位置偏差</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_Time Offset</td><td style='text-align: center;'>定义当前描述时刻(较早)相对于参考时间点(较晚)的偏差</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[1,65 535]</td><td style='text-align: center;'>以10 ms为单位,定义当前描述时刻(较早)相对于参考时间点(较晚)的偏差。表述范围:0.01 s～10 min 55.34 s时间偏差大于或等于655.34 s,将值置为65 534</td><td style='text-align: center;'>10 ms</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>65535</td><td style='text-align: center;'>无法取得信号,LTE V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_Speed</td><td style='text-align: center;'>车辆速度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>[0,8 191]</td><td style='text-align: center;'>车辆实时速度标量</td><td style='text-align: center;'>0.02 m/s</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_Coarse Heading</td><td style='text-align: center;'>粗粒度的车辆航向角</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>[0,240]</td><td style='text-align: center;'>车辆运动方向与正北方向的顺时针夹角,表示范围0°～358.5°</td><td style='text-align: center;'>1.5°</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>240</td><td style='text-align: center;'>无法取得信号,LTE V2X系统启动、通信异常、未安装等情况</td></tr></table>

###### 7.3.2.18.4 车辆预测路线

LTE-V2X 系统应按如下所述填充 BSM 中 DF_VehicleSafetyExtensions 数据帧中的 DF_PathPrediction。

当车辆处于曲率半径  $ 100 \, m \sim 2500 \, m $  范围内的稳态条件下，LTE-V2X 系统应以计算的半径填充 DF_PathPrediction，该半径相对实际半径的差距小于 2%。

注：出于轨迹预测的目的，当车辆行驶于有恒定半径的曲线时视为稳态条件。稳态时横摆角加速度的绝对值的平均值小于 $ 0.5\left({}^{\circ}\right)/s^{2} $ 。

在从恒定曲率半径  $ R_{1} $  过渡到恒定曲率半径  $ R_{2} $  之后，LTE-V2X 系统应在 4 s 时间内重新填充 DF PathPrediction，该半径相对实际半径的差距小于 2%。

当发送的车辆速度小于  $ 1 \, m/s $  时，LTE-V2X 系统应将半径填充为 32 767（表示直线轨迹），置信度填充为 200（表示置信度 100%）。

当发送的车辆半径大于最大半径(最大半径为2500 m)时，LTE-V2X系统应将半径填充为32767（表示直线轨迹），置信度填充为200（表示置信度100%）。

当发送的车辆半径小于最小半径(最小半径为  $ 100 \, m $ ) 时，LTE-V2X 系统应以计算的数值填充，置信度填充为 0（对应数据元素的值为 0）。

数据帧 DF_PathPrediction 的具体描述见表 28。

<div style="text-align: center;">表 28 车辆预测路线数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DF_Path Prediction</td><td style='text-align: center;'>车辆的预测路线</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.4 文字描述</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_Radius OfCurvature</td><td style='text-align: center;'>车辆预测自身前方行驶轨迹的曲率半径</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[-32 767, 32 767]</td><td style='text-align: center;'>轨迹曲线向右偏转(圆心在车辆行驶方向右侧)数值为正,向左为负。数值 32 767 表示直线行驶</td><td style='text-align: center;'>0.1 m</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DE_Confidence</td><td style='text-align: center;'>表示车辆预测路线置信度</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>[0, 200]</td><td style='text-align: center;'>用 0~200 之间的整数值表示 0~100 的置信度</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

###### 7.3.2.18.5 车身灯光状态

车身灯光状态数据单元描述见表29。

<div style="text-align: center;">表 29 车身灯光状态数据单元</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_ExteriorLights</td><td style='text-align: center;'>车辆外部的车灯状态</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>9位数值，B&#x27;000000000～B&#x27;11111111</td><td style='text-align: center;'>车灯开启设置对应比特位为1，未开启或未安装设置对应比特位为0。仅自动大灯为1可不发送该数据单元，全为0不应发送该数据单元。从左向右数，第1个比特代表近光灯，第2个比特代表远光灯，第3个比特代表左转信号灯，第4个比特代表右转信号灯，第5个比特代表危险信号灯，第6个比特代表自动大灯，第7个比特代表日间行车灯，第8个比特代表雾灯（车辆任一雾灯开启时应进行置位，全部雾灯关闭时应不置位），第9个比特代表驻车灯</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>否</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

##### 7.3.2.19 紧急车辆当前状态的集合

安装在紧急车辆上的 LTE-V2X 系统，应满足以下要求：

a）当车辆的警笛或任何专用发声装置工作时，将 DF_VehicleEmergencyExtensions 中的 SirenInUse 设置为 inUse(2)；

b) 当车辆的警示灯或外置专用显示设备工作时，将 DF_VehicleEmergencyExtensions 中的 LightbarInUse 设置为 inUse(2);

c) 当满足 a) 和/或 b) 时，将 DF_VehicleEmergencyExtensions 中的 ResponseType 设置为 emergency(1)。

注：紧急车辆包括警用车、消防车、救护车、工程救险车等紧急车辆。紧急车辆类型见附录D。

DF_VehicleEmergencyExtensions 包含紧急车辆行驶状态或驾驶行为 (DE_ResponseType)、警笛状态 (DE_SirenInUse) 和警示灯状态 (DE_LightBarInUse)。紧急车辆当前的行驶状态或驾驶行为数据帧见表 30。

当紧急车辆不满足以上条件或车辆为普通车辆时，LTE-V2X系统应不发送DF_VehicleEmergencyExtensions。

<div style="text-align: center;">表 30 紧急车辆当前的行驶状态或驾驶行为数据帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据单元</td><td style='text-align: center;'>字段定义</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>数值分辨率</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>是否可以设为无效值</td><td style='text-align: center;'>无效值</td><td style='text-align: center;'>无效值填充条件</td></tr><tr><td style='text-align: center;'>DE_ResponseType</td><td style='text-align: center;'>紧急车辆当前的行驶状态或驾驶行为</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>枚举值(0)～(4)</td><td style='text-align: center;'>(0):无效值(1):紧急状态——紧急情况服务中(2):非紧急状态——可用于紧急情况结束后(3):追逐——不稳定的驾驶行为(4):静止——不移动,停止在路边</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号,LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_SirenUse</td><td style='text-align: center;'>紧急车辆的警笛或任何专用发声装置的状态</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>枚举值(0)～(3)</td><td style='text-align: center;'>(0):无效值(1):未使用(2):正在使用(3):保留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号,LTE-V2X系统启动、通信异常、未安装等情况</td></tr><tr><td style='text-align: center;'>DE_LightBarInUse</td><td style='text-align: center;'>紧急车辆的警示灯或外置专用显示设备的工作状态</td><td style='text-align: center;'>条件性必选</td><td style='text-align: center;'>枚举值(0)～(7)</td><td style='text-align: center;'>(0):无效值(1):未使用(2):正在使用(3):黄色警示灯(4):未定义(5):箭头指示方向运动(6):慢行车辆(7):频繁停止</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>是</td><td style='text-align: center;'>0</td><td style='text-align: center;'>无法取得信号,LTE-V2X系统启动、通信异常、未安装等情况</td></tr></table>

### 7.4 通信安全要求

#### 7.4.1 通用要求

LTE-V2X 系统应从可信机构的安全证书管理系统获得并存储所需的假名证书或身份证书、可信根证书列表、可信域证书列表、证书撤销列表。

#### 7.4.2 安全层消息发送要求

##### 7.4.2.1 数据格式

LTE-V2X 系统发送 BSM 时使用的数字证书、SPDU 及编码格式，应符合 YD/T 3957—2021 中 6.3、6.4、6.5 的相关要求。

##### 7.4.2.2 数据发送

安全层数据发送应满足以下要求：

a）根据 YD/T 3957—2021 中 6.1.9.3 消息签名过程中证书一致性检查的要求，当不存在能够通过一致性检查的假名证书或身份证书时，不发送 BSM 消息；

b) 紧急车辆满足 7.3.2.19 c) 时发送的 BSM 使用身份证书；

c） LTE-V2X 系统构造 SPDU 进行安全层消息发送，SPDU 的字段填充要求满足表 31。

<div style="text-align: center;">表 31 SPDU 的字段填充要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="6">SPDU(V2XSecData 数据结构)</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>填充方法</td></tr><tr><td colspan="6">protocolVersion</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>按照7.4.3.1进行填充</td></tr><tr><td rowspan="16">content signedData</td><td rowspan="14">tbsData</td><td colspan="4">hashId</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>按照7.4.3.2进行填充</td></tr><tr><td rowspan="3">payload</td><td rowspan="2">data</td><td colspan="2">protocolVersion</td><td style='text-align: center;'>必选</td><td rowspan="3">按照7.4.3.3进行填充</td></tr><tr><td colspan="2">content</td><td style='text-align: center;'>必选</td></tr><tr><td colspan="3">extDataHash</td><td style='text-align: center;'>可选</td></tr><tr><td rowspan="10">headerInfo</td><td colspan="3">aid</td><td style='text-align: center;'>必选</td><td rowspan="10">按照7.4.3.4进行填充</td></tr><tr><td colspan="3">generationTime</td><td style='text-align: center;'>必选</td></tr><tr><td colspan="3">expiryTime</td><td style='text-align: center;'>可选</td></tr><tr><td colspan="3">generationLocation</td><td style='text-align: center;'>不填充</td></tr><tr><td colspan="3">p2pcdLearningRequest</td><td style='text-align: center;'>可选</td></tr><tr><td colspan="3">missingCtrlIdentifier</td><td style='text-align: center;'>可选</td></tr><tr><td colspan="3">encryptionKey</td><td style='text-align: center;'>可选</td></tr><tr><td colspan="3">inlineP2pcdRequest</td><td style='text-align: center;'>可选</td></tr><tr><td colspan="3">requestedCertificate</td><td style='text-align: center;'>可选</td></tr><tr><td colspan="3">pduFunctionalType</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>signer</td><td colspan="4">digest,certificate,self,x509 四选一</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>按照7.4.3.5进行填充</td></tr><tr><td style='text-align: center;'>signature</td><td colspan="4">sm2Signature</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>按照7.4.3.6进行填充</td></tr></table>

#### 7.4.3 SPDU 数据单元

##### 7.4.3.1 安全层消息(V2XSecData)

protocolVersion 字段应填充为 3，content 字段应选择为 signedData。

##### 7.4.3.2 密码杂凑算法字段(hashId)

hashId 字段应选择为 sm3。

##### 7.4.3.3 数据载荷(payload)

protocolVersion 字段应填充为 3；content 字段应选择为 unsecuredData，unsecuredData 字段应填充为 BSM 的消息帧（MessageFrame）；extDataHash 字段为可选字段，默认不填充。

##### 7.4.3.4 消息安全头(headerInfo)

aid 字段应按照表 7 填充十进制编码的 AID 参数值；generationTime 字段应填充 SPDU 的生成时间；generationLocation 字段不应填充；字段 expiryTime、p2pcdLearningRequest、missingCtrlIdentifier、encryptionKey、inlineP2pcdRequest、requestedCertificate、pduFunctionalType 为可选字段，默认不填充。

##### 7.4.3.5 签名者(signer)

signer 字段应选择为 digest 或 certificate，不应选择 self 或 x509，且应满足以下要求。

a）选择 certificate 时 SEQUENCE 的 SIZE 为 1，即不附加证书链中的其他证书机构的证书。

b）在以下情况中附加完整的假名证书(选择 certificate)，在其他情况中附加假名证书的摘要(选择 digest):

1）启动/重启操作后发送的第一条 BSM；

2）使用的假名证书发生变更后发送的第一条 BSM；

3）本条 BSM 距离上一条附加了完整假名证书的 BSM，其时间间隔等于或大于 450 ms；

4）表 26 中至少 1 个关键事件标志位处于置位状态。

##### 7.4.3.6 签名值(signature)

signature 字段应选择为 sm2Signature，密码算法的输入与输出应符合 YD/T 3957—2021 中 D.2 的要求。

#### 7.4.4 安全层消息接收要求

LTE-V2X 系统应对接收到的安全层 SPDU 进行验证。验证内容应满足 YD/T 3957—2021 中 6.1.9.3 的相关要求。

对于接收到的安全层 SPDU，若其 generationTime 早于当前 LTE-V2X 系统时间 1 s 或晚于当前 LTE-V2X 系统时间，则应视为无效数据并丢弃。

注：generationTime 是 YD/T 3957—2021 中的参考时间。

#### 7.4.5 隐私保护要求

##### 7.4.5.1 标识随机化

LTE-V2X 系统应对使用假名证书签名的 BSM 中的相关标识进行随机化处理，并满足以下要求：

a）启动/重启操作后，发送的第一条 BSM 的 24 bit Source_Layer-2 ID 按照 7.2.1 随机初始化；

b) 本条 BSM 与上一条 BSM 所使用的假名证书不同时，本条 BSM 的 24 bit Source_Layer-2 ID 按照 7.2.1 随机变化；

c) 本条 BSM 与上一条 BSM 所使用的假名证书不同时，本条 BSM 的 DE_MsgCount、id 按照 7.3.2.1 和 7.3.2.2 随机变化。

##### 7.4.5.2 假名证书更换

LTE-V2X 系统不应使用过期的假名证书。

LTE-V2X 系统每次进行启动/重启操作后，发送第一条 BSM 时，应从所有有效的假名证书中随机选取一张用于该消息签名，且该假名证书的连续使用时长应重新计时。

在证书有效期内，除以下情况外，同一个假名证书的连续使用时长不应超过300 s：

a） 若 LTE-V2X 系统当前位置距离上一次假名证书变更时的位置的直线距离小于 2100 m（允许误差为 100 m），则 LTE-V2X 系统应继续使用现有假名证书（上次使用的假名证书变更以后发生电源关闭和开启的情况除外）；

b）若表 26 定义的关键事件标志位 DE_VehicleEventFlags 中至少 1 个处于置位状态，则 LTE-V2X 系统应继续使用现有假名证书直至关键事件标志位全部被复位。

关键事件标志置位或行驶距离未达到2100 m，会导致计时达到 $ T(T=300\ \text{s}) $ 时不更换证书，此时继续进行计时。关键事件标志位复位后，若未达到证书更换条件，应继续进行之前计时；若达到证书更换条件，则应立即更换证书，并重新计时。

##### 7.4.5.3 车辆历史轨迹隐私保护要求

当假名证书变更时，LTE-V2X系统应清空历史轨迹数据相应的存储区并按照7.3.2.18.3进行隐私保护。

## 8 通信性能要求

### 8.1 总则

本文件规定的发射性能要求为车辆近水平面辐射功率要求，接收性能要求为车辆天线增益要求和LTE-V2X系统接收灵敏度要求。

### 8.2 发射性能

按照 9.4.1 进行计算，车辆近水平面辐射功率应符合表 32 的规定。按照附录 F 进行车辆方位区域划分。

<div style="text-align: center;">表 32 车辆近水平面辐射功率限值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">方位区域( $ \phi $ )</td><td style='text-align: center;'>俯仰区域( $ \theta $ )
(89°~91°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )
(84°~90°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )
(90°~96°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )
(89°~91°)</td></tr><tr><td colspan="3">车辆近水平面辐射功率/dBm</td><td style='text-align: center;'>70%覆盖/dBm</td></tr><tr><td style='text-align: center;'>[0°,60°)和[300°,360°)</td><td style='text-align: center;'>≥15</td><td style='text-align: center;'>≥12</td><td style='text-align: center;'>≥12</td><td style='text-align: center;'>≥12</td></tr><tr><td style='text-align: center;'>[60°,120°)</td><td style='text-align: center;'>≥9</td><td style='text-align: center;'>≥6</td><td style='text-align: center;'>≥6</td><td style='text-align: center;'>≥6</td></tr><tr><td style='text-align: center;'>[240°,300°)</td><td style='text-align: center;'>≥9</td><td style='text-align: center;'>≥6</td><td style='text-align: center;'>≥6</td><td style='text-align: center;'>≥6</td></tr></table>

<div style="text-align: center;">表 32 车辆近水平面辐射功率限值（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">方位区域( $ \phi $ )</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(89°~91°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(84°~90°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(90°~96°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(89°~91°)</td></tr><tr><td colspan="3">车辆近水平面辐射功率/dBm</td><td style='text-align: center;'>70%覆盖/dBm</td></tr><tr><td style='text-align: center;'>[120°,240°)</td><td style='text-align: center;'>$ \geq $ 15</td><td style='text-align: center;'>$ \geq $ 12</td><td style='text-align: center;'>$ \geq $ 12</td><td style='text-align: center;'>$ \geq $ 12</td></tr><tr><td colspan="5">注:70%覆盖是指在规定的仰角和方位角范围内,所有角度组合的功率值有70%在该限值以上。</td></tr></table>

### 8.3 接收性能

#### 8.3.1 LTE-V2X 系统接收灵敏度

按照 9.4.2.1 进行试验，在吞吐量大于或等于理论值的 95% 的条件下，LTE-V2X 系统接收灵敏度应小于或等于 -86.1 dBm。

#### 8.3.2 车辆天线增益

按照 9.4.2.2 进行试验，车辆天线用于接收信号时的线性平均增益应符合表 33 的规定。按照附录 F 进行车辆方位区域划分。

<div style="text-align: center;">表 33 线性平均增益限值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">方位区域( $ \phi $ )</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(89°~91°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(84°~90°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(90°~96°)</td><td style='text-align: center;'>俯仰区域( $ \theta $ )(89°~91°)</td></tr><tr><td colspan="3">线性平均增益/dBi</td><td style='text-align: center;'>70%覆盖/dBi</td></tr><tr><td style='text-align: center;'>[0°,60°)和[300°,360°)</td><td style='text-align: center;'>$ \geq $ -8</td><td style='text-align: center;'>$ \geq $ -11</td><td style='text-align: center;'>$ \geq $ -11</td><td style='text-align: center;'>$ \geq $ -11</td></tr><tr><td style='text-align: center;'>[60°,120°)</td><td style='text-align: center;'>$ \geq $ -14</td><td style='text-align: center;'>$ \geq $ -17</td><td style='text-align: center;'>$ \geq $ -17</td><td style='text-align: center;'>$ \geq $ -17</td></tr><tr><td style='text-align: center;'>[240°,300°)</td><td style='text-align: center;'>$ \geq $ -14</td><td style='text-align: center;'>$ \geq $ -17</td><td style='text-align: center;'>$ \geq $ -17</td><td style='text-align: center;'>$ \geq $ -17</td></tr><tr><td style='text-align: center;'>[120°,240°)</td><td style='text-align: center;'>$ \geq $ -8</td><td style='text-align: center;'>$ \geq $ -11</td><td style='text-align: center;'>$ \geq $ -11</td><td style='text-align: center;'>$ \geq $ -11</td></tr><tr><td colspan="5">注:70%覆盖是指在规定的仰角和方位角范围内,所有角度组合的增益值有70%在该限值以上。</td></tr></table>

## 9 试验方法

### 9.1 车规环境试验

#### 9.1.1 试验条件

##### 9.1.1.1 试验对象

试验对象为 LTE-V2X 系统。LTE-V2X 系统应至少包含如图 1 所示的无线通信子系统。

##### 9.1.1.2 试验电压

如无其他规定，试验电压应符合表 34 的规定。

<div style="text-align: center;">表 34  试验电压</div>


单位为伏特


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>额定电压</td><td style='text-align: center;'>试验电压( $ U_{t} $ )</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>14±0.2</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>28±0.2</td></tr></table>

##### 9.1.1.3 仪表要求

V2X PC5 消息解析仪表应将预配置参数设置为 YD/T 3756—2024 表 A.1、表 A.2、表 A.3 及表 A.4 对应的取值。

##### 9.1.1.4 试验环境的构建

###### 9.1.1.4.1 通用要求

天线一体式 DUT 进行空口试验，除 9.1.1.4.2 外，应按照图 3 a) 构建试验环境。其中，V2X PC5 消息接收仪表天线应与 DUT 天线正对且间距为 1 m。

天线分体式 DUT 可进行空口试验或传导试验。进行空口试验时，除 9.1.1.4.2 外，应按照图 3 a) 构建试验环境。V2X PC5 消息接收仪表天线与 DUT 天线正对且间距为 1 m。进行传导试验时，除 9.1.1.4.2 外，应按照图 3 b) 构建试验环境。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_814_1033_1090.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3 环境试验通用要求示意图</div>


###### 9.1.1.4.2 特殊要求

在进行9.1.2.2.1、9.1.3.2、9.1.3.4、9.1.3.5、9.1.3.7、9.1.3.8、9.1.3.9、9.1.5.1、9.1.5.2试验时，天线一体式LTE-V2X系统进行空口试验，应按照图4a)构建试验环境。其中，DUT的LTE-V2X天线应接近温箱透波材料且二者的距离至少应为温箱内表面延长的10%，V2X PC5消息接收仪表天线应与DUT的LTE-V2X天线正对且与温箱透波材料间距为1m。

在进行9.1.2.2.1、9.1.3.2、9.1.3.4、9.1.3.5、9.1.3.7、9.1.3.8、9.1.3.9、9.1.5.1、9.1.5.2试验时，天线分体式LTE-V2X系统可进行空口试验或直连试验。进行空口试验时，应按照图4a)构建试验环境。其中，DUT的LTE-V2X天线应接近温箱透波材料且二者的距离至少应为温箱内表面延长的10%，V2X PC5消息接收仪表天线应与DUT的LTE-V2X天线正对且与温箱透波材料间距为1m。进行直连试验时，应按照图4b)构建试验环境。

<div style="text-align: center;"><img src="imgs/img_in_image_box_145_194_557_464.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">a） 空口试验</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_612_193_1029_489.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">图 4  试验特殊要求示意图</div>


##### 9.1.1.5 功能验证

DUT 按照 100 ms 间隔周期性发送 BSM。在连续测试时间 t（单位为秒）内，当 V2X PC5 消息接收仪表接收到的必选数据元素均正确的 BSM 数据包的数量不低于 round $ (t \times 10 \times 95\%) $  时，则视为功能正常。

注 $ ^{1} $ ：round 表示取整数。

注 $ ^{2} $ ：DUT 不能发包和/或发包错误，均统计为发包失败。

#### 9.1.2 电气性能试验

##### 9.1.2.1 直流供电电压

DUT 以表 1 中工作模式 2，先将直流稳压电源电压调至  $ U_{t} $ ，然后逐渐将电压调至  $ U_{Smin} $  稳定 10 min，再逐渐将电压调至  $ U_{Smax} $  稳定 10 min。

##### 9.1.2.2 过电压

###### 9.1.2.2.1 $ T_{max}-20^{\circ}C $  条件下

DUT 以表 1 中的工作模式 2，按照 GB/T 28046.2—2019 中 4.3.1.1.2 和/或 4.3.2.2 的方法进行试验。对于具有过压保护措施的 LTE-V2X 系统，可在试验后进行功能验证。

###### 9.1.2.2.2 室温条件下

DUT 以表 1 中的工作模式 2，按照 GB/T 28046.2—2019 中 4.3.1.2.2 的方法进行试验。对于具有过压保护措施的 LTE-V2X 系统，可在试验后进行功能验证。

##### 9.1.2.3 供电电压缓降和缓升

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.5.2 的方法进行试验。

##### 9.1.2.4 叠加交流电压

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.4.2 严酷度 1 和 2 的方法进行试验。

##### 9.1.2.5 反向电压

DUT 以表 1 中工作模式 2，按照表 35 的方法进行试验。

<div style="text-align: center;">表 35 反向电压试验</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>名称</td><td colspan="2">试验参数</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>$ U_{1} $</td><td style='text-align: center;'>12 V</td><td style='text-align: center;'>24 V</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>试验电压(电源输入接口正负极反接)</td><td style='text-align: center;'>-14 V</td><td style='text-align: center;'>-28 V</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>试验时间</td><td colspan="2">$ (60 \pm 6) $ s</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>试验循环次数</td><td colspan="2">1 次</td></tr></table>

##### 9.1.2.6 供电电压瞬态变化

供电电压瞬态变化试验包括以下3项。

a）供电电压瞬时下降试验

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.6.1.2 的方法进行试验。

b) 复位特性试验

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.6.2.2 的方法进行试验。

c) 启动特性试验

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.6.3.2 等级Ⅱ的方法进行试验。

##### 9.1.2.7 参考接地和供电偏移

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.8.2 的方法进行试验。

##### 9.1.2.8 抛负载

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.6.4.2 的方法进行试验。

##### 9.1.2.9 开路

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中 4.9.1.2 及 4.9.2.2 的方法分别进行试验。

##### 9.1.2.10 短路保护

DUT 以表 1 中工作模式 2，按照 GB/T 28046.2—2019 中的 4.10.2.1 及 4.10.3.1 的方法分别进行试验。

##### 9.1.2.11 绝缘电阻

DUT 以表 1 中工作模式 1，按照 GB/T 28046.2—2019 中 4.12.2 的方法分别进行试验。

#### 9.1.3 环境耐候性试验

##### 9.1.3.1 低温贮存

DUT 以表 3 中贮存环境温度下限和表 1 中工作模式 1，按照 GB/T 28046.4—2011 中 5.1.1.1.2 的方法进行试验。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.2 低温工作

DUT 以表 3 中工作环境温度下限  $ T_{min} $  和表 1 中工作模式 2，按照 GB/T 28046.4—2011 中 5.1.1.2.2 的方法进行试验，试验期间以表 1 中工作模式 2 对 DUT 持续进行功能检查。试验后至少静置 1 h 以恢

复常温，以表1中工作模式2进行功能验证。

##### 9.1.3.3 高温贮存

DUT 以表 3 中贮存温度上限和表 1 中工作模式 1，按照 GB/T 28046.4—2011 中 5.1.2.1.2 的方法进行试验。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.4 高温工作

DUT 以表 3 中工作环境温度上限  $ T_{max} $  和表 1 中工作模式 2，按照 GB/T 28046.4—2011 中 5.1.2.2.2 的方法进行试验，试验期间以表 1 中工作模式 2 对 DUT 持续进行功能检查。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.5 温度梯度

DUT 在表 3 中工作环境温度  $ T_{\min} \sim T_{\max} $  范围内，以表 1 中工作模式 2，按照 GB/T 28046.4—2011 中 5.2.2 的方法进行试验。试验期间以表 1 中工作模式 2 对 DUT 持续进行功能验证。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.6 规定转换时间的温度快速变化

DUT 在表 3 中工作环境温度  $ T_{min} \sim T_{max} $  范围内，按照 GB/T 28046.4—2011 中 5.3.2.2 的方法进行试验。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.7 规定变化率的温度循环

DUT 在表 3 工作环境温度  $ T_{min} \sim T_{max} $  范围内，按照 GB/T 28046.4—2011 中 5.3.1.2 的方法进行试验，试验期间以表 1 中工作模式 2 持续进行功能验证。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.8 湿热循环

DUT 以表 1 中工作模式 2，按照 GB/T 28046.4—2011 中 5.6.2.2 的方法进行试验，试验期间以表 1 中工作模式 2 对 DUT 持续进行功能验证。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.9 稳态湿热

DUT 以表 1 中工作模式 1，按照 GB/T 28046.4—2011 中 5.7.2 的方法进行试验，试验最后 1 h 以表 1 中工作模式 2 持续进行功能验证。试验后静置至少 1 h 以恢复常温，以表 1 中工作模式 2 进行功能验证。

##### 9.1.3.10 耐盐雾

DUT 以表 1 中工作模式 1，按照 GB/T 28046.4—2011 中 5.5.1.2 的方法进行试验，试验后以表 1 中工作模式 2 进行功能验证。

#### 9.1.4 外壳防护试验

防尘试验：DUT以表1中工作模式1，按照GB/T30038—2013中8.3.3.2的方法进行试验，试验后以表1中工作模式2进行功能验证。

防水试验：DUT以表1中工作模式1，按照GB/T30038—2013中8.5.1的方法进行试验，试验后以

表 1 中工作模式 2 进行功能验证。

#### 9.1.5 机械性能试验

##### 9.1.5.1 机械振动

DUT 模拟在车辆上的安装方式在振动台上安装固定，以表 1 中工作模式 2，按照 GB/T 28046.3—2011 中 4.1.2.4.2[乘用车弹性体（车身）] 或 4.1.2.7.2（商用车弹性体）的方法进行试验。试验期间以表 1 中工作模式 2 持续进行功能验证。

##### 9.1.5.2 机械冲击

DUT 以表 1 中工作模式 2，按照 GB/T 28046.3—2011 中 4.2.2.2 的方法进行试验。试验期间以表 1 中工作模式 2 持续进行功能验证。

##### 9.1.5.3 自由跌落

DUT 以表 1 中工作模式 1，按照 GB/T 28046.3—2011 中 5.1.2 的方法进行试验。试验后以表 1 中工作模式 2 进行功能验证。

#### 9.1.6 耐久性试验

DUT 耐久性试验见附录 G 中 G.1，耐久性计算模型见 G.2。

#### 9.1.7 电磁兼容性试验

<div style="text-align: center;"><img src="imgs/img_in_image_box_462_802_500_838.jpg" alt="Image" width="3%" /></div>


##### 9.1.7.1 车辆电磁兼容性试验

###### 9.1.7.1.1 试验对象

试验对象为车辆。

###### 9.1.7.1.2 试验环境条件

试验过程中应进行冷却以防止发动机过热。

试验过程中环境温度为 $ 23\pm5 $  $ ℃ $ ，如果供需双方商定采用其他试验温度应在试验报告中声明。

###### 9.1.7.1.3 试验布置

在进行试验时，应按照图5进行试验布置。将V2X PC5消息接收仪表和GNSS模拟器分别连接至暗室LTE-V2X天线与暗室GNSS天线端口，暗室LTE-V2X天线高度与被测车辆LTE-V2X天线高度相同，水平距离5m。在进行抗扰测试时，暗室LTE-V2X天线应避开抗扰天线波束主波瓣，并确保V2X PC5消息接收仪表与测试系统接收到的功率在其动态范围之内。如有必要，需要在V2X PC5消息接收仪表与天线之间增加工作在V2X频率的带通滤波器，以保证V2X PC5消息接收仪表不受测试时施加的电磁骚扰影响。试验前应确认被测车辆工作状态。抗扰试验中，当施加的干扰信号处于LTE-V2X、GNSS接收机必要带宽内时，接收机的功能判定不需遵循失效准则。发射试验中，不考虑LTE-V2X发射机必要带宽内的有意发射和带外发射。

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_209_987_533.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">a）正视图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_229_595_941_1033.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">b) 俯视图</div>


标引序号说明：

1 ——电波暗室；

2 ——射频吸波材料；

3——带测功机的转台(转台可旋转 $ \pm180^{\circ} $ ，两组轴距可调的转毂以适应车辆不同尺寸和功能)；

4 ——抗扰天线；

5 ——放大器室；

6 ——控制室；

7 —— GNSS 模拟器；

8——V2X PC5 消息接收仪表；

9 —— GNSS 天线；

10——LTE-V2X 天线。

<div style="text-align: center;">图 5 车辆电磁兼容性试验布置示意图</div>


###### 9.1.7.1.4 试验方法

####### 9.1.7.1.4.1 宽带辐射发射试验

车辆以表 1 中工作模式 4，按照 GB 34660—2017 中 5.2 的方法进行试验。

####### 9.1.7.1.4.2 窄带辐射发射试验

车辆以表 1 中工作模式 4，按照 GB 34660—2017 中 5.3 的方法进行试验。

####### 9.1.7.1.4.3 对电磁辐射的抗扰试验

车辆以表 1 中工作模式 4，按照 GB 34660—2017 中 4.4 的抗扰试验强度和 5.4 的方法进行试验，车辆试验条件和失效判定准则见表 36。

<div style="text-align: center;">表 36 车辆抗扰试验条件和失效判定准则</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>车辆试验条件</td><td style='text-align: center;'>失效判定准则</td></tr><tr><td style='text-align: center;'>被测车辆按照 100 ms 间隔周期性发送 BSM</td><td style='text-align: center;'>在连续测试时间  $ t $ （单位为秒）内，V2X PC5 消息接收仪表接收到的 BSM 数据包的数量低于 round( $ t \times 10 \times 95\% $ )</td></tr></table>

##### 9.1.7.2 LTE-V2X 系统电磁兼容性试验

LTE-V2X 系统电磁兼容性试验见附录 A。

### 9.2 定位试验

#### 9.2.1 试验对象

试验对象为车载定位子系统。

#### 9.2.2 试验条件

采用 GNSS 模拟器进行试验。GNSS 模拟器应能模拟产生 BDS/GPS/GALILEO/GLONASS 4 种制式的卫星，应能混合模拟产生至少 2 种制式的卫星信号，应能完成星座仿真、大气传播仿真、用户轨迹仿真、闰秒调整事件仿真。

#### 9.2.3 定位模式试验方法

##### 9.2.3.1 北斗独立

卫星信号模拟器运行表37冷启动状态前置场景，车载定位子系统输出信号并进行定位后断电，使车载定位子系统处于冷启动状态。车载定位子系统上电，卫星信号模拟器按表38运行开阔天空独立北斗动态试验场景。试验场景运行90 s后，检查车载定位子系统输出的三维位置信息。

<div style="text-align: center;">表 37 冷启动状态前置场景参数设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>配置</td></tr><tr><td style='text-align: center;'>位置</td><td style='text-align: center;'>与表 38 要求设置的位置相距大于 1 000 km 且小于 10 000 km</td></tr><tr><td style='text-align: center;'>时间</td><td style='text-align: center;'>比表 38 要求设置的时间提前 2 周以上</td></tr></table>

<div style="text-align: center;">表 37 冷启动状态前置场景参数设置（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>配置</td></tr><tr><td style='text-align: center;'>仿真可见卫星数</td><td style='text-align: center;'>GPS $ \geq $ 6 颗, BDS $ \geq $ 6 颗, GALILEO $ \geq $ 6 颗, GLONASS $ \geq $ 6 颗</td></tr><tr><td style='text-align: center;'>HDOP、PDOP</td><td style='text-align: center;'>HDOP $ \leq $ 2、PDOP $ \leq $ 4</td></tr><tr><td style='text-align: center;'>场景仿真时长</td><td style='text-align: center;'>根据车载定位子系统是否输出定位信息, 最长 1 h</td></tr><tr><td style='text-align: center;'>轨迹</td><td style='text-align: center;'>静止</td></tr><tr><td style='text-align: center;'>信号输出功率</td><td style='text-align: center;'>-130 dBm</td></tr><tr><td style='text-align: center;'>卫星功率是否相同</td><td style='text-align: center;'>是</td></tr></table>

<div style="text-align: center;">表 38 独立北斗动态试验场景关键参数设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>配置</td></tr><tr><td style='text-align: center;'>位置</td><td style='text-align: center;'>中国领土范围内的陆地位置</td></tr><tr><td style='text-align: center;'>卫星星座与信号</td><td style='text-align: center;'>BDS B1I, B1C, B2a, B3I</td></tr><tr><td style='text-align: center;'>仿真可见卫星数</td><td style='text-align: center;'>BDS≥6 颗</td></tr><tr><td style='text-align: center;'>HDOP、PDOP</td><td style='text-align: center;'>开阔天空: HDOP≤1.5, PDOP≤2.5</td></tr><tr><td style='text-align: center;'>场景仿真时长</td><td style='text-align: center;'>1 h</td></tr><tr><td style='text-align: center;'>轨迹</td><td style='text-align: center;'>a) 起始位置开始向北初始速度为 30 km/h;b) 在 85 m 内从 30 km/h 匀加速到 150 km/h;c) 保持 150 km/h 速度运动 730 m 后, 在 85 m 内匀减速到 30 km/h;d) 顺时针 90° 转弯, 转弯半径 20 m, 保持时速 30 km/h;e) 在 85 m 内匀加速到最终速度 150 km/h;f) 保持 150 km/h 速度运动 1230 m 后, 在 85 m 内匀减速到 30 km/h;g) 顺时针 90° 转弯, 转弯半径 20 m, 保持时速 30 km/h。重复 b) ~ g) 来完成矩形(圆角), 并持续同样的运动轨迹至场景结束</td></tr></table>

##### 9.2.3.2 北斗单模

卫星信号模拟器运行表 37 冷启动状态前置场景，车载定位子系统输出信号并进行定位后断电，使车载定位子系统处于冷启动状态。车载定位子系统上电，卫星信号模拟器按表 39 运行开阔天空北斗单模试验场景。试验后，检查车载定位子系统输出的 GSA 信息；以卫星信号模拟器仿真的位置作为真实位置，将车载定位子系统输出的定位数据与真实位置进行比较，计算定位精度。

<div style="text-align: center;">表 39 北斗单模功能试验场景</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>配置</td></tr><tr><td style='text-align: center;'>位置</td><td style='text-align: center;'>中国领土范围内的陆地位置</td></tr><tr><td style='text-align: center;'>卫星星座与信号</td><td style='text-align: center;'>至少应涵盖 BDS B1I, B1C, B2a, B3I, GPS L1, GALILEO E1, GLONASS L1</td></tr><tr><td style='text-align: center;'>仿真可见卫星数</td><td style='text-align: center;'>BDS  $ \geq $  6 颗, GPS  $ \geq $  6 颗, GALILEO  $ \geq $  6 颗, GLONASS  $ \geq $  6 颗</td></tr><tr><td style='text-align: center;'>HDOP、PDOP</td><td style='text-align: center;'>开阔天空: HDOP  $ \leq $  1.5、PDOP  $ \leq $  2.5</td></tr><tr><td style='text-align: center;'>场景仿真时长</td><td style='text-align: center;'>1 h</td></tr></table>

<div style="text-align: center;">表 39 北斗单模功能试验场景（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>配置</td></tr><tr><td style='text-align: center;'>轨迹</td><td style='text-align: center;'>静态</td></tr><tr><td style='text-align: center;'>信号输出功率</td><td style='text-align: center;'>-130 dBm</td></tr><tr><td style='text-align: center;'>卫星功率是否相同</td><td style='text-align: center;'>是</td></tr><tr><td style='text-align: center;'>特殊设置</td><td style='text-align: center;'>在除北斗之外所有导航系统内增加 100 m 卫星时钟噪声</td></tr></table>

#### 9.2.4 定位性能试验方法

GNSS模拟器与车载定位子系统传导连接，如图6所示。车载定位子系统上电后，GNSS模拟器产生60min的动态轨迹，如图7所示，包含加速、减速、匀速、转向等动态阶段。测试场景参数设置如表40所示。读取车载定位子系统输出的定位坐标，将车载定位子系统输出的定位坐标值与GNSS模拟器基准轨迹值做差，查看结果是否满足6.1的要求。

<div style="text-align: center;"><img src="imgs/img_in_image_box_426_666_778_721.jpg" alt="Image" width="29%" /></div>


<div style="text-align: center;">图 6 车载定位子系统传导测试连接示意图</div>


<div style="text-align: center;">表 40 测试场景参数设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参数</td><td style='text-align: center;'>参数设置</td></tr><tr><td style='text-align: center;'>UTC时间</td><td style='text-align: center;'>由供需双方协商确定</td></tr><tr><td style='text-align: center;'>位置</td><td style='text-align: center;'>中国领土范围内的陆地位置</td></tr><tr><td style='text-align: center;'>仿真可见卫星数</td><td style='text-align: center;'>GPS≥6颗,BDS≥6颗,GALILEO≥6颗,GLONASS≥6颗</td></tr><tr><td style='text-align: center;'>HDOP、PDOP</td><td style='text-align: center;'>开阔天空:HDOP≤1.5,PDOP≤2.5</td></tr><tr><td style='text-align: center;'>场景仿真时长</td><td style='text-align: center;'>1 h</td></tr><tr><td style='text-align: center;'>轨迹</td><td style='text-align: center;'>a) 从起始点以10 m/s的初始速度、2 m/s²的加速度向西加速到20 m/s,接着保持匀速运动1 000 m;b) 以2 m/s²的减速度减速到10 m/s,匀速转弯90°,转弯半径为25 m;c) 以2 m/s²的加速度向北加速到20 m/s,保持匀速运动1 400 m;d) 以2 m/s²的减速度减速到10 m/s,匀速转弯90°,转弯半径为25 m;e) 以2 m/s²的加速度向东加速到20 m/s,接着保持匀速运动1 000 m;f) 以2 m/s²的减速度减速到10 m/s,匀速转弯90°,转弯半径为25 m;g) 以2 m/s²的加速度向南加速到20 m/s,保持匀速运动1 400 m;h) 以2 m/s²的减速度减速到10 m/s,匀速转弯90°,转弯半径为25 m。重复a)～h)来完成矩形(圆角),并持续同样的运动轨迹至场景结束</td></tr><tr><td style='text-align: center;'>信号输出功率</td><td style='text-align: center;'>-130 dBm</td></tr><tr><td style='text-align: center;'>卫星功率是否相同</td><td style='text-align: center;'>是</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_330_202_846_799.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图 7 定位轨迹示意图</div>


### 9.3 功能试验

#### 9.3.1 测试集

测试集相关字母及符号解释见表 41。接入层测试集见表 42，网络层测试集见表 43，应用层测试集见表 44、表 45，安全层 SPDU 发送要求测试集见表 46，消息优先级、隐私保护等的发送要求测试集见表 47。

<div style="text-align: center;">表 41 测试集相关字母及符号解释</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标号</td><td style='text-align: center;'>试验类别</td><td style='text-align: center;'>试验方法</td><td style='text-align: center;'>试验方法章条号</td></tr><tr><td style='text-align: center;'>A-1</td><td style='text-align: center;'>数据一致性试验</td><td style='text-align: center;'>道路静态试验</td><td style='text-align: center;'>9.3.3.1</td></tr><tr><td style='text-align: center;'>A-2</td><td style='text-align: center;'>数据一致性试验</td><td style='text-align: center;'>道路动态试验</td><td style='text-align: center;'>9.3.3.2</td></tr><tr><td style='text-align: center;'>A-3</td><td style='text-align: center;'>数据一致性试验</td><td style='text-align: center;'>道路关键事件触发试验</td><td style='text-align: center;'>9.3.3.3</td></tr><tr><td style='text-align: center;'>B-1</td><td style='text-align: center;'>通信安全试验</td><td style='text-align: center;'>试验室静态试验</td><td style='text-align: center;'>9.3.4.1</td></tr><tr><td style='text-align: center;'>B-2</td><td style='text-align: center;'>通信安全试验</td><td style='text-align: center;'>试验室动态试验</td><td style='text-align: center;'>9.3.4.2</td></tr><tr><td style='text-align: center;'>B-3</td><td style='text-align: center;'>通信安全试验</td><td style='text-align: center;'>试验室关键事件触发试验</td><td style='text-align: center;'>9.3.4.3</td></tr><tr><td style='text-align: center;'>✗</td><td colspan="3">第7章中有技术要求，本章中无对应试验内容</td></tr><tr><td style='text-align: center;'>—</td><td colspan="3">第7章中没有技术要求</td></tr></table>

<div style="text-align: center;">表 42 测试集——接入层试验方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验项目</td><td style='text-align: center;'>试验方法</td><td style='text-align: center;'>技术要求章条号</td></tr><tr><td style='text-align: center;'>PDCP</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.1.2.3</td></tr><tr><td style='text-align: center;'>RLC</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.1.2.4</td></tr><tr><td style='text-align: center;'>MAC</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.1.2.5</td></tr></table>

<div style="text-align: center;">表 43 测试集——网络层试验方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验项目</td><td style='text-align: center;'>试验方法</td><td style='text-align: center;'>技术要求章条号</td></tr><tr><td style='text-align: center;'>AID</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.2.1</td></tr><tr><td style='text-align: center;'>DSMP 版本和预留域</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.2.1</td></tr></table>

<div style="text-align: center;">表 44 测试集——应用层 BSM 发送要求试验方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验项目</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>无效值要求</td><td style='text-align: center;'>技术要求章条号</td></tr><tr><td style='text-align: center;'>DE_DSecond</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.3</td></tr><tr><td style='text-align: center;'>DE_TimeConfidence</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.4</td></tr><tr><td style='text-align: center;'>&gt;DE_Latitude</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.5</td></tr><tr><td style='text-align: center;'>&gt;DE_Longitude</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.5</td></tr><tr><td style='text-align: center;'>&gt;DE_Elevation</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.5</td></tr><tr><td style='text-align: center;'>&gt;DE_SemiMajorAxisAccuracy</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.6</td></tr><tr><td style='text-align: center;'>&gt;DE_SemiMinorAxisAccuracy</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.6</td></tr><tr><td style='text-align: center;'>&gt;DE_SemiMajorAxisOrientation</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.6</td></tr><tr><td style='text-align: center;'>&gt;DE_PositionConfidence</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.7</td></tr><tr><td style='text-align: center;'>&gt;DE_ElevationConfidence</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.7</td></tr><tr><td style='text-align: center;'>DE_TransmissionState</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.8</td></tr><tr><td style='text-align: center;'>DE_Speed</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.9</td></tr><tr><td style='text-align: center;'>DE_Heading</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.10</td></tr><tr><td style='text-align: center;'>DE_SteeringWheelAngle</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.11</td></tr><tr><td style='text-align: center;'>&gt;DE_SpeedConfidence</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.12</td></tr><tr><td style='text-align: center;'>&gt;DE_HeadingConfidence</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.12</td></tr><tr><td style='text-align: center;'>&gt;DE_SteeringWheelAngleConfidence</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.12</td></tr><tr><td style='text-align: center;'>&gt;DE_Acceleration(Longitudinal)</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td style='text-align: center;'>&gt;DE_Acceleration(Lateral)</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td style='text-align: center;'>&gt;DE_VerticalAcceleration</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.13</td></tr></table>

<div style="text-align: center;">表 44 测试集——应用层 BSM 发送要求试验方法（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验项目</td><td style='text-align: center;'>填充要求</td><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>填充方法</td><td style='text-align: center;'>精确度要求</td><td style='text-align: center;'>无效值要求</td><td style='text-align: center;'>技术要求章条号</td></tr><tr><td style='text-align: center;'>&gt;DE_YawRate</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.13</td></tr><tr><td style='text-align: center;'>&gt;DE_BrakePedalStatus</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_BrakeAppliedStatus</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_TractionControlStatus</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_AntiLockBrakeStatus</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_StabilityControlStatus</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_BrakeBoostApplied</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_AuxiliaryBrakeStatus</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.14</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleWidth</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.15</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleLength</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.15</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleHeight</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.15</td></tr><tr><td style='text-align: center;'>&gt;DE_BasicVehicleClass</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.16</td></tr><tr><td style='text-align: center;'>&gt;DE_FuelType</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.17</td></tr><tr><td style='text-align: center;'>&gt;DE_VehicleEventFlags</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>A-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.2</td></tr><tr><td style='text-align: center;'>&gt;&gt;DE_GNSSstatus</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;DF_PathHistoryPointList</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_PathHistoryPoint</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_PositionOffsetLLV</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_PositionOffsetLL</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_VerticalOffset</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_TimeOffset</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_Speed</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;&gt;&gt;DF_CoarseHeading</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td style='text-align: center;'>&gt;DF_PathPrediction</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.19.4</td></tr><tr><td style='text-align: center;'>&gt;&gt;DE_RadiusOfCurvature</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.4</td></tr><tr><td style='text-align: center;'>&gt;&gt;DE_Confidence</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.4</td></tr><tr><td style='text-align: center;'>&gt;DE_ExteriorLights</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.5</td></tr><tr><td style='text-align: center;'>&gt;DE_ResponseType</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.19</td></tr><tr><td style='text-align: center;'>&gt;DE_SirenInUse</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.19</td></tr><tr><td style='text-align: center;'>&gt;DE_LightBarInUse</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>7.3.2.19</td></tr></table>

<div style="text-align: center;">表 45 测试集——应用层 BSM 3 个数据元素发送要求及消息优先级、隐私保护等试验方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">试验项目</td><td rowspan="2">填充要求</td><td rowspan="2">取值范围</td><td colspan="5">填充方法</td><td rowspan="2">精确度要求</td><td rowspan="2">无效值要求</td><td rowspan="2">技术要求章条号</td></tr><tr><td style='text-align: center;'>启动试验</td><td style='text-align: center;'>时间试验</td><td style='text-align: center;'>位置改变试验</td><td style='text-align: center;'>关键事件试验</td><td style='text-align: center;'>紧急车辆试验</td></tr><tr><td style='text-align: center;'>DE_MsgCount</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.1</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>A-1</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.2</td></tr><tr><td style='text-align: center;'>DF_PathHistory</td><td style='text-align: center;'>A-2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>7.3.2.18.3</td></tr><tr><td colspan="11">注1:启动试验为被测车辆启动或者重启时,对被测变量进行验证。注2:时间试验为间隔一定时间(至少300 s),对被测变量进行验证。注3:位置改变试验为GNSS模拟器模拟的位置信息发生一定距离改变后,对被测变量进行验证。注4:关键事件试验为被测车辆关键事件触发后,对被测变量进行验证。注5:紧急车辆试验为被测车辆为紧急车辆时,对被测变量进行验证。</td></tr></table>

<div style="text-align: center;">表 46 测试集——安全层 SPDU 发送要求试验方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="6">试验项目</td><td style='text-align: center;'>试验方法</td><td style='text-align: center;'>技术要求章条号</td></tr><tr><td colspan="6">数据格式要求</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.2.1</td></tr><tr><td colspan="6">数据发送要求</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.2.2</td></tr><tr><td colspan="6">protocolVersion</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.1</td></tr><tr><td rowspan="4">content</td><td rowspan="4">signedData</td><td colspan="4">hashId</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.2</td></tr><tr><td rowspan="3">tbsData</td><td rowspan="3">payload</td><td rowspan="2">data</td><td style='text-align: center;'>protocolVersion</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.3</td></tr><tr><td style='text-align: center;'>content</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.3</td></tr><tr><td colspan="2">extDataHash</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.3</td></tr><tr><td rowspan="9">content</td><td rowspan="9">signedData</td><td rowspan="9">tbsData</td><td rowspan="9">headerInfo</td><td colspan="2">generationTime</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">expiryTime</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">generationLocation</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">p2pcdLearningRequest</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">missingCrlIdentifier</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">encryptionKey</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">inlineP2pcdRequest</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">requestedCertificate</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td colspan="2">pduFunctionalType</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.4</td></tr><tr><td rowspan="3">content</td><td rowspan="3">signedData</td><td rowspan="2">signer</td><td colspan="3">digest</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.5</td></tr><tr><td colspan="3">certificate</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.5</td></tr><tr><td style='text-align: center;'>signature</td><td colspan="3">sm2Signature</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>7.4.3.6</td></tr></table>

<div style="text-align: center;">表 47 测试集——消息优先级、隐私保护等的发送要求试验方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">策略类型</td><td rowspan="2">试验项目</td><td colspan="5">试验方法</td></tr><tr><td style='text-align: center;'>启动试验</td><td style='text-align: center;'>时间试验</td><td style='text-align: center;'>位置改变试验</td><td style='text-align: center;'>关键事件试验</td><td style='text-align: center;'>紧急车辆试验</td></tr><tr><td style='text-align: center;'>应用标识填充策略</td><td style='text-align: center;'>AID</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>B-1</td></tr><tr><td style='text-align: center;'>消息优先级策略</td><td style='text-align: center;'>PPPP</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">证书与证书摘要切换策略</td><td style='text-align: center;'>digest</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>certificate</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>假名证书变更策略</td><td style='text-align: center;'>certificate</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标识随机化策略</td><td style='text-align: center;'>Source_Layer-2 ID</td><td style='text-align: center;'>B-1</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-2</td><td style='text-align: center;'>B-3</td><td style='text-align: center;'>—</td></tr><tr><td colspan="7">注1:启动试验为被测车辆启动或者重启时,对被测变量进行验证。注2:时间试验为间隔一定时间(本表中B-1时间试验的时间间隔至少为450ms,B-2时间试验的时间间隔至少为300s),对被测变量进行验证。注3:位置改变试验为GNSS模拟器模拟的位置信息发生一定距离改变后,对被测变量进行验证。注4:关键事件试验为被测车辆关键事件触发后,对被测变量进行验证。注5:紧急车辆试验为被测车辆为紧急车辆时,对被测变量进行验证。</td></tr></table>

#### 9.3.2 试验条件

##### 9.3.2.1 试验对象

试验对象为车辆。

##### 9.3.2.2 仪表要求

V2X PC5 消息解析仪表应将预配置参数设置为 YD/T 3756—2024 表 A.1、表 A.2、表 A.3 及表 A.4 对应的取值。

##### 9.3.2.3 试验环境要求

###### 9.3.2.3.1 试验室试验环境

试验环境为配备了转毂的屏蔽室或暗室(半电波或全电波暗室)，转毂可使被测车辆在试验室内原地运转。试验设备为GNSS模拟器和V2X PC5消息接收仪表。

将 V2X PC5 消息接收仪表和 GNSS 模拟器分别连接到屏蔽室或暗室（半电波或全电波暗室）内的 LTE-V2X 天线端口和 GNSS 天线端口上，见图 8。水平方向上测试天线端口中心距离被测车辆中心 5 m，屏蔽室或暗室 LTE-V2X 天线端口中心高度为被测车辆 LTE-V2X 天线中心高度，见图 9 和图 10。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_392_198_813_574.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">图 8  试验室测试系统连接图</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_395_651_808_1022.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">图 9 试验室测试系统俯视图</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_396_1103_808_1471.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">图 10 试验室测试系统侧视图</div>


###### 9.3.2.3.2 道路试验环境

试验环境为开阔场地，路面平整。试验环境内除了 V2X PC5 消息接收仪表和被测车辆外无其他开启 V2X 功能的车辆或系统。试验环境应能允许被测车辆车速达到 80 km/h，并且有足够的空间允许被测车辆加减速。试验设备为 V2X PC5 消息接收仪表和车辆动态数据采集单元。

开阔场地是指开阔测试环境，用来描述从设备出发能够在遇到最小阻碍的情况下观测到天空。该环境应同时满足以下要求：

a）以被测车辆的 GNSS 天线为中心，在水平面  $ 5^{\circ} $  以上的所有方向内，无外部视野遮挡；

b) 车辆动态数据采集单元所使用的 GNSS 卫星数量: GPS≥6 颗, BDS≥6 颗, GALILEO≥6 颗, GLONASS≥6 颗;

c） 车辆动态数据采集单元从 GNSS 卫星所测得的  $ HDOP \leq 1.5 $ ，同时垂直精度因子  $ VDOP \leq 3 $ 。

在试验道路上由车辆动态数据采集单元采集被测车辆实时运动状态数据时，需确保所采集的数据精度高于7.3.2中规定的各项精度要求，车辆动态数据采集单元的GNSS天线应布置在被测车辆水平面几何中心。

如图 11 所示，将 V2X PC5 消息接收仪表固定于被测车辆内，且可稳定接收被测车辆发送的 BSM 消息。将车辆动态数据采集单元固定在车辆纵向中轴线上，且可稳定采集被测车辆的实时运动状态。

<div style="text-align: center;"><img src="imgs/img_in_image_box_313_702_861_926.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 11 道路试验环境布置图</div>


#### 9.3.3 数据一致性试验

##### 9.3.3.1 道路静态试验

道路静态试验方法如下。

a）将被测车辆驶入试验道路的静态测试区。

b）启动 V2X PC5 消息接收仪表，使其记录测试过程中接收到的第 1 条至最后 1 条 BSM。

c) 使被测车辆以工作模式 3 广播 BSM，有效测试时长不少于 600s；在 t 秒的连续测试时间内，V2X PC5 消息接收仪表接收到 BSM 的数量不低于 round $ (t \times 10 \times 95\%) $ 。测试期间对被测车辆进行必要的测试操作，如换挡、转动方向盘、开启或关闭车灯等。记录测试操作对应的顺序、时间等信息。

d）检验 V2X PC5 消息接收仪表记录的数据是否满足该文件要求。

##### 9.3.3.2 道路动态试验

道路动态试验方法如下。

a）将被测车辆驶入试验道路的动态测试区。

b）启动 V2X PC5 消息接收仪表，使其记录测试过程中收到的第 1 条至最后 1 条 BSM。

c）启动车辆动态数据采集单元，使其采集测试过程中被测车辆的位置、速度、航向角、加速度、横

摆角速度等数据。

d) 使被测车辆以工作模式 4 广播 BSM，有效测试时长不少于 600 s；在 t 秒的连续测试时间内，V2X PC5 消息接收仪表接收到 BSM 的数量不低于 round $ (t \times 10 \times 95\%) $ 。测试期间对被测车辆进行必要的驾驶操作，如使被测车辆行驶到目标车速[包括低速（10 km/h～20 km/h）、中速（20 km/h～50 km/h）、高速（50 km/h～80 km/h）]，使被测车辆转弯、掉头等。

e）对 V2X PC5 消息接收仪表记录的数据元素和车辆动态数据采集单元采集的车辆动态数据时间对齐后做差，检验结果是否满足该文件要求。

##### 9.3.3.3 道路关键事件触发试验

仅测试被测车辆生产厂家声明的关键事件。表 26 中关键事件 Hazard Lights 按照 9.3.3.1 的测试方法进行测试；表 26 中其他关键事件按照被测车辆生产厂家声明的实车运动触发或模拟触发方法进行测试。

a） 若关键事件测试时的触发方法为实车运动触发。

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_616_209_657.jpg" alt="Image" width="3%" /></div>


1）将被测车辆驶入试验道路的动态测试区。

2）启动 V2X PC5 消息接收仪表，使其记录测试过程中收到的第 1 条至最后 1 条 BSM。

3）使被测车辆以工作模式4广播BSM。按照被测车辆生产厂家提供的实车运动触发方法触发表26所列关键事件（如使车辆到达一定车速后急踩刹车触发ABS、轮胎放气触发轮胎欠压报警、车辆碰撞触发安全气囊弹出等），触发状态持续时间不少于5 s。记录关键事件触发时间和触发状态持续时长。

4）检验 V2X PC5 消息接收仪表记录的关键事件触发情况是否满足该文件要求。

b）若关键事件测试时的触发方法为模拟触发。

1）将被测车辆驶入试验道路的静态测试区。

2）启动 V2X PC5 消息接收仪表，使其记录测试过程中收到的第 1 条至最后 1 条 BSM。

3）使被测车辆以工作模式3广播BSM。测试期间按照被测车辆生产厂家提供的模拟触发方法触发表26所列关键事件（如在车辆总线上模拟触发信号或给被测车辆LTE-V2X系统灌输触发信号等），触发状态持续时间不少于5 s。记录关键事件触发时间和触发状态的持续时长。

4）检验 V2X PC5 消息接收仪表记录的关键事件触发情况是否满足该文件要求。

#### 9.3.4 通信安全试验

##### 9.3.4.1 试验室静态试验

试验室静态试验方法为：

a）将被测车辆驶入屏蔽室或暗室(半电波或全电波暗室)测试区域，摆正被测车辆位置并固定在测试区域；

b) 启动 V2X PC5 消息接收仪表，使其记录测试过程中收到的第 1 条至最后 1 条 BSM；

c) 启动 GNSS 模拟器，使其模拟产生预设的 GNSS 固定位置数据；

d）使被测车辆以工作模式3广播BSM，有效测试时长不少于600 s；

e）检验 V2X PC5 消息接收仪表记录的数据是否满足该文件要求。

##### 9.3.4.2 试验室动态试验

试验室动态试验方法如下。

a）将被测车辆驶入屏蔽室或暗室（半电波或全电波暗室）测试区域，使其前后车轮分别停放在两

组转毂上，摆正被测车辆位置并固定在测试区域。

b）启动 V2X PC5 消息接收仪表，使其记录测试过程中收到的第 1 条至最后 1 条 BSM。

c）启动 GNSS 模拟器，使其模拟产生预设的与被测车辆航向角方向一致的轨迹数据。

d）使被测车辆以工作模式4广播BSM，有效测试时长不少于600 s。

e) 语音引导驾驶员驾驶被测车辆，使转毂滚动线速度与 GNSS 轨迹中速度误差在  $ \pm 1  km/h $  以内。测试轨迹包括但不限于：

1）一段确定的直线轨迹，轨迹变化速度为40 km/h（约11.11 m/s，300 s约行驶3.3 km）；

2）一段确定的直线轨迹，轨迹变化速度为20 km/h（约5.6 m/s，300 s约行驶1.68 km）。

f）检验 V2X PC5 消息接收仪表记录的数据是否满足该文件要求。

##### 9.3.4.3 试验室关键事件触发试验

试验室关键事件触发试验方法如下。

a）将被测车辆驶入屏蔽室或暗室（半电波或全电波暗室）测试区域，使其前后车轮分别停放在两组转毂上，摆正被测车辆位置并固定在测试区域。

b）启动 V2X PC5 消息接收仪表，使其记录测试过程中收到的第 1 条至最后 1 条 BSM。

c) 启动 GNSS 模拟器，使其模拟产生预设的与被测车辆航向角方向一致的轨迹数据。测试轨迹包括但不限于：

1）一段确定的直线轨迹，轨迹变化速度为40 km/h（约11.11 m/s，300 s约行驶3.3 km）；

2）一段确定的直线轨迹，轨迹变化速度为20 km/h（约5.6 m/s，300 s约行驶1.68 km）。

d）使被测车辆以工作模式4广播BSM，有效测试时长不少于600 s；

e) 语音引导驾驶员驾驶被测车辆，使转毂滚动线速度与 GNSS 轨迹中速度误差在  $ \pm 1  km/h $  以内；

f) 语音引导驾驶员触发被测车辆生产厂家声明的某个关键事件。距 V2X PC5 消息接收仪表接收到被测车辆广播的第一条 BSM400 s 后，语音提示驾驶员取消触发关键事件。记录关键事件触发时间、触发状态的持续时长及取消时间。

<div style="text-align: center;"><img src="imgs/img_in_image_box_94_981_132_1016.jpg" alt="Image" width="3%" /></div>


g）检验 V2X PC5 消息接收仪表记录的数据是否满足该文件要求。

### 9.4 通信性能试验

#### 9.4.1 发射性能试验

按照 9.4.2.1.1 的试验条件和 YD/T 3848—2021 中 6.2.1.1 进行试验，测试 LTE-V2X 系统最大发射功率，测试点应与 9.4.2.2 中供需双方协商的等效测试点一致。若 DUT 使用一个发射射频口，则测试得出的最大发射功率即为最终结果；若 DUT 使用多个同一通信方式的发射射频口且射频口同时工作，则应将多个射频口的功率数值叠加后作为最终结果。

按照 9.4.2.2 的试验方法测试被测车辆发射天线系统的自由空间远场线性平均增益。

按照公式 $ （1） $ 计算得到被测车辆近水平面辐射功率。

 $$  NHPRP{=}G_{FFave_{-}Tx}+T_{x} $$ 

式中：

NHPRP —— 被测车辆近水平面辐射功率；

 $ G_{FFave\_Tx} $  —— 发射天线系统的自由空间远场线性平均增益；

 $ T_{x} $  ——LTE-V2X系统传导下的最大发射功率。

注：智能 LTE-V2X 天线系统的测试方法由供需双方确定。

#### 9.4.2 接收性能试验

##### 9.4.2.1 LTE-V2X 系统接收灵敏度试验

###### 9.4.2.1.1 试验条件

####### 9.4.2.1.1.1 试验对象

试验对象为 LTE-V2X 系统，LTE-V2X 系统至少应包含无线通信子系统。

####### 9.4.2.1.1.2 通用条件

采用传导方式进行试验，且应满足如下条件：

a） DUT 预留 LTE-V2X 天线和 GNSS 天线接口；

b）通过相关工具[如串口或者 USB(通用串行总线)口]能获取 DUT 的底层信息(如统计收包数等);

c） DUT 支持 GNSS 时钟同步。同时可通过工具或指示灯确定 GNSS 卫星锁定及定位。

####### 9.4.2.1.1.3 试验系统

试验系统由 GNSS 模拟器和 LTE-V2X PC5 射频测试仪表组成，见图 12。GNSS 模拟器应能产生 BDS、GPS、GALILEO、GLONASS 四种制式卫星信号，并能够同时产生多种卫星制式的混合卫星信号（例如 BDS+GPS），且每种卫星制式至少能产生 6 颗卫星信号。LTE-V2X PC5 射频测试仪表用于测试 DUT 的射频指标。

<div style="text-align: center;"><img src="imgs/img_in_image_box_471_841_733_980.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 12 射频性能试验连接图</div>


###### 9.4.2.1.2 试验方法

按照 YD/T 3848—2021 中 6.3.2 进行试验，测试点应与 9.4.2.2 中供需双方协商的等效测试点一致。

若 DUT 使用一个接收射频口，则测试得出的接收灵敏度即为最终结果；若 DUT 使用多个同一通信方式的接收射频口且射频口同时工作，则应将多个射频口的接收灵敏度数值叠加后作为最终结果。

注：智能 LTE-V2X 天线系统的测试方法由供需双方确定。

##### 9.4.2.2 车辆天线增益试验

###### 9.4.2.2.1 试验条件

####### 9.4.2.2.1.1 试验对象

试验对象为车辆。

####### 9.4.2.2.1.2 试验环境条件

试验场地宜采用具备天线测试系统的全电波暗室。也可采用其他场地，但试验结果应排除外界因

素影响。场地性能要求参考附录 H。

天线测试系统应符合如下要求：

——方位角度范围： $ 0^{\circ} $ ~ $ 360^{\circ} $ ；

——方位角度误差：不大于 $ 0.5^{\circ} $ ；

——俯仰角度范围：至少为 $ 0^{\circ} $ ~ $ 96^{\circ} $ ；

——俯仰角度误差：不大于 $ 0.5^{\circ} $ 。

####### 9.4.2.2.1.3 试验布置

方位角  $ \phi $ 、俯仰角  $ \theta $  和天线测试系统中心的定义应符合附录 F。将被测车辆置于转台上，被测车辆车头指向方向与  $ \phi=0^{\circ} $  方位角对齐，被测车辆 LTE-V2X 天线几何中心宜与天线测试系统中心对齐；若天线测试系统包含偏心修正功能，或天线测试系统的测量范围包含整个被测车辆所有被测天线，则允许被测车辆的 LTE-V2X 天线几何中心偏离天线测试系统中心。

在测试之前，需在 DUT 的射频端口处断开 LTE-V2X 天线的连接线束，采用同轴线缆将被测车辆连接线束与测试仪表（例如网络分析仪）连接，被测车辆 LTE-V2X 天线试验布置见图 13。

<div style="text-align: center;"><img src="imgs/img_in_image_box_211_651_942_1027.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 13 被测车辆 LTE-V2X 天线试验布置示意图</div>


如图 14 所示，若 LTE-V2X 天线系统或链路中包括放大器，则需要采取必要的手段（如增加偏置电源、提供唤醒信号等）保证放大器正常工作。

如果被测车辆的 LTE-V2X 天线系统包含一个发射天线，则将该天线各个角度测试值直接作为发射天线测试结果；如果被测车辆的 LTE-V2X 天线系统包含多个同一通信方式的发射或接收天线，则需要分别对各个天线进行测试，分别在各角度处取最大值作为发射天线和接收天线的测试结果。

除被测天线系统外，其他天线接口应适当连接匹配负载阻抗，以确保被测天线端口无射频干扰。

<div style="text-align: center;"><img src="imgs/img_in_image_box_317_1303_851_1466.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 14 LTE-V2X 天线系统示意图</div>


####### 9.4.2.2.1.4 参数配置

测量仪表参数配置见表48。

<div style="text-align: center;">表 48 测量仪表配置参数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>发射天线等效测试点的端口功率</td><td style='text-align: center;'>测试频率</td></tr><tr><td style='text-align: center;'>等效测试点端口功率应设置为可使天线系统正常工作的功率区间</td><td style='text-align: center;'>5 905 MHz, 5 910 MHz, 5 915 MHz, 5 920 MHz, 5 925 MHz</td></tr></table>

###### 9.4.2.2.2 试验方法

测试发射天线增益时，采用供需双方确定的等效测试点。被测车辆 LTE-V2X 天线系统与测试仪表（网络分析仪或信号源）连接作为发射天线；测试天线与测试仪表（网络分析仪或测量用接收机）连接作为接收天线。

测试接收天线增益时，采用供需双方确定的等效测试点。测试天线与测试仪表（网络分析仪或信号源）连接作为发射天线；被测车辆 LTE-V2X 天线系统与测试仪表（网络分析仪或测量用接收机）连接作为接收天线。

具体测试方法如下：

a）设置转台位置为  $ \phi=0^{\circ} $ ，测量天线位置为  $ \theta=0^{\circ} $ ；

b) 按照不同测试频率进行测试，记录水平和垂直极化接收电平幅值及对应相位；

c) 在  $ 0^{\circ} \sim 360^{\circ} $  方位角范围内以最大  $ 1^{\circ} $  间隔进行不同频率测试，记录角度位置和水平、垂直极化接收电平的幅值  $ G_{\mathrm{H}}(\theta, \phi, f) $  (dBi) 和  $ G_{\mathrm{V}}(\theta, \phi, f) $  (dBi) 及相位；

d）在 $ 0^{\circ}\sim96^{\circ} $ 俯仰角范围内以最大 $ 1^{\circ} $ 间隔移动，在每个俯仰位置按照步骤c)进行测试；

e）按公式(2)计算各位置的总增益，对测试结果进行近远场变换，获得远场试验结果；

f) 根据标准天线的场地校准数据，计算获得被测车辆 LTE-V2X 天线系统的远场增益  $  G_{\mathrm{FF}}(\theta, \phi, f)  $  (dBi)，并绘制相应方向图。

注：智能 LTE-V2X 天线系统的测试方法由供需双方确定。

 $$ G_{\mathrm{N F}}(\theta,\phi,f)=10\lg\left[10^{G_{\mathrm{H}}(\theta,\phi,f)}+10^{G_{\mathrm{V}}(\theta,\phi,f)}\right] $$ 

式中：

 $ G_{NF} $ ——近场天线增益；

 $ G_{H} $  ——水平极化接收电平幅值；

 $ G_{v} $  ——垂直极化接收电平幅值；

θ ——俯仰角；

 $ \phi $  ——方位角；

f ——信号频率。

###### 9.4.2.2.3 计算方法

线性平均增益计算方法如下。

a）将对数表示的天线增益 $ G_{\mathrm{FF}}(\theta,\phi,f) $ 转化成线性表示 $ g_{\mathrm{FF}}(\theta,\phi,f) $ ，见公式(3)。

 $$ g_{\mathrm{F F}}(\theta,\phi,f)=10^{G\mathrm{F F}(\theta,\phi,f)/10} $$ 

式中：

 $ g_{FF} $  ——线性天线增益；

θ ——俯仰角；

 $ \phi $  ——方位角；

f ——信号频率；

 $ G_{FF} $ ——对数天线增益。

b) 按照表 33 的角度区域，计算规定区域的天线增益平均值  $ g_{FFa} $ ，见公式(4)；

 $$ g_{_{\mathrm{FFave}}}=\frac{1}{m\times n\times5}\sum_{i=1}^{m}\sum_{j=1}^{n}\sum_{k=1}^{5}g_{_{\mathrm{FF}}}(\theta_{i},\phi_{j},f_{k}) $$ 

式中：

 $ g_{FFave} $  ——天线增益平均值；

m ——规定区域方位角个数；

i ——方位角序号；

n ——规定区域俯仰角个数；

j ——俯仰角序号；

k —— 测试频率序号；

 $ g_{FF} $  ——天线增益。

c）将计算后的平均值转换为对数形式 $ G_{FFave} $ ，见公式（5）。

 $$ G_{\mathrm{FFave}}=10\lg(g_{\mathrm{FFave}}) $$ 

式中：

 $ g_{FFave} $  ——天线增益平均值；

 $ G_{FFave} $  ——对数形式天线增益平均值。

## 附录 A

(资料性)

## LTE-V2X 系统电磁兼容性技术要求及试验方法

### A.1 电磁兼容性技术要求

#### A.1.1 对静电放电产生的电骚扰抗扰

##### A.1.1.1 LTE-V2X 系统不通电

参照 A.2.1.1 进行试验，试验后，LTE-V2X 系统功能宜正常。

##### A.1.1.2 LTE-V2X 系统通电

参照 A.2.1.2 进行试验，LTE-V2X 系统宜满足 5.1 等级 A 的要求。

#### A.1.2 对由传导和耦合引起的电骚扰抗扰

##### A.1.2.1 沿电源线的电瞬态传导抗扰

参照 A.2.2.1 进行试验，抗扰试验等级和试验要求宜满足表 A.1 的规定。

<div style="text-align: center;">表 A.1 沿电源线瞬态传导的抗扰性能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验脉冲</td><td style='text-align: center;'>抗扰试验等级</td><td style='text-align: center;'>试验要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>Ⅲ</td><td style='text-align: center;'>试验后，LTE-V2X系统功能正常</td></tr><tr><td style='text-align: center;'>2a</td><td style='text-align: center;'>Ⅲ</td><td style='text-align: center;'>试验中和试验后，LTE-V2X系统功能正常</td></tr><tr><td style='text-align: center;'>2b</td><td style='text-align: center;'>Ⅲ</td><td style='text-align: center;'>试验后，LTE-V2X系统功能正常</td></tr><tr><td style='text-align: center;'>3a/3b</td><td style='text-align: center;'>Ⅲ</td><td style='text-align: center;'>试验中和试验后，LTE-V2X系统功能正常</td></tr><tr><td colspan="3">注：抗扰试验等级定义见GB/T21437.2—2021的附录A。</td></tr></table>

##### A.1.2.2 除电源线外的导线通过容性和感性耦合的电瞬态抗扰

参照 A.2.2.2 进行试验，LTE-V2X 系统宜满足 5.1 等级 A 的要求。

#### A.1.3 对电磁辐射的抗扰

参照 A.2.3 进行试验，LTE-V2X 系统宜满足 5.1 等级 A 的要求。

#### A.1.4 无线电骚扰特性

##### A.1.4.1 传导发射

参照 A.2.4.1 进行试验，LTE-V2X 系统宜符合 GB/T 18655—2018 中表 5 和表 6 等级 3 的要求。

##### A.1.4.2 辐射发射

参照 A.2.4.2 进行试验，LTE-V2X 系统宜符合 GB/T 18655—2018 中表 7 等级 3 的要求。

### A.2 电磁兼容性试验

#### A.2.1 对静电放电产生的电骚扰抗扰试验

##### A.2.1.1 LTE-V2X 系统不通电

LTE-V2X系统以表1中工作模式1，按照GB/T19951—2019附录C中表C.1、表C.2的类别1试验严酷等级不低于 $ L_{3} $ 的测试电压要求和第9章规定的方法进行试验。试验后以表1中工作模式2进行测试。

##### A.2.1.2 LTE-V2X 系统通电

LTE-V2X 系统以表 1 中工作模式 2，按照 GB/T 19951—2019 附录 C 中表 C.1、表 C.2、表 C.3 的类别 1 试验严酷等级不低于  $ L_{3} $  的测试电压要求和第 8 章规定的方法进行试验。

#### A.2.2 对由传导和耦合引起的电骚扰抗扰试验

##### A.2.2.1 沿电源线的电瞬态传导抗扰

LTE-V2X系统以表1中工作模式2，按照表A.1规定的抗扰试验等级和GB/T21437.2—2021中的方法，在电源线以及可能连接到电源线的其他连接线上施加脉冲1，2a，2b，3a，3b进行试验。

##### A.2.2.2 除电源线外的导线通过容性和感性耦合的电瞬态抗扰

LTE-V2X 系统以表 1 中工作模式 2，按照 GB/T 21437.3—2021 中表 B.1、表 B.2 中等级Ⅲ的要求和 4.5、4.7 的方法进行试验。

#### A.2.3 对电磁辐射的抗扰试验

LTE-V2X 系统以表 1 中工作模式 2，按照 GB 34660—2017 中 4.7 的电波暗室法、大电流注入法的抗扰试验强度和 5.7 的方法进行试验。

#### A.2.4 无线电骚扰特性试验

##### A.2.4.1 传导发射

LTE-V2X 系统以表 1 中工作模式 2，按照 GB/T 18655—2018 中 6.3 和 6.4 的方法进行试验。

##### A.2.4.2 辐射发射

LTE-V2X 系统以表 1 中工作模式 2，按照 GB/T 18655—2018 中 6.5 的方法进行试验。

## 附录 B

(资料性)

## 关键事件触发 BSM 消息发送

图 B.1 给出了关键事件触发 BSM 代替原常规 BSM 发送的示例。LTE-V2X 系统在  $ t = 30 \, ms $  时发送第一个常规 BSM，并计划在  $ t = 130 \, ms $  时发送下一个常规 BSM。当 LTE-V2X 系统发送完第一个常规 BSM 后，车辆触发了紧急制动关键事件，此时 LTE-V2X 系统在  $ t = 70 \, ms $  时发送一个携带 eventHardBraking 标志位的关键事件触发 BSM。此后，LTE-V2X 系统取消发送  $ t = 130 \, ms $  的常规 BSM，按照  $ 100 \, ms $  的间隔在  $ t = 170 \, ms, t = 270 \, ms $  等时刻发送关键事件触发 BSM。

☐ 常规BSM ☑ 关键事件触发BSM ✗ 取消BSM发送

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_608_979_717.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">图 B.1 关键事件触发 BSM 替代原常规 BSM 发送时刻示意图</div>


图 B.2 给出了新关键事件触发 BSM 替代原关键事件触发 BSM 发送的示例。LTE-V2X 系统在  $ t = 30 \, ms $  时刻发送第一个关键事件触发 BSM 用以指示车辆发生紧急制动，并将  $ t = 130 \, ms $  时刻设置为下一个关键事件触发 BSM 的发送时刻，但在发送完第一个关键事件触发 BSM 后车辆发生爆胎，LTE-V2X 系统针对这个新增事件立刻生成一个新的关键事件触发 BSM 并取消原计划在  $ t = 130 \, ms $  时刻发送的原关键事件触发 BSM。在新的关键事件触发 BSM 中同时包含 eventHardBraking 和 eventFlatTire 两个数据用于指示车辆发生紧急制动和爆胎事件。假定该关键事件触发 BSM 在  $ t = 70 \, ms $  时刻发送，则 LTE-V2X 系统后续会按照  $ 100 \, ms $  的间隔在  $ t = 170 \, ms, t = 270 \, ms $  等时刻发送后续关键事件触发 BSM。

☐ 原关键事件触发BSM ☐ 新关键事件触发BSM ✗ 取消BSM发送

<div style="text-align: center;"><img src="imgs/img_in_chart_box_186_1106_970_1213.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 B.2 新关键事件触发 BSM 替代原关键事件触发 BSM 发送时刻示意图</div>


## 附录 C

(资料性)

## 拥塞控制机制

### C.1 概述

对于常规 BSM 消息的拥塞控制，可以采用 C.2 或 C.3 方式中的任一种方式。

### C.2 基于 CBR 的拥塞控制

对于使用 CBR 值进行拥塞控制的方式，在执行拥塞控制的时间段内，应用层根据底层递交的 CBR 值及表 C.1 调整常规 BSM 消息的生成周期。

当常规 BSM 消息的生成周期参照表 C.1 规则发生变化时，至少维持当前消息生成周期生成 10 次消息。

<div style="text-align: center;">表 C.1 应用层拥塞控制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="3">CBR范围</td><td colspan="4">车速范围</td></tr><tr><td style='text-align: center;'>0 km/h～5 km/h</td><td style='text-align: center;'>5 km/h～10 km/h</td><td style='text-align: center;'>10 km/h～25 km/h</td><td style='text-align: center;'>&gt;25 km/h</td></tr><tr><td colspan="4">BSM消息生成周期</td></tr><tr><td style='text-align: center;'>0≤CBR≤0.3</td><td style='text-align: center;'>100 ms</td><td style='text-align: center;'>100 ms</td><td style='text-align: center;'>100 ms</td><td style='text-align: center;'>100 ms</td></tr><tr><td style='text-align: center;'>0.3&lt;CBR&gt;0.6</td><td style='text-align: center;'>100 ms</td><td style='text-align: center;'>100 ms</td><td style='text-align: center;'>100 ms</td><td style='text-align: center;'>100 ms</td></tr><tr><td style='text-align: center;'>0.6&lt;CBR&gt;0.8</td><td style='text-align: center;'>1 000 ms</td><td style='text-align: center;'>500 ms</td><td style='text-align: center;'>200 ms</td><td style='text-align: center;'>100 ms</td></tr><tr><td style='text-align: center;'>0.8&lt;CBR&gt;1</td><td style='text-align: center;'>1 000 ms</td><td style='text-align: center;'>500 ms</td><td style='text-align: center;'>400 ms</td><td style='text-align: center;'>100 ms</td></tr></table>

### C.3 基于车辆密度的拥塞控制

#### C.3.1 概述

用于 PER 计算的子区间 vPERSubInterval（1 000 ms）、用于 PER 计算的区间 vPERInterval（5 000 ms）和拥塞控制计算间隔 vTxRateCntrlInt（100 ms）之间的关系如图 C.1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_320_1170_851_1374.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 C.1 参数 vPERSubInterval, vPERInterval 和 vTxRateCntrlInt 之间的关系</div>


#### C.3.2 消息生成周期

基于车辆密度进行拥塞控制，采用如下步骤进行常规 BSM 生成周期控制。

LTE-V2X 系统按照 C.3.2 定义的周期生成常规 BSM。LTE-V2X 系统使用公式(C.1)对 vPER-Range(100 m)范围内车辆的数目 N(k)进行平滑计算：

 $$ N_{\mathrm{s}}(k)=\lambda\times N(k)+(1-\lambda)\times N_{\mathrm{s}}(k-1) $$ 

式中：

 $ N(k) $  ——在第 k 个 vTxRateCntrlInt(100 ms)间隔的最后，主车计算的在 vPERRange(100 m)范围内的远车总数量（按照 BSM 内的 id 标示区分远车）；即在第 k 个 vTxRateCntrlInt(100 ms)间隔结束时刻之前的 vPERSublInterval 间隔内，按照接收到的远车最后一个 BSM 内包括的 2D 位置信息计算，所有位于主车最近获取的 2D 位置信息 vPERRange(100 m)范围内的远车数量；

 $ \lambda $ ——平滑加权因子 vDensityWeightFactor(0.05);

 $ N_{s}(k) $ ——当前平滑后的车辆密度。

LTE-V2X 系统使用公式(C.2)计算常规 BSM 消息生成周期  $ Max\_ITT(k) $ :

 $$ Max_{-}ITT(k)=\left\{\begin{aligned}&100&N_{s}(k)\leqslant B\\ &round\left[100\times\frac{N_{s}(k)}{B}\right]&B<N_{s}(k)<\frac{vMax_{-}ITT}{100}\times B\\ &vMax_{-}ITT&\frac{vMax_{-}ITT}{100}\times B\leqslant N_{s}(k)\end{aligned}\right. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_94_682_132_718.jpg" alt="Image" width="3%" /></div>


式中：

round()——对 100 ms 取整，其输出结果为 100 ms 的整数倍，取整方法宜采用四舍五入，以得到最接近的周期值；

 $ Max\_ITT(k) $  ——消息生成间隔，单位为 ms；

B ——密度系数 vDensityCoefficient(25);

 $ v_{Max\_ITT} $  ——上述计算中的最大门限(600 ms)。

LTE-V2X 系统调度下一个生成常规 BSM 的时间使用公式(C.3)。

 $$ NextScheduledMsgTime=LastTxTime+Max\_{I}TT $$ 

式中：

LastTxTime——上次 BSM 生成的时间。

#### C.3.3 跟踪误差

在 C.3.2 周期生成常规 BSM 的基础上，如果车辆位置发生较大变化，则需要考虑将常规 BSM 生成的时间提前，从而将主车的实时位置告知其他交通参与方。在第 k 个 vTxRateCntrlInt（100 ms）结束时，LTE-V2X 系统使用公式（C.4）计算发送概率  $ p(k) $ 。

 $$ p\left(k\right)=\left\{\begin{aligned}&1-\exp(-\alpha\times\left|e\left(k\right)-T\right|^{2})&&T\leqslant e\left(k\right)<S\\ &1&&e\left(k\right)\geqslant S\\ &0&& 否则 \end{aligned}\right. $$ 

式中：

T ——通信导致的最小跟踪误差(tracking error)门限 vTrackingErrMin（0.2 m）；

α ——误差灵敏度 vErrSensitivity(75);

S ——通信导致的跟踪误差饱和上限 vTrackingErrMax(0.5 m);

 $ e(k) $  ——跟踪误差，是由于远车接收主车的运动状态数据时，传输时延和数据包丢失造成的时延所导致的，该误差不同于车载定位子系统的定位精确度误差，可通过如下方法计算得到。在第 k 个 vTxRateCntrlInt 结束时，LTE-V2X 系统依次进行如下操作。

a） 本车进行自身位置估计(HV Local Estimate)。

假设 T 时刻是最近一次主车获知自身位置信息的时刻， $ T' $  时刻为当前时刻。如果  $ T' - T < vHVLocalPosEstIntMin(50\ ms) $ ，则估计出来的新的位置（New_Latitude_Local，New_Lon-

gitude_Local)即为最近一次本车获知的位置信息，无需做估计；如果 $ T^{\prime}-T>vHVLocalPos-EstIntMax(150\ ms) $ ，则认为主车的位置信息在其他交通参与方侧已长时间未更新， $ e(k)=0 $ ；如果 $ HVPosEstIntMin<T^{\prime}-T<HVPosEstIntMax $ ，则计算在 $ T^{\prime}-T $ 时间间隔内车辆朝向不变时，其往前移动的距离D，然后依据移动距离D通过平面坐标系到地球经纬度坐标系的转换得到估计出来的新的车辆位置（New_Latitude_Local，New_Longitude_Local）。

b) 主车进行远车在其他车辆的位置信息估计(HV Remote Estimate)。

其方法与主车进行自身位置估计一致，区别在于 T 时刻主车的位置信息在其他车辆处的状态是依据信道质量和主车最近一次发送的 BSM 包含的位置信息估计出来的。类似的， $ T^{\prime} $  时刻为当前时刻。如果  $ T^{\prime}-T<v_{HVRemotePosEstIntMin}(50\ ms) $ ，则估计出来的新的位置  $ (\mathrm{New\_Latitude\_Remote}, \mathrm{New\_Longitude\_Remote}) $  即为主车的位置信息在其他车辆处依据信道质量和主车最近一次发送的 BSM 包含的位置信息估计出来的最新信息，无需做额外的位置估计；如果  $ T^{\prime}-T>v_{HVRemotePosEstIntMax}(3000\ ms) $ ，则认为本车的位置信息在其他车辆处已经很长时间没有更新， $ e(k)=0 $ ；如果  $ v_{HVRemotePosEstIntMin}<T^{\prime}-T<v_{HVRemotePosEstIntMax} $ ，则计算在  $ T^{\prime}-T $  时间间隔内车辆朝向不变时，其往前移动的距离 D，然后依据移动距离 D 通过平面坐标系到地球经纬度坐标系的转换得到估计出来的新的车辆位置  $ (\mathrm{New\_Latitude\_Remote}, \mathrm{New\_Longitude\_Remote}) $ 。

c) 计算跟踪误差  $ e(k) $ ，方法为求步骤 a) 中计算出的 HV Local Estimate 和步骤 b) 中 HV Remote Estimate 之间的 2D 距离，如图 C.2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_339_748_833_1178.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 C.2 车辆朝前移动距离</div>


d）在第 k 个 vTxRateCntrlInt 结束时，LTE-V2X 系统使用跟踪误差  $ e(k) $ ，使用公式(C.4)计算由于跟踪误差导致生成 BSM 的概率  $ p(k) $ 。

注：公式(C.4)的设计原则是，当跟踪误差未超过门限 T 时，主车不会因为跟踪误差广播 BSM；当跟踪误差超过此门限时，则跟踪误差越大，发送概率越大，当跟踪误差超过门限 S 时，则会因为跟踪误差导致发送 BSM。因为主车的跟踪误差各不相同，它们会以不同的概率广播 BSM。

基于 Vehicle Dynamics 的发送（也就是基于上述跟踪误差），通过伯努利试验 rand() 取一个在 0 到 1 之间均匀分布的随机数，如果通过伯努利试验为真且下次调度 BSM 的时间大于或等于 vRescheduleTh(25 ms)，调度 BSM 生成，同时取消已有的 BSM 生成调度，分配 LastTxTime = CurrentTime。

e）信道质量估计。

 $ w_{k} $ ——第 k 个 vPERSubInterval。

需已知整体的信道状况，然后依据信道平均质量来估计主车发送的信息在其他车辆处被正确接收的概率，从而可估计在特定时刻其他车辆处主车的位置信息状态（是最新消息，还是若干次之前发送的信息）。平均信道质量指示（ $ \Pi $ ）可通过如下方法得到。

在第 k 个 vPERSubInterval（1 s）结束时刻计算 PER（误包率，在一对主车和远车之间进行计算）。

——LTE-V2X 系统采用如下计算方法，vPERInterval 内采用滑动窗计算第 k 个 vPERSubinterval 时刻的 PER。

在每个  $ \omega_{k} $  结束时，针对每个远车，按照公式(C.5)计算在  $ \delta_{k} $  间隔内预期接收到的 BSM 数量以及未接收到的 BSM 数量，其示意图如图 C.3 所示。

 $$ PER_{i}\left(k\right)=\frac{ 在 \left[\omega_{k-n+1},\omega_{k}\right] 期间 , 从 RV_{i} 未收到的 BSM 消息数量 }{ 在 \left[\omega_{k-n+1},\omega_{k}\right] 期间 , 从 RV_{i} 预期接收到的 BSM 消息总数 } $$ 

式中：

i ——第 i 辆远车；

k ——第 k 个 vPERSubInterval(1 s);

n ——在  $ \delta_{k} $  内子间隔的个数， $ \delta_{k} $  的长度是  $ w_{k} $  的 n 倍；

 $ w_{k} $  ——第 k 个 vPERSubInterval(1 s) 时间段。

 $$ \delta_{k+1} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_713_1050_857.jpg" alt="Image" width="75%" /></div>


标引序号说明：

 $ \delta_{k} $ ——第 k 个 vPERInterval(5 s);

<div style="text-align: center;">图 C.3 滑动计算窗</div>


在  $ \delta_{k} $  内对每辆接收到两个或多个 BSM 的远车，采用 BSM 中的 DE_MsgCount 数据单元计算 PER，其中预期接收到的 BSM 数量为在  $ \delta_{k} $  内接收到的最后一个 BSM 和第一个 BSM 中的 DE_MsgCount 之差加 1；而未接收到 BSM 数量为：在  $ \delta_{k} $  内预期接收到的 BSM 数量与实际接收到的消息数量之差。当计算特定远车预期和未接收到的 BSM 数量时，需要考虑 DE_MsgCount 数据单元达到最大值后会归零的特性。如果在  $ \delta_{k} $  间隔内，某个远车只接收到了一个数据包，不用于在  $ \delta_{k} $  间隔内计算这个远车的 PER。

——信道质量指示( $ \Pi $ ): 在  $ \omega_{k} $  间隔最后计算  $ \Pi(k) $ ，其为在 vPERRange(100 m) 内所有远车的 PER(k) 的平均值，并且满足公式(C.6) 的限制。

 $$ \begin{aligned}&If(\Pi(k)>v PERMax)\\&\Pi(k)=v PERMax\\ \end{aligned} $$ 

基于信道质量指示  $ \Pi(k) $ ，在每次主车发送 BSM 之后，均估计该消息是否被其他车辆接收到。对  $ \Pi(k) $  进行伯努利试验，如果试验的结果为真，则认为主车发送的 BSM 被其他远车正确接收到，主车采用本次 BSM 里面的位置信息更新其在其他车辆处的位置状态；否则，则认为消息未被其他车辆收到，主车不更新其位置在其他车辆处的状态。如果连续 vMaxSuccessiveFail(3) 次试验均为假，则认为其他车辆接收到最新的 BSM。

## 附录 D

(规范性)

车辆基本类型及编号

表 D.1 规定了车辆的基本类型及编号。表 D.1 载货汽车中，货车列车和半挂汽车列车，应按牵引车和挂车合并确定车辆类型。

<div style="text-align: center;">表 D.1 车辆基本类型及编号</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>车辆类型</td><td style='text-align: center;'>类型定义</td><td style='text-align: center;'>引用标准</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>未知车辆类型</td><td style='text-align: center;'>未知车辆类型</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>1～8</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>载客汽车,具体类型未知</td><td style='text-align: center;'>载客汽车,具体类型未知</td><td style='text-align: center;'>GB 7258—2017的3.2.1</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>载客汽车,一类客车</td><td style='text-align: center;'>载客汽车:车长小于6m且核定载人数不大于9人</td><td style='text-align: center;'>JT/T 489—2019的4.2.3中一类客车</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>载客汽车,二类客车</td><td style='text-align: center;'>载客汽车:车长小于6m且核定载人数为10人～19人,包括乘用车列车</td><td style='text-align: center;'>JT/T 489—2019的4.2.3中二类客车</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>载客汽车,三类客车</td><td style='text-align: center;'>载客汽车:车长不小于6m且核定载人数不大于39人</td><td style='text-align: center;'>JT/T 489—2019的4.2.3中三类客车</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>载客汽车,四类客车</td><td style='text-align: center;'>载客汽车:车长不小于6m且核定载人数不小于40人</td><td style='text-align: center;'>JT/T 489—2019的4.2.3中四类客车</td></tr><tr><td style='text-align: center;'>14～19</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>载货汽车,具体类型未知</td><td style='text-align: center;'>载货汽车,具体类型未知</td><td style='text-align: center;'>GB 7258—2017的3.2.2</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>载货汽车,小型货车</td><td style='text-align: center;'>载货汽车:车长小于6m,2轴</td><td style='text-align: center;'>JT/T 1008.1—2015的附录A中小型货车</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>载货汽车,中型货车</td><td style='text-align: center;'>载货汽车:车长大于或等于6m小于或等于12m,2轴</td><td style='text-align: center;'>JT/T 1008.1—2015的附录A中中型货车</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>载货汽车,大型货车</td><td style='text-align: center;'>载货汽车:车长大于或等于6m小于或等于12m,3轴或4轴</td><td style='text-align: center;'>JT/T 1008.1—2015的附录A中大型货车</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>载货汽车,特大型货车</td><td style='text-align: center;'>载货汽车:车长大于12m,或4轴以上,且车高小于3.8m或大于4.2m</td><td style='text-align: center;'>JT/T 1008.1—2015的附录A中特大型货车</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>载货汽车,集装箱车</td><td style='text-align: center;'>载货汽车:车长大于12m,或4轴以上,且车高大于或等于3.8m小于或等于4.2m</td><td style='text-align: center;'>JT/T 1008.1—2015的附录A中集装箱车</td></tr><tr><td style='text-align: center;'>26～29</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>载货汽车(运载危险货物),具体类型未知</td><td style='text-align: center;'>载货汽车(运载危险货物),具体类型未知</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>载货汽车(运载危险货物),第1类</td><td style='text-align: center;'>载货汽车:危险货物第1类:爆炸性物质和物品</td><td style='text-align: center;'>JT/T 617.2—2018的4.1.1中第1类</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>载货汽车(运载危险货物),第2类</td><td style='text-align: center;'>载货汽车:危险货物第2类:气体</td><td style='text-align: center;'>JT/T 617.2—2018的4.1.1中第2类</td></tr></table>

<div style="text-align: center;">表 D.1 车辆基本类型及编号（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>车辆类型</td><td style='text-align: center;'>类型定义</td><td style='text-align: center;'>引用标准</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>载货汽车(运载危险货物),第3类</td><td style='text-align: center;'>载货汽车:危险货物第3类:易燃液体</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第3类</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>载货汽车(运载危险货物),第4类</td><td style='text-align: center;'>载货汽车:危险货物第4类:易燃固体、易于自燃的物质、遇水放出易燃气体的物质</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第4类</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>载货汽车(运载危险货物),第5类</td><td style='text-align: center;'>载货汽车:危险货物第5类:氧化性物质和有机过氧化物</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第5类</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>载货汽车(运载危险货物),第6类</td><td style='text-align: center;'>载货汽车:危险货物第6类:毒性物质和感染性物质</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第6类</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>载货汽车(运载危险货物),第7类</td><td style='text-align: center;'>载货汽车:危险货物第7类:放射性物质</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第7类</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>载货汽车(运载危险货物),第8类</td><td style='text-align: center;'>载货汽车:危险货物第8类:腐蚀性物质</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第8类</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>载货汽车(运载危险货物),第9类</td><td style='text-align: center;'>载货汽车:危险货物第9类:杂项危险物质和物品,包括危害环境物质</td><td style='text-align: center;'>JT/T617.2-2018的4.1.1中第9类</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>专项作业车,具体类型未知</td><td style='text-align: center;'>专项作业车,具体类型未知</td><td style='text-align: center;'>GB7258-2017的3.2.3</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>专项作业车,一类专项作业车</td><td style='text-align: center;'>专项作业车:总轴数为2,车长小于6m且最大允许总质量小于4500kg</td><td style='text-align: center;'>JT/T489-2019的4.4.2中一类专项作业车</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>专项作业车,二类专项作业车</td><td style='text-align: center;'>专项作业车:总轴数为2,车长不小于6m且最大允许总质量不小于4500kg</td><td style='text-align: center;'>JT/T489-2019的4.4.2中二类专项作业车</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>专项作业车,三类专项作业车</td><td style='text-align: center;'>专项作业车:总轴数为3</td><td style='text-align: center;'>JT/T489-2019的4.4.2中三类专项作业车</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>专项作业车,四类专项作业车</td><td style='text-align: center;'>专项作业车:总轴数为4</td><td style='text-align: center;'>JT/T489-2019的4.4.2中四类专项作业车</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>专项作业车,五类专项作业车</td><td style='text-align: center;'>专项作业车:总轴数为5</td><td style='text-align: center;'>JT/T489-2019的4.4.2中五类专项作业车</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>专项作业车,六类专项作业车</td><td style='text-align: center;'>专项作业车:总轴数大于或等于6</td><td style='text-align: center;'>JT/T489-2019的4.4.2中六类专项作业车</td></tr><tr><td style='text-align: center;'>47～49</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>校车,具体类型未知</td><td style='text-align: center;'>校车,具体类型未知</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>幼儿校车</td><td style='text-align: center;'>用于有组织地接送3周岁以上学龄前幼儿上下学的7座及7座以上的载客汽车</td><td style='text-align: center;'>GA802-2019的6.2中幼儿校车</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>小学生校车</td><td style='text-align: center;'>用于有组织地接送小学生上下学的7座及7座以上的载客汽车</td><td style='text-align: center;'>GA802-2019的6.2中小学生校车</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>中小学生校车</td><td style='text-align: center;'>用于有组织地接送义务教育阶段学生(小学生和初中生)上下学的7座及7座以上的载客汽车</td><td style='text-align: center;'>GA802-2019的6.2中中小学生校车</td></tr></table>

<div style="text-align: center;">表 D.1 车辆基本类型及编号（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>车辆类型</td><td style='text-align: center;'>类型定义</td><td style='text-align: center;'>引用标准</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>初中生校车</td><td style='text-align: center;'>用于有组织地接送初中生上下学的7座及7座以上的载客汽车</td><td style='text-align: center;'>GA 802-2019 的 6.2 中初中生校车</td></tr><tr><td style='text-align: center;'>55～59</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>60</td><td style='text-align: center;'>紧急车辆,具体类型未知</td><td style='text-align: center;'>紧急车辆,具体类型未知</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>警用车</td><td style='text-align: center;'>公安机关、国家安全机关、司法行政系统(包括监狱、戒毒管理机关和司法局)和人民法院、人民检察院用于执行紧急职务的机动车</td><td style='text-align: center;'>GA 802-2019 的 6.2 中警用车</td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>消防车</td><td style='text-align: center;'>用于灭火的专用机动车和现场指挥机动车</td><td style='text-align: center;'>GA 802-2019 的 6.2 中消防车</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>救护车</td><td style='text-align: center;'>急救、医疗机构和卫生防疫等部门用于抢救危重病人或处理紧急疫情的专用机动车</td><td style='text-align: center;'>GA 802-2019 的 6.2 中救护车</td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>工程抢险车</td><td style='text-align: center;'>防汛、水利、电力、矿山、城建、交通、铁道等部门用于抢修公用设施、抢救人民生命财产的专用机动车和现场指挥机动车</td><td style='text-align: center;'>GA 802-2019 的 6.2 中工程抢险车</td></tr><tr><td style='text-align: center;'>65～69</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>70</td><td style='text-align: center;'>公共汽电车,具体类型未知</td><td style='text-align: center;'>公共汽电车,具体类型未知</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>71</td><td style='text-align: center;'>公共汽电车,级别1</td><td style='text-align: center;'>公共汽电车:车长≤5 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别1</td></tr><tr><td style='text-align: center;'>72</td><td style='text-align: center;'>公共汽电车,级别2</td><td style='text-align: center;'>公共汽电车:5 m&lt;车长≤7 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别2</td></tr><tr><td style='text-align: center;'>73</td><td style='text-align: center;'>公共汽电车,级别3</td><td style='text-align: center;'>公共汽电车:7 m&lt;车长≤10 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别3</td></tr><tr><td style='text-align: center;'>74</td><td style='text-align: center;'>公共汽电车,级别4</td><td style='text-align: center;'>公共汽电车:10 m&lt;车长≤13 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别4</td></tr><tr><td style='text-align: center;'>75</td><td style='text-align: center;'>公共汽电车,级别5</td><td style='text-align: center;'>公共汽电车:13 m&lt;车长≤16 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别5</td></tr><tr><td style='text-align: center;'>76</td><td style='text-align: center;'>公共汽电车,级别6</td><td style='text-align: center;'>公共汽电车:16 m&lt;车长≤18 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别6</td></tr><tr><td style='text-align: center;'>77</td><td style='text-align: center;'>公共汽电车,级别7</td><td style='text-align: center;'>公共汽电车:车长&gt;18 m</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别7</td></tr><tr><td style='text-align: center;'>78</td><td style='text-align: center;'>公共汽电车,级别8</td><td style='text-align: center;'>公共汽电车:双层车</td><td style='text-align: center;'>JT/T 1373.2-2021 的 5.1.34 级别8</td></tr><tr><td style='text-align: center;'>79～255</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

附录 E

(资料性)

车辆历史轨迹与预测路线参考设计

### E.1 车辆历史轨迹参考设计

PH 使用一系列简洁的数据来表征主车的真实路径。简洁的数据本质是真实数据的采样子集。如图 E.1 所示，三角形的路径点表示采样之后的简洁路径点，连接连续两点的弦表示车辆真实路径的近似。

简洁数据点采样的原则是真实路径点到两端两个简洁表征点组成的弦之间的垂直距离不超过PH ActualError(1 m)，如图 E.1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_204_581_1013_1409.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 E.1 简洁路径和真实路径表述</div>


### E.2 车辆预测路线参考设计

当路径预估中出现不准确的情况时，需有一种方法来区分并将动态情况告知其他车辆。通过在差分并经过滤的横摆角速度信号之间插入置信度信息来鉴别稳定状态，置信度查找见表 E.1。当车辆横摆角速度在短时间内发生很大变化时，置信度指示器将会发出低置信度报告。这些状态可能包含以下一种或多种：

——变换车道；

——弯曲道路的出入点；

——弯曲道路过渡点；

——避障以及其他高动态驾驶情况。

<div style="text-align: center;">表 E.1 置信度查找表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>输入:过滤差分横 摆角速度[(°)/s²]</td><td style='text-align: center;'>≥25</td><td style='text-align: center;'>[20,25)</td><td style='text-align: center;'>[15,20)</td><td style='text-align: center;'>[10,15)</td><td style='text-align: center;'>[5,10)</td><td style='text-align: center;'>[2.5,5)</td><td style='text-align: center;'>[2,2.5)</td><td style='text-align: center;'>[1.5,2)</td><td style='text-align: center;'>[1,1.5)</td><td style='text-align: center;'>[0.5,1)</td><td style='text-align: center;'>[0,0.5)</td></tr><tr><td style='text-align: center;'>输出:置信度/%</td><td style='text-align: center;'>0</td><td style='text-align: center;'>10</td><td style='text-align: center;'>20</td><td style='text-align: center;'>30</td><td style='text-align: center;'>40</td><td style='text-align: center;'>50</td><td style='text-align: center;'>60</td><td style='text-align: center;'>70</td><td style='text-align: center;'>80</td><td style='text-align: center;'>90</td><td style='text-align: center;'>100</td></tr></table>

# 附录 F

(规范性)

车辆方位区域划分

### F.1 三维球坐标系

三维球坐标系见图 F.1，俯仰角  $ \theta $  和方位角  $ \phi $  的数值表示矢量在球面的角向位置。三维球坐标系原点 A 在 xy 平面的投影点与转台中心重合，在 yz 平面的投影点与测量探头扫描轨迹的中心重合。 $ \theta=0^{\circ} $  为测量探头最高点方向， $ \phi=0^{\circ} $  为被测车辆正前方方向。

<div style="text-align: center;"><img src="imgs/img_in_image_box_376_521_826_896.jpg" alt="Image" width="37%" /></div>


标引序号说明：

l ——参数矢量；

θ——矢量与 $ +\varepsilon $ 轴之间的夹角；

 $ \phi $ ——矢量在 xy 平面上的投影与 +x 轴之间的夹角；

A——三维坐标系原点。

<div style="text-align: center;">图 F.1 三维球坐标系</div>


### F.2 被测车辆天线坐标位置

车辆天线与测试坐标系位置关系示意图见图 F.2， $ \theta=0^{\circ} $  表示车辆的正上方， $ \phi=0^{\circ} $  表示车辆的正前方，A 点为车辆天线的几何中心。

<div style="text-align: center;"><img src="imgs/img_in_image_box_229_203_1032_546.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 F.2 车辆天线与测试坐标系位置关系示意图</div>


### F.3 车辆方位区域

车辆前侧、后侧、左侧和右侧的方位角范围见图 F.3，方位角的原点为车辆通信天线的几何中心。

<div style="text-align: center;"><img src="imgs/img_in_image_box_295_719_884_1106.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 F.3 车辆角度示意图</div>


## 附录 G

(资料性)

耐久性试验

### G.1 耐久性试验方法

本试验用于较快速地验证 DUT 的寿命是否满足要求。试验时，DUT 工作模式为表 1 中工作模式 2。试验期间按照试验持续时间的 25%、50%、75% 以表 1 中工作模式 2 进行检查。试验后，静置至少 1 h 恢复常温，以表 1 中工作模式 2 进行功能验证试验。温度曲线如图 G.1 所示。最高、最低试验温度分别为  $ T_{max} $ 、 $ T_{min} $ 。温度梯度为  $ 4^{\circ}C/min $ 。DUT 在达到最高、最低工作温度时需要保持的时间为 10 min。试验循环次数及时间按照 G.2 描述进行计算。

<div style="text-align: center;"><img src="imgs/img_in_image_box_335_605_863_971.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 G.1 耐久寿命试验温度曲线</div>


### G.2 耐久性试验计算模型

#### G.2.1 在汽车上安装位置的典型温度模型

##### G.2.1.1 在汽车安装位置的平均温升

DUT 在汽车上不同安装位置的平均温升见表 G.1。

<div style="text-align: center;">表 G.1 不同安装位置的温度模型和平均温升</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>汽车上的安装位置</td><td style='text-align: center;'>位置温度模型</td><td style='text-align: center;'>位置平均温升( $ \Delta T $ )</td></tr><tr><td style='text-align: center;'>无特殊要求</td><td style='text-align: center;'>1</td><td style='text-align: center;'>36 K</td></tr><tr><td style='text-align: center;'>乘客舱太阳直射处</td><td style='text-align: center;'>2</td><td style='text-align: center;'>46 K</td></tr></table>

##### G.2.1.2 在不同温区的占比

DUT 的位置温度模型 1 见表 G.2，位置温度模型 2 见表 G.3。

<div style="text-align: center;">表 G.2 位置温度模型 1</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>温度( $ T.i $ )℃</td><td style='text-align: center;'>温度占比( $ P_i $ )%</td></tr><tr><td style='text-align: center;'>-40</td><td style='text-align: center;'>6</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>20</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>65</td></tr><tr><td style='text-align: center;'>80</td><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>85</td><td style='text-align: center;'>1</td></tr></table>

<div style="text-align: center;">表 G.3 位置温度模型 2</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>位置温度(T,i)℃</td><td style='text-align: center;'>温度占比(Pi)%</td></tr><tr><td style='text-align: center;'>-40</td><td style='text-align: center;'>6</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>20</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>65</td></tr><tr><td style='text-align: center;'>85</td><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>90</td><td style='text-align: center;'>1</td></tr></table>

#### G.2.2 加速模型

试验采用 Coffin-Manson 加速模型。为了计算温度交变条件下的耐久性试验的持续时间，考虑 DUT 由表 G.1 安装位置  $ \Delta T $  的平均温度变化和使用寿命期间的温度循环次数  $ N_{cycle} $ 。

按公式(G.1)计算 Coffin-Manson 模型的加速度系数与场地平均温度变化的关系。

 $$ \mathrm{ACM}=(\Delta T_{test}/\Delta T)^{c} $$ 

式中：

ACM —— Coffin-Manson 模型的加速度系数；

 $ \Delta T_{test} $ ——在一次试验循环期间的温差( $ \Delta T_{test}=T_{max}-T_{min} $ );

 $ \Delta T $  ——在场地使用寿命期间的平均温升, 见表 G.1;

C —— Coffin-Manson 模型参数(在本文件中 C 固定设置为 2.5)。

按公式 $  \text{(G.2)}  $ 计算试验循环次数。

 $$ N_{test}=N_{cycle}/ACM $$ 

式中：

 $ N_{test} $  ——试验循环次数；

 $ N_{cycle} $  ——在安装位置使用寿命期间的温度循环次数；

ACM —— Coffin-Manson 模型的加速度系数。

示例：以安装在无特殊要求处的 DUT 为例，耐久性为 10 年，每天使用 2 次， $ N_{cycle} $  为 7300 次，表 G.2 位置温度模型 1 给出的  $ T_{min} = -40^{\circ}C $  和  $ T_{max} = 85^{\circ}C $ ，由表 G.1 安装位置平均温升  $ \Delta T = 36 K $  的产品为例进行计算：

 $$ \Delta T_{test}=85\ ^{\circ}C-(-40\ ^{\circ}C)=125\ ^{\circ}C $$ 

按公式 $  \text{(G.1)}  $ 计算出 Coffin-Manson 模型的加速度系数为：

 $$ \mathrm{ACM}=(125/36)^{2.5}\approx22.47 $$ 

按公式 $  \text{(G.2)}  $ 计算出试验循环次数为：

 $$ N_{test}=7\ 300/22.47\approx325\  次 $$ 

DUT 温度热浸透的时间为 15 min，设定温度在 20 min 后浸透部件，则保持时间为 35 min 来计算一次循环的时间为：

 $$ T_{cycle}=2\times\left[\left(T_{max}-T_{min}\right)/\left(4\ ^{\circ}C/\min\right)+35\ min\right]=132.5\ min $$ 

325 次循环时整个试验时间为：

 $$ t=(325\times132.5\ min)/60\ min\approx718\ h $$ 

即：DUT 温度交变耐久性试验的每个循环时间为 132.5 min，总循环次数为 325 次，试验总的时间为 718 h。

# 附录 H

(资料性)

# 车辆天线性能测试场地要求

### H.1 一般要求

车辆天线性能测试场地满足以下要求：

——净空间尺寸满足测量设备和被测车辆天线安装架设和扫描采样的空间需求；

——确保来自外部物体的反射不影响测量结果。

### H.2 开阔场要求

开阔场满足以下要求：

——测量场地是一个没有电磁波反射物的空旷场地，避开建筑物、电力线、篱笆和树木等，并远离地下线缆、管道等；

——若测量场地采用气候保护罩，则气候保护罩能保护包括被测天线及系统在内的整个试验场地，所用材料具有射频透明性，以避免造成不必要的反射；

——宜使用金属接地平板的测量场地，可使用时域法消除地面反射，测量设施和测量人员都在无障碍区之外；

——对于旋转组件位于接地平板下的转台，旋转表面与接地平板齐平，并将其与接地平板导电连接。

注：测量区域顶部没有反射特性的防护罩。

### H.3 全电波暗室要求

全电波暗室满足表 H.1。

<div style="text-align: center;">表 H.1 全电波暗室场地性能要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>性能指标</td><td style='text-align: center;'>具体要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>屏蔽效能</td><td style='text-align: center;'>在700 MHz～6 GHz频率范围内，屏蔽效能大于100 dB</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>测量范围</td><td style='text-align: center;'>天线测试系统的测量区域应覆盖待测车辆的最大尺寸</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>辐射性能要求</td><td style='text-align: center;'>将喇叭天线偏离测试系统中心2 m，喇叭天线水平极化、垂直极化的峰值增益和该天线标准峰值增益相比，偏差小于2 dB</td></tr><tr><td colspan="3">注：增益的测试误差包含标准增益天线不确定性在内的所有系统测试误差。</td></tr></table>

## 參 考 文 献

[1] GB/T 18655—2018 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法

[2] GB/T 19951—2019 道路车辆 电气/电子部件对静电放电抗扰性的试验方法

[3] GB/T 21437.2—2021 道路车辆 电气/电子部件对传导和耦合引起的电骚扰试验方法 第2部分：沿电源线的电瞬态传导发射和抗扰性

[4] GB/T 21437.3—2021 道路车辆电气/电子部件对传导和耦合引起的电骚扰试验方法 第3部分：对耦合到非电源线电瞬态的抗扰性

[5] GB 26149—2017 乘用车轮胎气压监测系统的性能要求和试验方法

[6] GB/T 28046.1—2011 道路车辆电气及电子设备的环境条件和试验 第1部分:一般规定

[7] GB/T 44373—2024 智能网联汽车 术语和定义



