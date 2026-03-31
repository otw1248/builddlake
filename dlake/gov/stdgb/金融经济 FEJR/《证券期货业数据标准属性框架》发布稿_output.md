

# 中华人民共和国金融行业标准

JR/T 0319—2024

# 证券期货业数据标准属性框架

# Data standard attribute framework of securities and futures industry

2024-11-20 发布

2024-11-20 实施

Powered by TCPDF (www.tcpdf.org)

## 目 次

前言 …… II    
引言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 基础类数据标准属性框架 …… 2    
4.1 概述 …… 2    
4.2 业务属性 …… 3    
4.3 技术属性 …… 4    
4.4 管理属性 …… 6    
5 指标类数据标准属性框架 …… 7    
5.1 概述 …… 8    
5.2 业务属性 …… 9    
5.3 技术属性 …… 10    
5.4 管理属性 …… 11    
附录 A（资料性）基础类数据标准示例 …… 13    
附录 B（资料性）指标类数据标准示例 …… 15    
参考文献 …… 17

## 前言

本文件按照GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国金融标准化技术委员会证券分技术委员会（SAC/TC 180/SC4）提出。

本文件由全国金融标准化技术委员会（SAC/TC 180）归口。

本文件起草单位：中证数据有限责任公司、中国证券监督管理委员会科技监管司、中国证券监督管理委员会信息中心、中证信息技术服务有限责任公司、中国工商银行股份有限公司。

本文件主要起草人：王婷、朱旭、汪萌、周婵、汪洵、卢大彪、刘铁斌、侯智杰、黄璐、赵安、孔超、江子扬。

## 引言

数据标准是数据治理工作的核心领域之一，通过建立定义清晰、属性明确、约束规范的一组数据标准，有助于业务、数据、技术等各相关方对数据的统一理解和使用，确保数据在采集、加工、交换和共享等环节的一致性和准确性。编制证券期货业数据标准属性框架，旨在建立一套适用于证券期货业数据标准的属性说明体系，分别针对基础类数据标准及指标类数据标准，定义相应的属性结构和所属内容，明确业务、技术、管理等各类属性的填写要求和约束条件，帮助增强资本市场业务操作者、系统建设者、数据应用者等各相关参与方对数据理解和使用的一致性，为构建上层数据模型、信息模型、事件模型等打下基础，助力规范证券期货业数据标准定义、提升证券期货机构间数据交换共享及互操作效率。

Powered by TCPDF (www.tcpdf.org)

# 证券期货业数据标准属性框架

## 1 范围

本文件规定了证券期货业基础类数据标准和指标类数据标准的属性框架。

本文件适用于证券期货行业监管机构、市场核心机构、行业自律组织、中介经营机构、服务机构等开展数据治理活动、实施数据集成融合、进行数据交互共享、推进数据应用建设等数据类相关工作。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 42775 证券期货业数据安全风险防控 数据分类分级指引

JR/T 0176.1—2019 证券期货业数据模型 第1部分：抽象模型设计方法

JR/T 0304.1—2024 证券期货业基础数据元规范 第1部分：基础数据元

JR/T 0304.2—2024 证券期货业基础数据元规范 第2部分：基础代码

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 数据 data

信息的可再解释的形式化表示，以适用于通信、解释或处理。

注：数据可以由人工或自动的方式加工、处理。

[来源：GB/T 5271.1-2000，01.01.02]

### 3.2 

基础类数据标准 basic data standard

对基础类数据进行标准化后形成的定义规范，规定了统一的名称、含义、格式、类型等。 $ ^{*} $ 注：基础类数据指在日常业务开展过程中产生、未经过加工和处理的基础性数据。

### 3.3 

指标类数据标准 indicator data standard

对指标类数据进行标准化后形成的定义规范，规定了统一的名称、含义、维度、计算公式等。 $ ^{*} $ 注：指标类数据是指按一定统计规则和加工口径对基础类数据进行加工处理而产生的衍生数据。

### 3.4 

## 属性框架 attribute framework

描述数据标准所包含的各类属性的组织结构。

注：一般包括业务、技术和管理三类属性。

## 4 基础类数据标准属性框架

### 4.1 概述

基础类数据标准属性框架包括业务属性、技术属性和管理属性：

a）业务属性：描述数据与证券期货业务相关联的特性。业务属性包括主题、信息大类、信息小类、中文名称、业务含义、标准别名、被引用项名称、参考依据、代码取值、代码取值含义；

b）技术属性：描述数据与信息技术实现相关联的特性。技术属性包括英文名称、数据格式、数据类型及长度、度量单位、取值范围、数据来源；

c）管理属性：描述数据与数据管理控制相关联的特性。管理属性包括编码、代码编号、代码取值编码规则、归口管理部门、标准管理部门、业务管理部门、标准相关部门、安全级别、使用级别、防控级别、版本日期、当前版本号、发布状态、应用系统或产品。

框架中的属性分为必选、可选两种约束类型。在实际应用中可在上述属性框架的基础上进行扩展补充，证券期货业基础类数据标准属性框架如图1所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_180_736_1076_1481.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 1 证券期货业基础类数据标准架构</div>


基于上述数据标准架构的基础类数据标准示例参见附录A。

### 4.2 业务属性

#### 4.2.1 主题

描述标准数据项归属的数据标准主题。证券期货业相关主题包括：主体、品种、账户、行为、资产、协议、财务、监管、披露等。

约束类型：必选。

#### 4.2.2 信息大类

描述标准数据项的主分类，如：在主体主题域下，信息大类分为投资者信息、发行人信息、中介服务机构信息等。

约束类型：必选。

#### 4.2.3 信息小类

描述标准数据项的子分类，如：在投资者信息大类下，信息小类分为证券投资者信息、债券投资者信息、期货交易者信息等。

约束类型：必选。

#### 4.2.4 中文名称

描述标准数据项的中文名称。中文名称应易于被标准使用人员理解和识别。中文命名规则应符合JR/T 0304.1—2024中的规定。

约束类型：必选。

#### 4.2.5 业务含义

描述标准数据项的业务概念。业务含义应该精准、细致，以利于标准使用人员理解，不应有循环引用或直接用中文名称进行描述。业务含义可参考相关国家标准和行业标准、监管机构的定义、证券期货经营机构内部业务制度、信息系统业务需求定义以及行业经验的总结性归纳。

约束类型：必选。

#### 4.2.6 标准别名

描述除标准数据项中文名称属性定义的名称以外的常用名称列举，如：“报告所属年度”的标准别名为“报告年度”，在标准应用过程中应使用标准中文名称而非标准别名。

约束类型：可选。

#### 4.2.7 被引用项名称

描述被引用标准数据项的名称，如：“中介服务机构名称”的被引用标准名称为“机构名称”。约束类型：可选。

#### 4.2.8 参考依据

描述制定标准数据项的参考依据，包括：法律法规、部门规章、规范性文件、国家标准、行业标准等。

注：数据标准内容在国家标准或行业标准有规定的应该遵循国家标准或行业标准相关规定。

约束类型：可选。

#### 4.2.9 代码取值

描述代码的标识或简称，一般采用简短的数字或字母，如：HKG在“国家及地区代码”中代表“中国香港”，代码取值应符合JR/T 0304.2—2024中的规定。

约束类型：可选，标准数据项为枚举值类型时必填。

#### 4.2.10 代码取值含义

描述代码取值对应的具体业务含义。

约束类型：可选，标准数据项为枚举值类型时必填。

### 4.3 技术属性

#### 4.3.1 英文名称

描述标准数据项采用的英文名称，由字母、数字及下划线构成，原则上不超过60个字符，采用尽量简洁的英文缩写，通过下划线进行区隔。英文名称编制规则如下：

a）英文词根均应采用大写；

b）英文词根应用下划线“_”作为连接符；

c）单个英文词根不应超过5个字符；

d）单个英文词根不足5个字节时，一般全取，多于5个时，一般去掉形容词后缀，或仅取有标志性的前缀词头；

e）关键字不应作为词根，如：CREAT、SUBMIT、INSERT、DELETE等；

f）英文词根中不含标点符号等特殊字符；

g）对于复合词和词组，如有约定俗成的缩写，则作为单个词根采用；如需自定义，一般取其中单个词的首字母组合；

h）有特指的英文缩写优先采用，如：IPO对应“IPO”。

约束类型：必选。

#### 4.3.2 数据格式

描述标准数据项的数据格式分类，数据格式分成六类：N 数值型、C 字符型、D 日期型、T 时间型、B 布尔型、E 枚举型，描述应符合JR/T 0176.1—2019中的规定。

数据格式的详细描述如下:

a）数值型 N：实际实现的数据类型应为INTEGER或DECIMAL（长度,小数点），其中对于整型数值数据，数据类型应为INTEGER；对于浮点型数值数据，数据类型应为DECIMAL（长度,小数点）；

b）字符型 C：实际实现的数据类型应为CHAR(长度)、VARCHAR(长度)或TEXT;

c） 日期型 D：实际实现的数据类型应为 DATE；

d） 时间型 T：实际实现的数据类型应为TIMESTAMP；

e）布尔型 B：实际实现的数据类型应为CHAR(1)。在标准代码取值属性中应说明“0”“1”所代表的含义，一般“0”应表示“否”的含义，“1”应表示“是”的含义；

f） 枚举型 E：实际实现的数据类型应为CHAR(长度)或VARCHAR(长度)。

约束类型：必选。

#### 4.3.3 数据类型及长度

描述标准数据项采用的数据类型和长度。数据格式与数据类型及长度的对应关系示例见表1。

约束类型：必选。

<div style="text-align: center;">表 1 数据格式与数据类型及长度的对应关系示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据格式</td><td colspan="3">数据类型及长度</td></tr><tr><td rowspan="10">C 字符型</td><td style='text-align: center;'>VARCHAR(10)</td><td style='text-align: center;'>VARCHAR(500)</td><td style='text-align: center;'>CHAR(2) TEXT</td></tr><tr><td style='text-align: center;'>VARCHAR(20)</td><td style='text-align: center;'>VARCHAR(600)</td><td style='text-align: center;'>CHAR(4)</td></tr><tr><td style='text-align: center;'>VARCHAR(30)</td><td style='text-align: center;'>VARCHAR(800)</td><td style='text-align: center;'>CHAR(6)</td></tr><tr><td style='text-align: center;'>VARCHAR(40)</td><td style='text-align: center;'>VARCHAR(1000)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>VARCHAR(50)</td><td style='text-align: center;'>VARCHAR(2000)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>VARCHAR(60)</td><td style='text-align: center;'>VARCHAR(3000)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>VARCHAR(100)</td><td style='text-align: center;'>VARCHAR(4000)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>VARCHAR(200)</td><td style='text-align: center;'>VARCHAR(6000)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>VARCHAR(300)</td><td style='text-align: center;'>VARCHAR(32000)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>VARCHAR(400)</td><td style='text-align: center;'>VARCHAR(80000)</td><td style='text-align: center;'></td></tr><tr><td rowspan="6">N 数值型</td><td style='text-align: center;'>DECIMAL(4,0)</td><td style='text-align: center;'>DECIMAL(20,4)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>DECIMAL(9,0)</td><td style='text-align: center;'>DECIMAL(20,6)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>DECIMAL(9,4)</td><td style='text-align: center;'>DECIMAL(24,4)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>DECIMAL(18,0)</td><td style='text-align: center;'>DECIMAL(24,6)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>DECIMAL(18,4)</td><td style='text-align: center;'>DECIMAL(26,4)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>DECIMAL(18,6)</td><td style='text-align: center;'>DECIMAL(38,4)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>D 日期型</td><td style='text-align: center;'>DATE</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td rowspan="2">T 时间型</td><td style='text-align: center;'>TIMESTAMP(0)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>TIMESTAMP(6)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td rowspan="5">E 枚举型</td><td style='text-align: center;'>CHAR(1)</td><td style='text-align: center;'>CHAR(6)/VARCHAR(6)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CHAR(2)/VARCHAR(2)</td><td style='text-align: center;'>VARCHAR(10)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CHAR(3)/VARCHAR(3)</td><td style='text-align: center;'>VARCHAR(20)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CHAR(4)/VARCHAR(4)</td><td style='text-align: center;'>VARCHAR(30)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CHAR(5)/VARCHAR(5)</td><td style='text-align: center;'>VARCHAR(40)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>B 布尔型</td><td style='text-align: center;'>CHAR(1)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 4.3.4 度量单位

描述标准数据项采用的度量单位，常用的度量单位包括元、户、股等。约束类型：可选。

#### 4.3.5 取值范围

描述标准数据项取值的范围区间。

约束类型：可选。

#### 4.3.6 数据来源

描述标准数据项对应的权威数据来源方。

约束类型：可选。

### 4.4 管理属性

#### 4.4.1 编码

描述为标准数据项分配的唯一编号，由数据标准制定者规定统一的编码规则，如：由代表标准数据项归属主题的3位字母和4位数字序号构成。

约束类型：必选。

#### 4.4.2 代码编号

描述为代码分配的唯一编号。

约束类型：可选，标准数据项为枚举值类型时必填。

#### 4.4.3 代码取值编码规则

描述代码取值的编码规则，如：1级1位编码、1级2位编码、2级2位编码等。代码取值编码规则应符合表2的要求。

约束类型：可选，标准数据项为枚举值类型时必填。

<div style="text-align: center;">表 2 代码取值编码规则</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编码规则</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>字母编码</td><td style='text-align: center;'>代码取值编码由字母组成，遵循国家标准或其他编码标准中已定义的编码规则</td><td style='text-align: center;'>HKG 在“国家及地区代码”中代表“中国香港”；CNY 在“币种”中代表“人民币”</td></tr><tr><td rowspan="2">数字编码</td><td style='text-align: center;'>代码取值编码由数字组成，在国家标准或其他编码标准中有编码规则定义的，直接采用已有标准定义</td><td style='text-align: center;'>“民族”为1级2位编码采用GB/T 3304-1991 中国各民族名称的罗马字母拼写法和代码中定义的编码规则（01-汉族，02-蒙古族，03-回族，04-藏族，05-维吾尔族，06-苗族，……）</td></tr><tr><td style='text-align: center;'>代码取值编码由数字组成，在国家标准或其他编码标准中没有编码规则定义的，采用“2位数字为1级”的编码规则，如：1级2位编码、2级4位编码、3级6位编码</td><td style='text-align: center;'>“证件类型”为3级6位编码1级：01 个人，02 机构，03 产品2级：0101 身份证，……，0106 士兵证3级：010601 解放军士兵证，010602 武警士兵证</td></tr><tr><td style='text-align: center;'>混合编码</td><td style='text-align: center;'>代码取值编码由字母和数字混合组成，当数字编码不能满足业务需要时，增加具有特定含义的字母组成混合编码</td><td style='text-align: center;'>“国民经济行业类型”：A01-农业，A02-林业，A03-畜牧业，……，B06-煤炭开采和洗选业，B07-石油和天然气开采业，……</td></tr></table>

#### 4.4.4 归口管理部门

描述对标准数据项进行制修订及定义解释等相关管理工作的部门，包括标准管理部门和业务管理部门。

约束类型：可选。

#### 4.4.5 标准管理部门

描述对标准数据项进行制定、修订、发布等管理工作的部门。

约束类型：可选。

#### 4.4.6 业务管理部门

描述对标准数据项具有业务属性定义权、解释权的管理部门。

约束类型：可选。

#### 4.4.7 标准相关部门

描述涉及标准数据项使用的相关部门。

约束类型：可选。

#### 4.4.8 安全级别

描述标准数据项对应的行业重要数据分级认定相关制度规范所规定的数据级别，如标准数据项在不同应用场景中数据级别不同，应针对具体应用场景对应的数据级别加以说明。

约束类型：可选。

#### 4.4.9 使用级别

描述标准数据项对应的使用范围级别，从低到高划分为四级：

a）一级：依法公开数据；

b）二级：机构或者组织体系内共享数据；

c）三级：本业务领域范围共享数据，可在指定单位、部门范围内使用；

d）四级：特定共享，依申请经数据源单位同意后使用。

如标准数据项在不同应用场景中使用级别不同，应针对具体应用场景对应的使用级别加以说明。

约束类型：可选。

#### 4.4.10 防控级别

描述标准数据项对应的数据级别，数据级别应符合GB/T 42775的规定。

约束类型：可选。

#### 4.4.11 版本日期

描述标准数据项的版本日期。

约束类型：可选。

#### 4.4.12 当前版本号

描述标准数据项的版本号。

约束类型：可选。

#### 4.4.13 发布状态

描述标准数据项的发布情况。

约束类型：可选。

#### 4.4.14 应用系统或产品

描述应用标准数据项的信息系统或统计报告等数据产品。

约束类型：可选。

## 5 指标类数据标准属性框架

### 5.1 概述

指标类数据标准属性框架包括业务属性、技术属性和管理属性：

a）业务属性：描述数据与证券期货业务相关联的特性。业务属性包括信息大类、信息小类、指标中文名称、标准别名、业务含义、统计口径、计算公式、范围及条件、常用维度、统计周期、参考依据、相关指标标准；

b）技术属性：描述数据与信息技术实现相关联的特性。技术属性包括英文名称、数据类型及长度、度量单位、取值范围、加工逻辑、计算流程、伪代码、指标类型、数据来源；

c）管理属性：描述数据与数据管理控制相关联的特性。管理属性包括编码、归口管理部门、标准管理部门、业务管理部门、标准相关部门、安全级别、使用级别、防控级别、版本日期、当前版本号、发布状态、应用系统或产品。

框架中的属性分为必选、可选两种约束类型。在实际应用中可在上述属性框架的基础上进行扩展补充，证券期货业指标类数据标准属性框架如图2所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_208_588_1042_1475.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2 证券期货业指标类数据标准架构</div>


基于上述数据标准架构的指标类数据标准示例参见附录B。

### 5.2 业务属性

#### 5.2.1 信息大类

描述标准数据项的主分类，如：股票市场、债券市场、基金市场、期货市场等。

约束类型：必选。

#### 5.2.2 信息小类

描述标准数据项的子分类，如：在股票市场信息大类下，信息小类分为市场规模、新股发行、股票交易等。

约束类型：必选。

#### 5.2.3 指标中文名称

描述标准数据项的中文名称。

约束类型：必选。

#### 5.2.4 标准别名

描述除标准数据项中文名称属性定义的名称以外的常用名称列举。在标准应用过程中应使用标准中文名称而非标准别名。

约束类型：可选。

#### 5.2.5 业务含义

描述标准数据项的业务概念。业务含义应该精准、细致，以利于标准使用人员理解。

约束类型：必选。

#### 5.2.6 统计口径

描述标准数据项的业务加工方法和流程，包括计算公式、范围及条件两部分。

约束类型：可选。

#### 5.2.7 计算公式

描述标准数据项加工过程的数学公式。

约束类型：可选。

#### 5.2.8 范围及条件

描述计算标准数据项所采用的各种业务限制条件，如：统计范围的筛选规则、信息间的关联关系和约束条件以及例外情况等。

约束类型：可选。

#### 5.2.9 常用维度

描述标准数据项常见的统计维度集。

约束类型：可选。

#### 5.2.10 统计周期

描述标准数据项常用的计算频率周期，包括：日、周、月、季度、半年、年等。

约束类型：必选。

#### 5.2.11 参考依据

描述制定标准数据项的参考依据，包括：包括法律法规、部门规章、规范性文件、国家标准、行业标准等。

注：数据标准内容在国家标准或行业标准有规定的应该遵循国家标准或行业标准相关规定。

约束类型：可选。

#### 5.2.12 相关指标标准

描述标准数据项在计算过程中用到的其他指标标准数据项。

约束类型：可选。

### 5.3 技术属性

#### 5.3.1 英文名称

描述标准数据项采用的英文名称，由字母、数字及下划线构成，原则上不超过60个字符，采用尽量简洁的英文缩写，通过下划线进行区隔。英文名称编制的具体规则应符合4.3.1的规定。

约束类型：必选。

#### 5.3.2 数据类型及长度

描述标准数据项采用的数据类型和长度。

约束类型：必选。

#### 5.3.3 度量单位

描述标准数据项采用的度量单位。常用的度量单位包括元、户、股、百分比等。

约束类型：可选。

#### 5.3.4 取值范围

描述标准数据项取值的范围区间。

约束类型：可选。

#### 5.3.5 加工逻辑

描述标准数据项加工过程的处理逻辑，包括计算流程和伪代码两部分。

约束类型：可选。

#### 5.3.6 计算流程

描述标准数据项的加工流程和步骤。

约束类型：可选。

#### 5.3.7 伪代码

描述标准数据项的加工逻辑通过伪代码进行实现的表现形式。

约束类型：可选。

#### 5.3.8 指标类型

描述标准数据项的所属类型，包括：基础指标和衍生指标，基础指标是指具有特定的业务含义且不能进一步拆解的指标，包括原子指标和派生指标；衍生指标是指若干个基础指标通过各种逻辑运算复合而成的指标。

约束类型：必选。

#### 5.3.9 数据来源

描述标准数据项对应的权威数据来源方。

约束类型：可选。

### 5.4 管理属性

#### 5.4.1 编码

描述为标准数据项分配的唯一编号，由数据标准制定者规定统一的编码规则，如：由2位字母和6位数字序号构成。

约束类型：必选。

#### 5.4.2 归口管理部门

描述对标准数据项进行制修订及定义解释等相关管理工作的部门，包括标准管理部门和业务管理部门。

约束类型：可选。

#### 5.4.3 标准管理部门

描述对标准数据项进行制定、修订、发布等管理工作的部门。

约束类型：可选。

#### 5.4.4 业务管理部门

描述对标准数据项具有业务属性定义权、解释权的管理部门。

约束类型：可选。

#### 5.4.5 标准相关部门

描述涉及标准数据项使用的相关部门。

约束类型：可选。

#### 5.4.6 安全级别

描述标准数据项对应的行业重要数据分级认定相关制度规范所规定的数据级别，如标准数据项在不同应用场景中数据级别不同，应针对具体应用场景对应的数据级别加以说明。

约束类型：可选。

#### 5.4.7 使用级别

描述标准数据项对应的使用范围级别，从低到高划分为四级：

a） 一级：依法公开数据；

b）二级：机构或者组织体系内共享数据；

c）三级：本业务领域范围共享数据，可在指定单位、部门范围内使用；

d）四级：特定共享，依申请经数据源单位同意后使用。

如标准数据项在不同应用场景中使用级别不同，应针对具体应用场景对应的使用级别加以说明。

约束类型：可选。

#### 5.4.8 防控级别

描述标准数据项对应的数据级别，数据级别应符合GB/T 42775的规定。

约束类型：可选。

#### 5.4.9 版本日期

描述标准数据项的版本日期。

约束类型：可选。

#### 5.4.10 当前版本号

描述标准数据项的版本号。

约束类型：可选。

#### 5.4.11 发布状态

描述标准数据项的发布情况。

约束类型：可选。

#### 5.4.12 应用系统或产品

描述应用标准数据项的信息系统或统计报告等数据产品。

约束类型：可选。

# 附录 A

(资料性)

基础类数据标准示例

表A.1给出了根据基础类数据标准属性框架对“融资融券业务类型”数据标准的描述示例。

<div style="text-align: center;">表 A.1 “融资融券业务类型” 数据标准</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>内容</td></tr><tr><td style='text-align: center;'>编码</td><td style='text-align: center;'>BHV1045</td></tr><tr><td style='text-align: center;'>主题</td><td style='text-align: center;'>行为</td></tr><tr><td style='text-align: center;'>信息大类</td><td style='text-align: center;'>证券交易所行为数据</td></tr><tr><td style='text-align: center;'>信息小类</td><td style='text-align: center;'>证券交易数据</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>融资融券业务类型</td></tr><tr><td style='text-align: center;'>业务含义</td><td style='text-align: center;'>用于区分融资融券的业务类型的代码。融资融券业务是指在证券交易所或者国务院批准的其他证券交易场所进行的证券交易中，证券公司向客户出借资金供其买入证券或者出借证券供其卖出，并由客户交存相应担保物的经营活动</td></tr><tr><td style='text-align: center;'>标准别名</td><td style='text-align: center;'>融资融券业务类型代码</td></tr><tr><td style='text-align: center;'>被引用项名称</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>参考依据</td><td style='text-align: center;'>《证券公司融资融券业务管理办法》证监会令第117号</td></tr><tr><td style='text-align: center;'>代码编号</td><td style='text-align: center;'>D0001</td></tr><tr><td style='text-align: center;'>代码取值</td><td style='text-align: center;'>代码取值 代码取值含义01 担保品买入02 担保品卖出03 融资买入04 卖券还款05 买券还券06 融券卖出07 融券平仓08 融资平仓09 直接还款10 直接还券</td></tr><tr><td style='text-align: center;'>代码取值编码规则</td><td style='text-align: center;'>1级2位编码</td></tr><tr><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>SMT_BIZ_TYPE</td></tr><tr><td style='text-align: center;'>数据格式</td><td style='text-align: center;'>E</td></tr></table>

<div style="text-align: center;">表 A.1 “融资融券业务类型” 数据标准（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>内容</td></tr><tr><td style='text-align: center;'>数据类型及长度</td><td style='text-align: center;'>VARCHAR(2)</td></tr><tr><td style='text-align: center;'>度量单位</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>数据来源</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标准管理部门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>业务管理部门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标准相关部门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>安全级别</td><td style='text-align: center;'>一般</td></tr><tr><td style='text-align: center;'>使用级别</td><td style='text-align: center;'>三级</td></tr><tr><td style='text-align: center;'>防控级别</td><td style='text-align: center;'>2</td></tr><tr><td style='text-align: center;'>版本日期</td><td style='text-align: center;'>2022年12月</td></tr><tr><td style='text-align: center;'>当前版本号</td><td style='text-align: center;'>V2.0</td></tr><tr><td style='text-align: center;'>发布状态</td><td style='text-align: center;'>已发布</td></tr><tr><td style='text-align: center;'>应用系统或产品</td><td style='text-align: center;'>数据资产运营门户</td></tr></table>

# 附录 B

(资料性)

指标类数据标准示例

表B.1给出了根据指标类数据标准属性框架对“融资融券余额”数据标准的描述示例。

<div style="text-align: center;">表 B.1 “融资融券余额” 数据标准</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>内容</td></tr><tr><td style='text-align: center;'>编码</td><td style='text-align: center;'>MI000082</td></tr><tr><td style='text-align: center;'>信息大类</td><td style='text-align: center;'>股票市场</td></tr><tr><td style='text-align: center;'>信息小类</td><td style='text-align: center;'>信用交易</td></tr><tr><td style='text-align: center;'>指标中文名称</td><td style='text-align: center;'>融资融券余额</td></tr><tr><td style='text-align: center;'>常用维度</td><td style='text-align: center;'>1.证券类别（股票、基金）；2.业务类型（融资、融券）；3.证券交易所、中介机构</td></tr><tr><td style='text-align: center;'>业务含义</td><td style='text-align: center;'>是指统计期末投资者未了结的融资交易和融券交易的金额</td></tr><tr><td style='text-align: center;'>计算公式</td><td style='text-align: center;'>融资融券余额=融资余额+融券余额= $ \sum $ （融资买入金额-融资偿还额）+  $ \sum $ （融券卖出量-融券偿还量）×标的证券统计日收盘价格</td></tr><tr><td style='text-align: center;'>范围及条件</td><td style='text-align: center;'>1.融资偿还包括直接还款、卖券还款和融资强制平仓；2.融券偿还包括现金偿还、买券还券、直接还券、融券强制平仓、余券划转和融券正负权益调整；3.不计利息和费用</td></tr><tr><td style='text-align: center;'>标准别名</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>相关指标标准</td><td style='text-align: center;'>融资买入金额</td></tr><tr><td style='text-align: center;'>参考依据</td><td style='text-align: center;'>《证券期货业统计指标标准指引》证监会公告〔2019〕28号</td></tr><tr><td style='text-align: center;'>统计周期</td><td style='text-align: center;'>日、月、季、年</td></tr><tr><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>SMT_BAL</td></tr><tr><td style='text-align: center;'>数据类型及长度</td><td style='text-align: center;'>DECIMAL(18,4)</td></tr><tr><td style='text-align: center;'>度量单位</td><td style='text-align: center;'>元</td></tr><tr><td style='text-align: center;'>取值范围</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>指标类型</td><td style='text-align: center;'>衍生指标</td></tr><tr><td style='text-align: center;'>计算流程</td><td style='text-align: center;'>第一步：从投资者两融资产负债表中选取字段融资余额、融券余额，第二步：计算融资余额与融券余额的加总</td></tr><tr><td style='text-align: center;'>伪代码</td><td style='text-align: center;'>取自投资者两融资产负债表（AST_INVS_SMT_ASET_LBLT），选取字段 融资余额（FIN_BAL）、融券余额（SEC_LN_BAL）；筛选条件：S_DATE &lt;= 查询日期 并且 E_DATE &gt; 查询日期。</td></tr></table>

<div style="text-align: center;">表 B.1 “融资融券余额” 数据标准（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>内容</td></tr><tr><td style='text-align: center;'>数据来源</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标准管理部门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>业务管理部门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标准相关部门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>安全级别</td><td style='text-align: center;'>一般</td></tr><tr><td style='text-align: center;'>使用级别</td><td style='text-align: center;'>三级</td></tr><tr><td style='text-align: center;'>防控级别</td><td style='text-align: center;'>2</td></tr><tr><td style='text-align: center;'>版本日期</td><td style='text-align: center;'>2022年12月</td></tr><tr><td style='text-align: center;'>当前版本号</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>发布状态</td><td style='text-align: center;'>已发布</td></tr><tr><td style='text-align: center;'>应用系统或产品</td><td style='text-align: center;'>数据资产运营门户</td></tr></table>

## 参 考 文 献

[1] GB/T 5271.1—2000 信息技术词汇 第1部分：基本术语

[2] JR/T 0105—2014 银行数据标准定义规范