

# 中华人民共和国国家标准

GB/T 38381—2019

# 新闻出版 知识服务 知识元描述

## Press and publication—Knowledge services—Description of knowledge element

2019-12-31 发布

2020-07-01 实施

国家市场监督管理总局发布

国家标准化管理委员会

## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 缩略语 …… 1  
  
5 描述规则 …… 2  
  
5.1 基本原则 …… 2  
  
5.2 知识元模型 …… 2  
  
5.3 知识元类型 …… 2  
  
5.4 知识元基本属性 …… 3  
  
6 扩展规则 …… 3  
  
6.1 扩展原则 …… 3  
  
6.2 扩展说明 …… 3  
  
6.3 扩展方法 …… 4  
  
附录 A（资料性附录） 典型知识元描述示例 …… 5  
  
参考文献 …… 20

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由国家新闻出版署提出。

本标准由全国新闻出版标准化技术委员会(SAC/TC 527)归口。

本标准起草单位：中国铁道出版社有限公司、法律出版社有限公司、人大数媒科技（北京）有限公司、中国新闻出版研究院、广东经济出版社有限公司、中国林业出版社有限公司、中国法制出版社有限公司、中国人民大学出版社有限公司、英大传媒投资集团有限公司、海洋出版社。

本标准主要起草人：魏立华、李军、张立、周洋、钟哲、谢冰、李鹏、何英、黄立敬、陶颖、江波、孙巍、吴培培、谢秋学、臧晓然、李思尧、张安超。

# 新闻出版 知识服务 知识元描述

## 1 范围

本标准规定了知识元的描述规则及其扩展规则。

本标准适用于新闻出版及相关领域开展知识服务工作。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 38376—2019 新闻出版 知识服务 主题分类词表编制

GB/T 38377—2019 新闻出版 知识服务 知识资源建设与服务基础术语

GB/T 38380—2019 新闻出版 知识服务 知识资源通用类型

## 3 术语和定义

GB/T 38377—2019 界定的以及下列术语和定义适用于本文件。

### 3.1 

## 知识 knowledge

通过学习、实践或探索所获得的认知、判断或技能。

[GB/T 23703.2—2010, 定义 2.1]

### 3.2 

## 知识元 knowledge element

在应用需求下，表达一个完整事物或概念的不必再分的独立的知识单位。

[GB/T 38377—2019, 定义 2.3]

### 3.3 

## 属性 attribute

一个对象或实体的特征。

[GB/T 18391.2—2009, 定义 3.1]

## 4 缩略语

下列缩略语适用于本文件。

DC: 都柏林核心元数据规范 (Dublin Core)

OWL: OWL 网络本体语言 (OWL Web Ontology Language)

RDF: 资源描述框架 (Resource Description Framework)

SKOS: 简单知识组织系统 (Simple Knowledge Organization System)

URI:统一资源识别符(Uniform Resource Identifier)

XML: 可扩展标记语言 (Extensible Markup Language)

XPath:XML 路径语言(XML Path Language)

## 5 描述规则

### 5.1 基本原则

知识元描述遵循以下基本原则：

a）独立性：独立于特定的专业领域、内容、载体、知识服务；

b）可用性：支持基于语义关联的知识发现、检索、浏览、分析、重用等应用需求；

c）可扩展性：支持对知识元类型及属性的细化和增加；

d）规范性：遵循 RDF/OWL 语法规范，采用 XML 语言进行描述。

### 5.2 知识元模型

知识元模型采用标识、名称、主题、类型、说明和来源等属性进行描述，示意参见图1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_284_607_889_738.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 1 知识元模型示意</div>


### 5.3 知识元类型

知识元类型包括事实型、数值型、概念型、原理型、技能型和规则型，遵循 GB/T 38380—2019 的相关规定。知识元类型的名称及标签见表 1。典型知识元描述示例参见附录 A。

<div style="text-align: center;">表 1 知识元类型名称及标签</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类型名称</td><td style='text-align: center;'>类型标签</td><td style='text-align: center;'>子类型名称</td><td style='text-align: center;'>子类型标签</td></tr><tr><td rowspan="6">事实型</td><td rowspan="6">Fact</td><td style='text-align: center;'>人物</td><td style='text-align: center;'>Person</td></tr><tr><td style='text-align: center;'>机构</td><td style='text-align: center;'>Organization</td></tr><tr><td style='text-align: center;'>事件</td><td style='text-align: center;'>Event</td></tr><tr><td style='text-align: center;'>时间</td><td style='text-align: center;'>Time</td></tr><tr><td style='text-align: center;'>地理</td><td style='text-align: center;'>Place</td></tr><tr><td style='text-align: center;'>记录</td><td style='text-align: center;'>Record</td></tr><tr><td rowspan="3">数值型</td><td rowspan="3">Number</td><td style='text-align: center;'>常数</td><td style='text-align: center;'>Constant</td></tr><tr><td style='text-align: center;'>观测数据</td><td style='text-align: center;'>ObservationData</td></tr><tr><td style='text-align: center;'>统计数据</td><td style='text-align: center;'>StatisticalData</td></tr><tr><td rowspan="5">概念型</td><td rowspan="5">Concept</td><td style='text-align: center;'>术语</td><td style='text-align: center;'>Terminology</td></tr><tr><td style='text-align: center;'>定律</td><td style='text-align: center;'>ConceptLaw</td></tr><tr><td style='text-align: center;'>定理</td><td style='text-align: center;'>Theorem</td></tr><tr><td style='text-align: center;'>计量单位</td><td style='text-align: center;'>Unit</td></tr><tr><td style='text-align: center;'>量纲</td><td style='text-align: center;'>Dimension</td></tr></table>

<div style="text-align: center;">表 1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类型名称</td><td style='text-align: center;'>类型标签</td><td style='text-align: center;'>子类型名称</td><td style='text-align: center;'>子类型标签</td></tr><tr><td rowspan="2">原理型</td><td rowspan="2">Principle</td><td style='text-align: center;'>学术理论</td><td style='text-align: center;'>Theory</td></tr><tr><td style='text-align: center;'>机理</td><td style='text-align: center;'>Mechanism</td></tr><tr><td rowspan="3">技能型</td><td rowspan="3">Skill</td><td style='text-align: center;'>策略</td><td style='text-align: center;'>Policy</td></tr><tr><td style='text-align: center;'>方法</td><td style='text-align: center;'>Method</td></tr><tr><td style='text-align: center;'>程序</td><td style='text-align: center;'>Procedure</td></tr><tr><td rowspan="3">规则型</td><td rowspan="3">Rule</td><td style='text-align: center;'>法律</td><td style='text-align: center;'>RuleLaw</td></tr><tr><td style='text-align: center;'>标准</td><td style='text-align: center;'>Standard</td></tr><tr><td style='text-align: center;'>制度</td><td style='text-align: center;'>Regulation</td></tr></table>

### 5.4 知识元基本属性

#### 5.4.1 标识

描述知识元的唯一代码。

#### 5.4.2 名称

能识别单个知识元的专属名词。当有多个名称时明确其相互关系。

#### 5.4.3 主题

能概括和抽象知识元内容的主要含义或与其他知识元的差异的关键字、关键短语等。

#### 5.4.4 类型

类型属性分为知识元类型和知识元子类型两个属性，其中知识元类型是必选项，知识元子类型是有则必选项。类型和子类型取值遵循 GB/T 38376—2019 的附录 B 的规定。

#### 5.4.5 说明

对知识元内容进行的完整概述。

#### 5.4.6 来源

包括知识元的出处、版权信息、提供者、所有者等子属性。

## 6 扩展规则

### 6.1 扩展原则

知识元的属性可根据应用需求进行扩展，包括新增属性和对已有的属性增加子属性。

### 6.2 扩展说明

属性的扩展说明见表2。

<div style="text-align: center;">表 2 属性扩展说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性类别</td><td style='text-align: center;'>属性名称</td><td style='text-align: center;'>扩展性</td><td style='text-align: center;'>扩展说明</td></tr><tr><td rowspan="6">基本属性</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>不可扩展</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>可扩展</td><td style='text-align: center;'>可增加非首选标签、隐藏标签等子属性</td></tr><tr><td style='text-align: center;'>主题</td><td style='text-align: center;'>可扩展</td><td style='text-align: center;'>可增加分类号等子属性</td></tr><tr><td style='text-align: center;'>类型</td><td style='text-align: center;'>可扩展</td><td style='text-align: center;'>可增加类型号等子属性</td></tr><tr><td style='text-align: center;'>说明</td><td style='text-align: center;'>可扩展</td><td style='text-align: center;'>可增加注释、评论等子属性</td></tr><tr><td style='text-align: center;'>来源</td><td style='text-align: center;'>可扩展</td><td style='text-align: center;'>可增加修编者、修编时间名称等子属性</td></tr><tr><td style='text-align: center;'>扩展属性</td><td style='text-align: center;'>—</td><td style='text-align: center;'>可扩展</td><td style='text-align: center;'>可增加新的属性</td></tr></table>

### 6.3 扩展方法

#### 6.3.1 添加新属性

已有知识元属性不能满足应用需求时，可通过添加新属性进行扩展。新增属性为独立属性，或已有属性的细化但范围等于或大于已有属性边界。示例参见附录 A。

#### 6.3.2 添加子属性

已有知识元属性的定义域不能满足应用需求时，可通过添加子属性进行扩展。子属性的定义域可与父属性的定义域相同，也可根据应用需求进行调整。示例参见附录 A。

# 附录 A

# （资料性附录）

# 典型知识元描述示例

### A.1 描述约定

#### A.1.1 目标命名空间声明

指定明确的 URI 及前缀名称来指代相应的命名空间，可根据需求自定义命名空间。引用的命名空间清单见 A.2。

#### A.1.2 命名规则

定义知识元的名称时，每个英文单词的首字母大写，其余字母均小写，不使用任何连字符。在名称中不使用下划线“_”、下圆点“.”和连字符“-”。

单词均完整使用，名称不使用缩略语，以保证语义的清晰，提高可读性。因特殊原因需要在名称使用缩略语的，提供对应的全称和相应的说明。

#### A.1.3 XML 描述

XML 描述的元素在不同位置出现如有不同的语义，一般采用不同的元素全称；出现元素名称时用尖括号“<）”括起作为提示，便于同其他类型的名词出现相区别。

元素标记的声明不以该元素的相关父元素或祖元素的路径表达作为前缀，当相同语义的元素名在对应 XML 片段的描述中出现不止一次，且需要使用语境描述才能区别时，则采用 XPath 的规范表述方法，以明示其出现的具体位置。

#### A.1.4 XML 组件命名

与元素、属性、简单类型和复杂类型概念相关的命名基于如下约定。

对 XML 组件进行命名时，若命名的名称多于一个英文单词，则除第一个单词外，其后每个单词的首字母均大写。第一个单词首字母是否大写根据以下原则确定：

a） 组件元素的命名: 第一个单词的首字母大写;

b）组件属性的命名：第一个单词的首字母小写；

c) 复杂类型的命名: 第一个单词的首字母大写, 类型名后添加后缀 Type;

d）简单类型的命名：第一个单词的首字母小写，类型名后添加后缀 Type。

### A.2 命名空间

表 A.1 描述了所用到的命名空间和前缀。示例中采用 gkadm(General Knowledge Application Data Model) 知识应用数据模型作为自定义的命名空间。

知识元数据引用命名空间列表见表 A.1。

<div style="text-align: center;">表 A.1 知识元数据引用命名空间列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>前缀</td><td style='text-align: center;'>命名空间 URI</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>dc</td><td style='text-align: center;'>http://purl.org/dc/elements/1.1/</td><td style='text-align: center;'>都柏林核心元素</td></tr><tr><td style='text-align: center;'>dcterms</td><td style='text-align: center;'>http://purl.org/dc/terms/</td><td style='text-align: center;'>都柏林核心术语</td></tr><tr><td style='text-align: center;'>frbroo</td><td style='text-align: center;'>http://iflastandards.info/ns/fr/frbr/frbroo/</td><td style='text-align: center;'>书目记录的功能需求(FRBR)面向对象的释义</td></tr><tr><td style='text-align: center;'>frbr_core</td><td style='text-align: center;'>http://purl.org/vocab/frbr/core#</td><td style='text-align: center;'>书目记录的功能需求(FRBR)RDF 描述</td></tr><tr><td style='text-align: center;'>foaf</td><td style='text-align: center;'>http://xmlns.com/foaf/0.1/</td><td style='text-align: center;'>FOAF(Friend of a friend)词汇术语</td></tr><tr><td style='text-align: center;'>ore</td><td style='text-align: center;'>http://www.openarchives.org/ore/terms/</td><td style='text-align: center;'>ORE 词汇术语</td></tr><tr><td style='text-align: center;'>owl</td><td style='text-align: center;'>http://www.w3.org/2002/07/owl#</td><td style='text-align: center;'>OWL 词汇术语</td></tr><tr><td style='text-align: center;'>rdf</td><td style='text-align: center;'>http://www.w3.org/1999/02/22-rdf-syntax-ns#</td><td style='text-align: center;'>RDF 词汇术语</td></tr><tr><td style='text-align: center;'>rdfs</td><td style='text-align: center;'>http://www.w3.org/2000/01/rdf-schema#</td><td style='text-align: center;'>RDFS 词汇术语</td></tr><tr><td style='text-align: center;'>skos</td><td style='text-align: center;'>http://www.w3.org/2004/02/skos/core#</td><td style='text-align: center;'>SKOS 词汇术语</td></tr><tr><td style='text-align: center;'>wgs84_pos</td><td style='text-align: center;'>http://www.w3.org/2003/01/geo/wgs84_pos#</td><td style='text-align: center;'>WorldGeodeticSystem1984, 是为 GPS 全球定位系统使用而建立的坐标系统</td></tr></table>

### A.3 知识元属性中的数据结构

#### A.3.1 约束性说明

根据知识元的内容构成以及应用要求确定属性的约束性，分为必选、有则必选和可选。约束性可进行自定义，但在同一内容构成和应用条件下应保持稳定。

#### A.3.2 来源

名称：来源。

标签: gkadm:SourceMetaType.

定义：描述知识元的出处、版权信息，提供者、代理等信息。

注释：知识元的通用属性，可选项。

来源的属性说明见表 A.2。

<div style="text-align: center;">表 A.2 来源属性说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>dc:source</td><td style='text-align: center;'>出处</td><td style='text-align: center;'>知识元的溯源</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>dc:rights</td><td style='text-align: center;'>版权信息</td><td style='text-align: center;'>知识元的知识产权信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>dc:creator</td><td style='text-align: center;'>提供者</td><td style='text-align: center;'>知识元的提供者</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>dcterms:provenance</td><td style='text-align: center;'>所有者</td><td style='text-align: center;'>知识元的版权所有者</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr></table>

#### A.3.3 管理元数据

名称:管理元数据。

标签: gkadm: MgntMetaType.

定义:一个知识元的管理元数据。

注释：知识元的通用属性，可选项。

应使用 XML 对象对其进行描述。可根据应用的需求，自行定义其属性及属性值。例如，可以存放系统名称、系统路径等信息。

### A.4 概念知识元 (Concept)

名称：概念知识元。

标签: skos:Concept.

定义：对特定领域的概念进行定义和组织，并表达和显示概念间的语义关系。

注释：概念类知识元参考 skos:Concept 定义，提供了对叙词表、分类法、术语等受控词表的知识管理及语义处理方案。

属性：dc:identifier（标识）、rdfs:label（名称）、skos:altLabel（非首选标签）、skos:hiddenLabel（隐藏标签）、gkadm:ketype（知识元类型）、gkadm:kesubtype（知识元子类型）、skos:broader（上位关系）、skos:narrower（下位关系）、skos:related（相关关系）、skos:note（说明）、skos:notation（概念标记）、skos:inScheme（概念体系）、dc:subject（主题）、gkadm:sourceMeta（来源）、gkadm:mgntMeta（管理元数据）。

概念知识元的属性如图 A.1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_396_719_801_1471.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">图 A.1 概念知识元属性</div>


概念知识元属性的说明见表 A.3。

<div style="text-align: center;">表 A.3 概念知识元属性说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>dc;identifier</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>知识元的标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>rdfs;label</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>能识别单个知识元的专属名词</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>skos;altLabel</td><td style='text-align: center;'>非首选标签</td><td style='text-align: center;'>知识元的别名</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>skos;hiddenLabel</td><td style='text-align: center;'>隐藏标签</td><td style='text-align: center;'>隐藏标签在用户通过文本搜索功能与知识组织系统交互时非常有用。例如用户寻找一个相关概念时输入了拼错的词语，如果拼错的查询与隐藏标签匹配，用户仍然能够找到相关概念，但隐藏标签对与用户而言是不可见的</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>gkadm;ketype</td><td style='text-align: center;'>知识元类型</td><td style='text-align: center;'>知识元的类型标签</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>gkadm;kesubtype</td><td style='text-align: center;'>知识元子类型</td><td style='text-align: center;'>知识元的子类型标签</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>skos;broader</td><td style='text-align: center;'>上位关系</td><td style='text-align: center;'>两个概念知识元之间的等级连接，表示其中一个概念知识元比另一个概念知识元在某方面更概括（“宽泛”）</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf 资源</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>skos;narrower</td><td style='text-align: center;'>下位关系</td><td style='text-align: center;'>两个概念知识元之间的等级连接，表示其中一个概念知识元比另一个概念知识元“狭窄”</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf 资源</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>skos;related</td><td style='text-align: center;'>相关关系</td><td style='text-align: center;'>两个概念知识元之间的相关连接，表示两个概念内在“有关”但是其中任何一个概念知识元不以任何方式比另一个概念知识元更概括</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf 资源</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>skos;note</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>对知识元的内容进行的完整概述</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>skos;notation</td><td style='text-align: center;'>概念标记</td><td style='text-align: center;'>用于在给定的概念体系范围中唯一标识一个概念。如分类体系的分类号</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>skos;inScheme</td><td style='text-align: center;'>概念体系</td><td style='text-align: center;'>概念体系可以视为一个或多个概念的集合体。概念体系是当前词汇所在的概念体系</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>dc;subject</td><td style='text-align: center;'>主题</td><td style='text-align: center;'>能概括和抽象知识元内容的主要含义或与其他知识元的差异的关键字、关键短语等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>gkadm;sourceMeta</td><td style='text-align: center;'>来源</td><td style='text-align: center;'>描述知识元的出处、版权信息，提供者、所有者等信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>gkadm;SourceMeta-Type</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>gkadm;mgntMeta</td><td style='text-align: center;'>管理元数据</td><td style='text-align: center;'>一个概念知识元的管理元数据</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>gkadm;MgntMetaType</td></tr></table>

### A.5 事件知识元(Event)

名称：事件知识元。

标签:Event。

定义:用于描述有重要影响事件的名称、时间、地点、人物等属性的知识,如社会事件、历史事件、地理事件等。

注释：参考 FRBR(Functional Requirements for Bibliographic Records) 中规范事件(event)定义。

属性:dc:identifier(标识)、rdfs:label(名称)、skos:altLabel(非首选标签)、skos:hiddenLabel(隐藏标签)、gkadm:ketype(知识元类型)、gkadm:kesubtype(知识元子类型)、skos:note(说明)、skos:notation(主题术语的分类号)、gkadm:occurredAt(发生时间)、gkadm:happenedAt(发生地点)、dc:subject(主题)、gkadm:sourceMeta(来源)、gkadm:mgntMeta(管理元数据)。

事件知识元的属性见图 A.2。

<div style="text-align: center;"><img src="imgs/img_in_image_box_409_488_793_1148.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_116_1206_152_1243.jpg" alt="Image" width="3%" /></div>


<div style="text-align: center;">图 A.2 事件知识元属性</div>


事件知识元的属性说明见表 A.4。

<div style="text-align: center;">表 A.4 事件知识元属性说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>dc:identifier</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>知识元的标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>rdfs:label</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>能识别单个知识元的专属名词</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>skos:altLabel</td><td style='text-align: center;'>非首选标签</td><td style='text-align: center;'>知识元的别名</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>skos:hiddenLabel</td><td style='text-align: center;'>隐藏标签</td><td style='text-align: center;'>知识元的隐藏标签</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr></table>

<div style="text-align: center;">表 A.4 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>gkadm:ketype</td><td style='text-align: center;'>知识元类型</td><td style='text-align: center;'>知识元的类型标签</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>gkadm:kesubtype</td><td style='text-align: center;'>知识元子类型</td><td style='text-align: center;'>知识元的子类型标签</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>skos:note</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>对知识元的内容进行的完整概述</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>skos:notation</td><td style='text-align: center;'>主题术语的分类号</td><td style='text-align: center;'>事件主题术语的分类号</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>gkadm:occurredAt</td><td style='text-align: center;'>发生时间</td><td style='text-align: center;'>事件的发生时间</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>DateTime</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>gkadm:happenedAt</td><td style='text-align: center;'>发生地点</td><td style='text-align: center;'>事件的发生地</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>Place</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>dc:subject</td><td style='text-align: center;'>主题</td><td style='text-align: center;'>能概括和抽象知识元内容的主要含义或与其他知识元的差异的关键字、关键短语等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>gkadm:sourceMeta</td><td style='text-align: center;'>来源</td><td style='text-align: center;'>描述知识元的出处、版权信息，提供者、所有者等信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>gkadm: SourceMeta-Type</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>gkadm:mgntMeta</td><td style='text-align: center;'>管理元数据</td><td style='text-align: center;'>一个知识元的管理元数据</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>gkadm:MgntMetaType</td></tr></table>

### A.6 人物知识元(Person)

名称：人物知识元。

标签:Person。

定义: 人类社会的自然人成员。在知识体系中的人物, 包括名称、属性及相互之间关系。

注释：参考 FOAF(Friend of a friend) 中人物(foaf:Person)的定义。

属性:dc:identifier(标识)、rdfs:label(名称)、skos:altLabel(非首选标签)、skos:hiddenLabel(隐藏标签)、gkadm:ketype(知识元类型)、gkadm:kesubtype(知识元子类型)、skos:note(说明)、foaf:name(名称)、dc:date(日期)、dcterms:hasPart(由……组成)、dcterms:isPartOf(是……成员/部分)、gkadm:isRelatedTo(相关资源)、gkadm:hasMet(出现)、owl:sameAs(与……相同)、gkadm:acronym(缩略词名称)、foaf:homepage(主页)、dc:subject(主题)、gkadm:sourceMeta(来源)、gkadm:mgntMeta(管理元数据)、gkadm:biographicalInformation(人物简历)、gkadm:professionOrOccupation(职业)、gkadm:dateOfBirth(出生日期)、gkadm:dateOfDeath(死亡日期)、gkadm:gender(性别)、gkadm:placeOfBirth(出生地点)、gkadm:placeOfDeath(死亡地点)。

人物知识元属性如图 A.3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_390_201_807_1216.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">图 A.3 人物知识元属性</div>


人物知识元基本属性的基本属性说明见表 A.5。

<div style="text-align: center;">表 A.5 人物知识元基本属性说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>gkadm: biographicalInformation</td><td style='text-align: center;'>人物简历</td><td style='text-align: center;'>人物简历</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>gkadm: professionOrOccupation</td><td style='text-align: center;'>职业</td><td style='text-align: center;'>人物职业</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>gkadm: dateOfBirth</td><td style='text-align: center;'>出生日期</td><td style='text-align: center;'>出生日期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>Date</td></tr></table>

<div style="text-align: center;">表 A.5 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>gkadm:dateOfDeath</td><td style='text-align: center;'>死亡日期</td><td style='text-align: center;'>死亡日期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>Date</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>gkadm:gender</td><td style='text-align: center;'>性别</td><td style='text-align: center;'>性别</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>gkadm:placeOfBirth</td><td style='text-align: center;'>出生地点</td><td style='text-align: center;'>出生地</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>gkadm:placeOfDeath</td><td style='text-align: center;'>死亡地点</td><td style='text-align: center;'>死亡地点</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr></table>

### A.7 机构知识元(Organization)

名称：机构知识元。

标签: Organization。

定义：依法设立的机关、事业、企业、社团及其他依法成立的单位。

注释：参考 FOAF 中机构(foaf:Organization)的定义。机构是相对固定的社会组织机构，如行业协会、政府部门、企业等。

属性:dc:identifier(标识)、rdfs:label(名称)、skos:altLabel(非首选标签)、skos:hiddenLabel(隐藏标签)、gkadm:ketype(知识元类型)、gkadm:kesubtype(知识元子类型)、skos:note(说明)、foaf:name(名称)、dc:date(日期)、dcterms:hasPart(由……组成)、dcterms:isPartOf(是……成员/部分)、gkadm:isRelatedTo(相关资源)、gkadm:hasMet(出现)、owl:sameAs(与……相同)、gkadm:acronym(缩略词名称)、foaf:homepage(主页)、dc:subject(主题)、gkadm:sourceMeta(来源)、gkadm:mgntMeta(管理元数据)、gkadm:biographicalInformation(机构简介)、gkadm:dateOfEstablishment(成立日期)、gkadm:dateOfTermination(终止日期)、gkadm:placeOfBirth[成立(注册)地点]、gkadm:professionOrOccupation(相关行业)、gkadm:organizationScope(机构范围)、gkadm:organizationDomain(机构领域)、gkadm:organizationSector(机构性质)、gkadm:geographicLevel(机构地域范围)、gkadm:country(机构所属国家)。

机构知识元属性如图 A.4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_387_203_816_1229.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图 A.4 机构知识元属性</div>


机构知识元基本属性的说明见表 A.6。

<div style="text-align: center;">表 A.6 机构知识元基本属性说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>gkadm:biographicalInformation</td><td style='text-align: center;'>机构简介</td><td style='text-align: center;'>机构简介</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>gkadm:dateOfEstablishment</td><td style='text-align: center;'>成立日期</td><td style='text-align: center;'>机构成立日期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>Date</td></tr></table>

<div style="text-align: center;">表 A.6（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>gkadm:dateOfTermination</td><td style='text-align: center;'>终止日期</td><td style='text-align: center;'>机构终止日期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>Date</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>gkadm:placeOfBirth</td><td style='text-align: center;'>成立（注册）地点</td><td style='text-align: center;'>与机构相关的地点信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>gkadm:professionOrOccupation</td><td style='text-align: center;'>相关行业</td><td style='text-align: center;'>机构的相关行业</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>gkadm:organizationScope</td><td style='text-align: center;'>机构范围</td><td style='text-align: center;'>机构的业务范围，如 Cross/Single/Thematic/Individual 等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>gkadm:organizationDomain</td><td style='text-align: center;'>机构领域</td><td style='text-align: center;'>机构领域，如 Library/Archive/Museum 等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>gkadm:organizationSector</td><td style='text-align: center;'>机构性质</td><td style='text-align: center;'>机构实体性质，如 Private/Public/GovernmentDepartment 等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>gkadm:geographicLevel</td><td style='text-align: center;'>机构地域范围</td><td style='text-align: center;'>机构地域影响力范围，如 Regional/National/Worldwide 等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>gkadm:country</td><td style='text-align: center;'>机构所属国家</td><td style='text-align: center;'>国家地区名称</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr></table>

### A.8 地理知识元(Place)

名称：地理知识元。

标签: Place。

定义：用于描述人物、机构、事件所在的地理位置，以及随时间变化的地理位置名称的知识元。

注释：一个地理位置可以由多个标签标识。选择这些标签中的一个作为名称，以便始终如一地命名与参照该地点。其他的标签可以作为地点的变异术语看待。

属性：dc:identifier（标识）、rdfs:label（名称）、skos:altLabel（非首选标签）、skos:hiddenLabel（隐藏标签）、gkadm:ketype（知识元类型）、gkadm:kesubtype（知识元子类型）、skos:note（说明）、wgs84_pos:lat（维度）、wgs84_pos:long（经度）、wgs84_pos:alt（海拔高度）、dcterms:hasPart（由……组成）、dcterms:isPartOf（是……成员/部分）、owl:sameAs（与……相同）、dc:subject（主题）、gkadm:sourceMeta（来源）、gkadm:mgntMeta（管理元数据）。

地理知识元的属性如图 A.5 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_423_203_780_958.jpg" alt="Image" width="29%" /></div>


<div style="text-align: center;">图 A.5 地理知识元属性</div>


地理知识元的属性说明见表 A.7。

<div style="text-align: center;">表 A.7 地理知识元属性说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>dc;identifier</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>知识元的标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>rdfs;label</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>能识别单个知识元的专属名词</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>skos;altLabel</td><td style='text-align: center;'>非首选标签</td><td style='text-align: center;'>知识元的别名</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>skos;hiddenLabel</td><td style='text-align: center;'>隐藏标签</td><td style='text-align: center;'>知识元的隐藏标签</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>gkadm;ketype</td><td style='text-align: center;'>知识元类型</td><td style='text-align: center;'>知识元的类型标签</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>gkadm;kesubtype</td><td style='text-align: center;'>知识元子类型</td><td style='text-align: center;'>知识元的子类型标签</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>skos;note</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>对知识元的内容进行的完整概述</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>wgs84_pos;lat</td><td style='text-align: center;'>纬度</td><td style='text-align: center;'>一个地点的 GPS 坐标系纬度值</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>float 单精度</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>wgs84_pos;long</td><td style='text-align: center;'>经度</td><td style='text-align: center;'>一个地点的 GPS 坐标系经度值</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>float 单精度</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>wgs84_pos;alt</td><td style='text-align: center;'>海拔高度</td><td style='text-align: center;'>一个地点的 GPS 坐标系海拔高度值</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>float 单精度</td></tr></table>

<div style="text-align: center;">表 A.7 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>dcterms:hasPart</td><td style='text-align: center;'>由……组成</td><td style='text-align: center;'>一个知识元与另一知识元间有构成关系</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf资源</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>dcterms:isPartOf</td><td style='text-align: center;'>是……成员/部分</td><td style='text-align: center;'>一个知识元是另一个知识元的一部分</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf资源</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>owl:sameAs</td><td style='text-align: center;'>与……相同</td><td style='text-align: center;'>与另一个知识元相同</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf资源</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>dc:subject</td><td style='text-align: center;'>主题</td><td style='text-align: center;'>能概括和抽象知识元内容的主要含义或与其他知识元的差异的关键字、关键短语等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>gkadm:sourceMeta</td><td style='text-align: center;'>来源</td><td style='text-align: center;'>描述知识元的出处、版权信息，提供者、所有者等信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>gkadm:SourceMeta-Type</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>gkadm:mgntMeta</td><td style='text-align: center;'>管理元数据</td><td style='text-align: center;'>知识元的管理元数据</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>gkadm:MgntMetaType</td></tr></table>

### A.9 典型知识元 XML 描述示例

以下示例依据本系列标准的内容，以铁道工程专业术语为例，构建知识元的 XML 示例片段。

示例 1: 本示例是对属性进行扩展的样例。添加一个新属性“索引(index)”，采用出版机构的命名空间(“http://book.crphdm.com/”)。定义该新属性的示例代码(RDF/XML)如下：

<ObjectProperty rdf:about="http://book.crphdm.com/Property/23">
    <rdfs:label xml:lang="en">index</rdfs:label>
    <rdfs:label xml:lang="zh">索引</rdfs:label>
    <owl:versionInfo>1.0</owl:versionInfo>
    <skos:note xml:lang="zh">在 GB/T 50262—2013《铁路工程基本术语标准》中的索引号</skos:note>
    <rdfs:isDefinedBy rdf 资源="http://book.crphdm.com/"/>
</owl:versionInfo>

</owl:ObjectProperty>

示例 2: 本示例是对类型进行扩展的样例。对 rdfs:Concept 类型添加一个子类型 RailwayTerm，出版机构的命名空间为 http://book.crphdm.com/，其作为必选项的限制性定语（索引）应当使用属性扩展的方式进行定义。其 RDF/XML 定义的示例代码如下：

<owl:Class rdf:about="http://book.crphdm.com/class/1">
    <rdfs:subClassOf rdf 资源="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:label xml:lang="en">RailwayTerm</rdfs:label>
    <rdfs:label xml:lang="zh">铁路工程专业术语</rdfs:label>
    <skos:note xml:lang="zh">铁路工程专业术语</skos:note>
    <rdfs:isDefinedBy rdf 资源="http://book.crphdm.com"/>
</owl:Class>

示例 3: 本示例以铁路工程基本术语中的 2 个术语和与铁路工程相关的 3 个概念为例, 构建完整的知识元数据示例, 阐释知识元的定义方法、属性的扩展方法、知识元的关联关系、知识元关联关系的扩展。

根据 3.2 的定义，确认“铁路信号”“视觉信号”“听觉信号”“夜间信号”和“信号机”作为知识元，同时“铁路信号”和“信号机”作为铁路工程基本术语，在 GB/T 50262—2013《铁路工程基本术语标准》中存在索引号，其应作为必选项，放入“概念(Concept)”的扩展类型“铁路工程基本术语(Railway Term)”中，同时构建新的属性“索引号(Index)”。此外，根据新闻出版机构的应用需要，对于铁路工程相关的概念和术语，增加知识元的权重属性作为可选项。

另外，知识元间关联关系中，将对“等级关系”和“相关关系”进行扩展，分别为“包含”和“显示”，以细化知识元之间的

关系。

本示例中，使用自定义命名空间 gkadm 和出版机构自定义的命名空间 tdpress。

具体示例如下：

<?xml version="1.0" encoding="UTF-8"?>

<?xml-model href="GKADM-INTERNAL.xsd" type="application/xml" schematypens="http://purl.oclc.org/dsd1/schematron"?>
<rdf:RDFxmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:gkadm="http://xxx.com/gkadm/schema/cores/"
        xmlns:foaf="http://xmlns.com/foaf/0.1/" xmlns:ore="http://www.openarchives.org/ore/terms/"
        xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema #"
        xmlns:owl="http://www.w3.org/2002/07/owl #" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns #"
        xmlns:wgs84="http://www.w3.org/2003/01/geo/wgs84_pos #" xmlns:skos="http://www.w3.org/2004/02/skos/core #"
        xmlns:tdpress="http://book.crphdm.com">

    <owl:ObjectPropertyrdf:about="http://book.crphdm.com/Property/23">
        <rdf:label xml:lang="en">weight</rdf:label>
        <rdf:label xml:lang="zh">权重</rdf:label>
        <owl:versionInfo>1.0</owl:versionInfo>
        <skos:note xml:lang="zh">每个词在知识体系中所占的权重</skos:note>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://book.crphdm.com/Property/23">
        <rdf:label xml:lang="en">index</rdf:label>
        <rdf:label xml:lang="zh">索引</rdf:label>
        <owl:versionInfo>1.0</owl:versionInfo>
        <skos:note xml:lang="zh">在 GB/T 50262—2013《铁路工程基本术语标准》中的索引号</skos:note>
    </owl:ObjectProperty>

    <owl:Classrdf:about="http://book.crphdm.com/class */">
        <rdf:subClassOfrdf资源="http://www.w3.org/2004/02/skos/core#Concepts" />
        <rdf:label xml:lang="en">RailwayTerm</rdf:label>
        <rdf:label xml:lang="zh">铁路工程专业术语</rdf:label>
        <skos:note xml:lang="zh">铁路工程专业术语</skos:note>
    </owl:Class>

    <tdpress:RailwayTerm rdf:about="http://book.crphdm.com/concept/135">
        <dc:identifier>http://book.crphdm.com/concept/135</dc:identifier>
        <gkadm:ketype>Concept</gkadm:ketype>
        <gkadm:kesubtype>RailwayTerm</gkadm:kesubtype>
        <rdf:label>铁路信号</rdf:label>
        <skos:altLabel>信号</skos:altLabel>
        <tdpress:weight>92.3</tdpress:weight>
        <tdpress:index>14.1.1</tdpress:index>
        <skos:note>
            铁路运输系统中，为保证行车安全、提高区间和车站通过能力及编解能力而设置的手动控制、自动控制及遥控、遥信技术的总称。信号是对行车或调车人员发出指示运行条件的命令，它通过音响、颜色、形状、位置、灯光等来表示。
        </skos:note>
    </tdpress:weight>
</rdf:RDF>

</td>

铁路信号包括视觉信号和听觉信号两大类。用信号机、信号旗、信号灯、信号牌、信号表示器、信号标志及火炬等显示的信号均属视觉信号，列控车载设备的速度显示亦属视觉信号。

</skos:note>

<skos:notation>铁路工程基本术语.信号</skos:notation>

<skos:inScheme>铁路</skos:inScheme>

</rdfs:Concept>

<tdpress:RailwayTerm rdf:about="http://book.crphdm.com/concept/139">

<dc:identifier>http://book.crphdm.com/concept/139</dc:identifier>

<rdfs:label>信号机</rdfs:label>

<tdpress:weight>43.5</tdpress:weight>

<tdpress:index>14.2.21</tdpress:index>

<gkadm:ketype>Concept</gkadm:ketype>

<gkadm:kesubtype>RailwayTerm</gkadm:kesubtype>

<skos:note></skos:note>

<skos:notation>铁路工程基本术语.信号</skos:notation>

<skos:inScheme>铁路</skos:inScheme>

</tdpress:RailwayTerm>

<rdfs:Conceptrdf:about="http://book.crphdm.com/concept/137">

<dc:identifier>http://book.crphdm.com/concept/137</dc:identifier>

<rdfs:label>听觉信号</rdfs:label>

<gkadm:ketype>Concept</gkadm:ketype>

<tdpress:weight>58.8</tdpress:weight>

<skos:note>用号角、口笛、机车、动车组及自轮运转特种设备的鸣笛等发出的信号均属听觉信号</skos:note>

<skos:notation>铁路工程基本术语.信号</skos:notation>

<skos:inScheme>铁路</skos:inScheme>

</rdfs:Concept>

<rdfs:Conceptrdf:about="http://book.crphdm.com/concept/141">

<dc:identifier>http://book.crphdm.com/concept/141</dc:identifier>

<rdfs:label>夜间信号</rdfs:label>

<gkadm:ketype>Concept</gkadm:ketype>

<tdpress:weight>92.3</tdpress:weight>

<skos:note></skos:note>

<skos:notation>铁路工程基本术语.信号</skos:notation>

<skos:inScheme>铁路</skos:inScheme>

</rdfs:Concept>

<gkadm:RelationshipTyperdf:about="http://book.crphdm.com/relationtype/25">

<rdfs:subRelationshipOf rdfs:label="等级关系" rdf资源="http://book.crphdm.com/relationtype/01" />

<rdfs:labelxml:lang="zh">包含</rdfs:label>

<rdfs:isDefinedByrdf资源="http://book.crphdm.com/"/>

</gkadm:RelationshipType>

<gkadm:RelationshipTyperdf:about="http://book.crphdm.com/relationtype/26">
    <rdfs:subRelationshipOf rdfs:label="相关关系" rdf资源="http://book.crphdm.com/relationtype/02" />
    <rdfs:label xml:lang="zh">显示</rdfs:label>
    <rdfs:isDefinedBy rdf资源="http://book.crphdm.com/"/>
</gkadm:RelationshipType>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/131">
    <dc:identifier>http://book.crphdm.com/relation/131</dc:identifier>
    <gkadm:RelationshipType rdf资源="http://book.crphdm.com/relationtype/25" />
    <rdfs:labelxml:lang="zh">包含</rdfs:label>
    <gkadm:source rdf资源="http://book.crphdm.com/concept/135" />
    <gkadm:destination rdf资源="http://book.crphdm.com/concept/136" />
    <gkadm:distance>20</gkadm:distance>
    <rdfs:isDefinedBy rdf资源="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/132">
    <dc:identifier>http://book.crphdm.com/relation/132</dc:identifier>
    <gkadm:RelationshipType rdf资源="http://book.crphdm.com/relationtype/25" />
    <rdfs:label xml:lang="zh">包含</rdfs:label>
    <gkadm:source rdf资源="http://book.crphdm.com/concept/135" />
    <gkadm:destination rdf资源="http://book.crphdm.com/concept/137" />
    <gkadm:distance>50</gkadm:distance>
    <rdfs:isDefinedBy rdf资源="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/133">
    <dc:identifier>http://book.crphdm.com/relation/133</dc:identifier>
    <gkadm:RelationshipType rdf资源="http://book.crphdm.com/relationtype/26" />
    <rdfs:label xml:lang="zh">显示</rdfs:label>
    <gkadm:source rdf资源="http://book.crphdm.com/concept/139" />
    <gkadm:destination rdf资源="http://book.crphdm.com/concept/136" />
    <gkadm:distance>75</gkadm:distance>
    <rdfs:isDefinedBy rdf资源="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/134">
    <dc:identifier>http://book.crphdm.com/relation/134</dc:identifier>
    <gkadm:RelationshipType rdf资源="http://book.crphdm.com/relationtype/25" />
    <rdfs:label xml:lang="zh">包含</rdfs:label>
    <gkadm:source rdf资源="http://book.crphdm.com/concept/135" />
    <gkadm:destination rdf资源="http://book.crphdm.com/concept/141" />
    <gkadm:distance>99</gkadm:distance>
    <rdfs:isDefinedBy rdf资源="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

</gkadm:RelationshipType>

## 参考文献

[1] GB/T 4754—2017 国民经济行业分类

[2] GB/T 4880.2—2000 语种名称代码 第2部分：3字母代码

[3] GB/T 4880.3—2009 语种名称代码 第3部分：所有语种的3字母代码

[4] GB/T 7408—2005 数据元和交换格式 信息交换 日期和时间表示法

[5] GB/T 13190.1—2015 信息与文献 叙词表及与其他词表的互操作 第1部分:用于信息检索的叙词表

[6] GB/T 18391.2—2009 信息技术 元数据注册系统(MDR) 第2部分:分类

[7] GB/T 18793—2002 信息技术 可扩展置标语言(XML)1.0

[8] GB/T 23703.1—2009 知识管理 第1部分：框架

[9] GB/T 23703.2—2010 知识管理 第2部分：术语

[10] GB/T 23703.7—2014 知识管理 第 7 部分: 知识分类通用要求

[11] GB/T 25100 信息与文献 都柏林核心元数据元素集

[12] GB/T 50262—2013 铁路工程基本术语标准

[13] CY/T 90.1～90.5—2013 出版元数据

[14] 图书馆·情报与文献学名词审定委员会. 图书馆·情报与文献学名词 [M]. 北京: 科学出版社, 2017.

[15] 李军. 从产品融合到知识服务 [J]. 首都新闻出版, 2016(01): 18-21.

[16] RDF Working Group. RDF 1.1 XML Syntax [EB/OL]. (2014-02-25). http://www.w3.org/TR/2004/REC-rdf-syntax-grammar-20040210

[17] Motik, Boris, et al. OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition) [EB/OL]. (2012-12-11). http://www.w3.org/TR/2012/RECOwl2-syntax-20121211