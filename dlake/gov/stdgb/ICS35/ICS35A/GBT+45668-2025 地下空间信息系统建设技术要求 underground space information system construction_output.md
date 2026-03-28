

# 中华人民共和国国家标准

GB/T 45668—2025

# 地下空间信息系统建设技术要求

# Technical requirements for underground space information system construction

2025-05-30 发布

2025-09-01 实施



## 目次

前言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语、定义和缩略语 …… 2    
3.1 术语和定义 …… 2    
3.2 缩略语 …… 2    
4 总体要求 …… 2    
4.1 建设流程 …… 2    
4.2 建设内容 …… 3    
4.3 时空基准 …… 3    
4.4 数据要求 …… 3    
4.5 其他要求 …… 3    
5 系统设计 …… 3    
5.1 一般要求 …… 3    
5.2 设计过程 …… 3    
5.3 系统框架 …… 3    
5.4 功能要求 …… 5    
5.5 数据库设计 …… 6    
5.6 与其他信息系统的对接 …… 6    
5.7 运行环境要求 …… 6    
6 数据组织与建库 …… 7    
6.1 一般要求 …… 7    
6.2 数据准备与预处理 …… 7    
6.3 数据处理 …… 7    
6.4 数据入库 …… 9    
7 系统实现 …… 9    
7.1 一般要求 …… 9    
7.2 软件开发 …… 10    
7.3 运行环境建立 …… 10    
7.4 系统集成与测试 …… 10    
8 系统验收 …… 10    
8.1 一般要求 …… 10    
8.2 试运行 …… 11

8.3 验收测试 …… 11    
8.4 技术成果资料 …… 11    
8.5 验收实施 …… 11    
9 系统运行与维护 …… 11    
9.1 一般要求 …… 11    
9.2 日常运行管理 …… 11    
9.3 安全保密管理 …… 11    
9.4 数据备份与更新 …… 12    
9.5 系统升级与维护 …… 12    
附录 A（规范性） 地下空间数据大类分层与命名 …… 13    
附录 B（资料性） 地下空间设施数据图式符号 …… 17    
参考文献 …… 20

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由中华人民共和国自然资源部提出。

本文件由全国地理信息标准化技术委员会(SAC/TC 230)归口。

本文件起草单位：正元地理信息集团股份有限公司、南京市测绘勘察研究院股份有限公司、建设综合勘察研究设计院有限公司、南京师范大学、昆明市城市地下空间规划管理办公室、广州市城市规划勘测设计研究院、厦门精图信息技术有限公司、南京市人民防空办公室、上海勘察设计研究院（集团）股份有限公司、北京市测绘设计研究院、自然资源部地下管线勘测工程院、四川国测信息科技有限公司、北京市新技术应用研究所、成都市勘察测绘研究院、江苏舆图信息科技有限公司。

本文件主要起草人：李学军、储征伟、耿丹、张书亮、侯至群、张鹏程、乔志勇、冯兵、黄永进、龙家恒、陈勇、陈光华、刘克会、张勇、鞠建荣、解智强、许杰、潘良波、周文、王勇、沈雨。



# 地下空间信息系统建设技术要求

## 1 范围

本文件规定了地下空间信息系统建设的总体要求，以及系统设计、数据组织与建库、系统实现、系统验收、系统运行与维护的技术要求。

本文件适用于地下空间信息系统的设计、开发、应用与运维。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2887 计算机场地通用规范

GB/T 8566 系统与软件工程 软件生存周期过程

GB/T 8567 计算机软件文档编制规范

GB/T 9361 计算机场地安全要求

GB/T 9385 计算机软件需求规格说明规范

GB/T 12328 综合工程地质图图例及色标

GB/T 15532 计算机软件测试规范

GB/T 18578 城市地理信息系统设计规范

GB/T 20158 信息技术 软件生存周期过程 配置管理

GB/T 20273 信息安全技术 数据库管理系统安全技术要求

GB/T 21740 基础地理信息城市数据库建设规范

GB/T 22239 信息安全技术 网络安全等级保护基本要求

GB/T 22240 信息安全技术 网络安全等级保护定级指南

GB/T 28448 信息安全技术 网络安全等级保护测评要求

GB/T 28449 信息安全技术 网络安全等级保护测评过程指南

GB/T 28590 城市地下空间设施分类与代码

GB/T 33447 地理信息系统软件测试规范

GB/T 39786 信息安全技术 信息系统密码应用基本要求

GB/T 41447 城市地下空间三维建模技术规范

GB/T 42987 城市地下空间数据要求

GB/T 45666 陆域管线要素分类代码与符号表达

GB 50174 数据中心设计规范

CH/T 1037 管线信息系统建设技术规范

DZ/T 0197 数字化地质图图层及属性文件格式

DZ/T 0352 城市地质调查数据内容与数据库结构

## 3 术语、定义和缩略语

### 3.1 术语和定义

下列术语和定义适用于本文件。

#### 3.1.1 

地下空间 underground space

为满足生产和生活等需求在地表以下开发、建设和利用的空间。

[来源:GB/T 42987—2023,3.1]

#### 3.1.2 

## 地下空间设施 underground space facilities

在地下空间（3.1.1）建设，具有满足人类社会生产、生活、交通、能源、环保、安全、防灾减灾、信息与通信需求功能的建（构）筑物。

[来源:GB/T 28590—2012,2.1,有修改]

#### 3.1.3 

## 地质数据 geology data

与地下空间（3.1.1）开发、建设和利用相关的各类地质环境条件数据。

[来源:GB/T 42987—2023,3.5]

#### 3.1.4 

## 地下空间数据 underground space data

描述地下空间设施3.1.2的空间及关系和属性特征的数据以及地质数据3.1.3。

[来源:GB/T 42987—2023,3.2,有修改]

#### 3.1.5 

## 地下空间信息系统 underground space information system

基于计算机软硬件和网络环境，利用信息技术对地下空间数据（3.1.4）进行汇聚、处理、检查、入库、更新，实现数据管理、共享交换及应用服务的技术系统。

### 3.2 缩略语

下列缩略语适用于本文件。

BIM: 建筑信息模型 (Building Information Modeling)

CGCS2000:2000 国家大地坐标系(China Geodetic Coordinate System 2000)

CIM: 城市信息模型 (City Information Model)

## 4 总体要求

### 4.1 建设流程

系统建设流程应符合图 1 的规定，包括系统设计、数据组织与建库、系统实现、系统验收、系统运行与维护。

<div style="text-align: center;"><img src="imgs/img_in_image_box_186_1388_988_1474.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 1 地下空间信息系统建设流程图</div>


### 4.2 建设内容

系统建设内容应包括地下空间数据库、系统软件和运行环境。地下空间数据库应包括数据组织和数据入库；系统软件应包括数据管理、数据共享交换、数据应用服务及扩展功能的实现；运行环境应包括系统运行所必需的软硬件和网络设备及标准规范和安全保障措施。

### 4.3 时空基准

4.3.1 平面坐标系统应采用 CGCS2000，高程基准应采用 1985 国家高程基准。采用其他坐标系和高程基准时，应与 CGCS2000、1985 国家高程基准建立联系。

4.3.2 时间基准应采用公元纪年和北京时间。

### 4.4 数据要求

系统建设所使用的地下空间数据应符合 GB/T 42987 的相关规定。

### 4.5 其他要求

4.5.1 地下空间信息系统应关联对接有数据交换关系的其他信息系统。

4.5.2 系统建设的全周期管理应符合 GB/T 8566 的规定。

## 5 系统设计

### 5.1 一般要求

5.1.1 系统设计应以满足地下空间数据管理与应用服务业务需求为目标，实现地下空间数据集中管理和共享交换，为地下空间资源开发利用辅助决策及关联业务协同提供数据支撑和应用服务。

5.1.2 系统设计应遵循实用性、规范性、先进性、可靠性、共享性、安全性和经济高效的原则。

5.1.3 系统设计编制的设计方案应经过论证后实施。

### 5.2 设计过程

5.2.1 系统设计应符合 GB/T 18578 的规定，设计过程包括需求分析、总体设计和详细设计。

5.2.2 需求分析应调研分析地下空间数据业务、用户与访问接口、软硬件与网络环境、地下空间数据资源现状、本地已有相关的其他信息系统现状，按 GB/T 9385 的规定编制需求规格说明书，明确系统功能与性能需求，以及系统设计约束、安全性、适用性和内外接口要求。

5.2.3 总体设计应在需求分析基础上，确定总体目标、系统架构、模块功能，进行接口设计、运行设计、软硬件和网络设计、数据库设计，制定系统开发计划，并编制总体设计方案。

5.2.4 详细设计应根据总体设计方案进行用户界面设计、功能模块算法确定、数据库结构设计、软硬件和网络配置设计以及数据共享交换方式设计，并编制详细设计方案。

### 5.3 系统框架

5.3.1 系统应采用面向服务(SOA)的架构，具备条件的采用云技术架构。

5.3.2 系统总体框架设计应符合图 2 规定，包括基础设施层、数据资源层、系统软件支撑层和应用服务层，以及标准规范体系和安全保障体系。

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_196_985_1069.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 2 地下空间信息系统总体框架图</div>


5.3.3 基础设施层应包括计算、存储、网络、安全硬件设备及操作系统、数据库软件、安全防护软件，为系统运行提供软硬件及网络资源环境。

5.3.4 数据资源层应包括地下建筑物数据、地下交通设施数据、地下管线数据、综合管廊数据、地基基础数据、地质数据，通过数据组织建立数据库，实现地下空间数据汇聚与存储、治理与融合，为系统软件支撑层、应用服务层提供数据基础。

5.3.5 系统软件支撑层应具备满足业务需求的数据管理、数据共享交换与数据应用服务功能，并具有高效、友好的人机交互界面，为应用服务层提供系统软件支撑。

5.3.6 应用服务层应包括基于基础设施、数据资源及系统软件，实现多端业务协同，具有为不同用户提供地下空间数据共享交换与应用服务的能力，以及为地下空间安全风险防控、规划审批与管控、环境保护与监测、资源开发利用提供数据支撑的能力。

5.3.7 标准规范体系应包括符合系统运行管理与应用需求的相关技术标准与管理规范。

5.3.8 安全保障体系应包括符合国家信息安全保密有关规定的管理机制和措施。

### 5.4 功能要求

5.4.1 系统软件功能应包括基本功能和扩展功能。

5.4.2 系统软件基本功能应包括数据管理、数据共享交换、数据应用服务和系统运行管理。

5.4.3 数据管理应具备二三维数据管理的基本功能，并应符合下列要求：

a）具备数据手工录入、批量导入、在线接入功能；

b) 具备数据编辑、处理与入库功能；

c) 具备图形、属性、逻辑一致性检查及数据完整性与合理性的数据检查功能；

d）具备数据加载、浏览、漫游和条件查询统计功能；

e）具有输入、编辑、维护元数据的功能；

f）具备数据裁剪、成图导出、分层展示的数据输出功能；

g）具备不同来源、不同类型数据的目录管理功能；

h）具备历史数据库管理功能。

5.4.4 数据共享交换应具备数据服务、目录服务和数据分发的基本功能，并应符合下列要求：

a）具备数据格式转换和二三维数据的导入、导出功能；

b）具备按需求进行数据裁剪分发功能；

c）具备不同规格专题图制作输出功能；

d）具备目录管理服务、目录检索服务和目录交换服务功能；

e) 具备与其他系统之间的数据上传与下载的双向交换功能；

f) 具备数据分发、共享交换的记录与分类统计功能；

g）具备标准协议接口和接口识别功能。

5.4.5 数据应用服务的基本功能应符合下列要求：

a）具备多方式定位和条件查询功能以及历史数据追溯功能；

b）具备专题统计分析、剖切分析、连通分析、净距分析、碰撞分析、覆土分析、剥层分析、开挖分析和缓冲区分析功能；

c) 具备扯旗标注、属性标注、空间量测、面（体）积量算、图形裁切和地图缩放功能；

d) 具备数据治理与融合、实景影像叠加功能；

e）具备二三维数据叠加与集成、三维模拟与虚拟仿真功能；

f) 具备地上地下对照、空间关系分析、地下空间资源聚类分析功能；

g）具备地上基础地理信息、BIM数据的动态加载、浏览与查询功能；

h）具备隐患管理、事故应急指挥与疏散分析功能；

i) 具备地下空间选址与时空模拟推演功能；

i) 具备开放地理空间信息标准(OGC)的数据网络服务功能；

k）具备与其他系统对接的数据传输接口、应用编程接口。

5.4.6 系统运行管理功能应包括用户权限管理、业务流程管理、日志管理、系统配置管理、运行安全实时监测、运行问题实时分析功能。

5.4.7 系统宜针对业务应用场景需求进行功能扩展，在系统基本功能基础上，实现多端业务协同与地下空间运行状态实时感知，提高地下空间安全风险防控、规划审批与管控、环境保护与监测和资源开发利用的辅助决策与智能化应用能力。扩展功能包括下列内容：

a）基于二次开发的移动端、云端交互功能；

b) 物联感知数据动态接入汇聚与场景化渲染表达功能；

c) 地下空间安全风险防控分析与监测预警功能；

d) 地下空间三维动态建模及地上地下三维模型一体集成分析功能；

e） 地下空间规划适宜性评价、管控与资源承载力分析功能；

f） 地热分析、地面沉降模拟、地下水流向分析、土壤与地下水污染模拟功能。

### 5.5 数据库设计

5.5.1 系统设计时应在需求分析基础上进行数据库设计，设计过程应符合 GB/T 21740 的规定。

5.5.2 地下空间设施数据应包括历史数据、现状数据和规划数据，地质数据应包括构造地质数据、工程地质数据、水文地质数据、环境地质数据、资源地质数据、灾害地质数据和其他地质数据。

5.5.3 地下空间数据类型应按几何特征不同分为点、线、面、体（三维模型）和注记。

5.5.4 数据库设计应确定不同来源的同类数据转换方法，建立不同尺度数据的集成与关联。

5.5.5 创建数据库体时应根据不同类别数据量分配物理空间和建立空间索引，实现数据分类、分层存储和逻辑无缝联接，并保持标识码唯一。

5.5.6 地下空间数据的属性数据结构应统一。

5.5.7 建立地下空间数据库时应同步建立元数据库。

5.5.8 数据库应选用关系型数据库，采用空间数据引擎统一管理地下空间数据的空间数据、几何数据及属性数据，并具备海量数据处理与存储能力、数据备份恢复与安全管理功能。

5.5.9 数据库中涉及国家秘密的数据应按国家保密管理相关规定进行存储和管理。

5.5.10 数据库的安全技术设计应符合 GB/T 20273 的要求。

### 5.6 与其他信息系统的对接

5.6.1 系统应对接智慧城市时空大数据云平台，获取电子地图、影像地图、三维模型数据，提供地下空间数据与数据应用服务。

5.6.2 系统应对接 CIM 平台，获取 BIM 数据、三维模型数据和开展地下空间设施的 CIM+应用，提供地下空间数据与数据应用服务。

5.6.3 系统应对接国土空间基础信息平台，为国土空间信息模型(TIM)建设、应用及国土空间规划提供地下空间数据与数据应用服务。

5.6.4 系统应对接城市“一网统管”平台、城市运行管理服务平台，提供地下空间数据与功能服务。

5.6.5 系统应对接综合地下管线信息管理系统、专业管线信息管理系统，实现数据共享交换和提供数据应用服务。

5.6.6 系统应对接地下市政基础设施综合管理信息平台、城市安全风险综合监测预警平台，实现数据共享交换和提供数据应用服务。

5.6.7 系统应对接城市地质、人防工程、综合管廊、不动产等其他专业信息系统，实现数据共享交换和提供数据应用服务。

### 5.7 运行环境要求

5.7.1 系统运行环境除软硬件和网络配置外，还应包括标准规范和安全保障措施制定。

5.7.2 软硬件设备的性能、功能、数量应满足系统运行和数据备份的要求。

5.7.3 网络布设方式、网络性能应同时满足数据传输和国家有关数据保密管理要求，并应符合GB/T 22239、GB/T 22240、GB/T 39786的规定。

5.7.4 标准规范应统一制定，并应符合国家相关政策、法律法规要求和本地系统运行与维护需求。

5.7.5 安全保障措施应在评估系统安全等级基础上制定，并应符合国家有关信息安全等级保护要求和系统安全稳定运行保障需求。

## 6 数据组织与建库

### 6.1 一般要求

6.1.1 数据库建立应符合 5.5 的设计要求，建库过程应包括数据准备与预处理、数据处理、数据入库。

6.1.2 地下空间数据库应包括地下建筑物数据库、地下交通设施数据库、地下管线数据库、综合管廊数据库、地基基础数据库、地质数据库。

### 6.2 数据准备与预处理

6.2.1 数据准备时应收集、整理地下空间设施数据、地质数据，包括数据汇交和现状勘测、数据接入、三维建模形成的栅格数据、矢量数据、实景影像数据、点云数据、BIM数据、三维模型数据。

6.2.2 数据收集整理后应采用内业检查与外业核查相结合的方式进行数据检查，检查内容应符合下列要求：

a）检查数据的准确性，包括空间位置精度、属性精度的检查与评估；

b) 检查数据的完整性，包括数据齐全性及属性完整性的检查与评估；

c）检查数据的可靠性，包括数据来源的检查与评估；

d）检查数据的一致性，包括数据格式、逻辑关系、时空基准的检查与评估。

6.2.3 数据治理应包括数据清洗、格式转换、坐标转换，并符合下列要求：

a）通过数据清洗进行数据缺失和异常数据处理，剔除重复、无关、错误和冗余数据；

b）通过格式转换将同类多源异构数据转换为统一的数据格式；

c）通过坐标转换统一数据的空间基准。

6.2.4 数据融合应通过整合同类但不同来源的数据，消除数据间的冲突和不一致。

6.2.5 数据预处理后应进行全面检查，确认数据准确性、完整性、可靠性和一致性。

### 6.3 数据处理

6.3.1 地下空间数据的大类、中类、小类划分应符合 GB/T 42987 的相关规定。

6.3.2 地下空间数据应按照唯一性原则编制分类代码，地下管线数据、综合管廊数据的分类代码应符合 GB/T 45666 的规定，其他地下空间设施数据的分类代码应与 GB/T 28590 规定的设施分类代码相衔接，地质数据的分类代码应符合 DZ/T 0352 的相关规定。现有分类代码不能满足需要时，应按代码扩充原则进行扩充。

6.3.3 地下空间数据大类应按附录 A 的规定进行分层，划分为点图层、线图层、面图层、体（三维模型）图层和注记图层。

6.3.4 数据大类分层应按附录 A 的规定，采用“数据大类代号＋数据类型代号＋数据内容代号”的组合方式进行命名，命名结构见图 3，并符合下列要求：

a） 数据大类代号见表1，采用大类中文名称中4个关键字汉语拼音的首字母组合表示；

b）数据类型代号见表2，采用点、线、面、体、注记英文名称的2个缩写字母组合表示；

c） 数据内容代号见表 3，采用数据内容中文名称中 2 个关键字汉语拼音的首字母组合表示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_401_1341_802_1479.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">图 3 数据分层命名结构图</div>


<div style="text-align: center;">表 1 数据大类及代号表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类中文名称</td><td style='text-align: center;'>代号</td></tr><tr><td style='text-align: center;'>地下建筑物数据</td><td style='text-align: center;'>DXJZ</td></tr><tr><td style='text-align: center;'>地下交通设施数据</td><td style='text-align: center;'>DXJT</td></tr><tr><td style='text-align: center;'>地下管线数据</td><td style='text-align: center;'>DXGX</td></tr><tr><td style='text-align: center;'>综合管廊数据</td><td style='text-align: center;'>ZHGL</td></tr><tr><td style='text-align: center;'>地基基础数据</td><td style='text-align: center;'>DJJC</td></tr><tr><td style='text-align: center;'>地质数据</td><td style='text-align: center;'>DZSJ</td></tr></table>

<div style="text-align: center;">表 2 数据类型及代号表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>代号</td></tr><tr><td style='text-align: center;'>点</td><td style='text-align: center;'>Point</td><td style='text-align: center;'>PT</td></tr><tr><td style='text-align: center;'>线</td><td style='text-align: center;'>Line</td><td style='text-align: center;'>LN</td></tr><tr><td style='text-align: center;'>面</td><td style='text-align: center;'>Plane</td><td style='text-align: center;'>PL</td></tr><tr><td style='text-align: center;'>体</td><td style='text-align: center;'>Volume</td><td style='text-align: center;'>VL</td></tr><tr><td style='text-align: center;'>注记</td><td style='text-align: center;'>Text</td><td style='text-align: center;'>TX</td></tr></table>

<div style="text-align: center;">表 3 数据内容及代号表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">数据内容中文称谓</td><td style='text-align: center;'>代号</td></tr><tr><td rowspan="3">地下空间设施数据</td><td style='text-align: center;'>历史数据</td><td style='text-align: center;'>LS</td></tr><tr><td style='text-align: center;'>现状数据</td><td style='text-align: center;'>XZ</td></tr><tr><td style='text-align: center;'>规划数据</td><td style='text-align: center;'>GH</td></tr><tr><td rowspan="7">地质数据</td><td style='text-align: center;'>构造地质数据</td><td style='text-align: center;'>GZ</td></tr><tr><td style='text-align: center;'>工程地质数据</td><td style='text-align: center;'>GC</td></tr><tr><td style='text-align: center;'>水文地质数据</td><td style='text-align: center;'>SW</td></tr><tr><td style='text-align: center;'>环境地质数据</td><td style='text-align: center;'>HJ</td></tr><tr><td style='text-align: center;'>资源地质数据</td><td style='text-align: center;'>ZY</td></tr><tr><td style='text-align: center;'>灾害地质数据</td><td style='text-align: center;'>ZH</td></tr><tr><td style='text-align: center;'>其他地质数据</td><td style='text-align: center;'>QT</td></tr></table>

6.3.5 以数据中类、数据小类分层时，地下管线、综合管廊数据分层及命名应符合 CH/T 1037 的相关规定，地质数据分层及命名应符合 DZ/T 0197 的相关规定，其他地下空间数据应按照点、线、面、体（三维模型）和注记划分图层，采用“数据类别代号+数据类型代号+数据内容代号”的组合方式进行命名。

6.3.6 地下空间数据的图式符号分为点状符号、线状符号、面状符号，地下管线和综合管廊数据的图式符号应符合 GB/T 45666 的规定，地质数据的图式符号应符合 GB/T 12328 的相关规定，其他地下空间设施数据的图式符号应根据需要制定，部分地下空间设施数据的图式符号及颜色参见附录 B。现有图式符号不能满足需要时，应按照系统性、继承性和易读性原则进行扩充。

6.3.7 多层地下空间设施的空间层次表达宜符合下列要求：

a）采用对应颜色饱和度由低到高的渐变表示同一类地下空间设施从最浅层到最深层；

b) 采用地下空间最大范围实线边框和边框内推虚线表示重叠层，采用虚线表示不重叠空间的分间关系，按所在地下由浅至深顺序标注每层所在层数；

c）按所在地下由浅至深顺序分别标注每层地下空间设施的性质。

6.3.8 三维模型数据组织应符合 GB/T 41447 的规定。

6.3.9 属性数据建立、元数据建立应符合 GB/T 42987 的规定。

6.3.10 数据处理完成后应进行质量检查，及时处理问题和纠正错误。检查内容应包括时空基准、数据分类与分层、编码与命名、数学精度、属性精度、符号表达以及数据间的空间与逻辑关系。

### 6.4 数据入库

6.4.1 数据入库包括原始数据入库和更新数据入库。

6.4.2 原始数据入库前应进行数据检查通过后方可入库，检查内容应符合6.2.2的要求。

6.4.3 原始数据入库方式包括手工录入、批量导入和在线共享接入，并应符合下列要求：

a）现状勘测数据采用内外业一体化作业模式，按数据存储要求生成入库数据文件后入库；

b）收集数据、汇交数据按照6.2、6.3的要求进行数据组织后入库。

c）已有地下空间数据库的分类数据按照6.2.3、6.2.4的要求进行治理和融合后入库。

d）由其他系统在线共享接入的数据按入库要求检查比对确认后入库。

6.4.4 更新数据入库分为空间数据入库、属性数据入库、元数据入库和三维模型数据入库，并应符合下列要求：

a）更新数据入库前按照6.2、6.3的要求进行数据检查和处理，非结构化数据进行信息分析提取并经检查处理符合入库要求；

b）更新数据的逻辑关系、属性结构、分类分层、数据精度与数据库中同类数据保持一致；

c）更新数据时，同时更新元数据；

d）更新数据不降低原数据库的安全保密等级；

e）更新数据时，及时建立历史数据库。

6.4.5 数据入库后应进行数据检查，检查内容应包括数据内容与分类分层、时空基准、数学精度、属性精度、逻辑一致性、符号表达、空间层次表达、地下空间联通与从属关系、元数据，并应符合下列要求：

a） 数据内容完整，分类分层正确；

b) 数据的时空基准正确；

c) 数据的数学精度与入库前一致；

d）属性结构与属性值完整、正确；

e) 拓扑关系正确、逻辑一致；

f）符号表达与空间层次表达正确；

g） 地下空间联通与从属关系正确；

h）元数据内容完整、正确、唯一。

6.4.6 数据入库过程应记录操作日志。

## 7 系统实现

### 7.1 一般要求

7.1.1 系统实现应包括软件开发、运行环境建立、系统集成与测试。

7.1.2 软件开发过程应符合 GB/T 8566 的规定，技术文档编制应符合 GB/T 8567 的规定。

7.1.3 支撑系统运行的软硬件设备、网络环境以及标准规范、安全保密制度措施应同步建立。

### 7.2 软件开发

7.2.1 软件开发应包括编码与测试，实现的功能应符合5.4的要求。

7.2.2 软件开发应采用模块化、组件式的方式。

7.2.3 软件开发使用的开发工具应具有良好的模块化机制、编译和调试机制，并便于调用数据库接口和已有其他信息系统接口。

7.2.4 软件开发应制定编码规范，内容包括代码格式、命名、注释、语句、声明、目录设置和代码说明。软件代码应具有重构、重用和容错特性。

7.2.5 软件开发应使用管理工具进行软件配置管理，并应符合 GB/T 20158 的规定。

7.2.6 软件开发过程中应按 GB/T 15532、GB/T 33447 的相关规定进行代码测试，及时发现和消除编码问题。

7.2.7 软件开发应按 GB/T 15532、GB/T 33447 的相关规定，由开发人员进行检验代码功能正确性的单元测试，发现问题及时处置后应进行回归测试合格。

### 7.3 运行环境建立

7.3.1 运行环境建立应符合 5.7 的设计要求。

7.3.2 软件应选配正版化的操作系统、地理信息系统（GIS）平台软件、数据库软件、网络安全防护软件；选配计算机、服务器、存储设备、交换机以及数据输入输出设备、安全防护设备时，并应兼顾数据量、数据传输的未来发展需要。

7.3.3 配置网络时应根据实际需要确定网络结构、带宽与传输速率，经过测试确认与安全防护软硬件相匹配，并应实现涉密与非涉密网络间的物理隔离，按 GB/T 28448 的规定进行网络安全等级测评。

7.3.4 部署数据中心机房时应符合 GB/T 2887、GB 50174、GB/T 9361 的相关规定。

7.3.5 系统标准规范应包括数据标准、数据共享交换规则、数据应用服务规则、数据更新规范和系统运行与维护管理规范。

7.3.6 系统安全保密管理制度措施应包括人员、设备、网络、密码使用、系统维护、数据备份与恢复、安全事件处置的规范化管理制度，以及防火墙、加密、密码管理、身份认证、入侵监测、数据备份与恢复、数字水印、访问控制、安全审计技术措施与应急应对策略。

### 7.4 系统集成与测试

7.4.1 系统集成应包括环境集成、数据集成、功能集成和技术集成。

7.4.2 环境集成应包括软件开发配置、系统运行环境及与系统内外部接口集成。

7.4.3 数据集成应包括按照第 5 章、第 6 章要求建立的数据库集成。

7.4.4 功能集成应包括软件开发实现的所有功能集成。

7.4.5 技术集成应包括实现数据管理、共享交换与应用服务功能的相关技术集成。

7.4.6 系统集成后应按 GB/T 15532、GB/T 33447 的相关规定，由开发人员和用户代表共同进行系统集成测试，测试内容应包括系统功能适用性、模块间兼容协调性，系统负载并发用户量、数据量、系统配置的稳定性，以及系统安全性。发现问题应经处理再行合格性测试通过后进行系统安装。

## 8 系统验收

### 8.1 一般要求

系统验收应在完成试运行和通过验收测试，提交技术成果资料后进行。

### 8.2 试运行

试运行应在系统安装、调试和培训后进行，过程包括编制试运行计划、问题整改完善、填写日志记录和编制试运行报告。

### 8.3 验收测试

试运行后应按 GB/T 15532、GB/T 33447 的相关规定和系统设计要求，由第三方进行验收测试，测试内容应符合 7.4.6 的要求。

### 8.4 技术成果资料

提交的技术成果资料应齐全完整，包括需求规格说明书、系统设计方案、测试报告、系统部署文档、系统操作手册、系统运维手册、总结报告、试运行报告、系统软件安装包和数据库成果。

### 8.5 验收实施

系统验收依据应包括任务合同、需求规格说明书、系统设计方案，系统验收应出具明确验收意见。

## 9 系统运行与维护

### 9.1 一般要求

9.1.1 系统运行与维护应包括日常运行管理、安全保密管理、数据备份与更新、系统升级与维护。

9.1.2 系统运行应持续保持稳定、安全和高效，不应因系统升级与维护而中断。

9.1.3 系统运行维护应制定应急预案并定期组织进行应急演练。

### 9.2 日常运行管理

9.2.1 日常运行管理应包括数据汇聚整理与入库、系统软件与基础设施监测管理和运行质量评价。

9.2.2 系统运行期间应及时汇聚整理和入库地下空间数据，并应符合第6章的相关要求。

9.2.3 系统应利用 5.4.6 的功能进行运行管理，实时监测和记录系统操作使用状况，并规范进行数据管理、数据共享交换和应用服务。

9.2.4 系统运行期间应实时监测基础设施运行状态，并制定其功能性能优化以及问题处理机制。

9.2.5 日常运行管理应建立运行日志，及时记录系统运行情况。

9.2.6 日常运行管理应定期进行运行质量评价，评价内容包括系统稳定性、可靠性、功能适用性、安全保密性能和系统运行效率，以及根据评价结果提出的系统升级与维护及完善标准规范与安全保密制度措施建议。

### 9.3 安全保密管理

<div style="text-align: center;"><img src="imgs/img_in_image_box_646_1270_683_1307.jpg" alt="Image" width="3%" /></div>


9.3.1 安全保密管理内容应包括系统运行安全和数据保密。

9.3.2 系统运行安全管理应符合 7.3.6 的要求，并持续完善安全管理制度和保密技术措施。

9.3.3 系统运行期间网络应定期按 GB/T 28449 的规定进行网络安全等级保护测评与备案。

9.3.4 数据管理、数据共享交换与应用服务时应进行权限管理，并应及时按 9.4 的相关要求进行数据备份。

9.3.5 系统运行发现可疑行为及违规操作，应及时采取措施予以处置。当系统功能被破坏或发生故障时，应在规定时间内予以恢复。

### 9.4 数据备份与更新

9.4.1 数据备份内容应包括地下空间数据库数据以及系统软件及其升级版本、系统运行管理信息与网络管理信息。

9.4.2 数据备份形式应分为本地备份、异地备份。具备条件的，应进行异地备份。

9.4.3 地下空间数据库数据应定期进行全备份和增量备份，系统软件及其升级版本、系统运行管理信息与网络管理信息应随时进行全备份，系统升级时还应备份安装软件。

9.4.4 备份数据应采用不同介质进行同时存储，并应定期进行校核和转存，核验数据恢复能力。

9.4.5 数据更新应按照 6.4.4 的要求，通过地下空间信息系统进行更新数据检查、处理和入库。

### 9.5 系统升级与维护

9.5.1 系统升级与维护内容应包括系统软件和运行环境。

9.5.2 系统升级应具备如下条件：

a）系统软件现有功能不满足需求而进行功能拓展时；

b）软硬件和网络环境难以支持系统正常运行时；

c） 地下空间数据结构发生重大变化时。

9.5.3 系统升级前应制定升级方案并进行评估和论证，升级后应进行测试、验证和确认。

9.5.4 系统运行生命周期内应根据实时监控和预警系统的性能、访问压力以及运行状态，并根据监控分析结果及时进行维护和改进优化维护措施。

9.5.5 系统维护应按照系统运维手册执行，全程记录维护信息并实施档案管理。

## 附录 A

(规范性)

地下空间数据大类分层与命名

地下空间数据大类分层与命名应按表 A.1 进行。

<div style="text-align: center;">表 A.1 地下空间数据大类分层与命名表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类名称</td><td style='text-align: center;'>数据分层代号</td><td style='text-align: center;'>数据分层名描述</td></tr><tr><td rowspan="15">地下建筑物数据</td><td style='text-align: center;'>DXJZ_PT_LS</td><td style='text-align: center;'>历史点图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_LN_LS</td><td style='text-align: center;'>历史线图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_PL_LS</td><td style='text-align: center;'>历史面图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_VL_LS</td><td style='text-align: center;'>历史体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXJZ_TX_LS</td><td style='text-align: center;'>历史建筑物注记图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_PT_XZ</td><td style='text-align: center;'>现状点图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_LN_XZ</td><td style='text-align: center;'>现状线图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_PL_XZ</td><td style='text-align: center;'>现状面图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_VL_XZ</td><td style='text-align: center;'>现状体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXJZ_TX_XZ</td><td style='text-align: center;'>现状建筑物注记图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_PT_GH</td><td style='text-align: center;'>规划点图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_LN_GH</td><td style='text-align: center;'>规划线图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_PL_GH</td><td style='text-align: center;'>规划面图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_VL_GH</td><td style='text-align: center;'>规划体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXJZ_TX_GH</td><td style='text-align: center;'>规划建筑物注记图层数据层</td></tr><tr><td rowspan="15">地下交通设施数据</td><td style='text-align: center;'>DXJT_PT_LS</td><td style='text-align: center;'>历史点图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_LN_LS</td><td style='text-align: center;'>历史线图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_PL_LS</td><td style='text-align: center;'>历史面图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_VL_LS</td><td style='text-align: center;'>历史体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXJT_TX_LS</td><td style='text-align: center;'>历史交通设施注记图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_PT_XZ</td><td style='text-align: center;'>现状点图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_LN_XZ</td><td style='text-align: center;'>现状线图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_PL_XZ</td><td style='text-align: center;'>现状面图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_VL_XZ</td><td style='text-align: center;'>现状体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXJT_TX_XZ</td><td style='text-align: center;'>现状交通设施注记图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_PT_GH</td><td style='text-align: center;'>规划点图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_LN_GH</td><td style='text-align: center;'>规划线图层数据层</td></tr><tr><td style='text-align: center;'>DXJT_PL_GH</td><td style='text-align: center;'>规划面图层数据层</td></tr><tr><td style='text-align: center;'>DXJZ_VL_GH</td><td style='text-align: center;'>规划体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXJT_TX_GH</td><td style='text-align: center;'>规划交通设施注记图层数据层</td></tr></table>

<div style="text-align: center;">表 A.1 地下空间数据大类分层与命名表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类名称</td><td style='text-align: center;'>数据分层代号</td><td style='text-align: center;'>数据分层名描述</td></tr><tr><td rowspan="15">地下管线数据</td><td style='text-align: center;'>DXGX_PT_LS</td><td style='text-align: center;'>历史点图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_LN_LS</td><td style='text-align: center;'>历史线图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_PL_LS</td><td style='text-align: center;'>历史面图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_VL_LS</td><td style='text-align: center;'>历史体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXGX_TX_LS</td><td style='text-align: center;'>历史管线注记图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_PT_XZ</td><td style='text-align: center;'>现状点图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_LN_XZ</td><td style='text-align: center;'>现状线图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_PL_XZ</td><td style='text-align: center;'>现状面图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_VL_XZ</td><td style='text-align: center;'>现状体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXGX_TX_XZ</td><td style='text-align: center;'>现状管线注记图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_PT_GH</td><td style='text-align: center;'>规划点图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_LN_GH</td><td style='text-align: center;'>规划线图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_PL_GH</td><td style='text-align: center;'>规划面图层数据层</td></tr><tr><td style='text-align: center;'>DXGX_VL_GH</td><td style='text-align: center;'>规划体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DXGX_TX_GH</td><td style='text-align: center;'>规划管线注记图层数据层</td></tr><tr><td rowspan="15">综合管廊数据</td><td style='text-align: center;'>ZHGL_PT_LS</td><td style='text-align: center;'>历史点图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_LN_LS</td><td style='text-align: center;'>历史线图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_PL_LS</td><td style='text-align: center;'>历史面图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_VL_LS</td><td style='text-align: center;'>历史体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>ZHGL_TX_LS</td><td style='text-align: center;'>历史综合管廊注记图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_PT_XZ</td><td style='text-align: center;'>现状点图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_LN_XZ</td><td style='text-align: center;'>现状线图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_PL_XZ</td><td style='text-align: center;'>现状面图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_VL_XZ</td><td style='text-align: center;'>现状体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>ZHGL_TX_XZ</td><td style='text-align: center;'>现状综合管廊注记图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_PT_GH</td><td style='text-align: center;'>规划点图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_LN_GH</td><td style='text-align: center;'>规划线图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_PL_GH</td><td style='text-align: center;'>规划面图层数据层</td></tr><tr><td style='text-align: center;'>ZHGL_VL_GH</td><td style='text-align: center;'>规划体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>ZHGL_TX_GH</td><td style='text-align: center;'>规划综合管廊注记图层数据层</td></tr><tr><td rowspan="4">地基基础数据</td><td style='text-align: center;'>DJJC_PT_LS</td><td style='text-align: center;'>历史点图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_LN_LS</td><td style='text-align: center;'>历史线图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_PL_LS</td><td style='text-align: center;'>历史面图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_VL_LS</td><td style='text-align: center;'>历史体(三维模型)数据层</td></tr></table>

<div style="text-align: center;">表 A.1 地下空间数据大类分层与命名表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类名称</td><td style='text-align: center;'>数据分层代号</td><td style='text-align: center;'>数据分层名描述</td></tr><tr><td rowspan="11">地基基础数据</td><td style='text-align: center;'>DJJC_TX_LS</td><td style='text-align: center;'>历史地基基础注记图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_PT_XZ</td><td style='text-align: center;'>现状点图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_LN_XZ</td><td style='text-align: center;'>现状线图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_PL_XZ</td><td style='text-align: center;'>现状面图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_VL_XZ</td><td style='text-align: center;'>现状体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DJJC_TX_XZ</td><td style='text-align: center;'>现状地基基础注记图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_PT_GH</td><td style='text-align: center;'>规划点图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_LN_GH</td><td style='text-align: center;'>规划线图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_PL_GH</td><td style='text-align: center;'>规划面图层数据层</td></tr><tr><td style='text-align: center;'>DJJC_VL_GH</td><td style='text-align: center;'>规划体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DJJC_TX_GH</td><td style='text-align: center;'>规划地基基础注记图层数据层</td></tr><tr><td rowspan="23">地质数据</td><td style='text-align: center;'>DZSJ_PT_GZ</td><td style='text-align: center;'>构造地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_GZ</td><td style='text-align: center;'>构造地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_GZ</td><td style='text-align: center;'>构造地质面图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_VL_GZ</td><td style='text-align: center;'>构造地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_GZ</td><td style='text-align: center;'>构造地质注记图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PT_GC</td><td style='text-align: center;'>工程地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_GC</td><td style='text-align: center;'>工程地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_GC</td><td style='text-align: center;'>工程地质面图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_VL_GC</td><td style='text-align: center;'>工程地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_GC</td><td style='text-align: center;'>工程地质注记图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PT_SW</td><td style='text-align: center;'>水文地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_SW</td><td style='text-align: center;'>水文地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_SW</td><td style='text-align: center;'>水文地质面图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_VL_SW</td><td style='text-align: center;'>水文地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_SW</td><td style='text-align: center;'>水文地质注记图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PT_HJ</td><td style='text-align: center;'>环境地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_HJ</td><td style='text-align: center;'>环境地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_HJ</td><td style='text-align: center;'>环境地质面图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_VL_HJ</td><td style='text-align: center;'>环境地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_HJ</td><td style='text-align: center;'>环境地质注记图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PT_ZY</td><td style='text-align: center;'>资源地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_ZY</td><td style='text-align: center;'>资源地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_ZY</td><td style='text-align: center;'>资源地质面图层数据层</td></tr></table>

<div style="text-align: center;">表 A.1 地下空间数据大类分层与命名表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类名称</td><td style='text-align: center;'>数据分层代号</td><td style='text-align: center;'>数据分层名描述</td></tr><tr><td rowspan="12">地质数据</td><td style='text-align: center;'>DZSJ_VL_ZY</td><td style='text-align: center;'>资源地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_ZY</td><td style='text-align: center;'>资源地质注记图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PT_ZH</td><td style='text-align: center;'>灾害地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_ZH</td><td style='text-align: center;'>灾害地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_ZH</td><td style='text-align: center;'>灾害地质面图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_VL_ZH</td><td style='text-align: center;'>灾害地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_ZH</td><td style='text-align: center;'>灾害地质注记图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PT_QT</td><td style='text-align: center;'>其他地质点图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_LN_QT</td><td style='text-align: center;'>其他地质线图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_PL_QT</td><td style='text-align: center;'>其他地质面图层数据层</td></tr><tr><td style='text-align: center;'>DZSJ_VL_QT</td><td style='text-align: center;'>其他地质体(三维模型)数据层</td></tr><tr><td style='text-align: center;'>DZSJ_TX_QT</td><td style='text-align: center;'>其他地质注记图层数据层</td></tr></table>

## 附录 B

(资料性)

地下空间设施数据图式符号

B.1 除地下管线数据、综合管廊数据外，其他地下空间设施数据的图式符号参见表 B.1。

<div style="text-align: center;">表 B.1 部分地下空间设施数据图式符号表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类</td><td style='text-align: center;'>符号类型</td><td style='text-align: center;'>图式符号</td><td style='text-align: center;'>表达内容</td><td style='text-align: center;'>定位点</td><td style='text-align: center;'>备注</td></tr><tr><td rowspan="19">地下建筑物数据</td><td rowspan="12">点状符号</td><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下办公室</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下商业服务</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下商场</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td style='text-align: center;'>合</td><td style='text-align: center;'>居住工程</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.0mm×2.0mm(宽×高)</td></tr><tr><td style='text-align: center;'>图</td><td style='text-align: center;'>地下消防设施</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.0mm×2.0mm(宽×高)</td></tr><tr><td style='text-align: center;'>合</td><td style='text-align: center;'>水闸</td><td style='text-align: center;'>底线中心点</td><td style='text-align: center;'>2.0mm×2.5mm(宽×高)</td></tr><tr><td style='text-align: center;'>&gt;</td><td style='text-align: center;'>涵洞</td><td style='text-align: center;'>夹角顶点</td><td style='text-align: center;'>2.0mm×2.0mm(宽×高)</td></tr><tr><td style='text-align: center;'>+</td><td style='text-align: center;'>地下医疗救护设施</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.0mm×2.0mm(宽×高)</td></tr><tr><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下医院</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td style='text-align: center;'>合</td><td style='text-align: center;'>地下纪念馆</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td style='text-align: center;'>合</td><td style='text-align: center;'>地下污水处理厂</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td style='text-align: center;'>合</td><td style='text-align: center;'>废弃地下建筑</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0mm</td></tr><tr><td rowspan="2">线状符号</td><td style='text-align: center;'>——</td><td style='text-align: center;'>区域边界线</td><td style='text-align: center;'></td><td style='text-align: center;'>线粗0.75mm</td></tr><tr><td style='text-align: center;'>——</td><td style='text-align: center;'>区域内分线</td><td style='text-align: center;'></td><td style='text-align: center;'>线粗0.5mm,虚实1:1</td></tr><tr><td rowspan="5">面状符号</td><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下专业工程</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下商场</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下隐蔽工程</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>◎</td><td style='text-align: center;'>地下商业服务</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>图</td><td style='text-align: center;'>地下消防室</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">表 B.1 部分地下空间设施数据图式符号表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类</td><td style='text-align: center;'>符号类型</td><td style='text-align: center;'>图式符号</td><td style='text-align: center;'>表达内容</td><td style='text-align: center;'>定位点</td><td style='text-align: center;'>备注</td></tr><tr><td rowspan="4">地下建筑物数据</td><td rowspan="4">面状符号</td><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下医疗救护设施</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下医院</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下纪念馆</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下污水处理厂</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td rowspan="17">地下交通设施数据</td><td rowspan="10">点状符号</td><td style='text-align: center;'>⊕</td><td style='text-align: center;'>通道出入口</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.0 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>↔</td><td style='text-align: center;'>交通出入口</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.5 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>○</td><td style='text-align: center;'>交通、道路设施</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0 mm</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>阶梯</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.0 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>电梯</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.0 mm×3.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下汽车库</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>3.0 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下停车场</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>3.0 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>停车位</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>2.5 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>充电桩</td><td style='text-align: center;'>底线中心点</td><td style='text-align: center;'>2.0 mm×2.0 mm(宽×高)</td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>下水井</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'>规格直径2.0 mm</td></tr><tr><td rowspan="4">线状符号</td><td style='text-align: center;'>—</td><td style='text-align: center;'>通道边线</td><td style='text-align: center;'></td><td style='text-align: center;'>线粗0.5 mm</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>通道中心线</td><td style='text-align: center;'></td><td style='text-align: center;'>线粗0.5 mm,虚实1:1</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>地下铁路</td><td style='text-align: center;'></td><td style='text-align: center;'>虚线粗0.5 mm实线粗1.0 mm</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>区间联络通道</td><td style='text-align: center;'></td><td style='text-align: center;'>线粗0.5 mm,虚实1:1</td></tr><tr><td rowspan="3">面状符号</td><td style='text-align: center;'>⊕</td><td style='text-align: center;'>通道、道路范围</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下汽车库</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>⊕</td><td style='text-align: center;'>地下停车场</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td rowspan="3">地基基础数据</td><td style='text-align: center;'>点状符号</td><td style='text-align: center;'>•</td><td style='text-align: center;'>地基基础点</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>线状符号</td><td style='text-align: center;'>—</td><td style='text-align: center;'>地基基础线</td><td style='text-align: center;'></td><td style='text-align: center;'>线粗0.75 mm</td></tr><tr><td style='text-align: center;'>面状符号</td><td style='text-align: center;'>—</td><td style='text-align: center;'>地基基础范围</td><td style='text-align: center;'>几何中心点</td><td style='text-align: center;'></td></tr></table>

B.2 除地下管线数据、综合管廊数据外，其他地下空间设施数据图式符号的基本颜色参见表 B.2。

<div style="text-align: center;">表 B.2 部分地下空间设施数据图式符号基本颜色表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据大类</td><td style='text-align: center;'>表达内容</td><td style='text-align: center;'>颜色名称</td><td style='text-align: center;'>颜色色值(RGB)</td></tr><tr><td style='text-align: center;'>地下建筑物数据</td><td style='text-align: center;'>全部</td><td style='text-align: center;'>灰色</td><td style='text-align: center;'>127,127,127</td></tr><tr><td rowspan="3">地下交通设施数据</td><td style='text-align: center;'>轨道交通设施</td><td style='text-align: center;'>紫色</td><td style='text-align: center;'>127,0,127</td></tr><tr><td style='text-align: center;'>地下道路设施</td><td style='text-align: center;'>暗蓝色</td><td style='text-align: center;'>0,165,242</td></tr><tr><td style='text-align: center;'>地下停车设施</td><td style='text-align: center;'>暗黄色</td><td style='text-align: center;'>255,225,0</td></tr><tr><td style='text-align: center;'>地基基础数据</td><td style='text-align: center;'>全部</td><td style='text-align: center;'>灰色</td><td style='text-align: center;'>127,127,127</td></tr></table>

## 參 考 文 献

[1] GB/T 20157—2006 信息技术 软件维护

[2] GB/T 24356—2023 测绘成果质量检查与验收

[3] GB/T 29806—2013 信息技术 地下管线数据交换技术要求

[4] GB/T 35636—2017 城市地下空间测绘规范

[5] CH/T 1036—2015 管线要素分类代码与符号表达

[6] CJJ 61—2017 城市地下管线探测技术规程

[7] CJJ/T 100—2017 城市基础地理信息系统技术标准

[8] CJJ/T 144—2019 城市地理空间信息元数据标准

[9] DD 2015-06 三维地质模型数据交换格式(Geo3DML)

[10] DB31/T 401.1—2019 城市建设空间信息基础数据规范 第1部分：分类与代码

[11] DB42/T 1356—2018 城市地质调查数据分类编码及图式图例

[12] DB50/T 1263—2022 地下空间综合信息系统技术规范

[13] DBJ50/T-249—2016 重庆市城市地下空间信息数据库标准

