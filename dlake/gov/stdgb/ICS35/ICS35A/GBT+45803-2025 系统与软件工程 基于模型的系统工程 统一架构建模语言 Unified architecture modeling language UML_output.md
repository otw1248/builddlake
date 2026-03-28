

# 中华人民共和国国家标准

GB/T 45803—2025

# 系统与软件工程 基于模型的系统工程 统一架构建模语言

# System and software engineering—Model-based systems engineering—Unified architecture modeling language

2025-05-30 发布

2025-12-01 实施

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
3.2 缩略语 …… 5    
4 统一架构建模语言总体框架 …… 5    
5 关键字词汇结构 …… 6    
5.1 概述 …… 6    
5.2 字符编码 …… 6    
5.3 注释 …… 6    
5.4 标识符 …… 7    
5.5 字符的关键字 …… 7    
5.6 字符常量 …… 11    
6 类语法结构 …… 13    
6.1 元元模型类集合 …… 13    
6.2 元模型类集合 …… 13    
6.3 模型类集合 …… 20    
6.4 组织类集合 …… 27    
6.5 插件类集合 …… 28    
附录 A（资料性） 架构语言建模示例 …… 30    
A.1 可视化示例 …… 30    
A.2 元模型示例 …… 30    
A.3 模型示例 …… 33    
附录 B（资料性） 飞机机载维护与健康管理系统示例 …… 36    
B.1 建模需求 …… 36    
B.2 元模型 …… 36    
B.3 模型 …… 44    
附录 C（资料性） 单位 …… 52    
参考文献 …… 55

Powered by TCPDF (www.tcpdf.org)

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国信息技术标准化技术委员会(SAC/TC 28)提出并归口。

本文件起草单位：中国电子技术标准化研究院、北京航空航天大学、北京理工大学、中国商用飞机有限责任公司北京民用飞机技术研究中心、中国兵器装备集团兵器装备研究所、北京理工大学长三角研究院（嘉兴）、金航数码科技有限责任公司、北京蜂巢智创系统科技有限公司、中国人民解放军国防科技大学、南方科技大学、中国兵器工业信息中心、三一重工股份有限公司、北京互时科技股份有限公司、北京工业大学、凯德技术长沙股份有限公司、中船凌久电子（武汉）有限责任公司、浪潮软件科技有限公司、山东山科数字经济研究院有限公司、北京谷器数据科技有限公司、中国航天系统科学与工程研究院、国家应用软件产品质量检验检测中心、嘉兴市文诺财经大数据技术研究院、重庆市软件评测中心有限公司、联通（浙江）产业互联网有限公司、西南计算机有限责任公司、和元达信息科技有限公司、来未来科技（浙江）有限公司、北京鸿鹄云图科技股份有限公司、深圳市联合信息技术有限公司、湖北华中电力科技开发有限责任公司、联通在线信息科技有限公司。

本文件主要起草人：范科峰、鲁金直、李文鹏、苏伟、王国新、张旸旸、马君达、汪潞、于冬梅、王建国、姜苏倩、车江涛、陈金伟、李小波、郑晓晨、兰小平、郄永军、宋楠、刘潇健、谢宏、李锡武、李照川、李旺、董代、李书林、楼莉、王公韬、段海波、郑旭飞、杨晨、高亚男、郭梦雪、罗雪山、华传健、王国章、墙辉、只飞、汤代佳、田爱华、罗明强、阎艳、张恬恬、唐剑、李俊霖、卢继平、胡晓度、刘文军、张若彤、牛龙飞。

## 引言

随着装备研制过程的复杂性逐渐增加，基于模型的系统工程（MBSE）广泛应用于各装备研发过程中的项目管理、总体设计、需求分析、架构设计等活动，以提高研制的效率及效能。在面向复杂装备的正向设计过程中，不同层级架构设计需要不同的建模语言，如系统之系统层级使用UPDM建模语言，系统层级使用SysML建模语言，子系统层级使用EAST-ADL建模语言，不同建模语言的语义及存储结构不同，导致语言的集成和交互困难。

因此，本文件定义统一架构建模语言以将复杂装备的正向设计过程中的多种建模语言进行统一的架构视图描述与表达，实现多种建模语言的集成、数据的互通和一致性传递。本文件通过统一架构建模语言的元元模型类、元模型类及模型类等语法定义，明确语言的语法结构，支持基于统一建模语言的工具开发及模型集成。

本文件是在元对象机制（MOF）框架的基础上形成，图1展示了统一架构建模语言的构建的四个层次，分别为M3层（元元模型层）、M2层（元模型层）、M1层（模型层）、M0层（系统层）。M3至M0是逐层实例化的过程，M0至M3是逐层抽象的过程。

<div style="text-align: center;"><img src="imgs/img_in_image_box_213_729_964_1204.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 1 基于 MOF 的建模框架</div>


图 1 中各层级的主要内容如下。

a) M3 为元元模型层，代表最高程度的元模型抽象，即元模型的元语言。本质上元模型和元元模型没有区别，只是在元对象机制中的抽象水平不同。通过这种方式，设计人员按照需求解除元模型的限制——利用元元模型的组合自行构建多领域元模型库，实现不同模型的抽象与交互。在元对象机制 M3 层含义的基础上，统一架构建模语言提供了六种元元模型以及其之间的规则和约束，支持描述更多领域元模型之间的关联和约束关系。这六种元元模型分为属性元素和非属性元素两类：前者指属性元元模型，用来描述非属性元素的性质；而后者包括图元元模型、对象元元模型、点元元模型、角色元元模型、关系元元模型等。扩展概念用于指定六种元元模型。

模型之间的关联关系，并说明其规则和约束。这些扩展概念包括分解、剖视、类引用等。

b）M2为元模型层，是对元元模型的实例化，基于元对象机制的M2层框架，本文件的M2层包括图元模型、对象元模型、点元模型、角色元模型、关系元模型、属性元模型以及元模型b扩展，通过元模型的组合形成建模语言。这些元模型通过图形化的方式为系统设计提供建模手段。

c) M1 为模型层, 模型是对元模型的实例化, 是通常意义上的建模过程, 用于描述系统生存周期的活动。

d）M0为系统层，是对模型层在现实世界中的真实表征，即从某个系统视角对关注的问题进行的描述。

本文件基于元对象机制的 M3-M1 框架中指定六种元元模型和扩展，通过定义元元模型、元模型和模型的类，实现统一架构建模语言的规范定义。



# 系统与软件工程 基于模型的系统工程 统一架构建模语言

## 1 范围

本文件确立了统一架构建模语言的总体框架，规定了关键字词汇结构和类语法结构。

本文件适用于基于模型系统工程的架构视图的统一描述，通过更底层的文本语言，实现对现有建模语言（例如 UML、SysML、UPDM、BPMN、OPM 等）的功能覆盖，并具备可扩展性，根据任务场景定制特定域建模语言，通过统一的数据格式支持不同工具间的数据交互及语义集成。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB 3100 国际单位制及其应用

GB/T 3101 有关量、单位和符号的一般原则

GB/T 3102.1 空间和时间的量和单位

GB/T 3102.2 周期及其有关现象的量和单位

GB/T 3102.3 力学的量和单位

GB/T 3102.4 热学的量和单位

GB/T 3102.5 电学和磁学的量和单位

GB/T 3102.6 光及有关电磁辐射的量和单位

GB/T 3102.7 声学的量和单位

GB/T 3102.8 物理化学和分子物理学的量和单位

GB/T 3102.9 原子物理学和核物理学的量和单位

GB/T 3102.10 核反应和电离辐射的量和单位

GB/T 3102.11 物理科学和技术中使用的数学符号

GB/T 3102.12 特征数

GB/T 3102.13 固体物理学的量和单位

GB/T 11457 信息技术 软件工程术语

GB/T 13000 信息技术 通用编码字符集(UCS)

GB 18030 信息技术 中文编码字符集

## 3 术语、定义和缩略语

### 3.1 术语和定义

GB/T 11457 界定的以及下列术语和定义适用于本文件。

#### 3.1.1 

## 架构 architecture

实体在其环境中的基本概念或属性，以及该实体及其相关生存周期过程的实现和演化的管控原则。

[来源：ISO/IEC/IEEE 42010:2022,3.1]

#### 3.1.2 

## 类 class

用于将数据和操作的方法封装在一起，表示问题域的抽象概念。

#### 3.1.3 

## 属性类引用 class reference

在模型中通过属性引用对象、关系、角色、点、属性等模型。

注：类引用通常在属性元模型中定义。

#### 3.1.4 

## 元元模型 meta-meta model

元模型进一步抽象，定义元模型的元数据结构和语义。

注 $ ^{1} $ ：元元模型与元模型之间的关系，类同于元模型与模型间的关系。

注2：本文件包含图元元模型、对象元元模型、关系元元模型、点元元模型、角色元元模型、属性元元模型，以及扩展。

[来源:GB/T 28174.1—2011,3.1.73]

#### 3.1.5 

## 元模型 meta-model

定义用于表达模型的语言的模型。

注：元模型的典型作用，是定义模型元素在模型中如何得到实例化的语义。模型通常包含模型元素。这些模型元素是通过将元模型的模型元素（即元模型元素）实例化而创建的。

[来源:GB/T 28174.1—2011,3.1.73]

#### 3.1.6 

## 图元模型 meta-model of graph

模型的基础视图要素。

注：图元模型定义了在模型中使用的对象、关系元模型等语法和语义规则。

#### 3.1.7 

## 对象元模型 meta-model of object

模型中需要使用的主要建模对象的元模型。

#### 3.1.8 

## 关系元模型 meta-model of relationship

模型中需要使用的将建模对象建立关联关系的连接实体的元模型。

#### 3.1.9 

## 点元模型 meta-model of point

模型中对建模对象附加的端口实体的元模型。

#### 3.1.10 

## 属性元模型 meta-model of property

模型中视图、要素、关系、端口等要素基础参数的元模型。

注：提供在模型中各要素的基础参数。

#### 3.1.11 

## 角色元模型 meta-model of role

模型中定义关系实体两端输入输出性质的元模型。

#### 3.1.12 

## 元模型映射 meta-model mapping

两类元模型要素之间的映射，支撑采用元模型定义的模型之间的转换。

#### 3.1.13 

## 模型 model

实体或实体集合的抽象表征，提供了在所关注的条件或情况下，描绘、理解或预测实体或实体集合属性或特征的能力。

注1：模型能使用形式理论，而形式理论基于数学或者科学的原理与概念。模型能用已确立的元模型生成。元模型通常用于促进开发准确、完整、一致且可理解的模型。

注2：参考模型用于刻画一般实例，该一般实例用作具体条件或情况创建特殊实例模型的基础。参考模型能用于促进和加强架构与架构元素的一致性。

注3：根据具体情况，模型能是架构模型、架构实体模型、概念模型或者参考模型。

注4：物理模型是一种具体表示，它和数学与逻辑模型相区别，后两种模型都是系统的更抽象表示。抽象模型还能进一步分为描述模型（类似于逻辑模型）和分析模型（类似于数学模型）。

注5：（建模和仿真技术）所研究的系统、过程事物或概念的一种表达形式，是对现实世界的事物、现象、过程或系统的简化描述，或其部分属性的抽象。

[来源:ISO/IEC/IEEE 42020:2019,3.13,有修改]

#### 3.1.14 

## 模型实例 model instance

基于图元模型指定的图形化视图要素的集合。

#### 3.1.15 

## 对象实例 object instance

基于对象元模型的实例化，模型中用来建模的要素。

#### 3.1.16 

## 关系实例 relationship instance

基于关系元模型的实例化，模型中用来建立连接关系的要素。

#### 3.1.17 

## 点实例 point instance

基于点元模型的实例化，模型中用来指定对象端口的要素。

#### 3.1.18 

## 属性实例 property instance

基于属性元模型的实例化，模型中用来指定各要素参数信息的要素。

#### 3.1.19 

## 角色实例 role instance

基于角色元模型的实例化，模型中用来规定关系流方向的要素。

#### 3.1.20 

## 建模语言 modeling language

按照一套系统的规则和框架来设计和构建结构和模型的图形或文本计算机语言。

注：建模语言与编程语言不同，一般来说，编程语言抽象层次较低，采用面向计算机实现的概念作为建模元素，语言的可执行性强；建模语言抽象层次高，采用面向问题领域的概念作为建模元素，语言的可执行性弱。编程语言更侧重于技术域的计算机实现，其语法、语义的研究对象实际上是计算机程序；而建模语言的语法和语义则更针对问题域的研究对象描述。

#### 3.1.21 

## 基于模型的系统工程 model-based systems engineering

建模方法的形式化应用，以支持系统从概念设计阶段一直持续到开发阶段和后续生存周期阶段的

需求、设计、分析、验证和确认活动。

#### 3.1.22 

## 模型元素 model element

由单个组件、动作、状态、消息、属性、关系构成的原子(基本)项，或其他描述系统的组成、特性或行为的其他项。

#### 3.1.23 

## 阶段 stage

生存周期中的时间段。

注：在这段时间内为实现本段时间的目标而执行的活动。

[来源：ISO/IEC/IEEE 42020:2019,3.15]

#### 3.1.24 

## 系统 system

为实现一个或多个既定目的而组织起来的相互作用元素的组合。

注 $ ^{1} $ ：一个系统被认为是一种产品或者是一种它所提供的服务。

注2：实际中，对系统含义的解释通常通过使用一个联合名词来阐述，例如飞行器系统。有时候“系统”也能简单地由依赖语境的同义词来代替，例如飞行器，虽然会使系统的角度不太明显。

注3：完整的系统包括相关装置、设备、原料、计算机程序、固件、技术文档、服务和运行、支持所必需的人力，在预期的环境中实现某种程度的自给自足。

[来源：ISO/IEC/IEEE 15288:2023,3.46]

#### 3.1.25 

## 系统元素 system element

满足特定需求的一个系统的离散部分。

示例：硬件、软件、数据、人、过程（例如为用户提供服务的过程）、规程（例如操作指南）、设备、材料、自然存在的实体或其任意组合。

[来源：ISO/IEC/IEEE 15288:2023,3.47]

#### 3.1.26 

## 统一架构建模语言 unified architecture modeling language

用于支持基于模型的系统工程架构建模的可读文本式及语义式语言。

注 $ ^{1} $ ：采用一种统一的语义式建模语言及技术实现复杂系统的全周期、全要素、全领域架构描述及表达的方法。

注2：基于“文本可读的语义式形式化语言”的核心理念对复杂系统的需求、功能、逻辑、物理结构等系统工程架构视点进行建模。借助统一架构建模语言支持复杂系统之系统、系统、子系统等不同层级的架构视点统一语义表达，如任务定义、系统之系统结构定义、系统需求、系统功能、系统逻辑、系统物理结构等。统一架构建模语言实现对元模型及模型的形式化描述，是一种面向对象的可读的文本语言，有关模型的所有信息及数据都被形式化在统一架构建模语言中，包括元元模型、元模型以及模型。统一架构建模语言形式化模型支持面向对象的语法，例如“继承”“封装”等。

注3：具有下列主要能力：

a）支持不同图形化架构建模语言及框架的元模型开发及建模，如 UML、SysML、BPMN、UPDM 等；

b）支持基于特定域建模语言的元模型开发及建模，如 EAST-ADL 等。

注 $ ^{4} $ ：具有以下主要特点：

a）以可读文本的形式化语言表达 MBSE 模型，使语义描述更加清晰；

b) 支持元模型设计，能基于统一架构建模语言进行图元模型构建并编译；

c）支持基于元模型的架构建模。

#### 3.1.27 

## 视图 view

从单个视点的角度对系统的表示。

#### 3.1.28 

## 视点 viewpoint

从不同建模角度和利益相关方关注角度出发，为创建、解释和使用模型视图而建立的一组约定，以框定一个或多个关注点。

注：一个视点包含多个视图模型类型。

[来源：ISO/IEC/IEEE 42010:2022,3.8,有修改]

### 3.2 缩略语

下列缩略语适用于本文件。

BPMN: 业务过程模型和符号 (Business Process Model and Notation)

DoDAF: 美国国防部体系架构框架 (Department Of Defense Architecture Framework)

EAST-ADL: 电子体系架构与软件技术—架构描述语言 (Electronics Architecture and Software Technology-Architecture Description Language)

ID: 唯一编码(Identity Document)

MBSE: 基于模型的系统工程 (Model-Based Systems Engineering)

MODAF: 英国国防部体系架构框架 (Ministry Of Defence Architecture Framework)

MOF: 元对象机制 (Meta Object Facility)

SE: 系统工程 (Systems Engineering)

SysML:系统建模语言(Systems Modeling Language)

UML: 统一建模语言 (Unified Modeling Language)

UPDM:DoDAF/MODAF 的统一配置文件(the Unified Profile for DoDAF/MODAF)

## 4 统一架构建模语言总体框架

统一架构建模语言应包含三元模型类集合、元模型类集合、模型类集合、组织类集合，可包含插件类集合（见图2），各类集合的定义应使用第5章的关键字。其中：

a）元元模型类集合应包含图元元模型类、对象元元模型类、关系元元模型类、点元元模型类、属性元元模型类、角色元元模型类和扩展；

b) 元模型类集合根据所需构建建模语言的视图内容，应包含图元模型类，可包含对象元模型类、关系元模型类、点元模型类、属性元模型类、角色元模型类，以及元模型扩展子集合；当定义关系元模型类时，应同时定义角色元模型类；当定义对象元模型类时，可定义点元模型类；当未定义对象元模型类时，不应定义点元模型类；不应在建模语言中只定义角色元模型类、点元模型类和属性元模型类；

c) 模型类集合应包含图模型实例类，根据元元模型的组合及建模情况，应包含图模型实例类，可包含对象实例类、关系实例类、点实例类、属性实例类、角色实例类，以及模型扩展子集合；

d）组织类集合应包含项目类、语言类和包类，用于从不同层次对模型进行组织；

e）插件类集合可包含甘特图类、矩阵类、布局类，用于扩展构建模型的能力。

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_204_999_677.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 2 统一架构建模语言总体框架</div>


统一架构建模语言中各类的语法应按照第6章的要求描述。附录A给出了各个元模型和模型的语法示例，附录B针对使命分析、运行分析、功能分析、逻辑架构分析等设计过程给出了飞机机载维护与健康管理系统建模示例。

统一架构建模语言属性中涉及单位应依据 GB 3100、GB/T 3101、GB/T 3102.1、GB/T 3102.2、GB/T 3102.3、GB/T 3102.4、GB/T 3102.5、GB/T 3102.6、GB/T 3102.7、GB/T 3102.8、GB/T 3102.9、GB/T 3102.10、GB/T 3102.11、GB/T 3102.12、GB/T 3102.13 的要求描述，常用的单位见附录 C。

## 5 关键字词汇结构

### 5.1 概述

本章规定了统一架构建模语言语法的词汇结构，包含字符流关键字、字符常量等内容。

注1：统一架构建模语言的最小组成单元是单个字符，字符被组合成词汇单位，称为字符流。字符流包含文字常量和标识符。

注 $ ^{2} $ ：这些字符流会被统一架构建模语言翻译器检测。

注3：字符流被组合为统一架构建模语言的语法。

### 5.2 字符编码

统一架构建模语言的字符编码应按 GB 18030 的规定选用。

### 5.3 注释

注释并不是真正的词汇单位，是统一架构建模语言的解释和说明。注释在被词法分析器检测到之后会被忽略，不会被编译。统一架构建模语言中包含两种注释方法，见表1。

<div style="text-align: center;">表 1 注释方法</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>注释方式</td><td style='text-align: center;'>解释</td></tr><tr><td style='text-align: center;'>// 注释</td><td style='text-align: center;'>双斜杠//后到这一行结尾之间的字符均被忽略</td></tr><tr><td style='text-align: center;'>/* 注释 */</td><td style='text-align: center;'>/* 和 */之间的字符均被忽略</td></tr></table>

统一架构建模语言的注释不准许嵌套，也就是说，/* 和 */ 之间不准许再嵌套一个/* 注释 */。示例是不准许的。

示例：/* 注释不能被嵌套/* 该模块用于模型解释*/。

### 5.4 标识符

标识符是字母、数字和下划线组成的字符序列，用于命名统一架构建模语言中的类名称、变量名称、常数名称等其他项目的名称。标识符应以字母或者下划线开头，后续字符准许为字母、下划线或数字。标识符定义规则见表2。

<div style="text-align: center;">表 2 标识符</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>组成</td></tr><tr><td style='text-align: center;'>IDENT</td><td style='text-align: center;'>NONDIGITAL(DIGITAL| NONDIGITAL) *</td></tr><tr><td style='text-align: center;'>DIGITAL</td><td style='text-align: center;'>0~9</td></tr><tr><td style='text-align: center;'>NONDIGITAL</td><td style='text-align: center;'>a~z|A~Z| _”</td></tr></table>

### 5.5 字符的关键字

统一架构建模语言字符流中的关键字不应作为标识符命名统一架构建模语言的任何要素，统一架构建模语言字符流中包括的关键字见表3。

<div style="text-align: center;">表 3 关键字及定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>属性注解</td></tr><tr><td style='text-align: center;'>Array</td><td style='text-align: center;'>数组</td></tr><tr><td style='text-align: center;'>avoidObstructionsRouting</td><td style='text-align: center;'>避开障碍</td></tr><tr><td style='text-align: center;'>bind</td><td style='text-align: center;'>表示绑定约束关系</td></tr><tr><td style='text-align: center;'>blankPropertyMode</td><td style='text-align: center;'>对象的显示模式——不显示属性</td></tr><tr><td style='text-align: center;'>Boolean</td><td style='text-align: center;'>布尔型</td></tr><tr><td style='text-align: center;'>Cell</td><td style='text-align: center;'>元胞数组</td></tr><tr><td style='text-align: center;'>circle</td><td style='text-align: center;'>固定语法(形状)——圆</td></tr><tr><td style='text-align: center;'>class&lt;Graph&gt;</td><td style='text-align: center;'>图类型</td></tr><tr><td style='text-align: center;'>class&lt;Object&gt;</td><td style='text-align: center;'>对象类型</td></tr><tr><td style='text-align: center;'>class&lt;Relationship&gt;</td><td style='text-align: center;'>关系类型</td></tr></table>

<div style="text-align: center;">表 3 关键字及定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>class&lt;Role&gt;</td><td style='text-align: center;'>角色类型</td></tr><tr><td style='text-align: center;'>class&lt;Point&gt;</td><td style='text-align: center;'>点类型</td></tr><tr><td style='text-align: center;'>class&lt;Property&gt;</td><td style='text-align: center;'>属性类型</td></tr><tr><td style='text-align: center;'>closestDistanceRouting</td><td style='text-align: center;'>线的最短距离</td></tr><tr><td style='text-align: center;'>Collection</td><td style='text-align: center;'>集合</td></tr><tr><td style='text-align: center;'>color</td><td style='text-align: center;'>定义颜色</td></tr><tr><td style='text-align: center;'>Constraint</td><td style='text-align: center;'>约束</td></tr><tr><td style='text-align: center;'>Connect</td><td style='text-align: center;'>定义连接器</td></tr><tr><td style='text-align: center;'>connector</td><td style='text-align: center;'>标识连接器</td></tr><tr><td style='text-align: center;'>containerMode</td><td style='text-align: center;'>对象的显示模式——容器模式</td></tr><tr><td style='text-align: center;'>content</td><td style='text-align: center;'>标识文本内容</td></tr><tr><td style='text-align: center;'>customImage</td><td style='text-align: center;'>固定语法(形状)——自定义图片</td></tr><tr><td style='text-align: center;'>decompose</td><td style='text-align: center;'>对象/点/关系/角色的分解</td></tr><tr><td style='text-align: center;'>description</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>diagramKind</td><td style='text-align: center;'>声明图的类型</td></tr><tr><td style='text-align: center;'>Distribution</td><td style='text-align: center;'>分布</td></tr><tr><td style='text-align: center;'>Double</td><td style='text-align: center;'>双精度浮点数</td></tr><tr><td style='text-align: center;'>end</td><td style='text-align: center;'>标识结束</td></tr><tr><td style='text-align: center;'>endLocation</td><td style='text-align: center;'>关系的端点坐标</td></tr><tr><td style='text-align: center;'>Enumeration</td><td style='text-align: center;'>枚举</td></tr><tr><td style='text-align: center;'>explode</td><td style='text-align: center;'>对象/点/关系/角色的剖视</td></tr><tr><td style='text-align: center;'>Export</td><td style='text-align: center;'>角色方向——终端</td></tr><tr><td style='text-align: center;'>extends</td><td style='text-align: center;'>继承</td></tr><tr><td style='text-align: center;'>false</td><td style='text-align: center;'>布尔型——假</td></tr><tr><td style='text-align: center;'>frame</td><td style='text-align: center;'>对象边框的设置</td></tr><tr><td style='text-align: center;'>Float</td><td style='text-align: center;'>单精度浮点数</td></tr><tr><td style='text-align: center;'>GanttChart</td><td style='text-align: center;'>标识甘特图插件</td></tr><tr><td style='text-align: center;'>Graph</td><td style='text-align: center;'>标识图元元模型</td></tr><tr><td style='text-align: center;'>icon</td><td style='text-align: center;'>图标</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>唯一编码</td></tr><tr><td style='text-align: center;'>imageAddress</td><td style='text-align: center;'>对象的图片地址</td></tr><tr><td style='text-align: center;'>import</td><td style='text-align: center;'>角色方向——始端</td></tr><tr><td style='text-align: center;'>initial</td><td style='text-align: center;'>对元模型属性赋初始值的标志</td></tr><tr><td style='text-align: center;'>initialLocation</td><td style='text-align: center;'>定义水平/垂直位置和大小</td></tr></table>

<div style="text-align: center;">表 3 关键字及定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Input</td><td style='text-align: center;'>点方向——输入</td></tr><tr><td style='text-align: center;'>instanceOf</td><td style='text-align: center;'>图元模型到模型的实例化</td></tr><tr><td style='text-align: center;'>Int</td><td style='text-align: center;'>整型</td></tr><tr><td style='text-align: center;'>jumpLinkStatus</td><td style='text-align: center;'>跳转链接状态</td></tr><tr><td style='text-align: center;'>jumpLinkType</td><td style='text-align: center;'>跳转链接类型</td></tr><tr><td style='text-align: center;'>labelDisplay</td><td style='text-align: center;'>标签展示</td></tr><tr><td style='text-align: center;'>Language</td><td style='text-align: center;'>标识语言</td></tr><tr><td style='text-align: center;'>Layout</td><td style='text-align: center;'>标识布局插件</td></tr><tr><td style='text-align: center;'>List</td><td style='text-align: center;'>有序列表</td></tr><tr><td style='text-align: center;'>localLabel</td><td style='text-align: center;'>本地名称</td></tr><tr><td style='text-align: center;'>Map</td><td style='text-align: center;'>键值对</td></tr><tr><td style='text-align: center;'>Matrix</td><td style='text-align: center;'>矩阵</td></tr><tr><td style='text-align: center;'>metaGraph</td><td style='text-align: center;'>组织图元模型文件夹名</td></tr><tr><td style='text-align: center;'>metaObject</td><td style='text-align: center;'>组织对象元模型文件夹名</td></tr><tr><td style='text-align: center;'>metaPoint</td><td style='text-align: center;'>组织点元模型文件夹名</td></tr><tr><td style='text-align: center;'>metaProperty</td><td style='text-align: center;'>组织属性元模型文件夹名</td></tr><tr><td style='text-align: center;'>metaRelationship</td><td style='text-align: center;'>组织关系元模型文件夹名</td></tr><tr><td style='text-align: center;'>metaRole</td><td style='text-align: center;'>组织角色元模型文件夹名</td></tr><tr><td style='text-align: center;'>Model</td><td style='text-align: center;'>标识模型</td></tr><tr><td style='text-align: center;'>modelElementName</td><td style='text-align: center;'>声明模型元素名称</td></tr><tr><td style='text-align: center;'>modelElementType</td><td style='text-align: center;'>声明模型元素类型</td></tr><tr><td style='text-align: center;'>Node</td><td style='text-align: center;'>标识笔记</td></tr><tr><td style='text-align: center;'>nodeAttachment</td><td style='text-align: center;'>标识笔记附件</td></tr><tr><td style='text-align: center;'>Object</td><td style='text-align: center;'>标识对象元元模型</td></tr><tr><td style='text-align: center;'>OrderSet</td><td style='text-align: center;'>有序不重复列表</td></tr><tr><td style='text-align: center;'>Output</td><td style='text-align: center;'>点方向——输出</td></tr><tr><td style='text-align: center;'>packageDiagram</td><td style='text-align: center;'>固定语法(形状)——包型</td></tr><tr><td style='text-align: center;'>Point</td><td style='text-align: center;'>标识点元元模型</td></tr><tr><td style='text-align: center;'>polylineLocation</td><td style='text-align: center;'>关系上各折点坐标</td></tr><tr><td style='text-align: center;'>Project</td><td style='text-align: center;'>标识项目</td></tr><tr><td style='text-align: center;'>Property</td><td style='text-align: center;'>标识属性元元模型</td></tr><tr><td style='text-align: center;'>propertyMode</td><td style='text-align: center;'>对象的显示模式——显示属性</td></tr><tr><td style='text-align: center;'>Real</td><td style='text-align: center;'>实数</td></tr><tr><td style='text-align: center;'>rectangle</td><td style='text-align: center;'>固定语法(形状)——矩形</td></tr></table>

<div style="text-align: center;">表 3 关键字及定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>refer</td><td style='text-align: center;'>标识元模型实例化</td></tr><tr><td style='text-align: center;'>Relationship</td><td style='text-align: center;'>标识关系元模型</td></tr><tr><td style='text-align: center;'>reverseJumpLink</td><td style='text-align: center;'>反向跳转链接</td></tr><tr><td style='text-align: center;'>Role</td><td style='text-align: center;'>标识角色元元模型</td></tr><tr><td style='text-align: center;'>roundedRectangle</td><td style='text-align: center;'>固定语法(形状)——圆角矩形</td></tr><tr><td style='text-align: center;'>routingType</td><td style='text-align: center;'>关系的线型</td></tr><tr><td style='text-align: center;'>Set</td><td style='text-align: center;'>无序不重复列表</td></tr><tr><td style='text-align: center;'>SDIdentification</td><td style='text-align: center;'>时序图的唯一编码</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>固定语法(形状)</td></tr><tr><td style='text-align: center;'>smoothness</td><td style='text-align: center;'>线的平滑度</td></tr><tr><td style='text-align: center;'>strikeThrough</td><td style='text-align: center;'>删除线</td></tr><tr><td style='text-align: center;'>String</td><td style='text-align: center;'>字符串</td></tr><tr><td style='text-align: center;'>Table</td><td style='text-align: center;'>标识表单插件</td></tr><tr><td style='text-align: center;'>tableType</td><td style='text-align: center;'>表单类型</td></tr><tr><td style='text-align: center;'>text</td><td style='text-align: center;'>标识对象文本字体设置</td></tr><tr><td style='text-align: center;'>Text</td><td style='text-align: center;'>标识文本</td></tr><tr><td style='text-align: center;'>time</td><td style='text-align: center;'>时间，包含时间单位、时间间隔、起始时间、终止时间</td></tr><tr><td style='text-align: center;'>this</td><td style='text-align: center;'>指代</td></tr><tr><td style='text-align: center;'>triangle</td><td style='text-align: center;'>固定语法(形状)——三角箭头</td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>图的类型</td></tr><tr><td style='text-align: center;'>true</td><td style='text-align: center;'>布尔型——真</td></tr><tr><td style='text-align: center;'>Tuple</td><td style='text-align: center;'>元组</td></tr><tr><td style='text-align: center;'>unique</td><td style='text-align: center;'>唯一性</td></tr><tr><td style='text-align: center;'>unit</td><td style='text-align: center;'>单位</td></tr><tr><td style='text-align: center;'>underline</td><td style='text-align: center;'>下划线</td></tr><tr><td style='text-align: center;'>Undirected</td><td style='text-align: center;'>无向的点</td></tr><tr><td style='text-align: center;'>UnfoldDirection</td><td style='text-align: center;'>方向</td></tr><tr><td style='text-align: center;'>value</td><td style='text-align: center;'>表单的值(以矩阵形式表示)</td></tr><tr><td style='text-align: center;'>visualizationList</td><td style='text-align: center;'>分解、剖视图位置</td></tr><tr><td style='text-align: center;'>visualizedMode</td><td style='text-align: center;'>显示模式</td></tr><tr><td style='text-align: center;'>width</td><td style='text-align: center;'>宽度</td></tr><tr><td style='text-align: center;'>X</td><td style='text-align: center;'>方向——横向</td></tr><tr><td style='text-align: center;'>Y</td><td style='text-align: center;'>方向——纵向</td></tr><tr><td colspan="2">注1：关键词对大小写敏感，区分大小写。注2：括号内为定义内容的辅助说明。</td></tr></table>

### 5.6 字符常量

#### 5.6.1 实数型字符

实数型字符应在字符中带有小数点的十进制的数字序列。实数的小数点之后至少带有一个数字。实数准许表示 15 位小数。

示例：3.0、322.56。

#### 5.6.2 整数型字符

整数型字符应在字符中十进制的数字序列。整型的最小取值为 $ -2^{31} $ ，最大取值为 $ 2^{31}-1 $ 。

示例：33、0、30 044。

#### 5.6.3 布尔型字符

布尔型字符应取值范围为真或假的枚举类型。

#### 5.6.4 字符串

字符串一般应出现在双引号之间，如“字符串”。除了双引号和反斜杠以外，都应准许直接包括在字符串中，无需使用转义码。表4中字符不应作为字符串。

<div style="text-align: center;">表 4 非字符串字符</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字符</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>$ &#x27;&#x27; $</td><td style='text-align: center;'>单引号</td></tr><tr><td style='text-align: center;'>$ &quot;&quot; $</td><td style='text-align: center;'>双引号</td></tr><tr><td style='text-align: center;'>\\\\</td><td style='text-align: center;'>反斜杠</td></tr><tr><td style='text-align: center;'>\n</td><td style='text-align: center;'>换行</td></tr><tr><td style='text-align: center;'>\r</td><td style='text-align: center;'>回车</td></tr><tr><td style='text-align: center;'>\t</td><td style='text-align: center;'>水平标签</td></tr></table>

#### 5.6.5 单精度浮点数型字符

单精度浮点数型字符应由符号位、指数位和尾数位共32位组成，其中指数位占8位，尾数位占23位，提供约7位十进制数的精度。

示例：Float myFloat=3.14f。

#### 5.6.6 双精度浮点数型字符

双精度浮点数型字符应由符号位、指数位和尾数位共64位组成，其中指数位占11位，尾数位占52位，提供约15位十进制数的高精度。

示例：Double myDouble=3.14。

#### 5.6.7 元胞数组

元胞数组应由元胞组成的数组，准许是一维、二维或多维。不同于普通的数组，其中的元素准许是不同类型的数据。

示例：language1= $ \{SysML, OMG\} $ ；language2= $ \{UML, OMG\} $ ；languageArray= $ \{language1, language2\} $ ；则 lan

guageArray 为元胞数组，元胞存储了语言名称和提出组织的信息。

#### 5.6.8 枚举

枚举应是一种数据类型，其实例是命名值的列表。

示例：enum Day { SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY }。

#### 5.6.9 数组

数组应是一种用于存储相同类型元素的数据结构，这些元素通过索引进行访问。提供了一种有效的方式来组织和管理大量相似类型的数据。

 $$  示例：String[]fruits=new String[]\{\text{“Apple”，“Banana”，“Orange”，“Grapes”}\}。 $$ 

#### 5.6.10 矩阵

矩阵应是一个由数值按照规定的规则排列成的矩形数组。

示例： $$ 1,2,3 $$ 。

#### 5.6.11 元组

元组应是一个有序的、不可变的数据序列。包含不同数据类型的元素，且每个元素在元组中有固定的位置。元组的长度是固定的，一旦创建，就不应修改。

示例：my_tuple=(1,"hello",3.14,True)。

#### 5.6.12 集合

集合应是一个无序的、不包含重复元素的数据结构。通常用于表示一组独特的元素，而不关心元素的顺序。

#### 5.6.13 分布

分布应是一组数据或事件在不同取值或位置上的分散程度、频率或概率分布。

#### 5.6.14 有序列表

有序列表应是按照一定的顺序(通常是数字或字母)对列表项进行编号。

#### 5.6.15 无序不重复列表

无序不重复列表应是一个无序的、不包含重复元素的数据结构。通常用于表示一组独特的元素，而不关心元素的顺序。

#### 5.6.16 有序不重复列表

有序不重复列表应在有序性中的元素按照一定的顺序排列，列表中的元素不应重复。

示例： $ unique\_set=\{1,2,3,4,5\} $ 

#### 5.6.17 键值对

键值对应是一种数据存储和表示方式，其中数据被组织成一对（或多对）键和相应的值。每个键与其关联的值之间存在映射关系，准许通过键来访问对应的值。

#### 5.6.18 图类型

图类型是限定模型中属性引用的数据类型为图模型实例。

#### 5.6.19 对象类型

对象类型是限定模型中属性引用的数据类型为对象实例。

#### 5.6.20 关系类型

关系类型是限定模型中属性引用的数据类型为关系实例。

#### 5.6.21 角色类型

角色类型是限定模型中属性引用的数据类型为角色实例。

#### 5.6.22 点类型

点类型应是定模型中属性引用的数据类型为点实例。

#### 5.6.23 属性类型

属性类型是限定模型中属性引用的数据类型为属性实例。

## 6 类语法结构

### 6.1 元元模型类集合

元元模型类集合包含图、对象、关系、点、属性、角色和扩展，应按照表5的要求描述统一架构建模语言中的元元模型。

<div style="text-align: center;">表 5 元元模型类集合</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元元模型类型</td><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>图</td><td style='text-align: center;'>Graph</td><td style='text-align: center;'>用于对系统的某个视点进行分析，在一个框图内对系统进行描述</td></tr><tr><td style='text-align: center;'>对象</td><td style='text-align: center;'>Object</td><td style='text-align: center;'>模型中的主要元素，用于表示一种实体，可单独存在，也可与其他对象进行关系链接</td></tr><tr><td style='text-align: center;'>关系</td><td style='text-align: center;'>Relationship</td><td style='text-align: center;'>通过角色与对象连接，表示对象之间以何种方式进行连接</td></tr><tr><td style='text-align: center;'>点</td><td style='text-align: center;'>Point</td><td style='text-align: center;'>应附属在对象上，用于表示对象和角色连接的端口</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>Property</td><td style='text-align: center;'>用于定义及描述一些元类型（对象、角色及关系）的特性。属性不能单独存在，应附属到其他元元模型上用于表示其特性</td></tr><tr><td style='text-align: center;'>角色</td><td style='text-align: center;'>Role</td><td style='text-align: center;'>应在关系的两端，表示对象以何种方式进行连接</td></tr><tr><td style='text-align: center;'>扩展</td><td style='text-align: center;'>Extension</td><td style='text-align: center;'>表示分解、剖视、属性类引用等约束的集合</td></tr></table>

### 6.2 元模型类集合

#### 6.2.1 图元模型类语法

图元模型类可包含图的属性、对象元模型的声明、关系元模型的声明、约束，以及图元模型的注释共5个部分。其中，图的属性是对属性元模型的继承，约束可包含对象元模型和关系元模型的绑定关系、对象的分解和剖视，注释中应包含名称、描述和图的类型。图元模型类语法见示例。

示例：

partial Graph diagram1 //diagram1是图元模型的唯一编码。

initial Property unique graphProperty1 = "value" extends height1 annotation(localLabel="重量"); //图的属性中
extends 是图的属性继承属性元模型使用的关键字; "value"是字符串形式的属性值; "重量"是属性的名称。
Object requirement1; //requirement1是声明的对象元模型的唯一编码。
Object requirement2;
Relationship relat1; //relat1是声明的关系元模型的唯一编码。
Relationship relat1;
Constraint

(
    bind connector(requirement1.inPoint1, relat2.satisfyTo), //对象 requirement1 配置的点 inPoint1 绑定关系
relat2 的角色 satisfyTo。
    bind connector(requirement1.outPoint1, relat2.satisfyFrom),
    bind connector(requirement2, relat1.deriveFrom),
    bind connector(requirement2, relat1.deriveTo),
    requirement1.decompose(Diagram1, Diagram2), //对象 requirement1 可分解为 Diagram1 和 Diagram2。通过
", + 唯一编码的方式增加可分解的图元模型。
    requirement2.decompose(Diagram2, Diagram3),
    requirement1.explode(Diagram2, Diagram3), //对象 requirement1 可剖视为 Diagram1 和 Diagram2。通过
", + 唯一编码的方式增加可剖视的图元模型。
    relat1.deriveTo.explode(Diagram3),
);
annotation

(
    localLabel="图",
    description="描述",
    type=diagram,
);
end diagram1;

其中，图元模型类关键字的含义见表6。

<div style="text-align: center;">表 6 图元模型类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>partial</td><td style='text-align: center;'>图元模型的标识</td></tr><tr><td style='text-align: center;'>Graph</td><td style='text-align: center;'>定义图元模型的关键字</td></tr><tr><td style='text-align: center;'>Object</td><td style='text-align: center;'>在图下的声明对象元模型的关键字</td></tr><tr><td style='text-align: center;'>Relationship</td><td style='text-align: center;'>在图下声明关系元模型的关键字</td></tr><tr><td style='text-align: center;'>Constraint:</td><td style='text-align: center;'>对图的约束定义，包含绑定 bind 语句以及分解 decompose() 语句和剖视 explode() 语句</td></tr><tr><td style='text-align: center;'>bind</td><td style='text-align: center;'>定义图元模型中绑定的关键字</td></tr><tr><td style='text-align: center;'>connector</td><td style='text-align: center;'>确定实现绑定的连接器，通过声明应进行绑定的对象元模型、点元模型、关系元模型、角色元模型，将对象和关系进行绑定</td></tr></table>

<div style="text-align: center;">表 6 图元模型类含义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>decompose</td><td style='text-align: center;'>定义分解模式的关键字，分解是指对一个对象（点、关系）模型的展开，将一个对象（点、关系）模型分解为一个图模型进行展示和分析。图元模型定义分解是从元模型层确定对象（点、关系）展开为哪些类的图</td></tr><tr><td style='text-align: center;'>explode</td><td style='text-align: center;'>定义剖视模式的关键字，剖视是指从不同角度对对象（点、关系、角色）模型的内部结构用一个图模型进行展示。图元模型定义剖视是从元模型层确定对象（点、关系、角色）展开为那些类的图</td></tr><tr><td style='text-align: center;'>localLabel</td><td style='text-align: center;'>名称，用来命名图元模型的通用名称，可重复，类比人名，形式为带双引号的字符串</td></tr><tr><td style='text-align: center;'>description</td><td style='text-align: center;'>描述，描述系统工程师定义该属性的意图，形式为带双引号的字符串</td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>对图元模型类型的定义，不同的图元模型所包含的对象在画布的展示不同。图类型包含：图（diagram），时序图（sequenceDiagram），版本表格（editionTable），交叉表（crossTable），树形（tree）</td></tr><tr><td colspan="2">标点符号说明：图元模型属性使用半角分号“；”，Constraint（）内部内容以半角逗号“，”隔开，外部使用半角分号“；”，annotation（）内部内容以半角逗号“，”隔开，外部使用半角分号“；”，图元模型定义结尾end&lt;对象元模型ID&gt;后用半角分号“；”结束。</td></tr></table>

#### 6.2.2 对象元模型类语法

对象元模型类定义一组或一类具有相同特征的对象，是图元模型中的主要元素。对象元模型类可包含对象的属性、对象配置的点，应包含对象元模型的注释。其中，对象的属性是对属性元模型的继承，在注释中应包含名称、描述和对象角标、对象模式和对象形状。对象元模型类语法见示例。

示例：

Object requirement1 //requirement1 是对象元模型的唯一编码。

initial Property unique celltestPro="value" extends celltest annotation(localLabel="身高");
Output Point outPoint1 extends outPoint annotation(localLabel="输出点"); //对象点通过 extends 继承点元模型。

annotation
(
    localLabel="对象 requirement1", //对象元模型名称
    description="描述", //对象元模型描述
    icon="Entity.png", //对象的角标
    visualizedMode=property mode, //对象模式
    shape="circle", //对象形状
);
end requirement1;

对象元模型类关键字含义见表7。

<div style="text-align: center;">表 7 对象元模型类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Object</td><td style='text-align: center;'>定义对象元模型的关键字</td></tr><tr><td style='text-align: center;'>Output</td><td style='text-align: center;'>表示输出方向，与始端角色绑定，该位置可替换为 Input，表示输入方向，与终端角色绑定，可替换为 Undirected，表示没有方向性，应与始端、终端、无向角色绑定</td></tr><tr><td style='text-align: center;'>Point</td><td style='text-align: center;'>在对象元模型下声明对象点元模型的关键字</td></tr><tr><td style='text-align: center;'>extends</td><td style='text-align: center;'>元模型部分涉及继承的通用关键字</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>对象元模型包含五个固定语法：localLabel、description、icon、visualizedMode、shape</td></tr><tr><td style='text-align: center;'>icon</td><td style='text-align: center;'>对象元模型的图标，图标名是 png、jpg、gif、svg 等格式，图标名显示为带双引号的图标名全称，如“object.gif”</td></tr><tr><td style='text-align: center;'>visualizedMode</td><td style='text-align: center;'>对象元模型的可视化模式定义，可视化模式主要以在对象模型中是否可视化显示对象属性作为区分，可显示属性的定义为 property mode，不显示属性的定义为 blank property mode</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>对象元模型的形状定义，形状的分类受可视化模式约束。在“property mode”模式下，形状包含：圆角矩形（rounded rectangle），菱形（rhombus）；在“blank property mode”模式下，形状包含：矩形（rectangle），圆（circle），菱形（rhombus），椭圆（oval）</td></tr><tr><td colspan="2">标点符号说明：annotation（）内部内容以半角逗号“，”隔开，外部使用半角分号“；”，对象元模型属性使用半角分号“；”，对象点使用半角分号“；”，对象元模型定义结尾 end+对象元模型 ID 后用半角分号“；”结束。</td></tr></table>

#### 6.2.3 关系元模型类语法

关系元模型类应定义对象模块和对象模块之间的连接关系。关系元模型类可包含关系的属性，应包含一个始端角色和一个终端角色的声明，应包含关系元模型的注释。关系元模型类语法见示例。

示例：

Relationship relat1 //relat1 是关系元模型的唯一编码。

initial Property unique relationshipColor extends colors annotation(localLabel="颜色"); //relationshipColor 是关系的属性的唯一编码，colors 是关系的属性引用的属性元模型的唯一编码。

Role deriveTo; //输出角色声明。

Role deriveFrom; //输入角色声明。

annotation

(
    localLabel="关系 relat1", //关系名称。
    description="描述", //关系元模型描述。
    icon="Exchange.png", //关系元模型的角标。
    shape="solid", //关系元模型的形状。
);

end relat1;

关系元模型类关键字的含义见表8。

<div style="text-align: center;">表 8 关系元模型类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Relationship</td><td style='text-align: center;'>定义关系元模型的关键字</td></tr><tr><td style='text-align: center;'>Role</td><td style='text-align: center;'>在关系元模型下声明角色元模型的关键字</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>关系元模型包含四个固定语法：localLabel、description、icon、shape</td></tr><tr><td style='text-align: center;'>icon</td><td style='text-align: center;'>关系元模型的图标，图标名是 png、jpg、gif 等格式，图标名显示为带双引号的图标名全称</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>关系元模型的形状定义，目前 shape 已有三种，包含：实线（solid），虚线（dash），点线（dot），点划线（dash dot）</td></tr><tr><td colspan="2">标点符号说明：Relationship 中的 annotation（）内部内容以半角逗号“，”隔开，外部使用半角分号“；”，关系属性元模型使用半角分号“；”，声明的角色使用半角分号“；”，关系元模型定义结尾 end+关系元模型 ID 后用半角分号“；”结束。</td></tr></table>

#### 6.2.4 点元模型类语法

点元模型定义一组或一类端口，表示对象如何通过关系连接提供额外的语义或约束。点元模型应用于限定对象应被连接的关系元模型，其特性包括：

a）依赖关系：点元模型应独自定义，但点模型应依赖对象模型存在，当删除对象模型时，该对象模型上的点模型也一并删除；

b） 多样性：对象模型上应添加多个点，且点的方向不受限制；

c）多重性：对象模型上的每一个点都应与多个角色绑定，或者说每一个对象都通过点与多个关系连接。

点元模型类可包含点的属性，应包含点元模型的注释。点元模型类语法见示例。

Point outPoint1 //outPoint1 是点元模型的唯一编码。

initial Property unique address1="value" extends address00 annotation(localLabel="地址"); //点元模型属性
annotation
(
    localLabel="点", //点元模型的名称
    description="描述", //点元模型的描述
    shape="circle", //点元模型的形状
);
end outPoint1;

点元模型类关键字的含义见表9。

<div style="text-align: center;">表 9 点元模型类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Point</td><td style='text-align: center;'>定义点元模型的关键字</td></tr><tr><td style='text-align: center;'>initial</td><td style='text-align: center;'>表示初始化点元模型属性</td></tr><tr><td style='text-align: center;'>Property</td><td style='text-align: center;'>在点元模型下声明属性元模型的关键字</td></tr></table>

<div style="text-align: center;">表 9 点元模型类含义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>unique</td><td style='text-align: center;'>表示唯一性约束，指该属性在模型中只应被实例化一次，不应有同源属性</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>点元模型包含三个固定语法：localLabel、description、shape</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>点的形状定义，为建模提供多种形状展示，shape 可包含：矩形（rectangle），圆（circle），三角形（triangle）</td></tr><tr><td colspan="2">标点符号说明：annotation（）内部内容以半角逗号“，”隔开，外部使用半角分号“；”，点元模型属性使用以半角分号“；”，点元模型定义结尾 end+点 ID 后用半角分号“；”结束。</td></tr></table>

#### 6.2.5 属性元模型类语法

属性元模型类是其他元模型元素的属性。独立的属性元模型无实际含义，应配置在其他五种元模型使用。属性元模型的核心是定义数据类型，见5.6，当属性元模型的数据类型为“Int”“Real”时，应匹配响应的单位，属性中的单位见附录C。属性元模型类语法见示例。

示例：

Int Property address1 annotation(localLabel="属性1", unit="kg", description="属性元模型"); //address1 是属性元模型的唯一编码。

属性元模型类关键字的含义见表10。

<div style="text-align: center;">表 10 属性元模型类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Property</td><td style='text-align: center;'>定义属性类的关键字</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>注释元素的固定语法；不同的元素包含的固定语法不同，属性元模型包含两个固定语法；local-Label、description</td></tr><tr><td style='text-align: center;'>unit</td><td style='text-align: center;'>单位，只有是在 Int 或者 Real 类型的时候选择单位，形式为带双引号的字符串</td></tr><tr><td colspan="2">注：标点符号说明：annotation 内部内容以半角逗号“，”隔开，属性定义结尾以半角分号“；”结束。</td></tr></table>

#### 6.2.6 角色元模型类语法

角色元模型类定义对象元模型如何参与关系元模型。关系元模型应通过角色元模型间接关联对象元模型，关系元模型的一些特征被转移到角色元模型。角色元模型类可包含角色的属性，应包含角色元模型的注释。角色元模型类语法见示例。

示例：

Export Role deriveTo // deriveTo 是角色元模型的唯一编码。

initial Property unique address111 extends address00 annotation(localLabel="地址"); //角色元模型属性 annotation

(
localLabel="输出角色", //角色元模型名称。
description="角色的描述", //角色元模型描述。
)

shape="solid arrow", //角色元模型形状。
);
end deriveTo;

角色类元模型类语法中关键字的含义见表11。

<div style="text-align: center;">表 11 角色元模型类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Export</td><td style='text-align: center;'>定义角色的方向，端口方向有三种：始端（Import），终端（Export），无向端（Undirected）</td></tr><tr><td style='text-align: center;'>Role</td><td style='text-align: center;'>定义角色元模型的关键字</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>角色元模型包含三个固定语法：localLabel、description、shape</td></tr><tr><td style='text-align: center;'>Shape</td><td style='text-align: center;'>角色的形状定义，为建模提供多种形状展示，shape已有三种，包含：实心箭头（solidArrow），虚心箭头（dottedArrow），箭形（arrowShape），实心菱形（solidDiamond），虚心菱形（dottedDiamond），无形状（none），圆环（ring），实心圆（solidCircle）</td></tr><tr><td colspan="2">标点符号说明：annotation（）内部内容以半角逗号“，”隔开，外部使用半角分号“；”，角色元模型属性使用以半角分号“；”，角色元模型定义结尾end+点ID后用半角分号“；”结束。</td></tr></table>

#### 6.2.7 元模型扩展子集合

##### 6.2.7.1 通则

元模型扩展集合表达模型要素的引用关系，可包含分解、剖视以及类引用，见图3，其中：

a） 分解: 对象元模型类、点元模型类、关系元模型类或角色元模型类可分解为 1 个或者多个图元模型类；

b）剖视：对象元模型类、点元模型类与关系元模型类可剖视为1个或者多个图元模型类；

c) 类引用：属性元模型类可与图元模型类、对象元模型类、点元模型类、关系元模型类、角色元模型类或者属性元模型类建立类引用关系。

<div style="text-align: center;"><img src="imgs/img_in_image_box_233_1028_969_1447.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 3 元模型类引用关系</div>


##### 6.2.7.2 分解

展开视图的一种形式，通过一个新的视图展示视图中一个对象（关系、角色、点）内部包含的构造。

元模型中，一个对象（关系、角色、点）可分解出多个新的视图。分解过程应在图元模型中配置，关键词是 decompose，定义在 Constraint() 之中，分解在图元模型的语法见 6.2.1。

##### 6.2.7.3 剖视

展开视图的一种形式，剖视从一个或多个视图的角度对原视图中一个对象（关系、点）的内部构造进行展示。剖视过程应在图元模型中配置，关键词是 explode，定义在 Constraint() 之中，剖视在图元模型的语法见 6.2.1。

##### 6.2.7.4 类引用

用于在模型中通过属性引用对象、关系、角色、点、属性等模型，类引用通常在属性元模型中定义。类引用通过关键词 class<> 实现，包含图类型（class<Graph, ID>）、对象类型（class<Object, ID>）、关系类型（class<Relationship, ID>）、点类型（class<Point, ID>）、角色类型（class<Role, ID>）、属性类型（class<Property, ID>），这里 ID 是该元素的唯一编码。同样，多个同样类型使用关键词 classArray<> 实现。属性元模型中定义对象类型的语法见示例。

示例：

class<Object, obj1> Property property 1 annotation(localLabel="属性1", unit="null", description="属性元模型"); // obj1 是引用的对象类的唯一编码，property 1 是属性元模型的唯一编码。

class Array<Object, obj1, obj2> Property property1 annotation(localLabel="属性2", unit="null", description="属性元模型"); // obj1, obj2 为引用的两个对象类的唯一编码，property1 是属性元模型的唯一编码。

### 6.3 模型类集合

#### 6.3.1 图模型实例类语法

图模型实例类是对图元模型的实例化，图模型实例类可包含对象实例类和关系实例类，对象实例类和关系实例类通过连接器进行绑定，并在注释中，可包含甘特图、矩阵、SysML外框等插件类。以某性能需求图为例，图模型实例类定义语法见示例。

示例：

partial Model RequirementDiagram instanceof requirement1 // RequirementDiagram 为模型的唯一编码，requirement1 为该模型实例化的元模型的唯一编码。

ObjectInstances //需求图中的对象实例类，具体展开在 6.3.2。

RelationshipInstances //需求图中的关系实例类，具体展开在 6.3.3。

Connect(
    connector(object1, relationship1.role1), //object1 是对象实例的唯一编码，relationship1 是关系实例的唯一编码、role1 是角色的唯一编码。该连接器的含义是对象 object1 与关系 relationship1 的角色 role1 连接在一起。
    connector(object1, relationship1.role2),
    .....
); //连接器实例

annotation(
    localLabel="性能需求图", //图模型命名。
    SIDentification="null",
    plug-inClass //插件类，具体展开在 6.5。
)

);
end RequirementDiagram;

图模型实例类关键字的含义见表 12。

<div style="text-align: center;">表 12 图模型实例类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Model</td><td style='text-align: center;'>定义图模型的关键字</td></tr><tr><td style='text-align: center;'>instanceof</td><td style='text-align: center;'>专指图模型通过继承图元模型实例化</td></tr><tr><td style='text-align: center;'>connect</td><td style='text-align: center;'>表示对象和对象的连接关系，并通过两个 connector（）实现</td></tr><tr><td style='text-align: center;'>connector</td><td style='text-align: center;'>表示连接器，可包含对象模型与角色模型绑定的连接器，或点模型与角色模型绑定的连接器</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>图模型应包含固定语法 localLabel，可包含插件类 plug-inClass</td></tr><tr><td style='text-align: center;'>plug-inClass</td><td style='text-align: center;'>图中包含的插件包含：甘特图、矩阵、SysML 外框，在 6.5 具体介绍</td></tr></table>

#### 6.3.2 对象实例类语法

对象实例类语法定义一种实例化的对象，对象实例类可包含多个属性实例、点实例、分解、剖视，应包含注释。对象实例类定义语法见示例。

示例：

Object RequirementBlock refer object_Requirement //RequirementBlock 是对象实例的唯一编码，object Requirement 是该对象的元模型的唯一编码。

Property objProperty = “透平入口温度需求” refer objProperty_Requirement annotation(localLabel = “名称”, color = “0,0,0”, text = (“Microsoft YaHei UI”, 11, Normal, Normal), underline = false, strikeThrough = false); //objProperty 是对象的属性实例的唯一编码，属性值为命名为“透平入口温度需求”的字符串，objProperty_Requirement 是该属性的元模型的唯一编码，关键字具体介绍在 6.3.5 节。

PointInstances //对象中的点实例类，具体展开在 6.3.4。

annotation(
    initialLocation = (322, 365, 201, 103),
    localLabel = “需求”,
    shape = “rectangle”,
    color = “0,0,0;0,0,0;0,0,0;255,245,181;255,245,181”,
    screenMode = propertyMode,
    imageAddress = “image.jpg”,
    text = (“Microsoft YaHei UI”, 11, Normal, Normal),
    iconDisplay = true,
    frame = (1, “solid”),
    visualizationList = “”,
);
end RequirementBlock; //完成对象实例的创建。

对象实例类关键字的含义见表 13。

<div style="text-align: center;">表 13 对象实例类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Object</td><td style='text-align: center;'>定义对象模型的关键字</td></tr><tr><td style='text-align: center;'>refer</td><td style='text-align: center;'>模型中表示继承元模型的关键字</td></tr><tr><td style='text-align: center;'>Property</td><td style='text-align: center;'>定义对象模型属性的关键字</td></tr><tr><td style='text-align: center;'>PointInstance</td><td style='text-align: center;'>代表点模型，点模型的展开细节在下问有介绍，这里用于占位</td></tr><tr><td style='text-align: center;'>decompose:</td><td style='text-align: center;'>定义该对象的分解图</td></tr><tr><td style='text-align: center;'>explode:</td><td style='text-align: center;'>定义该对象的剖视图</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>注释，对象模型包含的固定语法</td></tr><tr><td style='text-align: center;'>initialLocation</td><td style='text-align: center;'>定义对象在画布的位置及尺寸大小，以对象最外框左上角为该对象的定位点，以画布左上角为坐标(0,0)点，定义对象定位点横坐标及对象定位点纵坐标，对象外框长和对象外框宽确定对象模型的尺寸大小。所有数值均为整数，单位为毫米</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>对象模型的形状与对象元模型形状种类相同，默认为对象元模型形状，根据具体建模要求进行变更</td></tr><tr><td style='text-align: center;'>color</td><td style='text-align: center;'>定义对象的颜色，颜色为对象填充颜色、边框颜色、字体颜色三部分组成，每种颜色由三原色数字代码组成</td></tr><tr><td style='text-align: center;'>screenMode</td><td style='text-align: center;'>显示模式，可是分解模式、剖视模式、属性模式、容器模式</td></tr><tr><td style='text-align: center;'>imageAddress</td><td style='text-align: center;'>定义对象的背景图，背景图名应是png、jpg、gif、svg等格式，图标名显示为带双引号的图标名全称</td></tr><tr><td style='text-align: center;'>text</td><td style='text-align: center;'>定义对象中文字的风格，如字体，字号，加粗体，斜体。字体显示为带双引号的字体名称，字号为整数，加粗显示为Bold，不加粗显示为Normal，是斜体显示为Italic，不是斜体显示为Normal</td></tr><tr><td style='text-align: center;'>iconDisplay</td><td style='text-align: center;'>布尔值，当显示图标时为true，不显示为false</td></tr><tr><td style='text-align: center;'>frame</td><td style='text-align: center;'>对象边框，定义边框大小和线条样式</td></tr><tr><td style='text-align: center;'>visualizationList</td><td style='text-align: center;'>定义分解剖视的视图内容</td></tr></table>

#### 6.3.3 关系实例类语法

关系实例类定义一种实例化的关系，可包含关系的属性实例，分解、剖视，应包含两个角色以及注释。关系实例类定义语法见示例。

示例：

Relationship relationship1 refer metaRelationship //relationship1 是关系模型的唯一编码，metaRelationship 是继承的关系元模型的唯一编码。

Property relationship_property_1 = "null" refer Relationship_Oper1 annotation(localLabel="名称", color="0", 0, 0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

RoleInstances //角色中的点实例类，具体展开在 6.3.6。

annotation(
    localLabel = "作战控制流",
    shape = "dashLine",
    endLocation = (179, 217; 179, 399),
    polylineLocation = "(179, 217); (300, 400); (179, 399)",
);

color="136,136,136;0,0,0",
labelDisplay=true,
text=("Microsoft YaHei UI",8,Normal,Normal),
smoothness="None",
avoidObstructionsRouting=false,
closestDistanceRouting=false,
jumpLinkStatus="Below",
jumpLinkType="Semicircle",
reverseJumpLink=false,
routingType="Manhattan",
);

关系实例类关键字及固有参数的含义见表 14。

<div style="text-align: center;">表 14 关系实例类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Relationship</td><td style='text-align: center;'>定义关系元模型的关键字</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>关系模型的形状与关系元模型形状种类相同，默认为关系元模型形状，应根据具体建模要求进行变更</td></tr><tr><td style='text-align: center;'>endLocation</td><td style='text-align: center;'>关系两端点位置坐标，分为始点横、纵坐标（179,217），终点横纵坐标（179,399），数据类型为整型，单位为毫米</td></tr><tr><td style='text-align: center;'>polylineLocation</td><td style='text-align: center;'>表示关系中的这点数量和坐标，用数字字符串表示，字符串中第一位数字3为关系中折点的数量（包含始端和终端），坐标分别为（179,217），（300,400），（179,399）</td></tr><tr><td style='text-align: center;'>color</td><td style='text-align: center;'>关系线的颜色</td></tr><tr><td style='text-align: center;'>labelDisplay</td><td style='text-align: center;'>关系的关系名称显示控制，当值为true时，显示关系名称；当值为false时，不显示关系名称</td></tr><tr><td style='text-align: center;'>smoothness</td><td style='text-align: center;'>关系线的平滑度，None为无平滑，Normal为正常的平滑，Less为较少平滑，More为更多平滑</td></tr><tr><td style='text-align: center;'>avoidObstructionsRouting</td><td style='text-align: center;'>布尔值，true为避开障碍，false为不避障</td></tr><tr><td style='text-align: center;'>closestDistanceRouting</td><td style='text-align: center;'>布尔值，true为最短距离，false为关闭最短距离</td></tr><tr><td style='text-align: center;'>jumpLinkStatus</td><td style='text-align: center;'>跳转连接状态，None为无跳转，All为跳转所有连接，Above为向上跳转，Below为向下跳转</td></tr><tr><td style='text-align: center;'>jumpLinkType</td><td style='text-align: center;'>跳转连接类型，Semicircle为半圆型，Square为直接型，Chamfered为倒棱型，Tunnel为隧道型</td></tr><tr><td style='text-align: center;'>reverseJumpLink</td><td style='text-align: center;'>布尔值，true为开启反向跳转连接，false为关闭反向跳转连接</td></tr><tr><td style='text-align: center;'>routingType</td><td style='text-align: center;'>布线样式，Manhattan为斜体，Straight为直线，Tree为树形</td></tr></table>

#### 6.3.4 点实例类语法

点实例类定义一种实例化的端口，可包含点的属性实例，分解、剖视，应包含点的注释。点实例类定义语法见示例。

示例：

Point point1 refer metaPoint1 //point1 是点模型的唯一编码，metaPoint1 是继承的点元模型的唯一编码。
Property point_property_1 = "null" refer point_Oper1 annotation(localLabel="名称", color="0,0,0", text="(Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);
annotation(
    localLabel="接口点",
    initialLocation=(59, -12, 22, 22),
    shape="triangle",
    color="0,0,0;0,0,0;0,0,0",
    text="(Microsoft YaHei UI", 7, Normal, Normal),
    iconDisplay=false,
    labelDisplay=false,
);
end metaObjPoint_point_Point1_d70e_57fd;

属性实例类关键字及固有参数的含义见表 15。

<div style="text-align: center;">表 15 属性实例类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Point</td><td style='text-align: center;'>定义点实例的关键字</td></tr><tr><td style='text-align: center;'>Property</td><td style='text-align: center;'>定义属性实例类的关键字</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>注释元素的固定语法</td></tr><tr><td style='text-align: center;'>labelLocation</td><td style='text-align: center;'>端口名称在画布中的位置</td></tr><tr><td style='text-align: center;'>initialLocation</td><td style='text-align: center;'>端口的初始位置</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>点模型的形状与点元模型形状种类相同，默认为点元模型形状，应根据具体建模要求进行变更</td></tr><tr><td style='text-align: center;'>color</td><td style='text-align: center;'>端口的颜色</td></tr><tr><td style='text-align: center;'>iconDisplay</td><td style='text-align: center;'>布尔值，true 为展示点的图标，false 为不展示点的图标</td></tr><tr><td style='text-align: center;'>labelDisplay</td><td style='text-align: center;'>布尔值，true 为展示点的名称，false 为不展示点的名称</td></tr><tr><td colspan="2">标点符号说明：annotation 内部内容以半角逗号“，”隔开，属性定义结尾以半角分号“；”结束。</td></tr></table>

#### 6.3.5 角色实例类语法

角色实例类定义一种实例化的角色元，可包含角色的属性、分解，应包含角色的注释。角色实例类定义的语法见示例。

示例：

Role role1 refer role_combeFrom //role1 是角色实例的唯一编码，role_combeFrom 是继承的角色元模型的唯一编码。

annotation(
    localLabel="组合始端",
    shape="solidDiamond"
);

end role1;

角色实例类关键字的含义见表 16。

<div style="text-align: center;">表 16 角色实例类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Role</td><td style='text-align: center;'>定义角色元模型的关键字</td></tr><tr><td style='text-align: center;'>refer</td><td style='text-align: center;'>含义与对象模型中相同</td></tr><tr><td style='text-align: center;'>decompose</td><td style='text-align: center;'>含义与对象模型中相同</td></tr><tr><td style='text-align: center;'>annotation</td><td style='text-align: center;'>角色模型包含两个固定语法：localLabel、shape</td></tr><tr><td style='text-align: center;'>shape</td><td style='text-align: center;'>定义角色模型的形状，默认情况下与角色元模型定义的形状相同，在角色模型中应手动进行变更</td></tr></table>

#### 6.3.6 模型扩展子集合

##### 6.3.6.1 通则

模型扩展集合表达模型要素引用关系，模型实例之间可包含分解、剖视、实例引用、克隆及拷贝，见图4，其中：

a）分解：对象实例、点实例、关系实例以及角色实例可分解为图模型实例，每个实例应分解为一个图模型实例；

b）剖视：对象实例、点实例以及关系实例可剖视为一个或多个图模型实例；

c）类引用：属性实例可引用多个图模型实例、对象实例、点实例、关系实例、角色实例或属性实例；

d）克隆：对象实例可通过克隆与另一个对象实例保持数据同步，且遵循组合关系；

e）拷贝：对象实例可通过拷贝产生另一个对象实例，同步拷贝时的数据，且遵循聚合关系。

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_935_976_1387.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 4 模型实例类引用关系</div>


##### 6.3.6.2 分解

模型实例中，每一个对象（关系、角色、点）实例实体只应分解为一个模型实例，通过 this.decompose

( )指定分解的目标模型,分解在对象模型应按照以下语法结构描述。

##### 6.3.6.3 剖视

模型实例中，每一个对象（关系、点）实例实体只应剖视为不同元模型对应的多个模型实例，通过this.explode()指定剖视的目标模型，剖视在对象应按照以下语法结构描述。

##### 6.3.6.4 属性类引用

模型中属性引用具体类在属性值中标识应见示例的语法结构描述。

示例：

Property pro11=class<obj1> refer pro1 annotation(localLabel="名称", color="0,0,0", text="Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);
Property pro21="classArray<obj1,obj2,...objn>" refer pro2 annotation(localLabel="名称", color="0,0,0", text="Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

<div style="text-align: center;"><img src="imgs/img_in_image_box_101_598_138_625.jpg" alt="Image" width="3%" /></div>


##### 6.3.6.5 克隆

将一个模型中的对象克隆至同一个模型或另外一个模型中，克隆体对象保持与源对象属性的同步，当源对象的属性发生变化时，克隆体的属性同步发生变化，反之亦然。克隆应通过关键词 clone 实现引用，包含对象、点及属性的克隆。克隆至另外一个模型的实现应需满足该模型中存在此对象的元模型，即原对象模型所引用的对象元模型在该图元模型之中。克隆在对象模型应见示例的语法结构描述。

示例：

Object obj11 clone obj1 //对象 obj11 克隆自对象 obj1。

Property pro11="×××" clone pro1 annotation(localLabel="名称", color="0,0,0", text=("Microsoft YaHei UI",7,Normal,Normal),underline=false,strikeThrough=false); //属性 pro11 克隆自属性 pro1。

Point point11 clone point1 //点 point11 克隆自点 point1。

.....

end point11;

annotation(
.....
);

end obj11;

##### 6.3.6.6 拷贝

将一个模型中的对象复制至同一个或另一个模型中，实现快速重构原有对象及属性信息，复制体对象修改后不同步至源对象。拷贝应通过关键字 copy 实现引用，包含对象、点及属性的拷贝。拷贝的实现应满足该模型中存在此对象的元模型，即原对象模型 ID 所引用的对象元模型在该图元模型之中。克隆在对象模型应见示例的语法结构描述。

示例：

Object obj11 copy obj1 //对象 obj11 拷贝自对象 obj1。

Property pro11 = "×××" copy pro1 annotation(localLabel = "名称", color = "0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false); //属性 pro11 拷贝自属性 pro1。

Point point11 copy point1 //点 point11 拷贝自点 point1。

.....

end point11;

annotation(
    .....
);
end obj11;

### 6.4 组织类集合

#### 6.4.1 项目类

项目类是开始统一架构建模语言建立的根节点，项目类应准许定义多个语言类。项目类定义的语法见示例。

示例：

Project pro1 annotation(localLabel="×××") //Project 为项目类定义的关键字，pro1 为定义项目类的唯一编码。
language //项目可包含多个语言内容。
.....
end pro1

#### 6.4.2 语言类

语言类是建模语言元模型类及模型类的集合。语言类定义的语法见示例。

示例：

Language lanl annotation(localLabel="×××") //Language 为语言类定义的关键字，lan1 为语言类定义的唯一编码。
meta-model of graph //语言应包含图元模型的内容。
meta-model of object //语言应包含对象元模型的内容。
meta-model of relationship //语言应包含关系元模型的内容。
meta-model of point //语言应包含点元模型的内容。
meta-model of property //语言应包含属性元模型的内容。
meta-model of role //语言应包含角色元模型的内容。
model //语言应包含模型的内容。
end lan1

#### 6.4.3 包类

包类是多个模型的集合，应用于表示由同一项目元模型实例化或相关性较大的模型的集合。语言类中应定义多个包类。

在包类中应定义多个模型类，应通过添加包类实现模型的需求、功能、逻辑、架构等设计阶段的归类或导航。包类定义的语法见示例。

示例：

Package pac1 annotation(localLabel="×××") //Package 为包类定义的关键字，pac1 为定义包类的唯一编码。
package //包内可包含多个包内容。
model //包内可包含多个模型内容。
.....
end pac1

### 6.5 插件类集合

#### 6.5.1 甘特图类

甘特图类应通过条状图来显示项目、进度和其他时间相关的系统进展的内在关系随着时间进展的情况，甘特图类没有元模型定义，是在每个模型视图中都应添加的插件元素。甘特图类定义的语法见示例。

示例：

GanttChart gantt //gantt 是定义甘特图的唯一编码。

(
    localLabel="甘特图", //甘特图名称。
    location=(600,400,300,400), //甘特图位置和大小。
    color="255,255,255;0,0,0;0,0,0", //甘特图背景颜色。
    time=(“年”;2;22;34), //时间单位，时间间隔，起始时间，终止时间。
    “task1” //甘特图任务名称。

    gantt1(“甘特图1”;30;20;“255,0,255;0,0,0;0,0,0”), //子任务1。
    gantt2(“甘特图2”;60;20;“255,255,0;0,0,0;0,0,0”), //子任务2。
)

“task2” //甘特图任务名称。

(
    gantt3(“甘特图3”;30;20;“255,0,255;0,0,0;0,0,0”), //子任务。
)
),

甘特图类关键字的含义见表17。

<div style="text-align: center;">表 17 甘特图类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>GanttChart</td><td style='text-align: center;'>定义甘特图的关键字</td></tr><tr><td style='text-align: center;'>localLabel</td><td style='text-align: center;'>同属性元模型中解释</td></tr><tr><td style='text-align: center;'>location</td><td style='text-align: center;'>确定甘特图的位置和大小</td></tr><tr><td style='text-align: center;'>color</td><td style='text-align: center;'>甘特图背景颜色的定义</td></tr><tr><td style='text-align: center;'>time</td><td style='text-align: center;'>定义甘特图的时间单位，有“年”“月”“日”“时”“分”“秒”，间隔表示在起始时间和结束时间之间每间隔几个单位进行显示</td></tr><tr><td colspan="2">数量说明：GanttChart有0次或多次定义，GanttChart中的子任务0次或多次定义；标点符号说明：除time及子任务内部使用半角分号“；”，其他的结束位置都使用半角逗号“，”。</td></tr></table>

#### 6.5.2 矩阵类

矩阵类是在系统设计中说明关系的一种传统媒介，是使用最少空间说明大量关系最有效的一种方式。矩阵类定义的语法见示例。

示例：

Matrix cellName //cellName 是矩阵插件定义唯一编码
(
localLabel="矩阵", //矩阵插件名称
location=(10,0,0,0), //矩阵插件的位置
value=" $$ 1,3;4,6;7,9 $$ ", //矩阵内容,应为数值型或者字符串
),

矩阵类关键字及固有参数的含义见表 18。

<div style="text-align: center;">表 18 矩阵类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Matrix</td><td style='text-align: center;'>定义矩阵的关键字</td></tr><tr><td style='text-align: center;'>location</td><td style='text-align: center;'>确定矩阵的位置和大小</td></tr><tr><td style='text-align: center;'>value</td><td style='text-align: center;'>定义矩阵的内容，形式为矩阵的字符串，或者是属性的 ID</td></tr><tr><td colspan="2">数量说明：Matrix 有 0 次或多次定义。标点符号说明：结束位置都使用半角逗号“，”。</td></tr></table>

#### 6.5.3 布局类

布局类是针对 SysML 语言定义的插件，主要应强调模型的头部信息，应包含四段信息：模型的名称、元模型的类型、模型元素类型、模型元素名称。布局类定义的语法见示例。

示例：

Layout drawing // drawing 为外框定义的唯一编码
localLabel="SysML 外框", // 模型的名称。
diagramKind=bdd, // 元模型的类型。
modelElementType=block, // 模型元素的类型。
modelElementName="String", // 模型元素的名称。
location=(10,0,0,0) // 外框的位置和大小。
),

布局类关键字的含义见表19。

<div style="text-align: center;">表 19 布局类含义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>关键字</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Layout</td><td style='text-align: center;'>定义 SysML 外框插件的关键字</td></tr><tr><td style='text-align: center;'>bdd</td><td style='text-align: center;'>元模型类型包含模块定义图(bdd)、内部模块图(ibd)、用例图(uc)、活动图(act)、序列图(sd)、状态机图(stm)、参数图(par)、需求图(req)、包图(pkg)</td></tr><tr><td style='text-align: center;'>modelElementType</td><td style='text-align: center;'>模型元素类型，每个图都代表已经在系统模型中某处定义的元素，这里声明该元素的类型</td></tr><tr><td style='text-align: center;'>modelElementName</td><td style='text-align: center;'>声明该模型元素的名称</td></tr><tr><td style='text-align: center;'>location</td><td style='text-align: center;'>确定 SysML 外框的位置和大小</td></tr><tr><td colspan="2">数量说明: Layout 有 0 次或多次定义。 标点符号说明: 结束位置都使用半角逗号“，”。</td></tr></table>

附录 A

(资料性)

架构语言建模示例

### A.1 可视化示例

该模型中包含两个名称为内部模块的对象实例，其中一个属性实例的名称为飞机控制系统，另一个属性实例的名称为飞机动力系统。对象实例之间的关系实例，名称为控制信息。每个对象实例各包含一个点实例，名称均为电子接口，见图 A.1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_514_1041_912.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 A.1 案例模型图</div>


### A.2 元模型示例

#### A.2.1 图元模型

图 A.1 中①，模型对应的图元模型为 neibujiegou。该图元模型中描述了所配置的图元模型 ID、对象元模型 ID、关系元模型 ID，以及关系元模型的绑定关系、图类型、图元模型本地名称、图元模型的描述内容，见图 A.2。

partial Graph neibumokuai // 图元模型 ID 为 “neibumokuai”。
Object neibumokuai; // 配置的对象元模型 ID 为 “neibumokuai”。
Relationship connectors; // 配置的关系元模型 ID 为 “connectors”。
Constraint( // 绑定关系。
    bind connector(neibumokuai, connectors.Role_Link_Input), // 绑定始端: 对象元模型 neibumokuai; 绑定终端: 与关系元模型 connectors 绑定的 Role_Link_Input 角色元模型。
    bind connector(neibumokuai, neibumokuai_jiekou_452c14, connectors.Role_Link_Input), // 绑定始端: 依附于对象元模型 neibumokuai 的点元模型 neibumokuai_jiekou_452c14; 绑定终端: 与关系元模型 connectors 绑定的 Role_Link_Input 角色元模型。
    bind connector(neibumokuai, connectors.Role_Link_Output), // 绑定始端: 对象元模型 neibumokuai; 绑定终端: 与关系元模型 connectors 绑定的 Role_Link_Output 角色元模型。

<div style="text-align: center;">图 A.2 图元模型</div>


bind connector(neibumokuai.neibumokuai_jiekou_452c14, connectors.Role_Link_Output), //绑定始端；依附于对象元模型neibumokuai的点元模型neibumokuai_jiekou_452c14；绑定终端：与关系元模型connectors绑定的Role_Link_Output角色元模型。
);

annotation(
    localLabel="内部结构图", //图元模型的本地名称为"内部结构图"。
    type=diagram, //图类型为diagram。
    description="", //描述内容为空。
);

end neibujiegoutu; //图元模型ID为"neibujiegoutu"。

<div style="text-align: center;">图 A.2 图元模型（续）</div>


#### A.2.2 对象元模型

图 A.1 中②，模型中包含的对象元模型有 neibumokuai，该对象元模型中描述了对象元模型 ID 等信息，以及配置的属性和点的信息，见图 A.3。

Object neibumokuai //对象元模型ID为“neibumokuai”。

initial Property neibumokuai_env_Name_e79f8f="null" extends env_Name annotation(localLabel="名称"); //对象元模型配置的属性元模型ID为“env_Name”，属性ID为“neibumokuai_env_Name_e79f8f”，属性的本地名称为“名称”，属性的值为“null”。

Undirected Point neibumokuai_jiekou_452c14 extends jiekou annotation(localLabel="接口"); //对象元模型配置的点元模型ID为“jiekou”，点ID为“neibumokuai_jiekou_452c14”，点的本地名称为“接口”。

annotation(
    localLabel="内部模块", //对象元模型的本地名称为“内部模块”。
    description="", //对象元模型的描述为空。
    icon="", //对象元模型的图标为默认。
    shape="rectangle", //对象元模型的形状为“rectangle”，表示矩形。
    visualizedMode=propertyMode, //对象元模型的可视化模式为propertyMode。
    imageAddress="", //对象元模型无背景图片。
    UnfoldDirection=Y, //在容器模式下支持方向。
);

end neibumokuai; //对象元模型的ID为“neibumokuai”。

<div style="text-align: center;">图 A.3 对象元模型</div>


#### A.2.3 关系元模型

图 A.1 中③，模型中包含的关系元模型有 connectors，该关系元模型中描述了关系元模型 ID 等信息，以及配置的属性和角色的信息，见图 A.4。

Relationship connectors //关系元模型 ID 为“connectors”。
initial Property connectors_env_Name_df6ecb = "null" extends env_Name annotation(localLabel = "名称"); //关系元模型配置的属性元模型 ID 为“env_Name”，属性的 ID 为“connectors_env_Name_df6ecb”，属性的本地名称为“名称”，属性的值为“null”。
Role Role_Link_Input; //关系元模型绑定的角色元模型 ID 为“Role_Link_Input”。

<div style="text-align: center;">图 A.4 关系元模型</div>


Role Role_Link_Output; //关系元模型绑定的角色元模型 ID 为“Role_Link_Output”。

annotation(
    localLabel="连接器", //关系元模型的本地名称为“连接器”。
    description="", //关系元模型描述为空。
    icon="", //关系元模型图标为默认。
    shape="boldSolidLine", //关系元模型的形状为"boldSolidLine"。
);

end connectors; //关系元模型的 ID 为"connectors"。

<div style="text-align: center;">图 A.4 关系元模型（续）</div>


#### A.2.4 属性元模型

图 A.1 中②对象元模型中包含的属性元模型有 env_Name，该属性元模型中描述了属性元模型 ID、属性名、属性单位等信息，见图 A.5。

String Property env_Name annotation(localLabel = "名称", unit = "null", description = ""); // 属性类型为 "String", 属性元模型 ID 为 "env_Name", 属性名为 "名称", 属性单位为 "null", 属性描述内容为空。

<div style="text-align: center;">图 A.5 属性元模型</div>


#### A.2.5 角色元模型

见图 A.1 中③关系元模型包含的角色元模型有 Role_Link_Input 和 Role_Link_Output 两种，角色元模型中描述了角色元模型 ID、本地名称等信息，见图 A.6。

Import Role Role_Link_Input //角色的方向端口为“始端”，角色元模型ID为“Role_Link_Input”。
annotation(
    localLabel="链接输入", //角色的本地名称为“链接输入”。
    description="", //角色的描述为空。
    shape="no", //角色的形状为“no”，表示无形状。
);
end Role_Link_Input; //角色元模型ID为“Role_Link_Input”。

Export Role Role_Link_Output //角色的方向端口为“终端”，角色元模型ID为“Role_Link_Output”。
annotation(
    localLabel="链接输出", //角色的本地名称为“链接输出”。
    description="", //角色的描述为空。
    shape="no", //角色的形状为“no”。
);
end Role_Link_Output; //角色的元模型ID为“Role_Link_Output”。

<div style="text-align: center;">b) Role Link Output</div>


<div style="text-align: center;">图 A.6 角色元模型</div>


#### A.2.6 点元模型

图 A.1 中②对象元模型包含的点元模型有 jiekou，点元模型中描述了点元模型 ID、配置的属性、本地名称等信息，见图 A.7。

Point jiekou //点元模型的 ID 为“jiekou”。

initial Property jiekou_env_Name_c69e78 = "null" extends env_Name annotation(localLabel = "名称");
//点元模型配置的属性元模型 ID 为“env_Name”，属性名为“名称”，属性 ID 为“jiekou_env_Name_c69e78”。

annotation(
    localLabel = "接口", //点的本地名称为“接口”。
    description = "", //点的描述为空。
    shape = "circle", //点的形状为圆形。
    imageAddress = "", //点无背景图片。
);

end jiekou; //点元模型 ID 为“jiekou”。

<div style="text-align: center;">图 A.7 点元模型</div>


### A.3 模型示例

#### A.3.1 图

图 A.1 中的④表示模型，该模型为图元模型的实例。在下方代码中，“neibujiegoutu”代表图元模型的 ID，“model_neibujiegoutu_9aa9d”代表模型 ID，“内部结构图示例”代表模型的本地名称，见图 A.8。

partial Model model_neibujiegoutu_9aa9d instanceof neibujiegoutu //模型 ID 为“model_neibujiegoutu_9aa9d”，图元模型 ID 为“neibujiegoutu”。

annotation(
    localLabel="内部结构图示例", //本地名称为"内部结构图示例"。
);

end model_neibujiegoutu_9aa9d; //模型 ID 为“model_neibujiegoutu_9aa9d”。

<div style="text-align: center;">图 A.8 图</div>


#### A.3.2 对象、点、属性

图 A.1 中的⑤表示对象，图中包含两个“内部模块”对象，每个对象包含一个“名称”属性以及一个“电子接口”点。以其中一个对象为例，下方代码定义了该对象、对象具有的属性、依附于对象的点的相关信息，见图 A.9。

Object model_neibujiegoutu_9aa9d_object_d22d refer neibumokuai //对象元模型ID为“neibumokuai”，对象ID为“model_neibujiegoutu_9aa9d_object_d22d”。

Property model_neibujiegoutu_9aa9d_object_d22d_property_1fb2 = “飞机控制系统” refer neibumokuai_env_Name_e79f8f annotation (localLabel = “名称”, color = “0, 0, 0”, text = (“Microsoft YaHei UI”, 8, Normal, Normal), underline = false, strikeThrough = false);

//该对象具有的属性ID为“neibumokuai_env_Name_e79f8f”，实例化后的属性ID为“model_neibujiegoutu_9aa9d_object_d22d_property_1fb2”，属性名为“名称”，属性值为“飞机控制系统”。

Point model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23 refer neibumokuai_jiekou_452c14 //该对象配置的点ID为“neibumokuai_jiekou_452c14”，实例化后的点ID为“model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23”。

<div style="text-align: center;">图 A.9 对象、点、属性</div>


Property model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23_property_f683="null" refer_jiekou_env_Name_c69e78_annotation(localLabel="名称", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false); //该点具有的属性ID为“jiekou_env_Name_c69e78”，实例化后的属性ID为“model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23_property_f683”，属性名为“名称”，属性值为“null”。

annotation(
    localLabel="电子接口", //点的本地名称为“电子接口”。
    initialLocation=(168,56,22,22), //点的位置为(168,56,22,22)。
    shape="circle", //点的形状为圆形。
    color="136,136,136;0,0,0;0,0,0", //点的颜色为“136,136,136;0,0,0;0,0,0”。
    text=("Microsoft YaHei UI", 7, Normal, Normal),
    iconDisplay=false, //是否展示图标：否。
    labelDisplay=false, //是否展示标签：否。
    imageAddress="", //点无背景照片。
);

end model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23;

annotation(
    initialLocation=(308,245,178,113), //对象在模型中的位置为(308,245,178,113)。
    localLabel="内部模块", //对象的本地名称为“内部模块”。
    shape="rectangle", //对象的形状为矩形。
    color="0,0,0;0,0,0;0,0,0;194,239,255;255,255,255", //对象的颜色为“0,0,0;0,0,0;0,0,0;0,0,0;194,239,255;255,255,255”。
    screenMode=propertyMode, //对象的显示模式为“显示属性模型”。
    imageAddress="", //对象无背景照片。
    SDIdentification="",
    text=("Microsoft YaHei UI", 8, Normal, Normal),
    iconDisplay=true, //图标是否展示：“是”。
    frame=(1,"solid"), //对象边框设置。
    visualizationList="", //无分解剖视。
);

end model_neibujiegoutu_9aa9d_object_d22d; //对象的ID为“model_neibujiegoutu_9aa9d_object_d22d”

<div style="text-align: center;">图 A.9 对象、点、属性（续）</div>


#### A.3.3 关系、属性、角色

图 A.1 中的⑥表示关系。下方代码定义了该关系的 ID、关系具有的属性、与关系绑定的角色以及关系两端绑定的模型元素等相关信息，见图 A.10。

Relationship model_neibujiegoutu_9aa9d_relationship_13d9 refer connectors//关系元模型ID为“connectors”，关系ID为“model_neibujiegoutu_9aa9d_relationship_13d9”。

Property model_neibujiegoutu_9aa9d_relationship_13d9_property_2592="null" refer connectors_env_Name_df6ecb annotation(localLabel="名称", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false); //该关系具有的属性ID为“connectors_env_Name_df6ecb”，实例化后的属性ID为“model_neibujiegoutu_9aa9d_relationship_13d9_property_2592”，属性名为“名称”，属性值为“null”。

<div style="text-align: center;">图 A.10 关系、属性、角色</div>


Role model_neibujiegoutu_9aa9d_fromrole_cc74 refer Role_Link_Input //该关系绑定的角色元模型ID为“Role_Link_Input”，角色ID为“model_neibujiegoutu_9aa9d_fromrole_cc74”。

annotation(
    localLabel="链接输入", //角色的本地名称为“链接输入”。
    shape="no" //角色的形状为“no”，表示没有形状。
);

end model_neibujiegoutu_9aa9d_fromrole_cc74;

Role model_neibujiegoutu_9aa9d_torole_f876 refer Role_Link_Output //该关系绑定的角色元模型ID为“Role_Link_Output”，角色ID为“model_neibujiegoutu_9aa9d_torole_f876”。

annotation(
    localLabel="链接输出", //角色的本地名称为“链接输出”。
    shape="no" //角色的形状为“no”，表示没有形状。
);

end model_neibujiegoutu_9aa9d_torole_f876;

annotation(
    localLabel="控制信息", //该关系的本地名称为“控制信息”。
    shape="boldSolidLine", //该关系的形状为“boldSolidLine”。
endLocation=(397,301;869,302), //该关系的端点坐标为(397,301;869,302)。

polylineLocation="[0,0,-136,0]$ [136,0,0,0];(1,0,0.4);(0,0,0.5)",//该关系的各折点坐标为“[0,0,-136,0]$ [136,0,0,0];(1,0,0.4);(0,0,0.5)”。

color="136,136,136;0,0,0", //该关系的颜色为“136,136,136;0,0,0”。

labelDisplay=true, //是否显示标签“是”。

text=("Microsoft YaHei UI",8,Normal,Normal),

smoothness="None", //线的平滑度为“None”。

avoidObstructionsRouting=false,//避开障碍。

closestDistanceRouting=false,//线最短距离。

jumpLinkStatus="None", //跳转链接状态为“None”。

jumpLinkType="Semicircle", //跳转链接类型为“Semicircle”。

reverseJumpLink=false, //反向跳转链接；否。

routingType="Manhattan", //关系线型为Manhattan。
);

end model_neibujiegoutu_9aa9d_relationship_13d9;

Connect(connector(model_neibujiegoutu_9aa9d_object_d22d.model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23,model_neibujiegoutu_9aa9d_relationship_13d9,model_neibujiegoutu_9aa9d_fromrole_cc74),connector(model_neibujiegoutu_9aa9d_object_956b.model_neibujiegoutu_9aa9d_object_956b_undirected_1714,model_neibujiegoutu_9aa9d_relationship_13d9,model_neibujiegoutu_9aa9d_torole_f876));//该关系与两个元素相连接：依附于model_neibujiegoutu_9aa9d_object_d22d对象的点model_neibujiegoutu_9aa9d_object_d22d_undirected_aa23；依附于model_neibujiegoutu_9aa9d_object_956b对象的点model_neibujiegoutu_9aa9d_object_956b_undirected_1714。

<div style="text-align: center;">图 A.10 关系、属性、角色（续）</div>


## 附录 B

(资料性)

飞机机载维护与健康管理系统示例

### B.1 建模需求

飞机机载维护与健康管理系统的主要功能是接收飞机机组告警系统的告警信息和其他系统计算机内置自检模块记录的故障数据，利用中央维护计算机或者中央维护功能软件将二者关联生成维护报告。维护人员通过维护报告查询手册确定故障源，但是飞机最终是否投入运行一般根据通用飞机维修系统消息和最低设备清单确定。同时，通用飞机维修系统还为维护人员提供开展地面测试，数据加载，查看构型，监控飞机状态等功能。

飞机机载维护与健康管理系统的主要使用者是航空公司地面维护人员和飞机运行监控人员，使用场景包括飞机制造检测、航线维护、机库维护、飞机运营状态监控、飞机运行数据分析等。系统的另一个潜在使用者是飞行机组，一定条件下机组人员能查看维护系统采集的飞机健康状态数据以辅助了解飞机运行状态。机载维护系统作为维护支持工具，高效地支持航空公司进行开展维护活动或健康监控活动。机载维护系统的主要设计依据包括行业标准、公司规范、航空公司调研信息和前置型号经验积累等。

图 B.1 展示的飞机机载维护与健康管理系统由中央维护子系统、飞机状态监控子系统及机载数据加载子系统组成，为飞机提供故障检测与隔离、系统健康数据收集与监控、机上软件或数据库升级更新等维护服务。本案例系统建模分为使命、运行、功能、逻辑和物理进行建模。

<div style="text-align: center;"><img src="imgs/img_in_image_box_140_868_1031_1189.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 B.1 案例研究对象</div>


### B.2 元模型

机载维护系统建模流程见图 B.2。

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_207_1051_665.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 B.2 建模方法论</div>


机载维护系统通过使命分析、运行分析、功能分析、逻辑架构分析以及物理架构分析阶段完成基于模型的架构设计过程，指导后续设计方案的权衡以及仿真验证等工作，自定义的领域元模型库见表B.1。

<div style="text-align: center;">表 B.1 机载维护系统特定域元模型库</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>建模流程</td><td style='text-align: center;'>图元模型</td><td style='text-align: center;'>对象元模型</td><td style='text-align: center;'>关系元模型</td></tr><tr><td rowspan="2">使命分析阶段</td><td style='text-align: center;'>模块定义图</td><td style='text-align: center;'>值类型、接口模块、包、视图、约束模块、模块、注释</td><td style='text-align: center;'>关联、附属、组合、泛化、项目流、约束</td></tr><tr><td style='text-align: center;'>活动图</td><td style='text-align: center;'>动作概率、开始、节点、发送动作、栓、终止、分流、选择、时间事件、接受事件、动作、注释</td><td style='text-align: center;'>连接注释、对象流、控制流</td></tr><tr><td rowspan="2">运行分析阶段</td><td style='text-align: center;'>用例图</td><td style='text-align: center;'>包、参与者、用例、边界系统、环境、外部系统、传感器、系统上下文</td><td style='text-align: center;'>包含、关联、扩展、归纳、控制</td></tr><tr><td style='text-align: center;'>活动图</td><td style='text-align: center;'>动作概率、开始、节点、发送动作、栓、终止、分流、选择、时间事件、接受事件、动作、注释</td><td style='text-align: center;'>连接注释、对象流、控制流</td></tr><tr><td rowspan="2">功能分析阶段</td><td style='text-align: center;'>模块定义图</td><td style='text-align: center;'>值类型、接口模块、包、视图、约束模块、模块、注释</td><td style='text-align: center;'>关联、附属、组合、泛化、项目流、约束</td></tr><tr><td style='text-align: center;'>活动图</td><td style='text-align: center;'>动作概率、开始、节点、发送动作、栓、终止、分流、选择、时间事件、接受事件、动作、注释</td><td style='text-align: center;'>连接注释、对象流、控制流</td></tr><tr><td rowspan="2">逻辑设计阶段</td><td style='text-align: center;'>序列图</td><td style='text-align: center;'>生命线、信息</td><td style='text-align: center;'>信号</td></tr><tr><td style='text-align: center;'>状态机图</td><td style='text-align: center;'>结束、开始、动作、状态、历史标记、点、注释、叉、发送动作、选择、仿真参数模块、性能模型模块</td><td style='text-align: center;'>转换</td></tr><tr><td rowspan="2">物理架构设计阶段</td><td style='text-align: center;'>模块定义图</td><td style='text-align: center;'>值类型、接口模块、包、视图、约束模块、模块、注释</td><td style='text-align: center;'>关联、附属、组合、泛化、项目流、约束</td></tr><tr><td style='text-align: center;'>内部模块图</td><td style='text-align: center;'>值、接口模块、连接器、内部模块、注释、约束</td><td style='text-align: center;'>附属、传递、对象流、项目流</td></tr></table>

模块定义图的图元模型描述如下，定义2个图属性，声明8个对象元模型，声明6个关系元模型，定义15个绑定关系，定义2个剖视，见示例1。

## 示例 1:

partial Graph Block_Definition_Diagram // 定义模块定义图。

initial Property Block_Definition_Diagram_Property_To_Do_3ac03f="null" extends Property_To_Do_annotation(localLabel="待办事项");

initial Property Block_Definition_Diagram_Property_Context_9794be="null" extends Property_Context_annotation(localLabel="上下文");

Object Object_Package;
Object Object_Block;
Object Object_Interface_Block;
Object Object_Flow_Specification;
Object Object_Constraint_Block;
Object Object_Domain;
Object Object_Subsystem;
Relationship Relationship_Interface_Realization;
Relationship Relationship_Link;
Relationship Relationship_Association_Block;
Relationship Relationship_Directed_Association;
Relationship Relationship_Association;
Relationship Relationship_Directed_Aggregation;
Constraint(
    bind connector(Object_Block, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_System, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_System_Context, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_Domain, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_Subsystem, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_Constraint_Block, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_Interface_Block, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_External, Relationship_Interface_Realization.Role_Implementing_Classifier),
    bind connector(Object_Flow_Specification, Relationship_Interface_Realization.Role_Contract),
    bind connector(Object_Interface, Relationship_Interface_Realization.Role_Contract),
    bind connector(Object_Interface, Relationship_Containment.Role_Part),
    bind connector(Object_Package, Relationship_Containment.Role_Part),
    bind connector(Object_Unit, Relationship_Containment.Role_Part),
    bind connector(Object_Block, Relationship_Containment.Role_Whole),
    bind connector(Object_System, Relationship_Containment.Role_Whole),
    Object_Interface_Block.explode(Internal_Block_Diagram),
    Object_Constraint_Block.explode(Internal_Block_Diagram),
);

annotation(
    localLabel="模块定义图",
    type=diagram,
    description="",
);

end Block_Definition_Diagram;

活动图的图元模型描述如下，包含两个图属性，声明 12 个对象元模型，声明 3 个关系元模型，定义 12 个绑定关系，定义 5 个剖视和 4 个分解，见示例 2。

## 示例 2:

partial Graph Activity_Diagram

initial Property Activity_Diagram_Property_To_Do_4f5d74 = "null" extends Property_To_Do_annotation (localLabel = "待办事项");

initial Property Activity_Diagram_Property_Context_2475bb = "null" extends Property_Context_annotation (localLabel = "上下文");

Object Object_Call_Behavior_Action;
Object Object_Call_Operation_Action;
Object Object_Opaque_Action;
Object Object_Central_Buffer_Node;
Object Object_Data_Store_Node;
Object Object_Activity_Parameter_Node;
Object Object_Send_Signal_Action;
Object Object_Accept_Event_Action;
Object Object_Accept_Time_Event_Action;
Object Object_Accept_Change_Structural_Feature_Event_Action;
Object Object_Initial_Node;
Object Object_Activity_Final_Node;
Relationship Relationship_Control_Flow;
Relationship Relationship_Object_Flow;
Relationship Relationship_Exception_Handler;
Constraint(
    bind connector(Object_Opaque_Action, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Initial_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Structured_Activity_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Accept_Event_Action, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Decision_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Fork_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Accept_Time_Event_Action, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Conditional_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Sequence_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Merge_Node, Relationship_Control_Flow, Role_Source),
    bind connector(Object_Send_Signal_Action, Relationship_Control_Flow, Role_Source),
    ence_Node_Point_Input_Pin_8f74f4, Relationship_Exception_Handler, Role_Exception_Input),
    bind connector(Object_Structured_Activity_Node, Object_Structured_Activity_Node_Point_Action_Input_Pin_7d44d9, Relationship_Exception_Handler, Role_Exception_Input),
    Object_Conditional_Node.explode(Activity_Diagram),
    Object_Loop_Node.explode(Activity_Diagram),
    Object_Swimlanes.explode(Activity_Diagram),
    Object_Call_Behavior_Action.explode(Activity_Diagram),
    Object_Block.explode(Activity_Diagram),
    Object_Interruptible_Activity_Region.decompose(Activity_Diagram),
    Object_Structured_Activity_Node.decompose(Activity_Diagram),
    Object_Expansion_Region.decompose(Activity_Diagram),
    Object_Sequence_Node.decompose(Activity_Diagram),

);

annotation(
    localLabel="活动图",
    type=diagram,
    description="",
);

end Activity_Diagram;

内部模块图部分描述如下，包含2个图属性，声明6个对象元模型，声明4个关系元模型，定义12个绑定关系，定义3个分解，见示例3。

示例 3:

partial Graph Internal_Block_Diagram

initial Property Internal_Block_Diagram_Property_To_Do_c37486="null" extends Property_To_Do_annotation(localLabel="待办事项");

initial Property Internal_Block_Diagram_Property_Context_9f574a="null" extends Property_Context_annotation(localLabel="上下文");

Object Object_Value_Property;
Object Object_Part_Property;
Object Object_Reference_Property;
Object Object_Constraint_Property;
Object Object_Flow_Property;
Object Object_Participant_Property;
Relationship Relationship_Connector;
Relationship Relationship_Binding_Connector;
Relationship Relationship_Item_Flow_Connector;
Relationship Relationship_Item_Flow_Binding_Connector;
Constraint(
    bind connector (Object_Reference_Property.Object_Reference_Property_Point_Proxy_Port_0f0b10, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Constraint_Property.Object_Constraint_Property_Point_Flow_Port_acf89, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Bound_Reference, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Reference_Property.Object_Reference_Property_Point_Constraint_Parameter_aaf75b, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Part_Property, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Classifier_Behavior_Property, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Reference_Property, Object_Reference_Property_Point_Full_Port_06fd14, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Part_Property, Object_Part_Property_Point_Constraint_Parameter_119082, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Reference_Property, Object_Reference_Property_Point_Port_b44640, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Constraint_Property, Object_Constraint_Property_Point_Constraint_Parameter_850c76, Relationship_Connector.Role_Connectot_End_A),
    bind connector (Object_Constraint_Property, Object_Constraint_Property_Point_Full_Port_2ca47c, Relationship_Connector.Role_Connectot_End_A),

bind connector (Object_Constraint_Property.Object_Constraint_Property_Point_Proxy_Port_d887al, Relationship_Connector.Role_Connectot_End_A),
Object_Part_Property.decompose(Internal_Block_Diagram),
Object_Reference_Property.decompose(Internal_Block_Diagram),
Object_Constraint_Property.decompose(Internal_Block_Diagram),
);
annotation(
    localLabel="内部模块图",
    type=diagram,
    description="",
);
end Internal_Block_Diagram;

时序图描述如下,包含2个图属性,声明2个对象元模型,声明1个关系元模型,定义2个绑定关系,见示例4。

示例 4:

partial Graph Sequence_Diagram

initial Property Sequence_Diagram_Property_To_Do_d3ddca="null" extends Property_To_Do_annotation(localLabel="待办事项");

initial Property Sequence_Diagram_Property_Context_847d79="null" extends Property_Context_annotation(localLabel="上下文");

Object Lifeline;
Object Object_Block;
Relationship Message;
Constraint(
    bind connector(Lifeline, Message.Message_Source),
    bind connector(Lifeline, Message.Message_Target),
);

annotation(
    localLabel="时序图",
    type=sequenceDiagram,
    description="",
);

end Sequence_Diagram;

状态机图描述如下，包含2个图属性，声明13个对象元模型，声明1个关系元模型，定义32个绑定关系，定义4个剖视，见示例5。

示例 5:

partial Graph State_Machine_Diagram

initial Property State_Machine_Diagram_Property_To_Do_a9cfle="null" extends Property_To_Do annotation (localLabel="待办事项");

initial Property State_Machine_Diagram_Property_Context_43446a="null" extends Property_Context annotation (localLabel="上下文");

Object Object_State;

Object Object_Composite_State;

Object Object_Orthogonal_State;

Object Object Submachine State;

Object Object Initial Pseudo State;

Object Object Final State;

Object Object_Terminate_Pseudo_State;

Object Object_Deep_History_Pseudostate;

Object Object_Shallow_History_Pseudo_State;

Object Object Junction Pseudo State;

Object Object_Choice_Pseudo_State;

Object Object_Fork_Pseudo_State;

Object Object_Join_Pseudo_State;

Relationship Relationship_Transition;

Constraint(

bind connector(Object_Terminate_Pseudo_State, Relationship_Transition, Role_Source),

bind connector(Object_Orthogonal_State, Relationship_Transition.Role_Source),

bind connector(Object_Composite_State.Object_Composite_State_Point_Pseudo_State_373e35, Relationship_Transition.Role_Source),

bind connector(Object_State, Relationship_Transition, Role_Source),

bind connector(Object_Submachine_State, Relationship_Transition.Role_Source),

bind connector(Object_Fork_Pseudo_State, Relationship_Transition.Role_Source),

bind connector(Object_Join_Pseudo_State, Relationship_Transition.Role_Source),

bind connector(Object_State.Object_State_Point_Pseudo_State_4d1a30, Relationship_Transition.Role_Source),

bind connector(Object_Deep_History_Pseudostate, Relationship_Transition.Role_Source),

bind connector(Object_Shallow_History_Pseudo_State, Relationship_Transition, Role_Source),

bind connector(Object_Initial_Pseudo_State, Relationship_Transition.Role_Source),

bind connector(Object_Choice_Pseudo_State, Relationship_Transition, Role_Source),

bind connector(Object_Junction_Pseudo_State, Relationship_Transition.Role_Source),

bind connector(Object_Orthogonal_State.Object_Opaque_Action_Point_Pseudo_State_981043, Relationship_Transition.Role_Source),

bind connector(Object_Submachine_State.Object_Submachine_State_Point_Connection_Point_Reference_b39e28, Relationship_Transition.Role_Source),

bind connector(Object_Composite_State, Relationship_Transition.Role_Source),

bind connector(Object_Terminate_Pseudo_State, Relationship_Transition.Role_Target),

bind connector(Object_Orthogonal_State, Relationship_Transition.Role_Target),

bind connector(Object_Composite_State.Object_Composite_State_Point_Pseudo_State_373e35, Relationship_

### Transition.Role Target),

bind connector(Object_State, Relationship_Transition, Role_Target),

bind connector(Object_Submachine_State, Relationship_Transition.Role_Target),

bind connector(Object_Fork_Pseudo_State, Relationship_Transition.Role_Target),

bind connector(Object_Join_Pseudo_State, Relationship_Transition.Role_Target),

bind connector(Object_Final_State, Relationship_Transition.Role_Target),

bind connector(Object_State.Object_State_Point_Pseudo_State_4d1a30, Relationship_Transition.Role_Target),

bind connector(Object_Deep_History_Pseudostate, Relationship_Transition.Role_Target),

bind connector(Object_Shallow_History_Pseudo_State, Relationship_Transition.Role_Target),

bind connector(Object_Choice_Pseudo_State, Relationship_Transition.Role_Target),

bind connector(Object_Junction_Pseudo_State, Relationship_Transition.Role_Target),

bind connector(Object_Orthogonal_State.Object_Opaque_Action_Point_Pseudo_State_981043, Relationship_Transition.Role_Target),

bind connector(Object_Submachine_State.Object_Submachine_State_Point_Connection_Point_Reference_b39e28, Relationship_Transition.Role_Target),

bind connector(Object_Composite_State, Relationship_Transition.Role_Target),

Object_State.explode(State_Machine_Diagram),

Object_Submachine_State.explode(State_Machine_Diagram),

Object_Composite_State.explode(State_Machine_Diagram),

Object_Orthogonal_State.explode(State_Machine_Diagram),

);

annotation(
    localLabel="状态机图",
    type=diagram,
    description="",
);

end State_Machine_Diagram;

用例图部分语言描述如下，包含2个图属性，声明8个对象元模型，声明5个关系元模型，定义28个绑定关系，定义4个剖视，见示例6。

示例 6:

partial Graph Use_Case_Diagram

initial Property Use_Case_Diagram_Property_To_Do_da51d5="null" extends Property_To_Do_annotation (localLabel="待办事项");

initial Property Use_Case_Diagram_Property_Context_afc85d="null" extends Property_Context_annotation (localLabel="上下文");

Object Object_Actor;
Object Object_Use_Case;
Object Object_Boundary_System;
Object Object_Environmental_Effect;
Object Object_External_System;
Object Object_Sensor;
Object Object_System_Context;
Object_Package;
Relationship Relationship_Include;
Relationship Relationship_Extend;
Relationship Relationship_Association;
Relationship Relationship_Generalization;
Relationship Relationship_Containment;
Constraint(
    bind connector(Object_Use_Case, Relationship_Include.Role_Including_Case),
    bind connector(Object_Use_Case, Relationship_Include.Role_Addition),
    bind connector(Object_Use_Case, Relationship_Extend.Role_Extension),
    bind connector(Object_Use_Case, Relationship_Extend.Role_Extended_Case),
    bind connector(Object_Boundary_System, Relationship_Association.Role_Role_B),
    bind connector(Object_External_System, Relationship_Association.Role_Role_B),
    bind connector(Object_System_Context, Relationship_Association.Role_Role_B),

bind connector(Object_Actor, Relationship_Association.Role_Role_B),
bind connector(Object_Sensor, Relationship_Association.Role_Role_B),
bind connector(Object_Use_Case, Relationship_Association.Role_Role_B),
bind connector(Object_Boundary_System, Relationship_Association.Role_Role_A),
bind connector(Object_Boundary_System, Relationship_Generalization.Role_General),
bind connector(Object_External_System, Relationship_Generalization.Role_General),
bind connector(Object_System_Context, Relationship_Generalization.Role_General),
bind connector(Object_Actor, Relationship_Generalization.Role_General),
bind connector(Object_Use_Case, Relationship_Generalization.Role_General),
bind connector(Object_Boundary_System, Relationship_Containment.Role_Part),
bind connector(Object_User_System, Relationship_Containment.Role_Part),
bind connector(Object_System_Context, Relationship_Containment.Role_Part),
bind connector(Object_Actor, Relationship_Containment.Role_Part),
bind connector(Object_Use_Case, Relationship_Containment.Role_Part),
bind connector(Object_Package, Relationship_Containment.Role_Part),
bind connector(Object_Boundary_System, Relationship_Containment.Role_Whole),
bind connector(Object_User_System, Relationship_Containment.Role_Whole),
bind connector(Object_System_Context, Relationship_Containment.Role_Whole),
bind connector(Object_Actor, Relationship_Containment.Role_Whole),
bind connector(Object_Use_Case, Relationship_Containment.Role_Whole),
bind connector(Object_Package, Relationship_Containment.Role_Whole),
Object_Block.explode(Internal_Block_Diagram),
Object_System_Context.explode(Internal_Block_Diagram),
Object_Package.decompose(Use_Case_Diagram),
);

annotation(
    localLabel="用例图",
    type=diagram,
    description="",
);

end Use_Case_Diagram;

### B.3 模型

#### B.3.1 使命分析阶段

在驾驶舱预先准备阶段，飞机首先进行系统上电，若上电失败，则进行辅助动力装置（APU）进行供电；若上电成功，则进行系统维护数据和健康数据的监控，并将数据进行记录。模型示意见图 B.3。

<div style="text-align: center;"><img src="imgs/img_in_image_box_386_204_818_920.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图 B.3 使命分析阶段模型示意图</div>


模型中对象实例“初始伪状态”的语法见示例。

示例：

partial Model_State_Machine_Diagram_9594e instance of State_Machine_Diagram

Property model_State_Machine_Diagram_9594e_property_54ad = "null" refer State_Machine_Diagram_Property_To_Do_a9ef1e annotation(localLabel = "待办事项", color = "0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false);

Property model_State_Machine_Diagram_9594e_property_9c2d = "null" refer State_Machine_Diagram_Property_Context_43446a annotation(localLabel = "上下文", color = "0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false);

Object model_State_Machine_Diagram_9594e_object_649c refer Object_Initial_Pseudo_State

Property model_State_Machine_Diagram_9594e_object_649c_property_f6d9 = "null" refer Object_Initial_Pseudo_State_Property_Name_8df0e9 annotation(localLabel = "名称", color = "0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false);

Property model_State_Machine_Diagram_9594e_object_649c_property_91cd = "null" refer Object_Initial_Pseudo_State_Property_To_Do_0010ed annotation(localLabel = "待办事项", color = "0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false);

annotation(
    initialLocation = (447, 140, 83, 46),
);

localLabel="初始伪状态",
shape="circle",
color="194,239,255;0,0,0;0,0,0",
screenMode=blankMode,
imageAddress="",
SDIdentification="",
text=("Microsoft YaHei UI",8,Normal,Normal),
iconDisplay=true,
frame=(0,"solid"),
visualizationList="",
);
end model_State_Machine_Diagram_9594e_object_649c;
.....

#### B.3.2 运行分析阶段

定义了机载维护与健康管理系统的使用和运行阶段，包括：飞机的行前准备阶段、推出/牵引和开发动机、画出、起飞、爬升、地面维护、硬/重着陆等阶段。模型示意见图 B.4。

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_737_1044_1367.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 B.4 运行分析阶段模型示意图</div>


模型中对象实例“初始伪状态”和“最终状态”的语法见示例：

示例：

partial Model_State_Machine_Diagram_675e4_instanceof_State_Machine_Diagram

Property model_State_Machine_Diagram_675e4_property_87d7="null" refer State_Machine_Diagram_Property_To_Do_a9cf1e_annotation(localLabel="待办事项", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_property_0c3a="null" refer State_Machine_Diagram_Property_Context_43446a_annotation(localLabel="上下文", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Object model_State_Machine_Diagram_675e4_object_5792_refer_Object_Initial_Pseudo_State

Property model_State_Machine_Diagram_675e4_object_5792_property_029d="null" refer Object_Initial_Pseudo_State_Property_Name_8df0e9_annotation(localLabel="名称", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_object_5792_property_117c="null" refer Object_Initial_Pseudo_State_Property_To_Do_0010ed_annotation(localLabel="待办事项", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

annotation(
    initialLocation=(74, 50, 106, 101),
    localLabel="初始伪状态",
    shape="circle",
    color="194,239,255;0,0,0;0,0,0",
    screenMode=blankMode,
    imageAddress="",
    SDIdentification="",
    text=("Microsoft YaHei UI", 8, Normal, Normal),
    iconDisplay=true,
    frame=(0,"solid"),
    visualizationList="",
);

end model_State_Machine_Diagram_675e4_object_5792;

Object model_State_Machine_Diagram_675e4_object_2762_refer_Object_Final_State

Property model_State_Machine_Diagram_675e4_object_2762_property_8252="null" refer Object_Final_State_Property_Name_d73887_annotation(localLabel="名称", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_object_2762_property_9c5d="null" refer Object_Final_State_Property_To_Do_cd58a6_annotation(localLabel="待办事项", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_object_2762_property_e4ff="null" refer Object_Final_State_Property_Redefined_Vertex_8d4b3f_annotation(localLabel="重定义顶点", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_object_2762_property_66a7="null" refer Object_Final_State_Property_Entry_Behavior_Element_b3affc_annotation(localLabel="入口行为元素", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_object_2762_property_89f6="null" refer Object_Final_State_Property_Do_Activity_Behavior_Element_3c6e7b_annotation(localLabel="执行活动行为元素", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property model_State_Machine_Diagram_675e4_object_2762_property_116f="null" refer Object_Final_State_Property_Exit_Behavior_Element_207108 annotation(localLabel="出口行为元素", color="0,0,0", text="(Microsoft YaHei UI",7,Normal,Normal),underline=false,strikeThrough=false);

annotation(
    initialLocation=(815,553,101,101),
    localLabel="最终状态",
    shape="circle",
    color="194,239,255;0,0,0;0,0,0",
    screenMode=blankMode,
    imageAddress="",
    SDIdentification="",
    text="(Microsoft YaHei UI",8,Normal,Normal),
    iconDisplay=true,
    frame=(0,"solid"),
    visualizationList="",
);

end model_State_Machine_Diagram_675e4_object_2762;

#### B.3.3 功能分析阶段

该模型为启动测试功能，成员系统启动测试功能，最后将测试结果给到维护人员，模型示意见图 B.5。

<div style="text-align: center;"><img src="imgs/img_in_image_box_117_819_1052_1290.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 B.5 功能分析阶段模型示意图</div>


模型中对象实例“模块”的语法见示例：

示例：

partial Model h6Cj24q4 instanceof Activity_Diagram

Property h6Cj24q4_property_0885="null" refer Activity_Diagram_Property_To_Do_4f5d74 annotation(localLabel="待办事项", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);

Property h6Cj24q4_property_0114="null" refer Activity_Diagram_Property_Context_2475bb annotation(localLabel="上下文", color="0,0,0", text=("Microsoft YaHei UI", 7, Normal, Normal), underline=false, strikeThrough=false);
Object h6Cj24q4_object_91f8 refer Object_Block
this.explode(pgH6ENh3);
annotation(
    initialLocation=(185,100,303,418),
    localLabel="模块",
    shape="rectangle",
    color="0,0,0;0,0,0;0,0,0;194,239,255;255,255,255",
    screenMode=decompositionMode,
    imageAddress="",
    SDIntification="",
    text=("Microsoft YaHei UI", 8, Normal, Normal),
    iconDisplay=true,
    frame=(1,"solid"),
    visualizationList="pgH6ENh3:(0,0,303,418)",
);
end h6Cj24q4_object_91f8;

#### B.3.4 逻辑架构分析阶段

图 B.6 所示为提供飞机状态信息功能场景时序图，先向机载维护与健康管理系统提供飞机的基本参数，随后机载维护与健康管理针对提供的基本参数进行计算，计算完成后将计算得到的状态消息输出给飞机，飞机接收相关状态消息。

<div style="text-align: center;"><img src="imgs/img_in_image_box_143_970_1058_1407.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 B.6 逻辑架构分析阶段模型示意图</div>


模型中对象实例“计算飞行状态消息参数”的语法见示例1：

示例 1:

partial Model sKIwwhQk instanceof Sequence_Diagram

Property sKIwwhQk_property_71ea = "null" refer Sequence_Diagram_Property_To_Do_d3ddca annotation (localLabel="待办事项", color="0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false);

Property sKIwwhQk_property_df6b = "null" refer Sequence_Diagram_Property_Context_847d79 annotation (localLabel="上下文", color="0,0,0", text = ("Microsoft YaHei UI", 7, Normal, Normal), underline = false, strikeThrough = false);

Object sKIwwhQk_Execution_Lifeline_3445 refer Lifeline

annotation(
    initialLocation = (324, 117, 10, 35),
    localLabel = "计算飞行状态消息参数",
    shape = "rectangle",
    color = "209,209,209;0,0,0;0,0,0,0",
    screenMode = propertyMode,
    imageAddress = "",
    SDIdentification = "Execution, relationship_Message_Message_Target_5c99",
    text = ("Microsoft YaHei UI", 7, Normal, Normal),
    iconDisplay = true,
    frame = (1, ""),
    visualizationList = "",
);

end sKIwwhQk_Execution_Lifeline_3445;

如图 B.7 所示，机载维护与健康管理系统的硬件由飞机健康监控单元、飞机健康监控单元托架、OMS IMA 驻留软件、OMS AHMU 软件、维护接口面板组成。

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_955_1035_1207.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 B.7 物理架构分析阶段模型示意图</div>


模型中对象实例“模块”包含对象属性“机载维护系统组成部件”的语法见示例2：

示例 2:

partial Model model_Block_Definition_Diagram_eefd_instanceof Block_Definition_Diagram

Property model_Block_Definition_Diagram_eefd_property_87af="null" refer Block_Definition_Diagram_Property_To_Do_3ac03f_annotation(localLabel="待办事项", color="0,0,0", text=("Microsoft YaHei UI",7, Normal,Normal),underline=false,strikeThrough=false);

Property model_Block_Definition_Diagram_eefd_property_c83e="null" refer Block_Definition_Diagram_Property_Context_9794be_annotation(localLabel="上下文", color="0,0,0", text=("Microsoft YaHei UI",7, Normal,Normal),underline=false,strikeThrough=false);

Object model_Block_Definition_Diagram_eefd_object_174b refer Object_Block

Property model_Block_Definition_Diagram_eefd_object_174b_property_19ba = “机载维护系统组成部件”
refer Object_Block_Property_Name_525f94 annotation(localLabel = “名称”, color = “0,0,0”, text = (“Microsoft YaHei UI”, 8, Normal, Normal), underline = false, strikeThrough = false);

annotation(
    initialLocation = (475, 135, 140, 70),
    localLabel = “模块”,
    shape = “rectangle”,
    color = “0,0,0;0,0,0;0,0,0;194,239,255;255,255,255”,
    screenMode = decompositionMode,
    imageAddress = “”,
    SDIidentification = “”,
    text = (“Microsoft YaHei UI”, 8, Normal, Normal),
    iconDisplay = true,
    frame = (1, “solid”),
    visualizationList = “”,
);

end model_Block_Definition_Diagram_eefd_object_174b;

## 附录 C

(资料性)

单位

单位表达式跟随在属性声明、属性初始化或属性赋值表达式中属性实例的后面，通过“unit”关键字定义单位表达式，见示例。表 C.1 展示统一架构建模语言单位。

示例：

<div style="text-align: center;">表 C.1 统一架构建模语言单位</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模语言语义</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模语言语义</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模语言语义</td></tr><tr><td style='text-align: center;'>系数</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>电阻</td><td style='text-align: center;'>Ohm</td><td style='text-align: center;'>ohm</td><td style='text-align: center;'>光量</td><td style='text-align: center;'>lm·s</td><td style='text-align: center;'>lms</td></tr><tr><td style='text-align: center;'>角度</td><td style='text-align: center;'>deg</td><td style='text-align: center;'>deg</td><td style='text-align: center;'>电阻率</td><td style='text-align: center;'>Ohm·m</td><td style='text-align: center;'>ohmm</td><td style='text-align: center;'>亮度</td><td style='text-align: center;'>cd/m²</td><td style='text-align: center;'>cd/m²</td></tr><tr><td style='text-align: center;'>弧度角</td><td style='text-align: center;'>rad</td><td style='text-align: center;'>rad</td><td style='text-align: center;'>传导率</td><td style='text-align: center;'>S/m</td><td style='text-align: center;'>s/m</td><td style='text-align: center;'>光出射</td><td style='text-align: center;'>lm/m²</td><td style='text-align: center;'>lm/m²</td></tr><tr><td style='text-align: center;'>立体角</td><td style='text-align: center;'>sr</td><td style='text-align: center;'>sr</td><td style='text-align: center;'>视在功率</td><td style='text-align: center;'>VA</td><td style='text-align: center;'>va</td><td style='text-align: center;'>照度</td><td style='text-align: center;'>lx</td><td style='text-align: center;'>lx</td></tr><tr><td style='text-align: center;'>长度</td><td style='text-align: center;'>m</td><td style='text-align: center;'>m</td><td style='text-align: center;'>物质的量</td><td style='text-align: center;'>mol</td><td style='text-align: center;'>mol</td><td style='text-align: center;'>曝光量</td><td style='text-align: center;'>lx·s</td><td style='text-align: center;'>lxs</td></tr><tr><td style='text-align: center;'>面积</td><td style='text-align: center;'>m²</td><td style='text-align: center;'>m²</td><td style='text-align: center;'>摩尔质量</td><td style='text-align: center;'>kg/mol</td><td style='text-align: center;'>kg/mol</td><td style='text-align: center;'>发光效率</td><td style='text-align: center;'>lm/W</td><td style='text-align: center;'>lm/w</td></tr><tr><td style='text-align: center;'>体积</td><td style='text-align: center;'>m³</td><td style='text-align: center;'>m³</td><td style='text-align: center;'>摩尔体积</td><td style='text-align: center;'>m³/mol</td><td style='text-align: center;'>m³/mol</td><td style='text-align: center;'>摩尔吸收系数</td><td style='text-align: center;'>m²/mol</td><td style='text-align: center;'>m²/mol</td></tr><tr><td style='text-align: center;'>角速度</td><td style='text-align: center;'>rad/s</td><td style='text-align: center;'>rad/s</td><td style='text-align: center;'>摩尔内能</td><td style='text-align: center;'>J/mol</td><td style='text-align: center;'>j/mol</td><td style='text-align: center;'>声阻抗</td><td style='text-align: center;'>(Pa·s)/m³</td><td style='text-align: center;'>pas/m³</td></tr><tr><td style='text-align: center;'>角加速度</td><td style='text-align: center;'>rad/s²</td><td style='text-align: center;'>rad/s²</td><td style='text-align: center;'>摩尔热容</td><td style='text-align: center;'>J/(mol·K)</td><td style='text-align: center;'>j/mol</td><td style='text-align: center;'>比声阻抗</td><td style='text-align: center;'>(Pa·s)/m</td><td style='text-align: center;'>pas/m</td></tr><tr><td style='text-align: center;'>速度</td><td style='text-align: center;'>m/s</td><td style='text-align: center;'>m/s</td><td style='text-align: center;'>摩尔速率</td><td style='text-align: center;'>mol/s</td><td style='text-align: center;'>mol/s</td><td style='text-align: center;'>响度级</td><td style='text-align: center;'>phon</td><td style='text-align: center;'>phon</td></tr><tr><td style='text-align: center;'>加速度</td><td style='text-align: center;'>m/s²</td><td style='text-align: center;'>m/s²</td><td style='text-align: center;'>跨导特性</td><td style='text-align: center;'>A/V²</td><td style='text-align: center;'>a/v²</td><td style='text-align: center;'>响度</td><td style='text-align: center;'>sone</td><td style='text-align: center;'>sone</td></tr><tr><td style='text-align: center;'>频率</td><td style='text-align: center;'>Hz</td><td style='text-align: center;'>hz</td><td style='text-align: center;'>反转电位</td><td style='text-align: center;'>1/V</td><td style='text-align: center;'>1/v</td><td style='text-align: center;'>分子数密度</td><td style='text-align: center;'>1/m³</td><td style='text-align: center;'>1/m³</td></tr><tr><td style='text-align: center;'>质量</td><td style='text-align: center;'>kg</td><td style='text-align: center;'>kg</td><td style='text-align: center;'>电力常数</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>n/a</td><td style='text-align: center;'>浓度</td><td style='text-align: center;'>mol/m³</td><td style='text-align: center;'>mol/m³</td></tr><tr><td rowspan="2">密度</td><td style='text-align: center;'>kg/m³</td><td style='text-align: center;'>kg/m³</td><td style='text-align: center;'>光谱辐射能密度</td><td style='text-align: center;'>J/m⁴</td><td style='text-align: center;'>j/m⁴</td><td style='text-align: center;'>化学势</td><td style='text-align: center;'>J/mol</td><td style='text-align: center;'>j/mol</td></tr><tr><td style='text-align: center;'>g/cm³</td><td style='text-align: center;'>g/cm³</td><td style='text-align: center;'>辐射强度</td><td style='text-align: center;'>W/sr</td><td style='text-align: center;'>w/sr</td><td style='text-align: center;'>分子极化率</td><td style='text-align: center;'>C·m²/V</td><td style='text-align: center;'>cm²/v</td></tr><tr><td style='text-align: center;'>力</td><td style='text-align: center;'>N</td><td style='text-align: center;'>n</td><td style='text-align: center;'>辐射亮度</td><td style='text-align: center;'>W/(sr·m²)</td><td style='text-align: center;'>w/srm²</td><td style='text-align: center;'>扩散系数</td><td style='text-align: center;'>m²/s</td><td style='text-align: center;'>m²/s</td></tr><tr><td style='text-align: center;'>刚度</td><td style='text-align: center;'>N/m</td><td style='text-align: center;'>n/m</td><td style='text-align: center;'>虚功率</td><td style='text-align: center;'>var</td><td style='text-align: center;'>var</td><td style='text-align: center;'>法拉第常数</td><td style='text-align: center;'>C/mol</td><td style='text-align: center;'>c/mol</td></tr></table>

<div style="text-align: center;">表 C.1 统一架构建模语言单位（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模
语言语义</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模
语言语义</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模
语言语义</td></tr><tr><td style='text-align: center;'>力矩</td><td style='text-align: center;'>N·m</td><td style='text-align: center;'>nm</td><td style='text-align: center;'>波数</td><td style='text-align: center;'>1/m</td><td style='text-align: center;'>1/m</td><td style='text-align: center;'>离子强度</td><td style='text-align: center;'>mol/kg</td><td style='text-align: center;'>mol/kg</td></tr><tr><td rowspan="2">压力</td><td style='text-align: center;'>Pa</td><td style='text-align: center;'>pa</td><td style='text-align: center;'>循环波数</td><td style='text-align: center;'>rad/m</td><td style='text-align: center;'>rad/m</td><td style='text-align: center;'>电导率</td><td style='text-align: center;'>S/m</td><td style='text-align: center;'>s/m</td></tr><tr><td style='text-align: center;'>bar</td><td style='text-align: center;'>bar</td><td style='text-align: center;'>分贝</td><td style='text-align: center;'>dB</td><td style='text-align: center;'>db</td><td style='text-align: center;'>摩尔电系数</td><td style='text-align: center;'>(S·m²)/mol</td><td style='text-align: center;'>sm²/mol</td></tr><tr><td style='text-align: center;'>能量</td><td style='text-align: center;'>J</td><td style='text-align: center;'>j</td><td style='text-align: center;'>比容</td><td style='text-align: center;'>m³/kg</td><td style='text-align: center;'>m³/kg</td><td style='text-align: center;'>旋磁系数</td><td style='text-align: center;'>(A·m²)/(J·s)</td><td style='text-align: center;'>am²/js</td></tr><tr><td style='text-align: center;'>能量密度</td><td style='text-align: center;'>J/m³</td><td style='text-align: center;'>j/m³</td><td style='text-align: center;'>线密度</td><td style='text-align: center;'>kg/m</td><td style='text-align: center;'>kg/m</td><td style='text-align: center;'>活度</td><td style='text-align: center;'>Bq</td><td style='text-align: center;'>bq</td></tr><tr><td style='text-align: center;'>功率</td><td style='text-align: center;'>W</td><td style='text-align: center;'>w</td><td style='text-align: center;'>面密度</td><td style='text-align: center;'>kg/m²</td><td style='text-align: center;'>kg/m²</td><td style='text-align: center;'>比活度</td><td style='text-align: center;'>Bq/kg</td><td style='text-align: center;'>bq/kg</td></tr><tr><td style='text-align: center;'>热力学温度</td><td style='text-align: center;'>K</td><td style='text-align: center;'>k</td><td style='text-align: center;'>动量</td><td style='text-align: center;'>(kg·m)/s</td><td style='text-align: center;'>kgm/s</td><td style='text-align: center;'>角截面</td><td style='text-align: center;'>m²/sr</td><td style='text-align: center;'>m²/sr</td></tr><tr><td style='text-align: center;'>温度斜率</td><td style='text-align: center;'>K/s</td><td style='text-align: center;'>k/s</td><td style='text-align: center;'>冲量</td><td style='text-align: center;'>N·s</td><td style='text-align: center;'>ns</td><td style='text-align: center;'>光谱截面</td><td style='text-align: center;'>m²/J</td><td style='text-align: center;'>m²/j</td></tr><tr><td style='text-align: center;'>线性温度因数</td><td style='text-align: center;'>1/K</td><td style='text-align: center;'>1/k</td><td style='text-align: center;'>角动量</td><td style='text-align: center;'>(kg·m²)/s</td><td style='text-align: center;'>kgm²/s</td><td style='text-align: center;'>光谱角截面</td><td style='text-align: center;'>m²/(sr·J)</td><td style='text-align: center;'>m²/srj</td></tr><tr><td style='text-align: center;'>二次温度因数</td><td style='text-align: center;'>1/K²</td><td style='text-align: center;'>1/k²</td><td style='text-align: center;'>角冲量</td><td style='text-align: center;'>N·m·s</td><td style='text-align: center;'>nms</td><td style='text-align: center;'>粒子注量</td><td style='text-align: center;'>1/m²</td><td style='text-align: center;'>1/m²</td></tr><tr><td style='text-align: center;'>压力因数</td><td style='text-align: center;'>Pa/K</td><td style='text-align: center;'>pa/k</td><td style='text-align: center;'>转动惯量</td><td style='text-align: center;'>kg·m²</td><td style='text-align: center;'>kgm²</td><td style='text-align: center;'>粒子注量率</td><td style='text-align: center;'>1/(s·m²)</td><td style='text-align: center;'>1/sm²</td></tr><tr><td style='text-align: center;'>压缩率</td><td style='text-align: center;'>1/pa</td><td style='text-align: center;'>1/pa</td><td style='text-align: center;'>平动阻
尼常数</td><td style='text-align: center;'>(N·s)/m</td><td style='text-align: center;'>ns/m</td><td style='text-align: center;'>能通量</td><td style='text-align: center;'>j/m²</td><td style='text-align: center;'>j/m²</td></tr><tr><td style='text-align: center;'>电流</td><td style='text-align: center;'>A</td><td style='text-align: center;'>a</td><td style='text-align: center;'>电力矩</td><td style='text-align: center;'>(N·m)/A</td><td style='text-align: center;'>nm/a</td><td style='text-align: center;'>能通量率</td><td style='text-align: center;'>W/m²</td><td style='text-align: center;'>w/m²</td></tr><tr><td style='text-align: center;'>电流斜率</td><td style='text-align: center;'>A/s</td><td style='text-align: center;'>a/s</td><td style='text-align: center;'>旋转弹
簧常数</td><td style='text-align: center;'>(N·m)/rad</td><td style='text-align: center;'>nm/rad</td><td style='text-align: center;'>粒子电
流密度</td><td style='text-align: center;'>1/(m²·s)</td><td style='text-align: center;'>1/m²s</td></tr><tr><td style='text-align: center;'>电荷</td><td style='text-align: center;'>C</td><td style='text-align: center;'>c</td><td style='text-align: center;'>旋转阻
尼常数</td><td style='text-align: center;'>(N·m·s)/rad</td><td style='text-align: center;'>nms/rad</td><td style='text-align: center;'>质量衰
减系数</td><td style='text-align: center;'>m²/kg</td><td style='text-align: center;'>m²/kg</td></tr><tr><td style='text-align: center;'>电荷体密度</td><td style='text-align: center;'>C/m³</td><td style='text-align: center;'>c/m³</td><td style='text-align: center;'>面积二阶矩</td><td style='text-align: center;'>m⁴</td><td style='text-align: center;'>m⁴</td><td style='text-align: center;'>线性功率</td><td style='text-align: center;'>J/m</td><td style='text-align: center;'>j/m</td></tr><tr><td style='text-align: center;'>电荷面密度</td><td style='text-align: center;'>C/m²</td><td style='text-align: center;'>C/m²</td><td style='text-align: center;'>质量流量</td><td style='text-align: center;'>kg/s</td><td style='text-align: center;'>kg/s</td><td style='text-align: center;'>总原子
阻止力</td><td style='text-align: center;'>J·m²</td><td style='text-align: center;'>jm²</td></tr><tr><td style='text-align: center;'>电场强度</td><td style='text-align: center;'>V/m</td><td style='text-align: center;'>v/m</td><td style='text-align: center;'>体积流量</td><td style='text-align: center;'>m³/s</td><td style='text-align: center;'>m³/s</td><td style='text-align: center;'>总质量
制动力</td><td style='text-align: center;'>(J·m²)/kg</td><td style='text-align: center;'>jm²/kg</td></tr><tr><td style='text-align: center;'>电势</td><td style='text-align: center;'>V</td><td style='text-align: center;'>v</td><td style='text-align: center;'>热通量</td><td style='text-align: center;'>W/m²</td><td style='text-align: center;'>w/m²</td><td style='text-align: center;'>动力</td><td style='text-align: center;'>m²/(V·s)</td><td style='text-align: center;'>m²/vs</td></tr><tr><td style='text-align: center;'>电势斜率</td><td style='text-align: center;'>V/s</td><td style='text-align: center;'>v/s</td><td style='text-align: center;'>热导</td><td style='text-align: center;'>W/K</td><td style='text-align: center;'>w/k</td><td style='text-align: center;'>中子源密度</td><td style='text-align: center;'>1/(m³·s)</td><td style='text-align: center;'>1/m³s</td></tr><tr><td style='text-align: center;'>电容</td><td style='text-align: center;'>F</td><td style='text-align: center;'>f</td><td style='text-align: center;'>热导率</td><td style='text-align: center;'>W/(m·K)</td><td style='text-align: center;'>w/mk</td><td style='text-align: center;'>吸收剂量</td><td style='text-align: center;'>Gy</td><td style='text-align: center;'>gy</td></tr></table>

<div style="text-align: center;">表 C.1 统一架构建模语言单位（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模语言语义</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模语言语义</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>单位</td><td style='text-align: center;'>多架构建模语言语义</td></tr><tr><td style='text-align: center;'>电容率</td><td style='text-align: center;'>F/m</td><td style='text-align: center;'>f/m</td><td style='text-align: center;'>热传递系数</td><td style='text-align: center;'>W/(m²·K)</td><td style='text-align: center;'>w/m²k</td><td style='text-align: center;'>剂量当量</td><td style='text-align: center;'>Sv</td><td style='text-align: center;'>sv</td></tr><tr><td style='text-align: center;'>电偶极矩</td><td style='text-align: center;'>C·m</td><td style='text-align: center;'>cm</td><td style='text-align: center;'>热绝缘</td><td style='text-align: center;'>(m²·K)/W</td><td style='text-align: center;'>m²2k/w</td><td style='text-align: center;'>吸收剂量率</td><td style='text-align: center;'>Gy/s</td><td style='text-align: center;'>gy/s</td></tr><tr><td style='text-align: center;'>电流密度</td><td style='text-align: center;'>A/m²</td><td style='text-align: center;'>a/m²</td><td style='text-align: center;'>热扩散率</td><td style='text-align: center;'>m²/s</td><td style='text-align: center;'>m²2/s</td><td style='text-align: center;'>照射</td><td style='text-align: center;'>C/kg</td><td style='text-align: center;'>c/kg</td></tr><tr><td style='text-align: center;'>线性电流密度</td><td style='text-align: center;'>A/m</td><td style='text-align: center;'>a/m</td><td style='text-align: center;'>热容</td><td style='text-align: center;'>J/K</td><td style='text-align: center;'>j/k</td><td style='text-align: center;'>照射率</td><td style='text-align: center;'>C/(kg·s)</td><td style='text-align: center;'>c/kgs</td></tr><tr><td style='text-align: center;'>磁通量密度</td><td style='text-align: center;'>T</td><td style='text-align: center;'>t</td><td style='text-align: center;'>比热容</td><td style='text-align: center;'>J/(kg·K)</td><td style='text-align: center;'>j/kgk</td><td style='text-align: center;'>光谱浓度</td><td style='text-align: center;'>s/m³</td><td style='text-align: center;'>s/m³</td></tr><tr><td style='text-align: center;'>磁通量</td><td style='text-align: center;'>Wb</td><td style='text-align: center;'>wb</td><td style='text-align: center;'>熵流量</td><td style='text-align: center;'>J/(K·s)</td><td style='text-align: center;'>j/ks</td><td style='text-align: center;'>状态密度</td><td style='text-align: center;'>1/(J·m³)</td><td style='text-align: center;'>1/jm³</td></tr><tr><td style='text-align: center;'>磁矢势</td><td style='text-align: center;'>Wb/m</td><td style='text-align: center;'>wb/m</td><td style='text-align: center;'>焓密度</td><td style='text-align: center;'>(kg·s²)/m⁵</td><td style='text-align: center;'>kgs²/m²5</td><td style='text-align: center;'>阻尼系数</td><td style='text-align: center;'>1/s</td><td style='text-align: center;'>1/s</td></tr><tr><td style='text-align: center;'>磁导率</td><td style='text-align: center;'>H/m</td><td style='text-align: center;'>h/m</td><td style='text-align: center;'>压力密度</td><td style='text-align: center;'>s²/m²</td><td style='text-align: center;'>s²/m²2</td><td style='text-align: center;'>对数减量</td><td style='text-align: center;'>1/S</td><td style='text-align: center;'>1/sa</td></tr><tr><td style='text-align: center;'>电磁矩</td><td style='text-align: center;'>A·m²</td><td style='text-align: center;'>am²2</td><td style='text-align: center;'>温度密度</td><td style='text-align: center;'>kg/(m³·K)</td><td style='text-align: center;'>kg/m³3k</td><td style='text-align: center;'>衰减系数</td><td style='text-align: center;'>1/m</td><td style='text-align: center;'>1/ma</td></tr><tr><td style='text-align: center;'>磁偶极矩</td><td style='text-align: center;'>Wb·m</td><td style='text-align: center;'>wbm</td><td style='text-align: center;'>压力焓</td><td style='text-align: center;'>(J·m·s²)/kg²</td><td style='text-align: center;'>jms²/kg²2</td><td style='text-align: center;'>默认单位</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>磁阻</td><td style='text-align: center;'>1/H</td><td style='text-align: center;'>1/h</td><td style='text-align: center;'>密度能量</td><td style='text-align: center;'>J·m³/kg</td><td style='text-align: center;'>jm³/kg</td><td style='text-align: center;'>时间</td><td style='text-align: center;'>s</td><td style='text-align: center;'>s</td></tr><tr><td style='text-align: center;'>磁导</td><td style='text-align: center;'>H</td><td style='text-align: center;'>h</td><td style='text-align: center;'>发光强度</td><td style='text-align: center;'>Cd</td><td style='text-align: center;'>cd</td><td style='text-align: center;'>热阻</td><td style='text-align: center;'>K/W</td><td style='text-align: center;'>k/w</td></tr><tr><td style='text-align: center;'>电导</td><td style='text-align: center;'>S</td><td style='text-align: center;'>s</td><td style='text-align: center;'>光通量</td><td style='text-align: center;'>lm</td><td style='text-align: center;'>lm</td><td style='text-align: center;'>压力能量</td><td style='text-align: center;'>(J·m·s²)/kg</td><td style='text-align: center;'>jms²/kg</td></tr><tr><td style='text-align: center;'>电感</td><td style='text-align: center;'>H</td><td style='text-align: center;'>h</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

## 參 考 文 献

[1] GB/T 28174.1—2011 统一建模语言(UML) 第1部分:基础结构

[2] GB/Z 34052.2—2017 统计数据与元数据交换(SDMX) 第2部分:信息模型 统一建模语言(UML)概念设计

[3] GB/T 22032—2021 系统与软件工程 系统生存周期过程

[4] GB/T 45630—2025 系统与软件工程架构描述

[5] ISO/IEC/IEEE 15288:2023 系统与软件工程 系统生存周期过程

[6] ISO/IEC/IEEE 42020:2019 Software, systems and enterprise—Architecture processes

[7] 鲁金直, 王国新, 张旸旸, 等. 基于模型的系统工程统一架构建模语言的标准体系构建 [J]. 信息技术与标准化, 2024, (Z1): 22-27+53.

[8] 陈立平, 周凡利, 丁建完, 等. 多领域物理统一建模语言 MODELICA 与 MWORKS 系统建模 [M]. 武汉: 华中科技大学出版社: 2019: 677.

[9] Lu J, Ma J, Zheng X, et al. Design ontology supporting model-based systems engineering for malisms[J]. IEEE Systems Journal, 2021, 16(4): 5465-5476.

[10] Lu J, Wang G, Ma J, et al. General modeling language to support model-based systems engineering formalisms (part 1) [C]. INCOSE International Symposium. Hoboken: Widly, 2020, 30(1): 323-338.

[11] Chen J, Wang G, Lu J, et al. Model-based system engineering supporting production scheduling based on satisfiability modulo theory [J]. Journal of Industrial Information Integration, 2022, 27: 100329.

[12] Kern H, Hummel A, Kühne S. Towards a comparative analysis of meta-metamodels[C]. Proceedings of the compilation of the co-located workshops on DSM'11, TMC'11, AGERE. New York: ACM, 2011: 7-12.