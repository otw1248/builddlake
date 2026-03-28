

# 中华人民共和国国家标准

GB/T 45688—2025

# 新能源汽车运行安全性能动态监测预警 技术要求

# Technical requirements for dynamic monitoring and early warning of new energy vehicle safety operation

2025-05-30 发布

2025-12-01 实施

国家市场监督管理总局  

国家标准化管理委员会  

发布



## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语、定义和缩略语 …… 1  
  
3.1 术语和定义 …… 1  
  
3.2 缩略语 …… 2  
  
4 一般要求 …… 2  
  
5 动态监测 …… 2  
  
5.1 故障监测 …… 2  
  
5.2 隐患监测 …… 3  
  
6 动态预警 …… 4  
  
6.1 一般要求 …… 4  
  
6.2 故障通知 …… 4  
  
6.3 隐患告警 …… 4  
  
附录 A（规范性） 新能源汽车运行安全平台数据格式和定义 …… 5  
  
附录 B（规范性） 上行和下行数据系统预留命令传输协议 …… 9  
  
B.1 上行数据系统预留命令传输协议 …… 9  
  
B.2 下行数据系统预留命令传输协议 …… 12  
  
附录 C（资料性） 新能源汽车运行安全隐患分析模型 …… 14  
  
C.1 动力蓄电池最高温度（充电） …… 14  
  
C.2 单体蓄电池最高电压（充电） …… 14  
  
C.3 单体电池电压极差（充电） …… 14  
  
C.4 动力蓄电池最高温度（放电） …… 15  
  
C.5 单体蓄电池最低电压（放电） …… 15  
  
C.6 驱动电机温度 …… 16  
  
C.7 驱动电机控制器温度 …… 16  
  
C.8 DC/DC 温度 …… 17  
  
C.9 绝缘电阻 …… 17  
  
C.10 电压采样异常 …… 18  
  
C.11 久置过放 …… 19  
  
C.12 长时间聚集停放 …… 19  
  
附录 D（资料性） 新能源汽车运行安全性能动态预警措施 …… 20  
  
D.1 故障处置措施 …… 20  
  
D.2 隐患告警措施 …… 20  
  
参考文献 …… 21



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由中华人民共和国公安部提出。

本文件由全国道路交通管理标准化技术委员会(SAC/TC 576)归口。

本文件起草单位：公安部交通管理科学研究所、北京理工大学、上海人工智能研究院有限公司、宁德时代新能源科技股份有限公司、深圳市安车检测股份有限公司、时代智慧科技（福建）有限公司。

本文件主要起草人：孙巍、俞春俊、张建国、张军、张昊、张希、王震坡、张堃、宋海涛、林倪、区刚、冯子建、孙康升、秦征骁、穆文浩、雍成明、镇煌。



# 新能源汽车运行安全性能动态监测预警   技术要求

## 1 范围

本文件规定了新能源汽车运行安全性能的动态监测和动态预警技术要求。

本文件适用于装备了符合 GB/T 32960.2 要求的车载终端的在用纯电动汽车、插电式混合动力（含增程式）汽车的运行安全性能动态监测及预警，其他类型在用新能源汽车参照使用。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 19596 电动汽车术语

GB/T 22239 信息安全技术 网络安全等级保护基本要求

GB/T 32960.1 电动汽车远程服务与管理系统技术规范 第1部分：总则

GB/T 32960.2 电动汽车远程服务与管理系统技术规范 第2部分：车载终端

GB/T 32960.3 电动汽车远程服务与管理系统技术规范 第3部分：通信协议及数据格式

GB 38031 电动汽车用动力蓄电池安全要求

## 3 术语、定义和缩略语

### 3.1 术语和定义

GB/T 19596、GB/T 32960.1、GB/T 32960.2、GB/T 32960.3 和 GB 38031 界定的以及下列术语和定义适用于本文件。

3.1.1

新能源汽车运行安全平台数据 platform data of new energy vehicle safety operation

通过新能源汽车车载终端获取并储存于公共平台、企业平台，能够反映新能源汽车运行安全状态的数据。

3.1.2

公共平台 public service and management platform

国家、地方政府或其指定机构建立的、对管辖范围内新能源汽车进行数据采集和统一管理的平台。

[来源:GB/T 32960.1—2016,3.2,有修改]

3.1.3

企业平台 enterprise service and management platform

整车企业自建或者委托第三方技术单位，对服务范围内的新能源汽车和用户进行管理，并提供安全运行服务与管理的平台。

[来源:GB/T 32960.1—2016,3.3,有修改]

#### 3.1.4 

## 动态监测 dynamic monitoring

利用新能源汽车运行安全平台数据或数据模型开展实时或准实时监测，分析运行安全故障或隐患。

注 $ ^{1} $ ：运行安全故障，可能引起新能源汽车运行过程中特有的电安全部件或系统等（动力蓄电池、驱动电机和电控系统等）不满足设计运行条件的情形。

注 $ ^{2} $ ：运行安全隐患，可能对新能源汽车特有的电安全部件或系统等（动力蓄电池、驱动电机和电控系统等）造成损失或威胁的风险。

#### 3.1.5 

## 动态预警 dynamic early warning

利用新能源汽车运行安全性能动态监测的结果，对存在运行安全故障或隐患的新能源汽车进行风险通知或告警。

### 3.2 缩略语

下列缩略语适用于本文件。

DC/DC: DC/DC 变换器(DC/DC Converter)

SOC: 荷电状态(State-of-Charge)

## 4 一般要求

4.1 企业平台应符合以下要求：

a）具备第5章规定的动态监测功能和第6章规定的动态预警功能；

b）能按照 GB/T 32960.3 的要求接收车载终端上报的新能源汽车运行安全平台数据，数据格式和定义符合附录 A 中表 A.1 的规定；

c） 能按照 GB/T 32960.3 的要求将新能源汽车运行安全平台数据、动态监测结果、故障处置信息和隐患处置信息等上报公共平台，通信协议符合附录 B 的规定；

d）能上报发生交通事故车辆的事发时间点前后各30 s事故信息，且信息采样周期不大于1 s，其中事故发生前数据以补发的形式进行传输，上报的数据格式和定义符合表B.5的要求；

e） 安全保护能力满足 GB/T 22239 规定的第二级及以上安全要求。

### 4.2 公共平台应符合以下要求：

a） 能按照 GB/T 32960.3 的要求接收企业平台上报的新能源汽车运行安全平台数据、动态监测结果、故障处置信息和隐患处置信息等；

b）通信协议符合附录 B 的规定；

c） 安全保护能力满足 GB/T 22239 规定的第三级及以上安全要求；

d）具备动态监测功能的公共平台，能将动态监测结果反馈给对应企业平台，并能提供新能源汽车运行安全性能检验动态监测结果。

注：新能源汽车运行安全性能依据 GB/T 44500 给出的检验规程进行检验。

## 5 动态监测

### 5.1 故障监测

#### 5.1.1 监测项目

故障监测项目应包括表1所列的内容。

<div style="text-align: center;">表 1 新能源汽车运行安全故障监测</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>故障监测项目</td><td style='text-align: center;'>通用报警标志位</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>动力蓄电池温度</td><td style='text-align: center;'>电池高温报警</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>动力蓄电池温差</td><td style='text-align: center;'>温度差异报警</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>单体蓄电池最高电压</td><td style='text-align: center;'>单体电池过压报警</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>单体蓄电池最低电压</td><td style='text-align: center;'>单体电池欠压报警</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>单体蓄电池电压一致性</td><td style='text-align: center;'>电池单体一致性差报警</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>SOC异常</td><td style='text-align: center;'>SOC跳变报警</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>驱动电机温度报警</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>驱动电机控制器温度报警</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>DC/DC温度</td><td style='text-align: center;'>DC/DC温度报警</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>DC/DC状态</td><td style='text-align: center;'>DC/DC状态报警</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>绝缘报警</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>高压互锁状态</td><td style='text-align: center;'>高压互锁状态报警</td></tr></table>

5.1.2 应按照以下程序开展监测：

a）根据表1所列的故障监测项目，提取表A.1中的通用报警标志数据；

b）根据表 A.6 的通用报警标志位进行分析，生成该项目的监测结果；

c）当企业平台监测结果存在异常时，实时上报监测结果，上报的数据格式和定义符合表 B.2 的要求。

### 5.2 隐患监测

#### 5.2.1 监测项目

隐患监测项目应包括表 2 所列的内容。

<div style="text-align: center;">表 2 新能源汽车运行安全隐患监测</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>隐患监测项目</td><td style='text-align: center;'>运行安全平台数据</td><td style='text-align: center;'>隐患分析模型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>动力蓄电池最高温度(充电)</td><td style='text-align: center;'>时间、电池温度、充电状态</td><td style='text-align: center;'>动力蓄电池最高温度(充电)分析模型(见C.1)</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>单体蓄电池最高电压(充电)</td><td style='text-align: center;'>时间、单体电池最高电压、充电状态</td><td style='text-align: center;'>单体蓄电池最高电压(充电)分析模型(见C.2)</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>单体蓄电池电压极差(充电)</td><td style='text-align: center;'>时间、单体电池电压、充电状态</td><td style='text-align: center;'>单体电池电压极差分析模型(见C.3)</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>动力蓄电池最高温度(放电)</td><td style='text-align: center;'>时间、电池温度、充电状态</td><td style='text-align: center;'>动力蓄电池最高温度(放电)分析模型(见C.4)</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>单体蓄电池最低电压(放电)</td><td style='text-align: center;'>时间、单体电池最低电压、充电状态</td><td style='text-align: center;'>单体蓄电池最低电压(放电)分析模型(见C.5)</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>时间、驱动电机温度</td><td style='text-align: center;'>驱动电机温度分析模型(见C.6)</td></tr></table>

<div style="text-align: center;">表 2 新能源汽车运行安全隐患监测（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>隐患监测项目</td><td style='text-align: center;'>运行安全平台数据</td><td style='text-align: center;'>隐患分析模型</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>时间、驱动电机控制器温度</td><td style='text-align: center;'>驱动电机控制器温度分析模型（见C.7）</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>DC/DC温度</td><td style='text-align: center;'>时间、DC/DC温度</td><td style='text-align: center;'>DC/DC变换器温度分析模型（见C.8）</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>时间、绝缘电阻</td><td style='text-align: center;'>绝缘电阻分析模型（见C.9）</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>电压采样异常</td><td style='text-align: center;'>时间、单体电池电压、单体电池最高电压、单体电池最低电压</td><td style='text-align: center;'>电压采样异常分析模型（见C.10）</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>久置过放</td><td style='text-align: center;'>时间、SOC</td><td style='text-align: center;'>久置过放分析模型（见C.11）</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>长时间聚集停放</td><td style='text-align: center;'>时间、车辆状态、车辆位置、SOC</td><td style='text-align: center;'>长时间聚集停放分析模型（见C.12）</td></tr></table>

5.2.2 应按照以下程序开展监测：

a）根据表2所列的隐患监测项目，提取表A.1中对应的运行安全平台数据；

b）利用隐患分析模型，生成该项目的监测结果；

c) 当企业平台监测结果存在异常时实时上报监测结果，上报的数据格式和定义符合表 B.3 的要求；

d）当公共平台监测结果存在异常时实时反馈监测结果，反馈的数据格式和定义符合表 B.7 的要求。

## 6 动态预警

### 6.1 一般要求

6.1.1 应能按照动态监测结果发出故障通知和隐患告警。

6.1.2 应按照运行安全故障等级、隐患次数等制定动态预警处置措施，处置措施内容见附录 D。

### 6.2 故障通知

6.2.1 应分级进行故障通知，故障等级分为3级。其中：1级故障，指不影响车辆正常行驶的故障；2级故障，指影响车辆性能，需限制车辆行驶速度、距离、路线或时间等的故障；3级故障，指驾驶人应立即停车处理或请求救援的故障；具体等级对应的故障内容由企业平台自行定义。

6.2.2 应按照动态预警处置措施进行故障通知，实时记录及上报故障处置信息，上报的数据格式和定义应符合表 B.4 的要求。

### 6.3 隐患告警

应依据动态预警处置措施进行隐患告警，实时记录及上报隐患处置信息，上报的数据格式和定义应符合表 B.4 的要求。

## 附录 A

(规范性)

## 新能源汽车运行安全平台数据格式和定义

表 A.1 规定了新能源汽车运行安全平台数据格式和定义。

<div style="text-align: center;">表 A.1 新能源汽车运行安全平台数据格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>数据采集时间</td><td style='text-align: center;'>6</td><td style='text-align: center;'>BYTE[6]</td><td style='text-align: center;'>时间定义按照表A.2</td></tr><tr><td style='text-align: center;'>车辆状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:车辆启动状态;0x02:熄火;0x03:其他状态;“0xFE”表示异常,“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>充电状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:停车充电;0x02:行驶充电;0x03:未充电状态;0x04:充电完成;“0xFE”表示异常,“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>运行模式</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:纯电;0x02:混动;0x03:燃油;0xFE表示异常;0xFF表示无效</td></tr><tr><td style='text-align: center;'>车速</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围:0~2200,表示(0 km/h~220 km/h),最小计量单元:0.1 km/h,“0xFF,0xFE”表示异常,“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>累计里程</td><td style='text-align: center;'>4</td><td style='text-align: center;'>DWORD</td><td style='text-align: center;'>有效值范围:0~999999,表示(0 km~999999.9 km),最小计量单元:0.1 km,“0xFF,0xFF,0xFF,0xFE”表示异常,“0xFF,0xFF,0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>总电压</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围:0~10000(表示0 V~1000 V),最小计量单元:0.1 V,“0xFF,0xFE”表示异常,“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>总电流</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围:0~20000(偏移量1000 A,表示-1000 A~1000 A),最小计量单元:0.1 A,“0xFF,0xFE”表示异常,“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>SOC</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围:0~100(表示0%~100%),最小计量单元:1%,0xFE表示异常;0xFF表示无效</td></tr><tr><td style='text-align: center;'>DC/DC状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:工作;0x02:断开;“0xFE”表示异常,“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>挡位</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>挡位定义按照表A.3</td></tr><tr><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围:0~60000,表示(0 kΩ~60000 kΩ),最小计量单元:1 kΩ</td></tr><tr><td style='text-align: center;'>驱动电机个数</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值1~253</td></tr><tr><td style='text-align: center;'>驱动电机总成信息列表</td><td style='text-align: center;'>∑每个驱动电机总成信息长度</td><td style='text-align: center;'>—</td><td style='text-align: center;'>按驱动电机序号依次排列,每个驱动电机数据格式和定义按照表A.4</td></tr><tr><td style='text-align: center;'>定位状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>状态位定义按照表A.5</td></tr><tr><td style='text-align: center;'>经度</td><td style='text-align: center;'>4</td><td style='text-align: center;'>DWORD</td><td style='text-align: center;'>以度为单位的经度值乘以10°,精确到百万分之一度</td></tr></table>

<div style="text-align: center;">表 A.1 新能源汽车运行安全平台数据格式和定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>纬度</td><td style='text-align: center;'>4</td><td style='text-align: center;'>DWORD</td><td style='text-align: center;'>以度为单位的纬度值乘以 $ 10^{6} $ ，精确到百万分之一度</td></tr><tr><td style='text-align: center;'>单体电池最高电压</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围：0～15 000（表示0 V～15 V），最小计量单元；0.001 V，“0xFF,0xFE”表示异常，“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>单体电池最低电压</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围：0～15 000（表示0 V～15 V），最小计量单元；0.001 V，“0xFF,0xFE”表示异常，“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>单体电池最高温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：0～250（数值偏移量40℃，表示-40℃～210℃），最小计量单元：1℃，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>单体电池最低温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：0～250（数值偏移量40℃，表示-40℃～210℃），最小计量单元：1℃，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>最高报警等级</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>当前发生的故障中的最高等级值，有效值范围：0～3，“0”表示无故障；“1”表示1级故障；“2”表示2级故障；“3”表示3级故障；“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>通用报警标志</td><td style='text-align: center;'>4</td><td style='text-align: center;'>DWORD</td><td style='text-align: center;'>通用报警标志位定义按照表A.6</td></tr><tr><td style='text-align: center;'>扩展数据长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>扩展数据长度N，有效范围1～65531</td></tr><tr><td style='text-align: center;'>扩展数据</td><td style='text-align: center;'>1×N</td><td style='text-align: center;'>BYTE[N]</td><td style='text-align: center;'>按照表A.7</td></tr></table>

<div style="text-align: center;">表 A.2 时间定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>有效值范围</td></tr><tr><td style='text-align: center;'>年</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0~99</td></tr><tr><td style='text-align: center;'>月</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>1~12</td></tr><tr><td style='text-align: center;'>日</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>1~31</td></tr><tr><td style='text-align: center;'>小时</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0~23</td></tr><tr><td style='text-align: center;'>分钟</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0~59</td></tr><tr><td style='text-align: center;'>秒</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0~59</td></tr></table>

<div style="text-align: center;">表 A.3 挡位状态位定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Bit7</td><td style='text-align: center;'>Bit6</td><td style='text-align: center;'>Bit5</td><td style='text-align: center;'>Bit4</td><td style='text-align: center;'>Bit3</td><td style='text-align: center;'>Bit2</td><td style='text-align: center;'>Bit1</td><td style='text-align: center;'>Bit0</td></tr><tr><td style='text-align: center;'>1:无效0:有效</td><td style='text-align: center;'>预留,预留位用0表示</td><td style='text-align: center;'>1:有驱动力0:无驱动力</td><td style='text-align: center;'>1:有制动力0:无制动力</td><td style='text-align: center;'>挡位:=0000=0001=0010=0011=0100=0101</td><td style='text-align: center;'>空挡1挡2挡3挡4挡5挡</td><td style='text-align: center;'>=0110=……=1101=1110=1111</td><td style='text-align: center;'>6挡倒挡自动D挡停车P挡</td></tr></table>

<div style="text-align: center;">表 A.4 每个驱动电机数据格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>驱动电机序号</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>驱动电机顺序号，有效值范围1~253</td></tr><tr><td style='text-align: center;'>驱动电机状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:耗电；0x02:发电；0x03:关闭状态；0x04:准备状态“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>驱动电机转速</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围：0~65 531（数值偏移量20 000表示-20 000 r/min~45 531 r/min），最小计量单元：1 r/min，“0xFF,0xFE”表示异常，“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>驱动电机转矩</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围：0~65 531（数值偏移量20 000表示-2 000 N·m~4 553.1 N·m），最小计量单元：0.1 N·m，“0xFF,0xFE”表示异常，“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：0~250（数值偏移量40℃，表示-40℃~210℃），最小计量单元：1℃，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：0~250（数值偏移量40℃，表示-40℃~+210℃），最小计量单元：1℃，“0xFE”表示异常，“0xFF”表示无效</td></tr></table>

<div style="text-align: center;">表 A.5 状态位定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>位</td><td style='text-align: center;'>状态</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0:有效定位;1:无效定位(当数据通信正常,而不能获取定位信息时,发送最后一次有效定位信息,并将定位状态置为无效)</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0:北纬;1:南纬</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0:东经;1:西经</td></tr><tr><td style='text-align: center;'>3~7</td><td style='text-align: center;'>保留</td></tr></table>

<div style="text-align: center;">表 A.6 通用报警标志位定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>位</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>处理说明</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1:温度差异报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1:电池高温报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>1:单体电池过压报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>1:单体电池欠压报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>1:SOC跳变报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>1:电池单体一致性差报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>1:绝缘报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>1:DC/DC温度报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>1:DC/DC状态报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr></table>

<div style="text-align: center;">表 A.6 通用报警标志位定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>位</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>处理说明</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>1:驱动电机控制器温度报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>1:高压互锁状态报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>1:驱动电机温度报警;0:正常</td><td style='text-align: center;'>标志维持到报警条件解除</td></tr></table>

<div style="text-align: center;">表 A.7 扩展数据格式及定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>DC/DC 温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：0～250（数值偏移量40℃，表示-40℃～210℃），最小计量单元：1℃，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01：开机；0x02：关机；0x03：正常；0x04：故障；0xFE：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>电池管理系统状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01：开机；0x02：关机；0x03：正常；0x04：故障；0xFE：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>电池单体总数</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>N个电池单体，有效值范围：1～250，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>电池单体信息列表</td><td style='text-align: center;'>Σ每个电池单体信息长度</td><td style='text-align: center;'>—</td><td style='text-align: center;'>按电池单体序号依次排列，每个单体电池数据格式和定义按表A.8</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_118_910_154_944.jpg" alt="Image" width="3%" /></div>


<div style="text-align: center;">表 A.8 电池单体数据格式及定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>单体电池代号</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：1～250，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>单体电池温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围：0～250（数值偏移量40℃，表示-40℃～210℃），最小计量单元：1℃，“0xFE”表示异常，“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>单体电池电压</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围：0～60 000（表示0 V～60.000 V），最小计量单元：0.001 V，“0xFF,0xFE”表示异常，“0xFF,0xFF”表示无效</td></tr></table>

## 附录 B

(规范性)

# 上行和下行数据系统预留命令传输协议

### B.1 上行数据系统预留命令传输协议

#### B.1.1 命令标识

表 B.1 规定了上行数据系统数据预留命令传输协议中的命令标识定义。

<div style="text-align: center;">表 B.1 上行数据系统命令标识定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编码</td><td style='text-align: center;'>定义</td></tr><tr><td style='text-align: center;'>0x10</td><td style='text-align: center;'>故障监测结果上报</td></tr><tr><td style='text-align: center;'>0x11</td><td style='text-align: center;'>隐患监测结果上报</td></tr><tr><td style='text-align: center;'>0x12</td><td style='text-align: center;'>故障及隐患处置信息上报</td></tr><tr><td style='text-align: center;'>0x13</td><td style='text-align: center;'>事故信息上报</td></tr></table>

#### B.1.2 数据单元格式和定义

##### B.1.2.1 故障监测结果上报

表 B.2 规定了故障监测结果上报数据格式和定义。

<div style="text-align: center;">表 B.2 故障监测结果上报数据格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>数据采集时间</td><td style='text-align: center;'>6</td><td style='text-align: center;'>BYTE[6]</td><td style='text-align: center;'>时间定义按照表A.2</td></tr><tr><td style='text-align: center;'>故障等级</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>当前发生的故障中的最高等级值，有效值范围：0～3，“0”表示无故障；“1”表示1级故障；“2”表示2级故障；“3”表示3级故障；“0”表示异常，“0”表示无效</td></tr><tr><td style='text-align: center;'>动力蓄电池温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>动力蓄电池温差</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最高电压</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最低电压</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>单体蓄电池电压一致性</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>SOC异常</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00：正常；0x01：异常；0xFF：无效</td></tr></table>

<div style="text-align: center;">表 B.2 故障监测结果上报数据格式和定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>DC/DC 温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00: 正常; 0x01: 异常; 0xFF: 无效</td></tr><tr><td style='text-align: center;'>DC/DC 状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00: 正常; 0x01: 异常; 0xFF: 无效</td></tr><tr><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00: 正常; 0x01: 异常; 0xFF: 无效</td></tr><tr><td style='text-align: center;'>高压互锁状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00: 正常; 0x01: 异常; 0xFF: 无效</td></tr></table>

##### B.1.2.2 隐患监测结果上报

表 B.3 规定了隐患监测结果上报数据格式和定义。

<div style="text-align: center;">表 B.3 隐患监测结果上报数据格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>数据采集时间</td><td style='text-align: center;'>6</td><td style='text-align: center;'>BYTE[6]</td><td style='text-align: center;'>时间定义按照表A.2</td></tr><tr><td style='text-align: center;'>动力蓄电池最高温度（充电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最高电压（充电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池电压极差（充电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>动力蓄电池最高温度（放电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最低电压（放电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>DC/DC温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>电压采样异常</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>久置过放</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>长时间聚集停放</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr></table>

##### B.1.2.3 故障及隐患处置信息上报

表 B.4 规定了故障及隐患处置信息上报数据格式和定义。

<div style="text-align: center;">表 B.4 故障及隐患处置信息上报数据格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>数据采集时间</td><td style='text-align: center;'>6</td><td style='text-align: center;'>BYTE[6]</td><td style='text-align: center;'>时间定义按照表A.2</td></tr><tr><td style='text-align: center;'>动力蓄电池温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>动力蓄电池温差</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最高电压</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最低电压</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池电压一致性</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>SOC异常</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>DC/DC温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>DC/DC状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>高压互锁状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>动力蓄电池最高温度(充电)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最高电压(充电)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池电压极差(充电)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>动力蓄电池最高温度(放电)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最低电压(放电)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>DC/DC温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>电压采样异常</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>久置过放</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr><tr><td style='text-align: center;'>长时间聚集停放</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:未处置;0xFF:无效</td></tr></table>

##### B.1.2.4 事故信息上报

表 B.5 规定了事故信息上报的数据格式和定义。

<div style="text-align: center;">表 B.5 事故信息上报数据格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>数据采集时间</td><td style='text-align: center;'>6</td><td style='text-align: center;'>BYTE[6]</td><td style='text-align: center;'>时间定义按照表A.2</td></tr><tr><td style='text-align: center;'>制动灯状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:启亮;0x02:熄灭;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>左转向灯状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:启亮;0x02:熄灭;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>右转向灯状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:启亮;0x02:熄灭;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>驾驶人安全带状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:使用;0x02:未使用;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>副驾驶安全带状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:使用;0x02:未使用;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>加速踏板信号</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围:0～100(表示0%～100%),最小计量单元:1%,“0xFE”表示异常,“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>制动踏板信号</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>有效值范围:0～100(表示0%～100%),最小计量单元:1%,“0”表示制动关的状态;在无具体行程值情况下,用“0x65”即“101”表示制动有效状态,“0xFE”表示异常,“0xFF”表示无效</td></tr><tr><td style='text-align: center;'>方向盘转角</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围:0～1080(数值偏移量540°,表示-540°～+540°),最小计量单元:1°,正值为右转,负值为左转</td></tr><tr><td style='text-align: center;'>巡航状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:开启;0x02:未开启;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>ABS状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:开启;0x02:未开启;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>ESP状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:开启;0x02:未开启;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>AEBS状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:开启;0x02:未开启;0xFE:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>制动主缸压力</td><td style='text-align: center;'>2</td><td style='text-align: center;'>WORD</td><td style='text-align: center;'>有效值范围:0～200 000(表示0 kPa～200 000 kPa),最小计量单元:0.1 kPa,“0xFF,0xFE”表示异常,“0xFF,0xFF”表示无效</td></tr><tr><td style='text-align: center;'>能量回收状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x01:工作;0x02:未工作;0xFE:异常;0xFF:无效</td></tr></table>

### B.2 下行数据系统预留命令传输协议

#### B.2.1 命令标识

表 B.6 规定了下行数据系统数据预留命令传输协议中的命令标识定义。

<div style="text-align: center;">表 B.6 下行数据系统命令标识定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编码</td><td style='text-align: center;'>定义</td></tr><tr><td style='text-align: center;'>0x90</td><td style='text-align: center;'>隐患监测结果反馈</td></tr></table>

#### B.2.2 数据单元格式和定义

表 B.7 规定了隐患监测结果反馈数据单元格式和定义。

<div style="text-align: center;">表 B.7 隐患监测结果反馈数据单元格式和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据表示内容</td><td style='text-align: center;'>长度/byte</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>描述及要求</td></tr><tr><td style='text-align: center;'>数据采集时间</td><td style='text-align: center;'>6</td><td style='text-align: center;'>BYTE[6]</td><td style='text-align: center;'>时间定义按照表A.2</td></tr><tr><td style='text-align: center;'>动力蓄电池最高温度（充电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最高电压（充电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池电压极差（充电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>动力蓄电池最高温度（放电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>单体蓄电池最低电压（放电）</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>驱动电机控制器温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>DC/DC温度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>绝缘电阻</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>电压采样异常</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>久置过放</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr><tr><td style='text-align: center;'>长时间聚集停放</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BYTE</td><td style='text-align: center;'>0x00:正常;0x01:异常;0xFF:无效</td></tr></table>

## 附录 C

(资料性)

## 新能源汽车运行安全隐患分析模型

### C.1 动力蓄电池最高温度(充电)

利用新能源汽车运行安全平台数据进行计算。根据表 C.1 的高温风险矩阵，评估指定时间段内新能源汽车动力蓄电池在充电时的历史高温情况，判断每次超过高温阈值时是否超过对应时长/次数，评估电池风险状态。

<div style="text-align: center;">表 C.1 高温风险矩阵(充电)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>高温阈值/ $ ^{\circ} $ C</td><td style='text-align: center;'>$ V_{1} $</td><td style='text-align: center;'>$ V_{2} $</td><td style='text-align: center;'>$ V_{3} $</td><td style='text-align: center;'>$ \cdots $</td></tr><tr><td style='text-align: center;'>允许时长/s</td><td style='text-align: center;'>$ T_{1} $</td><td style='text-align: center;'>$ T_{2} $</td><td style='text-align: center;'>$ T_{3} $</td><td style='text-align: center;'>$ \cdots $</td></tr><tr><td style='text-align: center;'>允许次数/次</td><td style='text-align: center;'>$ C_{1} $</td><td style='text-align: center;'>$ C_{2} $</td><td style='text-align: center;'>$ C_{3} $</td><td style='text-align: center;'>$ \cdots $</td></tr></table>

表 C.1 中的值由企业根据电池产品类型自行确定，每个电池产品类型使用一个高温风险矩阵（充电）。一般而言，更高的温度对应更短的允许时长和更少的允许次数，宜包含如下阈值：

——三元锂电池： $ V=60^{\circ}C,T=0,C=0; $ 

——磷酸铁锂电池： $ V=65^{\circ}C $ ，T=0，C=0。

当温度值大于高温阈值的时长或次数超过表 C.1 矩阵中的允许时长或允许次数时，模型输出结果为 1：异常，否则模型输出结果为 0：正常。

### C.2 单体蓄电池最高电压(充电)

利用新能源汽车运行安全平台数据进行计算。根据表 C.2 的高压风险矩阵，评估指定时间段内新能源汽车单体蓄电池在充电状态下的历史高压情况，判断各超过最高电压阈值的情况是否超过对应时长/次数，评估电池风险状态。

<div style="text-align: center;">表 C.2 高压风险矩阵(充电)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>电压阈值/V</td><td style='text-align: center;'>$ V_{1} $</td><td style='text-align: center;'>$ V_{2} $</td><td style='text-align: center;'>$ V_{3} $</td><td style='text-align: center;'>...</td></tr><tr><td style='text-align: center;'>允许时长/s</td><td style='text-align: center;'>$ T_{1} $</td><td style='text-align: center;'>$ T_{2} $</td><td style='text-align: center;'>$ T_{3} $</td><td style='text-align: center;'>...</td></tr><tr><td style='text-align: center;'>允许次数/次</td><td style='text-align: center;'>$ C_{1} $</td><td style='text-align: center;'>$ C_{2} $</td><td style='text-align: center;'>$ C_{3} $</td><td style='text-align: center;'>...</td></tr></table>

表 C.2 中的值由企业根据电池产品类型自行确定，每个电池产品类型使用一个高压风险矩阵（充电）。一般而言，更高的电压对应更短的允许时长和允许次数，宜包含如下阈值：

——三元锂电池： $ V=4.4\ V,\ T=0,\ C=0; $ 

——磷酸铁锂电池： $ V=3.7\ V,T=0,C=0 $ 。

当电压值大于电压阈值的时长或次数超过表 C.2 矩阵中的允许时长或允许次数时，模型输出结果为 1：异常，否则模型输出结果为 0：正常。

### C.3 单体电池电压极差(充电)

利用新能源汽车运行安全平台数据进行计算。在充电过程中，基于单体电池电压值，计算指定时间

段内每一个采样时刻对应的各单体电池之间的极差电压，将所有采样时刻对应的极差电压的均方根作为评价电压一致性的指标，按公式(C.1)计算：

 $$ r_{\mathrm{V}}=\sqrt{\frac{1}{N}\sum_{j=1}^{N}\left(V_{\max,j}-V_{\min,j}\right)^{2}} $$ 

式中：

N ——采样点个数；

j ——采样点时刻；

 $ V_{max,j} $  ——充电阶段第 j 时刻各单体电池电压的最大值，单位为伏特(V)；

 $ V_{min,j} $  ——充电阶段第 j 时刻各单体电池电压的最小值，单位为伏特(V)；

 $ r_{v} $  ——所有采样时刻对应的各单体电池之间的极差电压的均方根，即单体电池电压极差。

当  $ r_{V} $  小于 0.5 V 时模型输出结果宜为 0：正常； $ r_{V} $  大于或等于 0.5 V 时，模型输出结果宜为 1：异常。

### C.4 动力蓄电池最高温度(放电)

利用新能源汽车运行安全平台数据进行计算。根据表 C.3 的高温风险矩阵，评估指定时间段内新能源汽车动力蓄电池在放电时的历史高温情况，判断每次超过高温阈值时是否超过对应时长/次数，评估电池风险状态。

<div style="text-align: center;">表 C.3 高温风险矩阵(放电)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>高温阈值/ $ ^{\circ} $ C</td><td style='text-align: center;'>$ V_{1} $</td><td style='text-align: center;'>$ V_{2} $</td><td style='text-align: center;'>$ V_{3} $</td><td style='text-align: center;'>$ \cdots $</td></tr><tr><td style='text-align: center;'>允许时长/s</td><td style='text-align: center;'>$ T_{1} $</td><td style='text-align: center;'>$ T_{2} $</td><td style='text-align: center;'>$ T_{3} $</td><td style='text-align: center;'>$ \cdots $</td></tr><tr><td style='text-align: center;'>允许次数/次</td><td style='text-align: center;'>$ C_{1} $</td><td style='text-align: center;'>$ C_{2} $</td><td style='text-align: center;'>$ C_{3} $</td><td style='text-align: center;'>$ \cdots $</td></tr></table>

表 C.3 中的值由企业根据电池产品类型自行确定，每个电池产品类型使用一个高温风险矩阵（放电）。一般而言，更高的温度对应更短的允许时长和允许次数，宜包含如下阈值：

——三元锂电池： $ V=60^{\circ}C,T=0,C=0; $ 

——磷酸铁锂电池： $ V=65^{\circ}C,T=0,C=0 $ 

当温度值大于高温阈值的时长或次数超过表 C.3 矩阵中的允许时长或允许次数时，模型输出结果为 1：异常，否则模型输出结果为 0：正常。

### C.5 单体蓄电池最低电压(放电)

利用新能源汽车运行安全平台数据进行计算。根据表 C.4 的低压风险矩阵，评估指定时间段内新能源汽车单体蓄电池在放电状态下的历史低压情况，判断每次低于最低电压阈值时是否超过对应时长/次数，评估电池风险状态。

<div style="text-align: center;">表 C.4 低压风险矩阵(放电)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>电压阈值/V</td><td style='text-align: center;'>$ V_{1} $</td><td style='text-align: center;'>$ V_{2} $</td><td style='text-align: center;'>$ V_{3} $</td><td style='text-align: center;'>…</td></tr><tr><td style='text-align: center;'>允许时长/s</td><td style='text-align: center;'>$ T_{1} $</td><td style='text-align: center;'>$ T_{2} $</td><td style='text-align: center;'>$ T_{3} $</td><td style='text-align: center;'>…</td></tr><tr><td style='text-align: center;'>允许次数/次</td><td style='text-align: center;'>$ C_{1} $</td><td style='text-align: center;'>$ C_{2} $</td><td style='text-align: center;'>$ C_{3} $</td><td style='text-align: center;'>…</td></tr></table>

表 C.4 中的值由企业根据电池产品类型自行确定，每个电池产品类型使用一个低压风险矩阵（放电）。一般而言，更低的电压对应更短的允许时长和允许次数，宜包含如下阈值：

——三元锂电池： $ V=1.8\ V, T=0, C=0; $ 

——磷酸铁锂电池： $ V=1.5\ V, T=0, C=0 $ 。

当电压值小于电压阈值的时长或次数超过表 C.4 矩阵中的允许时长或允许次数时，模型输出结果为 1：异常，否则模型输出结果为 0：正常。

### C.6 驱动电机温度

基于新能源汽车运行安全平台数据，截取车辆最近90 d运行数据，经数据清洗和数据筛选后，形成n个连续运行片段，以运行片段为单位进行计算，记录驱动电机温度数据。将驱动电机温度大于安全阈值的累计时间占比 $ \varepsilon_{i} $ 作为驱动电机温度过高指标，按公式(C.2)～公式(C.5)进行计算：

 $$ f(n_{i})=\left\{\begin{aligned}f(n_{i}),T_{i,j}&\leqslant T_{0}\\ f(n_{i})+1,T_{i,j}&>T_{0}\end{aligned}\right. $$ 

 $$ t_{i}=f(n_{i})\times\Delta t $$ 

 $$ L_{i}=t_{n}\times\Delta t $$ 

 $$ \varepsilon_{i}=\frac{t_{i}}{T_{i}} $$ 

式中：

 $ f(n_{i}) $ ——第 i 次运动片段内驱动电机温度大于驱动电机温度安全阈值的累计次数， $ f(0)=0 $ ；

——第 i 次运行片段, $ i=1,2,\cdots,n $ ;

——第 i 次运动片段第 j 时刻， $ j=1,2,\cdots,t_{n},t_{n} $  为单个运行片段数据点数量；

 $ T_{i,j} $  ——第 i 次运动片段第 j 时刻驱动电机温度，单位为摄氏度( $ ℃ $ )；

 $ T_{0} $  ——驱动电机温度安全阈值，宜设置为  $ 80^{\circ}C $ ，单位为摄氏度( $ ^{\circ}C $ )；

 $ t_{i} $  ——第 i 次运动片段驱动电机温度大于驱动电机温度安全阈值的累计时间，单位为秒(s)；

 $ L_{i} $  ——第 i 次运动片段总时长，单位为秒(s)；

 $ \Delta t $  ——采样时间间隔,单位为秒(s);

 $ \varepsilon_{i} $  ——第 i 次运动片段驱动电机温度大于驱动电机温度安全阈值的累计时间占第 i 次运动片段总时长的比例，即驱动电机温度过高指标值。

当  $ \varepsilon_{i}\leqslant20\% $  时模型输出结果宜为 0：正常； $ \varepsilon_{i}>20\% $  时，模型输出结果宜为 1：异常。

### C.7 驱动电机控制器温度

基于线上检验数据，截取车辆最近90 d运行数据，经数据清洗和数据筛选后，形成n个连续运行片段，以运行片段为单位进行计算，记录电机控制器温度数据 $ T_{c} $ ，将电机控制器温度大于电机控制器温度安全阈值的累计时间占比 $ \delta_{i} $ 作为电机控制器温度过高指标。

按照公式 $  \text{(C.6)}  $ ～公式 $  \text{(C.9)}  $ 进行计算：

 $$ f(n_{i})=\left\{\begin{aligned}f(n_{i}),&T_{i,j}\leqslant T_{0}\\ f(n_{i})+1,&T_{i,j}>T_{0}\end{aligned}\right. $$ 

 $$ t_{i}=f(n_{i})\times\Delta t $$ 

 $$ L_{i}=t_{n}\times\Delta t $$ 

 $$ \delta_{i}=\frac{t_{i}}{T_{i}} $$ 

式中：

 $ f(n_{i}) $ ——第 i 次运动片段内电机控制器温度大于电机控制器温度安全阈值的累计次数，

 $ f(0)=0; $ 

——第 i 次运行片段， $ i=1,2,\cdots,n $ ;

——第 i 次运动片段第 j 时刻， $ j=1,2,\cdots,t_{n},t_{n} $  为单个运行片段数据点数量；

 $ T_{i,j} $  ——第 i 次运动片段第 j 时刻电机控制器温度，单位为摄氏度(℃)；

 $ T_{0} $  ——电机控制器温度安全阈值，宜设置为  $ 120^{\circ}C $ ，单位为摄氏度( $ ^{\circ}C $ )；

 $ t_{i} $  ——第 i 次运动片段电机控制器温度大于电机控制器温度安全阈值的累计时间，单位为秒(s);

 $ L_{i} $  ——第 i 次运动片段总时长，单位为秒(s);

 $ \Delta t $  ——采样时间间隔，单位为秒(s);

 $ \delta_{i} $  ——第 i 次运动片段电机控制器温度大于电机控制器温度安全阈值的累计时间占第 i 次运动片段总时长的比例。

当  $ \delta_{i}\leqslant20\% $  时模型输出结果宜为 0：正常； $ \delta_{i}>20\% $  时，模型输出结果宜为 1：异常。

### C.8 DC/DC 温度

基于线上检验数据，截取车辆最近90 d运行数据，经数据清洗和数据筛选后，形成n个连续运行片段，以运行片段为单位进行计算，记录DC/DC温度数据 $ T_{c} $ ，将DC/DC温度大于DC/DC温度安全阈值的累计时间占比 $ \delta_{i} $ 作为DC/DC温度过高指标。

按照公式 $  \text{(C.10)}  $ ～ $  \text{(C.13)}  $ 进行计算：

 $$ f(n_{i})=\left\{\begin{aligned}f(n_{i}),&T_{i,j}\leqslant T_{0}\\ f(n_{i})+1,&T_{i,j}>T_{0}\end{aligned}\right. $$ 

 $$ t_{i}=f(n_{i})\times\Delta t $$ 

 $$ L_{i}=t_{n}\times\Delta t $$ 

 $$ \delta_{i}=\frac{t_{i}}{T_{i}} $$ 

式中：

 $ f(n_{i}) $ ——第 i 次运动片段内 DC/DC 温度大于 DC/DC 温度安全阈值的累计次数， $ f(0)=0 $ ；

i ——第 i 次运行片段， $ i=1,2,\cdots,n $ ;

——第 i 次运动片段第 j 时刻， $ j=1,2,\cdots,t_{n} $ ;  $ t_{n} $  为单个运行片段数据点数量；

 $ T_{i,j} $  ——第 i 次运动片段第 j 时刻 DC/DC 温度，单位为摄氏度(℃)；

 $ T_{0} $  ——DC/DC 温度安全阈值，宜设置为  $ 90^{\circ}C $ ，单位为摄氏度( $ ^{\circ}C $ )；

 $ t_{i} $  ——第 i 次运动片段内 DC/DC 温度大于 DC/DC 温度安全阈值的累计时间，单位为秒(s)；

 $ L_{i} $  ——第 i 次运动片段总时长，单位为秒(s)；

 $ \Delta t $  ——采样时间间隔,单位为秒(s);

 $ \delta_{i} $  ——第 i 次运动片段内 DC/DC 温度大于 DC/DC 温度安全阈值的累计时间占第 i 次运动片段总时长的比例。

当  $ \delta_{i}\leqslant20\% $  时模型输出结果宜为 0：正常； $ \delta_{i}>20\% $  时，模型输出结果宜为 1：异常。

### C.9 绝缘电阻

利用新能源汽车运行安全平台数据进行计算。依据电池系统设计，通过机理分析或故障样本统计规则确定绝缘异常阈值。通过放电工况下绝缘阻值表现，评估绝缘阻值异常状态，具体步骤如下：

选取 1 d 运行数据进行计算，获取当日绝缘值常数量，依此判定绝缘阻值异常，按公式(C.14)～公式(C.16)计算：

 $$ f(r_{j})=\left\{\begin{aligned}&1,r_{j}\leqslant r_{T}\\ &0,r_{j}>r_{T}\end{aligned}\right. $$ 

 $$ C_{\mathrm{r}}=\sum_{j=1}^{N}f(r_{j}) $$ 

 $$ R=\left\{\begin{aligned}&1,C_{\mathrm{r}}\geqslant C_{\mathrm{T}}\\ &0,C_{\mathrm{r}}<C_{\mathrm{T}}\end{aligned}\right. $$ 

式中：

 $ r_{j} $  ——第 j 帧数据绝缘值，总帧数为 N，单位为欧姆( $ \Omega $ )；

 $ r_{T} $  ——绝缘异常阈值，由企业自行制定，宜设置为100  $ \Omega/V $ ，单位为伏特(V)；

 $ f(r_{i}) $ ——第i条数据绝缘低于阈值的状态；

 $ C_{r} $  ——当日绝缘数据低于阈值次数；

 $ C_{T} $  ——当日绝缘数据低于阈值次数的阈值，由企业自行制定，宜设置为5次；

R ——绝缘预警算法结果，0:正常；1:异常。

### C.10 电压采样异常

利用新能源汽车运行安全平台数据进行计算。通过电压采样键合断裂时，物理位置相邻的采样点电压值一高一低的数据特征，识别潜在电压采样异常问题：

a）截取1 d数据的详细电压列表 $ V_{list} $ 、电压最大值 $ V_{max} $ 、电压最大值物理位置 $ \operatorname{loc}_{V_{\operatorname{max}}} $ 、电压最小值 $ V_{\operatorname{min}} $ 、电压最小值物理位置 $ \operatorname{loc}_{V_{\operatorname{min}}} $ ，用于当日电压采样异常判定；

b) 基于每一条数据，计算电压中位数  $ V_{mid} $ ，电压极差 dV；

c） 全部满足如下条件，则判定为电压采样异常：

1）电压极差大；

2）最大电压最小电压物理位置相邻；

3）最高电压离群值与最低电压离群值相仿。

具体计算步骤见公式 $  \text{(C.17)}  $ ～ $  \text{(C.20)}  $ ：

 $$ C_{1}=\left\{\begin{aligned}&1,\mathrm{d}V\geqslant\mathrm{d}V_{T}\\ &0,\mathrm{d}V<\mathrm{d}V_{T}\end{aligned}\right. $$ 

 $$ C_{2}=\left\{\begin{aligned}&1,\mid\operatorname{loc}_{\mathrm{Vmax}}-\operatorname{loc}_{\mathrm{Vmin}}\mid=1\\ &0,\mid\operatorname{loc}_{\mathrm{Vmax}}-\operatorname{loc}_{\mathrm{Vmin}}\mid\neq1\end{aligned}\right. $$ 

 $$ C_{3}=\left\{\begin{aligned}1,&a<\left[(V_{\max}-V_{\mathrm{mid}})/(V_{\mathrm{mid}}-V_{\min})\right]<1/a\\ &0,(V_{\max}-V_{\mathrm{mid}})/(V_{\mathrm{mid}}-V_{\min})\leqslant a\\ &0,(V_{\max}-V_{\mathrm{mid}})/(V_{\mathrm{mid}}-V_{\min})\geqslant1/a\end{aligned}\right. $$ 

 $$ R=C_{1}\times C_{2}\times C_{3} $$ 

式中：

 $ C_{1} $  ——电压极差判定条件，0:不符合；1:符合；

 $ C_{2} $  ——最大电压最小电压物理位置相邻判定条件，0：不符合；1：符合；

 $ C_{3} $  ——最高电压离群值与最低电压离群值相仿判定条件，0：不符合；1：符合；

dV ——电压极差,单位为伏特(V);

 $ dV_{T} $  ——电压极差预警阈值，由企业自行制定，宜设置为0.5 V，单位为伏特(V)；

 $ \operatorname{loc}_{V_{\operatorname{max}}} $  ——电压最大值物理位置，单位为伏特(V)；

 $ loc_{Vmin} $  ——电压最小值物理位置，单位为伏特(V)；

 $ V_{max} $  ——电压最大值,单位为伏特(V);

 $ V_{min} $  ——电压最小值，单位为伏特(V)；

 $ V_{mid} $  ——电压中位数，单位为伏特(V)；

a ——电压离群常数，宜大于0.7且小于0.95；

R ——算法预警结果，0: 正常；1: 异常。

### C.11 久置过放

利用新能源汽车运行安全平台数据进行计算。

a）过放预警：通过制造商提供的产品自放电速率与最后时刻荷电状态，计算电池允许静置时长。当电池系统允许静置时长低于设定的阈值，且已经持续1 d处于下电状态，则触发久置过放预警。

具体计算步骤按公式 $  \text{(C.21)}  $ 和公式 $  \text{(C.22)}  $ ：

 $$ t=\frac{FSOC}{SD} $$ 

 $$ R=\left\{\begin{aligned}&1,t\leqslant t_{T}\\ &0,t>t_{T}\end{aligned}\right. $$ 

式中：

t ——电池系统允许静置时长,单位为小时(h);

FSOC——电池系统数据最后时刻的荷电状况；

SD ——制造商提供的产品自放电速率,单位为 SOC 每天(SOC/d);

 $ t_{T} $  ——电池系统允许静置时长预警阈值，由企业自行制定，宜设置为5 d，单位为天(d)；

R ——算法预警结果，0：正常；1：异常。

b) 长时间离线告警：通过数据在线情况，判定车辆离线状态，识别潜在隐患。非私人购买或营运车辆离线时长不超过60 d，私人车辆离线时长不超过90 d，最终输出结果为0：正常；1：异常。

### C.12 长时间聚集停放

利用新能源汽车运行安全平台数据进行计算，具体步骤如下：

a）判断新能源汽车当前车辆状态是否为熄火状态，并计算熄火后停放时间；

b） 获取新能源汽车当前时间和当前 SOC 值；

c) 选取所有停放时间超过 60 d 且 SOC 大于 80% 的车辆，记为车辆集 X，获取车辆集中车辆的位置信息；

d）对于车辆集 X 内每一台目标车辆，计算该车半径  $ 500 \, m $  内的车辆数量，见公式(C.23)～公式(C.25)：

 $$ N_{x}=\left\{\begin{aligned}&1,d_{x}<500\\ &0,d_{x}\geqslant500\end{aligned}\right. $$ 

 $$  Num=\sum_{x=1}^{y}N_{x} $$ 

 $$ R=\left\{\begin{aligned}&1,Num\geqslant Num_{T}\\ &0,Num<Num_{T}\end{aligned}\right. $$ 

式中：

 $ N_{x} $  ——目标车辆与车辆 x 距离是否小于 500 m,0:不符合;1:符合;

 $ d_{x} $  ——通过经纬度位置信息计算出的目标车辆与车辆 x 的距离，单位为米(m)；

Num ——目标车辆 500 m 内停放时间超 60 d 且 SOC 大于 80% 的车辆数；

 $ Num_{T} $  ——目标车辆 500 m 内停放时间超 60 d 且 SOC 大于 80% 的车辆数允许阈值，宜小于或等于 100 辆；

R ——目标车辆的算法预警结果，0: 正常；1: 异常。

# 附录 D

(资料性)

# 新能源汽车运行安全性能动态预警措施

### D.1 故障处置措施

新能源汽车运行安全性能故障处置措施见表D.1。

<div style="text-align: center;">表 D.1 故障处置措施</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>通知条件</td><td style='text-align: center;'>通知对象和方式</td><td style='text-align: center;'>处置建议</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>发生1级运行安全故障</td><td style='text-align: center;'>通过车载终端向车辆发送故障信息或向车辆所有者手机推送故障信息及处置建议</td><td style='text-align: center;'>7d内检修处理</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>发生2级运行安全故障</td><td style='text-align: center;'>通过车载终端向车辆发送故障信息或向车辆所有者手机推送故障信息及处置建议</td><td style='text-align: center;'>1d内检修处理</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>发生3级运行安全故障</td><td style='text-align: center;'>通过车载终端向车辆发送故障信息或向车辆所有者手机推送故障信息及处置建议</td><td style='text-align: center;'>停车、熄火立即检修处理</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>同一车型车辆在统计周期内（如1年）出现3级运行安全故障的车辆数占该车型在用车辆数的5%以上</td><td style='text-align: center;'>通过电话、电子邮件等方式向车辆生产企业相关负责人发出故障信息及处置建议</td><td style='text-align: center;'>对同批次产品进行质量核查</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>其他需要预警的情形</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td colspan="4">注：“—”部分由企业自定义。</td></tr></table>

### D.2 隐患告警措施

新能源汽车运行安全性能隐患告警措施见表D.2。

<div style="text-align: center;">表 D.2 隐患告警措施</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>告警条件</td><td style='text-align: center;'>告警对象和方式</td><td style='text-align: center;'>处置建议</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>24 h 内出现 1 次运行安全隐患</td><td style='text-align: center;'>向车辆所有者手机推送隐患信息及处置建议</td><td style='text-align: center;'>7 d 内维护处理</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>24 h 内出现 2 次及以上运行安全隐患</td><td style='text-align: center;'>向车辆所有者手机推送隐患信息及处置建议</td><td style='text-align: center;'>1 d 内维护处理</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>同一车型车辆在统计周期内（如 1 年）出现运行安全隐患的车辆数占该车型在用车辆数的 10% 以上</td><td style='text-align: center;'>通过电话、电子邮件等方式向车辆生产企业相关负责人发出隐患信息及处置建议</td><td style='text-align: center;'>对同批次产品进行质量核查</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>其他需要预警的情形</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td colspan="4">注：“—”部分由企业自定义。</td></tr></table>

## 参 考 文 献

[1] GB 18384—2020 电动汽车安全要求

[2] GB/T 31486—2015 电动汽车用动力蓄电池电性能要求及试验方法

[3] GB/T 32960.1—2016 电动汽车远程服务与管理系统技术规范 第1部分：总则

[4] GB/T 44500 新能源汽车运行安全性能检验规程

[5] 关于进一步加强新能源汽车企业安全体系建设的指导意见(工信厅联通装 $$ 2022 $$ 10号)