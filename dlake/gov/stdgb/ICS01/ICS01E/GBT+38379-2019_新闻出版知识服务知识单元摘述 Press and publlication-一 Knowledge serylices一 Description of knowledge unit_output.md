

# 中华人民共和国国家标准

GB/T 38379—2019

# 新闻出版 知识服务 知识单元描述

# Press and publication—Knowledge services—Description of knowledge unit

2019-12-31 发布

2020-07-01 实施

国家市场监督管理总局发布

国家标准化管理委员会

## 目次

前言 …… I  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 缩略语 …… 1  
  
5 概念模型 …… 2  
  
6 描述规则 …… 2  
  
6.1 基本原则 …… 2  
  
6.2 描述方法 …… 2  
  
附录 A（资料性附录） 知识单元属性描述 …… 7  
  
附录 B（资料性附录） 典型知识单元描述示例 …… 10  
  
参考文献 …… 19

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由国家新闻出版署提出。

本标准由全国新闻出版标准化技术委员会(SAC/TC 527)归口。

本标准起草单位：中国铁道出版社有限公司、广东经济出版社有限公司、中国农业出版社有限公司、中国新闻出版研究院、人大数媒科技（北京）有限公司、中国人民大学出版社有限公司、中国林业出版社有限公司、石油工业出版社有限公司、成都音像出版社有限公司、英大传媒投资集团有限公司、海洋出版社。

本标准主要起草人：魏立华、李军、魏玉山、刘爱芳、李鹏、谢冰、何英、王磊、刘玮、骈骅、周雪兵、包晓琦。

# 新闻出版 知识服务 知识单元描述

## 1 范围

本标准规定了知识单元的概念模型及描述规则。

本标准适用于新闻出版及相关领域开展知识服务工作。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 13190.1—2015 信息与文献 叙词表及与其他词表的互操作 第1部分:用于信息检索的叙词表

GB/T 38377—2019 新闻出版 知识服务 知识资源建设与服务基础术语

GB/T 38378—2019 新闻出版 知识服务 知识关联通用规则

GB/T 38380—2019 新闻出版 知识服务 知识资源通用类型

## 3 术语和定义

GB/T 38377—2019 界定的术语和定义适用于本文件。为了便于使用，以下重复列出了一些术语和定义。

### 3.1 

## 知识元 knowledge element

在应用需求下，表达一个完整事物或概念的不必再分的独立的知识单位。

[GB/T 38377—2019, 定义 2.3]

### 3.2 

## 知识单元 knowledge unit

按照一定关系组织的一组知识元相关信息的集合。

[GB/T 38377—2019, 定义 2.4]

## 4 缩略语

下列缩略语适用于本文件。

DC: 都柏林核心元数据规范 (Dublin Core)

DCMI: 都柏林核心元数据倡议 (Dublin Core Metadata Initiative)

ISLI: 国际标准关联标识符(International Standard Link Identifier)

OWL: OWL 网络本体语言 (OWL Web Ontology Language)

RDF: 资源描述框架 (Resource Description Framework)

RDFS:资源描述框架模式(RDF Schema)

SKOS: 简单知识组织系统 (Simple Knowledge Organization System)

URI:统一资源识别符(Uniform Resource Identifier)

URL:统一资源定位器(Uniform Resource Locator)

XML: 可扩展标记语言 (Extensible Markup Language)

XSD: XML 模式定义 (XML Schema Definition)

## 5 概念模型

知识单元由满足应用需求的若干个知识元组成，知识元之间存在序列关系或非序列关系。同一个知识元可从属于不同的知识单元。知识单元模型示意参见图1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_239_529_930_971.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">图 1 知识单元模型示意</div>


## 6 描述规则

### 6.1 基本原则

知识单元描述遵循以下基本原则：

a）实用性：基于应用满足具体的知识聚合推送需求；

b）规范性：在一个阶段，知识单元的内容及结构是完整、准确、可靠的；

c）关联性：根据应用需求，建立相关知识元的关联关系。

### 6.2 描述方法

#### 6.2.1 描述框架

知识单元应根据应用需求筛选知识元，形成知识元集合并建立关联关系。相关知识单元可形成知识单元集合。如图 2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_205_1007_594.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 2 知识单元描述框架</div>


#### 6.2.2 知识单元

名称：知识单元。

标签：KnowledgeUnit。

定义: 根据应用需求由若干知识元根据序列和关系组成的集合。

属性：标识、名称、说明、应用需求、与……相关、所属类型、主题、知识元集合、关联关系。知识单元的属性如图3所示，属性说明参见附录A，知识单元描述示例参见附录B。

<div style="text-align: center;"><img src="imgs/img_in_image_box_353_893_849_1340.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 3 知识单元属性</div>


#### 6.2.3 应用需求

##### 6.2.3.1 用户情境

名称：用户情境。

标签：UserContextType。

定义: 描述用户特征及其周围环境的相关信息。

注释：用户特征信息，如用户性别、年龄、职业、教育背景、兴趣；应用环境特征，如时间、地点、目标等；技术环境信息主要指知识服务运行时的软硬件设备的信息，如平台信息、应用交互特征、通信及计算能力、网络带宽等。

属性：标识、名称、说明、与……相关、最终用户角色、应用目的、运行时环境要求、受众范围、难度、语种、与……相同、用户情境元数据。用户情境的属性如图4所示。属性说明参见附录A。

<div style="text-align: center;"><img src="imgs/img_in_image_box_286_431_878_1077.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 4 用户情境属性</div>


##### 6.2.3.2 知识应用需求

名称：知识应用需求。

标签：RequirementType。

定义：以为用户提供个性化知识服务为目的，面向应用的场景、背景、基础内容需求等条件。

注释：知识应用需求与特定场景、背景、基础内容需求和时间、阶段密切相关，通过面向应用的场景、背景、基础内容需求等条件形成用户知识资源需求条件规范数据，并以此为基础条件分时段分阶段精确推送知识资源内容，提供个性化的知识服务。

属性：标识、名称、说明、应用场景、使用地点、文化环境、应用背景、应用时间。

知识应用需求的属性如图 5 所示。属性说明参见附录 A。

<div style="text-align: center;"><img src="imgs/img_in_image_box_426_215_775_583.jpg" alt="Image" width="29%" /></div>


<div style="text-align: center;">图 5 知识应用需求属性</div>


#### 6.2.4 知识元集合

名称：知识元集合。

标签:KnowledgeElementCollection。

定义: 基于特定应用需求各知识元的集合。

注释：知识元集合的类型遵循 GB/T 38380—2019 的相关规定。

属性：标识、名称、说明、知识元。

知识元集合的属性如图 6 所示。属性说明参见附录 A。

<div style="text-align: center;"><img src="imgs/img_in_image_box_333_935_869_1158.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图 6 知识元集合属性</div>


#### 6.2.5 关联关系

名称：关联关系。

标签：Relationship。

定义: 根据应用需求选取的知识元间的关联关系。

属性：标识、名称、说明、源知识元、目标知识元、关系类型。关联关系的标识符宜采用 ISLI 标识。关联关系的属性如图 7 所示，属性说明参见附录 A，示例参见附录 B。

<div style="text-align: center;"><img src="imgs/img_in_image_box_402_201_769_474.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">图 7 关联关系属性</div>


知识元的关联关系按照相关度、显现度和领域范围划分类型，见 GB/T 38378—2019 第 5 章的规定。

根据应用的具体需求可对关联关系进行扩展，扩展办法遵循 GB/T 13190.1—2015 中 10.4 自定义关系的相关规定。

## 附录 A

(资料性附录)

知识单元属性描述

知识单元的属性描述见表 A.1。

<div style="text-align: center;">表 A.1 知识单元属性描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>属性标签</td><td style='text-align: center;'>属性名称</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>KnowledgeUnit</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1.1</td><td rowspan="9">UserContextType</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>label</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>描述知识单元的唯一标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>note</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>描述知识单元的名称</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>applicationRequirement</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>与知识单元相关的介绍信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>isRelatedTo</td><td style='text-align: center;'>应用需求</td><td style='text-align: center;'>以为用户提供个性化知识服务为目的，面向应用的场景、背景、基础内容需求等条件</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>kUnitType</td><td style='text-align: center;'>所属类型</td><td style='text-align: center;'>遵循GB/T 38380-2019的相关规定</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf资源</td></tr><tr><td style='text-align: center;'>1.7</td><td style='text-align: center;'>subject</td><td style='text-align: center;'>主题</td><td style='text-align: center;'>知识单元主要内容的抽象和概括</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>knowledgeElementCollection</td><td style='text-align: center;'>知识元集合</td><td style='text-align: center;'>基于一个应用需求的知识元集合</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>rdf资源</td></tr><tr><td style='text-align: center;'>1.9</td><td style='text-align: center;'>relationship</td><td style='text-align: center;'>关联关系</td><td style='text-align: center;'>相应知识元间的关联关系</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>rdf资源</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>UserContextType</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2.1</td><td rowspan="8">userContextType</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>label</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>描述用户情境的唯一标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>2.3</td><td style='text-align: center;'>note</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>描述用户情境的名称</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>isRelatedTo</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>与用户情境相关的介绍信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>intendedEndUserRole</td><td style='text-align: center;'>与……相关</td><td style='text-align: center;'>与其他知识单元的关系</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String或rdf资源</td></tr><tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>purpose</td><td style='text-align: center;'>最终用户角色</td><td style='text-align: center;'>使用知识单元的最终用户角色</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.7</td><td style='text-align: center;'>runtimeEnv</td><td style='text-align: center;'>运行时环境要求</td><td style='text-align: center;'>受众使用知识单元的目的</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.7.1</td><td style='text-align: center;'>platform</td><td style='text-align: center;'>系统平台</td><td style='text-align: center;'>使用知识单元时的网络及软硬件环境要求</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr></table>

<div style="text-align: center;">表 A.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>属性标签</td><td style='text-align: center;'>属性名称</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>2.7.2</td><td style='text-align: center;'>Network</td><td style='text-align: center;'>network</td><td style='text-align: center;'>网络要求</td><td style='text-align: center;'>对网络的要求</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.7.3</td><td style='text-align: center;'>Other Requirement</td><td style='text-align: center;'>other requirement</td><td style='text-align: center;'>其他要求</td><td style='text-align: center;'>如特殊硬件等</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>Typical Range</td><td style='text-align: center;'>typical range</td><td style='text-align: center;'>受众范围</td><td style='text-align: center;'>知识单元的典型受众范围，如年龄或等级范围</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.9</td><td style='text-align: center;'>Difficulty</td><td style='text-align: center;'>difficulty</td><td style='text-align: center;'>难度</td><td style='text-align: center;'>对于典型的目标用户来说知识单元的难度</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.10</td><td style='text-align: center;'>Language</td><td style='text-align: center;'>language</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>所使用的语种</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>2.11</td><td style='text-align: center;'>Same As</td><td style='text-align: center;'>same as</td><td style='text-align: center;'>与……相同</td><td style='text-align: center;'>与另一个用户情境相同</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf 资源</td></tr><tr><td style='text-align: center;'>2.12</td><td style='text-align: center;'>Context Meta</td><td style='text-align: center;'>context meta</td><td style='text-align: center;'>用户情境元数据</td><td style='text-align: center;'>用户情境元数据</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>rdf 资源</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>Requirement Type</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3.1</td><td style='text-align: center;'>Identifier</td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>描述知识应用需求的唯一标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>3.2</td><td style='text-align: center;'>Label</td><td style='text-align: center;'>label</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>描述知识应用需求的名称</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3.3</td><td style='text-align: center;'>Note</td><td style='text-align: center;'>note</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>与知识应用需求相关的介绍信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3.4</td><td style='text-align: center;'>App Scenario</td><td style='text-align: center;'>app scenario</td><td style='text-align: center;'>应用场景</td><td style='text-align: center;'>描述知识单元的应用场景</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>Location</td><td style='text-align: center;'>location</td><td style='text-align: center;'>使用地点</td><td style='text-align: center;'>描述知识单元的使用地点</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3.6</td><td style='text-align: center;'>Culture</td><td style='text-align: center;'>culture</td><td style='text-align: center;'>文化环境</td><td style='text-align: center;'>描述知识单元的文化环境</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3.7</td><td style='text-align: center;'>Background</td><td style='text-align: center;'>background</td><td style='text-align: center;'>应用背景</td><td style='text-align: center;'>描述知识单元的应用背景</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>3.8</td><td style='text-align: center;'>Time</td><td style='text-align: center;'>time</td><td style='text-align: center;'>应用时间</td><td style='text-align: center;'>描述知识单元的应用时间</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>DateTime</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>Knowledge Element Collection</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4.1</td><td style='text-align: center;'>Identifier</td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>描述知识元集合的唯一标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>4.2</td><td style='text-align: center;'>Label</td><td style='text-align: center;'>label</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>描述知识元集合的名称</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>4.3</td><td style='text-align: center;'>Note</td><td style='text-align: center;'>note</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>与知识元集合相关的介绍信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>4.4</td><td style='text-align: center;'>Knowledge Element</td><td style='text-align: center;'>knowledge element</td><td style='text-align: center;'>知识元</td><td style='text-align: center;'>知识元集合中所包含的知识元</td><td style='text-align: center;'>有则必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr></table>

<div style="text-align: center;">表 A.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>属性标签</td><td style='text-align: center;'>属性名称</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>Relationship</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5.1</td><td rowspan="6"></td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>标识</td><td style='text-align: center;'>描述关联关系的唯一标识</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>URI</td></tr><tr><td style='text-align: center;'>5.2</td><td style='text-align: center;'>label</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>描述关联关系的名称</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>5.3</td><td style='text-align: center;'>note</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>与关联关系相关的介绍信息</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>String</td></tr><tr><td style='text-align: center;'>5.4</td><td style='text-align: center;'>source</td><td style='text-align: center;'>源知识元</td><td style='text-align: center;'>关联关系中的源知识元</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>destination</td><td style='text-align: center;'>目标知识元</td><td style='text-align: center;'>关联关系中的目标知识元</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr><tr><td style='text-align: center;'>5.6</td><td style='text-align: center;'>relationshipType</td><td style='text-align: center;'>关系类型</td><td style='text-align: center;'>关联关系的类型，遵循 GB/T 38380—2019 的相关规定</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>String 或 rdf 资源</td></tr></table>

# 附录 B

# (资料性附录)

# 典型知识单元描述示例

### B.1 描述约定

#### B.1.1 描述原则

采用 XSD 数据模型，参照 W3C XML Schema Definition Language（XSD）编制。

#### B.1.2 命名规则

定义知识单元的名称、属性时，每个英文单词的首字母大写，其余字母均小写，不使用任何连字符，在名称中不使用下划线“_”、下圆点“.”和连字符“-”。

单词均完整使用，名称不使用缩略语，以保证语义的清晰，提高可读性，因特殊原因需要在名称使用缩略语的，提供对应的全称和相应的说明。

#### B.1.3 XML 组件命名

与元素、属性、简单类型和复杂类型相关的命名基于如下约定。

对 XML 组件进行命名时，若名称多于一个英文单词，则除第一个单词外，其后每个单词的首字母均大写。第一个单词首字母是否大写根据以下原则确定：

a） 组件元素的命名: 第一个单词的首字母大写。

b）组件属性的命名：第一个单词的首字母小写。

c）复杂类型的命名：第一个单词的首字母大写，类型名后添加后缀 Type。

d）简单类型的命名：第一个单词的首字母小写，类型名后添加后缀 Type。

### B.2 命名空间

表 B.1 描述了所用到的命名空间和前缀。

<div style="text-align: center;"><img src="imgs/img_in_image_box_195_1125_234_1153.jpg" alt="Image" width="3%" /></div>


<div style="text-align: center;">表 B.1 知识单元数据引用命名空间列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>前缀</td><td style='text-align: center;'>命名空间</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>dc</td><td style='text-align: center;'>http://purl.org/dc/elements/1.1/</td><td style='text-align: center;'>都柏林核心元素</td></tr><tr><td style='text-align: center;'>dcterms</td><td style='text-align: center;'>http://purl.org/dc/terms/</td><td style='text-align: center;'>都柏林核心术语</td></tr><tr><td style='text-align: center;'>rdf</td><td style='text-align: center;'>http://www.w3.org/1999/02/22-rdf-syntax-ns#</td><td style='text-align: center;'>RDF 词汇术语</td></tr><tr><td style='text-align: center;'>rdfs</td><td style='text-align: center;'>http://www.w3.org/2000/01/rdf-schema#</td><td style='text-align: center;'>RDFs 词汇术语</td></tr><tr><td style='text-align: center;'>foaf</td><td style='text-align: center;'>http://xmlns.com/foaf/0.1/</td><td style='text-align: center;'>FOAF 词汇术语</td></tr><tr><td style='text-align: center;'>ore</td><td style='text-align: center;'>http://www.openarchives.org/ore/terms/</td><td style='text-align: center;'>ORE 词汇术语</td></tr><tr><td style='text-align: center;'>skos</td><td style='text-align: center;'>http://www.w3.org/2004/02/skos/core#</td><td style='text-align: center;'>SKOS 词汇术语</td></tr><tr><td style='text-align: center;'>gkadm</td><td style='text-align: center;'>自定义的管理元数据命名空间</td><td style='text-align: center;'>自定义的管理元数据词汇术语</td></tr></table>

### B.3 XML 描述示例

示例 1～示例 7 是知识单元相关的 XML 描述片段，用来解释知识单元中重要元素的描述方法；示例 8 是知识单元的完整 XML 描述示例，其中包含两个知识单元，分别来源于图书推荐需求和铁道专业术语检索需求，涉及 5 个知识元，示例 8 知识单元样例的示意如图 B.1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_305_394_899_824.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 B.1 示例 8 所对应的知识单元样例示意</div>


示例 1：本示例是描述知识单元属性扩展方法的样例。对象类型所包含属性的定义域或约束不能满足新闻出版机构对内容对象做进一步限定的描述时，可以通过细化增加已有类的属性进行扩展以满足应用。

本示例对知识单元中的已有属性进行细化：对“知识应用需求”类中的“应用背景”进行细化，细化为“铁路专业应用背景”。

示例代码如下：

<owl:ObjectProperty rdf:about="&.gkadm;railwayBackground">
    <rdfs:subPropertyOf rdfs:label="gkadm;background"/>
    <rdfs:label xml:lang="en">RailwayBackground</rdfs:label>
    <rdfs:label xml:lang="zh">铁路专业应用背景</rdfs:label>
    <owl:versionInfo>1.0</owl:versionInfo>
    <skos:note xml:lang="zh">铁路专业的应用背景</skos:note>
    <rdfs:isDefinedBy rdf:resource="&.gkadm;"/>
</owl:ObjectProperty>

示例 2：本示例是描述知识单元属性添加方法的示例。在当前知识单元数据模型中定义的对象类型所包含的属性不能满足新闻出版机构对内容对象的描述时，可通过添加新的属性进行扩展。本示例添加一个新属性（用“index”表示），采用所属单位自己的命名空间（“http://book.crphdm.com/”）。定义该新属性的示例代码（RDF/XML）如下：

<owl:ObjectProperty rdf; about="http://book.crphdm.com/Property/23">
    <rdfs:label xml:lang="en">index</rdfs:label>
    <rdfs:label xml:lang="zh">索引</rdfs:label>
    <owl:versionInfo>1.0</owl:versionInfo>
    <skos:note xml:lang="zh">在《GB/T 50262—2013 铁路工程基本术语标准》中的索引号</skos:note>
    <rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/"/>
</owl:ObjectProperty>

示例 3：本示例是描述知识单元类型扩展方法的示例。如果当前知识单元数据模型（及其扩展模型）中定义的对象类型粒度过粗，且未包含新闻出版机构所需要的确切对象类型，则新闻出版机构可以添加新的对象类型。例如新闻出版机构需要对知识应用需求加入“铁路应用背景”属性，则构建一个新的类型，并定义“铁路应用场景”属性。示例代码如下：

<owl:Class rdf:about="&gkadm;RailwayAppReq">
    <rdfs:subClassOf rdf:resource="&gkadm;ApplicationRequirementType"/>
    <rdfs:label xml:lang="en">RailwayApplicationRequirement</rdfs:label>
    <rdfs:label xml:lang="zh">铁路知识应用需求</rdfs:label>
    <skos:note xml:lang="zh">针对铁路专业的知识应用需求</skos:note>
    <rdfs:isDefinedBy rdf:resource="&gkadm"/>
</owl:Class>
<owl:ObjectProperty rdf:about="&gkadm;railwayBackground">
    <rdfs:subPropertyOf rdf:resource="gkadm;background"/>
    <rdfs:label xml:lang="en">RailwayBackground</rdfs:label>
    <rdfs:label xml:lang="zh">铁路专业应用背景</rdfs:label>
    <owl:versionInfo>1.0</owl:versionInfo>
    <skos:note xml:lang="zh">铁路专业的应用背景</skos:note>
    <rdfs:isDefinedBy rdf:resource="&gkadm"/>
</owl:ObjectProperty>

示例 4：本示例是描述知识元间等同关系数据表达的样例。等同关系采用参考 GB/T 13190.1—2015 第 8 章、第 9 章的相关规定，即对自然语言中优选词与它相对应非优选词间关系的语义进行描述。知识元关联关系的等同关系数据模型示例如下：

<Relationship rdf:about="http://book.crphdm.com/relation/122">
    <dc:identifier>http://book.crphdm.com/relation/122</dc:identifier>
    <RelationshipType rdf:resource="http://book.crphdm.com/relationtype/1"/>
    <label xml:lang="zh">等同</label>
    <source rdf:resource="http://book.crphdm.com/concept/135"/>
    <destination rdf:resource="http://book.crphdm.com/concept/136"/>
    <distance>99</distance>
    <isDefinedBy rdf:resource="http://book.crphdm.com/relation"/>
</Relationship>

示例 5：本示例是描述知识元间等级关系数据表达的样例。等级关系采用参考 GB/T 13190.1—2015 中 10.2 的相关规定进行描述，即等级关系指所描述知识元的范围边界与另一知识元的范围边界处于包含或被包含的范围内，基于上位和下位的程度或层次，上位表示一个类或整体，下位表示成员或部件。知识元间等级关系的数据模型示例如下：

Relationship rdf; about="http://book.crphdm.com/relation/123">
<dc; identifier>http://book.crphdm.com/relation/123</dc; identifier>
<RelationshipType rdf; resource="http://book.crphdm.com/relationtype/2"/>
<label xml:lang="zh">等级</label>
<source rdf:resource="http://book.crphdm.com/concept/137"/>
<destination rdf:resource="http://book.crphdm.com/concept/136"/>
<distance>20</distance>
<isDefinedBy rdf:resource="http://book.crphdm.com/relation"/>
/Relationship>

示例 6：本示例是描述知识元间相关关系数据表达的样例。相关关系采用参考 GB/T 13190.1 的相关规定，知识元间的相关关系指非等级相关，且语义上或概念上有一定程度关联的一对知识元间的关系。知识元间相关关系的数据模型示例如下：

<Relationship rdf:about="http://book.crphdm.com/relation/124">
    <dc:identifier>http://book.crphdm.com/relation/124</dc:identifier>
    <RelationshipType rdf:resource="http://book.crphdm.com/relationtype/3"/>
    <label xml:lang="zh">相关</label>
    <source rdf:resource="http://book.crphdm.com/concept/135"/>
    <destination rdf:resource="http://book.crphdm.com/concept/125"/>
    <distance>35</distance>
    <isDefinedBy rdf:resource="http://book.crphdm.com/relation"/>
</Relationship>
示例 7：本示例是描述关系扩展方法的样例。等级关系扩展的数据模型示例如下：
<RelationshipType rdf:about="http://book.crphdm.com/relationtype/25">
    <subRelationshipOf rdf:resource="http://book.crphdm.com/relationtype/2"/>
    <label xml:lang="zh">显示</label>
    <isDefinedBy rdf:resource=http://book.crphdm.com"/>
</RelationshipType>

示例 8：本示例以铁路专业相关资源和术语为例，构建两个完整的知识单元。

本示例引用“铁路信号”、“视觉信号”、“听觉信号”、“夜间信号”和“信号机”作为知识元，同时“铁路信号”和“信号机”作为铁路工程基本术语，在 GB/T 50262—2013 中存在索引号，将其作为必选项，放入“概念”的扩展类“铁路工程基本术语”中，同时构建新的属性“索引号”。此外，根据新闻出版机构的应用需要，增加知识元的权重属性作为可选项。知识元关联关系中，将对“等级关系”和“相关关系”进行扩展，以细化知识元之间的关系。

示例代码如下：

<?xml version="1.0" encoding="UTF-8"?>
<xml-model href="GKADM-INTERNAL.xsd" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron?" />
<rdf:RDF xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:dc="http://purl.org/dc/elements/1.1" xmlns:gkadm="http://xxx.com/gkadm/schema/cores/"
         xmlns:foaf="http://xmlns.com/foaf/0.1" xmlns:rdaGr2="http://rdvocab.info/ElementsGr2/"
         xmlns:ore="http://www.openarchives.org/ore/terms/" xmlns:dcterms="http://purl.org/dc/terms/"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:wgs84="http://www.w3.org/2003/01/geo/wgs84_pos#"
         xmlns:skos="http://www.w3.org/2004/02/skos/core#" xmlns:tdpress="http://book.crphdm.com">
    <owl:ObjectProperty rdf:about="http://book.crphdm.com/Property/23">
        <rdfs:label xml:lang="en">weight</rdfs:label>
        <rdfs:label xml:lang="zh">权重</rdfs:label>
        <owl:versionInfo>1.0</owl:versionInfo>
        <skos:note xml:lang="zh">每个词在知识体系中所占的权重</skos:note>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://book.crphdm.com/Property/23">
        <rdfs:label xml:lang="en">index</rdfs:label>
        <rdfs:label xml:lang="zh">索引</rdfs:label>
        <owl:versionInfo>1.0</owl:versionInfo>
        <skos:note xml:lang="zh">在《GB/T 50262—2013 铁路工程基本术语标准》中的索引号</skos:note>
    </owl:ObjectProperty>
    <owl:Class rdf:about="http://book.crphdm.com/class/">
        <rdfs:subClassOf rdf:resource="http://www.w3.org/2004/02/skos/core#Concepts" />
    </owl:Class>
</rdf:捧</rdfs:label>

<rdf:label xml:lang="en">RailwayTerm</rdf:label>
<rdf:label xml:lang="zh">铁路工程专业术语</rdf:label>
<skos:note xml:lang="zh">铁路工程专业术语</skos:note>
/owl:Class>
tdpress:RailwayTerm rdf:about="http://book.crphdm.com/concept/135">
    <dc:identifier>http://book.crphdm.com/concept/135</dc:identifier>
    <gkadm:ketype>Concept</gkadm:ketype>
    <gkadm:kesubtype>RailwayTerm</gkadm:kesubtype>
    <rdfs:label>铁路信号</rdfs:label>
    <skos:altLabel>信号</skos:altLabel>
    <tdpress:weight>92.3</tdpress:weight>
    <tdpress:index>14.1.1</tdpress:index>
    <skos:note>SAIC</skos:note>

铁路运输系统中，为保证行车安全、提高区间和车站通过能力及编解能力而设置的手动控制、自动控制及遥控、遥信技术的总称。信号是对行车或调车人员发出指示运行条件的命令，它通过音响、颜色、形状、位置、灯光等来表示。

<skos:notation>铁路工程基本术语.信号</skos:notation>
<skos:inScheme>铁路</skos:inScheme>
</tdpress:RailwayTerm>

<rdfs:Concept rdf:about="http://book.crphdm.com/concept/136">
<dc:identifier>http://book.crphdm.com/concept/136</dc:identifier>
<rdfs:label>视觉信号</rdfs:label>

<gkadm:ketype>Concept</gkadm:ketype>
<tdpress:weight>50</tdpress:weight>
<skos:note>

铁路信号包括视觉信号和听觉信号两大类。用信号机、信号旗、信号灯、信号牌、信号表示器、信号标志及火炬等显示的信号均属视觉信号，列控车载设备的速度显示亦属视觉信号。

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

<rdfs:Concept rdf:about="http://book.crphdm.com/concept/137">
<dc:identifier>http://book.crphdm.com/concept/137</dc:identifier>
<rdfs:label>听觉信号</rdfs:label>
<gkadm:ketype>Concept</gkadm:ketype>
<tdpress:weight>58.8</tdpress:weight>

〈skos:note〉用号角、口笛、机车、动车组及自轮运转特种设备的鸣笛等发出的信号均属听觉信号〈/skos:note〉

<skos:notation>铁路工程基本术语.信号</skos:notation>
<skos:inScheme>铁路</skos:inScheme>
</rdfs:Concept>

<rdfs:Concept rdf:about="http://book.crphdm.com/concept/141">
    <dc:identifier>http://book.crphdm.com/concept/141</dc:identifier>
    <rdfs:label>夜间信号</rdfs:label>
    <gkadm:ketype>Concept</gkadm:ketype>
    <tdpress:weight>92.3</tdpress:weight>
    <skos:note></skos:note>
    <skos:notation>铁路工程基本术语.信号</skos:notation>
    <skos:inScheme>铁路</skos:inScheme>
</rdfs:Concept>

<gkadm:RelationshipType rdf:about="http://book.crphdm.com/relationtype/25">
    <rdfs:subRelationshipOf rdfs:label="等级关系"/>
    <rdfs:label xml:lang="zh">包含</rdfs:label>
    <rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/"/>
</gkadm:RelationshipType>

<gkadm:RelationshipType rdf:about="http://book.crphdm.com/relationtype/26">
    <rdfs:subRelationshipOf rdfs:label="相关关系"/>
    <rdfs:label xml:lang="zh">显示</rdfs:label>
    <rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/"/>
</gkadm:RelationshipType>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/131">
    <dc:identifier>http://book.crphdm.com/relation/131</dc:identifier>
    <gkadm:RelationshipType rdf:resource="http://book.crphdm.com/relationtype/25"/>
    <rdfs:label xml:lang="zh">包含</rdfs:label>
    <gkadm:source rdf:resource="http://book.crphdm.com/concept/135"/>
    <gkadm:destination rdf:resource="http://book.crphdm.com/concept/136"/>
    <gkadm:distance>20</gkadm:distance>
    <rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/132">
    <dc:identifier>http://book.crphdm.com/relation/132</dc:identifier>
    <gkadm:RelationshipType rdf:resource="http://book.crphdm.com/relationtype/25"/>
    <rdfs:label xml:lang="zh">包含</rdfs:label>
    <gkadm:source rdf:resource="http://book.crphdm.com/concept/135"/>
    <gkadm:destination rdf:resource="http://book.crphdm.com/concept/137"/>
    <gkadm:distance>50</gkadm:distance>
    <rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/133">
    <dc:identifier>http://book.crphdm.com/relation/133</dc:identifier>
    <gkadm:RelationshipType rdf:resource="http://book.crphdm.com/relationtype/26"/>
    <rdfs:label xml:lang="zh">显示</rdfs:label>
    <gkadm:source rdf:resource="http://book.crphdm.com/concept/139"/>
    <gkadm:destination rdf:resource="http://book.crphdm.com/concept/136"/>
</gkadm:Relationship>

<gkadm:distance>75</gkadm:distance>
<rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:Relationship rdf:about="http://book.crphdm.com/relation/134">
<dc:identifier>http://book.crphdm.com/relation/134</dc:identifier>
<gkadm:RelationshipType rdf:resource="http://book.crphdm.com/relationtype/25"/>
<rdfs:label xml:lang="zh">包含</rdfs:label>
<gkadm:source rdf:resource="http://book.crphdm.com/concept/135"/>
<gkadm:destination rdf:resource="http://book.crphdm.com/concept/141"/>
<gkadm:distance>99</gkadm:distance>
<rdfs:isDefinedBy rdf:resource="http://book.crphdm.com/relation/"/>
</gkadm:Relationship>

<gkadm:UserContextType rdf:about="http://book.crphdm.com/usercontext/152">
<dc:identifier>http://book.crphdm.com/usercontext/152</dc:identifier>
<rdfs:label>图书推荐用户场景</rdfs:label>
<gkadm:purpose>图书推荐</gkadm:purpose>
<gkadm:typicalRange>职业教育</gkadm:typicalRange>
<gkadm:difficulty>难</gkadm:difficulty>
</gkadm:UserContextType>

<gkadm:KnowledgeApplicationRequirementType rdf:about="http://book.crphdm.com/appreq/123">
<dc:identifier>http://book.crphdm.com/appreq/123</dc:identifier>
<rdfs:label>图书推荐应用需求</rdfs:label>
<gkadm:kElemengType>概念知识元</gkadm:kElemengType>
<gkadm:appScenario>资源推荐</gkadm:appScenario>
<gkadm:location>中国</gkadm:location>
<gkadm:background>高校教育</gkadm:background>
</gkadm:KnowledgeApplicationRequirementType>

<gkadm:ApplicationRequirementType rdf:about="http://book.crphdm.com/applicationrequirement/172">
<gkadm:inUserContext rdf:resource="http://book.crphdm.com/usercontext/152"/>
<gkadm:inKnowledgeApplicationRequirement rdf:resource="http://book.crphdm.com/appreq/123"/>
</gkadm:ApplicationRequirementType>

<gkadm:KnowledgeElementCollection rdf:about="http://book.crphdm.com/elementcollection/105">
<dc:identifier>http://book.crphdm.com/elementcollection/105</dc:identifier>
</gkadm:KnowledgeElementCollection>

<rdfs:label>专业图书推荐知识元集合</rdfs:label>
<gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/135"/>
<gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/136"/>
<gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/137"/>
<gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/139"/>
<gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/141"/>
</gkadm:KnowledgeElementCollection>

<gkadm:KnowledgeUnit rdf:about="http://book.crphdm.com/knowledgeunit/125">

<dc:identifier>http://book.crphdm.com/kunit/141</dc:identifier>
<rdfs:label>铁道专业类图书推荐</rdfs:label>
<skos:notation>铁路工程基本术语</skos:notation>
<gkadm:inApplicationRequirement>
    <rdf:resource="http://book.crphdm.com/applicationrequirement/172" />
    <gkadm:knowledgeElementCollection>
        <rdf:resource="http://book.crphdm.com/elementcollection/105" />
        <gkadm:relationship rdf:resource="http://book.crphdm.com/relation/131" />
        <gkadm:relationship rdf:resource="http://book.crphdm.com/relation/132" />
        <gkadm:relationship rdf:resource="http://book.crphdm.com/relation/133" />
        <gkadm:relationship rdf:resource="http://book.crphdm.com/relation/134" />
    </gkadm:KnowledgeUnit>
    <gkadm:UserContextType rdf:about="http://book.crphdm.com/usercontext/157">
        <dc:identifier>http://book.crphdm.com/usercontext/157</dc:identifier>
        <rdfs:label>铁道专业术语检索</rdfs:label>
        <gkadm:purpose>术语检索</gkadm:purpose>
        <gkadm:typicalRange>职业教育</gkadm:typicalRange>
        <gkadm:difficulty>难</gkadm:difficulty>
    </gkadm:UserContextType>
    <gkadm:KnowledgeApplicationRequirementType>
        <rdf:about="http://book.crphdm.com/appreq/125">
            <dc:identifier>http://book.crphdm.com/appreq/125</dc:identifier>
            <rdfs:label>术语检索应用需求</rdfs:label>
            <gkadm:kElemengType>概念知识元</gkadm:kElemengType>
            <gkadm:appScenario>术语检索</gkadm:appScenario>
            <gkadm:location>中国</gkadm:location>
            <gkadm:background>高等教育</gkadm:background>
        </gkadm:KnowledgeApplicationRequirementType>
        <gkadm:ApplicationRequirementType>
            <rdf:about="http://book.crphdm.com/applicationrequirement/157">
                <gkadm:inUserContext rdf:resource="http://book.crphdm.com/usercontext/157" />
                <gkadm:inKnowledgeApplicationRequirement>
                    <rdf:resource="http://book.crphdm.com/appreq/125" />
                </gkadm:ApplicationRequirementType>
            </gkadm:KnowledgeElementCollection>
            <rdf:about="http://book.crphdm.com/elementcollection/125">
                <dc:identifier>http://book.crphdm.com/elementcollection/125</dc:identifier>
            </rdfs:label>
            <gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/135" />
                <gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/136" />
                <gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/137" />
                <gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/139" />
                <gkadm:knowledgeElement rdf:resource="http://book.crphdm.com/concept/141" />
            </gkadm:KnowledgeElementCollection>
        </gkadm:KnowledgeUnit rdf:about="http://book.crphdm.com/knowledgeunit/137">
    </gkadm:KnowledgeUnit>
</gkadm>

（dc:identifier）http://book.crphdm.com/kunit/141（/dc:identifier）
（rdfs:label）铁道专业术语检索（/rdfs:label）
（skos:notation）铁路工程基本术语（/skos:notation）
（gkadm:inApplicationRequirement）
（rdf:resource="http://book.crphdm.com/appreq/157" />
（gkadm:knowledgeElementCollection）
（rdf:resource="http://book.crphdm.com/elementcollection/125" />
（gkadm:relationship rdf:resource="http://book.crphdm.com/relation/131" />
（gkadm:relationship rdf:resource="http://book.crphdm.com/relation/132" />
（gkadm:relationship rdf:resource="http://book.crphdm.com/relation/133" />
（gkadm:relationship rdf:resource="http://book.crphdm.com/relation/134" />
（/gkadm:KnowledgeUnit）
（rdf:RDF）

## 参 考 文 献

[1] GB/T 4880.2—2000 语种名称代码 第2部分：3字母代码

[2] GB/T 4880.3—2009 语种名称代码 第3部分:所有语种的3字母代码

[3] GB/T 5795—2006 中国标准书号

[4] GB/T 7408—2005 数据元和交换格式 信息交换 日期和时间表示法

[5] GB/T 18793—2002 信息技术 可扩展置标语言(XML)1.0

[6] GB/T 25100 信息与文献 都柏林核心元数据元素集

[7] GB/T 32867—2016 中国标准关联标识符(ISLI)

[8] GB/T 50262—2013 铁路工程基本术语标准

[9] CY/T 90.1～90.5—2013 出版元数据

[10] CY/T 102.1～102.2—2014 数字内容对象存储、复用与交换规范

[11] 李军. 从产品融合到知识服务 [J]. 首都新闻出版, 2016(01): 18-21.

[12] RDF Working Group. RDF 1.1 XML Syntax [EB/OL]. (2014-02-25). http://www.w3.org/TR/2004/REC-rdf-syntax-grammar-20040210

[13] Motik, Boris, et al. OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition) [EB/OL]. (2012-12-11). http://www.w3.org/TR/2012/RECOwl2-syntax-20121211

[14] Open Archives Initiative. ORE Specifications and User Guides—Table of Contents[EB/OL].(2014-08-14). http://www.openarchives.org/ore/1.0/toc

[15] XML Schema Working Group. W3C XML Schema Definition Language (XSD) 1.1 Part 1: Structures $$ EB/OL $$ .(2012-04-05).https://www.w3.org/TR/2012/REC-xmlschema11-1-20120405