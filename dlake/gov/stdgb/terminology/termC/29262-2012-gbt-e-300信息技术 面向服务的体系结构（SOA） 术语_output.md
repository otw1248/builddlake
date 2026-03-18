

# 中华人民共和国国家标准

GB/T 29262—2012

# 信息技术 面向服务的体系结构(SOA) 术语

# Information technology—Service Oriented Architecture (SOA)—Terminology

2012-12-31 发布

2013-06-01 实施



## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国信息技术标准化技术委员会(SAC/TC 28)提出并归口。

本标准起草单位：中国电子技术标准化研究院、长风开放标准平台软件联盟、东方通科技发展有限公司、上海普元信息技术有限公司、中软国际信息技术有限公司、山东浪潮齐鲁软件产业股份有限公司、北京锐易特软件技术有限公司、中国软件行业协会、北京炎黄盈动科技发展有限责任公司、深圳市金蝶中间件有限公司、同济大学、用友软件股份有限公司、北京大学。

本标准主要起草人：袁媛、高林、耿建光、朱律玮、付东普、钱军、韩鹏、毛国兴、贾德星、李轶强、王钧、刘金柱、滕腾、刘琴、董乃文、李海波、刘贤刚、王潮阳、董建、田忠、刘韙哲。



# 信息技术 面向服务的体系结构(SOA) 术语

## 1 范围

本标准界定了信息技术中面向服务的体系结构领域通用术语及其定义。

本标准适用于面向服务的体系结构的核心概念理解、国内国际间信息交流和科研教学出版。

## 2 术语和定义

### 2.1 

## 体系结构 architecture

系统的组织结构，包括组成元素及各元素之间的关系。

注：改写 GB/T 11457—2006，定义 2.73。

### 2.2 

## 构件 component

软件系统中具有相对独立功能、可以明确辨识、接口由契约指定、和语境有明显依赖关系、可独立部署的可组装软件实体。

[SJ/T 11409—2009, 定义 3.1.1]

### 2.3 

## 功能单元 functional unit

能实现某一特定目标的硬件、软件或两者兼而有之的实体。

[GB/T 11457—2006, 定义 2.670]

### 2.4 

## 信息服务 information service

提供信息采集、编目、发布和检索等功能的服务。

### 2.5 

## I T 基础设施 information-technology infrastructure

SOA 应用运行所必要的基础环境，包括网络、硬件和基础软件等，为 SOA 应用提供可靠、有效的运行环境和信息传输服务通道，保障 SOA 应用的安全、稳定。

### 2.6 

## 服务质量 quality of service: QoS

服务能够满足明确和隐含需求的特征和特性的总和，即在实际条件下使用时，服务提供者提供的服务可满足服务使用者需求的程度。

### 2.7 

## 表示状态转换 representational state transfer: REST

一种用于针对网络应用的设计和开发方式，强调对资源状态的描述以及导致资源状态迁移的一组操作。

注：REST 是实现 SOA 的典型技术之一。

### 2.8 

## 服务 service

通过规范化的描述来表征、对外提供访问地址、并可被重复使用的业务功能单元。

示例：审批服务、客户管理服务、登录注册服务等。

注 $ ^{1} $ ：创建服务的目的是为了供需要使用该服务实现的功能的使用者调用。

注2：每个服务通过规范化的描述来表征，包括接口、操作、语义、动态行为、策略、服务质量等描述。

### 2.9 

## 服务代理 service agent

## 服务中介 service broker

实现了服务信息的统一注册和发布等功能的实体，可为服务提供者及服务使用者提供服务注册、发现、路由及服务的透明访问等支撑功能。

### 2.10 

## 服务总线 service bus

服务接入与消费的中介基础设施，为基本服务提供了基于标准的事件驱动消息路由。其基本功能包括：服务路由、消息转换、事件处理，提供服务调用，及相关中介服务，支持 Web Service 或 JMS 连接，连接各种应用，服务，信息，平台资源。

### 2.11 

## 候选服务 service candidate

在服务建模过程中所产生的预备的服务，这些预备的服务在后续的面向服务的设计阶段还需要被验证、修改或重新定义。

### 2.12 

## 服务目录 service catalog: SC

记录服务提供者所提供服务的全部种类以及服务目标情况，为选择服务、检索服务提供支撑的列表。

### 2.13 

## 服务编排 service choreography

为实现特定业务协作，从系统全局的角度，描述一组（对等）服务之间的公共消息交互过程。

### 2.14 

## 服务构件 service component

具体业务功能的数据和方法的封装，是服务和服务接口的具体技术实现。

### 2.15 

## 服务构件体系结构 service component architecture; SCA

基于服务构件的 SOA 应用和解决方案的编程模型。

### 2.16 

## 服务组合 service composition

将一组服务按照一定的规则进行组合，使它们可以一起共同完成一个特定的任务或业务流程。

注：服务组合的方式一般有服务编制和服务编排两种。

### 2.17 

## 服务消费者 service consumer

服务使用者

使用服务的实体。

### 2.18 

## 服务合约 service contract

关于服务元信息的规格化描述，由一个或多个已发布的描述服务的文档所组成，服务提供者和服务

使用者共同遵循。

注：描述服务的元信息包括服务技术接口、服务质量水平、服务版本等。

### 2.19 

## 服务数据对象 service data object: SDO

为简化针对数据的编程而设计的一个数据编程架构，同时它也是应用程序接口。

### 2.20 

## 服务部署 service deployment

将所开发的各类服务部署至物理环境内，并可以实际运行的过程。

注 $ ^{1} $ ：服务部署包括静态和动态两种。静态部署是指服务之间的调用关系在运行前已确定，动态部署是指在应用系统运行中需要通过动态路由后确定服务调用关系。

注2：对于单个服务，部署后的服务可以被终端用户、其他IT系统或服务实际调用；对于多个基于服务的流程，部署后可形成完整应用系统，从而为用户业务提供相应的IT支持。

### 2.21 

## 服务描述 service description

用统一的语法，对服务功能、接口等进行形式化的描述文档。

注：服务描述是组成服务合约的基础。

### 2.22 

## 服务开发 service development

服务的技术开发和物理实现过程。

### 2.23 

## 服务发现 service discovery

服务使用者依靠服务描述、查找获取可以满足特定功能性需求和非功能性需求的服务的过程。它涉及功能性和其他指标描述及匹配。

### 2.24 

## 服务治理 service governance

在服务生存周期中对服务的修改、版本更新、终止通知、分解细分、代理能力、分解能力、满足个性需求能力等的策略和机制制定。

### 2.25 

## 服务粒度 service granularity

表征服务能提供功能的层次。

注：服务粒度由规定服务的功能相关描述内容决定。

### 2.26 

## 服务实现 service implementation

将已定义的服务合约通过技术开发手段变成服务的过程，可通过服务集成、服务开发等具体方式。

### 2.27 

## 服务接口 service interface

用于实现使用者和提供者之间的通信合约，它提供了服务的功能、位置等执行通信时所需要的所有细节的描述。

注：服务接口一般是采用某种规范，如 WSDL 接口语言。

### 2.28 

## 服务互操作性 service interoperability

不同服务之间互相通信、调用执行、交换信息的能力。

### 2.29 

## 服务等级协定 service level agreement; SLA

服务水平协议

服务提供者与服务使用者之间的就服务需要达成的主要目标和双方具体的责任达成的约定。

### 2.30 

## 服务生存周期 service lifecycle

服务的生存全过程，包括服务的各个阶段：规划、分析、定义、标识、实现、审批、部署、服务启动、使用、发布、暂停、回复、更新、停止、回收、卸载/删除和弃用。

### 2.31 

## 服务管理 service management

制定具体措施来对服务策略进行实施的过程。

### 2.32 

## 服务建模 service modeling

面向服务的分析过程中的子过程，是通过将对业务流程进行分解、发现一系列可独立定义的功能或行为的候选服务的过程。

注：服务建模所得到候选服务包括不可细分的候选原子服务、基于原子服务的组合服务或者表示流程的服务。

### 2.33 

## 服务监控 service monitor

对服务的运行状态和绩效进行监测和控制的过程。

### 2.34 

## 服务编制 service orchestration

为实现特定业务功能，将一组服务以中心控制、可执行业务流程的方式进行组合，形成更大粒度服务的过程。

### 2.35 

## 面向服务 service oriented

通过一组有联系的服务的组合和集成来对软件或系统进行分析、设计和实现的思想。

### 2.36 

## 面向服务的分析 service oriented analysis

SOA 的生存周期及服务生存周期中的起始过程之一。

注 $ ^{1} $ ：面向服务的分析是对业务进行分析后形成一系列候选服务的过程。

注2：面向服务的分析过程也会根据业务发展及变化中而不断重复，并指导后续的过程。

### 2.37 

## 面向服务的体系结构 service oriented architecture; SOA

遵循面向服务原则、具有松耦合特性的体系结构风格。

### 2.38 

## 面向服务的设计 service oriented design

服务生存周期过程中的一个阶段，是根据面向服务的分析阶段所产生分析结果，对候选服务来进一步进行服务定义、并产生一系列正式的服务以及其服务合约的过程。

### 2.39 

## 服务策略 service policy

通过通用模型及相应语法，来对服务的消息传递方式、安全性、事务性、质量等不同的要求和功能所进行的规约，以方便服务使用者能够发现他们需要知道的信息，从而能够访问服务提供者的服务。

### 2.40 

## 服务提供者 service provider

提供服务的组织、个人及具体实现等实体。

### 2.41 

## 服务发布 service publishing

将已注册服务的信息对外公开的过程。

### 2.42 

## 服务注册 service register

将服务的服务合约注册到服务注册中心，以供服务的使用者查找和使用。

### 2.43 

## 服务注册中心 service registry

支撑服务及其相关资源的注册、发布、查找、评估等工作的实体。

### 2.44 

## 服务安全 service security

服务在运行过程中不会受到破坏、篡改、泄露及非法使用的技术和管理特性。

### 2.45 

## SOA 应用 SOA application

采用 SOA 的理念、方法、技术的软件实现。

### 2.46 

## SOA 应用概念模型 SOA application conceptual model

SOA 应用基本要素及相互关系的抽象描述。

### 2.47 

## SOA 应用技术参考模型 SOA application technical reference model

基于 SOA 应用概念模型，SOA 应用实现所需的逻辑功能单元及相互关系的描述。

### 2.48 

## SOA 治理 SOA governance

基于传统 IT 治理的基础之上，针对基于 SOA 的系统的最终用户所特有的服务生存周期定制的管控策略和机制。它通过制定人员、角色、管理流程及决策，以管理整个 SOA 的生存周期。

注：SOA 治理需要采纳相应的方法论和最佳实践，通常需要有工具辅助最后定制并管治符合企业自身需要的治理决策。治理处理的是分配决策权力，并决定使用何种措施以及遵循哪些策略来进行这些决策；管理是指具体执行决策的管理控制过程。

### 2.49 

## SOA 实现 SOA implementation

SOA 方法或技术实现的过程。

### 2.50 

## SOA 生存周期 SOA lifecycle

基于 SOA 的软件及系统实施的过程，包括分析和设计、实现、部署、测试评估、管理各方面。

### 2.51 

## SOA 管理 SOA management

根据 SOA 治理所确定的决策和机制，通过具体制定相关措施来进行实施的过程。

### 2.52 

## SOA 成熟度 SOA maturity: SOAM

对一个组织内的 IT 整体体系结构对 SOA 应用水平的量化描述。

### 2.53 

## SOA 成熟度模型 SOA maturity model; SOAMM

评估 SOA 成熟度的一种框架和方法。

### 2.54 

## SOA 产品 SOA product

遵循面向服务方法及技术的软件及解决方案。

### 2.55 

## SOA 产品互操作性 SOA product interoperability

运行时存在于不同 SOA 产品环境中的服务之间互相通信（调用）的能力。

### 2.56 

## SOA 资源 SOA resource

实现 SOA 应用所需的应用系统、数据以及现存服务等 IT 资源。

注：这些资源存在于企业、政府部门以及其他组织机构内，作为 SOA 应用建设中服务的初始来源。

### 2.57 

## Web 服务 Web service

一种应用编程接口或 Web 应用编程接口，通过标准的规约进行定义、并通过标准进行访问和使用。注：Web 服务是实现 SOA 的典型技术之一。

GB/T 29262—2012

參 考 文 献

[1] GB/T 11457—2006 信息技术 软件工程术语

[2] SJ/T 11409—2009 软件构件模型

## 索引

## B

F  
  
服务……2.8  
服务安全……2.44  
服务编排……2.13  
服务编制……2.34  
服务部署……2.20  
服务策略……2.39  
服务代理……2.9  
服务等级协定……2.29  
服务发布……2.41  
服务发现……2.23  
服务构件……2.14  
服务构件体系结构……2.15  
服务管理……2.31  
服务合约……2.18  
服务互操作性……2.28  
服务监控……2.33  
服务建模……2.32  
服务接口……2.27  
服务开发……2.22  
服务粒度……2.25  
服务描述……2.23  
服务目录……2.13  
服务生存周期……2.30  
服务实现……2.26  
服务使用者……2.17  
服务数据对象……2.19  
服务水平协议……2.29  
服务提供者……2.40  
服务消费者……2.17  
服务质量……2.6  
服务治理……2.24  
服务中介……2.9  
服务注册……2.42

服务注册中心 …… 2.43  
服务总线 …… 2.10  
服务组合 …… 2.16  
  
G  
  
功能单元 …… 2.3  
构件 …… 2.2  
  
H  
  
候选服务 …… 2.11  
  
M  
  
面向服务 …… 2.35  
面向服务的分析 …… 2.36  
面向服务的设计 …… 2.38  
面向服务的体系结构 …… 2.37  
  
T  
  
体系结构 …… 2.1  
  
X  
  
信息服务 …… 2.4  
  
I  
  
IT 基础设施 …… 2.5  
  
S  
  
SOA 产品 …… 2.54  
SOA 产品互操作性 …… 2.55  
SOA 成熟度 …… 2.52  
SOA 成熟度模型 …… 2.53  
SOA 管理 …… 2.51  
SOA 生存周期 …… 2.50  
SOA 实现 …… 2.49  
SOA 应用 …… 2.45  
SOA 应用概念模型 …… 2.46  
SOA 应用技术参考模型 …… 2.47  
SOA 治理 …… 2.48  
SOA 资源 …… 2.56

Web 服务 …… 2.57

## 英文对应词索引

A  
architecture 2.1  
C  
component 2.2  
F  
functional unit 2.3  
I  
information service 2.4  
information-technology infrastructure 2.5  
Q  
quality of service 2.6  
QoS 2.6  
R  
representational state transfer 2.7  
REST 2.7  
S  
SC 2.12  
SCA 2.15  
SDO 2.19  
service 2.8  
service agent 2.9  
service broker 2.9  
service bus 2.10  
service candidate 2.11  
service catalogue 2.12  
service choreography 2.13  
service component 2.14  
service component architecture 2.15  
service composition 2.16  
service consumer 2.17  
service contract 2.18  
service data object 2.19  
service deployment 2.20  
service description 2.21  
service development 2.22

service discovery 2.23  
service governance 2.24  
service granularity 2.25  
service implementation 2.26  
service interface 2.27  
service interoperability 2.28  
service level agreement 2.29  
service lifecycle 2.30  
service management 2.31  
service modeling 2.32  
service monitor 2.33  
service orchestration 2.35  
service oriented 2.35  
service oriented analysis 2.36  
service oriented architecture 2.37  
service oriented design 2.38  
service policy 2.39  
service provider 2.40  
service publishing 2.41  
service register 2.42  
service registry 2.43  
service security 2.44  
SLA 2.29  
SOA 2.37  
SOAM 2.52  
SOAMM 2.53  
SOA application 2.45  
SOA application conceptual model 2.46  
SOA application technical reference model 2.47  
SOA governance 2.48  
SOA implementation 2.49  
SOA lifecycle 2.50  
SOA management 2.51  
SOA maturity 2.52  
SOA maturity model 2.53  
SOA product 2.54  
SOA product interoperability 2.55  
SOA resource 2.56

## W

Web service 2.57

GB/T 29262-2012

中华人民共和国

国家标准

信息技术 面向服务的体系结构(SOA)

术语

GB/T 29262—2012

中国标准出版社出版发行  

北京市朝阳区和平里西街甲2号（100013）  

北京市西城区三里河北街16号（100045）

网址: www.gb168.cn

服务热线：010-68522006

2013年4月第一版

书号：155066·1-46788

版权专有 侵权必究