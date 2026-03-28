

# 中华人民共和国国家标准

GB/T 45256—2025

# 新闻出版 知识服务 知识本体构建流程

# Press and publication—Knowledge services—Construction process of knowledge ontology

2025-02-28 发布

2025-06-01 实施



## 目次

前言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
3.1 基础术语 …… 1    
3.2 专业术语 …… 2    
4 构建原则 …… 2    
5 构成要素 …… 3    
5.1 类 …… 3    
5.2 属性 …… 3    
6 创建流程 …… 4    
6.1 整体创建流程 …… 4    
6.2 资源准备阶段 …… 4    
6.3 本体构建阶段 …… 5    
6.4 知识标引阶段 …… 7    
7 构建工具功能要求 …… 7    
参考文献 …… 8



## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国新闻出版标准化技术委员会（SAC/TC 527）归口。

本文件起草单位：时代出版传媒股份有限公司、中国建筑出版传媒有限公司、国防工业出版社、北京中企智造科技有限公司、北京拓标卓越信息技术研究院、中国新闻出版研究院、人教数字出版有限公司、内蒙古出版集团有限责任公司、保定市魁信达数据处理有限公司、中国农业出版社有限公司、中国中医药出版社有限公司、河南教育电子音像出版社有限责任公司、研究出版社有限公司、《中国标准化》杂志社有限公司、北京时代华文书局有限公司、北方工业大学、英大传媒投资集团有限公司。

本文件主要起草人：卫敏、邢剑飞、张莉英、孙春晓、安秀敏、蔡志伟、马嵩、汪智、谢冰、刘颖丽、张希刚、周长岭、余敬春、裴飞、樊帆、尉晓玺、翟理、崔振华、李萨日娜、郑艳蓉、王磊、刘杰、翟永勇、刘雅菲、徐强。

20

## 新闻出版 知识服务

# 知识本体构建流程

## 1 范围

本文件确立了知识本体的构建原则，规定了构成要素、创建流程和构建工具的功能要求。

本文件适用于新闻出版领域知识库和知识资源库的建设与管理。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 18391.3—2009 信息技术 元数据注册系统（MDR） 第3部分：注册系统元模型与基本属性

GB/T 45257 新闻出版 知识服务 知识元提取与标引

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 基础术语

#### 3.1.1 

## 知识 knowledge

通过学习、实践或探索获得的认识、判断或技能。

[来源：GB/T 23703.2—2010，2.1]

#### 3.1.2 

## 概念 concept

由特征的唯一组合创建的知识。

注：概念不局限于特定范围，但它们受社会和文化环境的影响。

[来源：GB/T 15237.1—2000，3.2.1，有修改]

#### 3.1.3 

## 术语 term

在一个特定的主题领域中，一个一般概念词语的标识。

[来源：GB/T 15237.1—2000，3.4.3，有修改]

#### 3 \.1\.4

## 语义关系 semantic relation

概念之间、类之间符号及其含义的关系。

[来源：GB/T 4894—2024，3.1.7.1]

#### 3.1.5 

## 知识本体 knowledge ontology

知识概念与概念之间的规范化描述。

注：知识本体由类、属性、实例等要素构成。

[来源：GB/T 38377—2020，2.31，有修改]

#### 3.1.6 

## 知识元 knowledge element

在应用需求下，表达一个完整事物或概念的不必再分的独立的知识单位。

[来源：GB/T 38377—2019，2.3]

### 3.2 专业术语

#### 3.2.1 

## 类 class

一个对象集的描述。

注：该对象集具有公共的属性、操作、方法、关系和语义。

[来源：GB/T 18391.3—2009，3.1.4，有修改]

#### 3.2.2 

## 实例 instance

包含实际数据的数字对象。

#### 3.2.3 

## 属性 property

一个对象或实体的特征。

[来源：GB/T 18391.3—2009，3.1.3]

#### 3.2.4 

## 网络本体语言 web ontology language; OWL

用于表述相关事务、事务组和事务之间关系丰富而复杂的知识的一种语义 Web 语言。

[来源：GB/T 38371.1—2020，3.8，有修改]

#### 3.2.5 

## 知识库 knowledge base

针对特定需求，依据一定规则，采用特定的组织方式描述知识及其关系，并具有存储和应用等功能的数据库。

[来源：GB/T 38377—2019，4.2]

#### 3.2.6 

## 知识图谱 knowledge graph

揭示实体间关系并可进行形式化表示的一种语义的网络。

[来源：GB/T 38377—2019，4.3]

#### 3.2.7 

## 资源描述框架 resource description framework；RDF

由万维网联盟制定的一种用来表示 Web 资源的特性以及资源之间关系的表示规范。

[来源：GB/T 38371.1—2020，3.5]

#### 3.2.8 

## 资源描述框架模式 resource description framework schema; RDFS

由万维网联盟制定的基于资源描述框架的数据建模词汇集。

[来源：GB/T 38371.1—2020，3.6]

## 4 构建原则

知识本体构建的基本原则包括但不限于：

a）实用性，满足知识元提取、加工和应用等环节标准化的需求；

b）兼容性，采用国内外相关标准对象属性、元数据和术语等进行描述；

c）明确性，明确建设目标、层级设计、领域范围和应用场景，技术路线符合知识本体构建的一般方法，知识元描述符合资源描述框架模式（RDFS）的表达方式；

d）一致性，保持相同概念定义、描述语言、存储方式和值域约束一致，支持知识标引及知识推理等应用；

e）扩展性，通用知识本体构建充分考虑发展与服务需求变化，专业领域知识本体构建重点考虑核心概念的延展性，支持在现有概念基础上继续开发满足其他任务的新概念。

## 5 构成要素

### 5.1 类

类包括子类，子类下可衍生子类，并允许子类之间存在交集。按照 GB/T 18391.3 中相关元数据定义，依据网络本体语言/资源描述框架（OWL/RDF）对类定义描述方式，知识本体类定义见表 1。

<div style="text-align: center;">表 1 知识本体类定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>项中文名</td><td style='text-align: center;'>项英文名</td><td style='text-align: center;'>必选性</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>IRI</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>IRI是Internationalized Resource Identifier国际化资源标识符简称，类的唯一标识符，取值为符合IRI格式标准的字符串</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>类的唯一标记，取值一般用英文字母表示，首字母通常为大写</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>Label</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>可供人阅读的标识</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>Definition</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>给出类的概念和含义，取值一般为中文</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>注释</td><td style='text-align: center;'>Comment</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>给出类的使用说明</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>术语类型</td><td style='text-align: center;'>TypeOfTerms</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>表示类的类型</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>父类</td><td style='text-align: center;'>SubClassOf</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>被包含的类</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>子类</td><td style='text-align: center;'>HasSubclass</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>包含的子类</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>等价类</td><td style='text-align: center;'>EquivalentClass</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>列出该类的等价类</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>包含属性</td><td style='text-align: center;'>IncludesProperties</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>列出所含的属性名称，取值为属性名称的集合</td></tr></table>

### 5.2 属性

属性用以描述类所具有的特征，类和类之间、类和实例之间、实例和实例之间的关系。根据OWL/RDF对属性的定义方式，知识本体属性定义见表2。

<div style="text-align: center;">表 2 知识本体属性定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>项中文名</td><td style='text-align: center;'>项英文名</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>IRI</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>IRI 是 Internationalized Resource Identifier 国际化资源标识符简称，属性的唯一标识符，取值为符合 IRI 格式标准的字符串</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>name</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>属性的唯一标记，取值一般用英文字母表示，首字母通常为小写</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>label</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>可供人阅读的属性的标识</td></tr></table>

<div style="text-align: center;">表 2 知识本体属性定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>项中文名</td><td style='text-align: center;'>项英文名</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>definition</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>给出属性的概念和含义，取值一般为中文</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>注释</td><td style='text-align: center;'>comment</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>给出属性的使用说明</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>属性类型</td><td style='text-align: center;'>typeOfTerms</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>属性的类型分为对象属性和数值属性两类，取值分别为 owl:ObjectProperty 和 owl:DatatypeProperty</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>定义域</td><td style='text-align: center;'>domain</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>属性所在的类</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>range</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>属性的取值范围</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>父属性</td><td style='text-align: center;'>subPropertyOf</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>被包含的属性</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>子属性</td><td style='text-align: center;'>hasSubProperty</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>包含的子属性</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>逆属性</td><td style='text-align: center;'>inverseOf</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>属性作为对象属性时对应的逆属性名</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>等价属性</td><td style='text-align: center;'>equivalentProperty</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>与该属性等价的属性</td></tr></table>

## 6 创建流程

### 6.1 整体创建流程

知识本体创建的整体流程由资源准备、本体构建和知识标引3个阶段组成，如图1所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_119_811_1030_1299.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 1 知识本体创建整体流程</div>


### 6.2 资源准备阶段

#### 6.2.1 确定目标范围

建立知识本体前应首先确定知识本体覆盖的专业领域、范围和应用目标，以及知识本体作用及应用

对象。

#### 6.2.2 评估内容资源

建立知识本体前应对内容资源进行收集整理，分析内容资源的结构和使用价值，评估并确定内容资源的应用方式。

注：新闻出版领域的内容资源包括新闻出版领域的图书、期刊、研究报告、会议论文、标准、报纸文章和其他具有参考价值资料。

#### 6.2.3 内容资源数字化

在内容资源分析的基础上，对内容资源进行全文可扩展置标语言（XML）数字化加工，加工格式与要求应符合所建知识本体模型的要求。

#### 6.2.4 进入内容资源库

加工后的全文 XML 进入内容资源库。

### 6.3 本体构建阶段

#### 6.3.1 概念提取

##### 6.3.1.1 收集知识概念

全面收集知识本体领域范围内的概念，列举领域内的重要术语和概念，形成领域范围内的知识概念清单。宜尽量枚举概念，暂不考虑概念之间的重叠和关系以及概念是类还是属性等。

##### 6.3.1.2 筛选核心概念

对获取的大量而庞杂的概念进行筛选、评估、梳理和分类，筛选能精确表达领域知识的关键性概念，摒弃不必要或超出领域范围的概念，形成领域内的核心概念集。

##### 6.3.1.3 建立概念关系

###### 6.3.1.3.1 概念关系概述

抽取概念与概念间的关系是不可或缺的步骤。在同一知识本体中，概念间的关系决定知识本体的最终结构和质量。

###### 6.3.1.3.2 概念关系定义

概念关系包括但不限于：

a）层次关系：在概念之间建立层次，通常为一种“父子”关系；

b）非层次关系：概念之间的层次关系以外的类型关系。

###### 6.3.1.3.3 概念关系类型

概念关系的典型类型包括子类关系、成员关系、实例关系、相似关系、逆关系、时间顺序关系等。

##### 6.3.1.4 形成概念词汇表

形成概念词汇表是构建概念提取的结果，旨在为知识本体建模提供参考信息。针对领域内的核心术语和概念给出基本定义，包含词汇（概念）本身，以及词汇之间的关系（即定义在概念上的谓词）。

#### 6.3.2 本体建模

##### 6.3.2.1 定义类和层次

知识本体的概念通常用类表示，通过确定类的层次结构形成框架，用以描述领域概念。

类的定义与划分是将词汇表中的概念进行归纳、整理，抽象具有规范化定义的类，并对所建立的类层次进行检验，确保无重复概念，防止冗余定义。定义类和类的层次可采用以下方法：

a）自顶向下法：先定义领域中综合的、概括性的类，后对这些类进行细化；

b）自底向上法：先定义具体的类，再把这些具体类泛化成综合的类；

c）综合法：综合对以上两种方法进行类和层次的定义。

##### 6.3.2.2 定义类属性

通过上述步骤建立知识本体的整体框架，确定了知识本体的类以及类的层次关系。仅有类和类的层次关系不能提供知识本体模型所表达的知识信息，应在类和类的层次结构的框架基础上进一步描述这些类的内在结构，即类的属性。类的属性分为：

a）对象属性，用于描述类的个体实例之间的关系；

b）数值属性，用于描述类个体数值特征，不同属性取值类型不同，一般包括文本、数值、日期等。

##### 6.3.2.3 形式化表达

采用本体描述语言（XML、RDF/RDFS、OWL等）对知识本体建模进行规范表示。

##### 6.3.2.4 创建实例

实例是知识本体类的具体实现。创建实例的过程称为类的实例化。创建一个实例主要包括以下步骤：

a）选择一个类；

b）创建类的一个实例；

c）填充实例中各属性值。

##### 6.3.2.5 本体验证

知识本体构建是一个逐步完善和消歧的过程，应对知识本体构建的质量进行评价，包括衡量知识本体的正确性、一致性和可扩展性等。若不满足则应返回，重新调整相应的知识本体模型，直到构建出满足要求的知识本体模型。

#### 6.3.3 知识提取

##### 6.3.3.1 规范档加工

规范档用以实现规范控制，保证文档一致性和有效性，统一管理文档。规范档加工包括分类法、受控术语和知识元构建及属性的加工等。

##### 6.3.3.2 创建实例属性

实例是知识本体的具体化，创建一个实例包括创建实例基本属性和构建实例关系。创建实例基本属性即填充每个实例中的各个数值属性的值，数据属性的取值范围包括字符型、布尔型、数字型等。

##### 6.3.3.3 创建实例关系

实例是知识本体的具体化，创建一个实例包括创建实例基本属性和构建实例关系。创建实例关系即

填充每个实例中的各个对象属性的值，呈现相应的语义关系，对象属性的取值范围是定义的类。

##### 6.3.3.4 形成实例库

在知识本体框架构建完成时可添加实例。实例是知识本体类的具体实现，可继承类的属性。通过在实例中添加相应的属性值，呈现相应的语义关系，知识本体实例库是所有类的实例的集合。

##### 6.3.3.5 形成知识库

知识库由上述步骤形成的知识本体形式化表达、规范档加工和实例库组成。可用于知识的存储、组织和推理等。

### 6.4 知识标引阶段

#### 6.4.1 知识标引

基于知识本体的构建对内容资源进行知识化的标引。知识标引包括主题标引、扩展标引、关联标引和其他标引，按照 GB/T 45257 的相关规定。

#### 6.4.2 形成知识资源库

通过对内容资源进行知识标引，完成知识资源库的建设。

## 7 构建工具功能要求

知识本体构建工具是本体开发与构建的重要工具。本体构建工具应满足以下基本功能：

a）具有知识本体定义、导入和导出功能；

b）支持知识本体建模、存储和提取；

c）支持XML、RDF/RDFS、OWL语言转化和输出；

d）具备友好的操作界面；

e）具有多媒体资源导入和呈现功能；

f）具有自动或半自动构建功能。

## 参 考 文 献

[1] GB/T 4894—2024 信息与文献 基础和术语

[2] GB/T 15237.1—2000 术语工作 词汇 第1部分：理论与应用

[3] GB/T 23703.2—2010 知识管理 第2部分：术语

[4] GB/T 38371.1—2020 数字内容对象存储、复用与交换规范 第1部分：对象模型

[5] GB/T 38377—2019 新闻出版 知识服务 知识资源建设与服务基础术语

[6] Resource Description Framework[RDF]. https://www.w3.org/RDF/

[7] Web Ontology Language $$ OWL $$ . <https://www.w3.org/OWL/>

