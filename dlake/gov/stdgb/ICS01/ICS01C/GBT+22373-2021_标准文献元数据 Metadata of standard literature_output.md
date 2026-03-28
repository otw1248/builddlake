

# 中华人民共和国国家标准

GB/T 22373—2021

代替 GB/T 22373—2008

# 标准文献元数据

# Metadata of standard literature

2021-03-09 发布

2021-10-01 实施

## 目次

前言 …… I  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 标准文献元数据的描述方法 …… 2  
  
4.1 摘要表示 …… 2  
  
4.2 字典表示 …… 3  
  
5 标准文献元数据构成 …… 4  
  
6 标准文献核心元数据 …… 4  
  
6.1 概述 …… 4  
  
6.2 标准文献核心元数据的摘要表示 …… 5  
  
6.3 标准文献核心元数据的字典表示 …… 7  
  
7 标准文献公共元数据 …… 8  
  
7.1 概述 …… 8  
  
7.2 标准文献公共元数据的摘要表示 …… 11  
  
附录 A（规范性附录） 标准文献实体元数据与标准文献元数据代码集 …… 21  
  
附录 B（资料性附录） 常用标准文献元数据表 …… 27  
  
参考文献 …… 31

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准代替 GB/T 22373—2008《标准文献元数据》，与 GB/T 22373—2008 相比主要技术变化如下：

——扩充了平台建设所需的元数据与标准文献实体管理所需的元数据。本标准修订中新增了8项

元数据：发布单位代码、前言、引言、卷期号、出版周期、标引依据、标准历史、参建单位。在规范

性附录中新增了标准实体管理元数据，包括：标准实体元数据、标准实体是否译文、标准实体载

体形态、标准实体功能种类、标准实体是否合订。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别这些专利的责任。

本标准由中华人民共和国科学技术部提出。

本标准由全国科技平台标准化技术委员会(SAC/TC 486)归口。

本标准起草单位:中国标准化研究院、国家科技基础条件平台中心、广州市标准化研究院、深圳市标准技术研究院。

本标准主要起草人：周洁、李爱仙、汪滨、程女范、李景、黄海、肖永舒、吕勇、周琼琼、许东惠、李菁、刘恬渊。

本标准所代替标准的历次版本发布情况为：

——GB/T 22373—2008.

# 标准文献元数据

## 1 范围

本标准规定了标准文献数据集合的基本元数据，给出了标准文献核心元数据、公共元数据的定义及其表示方法。

本标准适用于各类标准文献数据集合的加工、整理、建库、汇编、发布和查询。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 788—1999 图书和杂志开本及其幅面尺寸

GB/T 2659 世界各国和地区名称代码

GB/T 3469 信息资源的内容形式和媒体类型标识

GB/T 4880.1 语种名称代码 第1部分：2字母代码

GB/T 4880.2 语种名称代码 第2部分：3字母代码

GB/T 7156 文献保密等级代码与标识

GB/T 7408 数据元和交换格式 信息交换 日期和时间表示法

中国标准文献分类法

国际标准分类法

标准文献主题词表

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 数据集 dataset

可以标识的数据集合。

注：数据集在物理上可以是更大数据集的比较小的数据组。从理论上讲，数据集可以小到更大数据集内的单个要素或要素属性。

### 3.2 

数据集系列 dataset series

符合相同产品规范的数据集集合。

### 3.3 

元数据 metadata

定义和描述其他数据的数据。

### 3.4 

## 元数据元素 metadata element

元数据的基本单元。

注：元数据元素在元数据实体中是唯一的。

### 3.5 

## 元数据实体 metadata entity

一组说明数据相同特性的元数据元素。

注：可以包含一个或一个以上元数据实体。

### 3.6 

## 元数据子集 metadata section

元数据的子集合，由相关的元数据实体和元素组成。

### 3.7 

## 核心元数据 core metadata

在特定的领域中，用于描述数据集（信息资源）最基本属性的元数据，是制定其元数据标准时必须选择的或有条件必须元数据实体和元数据元素。

### 3.8 

## 公共元数据 common metadata

在特定的领域中，具有共性的元数据。

注 $ ^{1} $ ：公共元数据包含核心元数据的全部内容，是特定领域在制定其元数据标准时的工作起点。

注 2：描述标准文献实体的标准实体元数据见附录 A 的 A.7～A.11。

### 3.9 

## 著录 description

对文献的内容和形式特征进行分析、选择和记录的过程。

### 3.10 

## 母体文献 parent document

包含所著录文献的整体文献或收录所著录文献的文献合集实体。

## 4 标准文献元数据的描述方法

### 4.1 摘要表示

#### 4.1.1 概述

摘要表示使用名称、定义、英文名称、数据类型、值域、注解来描述元数据。

#### 4.1.2 名称

名称是赋给元数据实体或元数据元素的一个标记。

元数据实体名称以一个大写字母开头。元数据实体名称应由多个单词连写组成，中间不应有空格，每个单词的首字母应为大写字母（如：XnnnYmmm）。元数据实体名称在本标准的数据字典中应是唯一的。

元数据元素名称在元数据实体中应是唯一的，但在本标准的数据字典中并不是唯一的。通过元数据实体和元数据元素名称的组合，可使元数据元素名称在一个应用中唯一（如：元数据.元数据元素名称）。

#### 4.1.3 定义

描述元数据的基本内容。

#### 4.1.4 英文名称

元数据的英文名称一般用英文全称。

#### 4.1.5 数据类型

元数据的有效值域和允许对该值域内的值进行有效操作的规定。例如整型、实型、布尔型、字符型、日期等。

#### 4.1.6 值域

对元数据元素而言，值域说明其有效值或使用自由文本。“自由文本”表明对字段的内容没有限制。

#### 4.1.7 注解

##### 4.1.7.1 约束/条件

约束/条件是元数据实体或元数据元素选取的属性，包括必选（M）、可选（O）和条件必选（C）。约束/条件代码见表1。

<div style="text-align: center;">表 1 约束/条件代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>M</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>表明该元数据实体或元数据元素必须选择</td></tr><tr><td style='text-align: center;'>O</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>根据实际应用可以选择也可以不选的元数据实体或元数据元素。已经定义的可选元数据实体和可选元数据元素，可指导领域元数据标准制定人员充分说明其数据。可选元数据实体可以有必选元素；但这些元素仅在可选实体被选用时才成为必选的。如果一个可选元数据实体未被选用，则该实体所包含的元素（包括必选元素）也不选用</td></tr><tr><td style='text-align: center;'>C</td><td style='text-align: center;'>条件必选</td><td style='text-align: center;'>选择该元数据实体或元素的条件，当该条件满足时，至少一个元数据实体或元数据元素必选。“条件必选”用于以下三种可能性之一：a）在2个或2个以上元数据实体或元数据元素中进行选择，至少存在一个元数据实体或元数据元素必选；b）当已经选用另一个元数据实体或元数据元素时，此元数据实体或元数据元素为必选；c）当另一个元数据元素已经选择了一个特定值时，此元数据元素为必选</td></tr></table>

##### 4.1.7.2 最大出现次数

最大出现次数是元数据实体或元数据元素可以具有的最大实例数目。实例数目为固定出现次数的用相应的数字表示，如“1”“2”“3”“4”等。实例数目不确定重复出现的用“N”表示。

### 4.2 字典表示

#### 4.2.1 概述

数据字典以表格形式描述元数据的特征属性。数据字典通过以下 7 个属性定义元数据实体和元数据元素。

#### 4.2.2 标识符

标识符是用来表示元数据元素的唯一代码。

#### 4.2.3 名称

按 4.1.2 给出的要求。

#### 4.2.4 定义

描述元数据的基本内容。

#### 4.2.5 约束/条件

按 4.1.7.1 给出的要求。

#### 4.2.6 最大出现次数

最大出现次数是元数据实体或元数据元素可以具有的最大实例数目。实例数目为固定出现次数的用相应的数字表示，如“1”“2”“3”“4”等。实例数目不确定重复出现的用“N”表示。

#### 4.2.7 数据类型

元数据的有效值域和允许对该值域内的值进行有效操作的规定。例如整型、实型、布尔型、字符型、日期等。

#### 4.2.8 值域

对元数据元素而言，值域说明其有效值或使用自由文本。“自由文本”表明对字段的内容没有限制。

## 5 标准文献元数据构成

标准文献元数据由标准文献核心元数据和标准文献公共元数据组成。标准文献核心元数据是各类标准文献元数据标准的基础。

## 6 标准文献核心元数据

### 6.1 概述

标准文献核心元数据元素包括 11 个必选元数据和 3 个条件必选元数据元素（即数据元），可用于标准文献数据集编目、数据交换、网站活动和对最基本数据集的描述。

标准文献核心元数据内容见表2。

<div style="text-align: center;">表 2 标准文献核心元数据内容</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>000</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>001</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>101</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>102</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>200</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>必选</td></tr></table>

## 表 2（续）


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>205</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>207</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>298</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>301</td><td style='text-align: center;'>原文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>302</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>462</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>820</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>823</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>必选</td></tr></table>

### 6.2 标准文献核心元数据的摘要表示

#### 6.2.1 记录状态

定义: 关于标准文献数据库中记录所处的状态(修改、删除、新增)的说明。

英文名称: record status

数据类型: 字符型

值域:采用表A.1的代码

注 解:必选项;最大出现次数为1。

#### 6.2.2 记录识别符

定义: 建立记录的单位对某一记录的给定的唯一识别符号。

英文名称: record identifier

数据类型: 字符型

值域：6位阿拉伯数字序号

注 解:必选项;最大出现次数为1。

#### 6.2.3 标准号

定义:由有关标准化机构给定的用于唯一识别某一标准的注册号或登记号,标准号由标准代号、顺序号、发布年份及有关标识符组成。

英文名称: document reference

数据类型: 字符型

值域：标准代号+1个空格+顺序号+1个连字符“−”+4位发布年份

注 解:必选项;最大出现次数为1。

#### 6.2.4 发布日期

定义: 标准经有关机构批准, 予以发布的日期。

英文名称: date of announcement

数据类型: 字符型

值域:采用 YYYY-MM-DD 格式

注 解:必选项;最大出现次数为1。

#### 6.2.5 发布机构

定义: 公布所著录标准的单位。

英文名称: announcing body

数据类型: 字符型

值域: 发布机构的全称或公认的简称

注 解:必选项;最大出现次数为 N。

#### 6.2.6 标准状态

定义: 标准文献所处的状态或属性, 说明所著录标准是草案、试行、暂行、废止或其他状态。

英文名称: document status

数据类型: 字符型

值域：按所著录标准或其发布机构的通报和目录所标明的符号著录标准状态代码

注 解:必选项;最大出现次数为1。

#### 6.2.7 实施或试行日期

定义: 标准经有关机构批准后正式生效或试行的日期。

英文名称: effective date

数据类型: 字符型

值域:采用 YYYY-MM-DD 格式

注 解:必选项;最大出现次数为1。

#### 6.2.8 确认日期

定义:标准经重审确认继续有效的日期。

英文名称: confirmation date

数据类型: 字符型

值域：采用 YYYY-MM-DD 格式。多个确认日期之间以半角分号“;”相隔

注 解:必选项;最大出现次数为 N。

#### 6.2.9 中文标准名称

定义:标准的中文名称或中文译名。

英文名称: document name in Chinese

数据类型: 字符型

值域：自由文本（中国标准应著录中文标准名称；国外标准应著录标准的中文译名）

注 解:条件必选项;最大出现次数为1,中文标准名称、英文标准名称和原文标准名称应至少存在一个必选。

#### 6.2.10 原文标准名称

定义：中、英文以外语种的标准名称。

英文名称: original document name

数据类型: 字符型

值域:自由文本

注 解:条件必选项;最大出现次数为1,中文标准名称、英文标准名称和原文标准名称应至少存在一个必选。

#### 6.2.11 英文标准名称

定义:标准的英文名称或英文译名。

英文名称: document name in English

数据类型: 字符型

值域：自由文本（中国标准应著录标准的英文译名；国外标准应著录标准的英文名称）

注 解:条件必选项;最大出现次数为1,中文标准名称、英文标准名称和原文标准名称应至少存在一个必选。

#### 6.2.12 被代替标准

定义：所著录标准代替的标准。

英文名称: replaces

数据类型: 字符型

值域：著录被代替标准的标准号，有多个被代替标准时，各标准号之间以半角分号“；”相隔。

某标准部分内容被所著录标准代替时，应在被代替标准号后加相关说明文字并用括号包含

注 解:必选项;最大出现次数为 N。

#### 6.2.13 修改件

定义: 修改所著录标准的文献的代号、总次和总次发布年份的说明。

英文名称: amended by

数据类型: 字符型

值域：著录修改件代号、总次和总次发布年份，总次和发布年份之间以半角逗号“，”相隔

注 解:必选项;最大出现次数为 N。

#### 6.2.14 补充件

定义: 补充所著录标准的文献的代号、总次和总次发布年份的说明。

英文名称: supplemented by

数据类型: 字符型

值域：著录补充件代号、总次和总次发布年份，总次和发布年份之间以半角逗号“，”相隔

注 解:必选项;最大出现次数为 N。

### 6.3 标准文献核心元数据的字典表示

标准文献核心元数据的字典表示见表3。

<div style="text-align: center;">表 3 标准文献核心元数据的字典表示</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值域</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>关于标准文献数据库中记录所处的状态（修改、删除、新增）的说明</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>表A.1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>建立记录的单位对某一记录给定的唯一识别符号</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>由有关标准化机构给定的用于唯一识别某一标准的注册号或登记号，标准号由标准代号、顺序号、发布年份及有关标识符组成</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>标准经有关机构批准，予以发布的日期</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>YYYY-MM-DD</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>发布标准的机构</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>标准文献所处的状态</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>标准经有关机构批准后，正式生效或试行的日期</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>YYYY-MM-DD</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>标准经重审确认继续有效的日期</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>YYYY-MM-DD</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>标准文献的中文名称或中文译名</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>原文标准名称</td><td style='text-align: center;'>中、英文以外的标准正文语种的标准名称</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>标准的英文名称或英文译名</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>所著录标准代替的标准</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>修改所著录文献的文献代号、总次和总次发布年份的说明</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>补充所著录文献的文献代号、总次和总次发布年份的说明</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>自由文本</td></tr></table>

## 7 标准文献公共元数据

### 7.1 概述

标准文献公共元数据元素包括 14 个必选元数据、48 个可选元数据和 6 个条件必选元数据元素（即数据元），可用于标准文献数据集编目、数据交换网站活动和对共性数据集的描述。

各类标准文献元数据标准应包含标准文献核心元数据，并可依据领域和专业自身特点在标准文献公共元数据的基础上进行扩展和裁减(参见附录 B)

标准文献公共元数据内容见表4。

<div style="text-align: center;">表 4 标准文献公共元数据内容</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>000</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>001</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>003</td><td style='text-align: center;'>记录日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>010</td><td style='text-align: center;'>ISBN</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>011</td><td style='text-align: center;'>ISSN</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>100</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>101</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>102</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>104</td><td style='text-align: center;'>发布机构代码</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>103</td><td style='text-align: center;'>版本</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>200</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>203</td><td style='text-align: center;'>有效区域</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>204</td><td style='text-align: center;'>批准单位</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>205</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>206</td><td style='text-align: center;'>废止日期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>207</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>208</td><td style='text-align: center;'>原分类号</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>209</td><td style='text-align: center;'>起草单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>210</td><td style='text-align: center;'>截止日期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>298</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>300</td><td style='text-align: center;'>正文语种</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>301</td><td style='text-align: center;'>原文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>302</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>304</td><td style='text-align: center;'>出版单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>305</td><td style='text-align: center;'>稽核项</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>309</td><td style='text-align: center;'>译文</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>310</td><td style='text-align: center;'>价格</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>311</td><td style='text-align: center;'>其他载体</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>330</td><td style='text-align: center;'>中文文摘</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>331</td><td style='text-align: center;'>英文文摘</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>390</td><td style='text-align: center;'>英文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>409</td><td style='text-align: center;'>附注</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>448</td><td style='text-align: center;'>文献出处</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>461</td><td style='text-align: center;'>代替标准</td><td style='text-align: center;'>可选</td></tr></table>

<div style="text-align: center;">表 4（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>462</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>502</td><td style='text-align: center;'>引用文件</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>505</td><td style='text-align: center;'>相关法律</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>800</td><td style='text-align: center;'>一致性程度</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>805</td><td style='text-align: center;'>第二标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>807</td><td style='text-align: center;'>前言</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>808</td><td style='text-align: center;'>引言</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>820</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>821</td><td style='text-align: center;'>被修改件</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>823</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>824</td><td style='text-align: center;'>被补充件</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>825</td><td style='text-align: center;'>中国标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>826</td><td style='text-align: center;'>国际标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>48</td><td style='text-align: center;'>835</td><td style='text-align: center;'>中文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>840</td><td style='text-align: center;'>中文自由词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>837</td><td style='text-align: center;'>原文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>845</td><td style='text-align: center;'>索取号</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>846</td><td style='text-align: center;'>馆藏标志</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>847</td><td style='text-align: center;'>排序码</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>850</td><td style='text-align: center;'>标准类型</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>860</td><td style='text-align: center;'>文献类型</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>861</td><td style='text-align: center;'>卷期号</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>863</td><td style='text-align: center;'>文献代号</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>864</td><td style='text-align: center;'>出版周期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>865</td><td style='text-align: center;'>出版地</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>60</td><td style='text-align: center;'>866</td><td style='text-align: center;'>密级</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>870</td><td style='text-align: center;'>提出单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>871</td><td style='text-align: center;'>归口单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>885</td><td style='text-align: center;'>国别</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>886</td><td style='text-align: center;'>标引依据</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>65</td><td style='text-align: center;'>890</td><td style='text-align: center;'>更新批号</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>66</td><td style='text-align: center;'>891</td><td style='text-align: center;'>标准历史</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>67</td><td style='text-align: center;'>892</td><td style='text-align: center;'>参建单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>68</td><td style='text-align: center;'>893</td><td style='text-align: center;'>电子文件名称</td><td style='text-align: center;'>可选</td></tr></table>

### 7.2 标准文献公共元数据的摘要表示

#### 7.2.1 记录状态

按 6.2.1 的要求。

#### 7.2.2 记录识别符

按 6.2.2 的要求。

#### 7.2.3 记录日期

定义：建立记录的日期。

英文名称: date of record

数据类型: 字符型

值域：按 GB/T 7408 的规定著录，采用 YYYY-MM-DD 格式

注 解:必选项;最大出现次数为1。

#### 7.2.4 ISBN

定义: 国际标准书号。由文献出版单位给定的唯一标识某文献的国际统一书号。

英文名称: International Standard Book Number

数据类型: 字符型

值域：著录文献的国际标准书号，不包括其代号“ISBN”

注 解: 可选项; 最大出现次数为 1。

#### 7.2.5 ISSN

定义: 国际标准连续出版物编号。由文献出版单位给定的唯一标识某文献的国际统一连续出版物编号。

英文名称: International Standard Serial Number

数据类型: 字符型

值域：著录文献的国际连续出版物编号，不包括其代号“ISSN”

注 解: 可选项; 最大出现次数为 1。

#### 7.2.6 标准号

按 6.2.3 的要求。

#### 7.2.7 发布日期

按 6.2.4 的要求。

#### 7.2.8 发布机构

按 6.2.5 的要求。

#### 7.2.9 发布机构代码

定义: 公布所著录标准的单位的代码。

英文名称: code of announcing body

数据类型: 字符型

值域：唯一识别发布机构的编码。按 A.2 给出的要求

注 解:条件必选;最大出现次数为1。

#### 7.2.10 版本

定义: 标准出版的版次或其他版本形式说明。

英文名称:edition

数据类型: 字符型

值域：仅限于第二版及其以后的版次说明。著录时可省略第×版中反映版次序列的“第”等说明文字。例：第二版，著录为：2版；修改版，著录为：修改版；Second edition，著录为：2ed 注解：可选项；最大出现次数为1。

#### 7.2.11 标准状态

按 6.2.6 的要求。

#### 7.2.12 有效区域

定义: 标准文献所适用的地域。

英文名称: area of validity

数据类型: 字符型

值域：著录有效区域名称

注 解: 可选项; 最大出现次数为 1。

#### 7.2.13 批准单位

定义: 标准的审查批准单位。

英文名称: validating body

数据类型: 字符型

值域：著录批准单位的全称或公认的简称

注 解:必选项;最大出现次数为1。

#### 7.2.14 实施或试行日期

按 6.2.7 的要求。

#### 7.2.15 废止日期

定义: 标准作废的日期。

英文名称:withdrawal date

数据类型: 字符型

值域:采用 YYYY-MM-DD 格式

注 解: 可选项; 最大出现次数为 1。

#### 7.2.16 确认日期

按 6.2.8 的要求。

#### 7.2.17 原分类号

定义: 标准发布机构给定的分类号或其他专业分类号。

英文名称: original notation

数据类型: 字符型

值域：按原形式著录，有多个分类号时，各分类号之间以半角分号“；相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.18 起草单位

定义: 起草标准的单位名称。

英文名称:drafting body

数据类型: 字符型

值域：起草单位的全称或公认的简称，各起草单位之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.19 截止日期

定义: 标准发布时所规定的标准有效期限的终止日期。

英文名称: date of expiration

数据类型: 字符型

值域:采用 YYYY-MM-DD 格式

注 解: 可选项; 最大出现次数为 1。

#### 7.2.20 中文标准名称

按 6.2.9 的要求。

#### 7.2.21 正文语种

定义: 标准正文所用文字的语种。

英文名称:text language

数据类型: 字符型

值域：按照 GB/T 4880.1 和 GB/T 4880.2 的规定著录所用语种的代码

注 解: 可选项; 最大出现次数为 N。

#### 7.2.22 原文标准名称

按 6.2.10 的要求。

#### 7.2.23 英文标准名称

按 6.2.11 的要求。

#### 7.2.24 出版单位

定义：出版标准的单位名称。

英文名称: publishing body

数据类型: 字符型

值域:出版单位的全称或公认的简称

注 解: 可选项; 最大出现次数为 1。

#### 7.2.25 稽核项

定义：关于标准文献有字面的总页数、开本的说明。

英文名称: collation

数据类型: 字符型

值域：自由文本（页数用××P.表示，开本按照GB/T 788—1999的规定著录。稽核项中各小项之间以半角分号“；”相隔）

注 解: 可选项; 最大出现次数为 1。

#### 7.2.26 译文

定义: 标准译文版本说明。

英文名称: translation

数据类型: 字符型

值域:按照 GB/T 4880.1 的规定著录所用语种的代码

注 解: 可选项; 最大出现次数为 N。

#### 7.2.27 价格

定义: 标准文献价格或价格组别。

英文名称: price

数据类型: 字符型

值域：著录标准文献的价格或价格组代码与币种标识

注 解: 可选项; 最大出现次数为 N。

#### 7.2.28 其他载体

定义: 标准文献实体除纸版载体以外的其他载体形态。

英文名称: other mediums

数据类型: 字符型

值域：按照 A.9 的规定著录

注 解: 可选项; 最大出现次数为 N。

#### 7.2.29 中文文摘

定义: 标准文献的中文内容摘要。

英文名称: abstract in Chinese

数据类型: 字符型

值域：著录概要反映标准文献主题内容与适用范围的文字

注 解: 可选项; 最大出现次数为 1。

#### 7.2.30 英文文摘

定义: 标准文献的英文内容摘要。

英文名称: abstract in English

数据类型: 字符型

值域：著录概要反映标准文献主题内容与适用范围的文字

注 解: 可选项; 最大出现次数为 1。

#### 7.2.31 英文主题词

定义: 反映标准文献主题内容的英文规范词。

英文名称: descriptor in English

数据类型: 字符型

值域：采用《标准文献主题词表》中的英文主题词，各主题词之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.32 附注

定义: 对所著录标准进行的补充说明。

英文名称: general note

数据类型: 字符型

值域:该项内容应是著录标准正文的各项中没有被反映的材料,如标准首次发布时间、标准更正及勘误情况等

注 解: 可选项; 最大出现次数为 1。

#### 7.2.33 文献出处

定义: 母体文献的标识。

英文名称: document source

数据类型: 字符型

值域: 著录母体文献的题名与责任项及出版项等的主要信息

注 解: 可选项; 最大出现次数为 N。

#### 7.2.34 代替标准

定义:代替所著录标准的标准。

英文名称:replaced by

数据类型: 字符型

值域：著录代替标准的标准号。有多个代替标准时，各标准号之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.35 被代替标准

按 6.2.12 的要求。

#### 7.2.36 引用文件

定义: 被著录标准所涉及的内容在有关标准中已有规定, 为避免重复, 对有关文件直接引用。

英文名称:referenced by

数据类型: 字符型

值域：著录引用文件的代号。有多个引用文件时，各引用文件号之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.37 相关法律

定义：对所发布标准进行授权的法律。

英文名称: regulations referred to

数据类型: 字符型

值域：著录有关部门和法律文件的文字或代码

注 解: 可选项; 最大出现次数为 N。

#### 7.2.38 一致性程度

定义: 所著录标准在技术内容上采用其他标准的标准号及一致性程度的标识。

英文名称: adoption

数据类型: 字符型

值域：采用其他标准的标准号+半角逗号“，”+一致性程度代码，有多个采用关系时，各采用关系之间以半角分号“；”相隔。一致性程度代码按照A.3的规定著录

注 解: 可选项; 最大出现次数为 N。

#### 7.2.39 第二标准号

定义: 所著录标准有多个标准号时, 其第二个及以上的标准号。

英文名称: second document reference

数据类型: 字符型

值域：标准代号+1个空格+顺序号+1个连字符“−”+4位发布年份。

有多个标准号时，各标准号之间以半角分号“；”相隔

注 解:必选项;最大出现次数为 N。

#### 7.2.40 前言

定义：所著录标准的前言。

英文名称: preface

数据类型: 字符型

值域: 自由文本

注 解: 可选项; 最大出现次数为 1。

#### 7.2.41 引言

定义：所著录标准的引言。

英文名称: introduction

数据类型: 字符型

值域：自由文本

注 解: 可选项; 最大出现次数为 1。

#### 7.2.42 修改件

按 6.2.13 的要求。

#### 7.2.43 被修改件

定义: 被所著录文件修改的标准。

英文名称: amends

数据类型: 字符型

值域: 被修改标准的标准号

注 解: 可选项; 最大出现次数为 N。

#### 7.2.44 补充件

按 6.2.14 的要求。

#### 7.2.45 被补充件

定义：被所著录文件补充的标准。

英文名称: supplement

数据类型: 字符型

值域：著录被补充标准的标准号

注 解: 可选项; 最大出现次数为 N。

#### 7.2.46 中国标准分类号

定义：标准的《中国标准文献分类法》分类号。

英文名称:CCS number

数据类型: 字符型

值域：《中国标准文献分类法》的分类号。有多个分类号时，各分类号之间以半角分号“；”相隔

注 解：条件必选项；最大出现次数为 N，中国标准分类号和国际标准分类号至少存在一个必选。

#### 7.2.47 国际标准分类号

定义：标准的《国际标准分类法》分类号。

英文名称: ICS number

数据类型: 字符型

值域：《国际标准分类法》的分类号。有多个分类号时，各分类号之间以半角分号“；”相隔

注 解:条件必选项;最大出现次数为 N,中国标准分类号和国际标准分类号至少存在一个必选。

#### 7.2.48 中文主题词

定义: 反映标准文献主题内容的中文规范词。

英文名称: descriptor in Chinese

数据类型: 字符型

值域：采用《标准文献主题词表》中的中文主题词，各主题词之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.49 中文自由词

定义: 直接从文献中抽出的作为文献检索标识的中文词语或字符。

英文名称：free descriptor in Chinese

数据类型: 字符型

值域：自由文本，各自由词之间以半角分号“；相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.50 原文主题词

定义：除中、英文以外语种反映标准文献主题内容的原文规范词。

英文名称: descriptor of original language

数据类型: 字符型

值域：各主题词之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.51 索取号

定义: 文献收藏单位的索书号。

英文名称:access number

数据类型: 字符型

值域：所著录标准的索取号

注 解: 可选项; 最大出现次数为 N。

#### 7.2.52 馆藏标志

定义：所著录标准是否有馆藏的说明。

英文名称: stock sign

数据类型: 字符型

值域：0：无馆藏，1：有馆藏

注 解: 可选项; 最大出现次数为 1。

#### 7.2.53 排序码

定义：为按标准号排序而生成的代码。

英文名称: sorting code

数据类型: 字符型

值域:无限定

注 解: 可选项; 最大出现次数为 1。

#### 7.2.54 标准类型

定义: 反映所著录标准的标准化对象类别的代码。

英文名称: type of standard

数据类型: 字符型

值域:按照 A.4 的规定著录

注 解: 可选项; 最大出现次数为 1。

#### 7.2.55 文献类型

定义: 文献的种类。

英文名称: document type

数据类型: 字符型

值域：按照 GB/T 3469 中的字母代码著录，见 A.5 文献类型代码。

注 解: 可选项; 最大出现次数为 1。

#### 7.2.56 卷期号

定义: 分卷出版的文献的卷期编号。

英文名称: number of volume

数据类型: 字符型

值域:无限定

注 解: 可选项; 最大出现次数为 1。

#### 7.2.57 文献代号

定义: 标准文献发布机构赋予本类标准的统一代号。

英文名称: document code

数据类型: 字符型

值域:无限定

注 解: 可选项; 最大出现次数为 1。

#### 7.2.58 出版周期

定义: 连续出版的文献的出版周期。

英文名称: period of publication

数据类型: 字符型

值域:无限定

注 解: 可选项; 最大出现次数为 1。

#### 7.2.59 出版地

定义: 标准出版单位所在地。

英文名称: place of publication

数据类型: 字符型

值域：文献出版地名称

注 解: 可选项; 最大出现次数为 1。

#### 7.2.60 密级

定义：文献的保密等级。

英文名称: confidentiality

数据类型: 字符型

值域:按照 GB/T 7156 的规定著录

注 解: 可选项; 最大出现次数为 1。

#### 7.2.61 提出单位

定义: 提出标准的单位的名称。

英文名称: proposer

数据类型: 字符型

值域: 提出单位的全称或公认的简称

注 解: 可选项; 最大出现次数为 N。

#### 7.2.62 归口单位

定义: 标准的技术归口单位的名称。

英文名称: mirror body

数据类型: 字符型

值域：归口单位的全称或公认的简称

注 解: 可选项; 最大出现次数为 1。

#### 7.2.63 国别

定义: 标准文献的批准发布机构所属的国家或地区。

英文名称:country

数据类型: 字符型

值域：国别按照 GB/T 2659 的 2 字母国家代码著录，国际区域性标准著录代码“IX”

注 解: 可选项; 最大出现次数为 1。

#### 7.2.64 标引依据

定义: 标引或修改当前记录的依据。

英文名称：according to

数据类型: 字符型

值域：自由文本，各自由词之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.65 更新批号

定义: 更新数据的批次号。

英文名称: update batch number

数据类型: 字符型

值域：采用更新数据的年月号作为更新批号，年代取后2位，月份取2位，即YYMM格式

注 解: 可选项; 最大出现次数为 1。

#### 7.2.66 标准历史

定义:标准的首次发布到本版标准的沿革信息。

英文名称：history of standard

数据类型: 字符型

值域：标准号或文献题名及相关描述，各部分之间以半角分号“；”相隔

注 解: 可选项; 最大出现次数为 N。

#### 7.2.67 参建单位

定义: 标准文献数据建设单位。

英文名称：unit for data processing

数据类型: 字符型

值域：自由文本。按照 A.6 的规定著录

注 解: 可选项; 最大出现次数为 N。

#### 7.2.68 电子文件名称

定义: 标准文献电子版的文件名称。

英文名称：name of electronic format document

数据类型: 字符型

值域：电子文件存储许可的字符。按照标准号命名电子文件名称，其中斜线“/”用下划线“_”代替

注 解：可选项；最大出现次数为 N。

# 附录 A

# (规范性附录)

# 标准文献实体元数据与标准文献元数据代码集

### A.1 记录状态代码

说明：标准文献数据库中记录所处状态（新增、修改、删除）的标识代码。

表示：1位字母码。

编码方法：采用英文缩略码，用1位大写英文字母表示。

记录状态代码见表 A.1。

<div style="text-align: center;">表 A.1 记录状态代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>A</td><td style='text-align: center;'>修改</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>D</td><td style='text-align: center;'>删除</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>N</td><td style='text-align: center;'>新增</td><td style='text-align: center;'></td></tr></table>

### A.2 发布机构代码

说明：标准发布机构代码由国别代码＋标准代号或发布机构缩写构成，是为了对标准品种进行管理、检索与统计分析的唯一代码。中国地方法规用代号“FG”＋地方代码表示。如“FG11”等。中国团体标准用团体标准代号“T/”＋社会团体标准代码表示。国际标准用“IX”表示。

表示：字母+代号。

编码方法：双位数国别代码+1个连字符“—”+标准代号。

发布机构代码示例见表 A.2。

<div style="text-align: center;">表 A.2 标准发布机构代码示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>CN-JB</td><td style='text-align: center;'>中国机械行业</td><td style='text-align: center;'>中国机械行业标准</td></tr><tr><td style='text-align: center;'>CN-GB</td><td style='text-align: center;'>国家市场监督管理总局</td><td style='text-align: center;'>中国国家标准</td></tr><tr><td style='text-align: center;'>CN-DB11</td><td style='text-align: center;'>北京市市场监督管理局</td><td style='text-align: center;'>中国北京地方标准</td></tr><tr><td style='text-align: center;'>CN-FG11</td><td style='text-align: center;'>中国北京地方法规发布机构</td><td style='text-align: center;'>中国北京地方法规</td></tr><tr><td style='text-align: center;'>IX-ISO</td><td style='text-align: center;'>国际标准化组织</td><td style='text-align: center;'>国际标准</td></tr><tr><td style='text-align: center;'>UK-BS</td><td style='text-align: center;'>英国标准协会</td><td style='text-align: center;'>英国国家标准</td></tr><tr><td style='text-align: center;'>US-UL</td><td style='text-align: center;'>美国保险商实验室</td><td style='text-align: center;'>美国保险商实验室标准</td></tr></table>

### A.3 一致性程度代码

说明：所著录标准与对应标准相互的一致性程度的标识代码。

表示：3位字母码。

编码方法：采用英文缩略语码，用3位大写英文字母表示。

标准一致性程度代码见表 A.3。

<div style="text-align: center;">表 A.3 标准一致性程度代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>IDT</td><td style='text-align: center;'>等同</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>MOD</td><td style='text-align: center;'>修改</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>NEQ</td><td style='text-align: center;'>非等效</td><td style='text-align: center;'></td></tr></table>

### A.4 标准类型代码

说明：所著录标准的标准化方面类别的代码。

表示：2位字母码。

编码方法:除完整的产品标准外,代码采用标准对象中文名称的2字缩略语的汉语拼音首字母表示(即2位大写英文字母)。

注 $ ^{1} $ ：标准分为若干部分时，根据各部分的内容划定标准对象类别。

注2：当标准对象涉及不同类别时，以其主要对象确定类别，不能同时反映几种类别，以避免重复。

标准类型代码见表 A.4。

<div style="text-align: center;">表 A.4 标准类型代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>CP</td><td style='text-align: center;'>产品标准</td><td style='text-align: center;'>完整的产品标准，至少包含产品质量要求、结构形式参数、试验方法及有关安全、环保、卫生等内容的标准</td></tr><tr><td style='text-align: center;'>CZ</td><td style='text-align: center;'>产品质量标准</td><td style='text-align: center;'>指某种（或某类）产品质量、性能要求方面的标准，如技术条件、技术要求、性能参数，以及与质量有关的安全、卫生指标的标准</td></tr><tr><td style='text-align: center;'>CF</td><td style='text-align: center;'>产品方法标准</td><td style='text-align: center;'>指某种（或某类）产品的方法标准，如试验、检验方法、测定方法、采样方法、评定方法等</td></tr><tr><td style='text-align: center;'>CJ</td><td style='text-align: center;'>产品基础标准</td><td style='text-align: center;'>指某种（或某类）产品的基础性标准，如产品的形式、尺寸系列、型谱、型号、牌号、编号及名词术语等</td></tr><tr><td style='text-align: center;'>CA</td><td style='text-align: center;'>产品安全标准</td><td style='text-align: center;'>为保护人和物的安全为目的。对某种（或某类）产品制定的标准，如电器安全标准、机械设备安全要求等</td></tr><tr><td style='text-align: center;'>CW</td><td style='text-align: center;'>产品卫生标准</td><td style='text-align: center;'>为保护人的健康，对某种（或某类）产品制定的卫生要求标准，如食品卫生等</td></tr><tr><td style='text-align: center;'>CQ</td><td style='text-align: center;'>产品其他标准</td><td style='text-align: center;'>指产品标准中不宜列入上述各类的标准，如产品的包装、运输、贮存标准等</td></tr><tr><td style='text-align: center;'>TF</td><td style='text-align: center;'>通用方法标准</td><td style='text-align: center;'>指在生产、技术、经济活动中，一切与行为、动作有关并在全国或几个专业范围内通用的方法性标准，例如通用的试验、检验、检查、分析、抽样、统计、计算、测定、评定、操作、施工等有关的方法、规程标准</td></tr></table>

<div style="text-align: center;">表 A.4 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>TJ</td><td style='text-align: center;'>通用基础标准</td><td style='text-align: center;'>指在全国几个专业范围内作为其他标准的基础并普遍使用，具有广泛指导意义的基础性标准。例如为合理发展产品品种、确保产品质量、提高通用互换程度而制定的优选系数、额定电压与频率、机械制图、形位公差、公差配合、标准化工作指导性文件、科学技术名词术语等基础标准</td></tr><tr><td style='text-align: center;'>TA</td><td style='text-align: center;'>通用安全标准</td><td style='text-align: center;'>指以保护人和物的安全为目的而制定的通用标准，包括全国几个专业范围内通用的劳动安全技术、生产设备安全要求、防护防毒技术、物理因素危害控制及劳动保护管理方面的标准，如“高温作业分级”标准等</td></tr><tr><td style='text-align: center;'>TW</td><td style='text-align: center;'>通用卫生标准</td><td style='text-align: center;'>指以保护人的健康而制定的通用卫生要求标准，包括全国通用环境卫生、劳动卫生、场所卫生、防护卫生、职业病与公害病诊断、卫生检疫及人、兽防疫等标准</td></tr><tr><td style='text-align: center;'>AQ</td><td style='text-align: center;'>安全标准</td><td style='text-align: center;'>各类安全标准</td></tr><tr><td style='text-align: center;'>HB</td><td style='text-align: center;'>环境保护标准</td><td style='text-align: center;'>指为保护室外（厂外）环境和有利于生态平衡，对大气、水、土壤、噪声、振动环境质量、污染源、检测方法及其他事项制定的标准，包括环保基础标准、环保方法标准、环境质量标准、污染物排放标准及环境标准参考物质等</td></tr><tr><td style='text-align: center;'>JG</td><td style='text-align: center;'>建设工程标准</td><td style='text-align: center;'>指对基础建设中各类工程的勘察、规划、设计、施工、安装、验收等需要协调统一的事项所制定的标准，包括城市规划、工程勘察与测量、设计、施工及有关的供水、供电、供热、供气、防火、空调、设备安装等标准</td></tr><tr><td style='text-align: center;'>GL</td><td style='text-align: center;'>管理标准</td><td style='text-align: center;'>指对某一领域中需要协调统一的管理事项所制定的标准，包括技术管理、生产组织管理、经济管理、行政管理等工作标准</td></tr><tr><td style='text-align: center;'>QT</td><td style='text-align: center;'>其他标准</td><td style='text-align: center;'>凡不属于以上各类标准的其他类型标准均归此类</td></tr></table>

### A.5 文献类型代码

说明：标识标准文献类型的代码。

表示：2位字母码。

编码方法：按照 GB/T 3469 中的双字码标识文献类型。

文献类型代码见表 A.5。

<div style="text-align: center;">表 A.5 文献类型代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td></tr><tr><td style='text-align: center;'>HY</td><td style='text-align: center;'>会议文献</td></tr><tr><td style='text-align: center;'>XL</td><td style='text-align: center;'>学位论文</td></tr><tr><td style='text-align: center;'>SG</td><td style='text-align: center;'>手稿</td></tr><tr><td style='text-align: center;'>ZZ</td><td style='text-align: center;'>专著</td></tr><tr><td style='text-align: center;'>BZ</td><td style='text-align: center;'>报纸</td></tr><tr><td style='text-align: center;'>GJ</td><td style='text-align: center;'>古籍</td></tr><tr><td style='text-align: center;'>ZL</td><td style='text-align: center;'>专利文献</td></tr><tr><td style='text-align: center;'>QK</td><td style='text-align: center;'>期刊</td></tr></table>

<div style="text-align: center;">表 A.5 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td></tr><tr><td style='text-align: center;'>TP</td><td style='text-align: center;'>拓片</td></tr><tr><td style='text-align: center;'>JB</td><td style='text-align: center;'>标准文献</td></tr><tr><td style='text-align: center;'>BG</td><td style='text-align: center;'>技术报告</td></tr></table>

### A.6 参建单位代码

说明：参建单位代码是指参加建设数据库建设与信息整合的单位。

表示：参建单位代码由两部分组成。第一部分用代码“H”表示行业参建单位，代码“D”表示地方参建单位，“G”表示国家级参建单位，代码“Q”表示其他参建单位。第二部分由参建机构特性代码组成。行业参建单位由所发布标准代号组成，地方参建单位由省市拼音缩写组成，省以下单位由地区区号组成，国家或其他参建单位由其通用的缩写构成。

编码方法：为类型代码+1个连字符“—”+单位代码。

参建单位代码示例见表 A.6。

<div style="text-align: center;">表 A.6 参建单位代码示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>G-CNIS</td><td style='text-align: center;'>中国标准化研究院</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>H-JB</td><td style='text-align: center;'>机械科学研究院</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>D-JX</td><td style='text-align: center;'>江西省标准化研究院</td><td style='text-align: center;'></td></tr></table>

### A.7 标准实体元数据

说明: 标准文献数据库中对纸质文本、电子文本等标准正文实体进行管理所形成的元数据。一件标准可能存在多个实体。每个实体可能存在不同载体形态、不同语种、不同功能种类等诸多个性化属性要素，当需要对每个标准文献实体分别进行描述和管理维护时，就形成了标准实体元数据。每个实体元数据与标准题录记录产生关联，形成一对多的标准实体管理体系。

标准实体元数据见表 A.7。

<div style="text-align: center;">表 A.7 标准实体元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>RECORDID</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>按 6.2.2 给出的要求</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>LANGUAGE</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>按 7.2.21 给出的要求</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>TRANSTYLE</td><td style='text-align: center;'>是否译文</td><td style='text-align: center;'>按 A.8 给出的要求</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>PHYSICAL DESCP</td><td style='text-align: center;'>载体形态</td><td style='text-align: center;'>按 A.9 给出的要求</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>FUNCTYPE</td><td style='text-align: center;'>功能种类</td><td style='text-align: center;'>按 A.10 给出的要求</td></tr></table>

<div style="text-align: center;">表 A.7 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>PAGECOUNT</td><td style='text-align: center;'>页数</td><td style='text-align: center;'>按7.2.25给出的要求</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>PAGENUMRANGE</td><td style='text-align: center;'>页数范围</td><td style='text-align: center;'>在合订本中页码范围</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>SUMMARY</td><td style='text-align: center;'>实体附注</td><td style='text-align: center;'>对实体的补充说明</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>ENTITYNAME</td><td style='text-align: center;'>实体名称</td><td style='text-align: center;'>标准或合订本题名</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>PUBLISHER</td><td style='text-align: center;'>出版单位</td><td style='text-align: center;'>按7.2.24给出的要求</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>FORMATVALUE</td><td style='text-align: center;'>开本</td><td style='text-align: center;'>按7.2.25给出的要求</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>SINGLETYPE</td><td style='text-align: center;'>实体合订</td><td style='text-align: center;'>按A.11给出的要求</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>PRICE</td><td style='text-align: center;'>价格</td><td style='text-align: center;'>按7.2.27给出的要求</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>ACCESSNUMBER</td><td style='text-align: center;'>索取号</td><td style='text-align: center;'>按7.2.51给出的要求</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>BARCODE</td><td style='text-align: center;'>条码</td><td style='text-align: center;'>标准文本的馆藏条形码</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>WEBSITE</td><td style='text-align: center;'>网址</td><td style='text-align: center;'>网络版信息的网页地址</td></tr></table>

### A.8 标准实体是否译文

说明:标准文献是出版发布机构出版的原文版标准还是收藏单位获取的译文版标准。标准实体是否译文代码见表 A.8。

<div style="text-align: center;">表 A.8 标准实体是否译文</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>TEXT</td><td style='text-align: center;'>原文</td><td style='text-align: center;'>原出版发布机构出版的文献</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>TRANSLATION</td><td style='text-align: center;'>译文</td><td style='text-align: center;'>文献收藏单位获取的文献</td></tr></table>

### A.9 标准实体载体形态

说明：标准文献是以何种载体形态出版发行的。

标准实体载体形态代码见表 A.9。

<div style="text-align: center;">表 A.9 标准实体载体形态</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>PAPER</td><td style='text-align: center;'>纸本</td><td style='text-align: center;'>纸质印刷的文献</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>ELECVERSION</td><td style='text-align: center;'>电子版</td><td style='text-align: center;'>以电子格式存储的文献</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>DISK</td><td style='text-align: center;'>CD/DVD</td><td style='text-align: center;'>CD/DVD等光盘格式存储的文献</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>SOFTWARE</td><td style='text-align: center;'>软件</td><td style='text-align: center;'>以软件形式存储的文献</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>WITE WEB</td><td style='text-align: center;'>网站</td><td style='text-align: center;'>互联网信息发布形式的文献</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>MICRO FORM</td><td style='text-align: center;'>缩微</td><td style='text-align: center;'>缩微胶卷或平片</td></tr></table>

### A.10 标准实体功能种类

说明：相对于标准正文内容而言的独立出版的标准文献实体的功能类型。

标准实体功能种类代码见表 A.10。

<div style="text-align: center;">表 A.10 标准实体功能种类</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>TEXT</td><td style='text-align: center;'>正文</td><td style='text-align: center;'>标准的正文</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>ATTACHMENT</td><td style='text-align: center;'>附件</td><td style='text-align: center;'>另外出版的标准文献的补充部分</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>SUPPLEMENT</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>对标准文献内容进行补充的文献</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>MODIFICATION</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>对标准文献内容进行修改的文献</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>CORRIGENDA</td><td style='text-align: center;'>勘误</td><td style='text-align: center;'>对标准文献内容错误进行校勘的文献</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>TEXT+MODIFICATION</td><td style='text-align: center;'>正文+修改信息</td><td style='text-align: center;'>标准正文附加/包含修改补充勘误信息一同出版的文献</td></tr></table>

### A.11 标准实体是否合订

说明：标准文献是以单行本还是合订本出版的。

标准实体是否合订代码见表 A.11。

<div style="text-align: center;">表 A.11 标准实体是否合订</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>代码</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>OFFPRINT</td><td style='text-align: center;'>单行本</td><td style='text-align: center;'>一份标准单独出版的版本</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>BOUNDVOLUMEM</td><td style='text-align: center;'>合订本</td><td style='text-align: center;'>多分标准合订出版的版本</td></tr></table>

# 附录 B

# (资料性附录)

# 常用标准文献元数据表

### B.1 常用标准文献元数据表概述

本附录给出了常用各类标准文献元数据，使用单位可参考本附录进行著录。

### B.2 国家标准文献元数据

<div style="text-align: center;"><img src="imgs/img_in_image_box_219_625_258_659.jpg" alt="Image" width="3%" /></div>


国家标准文献元数据见表 B.1。

<div style="text-align: center;">表 B.1 国家标准文献元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>000</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>001</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>101</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>102</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>200</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>205</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>206</td><td style='text-align: center;'>废止日期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>207</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>209</td><td style='text-align: center;'>起草单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>298</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>302</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>305</td><td style='text-align: center;'>稽核项</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>390</td><td style='text-align: center;'>英文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>461</td><td style='text-align: center;'>代替标准</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>462</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>800</td><td style='text-align: center;'>一致性程度</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>820</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>823</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>825</td><td style='text-align: center;'>中国标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>826</td><td style='text-align: center;'>国际标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>835</td><td style='text-align: center;'>中文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>840</td><td style='text-align: center;'>中文自由词</td><td style='text-align: center;'>可选</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>846</td><td style='text-align: center;'>馆藏标志</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>871</td><td style='text-align: center;'>归口单位</td><td style='text-align: center;'>可选</td></tr></table>

### B.3 行业标准文献元数据

行业标准文献元数据见表B.2。

<div style="text-align: center;">表 B.2 行业标准文献元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>000</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>001</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>101</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>102</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>200</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>205</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>206</td><td style='text-align: center;'>废止日期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>207</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>209</td><td style='text-align: center;'>起草单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>298</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>302</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>305</td><td style='text-align: center;'>稽核项</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>390</td><td style='text-align: center;'>英文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>462</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>461</td><td style='text-align: center;'>代替标准</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>800</td><td style='text-align: center;'>一致性程度</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>820</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>823</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>825</td><td style='text-align: center;'>中国标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>826</td><td style='text-align: center;'>国际标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>835</td><td style='text-align: center;'>中文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>840</td><td style='text-align: center;'>中文自由词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>846</td><td style='text-align: center;'>馆藏标志</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>871</td><td style='text-align: center;'>归口单位</td><td style='text-align: center;'>可选</td></tr></table>

### B.4 地方标准文献元数据

地方标准文献元数据见表 B.3。

<div style="text-align: center;">表 B.3 地方标准文献元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>000</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>001</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>101</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>102</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>200</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>205</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>206</td><td style='text-align: center;'>废止日期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>207</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>209</td><td style='text-align: center;'>起草单位</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>298</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>302</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>305</td><td style='text-align: center;'>稽核项</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>390</td><td style='text-align: center;'>英文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>462</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>461</td><td style='text-align: center;'>代替标准</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>800</td><td style='text-align: center;'>一致性程度</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>820</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>823</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>825</td><td style='text-align: center;'>中国标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>826</td><td style='text-align: center;'>国际标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>835</td><td style='text-align: center;'>中文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>840</td><td style='text-align: center;'>中文自由词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>846</td><td style='text-align: center;'>馆藏标志</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>871</td><td style='text-align: center;'>归口单位</td><td style='text-align: center;'>可选</td></tr></table>

### B.5 国外标准文献元数据

国外标准文献元数据见表 B.4。

<div style="text-align: center;">表 B.4 国外标准文献元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>约束/条件</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>000</td><td style='text-align: center;'>记录状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>001</td><td style='text-align: center;'>记录识别符</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td><td style='text-align: center;'>标准号</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>101</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>102</td><td style='text-align: center;'>发布机构</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>200</td><td style='text-align: center;'>标准状态</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>205</td><td style='text-align: center;'>实施或试行日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>206</td><td style='text-align: center;'>废止日期</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>207</td><td style='text-align: center;'>确认日期</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>208</td><td style='text-align: center;'>原分类号</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>298</td><td style='text-align: center;'>中文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>301</td><td style='text-align: center;'>原文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>302</td><td style='text-align: center;'>英文标准名称</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>305</td><td style='text-align: center;'>稽核项</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>390</td><td style='text-align: center;'>英文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>462</td><td style='text-align: center;'>被代替标准</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>461</td><td style='text-align: center;'>代替标准</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>800</td><td style='text-align: center;'>一致性程度</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>820</td><td style='text-align: center;'>修改件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>823</td><td style='text-align: center;'>补充件</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>825</td><td style='text-align: center;'>中国标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>826</td><td style='text-align: center;'>国际标准分类号</td><td style='text-align: center;'>条件必选</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>835</td><td style='text-align: center;'>中文主题词</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>846</td><td style='text-align: center;'>馆藏标志</td><td style='text-align: center;'>可选</td></tr></table>

## 參 考 文 献

[1] GB/T 30522—2014 科技平台 元数据标准化基本原则与方法

[3] 都柏林核心元数据集 (Dublin Core Metadata Element Set, Version 1.1: Reference Description 2003-06-02)

[2] SDS/T 2112 科学数据共享元数据内容