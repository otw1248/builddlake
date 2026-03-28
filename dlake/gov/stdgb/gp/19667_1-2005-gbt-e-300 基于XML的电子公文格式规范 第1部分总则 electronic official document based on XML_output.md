

# 中华人民共和国国家标准

GB/T 19667.1—2005

# 基于 XML 的电子公文格式规范 第 1 部分: 总则

# Specification for the structure of electronic official document based on XML— Part 1: General principles

2005-02-18 发布

2005-05-01 实施

## 目次

前言 …… I    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 缩略语 …… 2    
5 电子公文基本要素 …… 2    
6 电子公文特性 …… 3    
6.1 真实性 …… 3    
6.2 安全性 …… 3    
6.3 易用性 …… 3    
7 电子公文分类 …… 3    
7.1 党的机关公文 …… 3    
7.2 行政机关公文 …… 3    
7.3 其他机关公文 …… 3    
8 电子公文处理过程 …… 4    
8.1 过程模型 …… 4    
8.2 创建 …… 4    
8.3 办理 …… 4    
8.4 交换 …… 4    
8.5 归档 …… 4    
8.6 销毁 …… 4    
9 标准各部分内容和相互关系 …… 4    
9.1 各部分综述 …… 4    
9.2 各部分之间相互关系 …… 5    
9.3 各部分依赖关系模型 …… 5    
10 电子公文 XML 描述规则 …… 6    
10.1 字符集 …… 6    
10.2 命名方法 …… 6    
10.3 映射规则 …… 6    
10.4 命名空间 …… 6    
11 电子公文 XML 描述 …… 6    
11.1 概述 …… 6    
11.2 电子公文 …… 6    
附录 A（资料性附录） 层次模型图中所用的图型符号说明 …… 9    
附录 B（资料性附录） 参与本部分制定工作的单位名单 …… 10

## 前言

GB/T 19667 在总标题《基于 XML 的电子公文格式规范》下，拟分为七个部分：

——第1部分：总则；

——第2部分:公文体;

——第3部分:显现;

——第4部分:办理;

——第5部分:交换;

——第6部分:归档;

——第7部分:安全。

本部分为 GB/T 19667 的第 1 部分。

本部分公文用语与《中国共产党机关公文处理条例》及《国家行政机关公文处理办法》中规定的用语一致。

本部分的附录 A、附录 B 为资料性附录。

本部分由国家电子政务标准化总体组提出并归口。

本部分主要起草单位：深圳市质量技术监督局、深圳市科健信息技术有限公司、南京政治学院上海分院、上海市信息化办公室、金山软件股份有限公司、北大方正技术研究院、深圳市标准技术研究院、深圳市政府机关政务信息化办公室、深圳市委机关办公自动化办公室、上海万达信息股份有限公司、上海颐东网络信息有限公司、上海长城颐东软件有限公司、北京书生电子技术有限公司。

本部分主要起草人：谭建军、李翔、廖志飞、张正强、张峰昌、张建良、俞科。

# 基于 XML 的电子公文格式规范   第 1 部分: 总则

## 1 范围

GB/T 19667 的本部分规定了基于 XML 的电子公文的通用要求和基本原则。

本部分适用于党政机关制发的基于 XML 的电子公文。其他机关和团体制发的电子公文可参照执行。

## 2 规范性引用文件

下列文件中的条款通过 GB/T 19667 的本部分的引用而成为本部分的条款。凡是注明日期的引用文件，其随后所有的修改单（不包括勘误的内容）或修订版均不适用于本部分。然而，鼓励根据本部分达成协议的各方研究是否可使用这些文件的最新版本。凡是不注明日期的引用文件，其最新版本适用于本部分。

GB/T 9704—1999 国家行政机关公文格式

GB 11714—1997 全国组织机构代码编制规则

GB 13000.1—1993 信息技术 通用多八位编码字符集(UCS) 第一部分:体系结构与基本多文种平面(idt ISO/IEC 10646-1:1993)

GB 18030—2000 信息技术 信息交换用汉字编码字符集 基本集的扩充

《中国共产党机关公文处理条例》中办发 $$ 1996 $$ 14号

《国家行政机关公文处理办法》 国发 $$ 2000 $$ 23号

## 3 术语和定义

GB/T 9704—1999、《中国共产党机关公文处理条例》和《国家行政机关公文处理办法》中确立的以及下列术语和定义均适用于 GB/T 19667 的本部分。

### 3.1 

## 电子公文 electronic official document

以数字形式存储于磁带、磁盘、光盘等媒体，依赖计算机系统阅读、处理并可在通信网络上传输的公文。

### 3.2 

## 基于 XML 的电子公文 electronic official document based on XML

以可扩展置标语言(XML)对公文处理过程的相关信息进行结构化描述的电子公文。

注：本部分中所使用的“电子公文”术语如无特别说明，专指基于 XML 的电子公文。

### 3.3 

## 公文体 document body

公文实体的内容，由眉首、主体、版记三部分组成。

### 3.4 

## 显现 display

以可感知、并符合规范格式的形式来呈现文件内容的操作。

注：典型的显现媒体有纸和视频屏幕。

### 3.5 

## 文档类型定义 DTD

用置标语言表达并为某个具体文档或一类文档定义内容模型和文档元素(包括控制元素内容与特性的规则)的一种特殊形式的文档定义。

### 3.6 

## 模式 schema

一种以含有逻辑约束规则的式样为基础的结构化模式语言。

### 3.7 

## 元素 element

某个数据集内的一个具体数据项。

### 3.8 

## 属性 attribute

给一个具体元素实例添加信息或修改其信息的一个名称——值对。

### 3.9 

## 层次模型 hierarchy model

XML 文档元素的层次结构模型。

### 3.10 

## 属性列表 attribute list

与一个具体文档元素相关联的一个或多个属性的集合。

## 4 缩略语

下列缩略语适用于本标准。

DTD 文档类型定义

UML 统一建模语言

W3C 万维网联盟

XML 可扩展置标语言

## 5 电子公文基本要素

基于 XML 的电子公文应能满足各级党政机关电子公文处理的需要，组成要素应包括记录公文处理全过程的必要信息。电子公文基本要素如下：

——公文体信息；

——公文式样信息；

——公文办理信息；

——公文交换信息；

——公文归档信息；

——公文安全信息。

各要素层次关系如图 1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_345_194_842_656.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 1 各要素层次关系图</div>


## 6 电子公文特性

### 6.1 真实性

电子公文在其整个生命周期内应当保证其真实性，电子公文的真实性是：

a）与原文的意图相符；

b）与原文的形成者和发送者相符；

c）与原文的形成和发送时间一致。

### 6.2 安全性

电子公文在其整个生命周期内应当保证其安全性，电子公文的安全性是：

a）电子公文来源于或发送至可信赖的发送者或接收者；

b）对电子公文所作的任何处理不可否认；

c） 电子公文在处理过程中不被未获授权人员篡改或窃取。

### 6.3 易用性

电子公文与原文相比，应当更易于查找、检索、显现和理解。在形成电子公文过程中所产生的各类附加信息应当有助于对公文的理解。

## 7 电子公文分类

### 7.1 党的机关公文

党的机关公文是指《中国共产党机关公文处理条例》中规定的法定性公文，主要包括决议、决定、指示、意见、通知、通报、公告、报告、请示、批复、条例、规定、函及会议纪要等14种公文。

### 7.2 行政机关公文

行政机关公文是指《国家行政机关公文处理办法》中规定的法定性公文，主要包括命令（令）、决定、公告、通告、通知、通报、议案、报告、请示、批复、意见、函及会议纪要等13种公文。

### 7.3 其他机关公文

党政机关以外的其他机关和团体的公文，为本标准中的扩展公文类型。

## 8 电子公文处理过程

### 8.1 过程模型

图 2 中的模型描述了电子公文从创建到归档或销毁的一般过程，“办理”和“交换”之间可以有循环过程。

<div style="text-align: center;"><img src="imgs/img_in_image_box_240_348_904_554.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">图 2 过程模型图</div>


### 8.2 创建

根据一定的规则建立电子公文的过程。

### 8.3 办理

通过计算机系统对电子公文进行收发文、批阅等相关操作。

### 8.4 交换

按始发者意图进行跨系统、跨平台电子公文传递。

### 8.5 归档

依据国家或本部门档案管理规定对办理完毕后的电子公文进行存储。

### 8.6 销毁

依据有关规定将电子公文从存储介质上物理删除。

## 9 标准各部分内容和相互关系

### 9.1 各部分综述

#### 9.1.1 第1部分: 总则

该部分定义了用于标准各部分的术语，规定了电子公文基本要素和分类，描述了电子公文特性、电子公文处理过程以及标准各部分内容概述和相互关系，给出了基于 XML 的描述规则。

#### 9.1.2 第2部分: 公文体

该部分定义了电子公文公文体的组成要素、逻辑结构 UML 模型，给出了各组成要素的 DTD 和 Schema 描述及电子公文和公文体的 DTD 和 Schema 描述。

#### 9.1.3 第3部分:显现

该部分定义了电子公文显现的方式，主要包括党的机关公文的显现格式、行政机关公文的显现格式。

#### 9.1.4 第4部分:办理

该部分定义了电子公文收发、审阅等办理环节的元数据，并对元数据与电子公文的关系加以描述。

#### 9.1.5 第5部分:交换

该部分定义了电子公文交换过程中各个环节的元数据，并对元数据与电子公文的关系加以描述。

#### 9.1.6 第6部分:归档

该部分定义了电子公文归档要求、归档方法和归档过程，并对归档过程中的元数据与电子公文的关系加以描述。

#### 9.1.7 第7部分:安全

该部分定义了电子公文的安全机制。

### 9.2 各部分之间相互关系

如果需要显现基于 XML 的电子公文,可使用:

a）第1部分：总则；

b) 第 2 部分: 公文体;

c) 第 3 部分: 显现;

d) 第 7 部分: 安全。

如果需要办理基于 XML 的电子公文,可使用:

a）第1部分：总则；

b) 第 2 部分: 公文体；

c) 第 3 部分: 显现;

d) 第 4 部分: 办理;

e）第5部分：交换；

f）第7部分：安全。

如果需要对基于 XML 的电子公文进行归档,可使用:

a）第1部分：总则；

b) 第 2 部分: 公文体;

c) 第 3 部分: 显现;

d) 第 6 部分: 归档;

e) 第 7 部分: 安全。

如果需要交换基于 XML 的电子公文,可使用:

a）第1部分：总则；

b) 第 2 部分: 公文体;

c) 第 3 部分: 显现;

d) 第 5 部分: 交换;

e) 第 6 部分: 归档;

f) 第 7 部分: 安全。

### 9.3 各部分依赖关系模型

本标准各部分之间相互依赖关系的模型见图3：

<div style="text-align: center;"><img src="imgs/img_in_image_box_346_1110_836_1486.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 3 依赖关系模型图</div>


## 10 电子公文 XML 描述规则

### 10.1 字符集

电子公文应采用 GB 13000.1—1993 或 GB 18030—2000 中的双字节 1 区、2 区和 5 区规定的字符集。

### 10.2 命名方法

电子公文的 DTD 和 Schema 中各组成元素和属性的标记采用规范性汉字字符命名。

### 10.3 映射规则

本标准各个部分的 UML 结构模型和 XML 结构模型的映射关系的规定见表 1。

<div style="text-align: center;">表 1 UML-XML 映射关系</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UML 结构模型</td><td style='text-align: center;'>XML 结构模型</td></tr><tr><td style='text-align: center;'>类/对象</td><td style='text-align: center;'>元素</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>属性</td></tr><tr><td style='text-align: center;'>组成关系</td><td style='text-align: center;'>元素与子元素的包含关系</td></tr><tr><td style='text-align: center;'>继承关系</td><td style='text-align: center;'>基于自定义复杂类型的扩展关系</td></tr></table>

### 10.4 命名空间

电子公文的各个部分命名空间见表2。

<div style="text-align: center;">表 2 命名空间</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>命名空间</td></tr><tr><td style='text-align: center;'>电子公文</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc</td></tr><tr><td style='text-align: center;'>公文体</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc/body</td></tr><tr><td style='text-align: center;'>交换</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc/exchange</td></tr><tr><td style='text-align: center;'>办理</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc/process</td></tr><tr><td style='text-align: center;'>归档</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc/archive</td></tr><tr><td style='text-align: center;'>显现</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc/display</td></tr><tr><td style='text-align: center;'>安全</td><td style='text-align: center;'>http://www.egs.org.cn/eGovDoc/security</td></tr></table>

## 11 电子公文 XML 描述

### 11.1 概述

采用可扩展置标语言(XML)对电子公文的结构进行描述。

### 11.2 电子公文

XML 标记: 电子公文。

定义: 电子公文的 XML 根元素。命名空间为“http://www.egs.org.cn/eGovDoc”。

值域：不作要求。

DTD 定义：

<! ELEMENT 电子公文 (ANY*)>

## <! ATTLIST 电子公文

xmlns CDATA #FIXED "http://www.egs.org.cn/eGovDoc"

公文标识 CDATA #REQUIRED

版本号 CDATA #FIXED "1.0"

公文类别 CDATA #REQUIRED

公文种类 CDATA #REQUIRED

>

Schema 定义: 见表 3.

<div style="text-align: center;">表 3 电子公文 schema 定义</div>


层次模型<fcel>电子公文<fcel>any http://www.egs.org.cn/eGovDoc/body<nl><ucel><ucel><fcel>any http://www.egs.org.cn/eGovDoc/display<nl><ucel><ucel><fcel>any http://www.egs.org.cn/eGovDoc/exchange<nl><ucel><ucel><fcel>any http://www.egs.org.cn/eGovDoc/process<nl><ucel><ucel><fcel>any http://www.egs.org.cn/eGovDoc/archive<nl><ucel><ucel><fcel>any http://www.egs.org.cn/eGovDoc/security<nl><ucel><ucel><fcel>0. .*<nl><ucel><ucel><fcel>any ##any<nl><fcel>命名空间<fcel>http://www.egs.org.cn/eGovDoc<lcel><nl><fcel>属性列表<fcel>公文标识<fcel>版本号 公文类别 公文种类<nl><fcel>源代码<fcel><xs:element name="电子公文"><nl><ucel><fcel><xs:complexType><nl><ucel><fcel><xs:sequence><nl><ucel><fcel><xs:any namespace="http://www.egs.org.cn/eGovDoc/body"/><nl><ucel><fcel><xs:any namespace="http://www.egs.org.cn/eGovDoc/display" minOccurs="0"/><nl><ucel><fcel><xs:any namespace="http://www.egs.org.cn/eGovDoc/exchange" minOccurs="0"/><nl><ucel><fcel><xs:any namespace="http://www.egs.org.cn/eGovDoc/process" minOccurs="0"/><nl><ucel><fcel><xs:any namespace="http://www.egs.org.cn/eGovDoc/archive" minOccurs="0"/><nl><ucel><fcel><xs:any namespace="http://www.egs.org.cn/eGovDoc/security" minOccurs="0"/><nl><ucel><fcel><xs:any namespace="# # any" minOccurs="0" maxOccurs="unbounded" /><nl><ucel><fcel></xs:sequence><nl><fcel>源代码<fcel><xs:attribute name="公文标识" use="required"><nl><ucel><fcel><xs:simpleType><nl><ucel><fcel><xs:restriction base="xs:string"><nl><ucel><fcel><xs:pattern value=" $$ A-Z0-9 $$ \{9\}-\d{4}- $$ 1-9 $$ \d */"><nl><ucel><fcel></xs:restriction><nl><ucel><fcel></xs:simpleType><nl><ucel><fcel></xs:attribute><nl><ucel><fcel><xs:attribute name="版本号" type="xs:decimal" use="required" fixed="1.0"/><nl><ucel><fcel><xs:attribute name="公文类别" type="xs:string" use="required"/><nl><ucel><fcel><xs:attribute name="公文种类" type="xs:string" use="required"/><nl><ucel><fcel></xs:complexType><nl><ucel><fcel></xs:element><nl>

注：本部分各层次模型图中所用图型符号说明均参见附录 A。

#### 11.2.1 公文标识

XML 标记: 公文标识。

定义：记录用于唯一标识电子公文的一组编码，由主办机关的组织机构代码、年份和主办机关当年电子公文流水号组成，中间用“—”号隔开，即“组织机构代码—年份—主办机关当年电子公文流水号”，如“AAAAAAAAA-2004-1”。

值域：组织结构代码的取值符合 GB 11714—1997 的规定，年份和流水号用阿拉伯数码标识，年份应标全称，流水号不编虚位（即 1 不编为 001）。

#### 11.2.2 版本号

XML 标记: 版本号。

定义: 记录基于 XML 电子公文标准的版本编号。

值域：电子公文所采用的 XML Schema 或 DTD 的版本编号，本标准的版本号为“1.0”。

#### 11.2.3 公文类别

XML 标记: 公文类别。

定义: 记录公文主办机关的单位性质。

值域：以“党”或“行政”表示，扩展的类别必须是其他机关和团体的规范性简称。

#### 11.2.4 公文种类

XML 标记: 公文种类。

定义: 记录党政机关或其他机关公文的种类名称。

值域: 国家党政机关法定公文种类名称, 经扩展后, 亦可包括党政机关的其他公文种类及其他机关和团体的公文种类的规范名称。

附录 A

(资料性附录)

层次模型图中所用的图型符号说明

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_432_396_753_517.jpg" alt="Image" width="26%" /></div>


其中：

——图型符号 A 表示元素 A 为当前文档的根元素，图型符号 B 表示元素 B 为元素 A 的子元素。

——图型符号——表示内容模式遵守已定义的子元素顺序。

——图型符号 $ \frac{1.}{} $ 表示内容模式为从已定义的子元素中选择一个。图符上方的“1..*”表示该内容模式为一个到任意多个，缺省为一个。

——图型符号0. $ \cdot $  $ ^{*} $  $ ^{-} $  $ _{C} $  $ ^{-} $  $ _{1} $  $ _{1} $ 表示子元素C的个数为0到任意多个，虚线表示该子元素为可选项。

附录 B

(资料性附录)

### B.1 本部分协调员是

中央办公厅信息中心郭瑞明

国务院办公厅秘书一局技术处胡佳

中国电子技术标准化研究所吴志刚

### B.2 参与本部分制定的单位除了前言中提到的外还有

中央办公厅信息中心

国务院办公厅秘书一局技术处

中国标准化研究院

中国电子技术标准化研究所

中国科学技术信息研究所

中科院软件所电子商务中心

武汉大学

太极计算机公司

上海因特奈信息有限公司