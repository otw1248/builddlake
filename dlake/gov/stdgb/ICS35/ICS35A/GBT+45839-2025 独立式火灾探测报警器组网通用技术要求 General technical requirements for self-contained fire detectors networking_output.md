

# 中华人民共和国国家标准

GB/T 45839—2025

# 独立式火灾探测报警器组网通用技术要求

# General technical requirements for networking of self-contained fire detection and alarm devices

2025-05-30 发布

2026-06-01 实施



## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 分类 …… 2  
  
5 要求 …… 2  
  
5.1 通则 …… 2  
  
5.2 外观 …… 3  
  
5.3 收发装置 …… 3  
  
5.4 火灾报警功能 …… 3  
  
5.5 故障报警功能 …… 3  
  
5.6 无线通信功能 …… 4  
  
5.7 电源性能 …… 4  
  
5.8 平台通用性能 …… 4  
  
5.9 现场端平台 …… 5  
  
5.10 生产者远端管理平台 …… 5  
  
5.11 中心级远端管理平台 …… 6  
  
5.12 移动端软件 …… 6  
  
5.13 绝缘电阻 …… 6  
  
5.14 电气强度 …… 6  
  
5.15 电磁兼容性能 …… 7  
  
附录 A（规范性） 组网架构 …… 8  
  
附录 B（规范性） 身份标识码 …… 9  
  
附录 C（规范性） 无线测试试验 …… 11  
  
附录 D（规范性） 现场端平台、远端管理平台 HTTPS API 数据传输格式 …… 13



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由国家消防救援局提出。

本文件由全国消防标准化技术委员会(SAC/TC 113)归口。

本文件起草单位：应急管理部沈阳消防研究所、辽宁省消防救援总队、电子科技大学、青鸟消防股份有限公司、深圳市泰和安科技有限公司、中消联（深圳）智慧消防创新科技有限公司、青岛鼎信通讯消防安全有限公司、西安盛赛尔电子有限公司、北京利达华信电子股份有限公司、山东龙成消防科技股份有限公司。

本文件主要起草人：丁宏军、李宁宁、张颖琮、王力、梅志斌、王卓甫、林强、曹振、郭金龙、金丹丹、李小白、邵宇、王勇俞、解梅、蔡为民、陈宇弘、杜景钦、王建华、张雄飞、陈洪颖、崔庆海。



# 独立式火灾探测报警器组网通用技术要求

## 1 范围

本文件规定了独立式火灾探测报警器联网系统的分类和要求。

本文件适用于独立式火灾探测报警器联网系统的组网建设和运行。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB 4717 火灾报警控制器

GB 14287.2 电气火灾监控系统 第2部分：剩余电流式电气火灾监控探测器

GB 14287.3 电气火灾监控系统 第3部分：测温式电气火灾监控探测器

GB 14287.4 电气火灾监控系统 第4部分：故障电弧探测器

GB 15322.1 可燃气体探测器 第1部分：工业及商业用途点型可燃气体探测器

GB 15322.2 可燃气体探测器 第 2 部分: 家用可燃气体探测器

GB 19880 手动火灾报警按钮

GB 20517 独立式感烟火灾探测报警器

GB 22370 家用火灾安全系统

GB 26851 火灾声和/或光警报器

GB 30122 独立式感温火灾探测报警器

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

独立式火灾探测报警器联网系统 networking of self-contained fire detection and alarm devices

由独立式火灾探测报警器、手动火灾报警按钮、收发装置、火灾声和/或光警报器、扬声器/广播等现场设备，以及家用火灾安全系统、现场端平台和远端管理平台等全部或部分通过无线通信联接方式组成的火灾监测预警系统。

注：独立式火灾探测报警器包括独立式感烟火灾探测报警器、独立式感温火灾探测报警器、独立式可燃气体探测器、家用可燃气体探测器、独立式电气火灾监控探测器等。

### 3.2 

## 报警触发器件 alarm trigger device

通过感知监视对象与火灾及火灾风险相关的物理或化学现象的变化，向平台传送报警信号的装置。 $ ^{*} $ 注：报警触发器件包括独立式火灾探测报警器、手动火灾报警按钮等。

### 3.3 

## 现场端平台 on-site platform

在现场保护区域直接或间接接收和处理各设备相关信息，并具有发出火灾警报信号等独立控制输

出功能的管理终端。

注：现场端平台能用火灾报警控制器、控制中心监控设备替代。

### 3.4 

## 远端管理平台 remote management platform

在非现场保护区域接收和处理独立式火灾探测报警器联网系统相关信息，并进行综合管理的终端。

注：远端管理平台包括生产者远端管理平台和中心级远端管理平台。

### 3.5 

生产者远端管理平台 remote management platform for manufacturer

在非现场保护区域生产者用于对其生产的独立式火灾探测报警器联网系统产品进行管理的终端。

### 3.6 

中心级远端管理平台 remote management platform for management authority

在非现场保护区域管理机构对独立式火灾探测报警器联网系统进行管理的终端。

### 3.7 

## 收发装置 collection and transmission device

在独立式火灾探测报警器联网系统中用于收集并转发现场保护区域报警触发器件（或家用火灾安全系统）、火灾声和/或光警报器、扬声器/广播信息的设备。

### 3.8 

身份标识码 identification code; ID

独立式火灾探测报警器联网系统中每个设备的唯一身份识别码。

## 4 分类

4.1 独立式火灾探测报警器联网系统（以下简称“系统”）按组网架构（按附录 A 的要求）分为：

a）直接接入型：各现场设备不通过收发装置与现场端平台通信联接；

b）汇总接入型：各现场设备通过收发装置与现场端平台通信联接。

4.2 系统的现场设备按供电方式可分为：

a）仅内部电池供电型；

b) 仅外部电源供电型；

c） 外部电源供电且配有内部电池型。

注：仅外部电源供电型仅限于独立式可燃气体探测器、家用可燃气体探测器和独立式电气火灾监控探测器。

## 5 要求

### 5.1 通则

5.1.1 独立式火灾探测报警器与外部组网连接线开路、短路或组网功能失效时，不应影响自身的报警功能。

5.1.2 系统的各类设备应符合下述要求：

a）独立式感烟火灾探测报警器符合 GB 20517 的要求；

b) 独立式感温火灾探测报警器符合 GB 30122 的要求；

c) 独立式工业及商业用途点型可燃气体探测器符合 GB 15322.1 的要求，家用可燃气体探测器符合 GB 15322.2 的要求；

d）独立式剩余电流式电气火灾监控探测器符合 GB 14287.2 的要求，独立式测温式电气火灾监控探测器应符合 GB 14287.3 的要求，独立式故障电弧探测器符合 GB 14287.4 的要求；

e）手动火灾报警按钮符合 GB 19880 的要求；

f）火灾声和/或光警报器符合 GB 26851 的要求；

g） 家用火灾安全系统符合 GB 22370 的要求。

5.1.3 系统应有授时功能。

5.1.4 独立式火灾探测报警器组网系统可根据使用需求选择组网方式及网络类型。

### 5.2 外观

系统的各类设备表面应无腐蚀、涂覆层脱落和起泡现象，无明显划伤、裂痕、毛刺等机械损伤，各类设备紧固部位无松动。

### 5.3 收发装置

5.3.1 收发装置的接收与转发节点数不宜超过 200 点，超过 200 点应按照生产者标称点数检验。

5.3.2 收发装置应采用外部电源供电且配有内部电池型供电方式，并应设有正常工作状态、故障状态、外部电源供电正常状态、外部电源供电故障状态、内部电池供电正常状态、内部电池供电故障状态指示灯。正常工作状态指示、外部电源供电正常状态指示、内部电池供电正常状态指示应为绿色，故障状态指示、外部电源供电故障状态指示、内部电池供电故障状态指示应为黄色。

5.3.3 收发装置应能记录并存储其所联接的全部报警触发器件的报警和故障信息、火灾声和/或光警报器或扬声器/广播的工作状态信息、故障及控制输出信息，及对应的年、月、日、时、分、秒等时间信息，并应具有按照时间顺序导出记录信息的功能，收发装置应能记录至少999条信息。

### 5.4 火灾报警功能

5.4.1 系统的每只报警触发器件和家用火灾安全系统应在 30 s 内将其火灾报警信号传输给现场端平台。现场端平台与远端管理平台之间的报警信息传送时间应小于 10 s。

5.4.2 现场端平台应能接收系统的所有报警触发器件和家用火灾安全系统发出的火灾报警信号，并发出火灾报警声、光信号，指示报警部位，并予以保持，直至现场端平台手动复位。报警声信号应能手动消除，当再次有报警信号输入时，应能再启动。

5.4.3 系统应能在 60 s 内接收不少于 20 个独立的火灾报警信号。收发装置接收与转发节点数大于 200 点时，系统应能在 60 s 内接收不少于生产者标称点数 10% 的独立火灾报警信号。

5.4.4 系统的独立式火灾探测报警器的报警声信号除应在其设置的保护部位消音外，可通过现场端平台或远端管理平台由业主授权的注册用户进行消音，并应保存消音操作记录。

### 5.5 故障报警功能

5.5.1 当发生以下故障时，现场端平台应在 100 s 内发出与火灾报警信号有明显区别的故障声、光信号，并显示故障部位。故障声信号应能手动消除，再有故障信号输入时，应能再启动；故障光信号应保持至故障排除。

a）报警触发器件主体部分自身故障。

b）报警触发器件主体脱离底座。

c）报警触发器件主体部分与无线传输部分失联故障（报警触发器件主体部分与无线传输部分为分离结构时适用）。

d）不影响正常通信的外部电源或内部电池供电故障。

e） 收发装置与现场端平台之间的通信故障。

5.5.2 直接接入型系统的报警触发器件、火灾声和/或光警报器、扬声器/广播与现场端平台之间发生通信故障时，汇总接入型系统的报警触发器件、火灾声和/或光警报器、扬声器/广播与收发装置之间发

生通信故障时，现场端平台应在24 h内发出与火灾报警声光信号有明显区别的故障声、光信号，并显示故障部位。故障声信号应能手动消除，再有故障信号输入时，应能再启动；故障光信号应保持至故障排除。

5.5.3 现场端平台与远端管理平台之间的故障信息传送时间应小于 10 s。

5.5.4 现场端平台应能显示所有故障信息，在不能同时显示所有故障信息时，未显示的故障信息应手动可查。

5.5.5 系统中任一故障均不应影响非故障部分的正常工作。

### 5.6 无线通信功能

5.6.1 系统的各设备应具有唯一的经授权的身份标识码，编码方式应符合附录 B 的规定。

5.6.2 系统的设备之间采用授权频谱的蜂窝无线网络传输信息时，应具有加密措施。

5.6.3 采用自建无线通信网络的设备应在满足生产者组建的网络环境下正常通信。

5.6.4 采用授权频谱的蜂窝无线网络的设备应符合以下要求：

a）在生产者标称的网络环境下正常通信；

b）具有自动搜索可用小区进行通信的功能。

5.6.5 系统中采用无线方式通信的设备应具有无线通信信号质量监测功能，网络信号质量满足 5.6.3 及 5.6.4 的要求，当设备通电时应上报 1 次，正常监视状态下应至少 24 h 上报 1 次。

5.6.6 5.6.1～5.6.5 规定的无线通信功能应按照附录 C 的要求进行无线测试试验。

### 5.7 电源性能

5.7.1 对于系统中采用仅内部电池供电型供电方式的设备，其电源性能应符合以下要求：

a）设备持续工作时间符合生产者标称指标要求，且不低于相应产品标准的规定；

b）设备具有电池电压的检测功能，在设备通电后，首先检测电池电压，且电池电压的检测周期不应大于24 h。

5.7.2 火灾声和/或光警报器、收发装置、现场端平台和扬声器/广播应采用外部电源供电且配有内部电池型的供电方式，其电源性能应符合以下要求。

a）电源部分具有外部电源供电和内部电池供电转换的功能；当外部电源断电或不能保证正常供电时，自动转换到内部电池供电；当外部电源恢复后，自动转换到外部电源供电；设备有外部电源和内部电池供电状态指示，且外部电源与内部电池供电的转换不影响设备正常工作。

b）内部电池的容量保证设备正常监视状态工作8 h后，火灾声和/或光警报器、扬声器/广播发出报警信号至少保持30 min，收发装置、现场端平台在10只报警器处于火灾报警状态下至少工作30 min。

c）内部电池具有充电功能时，内部电池在放电至终止电压条件下，充电24 h，其容量可保证声和/或光警报器、收发装置、现场端平台和扬声器/广播的工作时间满足b)的要求。

d）内部电池电压达到设定的欠压阈值时，设备向平台发出欠压故障信号。

### 5.8 平台通用性能

5.8.1 具有可对独立式火灾探测报警器实施消音功能的现场端平台或远端管理平台应具有对授权用户进行注册和分类管理的功能，且在满足下述条件之一时，方可实施消音操作，平台应保存下述信息和消音操作：

a）发出火灾报警信号的独立式火灾探测报警器显示的烟或其他参数特性未达到设定的报警条件；

b）同一探测区内视频信号明确显示未发生火灾；

c）注册用户授权人明确确认未发生火灾。

5.8.2 应具有中文信息显示功能，并满足以下显示与记录要求。

a）运行统计信息：设备总数、当前在线设备数量、当前火灾报警设备数量、当前故障设备数量。

b）用户资料信息：保护单位及区域信息、设备信息、消防责任人联系信息。

c) 当前火灾报警指示: 当设备处于火灾报警状态时, 指示并记录火灾报警类型、位置和时间信息且记录不受复位影响。平台具有记录报警原因及处理结果功能。

d）故障指示：当设备处于故障状态时，指示并记录故障类型、位置和时间信息且记录不受复位影响。

e）设备地址注释信息：显示现场设备和收发装置安装地址、场所、房间及具体设置部位。

f) 运维监测：平台宜具有设备异常耗电、无线网络信号质量降低、服务器 CPU/内存/网络资源占用率监测功能。

5.8.3 应具有数据存储功能。

5.8.4 应具有区分调试、检测、维保等状态下各类信息与正常运行状态下各类信息的功能。

### 5.9 现场端平台

5.9.1 对于系统连接的火灾声和/或光警报器、扬声器/广播等设备，现场端平台应能通过手动或控制程序方式进行启动，且在接收到满足规定逻辑关系的火灾报警信号后，应能在10 s内自动启动至少10只上述设备（不足10只时，全部启动）。

5.9.2 应具有操作日志记录功能，并对所有的操作进行记录。

5.9.3 当使用视频监控系统时，如发生火灾报警，现场端平台应能联动视频监控系统，获取相关监控画面进行火警确认。

5.9.4 应具有与远端管理平台进行信息交互的功能，并应能直接或间接将相关信息发送给业主或必要的相关责任人；应具有接收报警事件现场核实信息的功能，确认火灾后应按灭火和应急救援预案自动向相关人员推送火警信息。

5.9.5 未接入远端管理平台的现场端平台对火灾报警、故障、操作日志等历史数据的存储时间不应少于1年，接入远端管理平台时不应少于30 d。

### 5.10 生产者远端管理平台

5.10.1 信息记录功能还应能记录以下信息：设备出厂日期、火灾报警处理的进程、火灾报警处理的操作人、故障处理的进程、故障处理的结果、故障处理的操作人。

5.10.2 应支持各类信息的分类统计、分区域统计及指定类型的统计，并同时具备列表及图形方式展现，应支持管理效率的统计功能（例如：处警间隔时差、故障响应及恢复间隔时长等）。

5.10.3 应支持通过超文本传输安全协议应用程序接口(HTTPS API)与上下级平台进行信息交互共享,数据传输格式应符合附录 D 的要求。

5.10.4 通知的信息类型应至少包括火灾报警信息、故障信息、火警解除信息、故障恢复信息、设备报废信息。信息内容应含信息类型、上报时间、上报设备的位置。在收到火灾报警信息后，应能在15 s内自动将信息推送给相关人员，推送消息形式至少包含两种类型但不局限于短信、电话、移动端软件推送消息等。

5.10.5 未连接中心级管理平台时，产品信息应在其生命周期内予以保存，接入中心级管理平台时产品信息保存时间不少于1年。

5.10.6 应可使用管理员权限分配不同权限至相关人员，授予设备增删改查等不同的权限、推送接收消息的权限以及报警记录处理与查看等相应权限。

5.10.7 应将相应人员按照组织架构建立上下级关系，并且与被保护单位、设备进行关联。应可配置设

备地址与序号、设备安装位置、设备出厂日期、被保护单位名称、被保护单位地址。

### 5.11 中心级远端管理平台

5.11.1 信息记录、信息统计和信息传输功能应分别满足 5.10.1～5.10.3 的要求。

5.11.2 应在产品的生命周期内保存产品的相关信息。

5.11.3 应具有表单的上传和下载功能。

5.11.4 应具有查询设施状态的功能，并应具有通过基础数据对系统进行完好有效性分析的功能。

5.11.5 应具有主数据、基础模型以及应用业务数据同步功能，支持上述数据的查看与集成。

5.11.6 应具有业务证书生成与发布功能。

5.11.7 应具有鉴权功能，相关机构或用户登录平台后按平台划分的权限实现相应功能的访问。

### 5.12 移动端软件

5.12.1 应按照人员相应权限账号进行登录，角色权限应含但不局限于物业管理人员端、维保人员端、业主端。

5.12.2 物业管理人员端应符合以下要求。

a）信息查看：能查看并统计本单位所有的设备状态、火灾报警信息、故障信息、火警处理信息、故障恢复信息、设备报废信息等。

b) 信息处理：支持相应人员对火灾报警信息进行接收与处理，处理后上传图文描述，处理过程上传管理平台进行存储。处理结果如为火警，应按灭火和应急救援预案自动向相关人员推送火警信息；处理结果如为误报，应通过现场端平台手动复位；处理结果如为故障，平台自动生成该设备的故障信息转发至维保人员端。

c）信息接收：能接收相应平台推送的火灾报警信息、故障信息、故障恢复信息、设备报废信息。

5.12.3 维保人员端应符合以下要求。

a）信息查看：可查看设备的状态、故障信息、故障恢复信息、设备报废信息、处理超时信息。

b）信息处理：支持相应维保人员对设备故障信息进行接收，处理完成后上传图文描述；支持配置设备地址、设备安装位置、被保护单位名称、被保护单位地址、责任人姓名与电话；支持输入设备ID或通过扫描二维码、近场通信(NFC)标签的形式对设备与单位进行关联。

c）信息接收：能接收相应平台推送的故障信息、故障恢复信息、设备报废信息、工作超时信息。

5.12.4 业主端应可查看并统计本场所所有的设备状态、火灾报警信息、故障信息、火警处理信息、故障恢复信息、设备报废信息等，应能接收相应平台推送的火灾报警信息、故障信息、故障恢复信息、设备报废信息。

5.12.5 移动端与各平台之间的传输时间应小于5 s。

### 5.13 绝缘电阻

现场端平台和收发装置的外部带电端子和电源端子的工作电压大于50 V时，外部带电端子和电源端子与外壳间的绝缘电阻在正常大气条件下不应小于100 MΩ。

### 5.14 电气强度

现场端平台和收发装置的外部带电端子和电源端子的工作电压大于50 V时，外部带电端子和电源端子与机壳间应能耐受频率为50 Hz、有效值电压为1250 V的交流电压，历时60 s的电气强度试验。试验期间，现场端平台和收发装置不应发生击穿现象（击穿报警预置电流为20 mA）。试验后，现场端平台和收发装置功能应满足5.4.2和5.5.1的要求。

### 5.15 电磁兼容性能

现场端平台和收发装置应能耐受表1所规定的电磁干扰条件下的各项试验，试验期间及试验后应满足下述要求：

a）试验期间，现场端平台和收发装置保持正常监视状态；

b）试验后，现场端平台和收发装置功能满足5.4.2和5.5.1的要求。

<div style="text-align: center;">表 1 电磁干扰条件</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>试验名称</td><td style='text-align: center;'>试验参数</td><td style='text-align: center;'>试验条件</td><td style='text-align: center;'>工作状态</td></tr><tr><td rowspan="4">射频电磁场辐射抗扰度试验</td><td style='text-align: center;'>场强/(V/m)</td><td style='text-align: center;'>10</td><td rowspan="4">正常监视状态</td></tr><tr><td style='text-align: center;'>频率范围/MHz</td><td style='text-align: center;'>80～1000</td></tr><tr><td style='text-align: center;'>扫频步长</td><td style='text-align: center;'>不超过前一频率的1%</td></tr><tr><td style='text-align: center;'>调制幅度</td><td style='text-align: center;'>80%(1 kHz,正弦)</td></tr><tr><td rowspan="3">射频场感应的传导骚扰抗扰度试验</td><td style='text-align: center;'>频率范围/MHz</td><td style='text-align: center;'>0.15～80</td><td rowspan="3">正常监视状态</td></tr><tr><td style='text-align: center;'>电压/dBμV</td><td style='text-align: center;'>140</td></tr><tr><td style='text-align: center;'>调制幅度</td><td style='text-align: center;'>80%(1 kHz,正弦)</td></tr><tr><td rowspan="4">静电放电抗扰度试验</td><td style='text-align: center;'>放电电压/kV</td><td style='text-align: center;'>空气放电(绝缘体外壳):8接触放电(导体外壳和耦合板):6</td><td rowspan="4">正常监视状态</td></tr><tr><td style='text-align: center;'>放电极性</td><td style='text-align: center;'>正、负</td></tr><tr><td style='text-align: center;'>放电间隔/s</td><td style='text-align: center;'>≥1</td></tr><tr><td style='text-align: center;'>每点放电次数</td><td style='text-align: center;'>10</td></tr><tr><td rowspan="5">电快速瞬变脉冲群抗扰度试验</td><td style='text-align: center;'>瞬变脉冲电压/kV</td><td style='text-align: center;'>AC电源线:2×(1±0.1)其他连接线:1×(1±0.1)</td><td rowspan="5">正常监视状态</td></tr><tr><td style='text-align: center;'>重复频率/kHz</td><td style='text-align: center;'>5×(1±0.2)</td></tr><tr><td style='text-align: center;'>极性</td><td style='text-align: center;'>正、负</td></tr><tr><td style='text-align: center;'>时间</td><td style='text-align: center;'>每次1 min</td></tr><tr><td style='text-align: center;'>施加次数</td><td style='text-align: center;'>3</td></tr><tr><td rowspan="4">浪涌(冲击)抗扰度试验</td><td style='text-align: center;'>浪涌(冲击)电压/kV</td><td style='text-align: center;'>AC电源线:线-线1×(1±0.1)AC电源线:线-地2×(1±0.1)其他连接线:线-地1×(1±0.1)其他连接线:线-线0.5×(1±0.1)</td><td rowspan="4">正常监视状态</td></tr><tr><td style='text-align: center;'>极性</td><td style='text-align: center;'>正、负</td></tr><tr><td style='text-align: center;'>试验次数</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>试验间隔/s</td><td style='text-align: center;'>60</td></tr></table>

附录 A

(规范性)

组网架构

系统的组网架构见图 A.1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_125_383_1047_1054.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 A.1 系统的组网架构</div>


注 $ ^{1} $ ：虚线框标注为可选项。

注 $ ^{2} $ ：现场设备设置有收发装置时为汇总接入型，未设置收发装置时为直接接入型。

## 附录 B

(规范性)

身份标识码

### B.1 要求

B.1.1 身份标识码(ID)由多个字段组成，总计27字节。

B.1.2 有效的 ID 格式见表 B.1。

<div style="text-align: center;">表 B.1 有效的 ID 格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>CD</td><td style='text-align: center;'>NT</td><td style='text-align: center;'>PD</td><td style='text-align: center;'>SN</td><td style='text-align: center;'>TAC</td><td style='text-align: center;'>CHK</td></tr><tr><td style='text-align: center;'>公司代码(Company Code)</td><td style='text-align: center;'>传输及网络类型(Network Type)</td><td style='text-align: center;'>生产日期(Production Date)</td><td style='text-align: center;'>序列号(Serial Number)</td><td style='text-align: center;'>类型分配码(Type Allocation Code)</td><td style='text-align: center;'>校验码(Check Code)</td></tr><tr><td style='text-align: center;'>4 字节</td><td style='text-align: center;'>2 字节</td><td style='text-align: center;'>6 字节</td><td style='text-align: center;'>9 字节</td><td style='text-align: center;'>2 字节</td><td style='text-align: center;'>4 字节</td></tr></table>

### B.2 编码格式

ID 的编码格式如下。

a）公司代码(CD)为4字节，每字节编码格式为 ASCII 码“0”～“9”及“A”～“Z”，由消防管理部门统一分配，各设备生产者分别对应一个特定编号。

b) 传输及网络类型(NT)为2字节，每字节编码格式为ASCII码“0”～“9”及“A”～“Z”，由消防管理部门统一分配，标明该设备基于何种通信方式传输数据；NT码对应的通信方式如表B.2所示，对于表B.2中未规定的网络类型，由消防管理部门分配新码。

<div style="text-align: center;">表 B.2 网络类型码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编码</td><td style='text-align: center;'>传输及网络类型</td></tr><tr><td style='text-align: center;'>00</td><td style='text-align: center;'>有线</td></tr><tr><td style='text-align: center;'>01</td><td style='text-align: center;'>NB-IoT</td></tr><tr><td style='text-align: center;'>02</td><td style='text-align: center;'>CAT.1</td></tr><tr><td style='text-align: center;'>03</td><td style='text-align: center;'>Wi-Fi</td></tr><tr><td style='text-align: center;'>04</td><td style='text-align: center;'>LoRa</td></tr><tr><td style='text-align: center;'>05</td><td style='text-align: center;'>ZigBee</td></tr><tr><td style='text-align: center;'>06～ZZ</td><td style='text-align: center;'>预留</td></tr></table>

c) 生产日期(PD)为6字节，每字节编码格式为 ASCII 码“0”~“9”，由设备生产者标识，标明该设备的生产日期，按年、月、日顺序编写，格式为“yymmdd”。

d）序列号(SN)为9字节，每字节编码格式为 ASCII 码“0”~“9”及“A”~“Z”，由设备生产者标识，区分设备同一生产厂内同一流水线的产品序列号。

e）类型码(TAC)为uint类型，长度2字节，取值范围是：0～65535，由设备生产者标识，区分设备

类型方法应符合 GB 4717 的要求。

f) 校验码(CHK)为4字节，每个字节的编码格式为 ASCII 码“0”～“9”及“A”～“F”，由公钥、私钥、CD、NT、PD、SN、TAC 通过校验算法计算出的十六进制校验码，转为 ASCII 码保存。公钥、私钥和校验算法由消防管理部门统一制定和发放。

附录 C

(规范性)

无线测试试验

### C.1 系统试验环境

无线测试试验环境见图 C.1，用于进行火灾报警功能、故障报警功能以及电池使用时间试验等测试。

<div style="text-align: center;"><img src="imgs/img_in_image_box_316_477_890_805.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">图 C.1 无线测试试验环境</div>


### C.2 试样与程序

#### C.2.1 自建网络系统试样

按图 C.1 配置系统，生产者应提供 2 台收发装置，A 信号和 B 信号分别配置为收发装置 1 和收发装置 2 的信号。收发装置所配备的设备点数按生产者标称的最大点数配置，设备类型按生产者标称的配备。试验前生产者应提供配套的现场端平台登录账号信息和软件设备 1 台、配套的远端管理平台登录账号信息和软件设备 1 台（如适用），以及各级移动端软件设备 2 台（如适用）。

#### C.2.2 授权频谱蜂窝网络系统试样

按图 C.1 配置系统，测试环境将提供 2 个蜂窝基站信号，A 信号和 B 信号分别配置为蜂窝基站 1 和蜂窝基站 2 的信号。系统应包含 20 只设备，设备类型按生产者标称的配备。试验前生产者应提供配套的现场端平台登录账号信息和软件设备 1 台、配套的远端管理平台登录账号信息和软件设备 1 台（如适用），以及各级移动端软件设备 2 台（如适用）。

### C.3 身份标识码检验

使系统处于正常运行状态，按附录 D 的格式，通过现场端平台读取解析设备 ID，检查 ID 各字节与附录 B 规定编码格式的一致性。按附录 B 要求校验 ID 是否为消防管理部门统一制定和发放。

### C.4 数据加密验证试验

使系统处于正常监视状态，抓取现场端平台与系统的各类设备之间的网络通信数据，抓取远端管理平台与系统的各类设备之间的网络通信数据（如适用），检查数据是否明文传输。

### C.5 自建网络系统通信试验

C.5.1 使系统设备处于生产者标称的网络环境，记录试验时的网络参数状态。

C.5.2 在一台收发装置配接的设备中，同步模拟产生生产者标称的收发装置最大配接设备数的10%的火灾报警信号，收发装置最大配接设备数少于200点的，按20点同步模拟火灾报警信号，其中第一个火灾报警信号指示情况应满足5.4.1和5.4.2的要求，其他火灾报警信号指示情况应满足5.4.3的要求，系统内如有火灾声和/或光警报器、扬声器/广播等设备，其启动时间和启动数量应满足5.9.2的要求。

C.5.3 在两台收发装置配接的设备中，同时实施 C.5.2 中的试验内容，要求每个收发装置配接设备的第一个火灾报警信号指示情况应满足 5.4.1 和 5.4.2 的要求，其他火灾报警信号指示情况应满足 5.4.3 的要求，系统内如有火灾声和/或光警报器、扬声器/广播等设备，其启动时间和启动数量应满足 5.9.2 的要求。

C.5.4 分别通过消音按钮、现场端或远端管理平台业主授权注册用户账户、现场端平台或远端管理平台业主未授权注册用户账户，进行消音操作，消音功能应满足5.4.4的要求。

C.5.5 在不同种类设备中各抽选1只设备，对每只设备依次模拟5.5.1和5.5.2中设备对应故障种类，观察记录系统中现场端平台、远端管理平台（如适用）以及移动端（如适用）的指示与记录情况，应满足5.5.1和5.5.2的要求。

### C.6 授权频谱蜂窝网络系统通信试验

C.6.1 使系统设备处于生产者标称的网络环境，记录试验时的网络参数状态。

C.6.2 同步模拟产生 20 个火灾报警信号，第一个火灾报警信号指示情况应满足 5.4.1 和 5.4.2 的要求，其他火灾报警信号指示情况应满足 5.4.3 的要求，系统内如有火灾声和/或光警报器、扬声器/广播等设备，其启动时间和启动数量应满足 5.9.1 的要求。

C.6.3 分别通过消音按钮、现场端平台或远端管理平台业主授权注册用户账户、现场端平台或远端管理平台业主未授权注册用户，进行消音操作，消音功能应满足5.4.4的要求。

C.6.4 在不同种类设备中各抽选1只设备，对每只设备依次模拟5.5.1和5.5.2中设备对应故障种类，观察记录系统中现场端平台、远端管理平台（如适用）以及移动端（如适用）的指示与记录情况，应满足5.5.1和5.5.2的要求。

C.6.5 建立两个小区，使设备处于两个小区覆盖范围内，使设备向现场端平台发送数据，检查通信数据是否具有自动重选小区的能力。

### C.7 网络状态监测功能试验

使系统处于正常监视状态，通过现场端平台或远端管理平台（如适用）检查所有设备上电联网注册完成后是否有信号强度、信噪比（如适用）、小区信息（如适用）等网络质量状态监测信息记录，之后保持系统正常运行48 h，每24 h通过现场端平台或远端管理平台（如适用）检查所有设备的网络质量状态监测信息记录是否满足5.6.5的要求，试验期间系统不应发生故障。

附录 D

(规范性)

现场端平台、远端管理平台 HTTPS API 数据传输格式

D.1 现场端平台、远端管理平台 HTTPS API 设备基础信息数据交换传输格式见表 D.1。

<div style="text-align: center;">表 D.1 设备基础信息数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口名称</td><td style='text-align: center;'>接口作用</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>数据项</td><td style='text-align: center;'>数据项含义</td><td style='text-align: center;'>数据项类型</td><td style='text-align: center;'>数据内容</td></tr><tr><td rowspan="18">Install_info</td><td rowspan="18">上报设备安装位置、被保护单位等信息</td><td rowspan="16">Json对象</td><td style='text-align: center;'>company</td><td style='text-align: center;'>生产厂商</td><td style='text-align: center;'>string</td><td rowspan="16"></td></tr><tr><td style='text-align: center;'>serial</td><td style='text-align: center;'>设备身份识别码ID</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>name</td><td style='text-align: center;'>设备名称</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>categoryName</td><td style='text-align: center;'>设备类型</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>netType</td><td style='text-align: center;'>网络通信方式</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>client</td><td style='text-align: center;'>被保护单位名称</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>address</td><td style='text-align: center;'>被保护单位地址</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>deviceAddress</td><td style='text-align: center;'>设备安装地址</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>productingDate</td><td style='text-align: center;'>出厂日期</td><td style='text-align: center;'>date</td></tr><tr><td style='text-align: center;'>longitude</td><td style='text-align: center;'>经度</td><td style='text-align: center;'>number</td></tr><tr><td style='text-align: center;'>latitude</td><td style='text-align: center;'>纬度</td><td style='text-align: center;'>number</td></tr><tr><td style='text-align: center;'>activeTime</td><td style='text-align: center;'>激活时间</td><td style='text-align: center;'>dateTime</td></tr><tr><td style='text-align: center;'>organizationName</td><td style='text-align: center;'>设备所属组织机构名称</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>area</td><td style='text-align: center;'>设备所属区域的行政区域代码</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>responsible</td><td style='text-align: center;'>负责人姓名</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>mobile</td><td style='text-align: center;'>联系电话</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>输出</td><td style='text-align: center;'>数据项</td><td style='text-align: center;'>数据项含义</td><td style='text-align: center;'>数据项类型</td><td style='text-align: center;'>数据内容</td></tr><tr><td style='text-align: center;'>Json对象</td><td style='text-align: center;'>success</td><td style='text-align: center;'>上传是否成功(1表示成功;0表示失败)</td><td style='text-align: center;'>int</td><td style='text-align: center;'>例如：{“success”:1}</td></tr></table>

D.2 现场端平台、远端管理平台 HTTPS API 设备运行状态信息数据交换传输格式见表 D.2。

<div style="text-align: center;">表 D.2 设备运行状态信息数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口名称</td><td style='text-align: center;'>接口作用</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>数据项</td><td style='text-align: center;'>数据项含义</td><td style='text-align: center;'>数据项类型</td><td style='text-align: center;'>数据内容</td></tr><tr><td rowspan="8">status_info</td><td rowspan="8">上报设备运行状态（正常监视、报警/故障、屏蔽）信息</td><td rowspan="6">Json对象</td><td style='text-align: center;'>company</td><td style='text-align: center;'>生产厂商</td><td style='text-align: center;'>string</td><td rowspan="6"></td></tr><tr><td style='text-align: center;'>serial</td><td style='text-align: center;'>设备身份识别码ID</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>status</td><td style='text-align: center;'>运行状态(1:正常监视；2:报警；3:故障；4:屏蔽)</td><td style='text-align: center;'>int</td></tr><tr><td style='text-align: center;'>signalStrength</td><td style='text-align: center;'>信号强度</td><td style='text-align: center;'>int</td></tr><tr><td style='text-align: center;'>batteryPercentage</td><td style='text-align: center;'>剩余电池电量百分比0~100%</td><td style='text-align: center;'>int</td></tr><tr><td style='text-align: center;'>datetime</td><td style='text-align: center;'>时间(2019-06-11 07:25:55)</td><td style='text-align: center;'>string</td></tr><tr><td style='text-align: center;'>输出</td><td style='text-align: center;'>数据项</td><td style='text-align: center;'>数据项含义</td><td style='text-align: center;'>数据项类型</td><td style='text-align: center;'>数据内容</td></tr><tr><td style='text-align: center;'>Json对象</td><td style='text-align: center;'>success</td><td style='text-align: center;'>上传是否成功(1表示成功；0表示失败)</td><td style='text-align: center;'>int</td><td style='text-align: center;'>例如：{“success”:1}</td></tr></table>





