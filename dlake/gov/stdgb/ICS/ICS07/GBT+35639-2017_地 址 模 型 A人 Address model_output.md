

# 中华人民共和国国家标准

GB/T 35639—2017

地址模型

Address model

2017-12-29 发布

2018-07-01 实施

## 目次

前言 …… I    
引言 …… II    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 缩略语和符号 …… 2    
5 地址数据模型 …… 2    
5.1 地址数据模型的构成 …… 2    
5.2 地址数据模型中的类 …… 4    
5.3 地址数据类别 …… 7    
5.4 地址数据代码表 …… 11    
6 地址数据结构 …… 13    
6.1 概述 …… 13    
6.2 地址数据结构类型 …… 14    
6.3 通用地址数据结构 …… 14    
6.4 专用信箱数据结构 …… 15    
7 地址数据与外部数据的关联 …… 16    
7.1 概述 …… 16    
7.2 地址与外部数据关联 …… 16    
7.3 地址组分与外部类的关联 …… 17    
附录 A（规范性附录） 地址数据模型的 XML 描述 …… 20    
附录 B（资料性附录） 院门/楼址的编制规则 …… 33    
参考文献 …… 34

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由国家测绘地理信息局提出。

本标准由全国地理信息标准化技术委员会(SAC/TC 230)归口。

本标准起草单位：国家基础地理信息中心、公安部第一研究所、北京市测绘设计研究院、民政部地名研究所、公安部信息中心、北京中科精图信息技术有限公司、浙江省测绘科学技术研究院、国家邮政局发展研究中心。

本标准主要起草人：李莉、谭宁生、张保钢、阮文斌、贺日兴、刘浩、陈绍勤、朱桂芳、张辛、王新健、黄蔚、唐德瑾。

## 引言

地址是对人们生活、生产以及各类活动处所位置的标识和定位，是描述空间位置最常用的一种方式。伴随定位技术和位置服务的普及应用，地址标准化问题日益凸显。规范的地址信息能便利百姓生活和社会公众服务，提高政府履职的管理水平和效率，有利于各类社会信息的分析、统计、管理和可视化表达，对于现代服务业和公共文化服务体系的发展具有支撑作用。制定和颁布国家地址标准，有利于地址编配和编码的科学性、整体性和系统性，提高地址数据的采集、处理效率，减少重复投入，有利于地址数据的使用、交换与共享。

## 地址模型

## 1 范围

本标准定义了地址的数据模型、数据结构、地址数据与外部数据的关联。

本标准适用于地址数据的编配、转换与互操作。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2260 中华人民共和国行政区划代码

GB/T 23707—2009 地理信息 空间模式(ISO 19107:2003, IDT)

GB/T 30170—2013 地理信息 基于坐标的空间参照(ISO 19111:2007, IDT)

ISO 19103:2015 地理信息 概念模式语言(Geographic information—Conceptual schema language)

ISO 19115-1:2014 地理信息 元数据 第1部分:基础(Geographic information—Metadata—Part 1:Fundamentals)

ISO 19152:2012 地理信息 土地管理域模型[Geographic information—Land administration domain model(LADM)]

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 地址 address

标识和定位人们生产、生活等活动处所位置的结构化信息。

示例 1：建筑物地址：北京市西城区西长安街 2 号

示例 2：居住地址：北京市海淀区定慧北里 9 号楼 5 单元 1201 室

示例 3: 专用邮箱地址: 北京市朝阳区大屯路 9718 信箱

注 $ ^{1} $ ：可标识和定位的对象是指现实世界中的空间对象，不包括电子或虚拟对象。

注2：一个空间对象可能有多个地址，但在任一时刻（或生命期内），一个空间对象唯一对应一个地址。

### 3.2 

<div style="text-align: center;"><img src="imgs/img_in_image_box_106_1380_144_1418.jpg" alt="Image" width="3%" /></div>


## 可编配地址对象 addressable object

可指定或编配地址的、具有固定位置的空间对象。如建筑物、居住或办公的处所等。

注：可编配地址对象可能涉及组织机构、收件人或与地址相关的对象，但这些对象不属于本地址数据模型讨论范畴。

### 3.3 

地址组分 address component

构成地址的基本组成部分。

### 3.4 

## 地址来源 address provenance

地址的生成、维护和使用的组织机构或个体。包括地址的出处、变更以及保管维护地址的组织机构或个体。

### 3.5 

## 地址位置 address position

地址的空间坐标。

## 4 缩略语和符号

下列缩略语和符号适用于本文件。

### 4.1 缩略语

UML: 统一建模语言 (Unified Modeling Language)

### 4.2 UML 符号

在本标准中，采用的 UML 关系符号见图 1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_315_731_854_893.jpg" alt="Image" width="45%" /></div>


说明：

1——关联(association)——代表两个类之间的操作关系。即类与类之间可通过句柄对对方的属性、方法进行操作。它可连接在同一个类上。



2——聚合(aggregation)——是一种特殊的关联关系，代表一个类是另一个类的一部分，即部分与整体的关系。

<div style="text-align: center;">图 1 UML 中的关系符号</div>


### 4.3 巴科斯范式符号

“::=”表示“被定义为”的意思；“<>”内包含的为必选项；“[]”内包含的为可选项；“{}”内包含的为可重复0至无数次的项；“|”表示在其左右两边任选一项。

## 5 地址数据模型

### 5.1 地址数据模型的构成

地址是描述位置的一种最常用的方式。本标准将地址的通用表述信息归纳为: 构成地址的文字描述内容、可编配地址的空间对象、编配地址的参照物、地址元数据以及编配地址中引用的法律法规和标准。

地址数据模型采用 UML 的定义的类（class）及关联关系表述。地址数据模型由 Address（地址类）、AddressComponent（地址组分类）、AddressableObject（可编配地址对象类）、ReferenceObject（参照对象类）、AddressMetadata（地址元数据类）和 AddressSpecification（地址引用标准类）组成，见图 2。采用 XML 描述的地址数据模型见附录 A。

Address 由一组非空的地址组分组成，每个地址有唯一的地址标识码。Address Component 是构成地址的描述性信息，包括行政区划名（省/地/市/县/乡）、街路巷/片区/村/社区名、院门/楼址、单元户室号或地块号等。Addressable Object 指地址所指代的空间对象。Reference Object 是地址组分所参照的对象，可是某一行政区划单元的空间范围、构成道路或街区的中心线或一组线段。其位置可用空间坐标（平面坐标/球面坐标/几何坐标'GM_Object'）表示。参照对象的几何（坐标）采用 GB/T 23707—2009 中定义的 GM_Object 类别表达。GM_Object 是特定参照系下（直接）位置集合的抽象，是抽象化子类别（如 GM_Point、GM_Curve 和 GM_Surface 等）的实例。Address Metadata 记录了地址的起源和维护信息。Address Specification 是地址及其组成部分引用的技术标准。

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_450_1036_1057.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2 地址数据模型</div>


地址数据模型通过类(class)、数据类别(type)、属性(attribute)、代码表(codelist)以及关联关系等来表述。图2中的关联关系应满足以下要求：

——地址组分不能为空，其中应包含一个或多个地址组分，同一地址组分可属于一个或多个地址。——在任一给定的时间点或生命期内，一个地址仅参照一个可编配地址对象；多个地址也可参照同一个可编配地址对象。

示例 1：多个地址参照同一可编配地址对象的示例：一个建筑物有多个出入口。

——一个参照对象可被一个或多个地址组分参照。

示例 2：对源自 AddressComponent 的道路名类，街道中心线可与参照对象关联。

示例 3：对源自 AddressComponent 的道路名类，构成街道的中心线段可与参照对象关联。

——地址可引用一个或多个地址标准，这些标准可能涉及不同的地址类，各个地址类规定了相应的有效地址组分类别。地址引用的标准可是法律法规、技术规范或相关地址标准。

### 5.2 地址数据模型中的类

#### 5.2.1 概述

地址数据模型中的类包括：Address、AddressComponent、AddressableObject、ReferenceObject、AddressMetadata 和 AddressSpecification6 类。这些类分为必选类和可选类。其中 Address 和 AddressComponent 为必选类；AddressableObject、ReferenceObject、AddressSpecification 和 AddressMetadata 为可选类。本节给出这 6 个类的定义及其属性。

#### 5.2.2 Address(地址类)

Address 类由一组非空的地址组分组成。表 1 定义了 Address 类的属性。示例：“北京市海淀区羊坊店路 15 号”包括以下地址组分：行政区名、街道名和门牌号。

<div style="text-align: center;">表 1 Address(地址类)属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>地址的唯一标识码</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;Datatype&gt;&gt;Oid $ ^{a} $</td></tr><tr><td style='text-align: center;'>addressComponent</td><td style='text-align: center;'>地址组分是地址的组成部分</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>AddressComponent</td></tr><tr><td style='text-align: center;'>addressValue</td><td style='text-align: center;'>地址的完整描述</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>position</td><td style='text-align: center;'>可编配地址对象的几何(坐标)位置</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;AddressPosition</td></tr><tr><td style='text-align: center;'>status</td><td style='text-align: center;'>地址的状况,例如,未知、官方、非官方</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt;AddressStatus</td></tr><tr><td style='text-align: center;'>lifestyle</td><td style='text-align: center;'>地址当前生命期状况的信息</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;Lifecycle</td></tr><tr><td style='text-align: center;'>lifestyleStage</td><td style='text-align: center;'>地址生命期的当前阶段</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt;AddressLifecycleStage</td></tr><tr><td style='text-align: center;'>metadata</td><td style='text-align: center;'>地址元数据</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>关联</td><td style='text-align: center;'>AddressMetadata</td></tr><tr><td style='text-align: center;'>addressedObject</td><td style='text-align: center;'>编配了地址的对象</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>关联</td><td style='text-align: center;'>AddressableObject</td></tr><tr><td style='text-align: center;'>specification</td><td style='text-align: center;'>关于地址及其组成部分的技术规定</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>关联</td><td style='text-align: center;'>AddressSpecification</td></tr><tr><td colspan="6">注:M——必选项;O——可选项;N——出现次数&gt;1。</td></tr><tr><td colspan="6">$ ^{a} $  Oid在ISO 19152:2012中定义为对象标识符。它在命名空间内唯一,即其他空间对象不能使用相同标识符。</td></tr></table>

#### 5.2.3 AddressComponent(地址组分类)

AddressComponent 类构成地址的描述性信息。表 2 定义了 AddressComponent 类的属性。示例：“西堤北村”是地址“河北省冀州市门庄乡西堤北村 66 号”的组成部分。

<div style="text-align: center;">表 2 AddressComponent(地址组分类) 属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>地址组分的唯一标识码</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;Datatype&gt;&gt; Oid $ ^{a} $</td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>组分的类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt; AddressComponentType</td></tr><tr><td style='text-align: center;'>value</td><td style='text-align: center;'>组分的一个或多个值</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt; AddressComponentValue</td></tr><tr><td style='text-align: center;'>address</td><td style='text-align: center;'>地址组分是构成地址的组成部分</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>Address</td></tr><tr><td style='text-align: center;'>referenceObject</td><td style='text-align: center;'>地址组分值的属性所指的对象</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>ReferenceObject</td></tr><tr><td colspan="6">注：M——必选项；O——可选项；N——出现次数&gt;1。</td></tr><tr><td colspan="6">$ ^{a} $  Oid 在 ISO 19152:2012 定义为对象标识符。它在命名空间内唯一，即其他空间对象不能使用相同标识符。</td></tr></table>

#### 5.2.4 AddressableObject(可编配地址对象类)

AddressableObject 可无歧义地对应一个地址，即一个对象可通过地址标识或定位。表 3 定义了 AddressableObject 类的属性。

<div style="text-align: center;">表 3 AddressableObject(可编配地址对象类)属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>可编配地址对象的唯一标识符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;Datatype&gt;&gt; Oid $ ^{a} $</td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>可编配地址对象类型</td><td style='text-align: center;'>当可编配地址对象没有子类时选用</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt; AddressableObjectType</td></tr><tr><td style='text-align: center;'>position</td><td style='text-align: center;'>可编配地址对象的几何(坐标)位置</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt; AddressPosition</td></tr><tr><td style='text-align: center;'>address</td><td style='text-align: center;'>地址无歧义地确定地址可编配对象</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>Address</td></tr><tr><td colspan="6">注：M——必选项；O——可选项；N——出现次数＞1。</td></tr><tr><td colspan="6">$ ^{a} $  Oid 在 ISO 19152:2012 定义为对象标识符。它在命名空间内唯一，即其他空间对象不能使用相同标识符。</td></tr></table>

#### 5.2.5 ReferenceObject(参照对象类)

ReferenceObject 类是地址组分的参照对象。表 4 定义了 ReferenceObject 类的属性。

示例 1: 一个地名的边界可以是一个地名的参照对象。

示例 2: 多条道路中心线可以是一条道路名的参照对象。

<div style="text-align: center;">表 4 ReferenceObject(参照对象类) 属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>可编配地址对象的唯一标识符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;Datatype&gt;&gt; Oid $ ^{a} $</td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>参照对象的类型</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt; ReferenceObjectType</td></tr><tr><td style='text-align: center;'>geometry</td><td style='text-align: center;'>参照对象的几何(坐标)注:特指GM_Object</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt; GM_Object.见 GB/T 23707—2009</td></tr><tr><td style='text-align: center;'>addressComponent</td><td style='text-align: center;'>引用参照对象作为地址组分的值</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>AddressComponent</td></tr><tr><td colspan="6">注:M——必选项;O——可选项;N——出现次数&gt;1。</td></tr><tr><td colspan="6">$ ^{a} $  Oid 在 ISO 19152:2012 定义为对象标识符。它在命名空间内唯一,即其他空间对象不能使用相同标识符。</td></tr></table>

#### 5.2.6 AddressSpecification(地址引用标准类)

AddressSpecification 类是约束地址及其组成部分的技术标准，可用于地址数据有效性和质量检查。表 5 定义了 AddressSpecification 类的属性。

<div style="text-align: center;">表 5 AddressSpecification(地址引用标准类)属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>citation</td><td style='text-align: center;'>引用的标准</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>CI_Citation®</td></tr><tr><td style='text-align: center;'>classSpecification</td><td style='text-align: center;'>地址类标准,如地址类的一组有效组分类型</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt; AddressClass-Specification</td></tr><tr><td style='text-align: center;'>specifiedAddress</td><td style='text-align: center;'>符合地址标准要求的地址</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>Address</td></tr><tr><td colspan="6">注:M——必选项;O——可选项;N——出现次数&gt;1。</td></tr><tr><td colspan="6">a CL_Citation(引用文献)采用 ISO 19115-1:2014 中定义的类型。</td></tr></table>

#### 5.2.7 AddressMetadata(地址元数据类)

AddressMetadata 类记录了地址的起源和维护信息。表 6 定义了 AddressMetadata 类的属性。

<div style="text-align: center;">表 6 AddressMetadata(地址元数据类)属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>id</td><td style='text-align: center;'>地址的唯一标识码</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;Datatype&gt;&gt; Oid $ ^{a} $</td></tr><tr><td style='text-align: center;'>addressableObject-LifecycleStage</td><td style='text-align: center;'>可赋予地址对象生命期的当前阶段</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt; AddressableObject-LifecycleStage</td></tr></table>

<div style="text-align: center;">表 6 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>provenance</td><td style='text-align: center;'>地址的来源信息</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;AddressProvenance</td></tr><tr><td style='text-align: center;'>dataQuality</td><td style='text-align: center;'>数据质量</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;AddressDataQuality</td></tr><tr><td colspan="6">注：M——必选项；O——可选项。</td></tr><tr><td colspan="6">$ ^{a} $  Oid 在 ISO 19152:2012 定义为对象标识符。它在命名空间内唯一，即其他空间对象不能使用相同标识符。</td></tr></table>

### 5.3 地址数据类别

#### 5.3.1 概述

地址数据类别通过属性名、定义、条件、最大出现次数、数据类型以其属性域等加以描述。地址数据类别见图 3。

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_747_1016_1342.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 3 地址数据类别</div>


#### 5.3.2 AddressPosition(地址位置类别)

AddressPosition 类别表示可赋予地址对象（如建筑物、地块或专属场所等）所处的空间位置坐标。

其位置应选在可赋予地址对象的通用位置，如大门、出入口、几何形状中心；而不是一个域或特定目标位置，如救灾通道或电表。后者的位置可置于与地址或赋予地址对象关联类的位置属性中。

门楼址的位置宜选在所指实体的出入口，当存在多个出入口时，可用点群表示地址位置，同时注明出入口的方位或主次信息，如“正门”“西南侧门”“1门”“3单元”等。对于建设工程地块地址的位置，有出入口的，参照门楼址确定位置的方法；没有出入口的，宜取地块中心点作为该地块地址的位置。表7定义了AddressPosition类别的属性。

<div style="text-align: center;">表 7 AddressPosition(地址位置类别) 属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>geometry</td><td style='text-align: center;'>表示地址位置的几何对象(坐标)</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt; GM_Object</td></tr><tr><td style='text-align: center;'>X</td><td style='text-align: center;'>地址位置的X坐标</td><td style='text-align: center;'>C:与Y同时使用</td><td style='text-align: center;'>N</td><td style='text-align: center;'>双精度</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Y</td><td style='text-align: center;'>地址位置的Y坐标</td><td style='text-align: center;'>C:与X同时使用</td><td style='text-align: center;'>N</td><td style='text-align: center;'>双精度</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Z</td><td style='text-align: center;'>地址位置的Z坐标</td><td style='text-align: center;'>C/O:与X、Y同时使用</td><td style='text-align: center;'>N</td><td style='text-align: center;'>双精度</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>longitude</td><td style='text-align: center;'>地址位置的经度坐标</td><td style='text-align: center;'>C:与latitude同时使用</td><td style='text-align: center;'>N</td><td style='text-align: center;'>双精度</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>latitude</td><td style='text-align: center;'>地址位置的纬度坐标</td><td style='text-align: center;'>C:与longitude同时使用</td><td style='text-align: center;'>N</td><td style='text-align: center;'>双精度</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>elevation</td><td style='text-align: center;'>地址位置的海拔高度</td><td style='text-align: center;'>C/O:与longitude、latitude同时使用</td><td style='text-align: center;'>N</td><td style='text-align: center;'>双精度</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>coordinateReferenceSystem</td><td style='text-align: center;'>坐标参照系统</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt; SC_CRS*</td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>地址位置的类别</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt; AddressPositionType</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>示例:中心点,街道类型,概略位置</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td colspan="6">注:M——必选项;C——条件可选项;O——可选项;N——出现次数&gt;1。可选用geometry、X/Y/Z、longitude/latitude/elevation三种位置表达方式。X、Y与Z,经度(longitude)、纬度(latitude)与高程(elevation)需配对使用,其中Z和高程为可选项。</td></tr><tr><td colspan="6">a SC_CRS(基于坐标的空间参照_坐标参照系)采用GB/T 30170—2013中定义的SC_CRS类型表达。</td></tr></table>

#### 5.3.3 AddressComponentValue(地址组分值类别)

AddressComponentValue 类别说明了地址组分值及其数据类型。AddressComponentValue 类别

的属性见表8。

<div style="text-align: center;">表 8 AddressComponentValue(地址组分值类别) 属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>value</td><td style='text-align: center;'>地址组分的值</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>任意</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>type</td><td style='text-align: center;'>地址组分值的类别，缺省值为其初始值</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt;AddressComponentValue-Type</td></tr><tr><td colspan="6">注：M——必选项；O——可选项。</td></tr></table>

#### 5.3.4 AddressProvenance(地址来源类别)

AddressProvenance 类别记录了地址组分或可赋予地址对象的出处、变化以及监管维护地址的组织机构或个体信息。AddressProvenance 类别属性见表 9。

<div style="text-align: center;">表 9 AddressProvenance(地址来源类别) 属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>authority</td><td style='text-align: center;'>地址的编配机构, 编配地址或地址组分的权威机构</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;CL_Organisation $ ^{a} $</td></tr><tr><td style='text-align: center;'>owner</td><td style='text-align: center;'>地址的维护机构, 维护地址数据的机构</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;CL_Organisation</td></tr><tr><td style='text-align: center;'>lineage</td><td style='text-align: center;'>来源信息, 地址或地址组分的来源信息(出处及形成过程)</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;LL_Lineage $ ^{b} $</td></tr><tr><td colspan="6">注: M——必选项; O——可选项; N——出现次数&gt;1。</td></tr><tr><td colspan="6">$ ^{a} $  CI_Organisation(引用负责机构)采用 ISO 19115-1:2014 中定义的类型。 $ ^{b} $  LI_Lineage(数据志)采用 ISO 19115-1:2014 中定义的类型。</td></tr></table>

#### 5.3.5 Lifecycle(地址生命周期类别)

Lifecycle 类别包含地址或可赋予地址对象的生命期描述信息。Lifecycle 类别属性见表 10。

<div style="text-align: center;">表 10 Lifecycle(地址生命周期类别)属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>validFrom</td><td style='text-align: center;'>起始日期,经权威机构认可的起始日期和时间</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>DateTime, 日期时间字符编码,在 ISO 19103 定义了该类数据类型</td></tr><tr><td style='text-align: center;'>validTo</td><td style='text-align: center;'>失效日期,失效的日期和时间</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>DateTime, 同前</td></tr><tr><td style='text-align: center;'>beginLifespan</td><td style='text-align: center;'>数据版本形成时间,将数据对象插入数据集,形成的数据集版本的日期或时间</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>DateTime, 同前</td></tr></table>

<div style="text-align: center;">表 10 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>endLifespan</td><td style='text-align: center;'>数据版本失效时间，说明数据集中数据对象被其他版本更替或撤销的日期或时间</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>DateTime，同前</td></tr><tr><td rowspan="2">version</td><td style='text-align: center;'>数据集最新版本的说明信息</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>任意文本</td></tr><tr><td colspan="5">注：随数据对象的变化，提供新的数据版本。</td></tr><tr><td colspan="6">注：M——必选项；O——可选项。</td></tr></table>

#### 5.3.6 AddressDataQuality(地址数据质量类别)

AddressDataQuality 类别包含地址数据质量的描述信息。AddressDataQuality 类别的属性见表 11。

<div style="text-align: center;">表 11 AddressDataQuality(地址数据质量类别)属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>geometryType</td><td style='text-align: center;'>空间位置类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt;MD_GeometricObjectTypeCodea</td></tr><tr><td style='text-align: center;'>dataQuality</td><td style='text-align: center;'>数据质量</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;DQ_DataQualityb</td></tr><tr><td style='text-align: center;'>collectionTime</td><td style='text-align: center;'>位置数据获取时间</td><td style='text-align: center;'>O</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>DateTime(同前)</td></tr><tr><td style='text-align: center;'>responsibleParty</td><td style='text-align: center;'>数据负责机构</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;type&gt;&gt;CI_ResponsiblePartyc</td></tr><tr><td colspan="6">注：M——必选项；O——可选项；N——出现次数＞1。</td></tr><tr><td colspan="6">aMD_GeometricObjectTypeCode(元数据几何对象类型代码)采用ISO 19115-1:2014中定义的类型。bDQ_DataQuality(数据质量信息)采用ISO 19115-1:2014中定义的类型,涉及质量评价范围(包括数据志&lt;ll_Lineage&gt;和质量元素&lt;dQ_Element&gt;),对数据质量作总体评价。cCL_ResponsibleParty(引用职责方)采用ISO 19115-1:2014中定义的类型。</td></tr></table>

#### 5.3.7 AddressClassSpecification(地址类标准类别)

AddressClassSpecification 类别中包含地址类所引用的标准信息。AddressClassSpecification 类别的属性见表 12。

<div style="text-align: center;">表 12 AddressClassSpecification(地址类标准类别) 属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性名</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>约束条件</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>域</td></tr><tr><td style='text-align: center;'>class</td><td style='text-align: center;'>具体指定地址类</td><td style='text-align: center;'>M</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt;AddressClass</td></tr><tr><td style='text-align: center;'>component</td><td style='text-align: center;'>一个或多个有效的地址组分</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>类</td><td style='text-align: center;'>&lt;&lt;codelist&gt;&gt;AddressComponentType</td></tr><tr><td colspan="6">注：M——必选项；N——出现次数＞1。</td></tr></table>

### 5.4 地址数据代码表

#### 5.4.1 概述

本条给出了地址模型中的核心代码表的值，见图4。根据需要，可追加代码表值和/或选用该代码表值的子集。图中为列举的代码表举例，AddressableObjectTypeCode可为：房屋、地标、寓所和综合楼等建筑物；AddressPositionTypeCode可为：道路地址、街区地址；AddressClassCode可为：中心点、街道和邻近区；ReferenceObjectTypeCode可为：街道、行政区域、个体和组织机构。用户可根据具体情况添加补充代码值。

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_469_1015_1060.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 4 地址数据的核心代码表及值</div>


#### 5.4.2 AddressComponentType(地址组分类别)

AddressComponentType 类别中包含通用地址组分类别值及说明，见表 13。

<div style="text-align: center;">表 13 AddressComponentType(地址组分类别)值及说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>行政区划名</td><td style='text-align: center;'>GB/T 2260 中规定的行政区划名称</td></tr><tr><td style='text-align: center;'>省级区划名</td><td style='text-align: center;'>GB/T 2260 中规定的省级行政区划名称，包括省、自治区、直辖市、特别行政区等</td></tr><tr><td style='text-align: center;'>地级区划名</td><td style='text-align: center;'>GB/T 2260 中规定的地级行政区划名称，包括地级市、地区、自治州、盟等</td></tr><tr><td style='text-align: center;'>县级区划名</td><td style='text-align: center;'>GB/T 2260 中规定的县级行政区划名称，包括县、自治县、县级市、旗、自治旗、市辖区、林区、特区等</td></tr><tr><td style='text-align: center;'>乡镇/街道级区划名</td><td style='text-align: center;'>GB/T 2260 中规定的乡镇/街道级行政区划名称，包括镇、乡、民族乡、街道等</td></tr></table>

<div style="text-align: center;">表 13（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>社区/村(居)委名</td><td style='text-align: center;'>社区/行政村(居)委会等基层群众性自治组织名称等</td></tr><tr><td style='text-align: center;'>街路巷/片区名</td><td style='text-align: center;'>街路巷或片区的名称,用于描述可编配地址对象所在的更小区域位置</td></tr><tr><td style='text-align: center;'>街路巷名</td><td style='text-align: center;'>街、道、路、巷的名</td></tr><tr><td style='text-align: center;'>片区名</td><td style='text-align: center;'>包含地片名、标识性地物名、居民小区名、自然村名、村民小组和专署区域名等</td></tr><tr><td style='text-align: center;'>地片名</td><td style='text-align: center;'>包括权威机构确定或约定俗成的名称、学校、工厂、广场、公园名等</td></tr><tr><td style='text-align: center;'>标识性地物名</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>居民小区名</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>自然村名</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>村民小组</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>专署区域名</td><td style='text-align: center;'>包括各类大型经济开发区、高新技术区、产业聚集区、工业园区、农垦区(农场、林场、养殖场)、机场(码头、港口)、风景名胜区、建设兵团等特定区域名等</td></tr><tr><td style='text-align: center;'>院门/楼址</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>门牌号</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>院落名</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>楼牌号</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>建筑物名</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>单元户室号</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>单元门号</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>楼层</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>户室号</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>专用信箱号</td><td style='text-align: center;'>邮政部门提供给机关、工矿、企业、团体等单位或个人使用,通过信箱通信</td></tr><tr><td style='text-align: center;'>信箱号</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>分信箱号</td><td style='text-align: center;'></td></tr><tr><td colspan="2">注:灰色填充栏中的内容是类别,空白栏为地址组分类型值。</td></tr></table>

#### 5.4.3 AddressComponentValueType(地址组分值类别)

AddressComponentValueType 类别值及说明见表 14。

<div style="text-align: center;">表 14 AddressComponentValueType(地址组分值类别)值及说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>缺省的组分值（如，不可替换的组分值）</td></tr><tr><td style='text-align: center;'>替换值</td><td style='text-align: center;'>可替换的组分值：缩略语</td></tr></table>

#### 5.4.4 AddressStatus(地址状况类别)

AddressStatus 说明地址状况。其类别值及说明见表 15。

<div style="text-align: center;">表 15 AddressStatus(地址状况)值及说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>未知</td><td style='text-align: center;'>不知状态的地址</td></tr><tr><td style='text-align: center;'>官方</td><td style='text-align: center;'>由法定地址管理机构编配的地址</td></tr><tr><td style='text-align: center;'>非官方</td><td style='text-align: center;'>非法定地址管理机构编配的地址</td></tr></table>

#### 5.4.5 AddressLifecycleStage(地址生命期阶段)

AddressLifecycleStage 的代码值及说明见表 16。

<div style="text-align: center;">表 16 AddressLifecycleStage(地址生命期阶段)值及说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>值</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>现行</td><td style='text-align: center;'>当前使用的地址或地址组分</td></tr><tr><td style='text-align: center;'>规划</td><td style='text-align: center;'>规划的地址或地址组分。如，由管理机构通过常规程序推荐使用的地址</td></tr><tr><td style='text-align: center;'>拒绝</td><td style='text-align: center;'>规划的但被拒绝的地址或地址组分</td></tr><tr><td style='text-align: center;'>保留</td><td style='text-align: center;'>保留作为未来使用的地址或地址组分</td></tr><tr><td style='text-align: center;'>废弃</td><td style='text-align: center;'>曾经使用，已经不再使用的地址或地址组分</td></tr><tr><td style='text-align: center;'>未知</td><td style='text-align: center;'>生命阶段未知的地址或地址组分</td></tr></table>

#### 5.4.6 AddressableObjectLifecycleStage(可赋予地址对象生命期阶段)

AddressableObjectLifecycleStage 的代码值及说明见表 17。

<div style="text-align: center;">表 17 AddressableObjectLifecycleStage(可赋予地址对象生命期阶段)值及说明</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>规划</td><td style='text-align: center;'>已经提议建设的可赋予地址对象，例如管理部门按程序已提出建设的可赋予地址对象</td></tr><tr><td style='text-align: center;'>批准</td><td style='text-align: center;'>已获得批准建设的可赋予地址对象</td></tr><tr><td style='text-align: center;'>建设中</td><td style='text-align: center;'>处于建设过程中的可赋予地址对象</td></tr><tr><td style='text-align: center;'>在用</td><td style='text-align: center;'>在用的可赋予地址对象</td></tr><tr><td style='text-align: center;'>消失</td><td style='text-align: center;'>不复存在的可赋予地址对象（如，建筑物已拆毁）</td></tr><tr><td style='text-align: center;'>未知</td><td style='text-align: center;'>未知生命阶段的可赋予地址对象</td></tr></table>

## 6 地址数据结构

### 6.1 概述

地址数据结构由行政区划名、街路巷/片区/村/社区名、院门/楼址、单元户室号、地块号和专用信箱号等地址组分类构成，采用巴科斯范式描述地址组分之间的关系。

### 6.2 地址数据结构类型

地址数据结构分为通用地址和专用信箱两种类型。

通用地址数据类别：=＜行政区划名＞ $$ ＜\{[街路巷/片区/村/社区名]|[院门/楼址]\}＞ $$ 单元户室号 $$  $$ |地块号 $$ 

专用信箱地址数据类别：=＜行政区划名＞ $$ 街路巷/片区名 $$ ＜专用信箱代号＞

### 6.3 通用地址数据结构

#### 6.3.1 行政区划名

行政区划名：:=<省级区划名>「地级区划名」|「县级区划名」|「乡镇/街道级区划名」|「社区/村（居）委名」

地址的行政区划名由多级行政区划自上向下顺序排列，允许跨级。社区/村（居）委会等基层群众性自治组织名可作为地址组分。

根据 GB/T 2260 规定，地址中行政区划分为以下 4 级：

a）省级，包括省、自治区、直辖市、特别行政区；

b） 地级，包括地级市、地区、自治州、盟；

c）县级，包括县、自治县、县级市、旗、自治旗、市辖区、林区、特区；

d）乡镇/街道级，包括镇、乡、民族乡、街道。

#### 6.3.2 街路巷/片区名

街路巷/片区名：= $ [街路巷名] $  $ [片区名] $  $ [村名] $  $ [社区名] $ 

街路巷/片区用于描述地址对象所在的小区域范围，由地片名、标识性地物名、居民小区名、自然村名、村民小组和专署区域名等组成。此部分地址组分的排列顺序按照其隶属、包含或主次分支等关系排列，允许循环嵌套。如在片区内含有街路巷、小区等情况。但应减少循环嵌套现象。

含街路巷/片区名地址组分(黑体字标注)的地址举例如下：

a）街路巷名

示例 1：北京市 | 海淀区 | 莲花池西路 | 28 号

示例 2: 新疆 | 伊犁州 | 新源县 | 吐尔根乡 | 阿吾孜村 | 吾热克特路 | 011 号

b）片区名

示例：贵州省|织金县|城关镇|平安小区|一单元|4层|1号

c) 自然村名

示例：辽宁省 | 瓦房店市 | 赵屯乡 | 新立村 | 上沟屯 | 30 号

d） 村民小组

示例：四川省 | 犍为县 | 双溪乡 | 硝水村 | 3 组 | 10 号

e）街路巷名＋片区名

示例: 河南省 | 三门峡市 | 湖滨区 | 金昌东路 | 化机厂 | 单身楼 | 20 号

f） 自然村名＋村民小组

示例：安徽省铜陵县中心村 | 新庄 | 十八组 | 24 号

g） 专署区域名+ $$ 街路巷名 $$  $$ 片区名 $$  $$ 自然村名 $$  $$ 村民小组 $$  $$ 专署区域名 $$ 

示例 1: 安徽省 | 合肥市 | 经济技术开发区 | 翡翠路 | 398 号

示例 2: 河北省 | 三河市 | 燕郊开发区 | 铁三局家属区 | 61 号

示例 3: 湖北省 | 孝感市 | 孝南区 | 下湾开发区 | 罗坡村 | 十二组 | 17 号

h）其他复杂组合与嵌套：

1）街路巷名＋街路巷名

示例 1: 贵州省 | 六盘水市 | 钟山区 | 交通南路 | 一巷 | 10 号 | 101 室

示例 2: 河北省 | 张家口市 | 桥东区 | 南站西街 | 北一道 | 3 排 | 1 号

2）片区名＋街路巷名

示例: 河北省 | 安国市 | 西城乡 | 横头村 | 第十四小区 | 华长胡同 | 388 号

#### 6.3.3 院门/楼址

院门/楼址：= $ [门牌号]|[院落名]|[楼牌号]|[建筑物名] $ 

地址的门楼址由门牌号、院落名、楼牌号、建筑物名等组成。编制院门楼址的规则参见附录 B。含门楼址组分地址（黑体字标注）的地址举例如下：

a）门牌号

示例：浙江省 | 丽水市 | 青田县 | 岭根乡 | 政府路 | 51号

b）院落名

示例：陕西省 | 渭南市 | 临渭区 | 东风大街 | 西段 | 金城园家属院 | 2栋 | 1单元 6号

c）建筑物名

示例：陕西省 | 合阳县 | 城关镇 | 东大街 | 北方大厦 | 403 室

d) 门牌号 + 楼牌号

示例：河南省 | 郑州市 | 经北二路 | 66 号 | 40 号楼 | 1 单元 | 202 号

e）院落名＋楼牌号

示例：内蒙古自治区|呼和浩特市|赛罕区|乌兰察布东路|建材设计院|1号楼|2单元|6号

f）建筑物名＋楼牌号

示例:贵州省|松桃苗族自治县|蓼皋镇|世昌广场|丽景大厦|5幢|B单元|11层|2号

#### 6.3.4 单元户室号

单元户室号：=[单元门号]|[楼层]|[户室号]

地址中单元户室号部分由单元门号、楼层和户室号组成。含单元户室号地址组分(黑体字标注)的地址举例如下：

a）单元门号＋楼层＋户室号

示例：河南省 | 洛阳市 | 洛龙区 | 关林镇 | 胜利街 | 锦园小区 | 3号楼 | 1单元 | 6层 | 2号

b) 单元门号+户室号

示例：北京市|海淀区|田村|畅茜园|碧森里小区|8号楼|5门|201室

c）楼层号＋户室号

示例:云南省|昆明市|五华区|青年路北延长线|住宅楼|1幢|14层|02室

d) 户室号(含楼层)

示例：云南省 | 昆明市 | 五华区 | 昆明卷烟厂宿舍 | 红云高层 | 1幢 | 1603室

### 6.4 专用信箱数据结构

#### 6.4.1 专用信箱

邮政专用信箱是设邮政部门内供用户租用并自行开取邮件的信箱。邮政专用信箱由邮政部门按规定统一编列号码。用户租用专用信箱，可以用信箱代号代替地址进行通信。

#### 6.4.2 专用信箱结构

专用信箱地址：:=＜行政区划名＞[街路巷/片区名]＜专用信箱代号＞[分信箱号]

专用信箱地址由行政区划名、街路巷/片区名和专用信箱号组成。其中行政区划名、街路巷/片区名等地址组分与通用地址组分相同，其中街路巷/片区名等为可选组分；专用信箱号由信箱编号和分信箱编号组成。专用信箱地址的常见形式举例如下：

## a）信箱编号

示例 1: 成都市 | 第 8 邮政信箱

示例 2: 北京市 | 朝阳区 | 大屯路 | 9718 信箱

b）信箱编号+分信箱号

示例：天津市 | 296 信箱 | 41 分箱

## 7 地址数据与外部数据的关联

### 7.1 概述

地址数据的关联有多种方式，可通过地址与外部数据关联或地址组分与外部类关联，通过关联实现地址数据的多种应用服务。

### 7.2 地址与外部数据关联

一个或多个地址可与外部数据关联。如地址与个人(Employee)的住址、注册工商机构(Business-Register)总部/分支的办公地址或客户(Client)的办公地址类相关联，见图5。

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_197_1015_923.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 5 地址与外部数据关联</div>


### 7.3 地址组分与外部类的关联

地址组分与外部数据的关联见图6和图7。在图6中，参照空间对象（ReferenceSpatialObject）、组织机构（Organization）类和人员（Person）类聚合而成地址组分参照对象；当存在位置空间单元类（LA_SpatialUnit）和位置空间单元组类（LA_SpatialUnitGroup）两个可关联外部数据类时，可将地址组分与外部数据关联。图7中行政区域（AdministrativeArea）和街道（Thoroughfare）与ReferenceSpatialObject（或源自ReferenceSpatialObject的其他类）的关联，表明空间参照对象（行政区域和街道）之间彼此间的关联。

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_199_1023_806.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 6 外部管理类通过 ReferenceObject 与 AddressComponent 关联</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_173_199_1031_847.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 7 外部行政管理区和道路类通过 ReferenceObject 与地址组分关联</div>


附录 A

(规范性附录)

地址数据模型的 XML 描述

采用 XML 描述的地址数据模型见图 A.1，地址组分结构见图 A.2，地址位置结构见图 A.3，地址生命期类别结构见图 A.4，地址元数据结构见图 A.5，可编配地址对象结构见图 A.6，规范的地址结构见图 A.7。

<div style="text-align: center;"><img src="imgs/img_in_image_box_228_457_935_1431.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 A.1 采用 XML 描述的地址模型</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_138_201_1064_874.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 A.2 采用 XML 描述的地址组分结构</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_189_954_1012_1392.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 A.3 采用 XML 描述的地址位置结构</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_347_203_824_462.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">图 A.4 采用 XML 描述的地址生命期类别结构</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_152_539_1021_1219.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 A.5 采用 XML 描述的地址元数据结构</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_139_201_1063_850.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 A.6 采用 XML 描述的可编配地址对象结构</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_139_927_1064_1270.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 A.7 采用 XML 描述的规范地址结构</div>


地址数据模型 XML 语义定义如下：

<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:element name="Address" type="Address"/>
    <xs:complexType name="Address">
        <xs:annotation>

<xs:documentation>地址是标识和定位人们生产、生活以及各类活动处所（即空间对象）位置的结构化信息。地址类（Address）由一组为非空的地址组分组成。<xs:documentation>

</xs:annotation>

<xs:sequence>
    <xs:element name="id" type="Oid" minOccurs="1" maxOccurs="1"/>
    <xs:element name="address" component" type="Address" component" minOccurs="1" maxOccurs="unbounded"/>
    <xs:element name="addressValue" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="position" type="AddressPosition" id="addressPosition" minOccurs="1" maxOccurs="1"/>
    <xs:element name="status" type="AddressStatus" id="status" minOccurs="0" maxOccurs="1"/>
    <xs:element name="cycle" type="Lifecycle" id="cycle" minOccurs="0" maxOccurs="1"/>
    <xs:element name="cycleStage" type="AddressLifecycleStage" minOccurs="0" maxOccurs="1"/>
    <xs:element name="metadata" type="AddressMetadata" minOccurs="0" maxOccurs="1"/>
    <xs:element name="addressedObject" type="AddressableObject" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="specification" type="AddressSpecification" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>

</xs:complexType>

<xs:complexType name="AddressComponent">
    <xs:annotation>
        <xs:documentation>地址组分(Address Component)是构成地址的基本成分。地址由一个非空集的 Address Component 构成。</xs:documentation>
        <xs:annotation>
            <xs:element name="id" type="Oid" minOccurs="1" maxOccurs="1"/>
            <xs:element name="address" componentType="type="Address" componentType="minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="Address" componentValue="minOccurs="1" maxOccurs="unbounded"/>
            <xs:element name="address" type="Address" minOccurs="0" maxOccurs="unbounded"/>
        </xs:annotation>
    </xs:documentation>
    <xs:documentation>
        <xs:documentation>
            <xs:element name="referenceObject" type="ReferenceObject" minOccurs="0" maxOccurs="unbounded"/>
        </xs:annotation>
    </xs:element>
</xs:documentation>

Occurs="unbounded"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="AddressableObject">
<xs:annotation>
<xs:documentation>一个地址可无歧义地确定一个 AddressableObject，即一个对象可通过地址标识或定位。</xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:element name="id" type="Oid" minOccurs="1" maxOccurs="1"/>
<xs:element name="type" type="AddressableObjectType" minOccurs="0" maxOccurs="1"/>
<xs:element name="position" type="AddressPosition" minOccurs="1" maxOccurs="1"/>
<xs:element name="address" type="Address" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="ReferenceObject">
<xs:annotation>
<xs:documentation>参照对象类(ReferenceObject)是地址组分值的参照对象。</xs:annotation>
</xs:complexType>
<xs:sequence>
<xs:element name="id" type="Oid" minOccurs="1" maxOccurs="1"/>
<xs:element name="type" type="ReferenceObjectType" minOccurs="0" maxOccurs="1"/>
<xs:element name="geometry" type="GM_Object" minOccurs="0" maxOccurs="1"/>
<xs:element name="address" component="type" addressComponent="minOccurs="1" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="AddressSpecification">
<xs:annotation>
<xs:documentation>地址标准类(AddressSpecification)是约束地址及其组成部分的技术标准，可用于地址数据有效性和质量检查。</xs:documentation>
</xs:complexType>
<xs:sequence>
<xs:element name="citation" type="CL_Citation" minOccurs="1" maxOccurs="1"/>
<xs:element name="classSpecification" type="AddressClassSpecification" minOccurs="0" maxOccurs="unbounded"/>
<xs:element name="specifiedAddress" type="Address" minOccurs="0" maxOccurs="unbounded"/>
<xs:annotation>
<xs:documentation>specifiedAddress属性在本标准定义的模型中为必选。</xs:documentation>
</xs:complexType>
</xs:sequence>
</xs:complexType>
</xs:collection>

考虑到 xml 以单条地址对象为记录，为保证其简洁性与可用性，在使用 xml 进行地址数据交换时，此属性可选。

<xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="AddressMetadata">
<xs:annotation>
<xs:documentation>地址元数据类（AddressMetadata）记录了地址的起源和维护信息。
</xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:element name="id" type="Oid" id="id" minOccurs="1" maxOccurs="1"/>
<xs:element name="addressableObjectLifecycleStage" type="AddressableObjectLifecycleStage" minOccurs="0" maxOccurs="1"/>
<xs:element name="provenance" type="AddressProvenance" minOccurs="0" maxOccurs="1"/>
<xs:element name="dataQuality" type="AddressDataQuality" minOccurs="0" maxOccurs="1"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="AddressPosition">
<xs:annotation>
<xs:documentation>表示可赋予地址对象（如建筑物或专属场所等）所在空间位置坐标。
</xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:choice minOccurs="1">
<xs:element name="geometry" type="GM_Object" minOccurs="0" maxOccurs="1"/>
<xs:group ref="XYZ" minOccurs="0" maxOccurs="unbounded"/>
<xs:group ref="LngLatEle" minOccurs="0" maxOccurs="unbounded"/>
</xs:choice>
<xs:element name="coordinateReferenceSystem" type="SC_CRS" minOccurs="1" maxOccurs="1"/>
<xs:element name="type" type="AddressPositionType" minOccurs="0" maxOccurs="1"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="AddressComponentValue">
<xs:annotation>
<xs:documentation>地址组分值（AddressComponentValue）说明了地址组分值及其类别。
</xs:documentation>
</xs:annotation>
<xs:sequence>
26

GB/T 35639—2017

<xs:element name="value" type="xs:anySimpleType" minOccurs="1" maxOccurs="1"/>
<xs:element name="type" type="AddressComponentValueType" minOccurs="0" maxOccurs="1"/>

</xs:sequence>

</xs:complexType>

<xs:complexType name="AddressProvenance">
<xs:annotation>
<xs:documentation>在地址来源类(AddressProvenance)中记录了地址组分或可赋予地址对象的出处、变化以及管理维护地址的组织机构或个体信息。<xs:documentation>
<xs:element name="authority" type="CI_Organisation" minOccurs="1" maxOccurs="1"/>
<xs:element name="owner" type="CI_Organisation" minOccurs="0" maxOccurs="1"/>
<xs:element name="lineage" type="LI_Lineage" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>

<xs:complexType name="Lifecycle">
<xs:annotation>
<xs:documentation>地址生命期类别(Lifecycle)包含地址或可赋予地址对象生命期的描述信息。<xs:documentation>
<xs:element name="validFrom" type="DateTime" minOccurs="1" maxOccurs="1"/>
<xs:element name="validTo" type="DateTime" minOccurs="0" maxOccurs="1"/>
<xs:element name="beginLifespan" type="DateTime" minOccurs="0" maxOccurs="1"/>
<xs:element name="endLifespan" type="DateTime" minOccurs="0" maxOccurs="1"/>
<xs:element name="version" type="xs:string" minOccurs="0" maxOccurs="1"/>
</xs:sequence>
</xs:complexType>

<xs:complexType name="AddressDataQuality">
<xs:annotation>
<xs:documentation>地址数据质量类别(AddressDataQuality)包含地址数据质量的描述信息。<xs:documentation>
<xs:element name="geometryType" type="MD_GeometricObjectTypeCode" minOccurs="1" maxOccurs="1"/>
<xs:element name="dataQuality" type="DQ_DataQuality" minOccurs="0" maxOccurs="1"/>
<xs:element name="collectionTime" type="DateTime" minOccurs="0" maxOccurs="1"/>
<xs:element name="responsibleParty" type="CI_ResponsibleParty" minOccurs="0" maxOccurs="unbounded"/>
</xs:collectionTime>
</xs:complexType>

</xs:sequence>
</xs:complexType>
<xs:complexType name="AddressClassSpecification">
<xs:annotation>
<xs:documentation>地址类标准类别（AddressClassSpecification）包含地址类所引用的标准信息。</xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:element name="class" type="AddressClass" minOccurs="1" maxOccurs="1"/>
<xs:element name="component" type="AddressComponentType" minOccurs="1" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="AddressableObjectType">
<xs:annotation>
<xs:documentation>房屋、地标、寓所和综合楼等建筑物是 AddressableObjectType 代码表的示例。</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string"/>
</xs:simpleType>
<xs:simpleType name="AddressClass">
<xs:annotation>
<xs:documentation>道路地址、地标地址是 AddressClass 代码表的示例。</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string"/>
</xs:simpleType>
<xs:simpleType name="AddressPositionType">
<xs:annotation>
<xs:documentation>中心点、街面和邻近区是 AddressPositionType 代码表的样例代码。</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string"/>
</xs:simpleType>
<xs:simpleType name="ReferenceObjectType">
<xs:annotation>
<xs:documentation>街道、行政区域、个体和组织机构是 AddressPositionType 代码表的示例。</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string"/>
</xs:simpleType>
<xs:simpleType name="AddressComponentType">
<xs:annotation>

<xs:documentation>地址组分类别（Address Component Type）中包括表达共同使用的地址组分类别的值</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string">
    <xs:enumeration value="省级区划名"/>
    <xs:enumeration value="地级区划名"/>
    <xs:enumeration value="县级区划名"/>
    <xs:enumeration value="乡镇/街道级区划名"/>
    <xs:enumeration value="社区/村（居）委名"/>
    <xs:enumeration value="街路巷名"/>
    <xs:enumeration value="片区名"/>
    <xs:enumeration value="地片名"/>
    <xs:enumeration value="标识性地物名"/>
    <xs:enumeration value="居民小区名"/>
    <xs:enumeration value="自然村名"/>
    <xs:enumeration value="村民小组"/>
    <xs:enumeration value="专署区域名"/>
    <xs:enumeration value="门牌号"/>
    <xs:enumeration value="院落名"/>
    <xs:enumeration value="楼牌号"/>
    <xs:enumeration value="建筑物名"/>
    <xs:enumeration value="单元门号"/>
    <xs:enumeration value="楼层"/>
    <xs:enumeration value="户室号"/>
    <xs:enumeration value="信箱号"/>
    <xs:enumeration value="分信箱号"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="AddressComponentValueType">
    <xs:annotation>
        <xs:documentation>地址组分值类别（Address Component Value Type）说明地址组分值的类别</xs:documentation>
        <xs:annotation>
            <xs:restriction base="xs:string">
                <xs:enumeration value="缺省值"/>
                <xs:enumeration value="替代值"/>
            </xs:restriction>
        </xs:simpleType>
        <xs:simpleType name="AddressStatus">
            <xs:annotation>
                <xs:documentation>地址状态（Address Status）包含说明地址状况的值</xs:documentation>
                <xs:annotation>
                    <xs:restriction base="xs:string">

GB/T 35639—2017

<xs:enumeration value="未知"/>
<xs:enumeration value="官方"/>
<xs:enumeration value="非官方"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="AddressLifecycleStage">
<xs:annotation>
<xs:documentation/>
</xs:annotation>

<xs:restriction base="xs:string">
<xs:enumeration value="现行"/>
<xs:enumeration value="规划"/>
<xs:enumeration value="拒绝"/>
<xs:enumeration value="保留"/>
<xs:enumeration value="废弃"/>
<xs:enumeration value="未知"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="AddressObjectLifecycleStage">
<xs:annotation>
<xs:documentation/>
</xs:annotation>

<xs:restriction base="xs:string">
<xs:enumeration value="规划"/>
<xs:enumeration value="批准"/>
<xs:enumeration value="建设中"/>
<xs:enumeration value="在用"/>
<xs:enumeration value="消失"/>
<xs:enumeration value="未知"/>
</xs:restriction>

</xs:simpleType>

<xs:complexType name="Oid">
<xs:annotation>
<xs:documentation>
<xs:documentation>
</xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:element name="localId" type="xs:string"/>
<xs:element name="namespace" type="xs:string"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="GM_Object">
<xs:annotation>

<xs:documentation> GM_Object 是特定参照系下（直接）位置集合的抽象，是抽象化子类别（如 GM_Point、GM_Curve 或 GM_Surface 等）的实例。具体请见 GB/T 23707—2009</xs:documentation>
</xs:annotation>
</xs:complexType>
<xs:group name="XYZ">
<xs:annotation>
<xs:documentation>坐标(x,y,z)<xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:element name="X" type="xs:double" minOccurs="1" maxOccurs="1"/>
<xs:element name="Y" type="xs:double" minOccurs="1" maxOccurs="1"/>
<xs:element name="Z" type="xs:double" minOccurs="0" maxOccurs="1"/>
</xs:sequence>
</xs:group>
<xs:group name="LngLatEle">
<xs:annotation>
<xs:documentation>坐标(lng, lat, z)<xs:documentation>
</xs:annotation>
<xs:sequence>
<xs:element name="longitude" type="xs:double" minOccurs="1" maxOccurs="1"/>
<xs:element name="latitude" type="xs:double" minOccurs="1" maxOccurs="1"/>
<xs:element name="elevation" type="xs:double" minOccurs="0" maxOccurs="1"/>
</xs:sequence>
</xs:group>
<xs:simpleType name="SC_CRS">
<xs:annotation>
<xs:documentation>SC_CRS（基于坐标的空间参照_坐标参照系）采用 GB/T 30170—2013 中定义的 SC_CRS 类别表达</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string"/>
</xs:simpleType>
<xs:complexType name="DateTime">
<xs:annotation>
<xs:documentation>日期时间字符编码，在 ISO 19103 定义了该类数据类型。</xs:documentation>
</xs:annotation>
</xs:complexType>
<xs:complexType name="CI_Organisation">
<xs:annotation>
<xs:documentation>CI_Organisation（引用权威机构）采用 ISO 19115-1:2014 中定义的类别表达</xs:documentation>
</xs:annotation>
</xs:complexType>
</xs:collection>
</xs:collection>

</xs:complexType>

<xs:complexType name="CI_Citation">
    <xs:annotation>
        <xs:documentation>(引用文献)采用 ISO 19115-1:2014 中定义的类别表达</xs:documentation>
    </xs:annotation>
</xs:complexType>

<xs:complexType name="LI_Lineage">
    <xs:annotation>
        <xs:documentation>(数据志)采用 ISO 19115-1:2014 中定义的类别表达</xs:documentation>
    </xs:annotation>
</xs:complexType>

<xs:complexType name="MD_GeometricObjectTypeCode">
    <xs:annotation>
        <xs:documentation>MD_GeometricObjectTypeCode(元数据几何对象类别代码)采用 ISO 19115-1:2014 中定义的类别表达</xs:documentation>
    </xs:annotation>
</xs:complexType>

<xs:complexType name="CI_ResponsibleParty">
    <xs:annotation>
        <xs:documentation>(引用职责方)采用 ISO 19115-1:2014 中定义的类别表达</xs:documentation>
    </xs:annotation>
</xs:complexType>

<xs:complexType name="DQ_DataQuality">
    <xs:annotation>
        <xs:documentation>(数据质量信息)采用 ISO 19115-1:2014 中定义的类别,涉及质量评价范围(包括数据志 &lt;li;LI_Lineage&gt;；和质量元素 &lt;li;DQ_Element&gt;)，对数据质量作总体评价。<xs:documentation>
    </xs:annotation>
</xs:complexType>

</xs:schema>

# 附录 B

（资料性附录）

# 院门/楼址的编制规则

### B.1 一般性原则

依据行政管理机构对街区（块）划分、街路巷以及地名命名等，遵循科学合理、方便寻址的原则，编制门楼址，规范地址中的门楼址编号规则。按照以南北或东西方向线作为门楼址编号的起始线确定门楼址的编制基线和基准点（编号的起点）；或沿某一街道确定门楼址的起点或终点位置（断点）作为基准点；或标识和连接某一地址编配方案结束点与另一方案起始点的标识线（隔离线）作为基线。采用几何线或在某一地址编配系统中编配院门楼址号的行/列间隔线作为门楼址的轮廓线。

### B.2 院门/楼址编配规则

院门/楼址编配规则如下：

a）实行“一院一号、一楼一号”的规则编排院门号和楼号。

b）门楼址号应按照顺序排列，不应跳号、重号。

c) 条带状院门/楼址的编排规则：

1）应以街、路、巷为单位，街路巷两侧门楼址分单、双号编排；

2）沿江、河、铁路等街路巷，仅一侧有建筑物的，应按单侧顺序编排。若另一侧有少量建筑物的，两侧楼门址应相互对应；

3）分段命名的街、路、巷，每条路段应作为独立的街、路、巷独立编排；

4）单一出入口的街、路、巷（俗称死胡同）应不分方向，由入口向里编排。

d) 面状院门/楼址的编排规则：

1）面状居民片区应按先外后里、由近及远、先左后右编排；

2）居民小区内的楼号应按先自北向南、后自东向西的顺序编排。

e）院门/楼址号的编排顺序：

1）东西走向的路、街、巷，应自东向西编排，北侧编单号，南侧编双号；

2）南北走向的路、街、巷，应自北向南编排，西侧编单号，东侧编双号；

3）东北、西南走向的路、街、巷，应自东北向西南编排，右侧编单号，左侧编双号；

4）西北、东南走向的路、街、巷，应自西北向东南编排，右侧编单号，左侧编双号；

5）门牌编号的起点顺序，应以街路巷的稳定方为编号的起点，向街路巷延伸方向按顺序编号。

f）楼房单元号，应按照自东向西、自北向南的顺序编排，楼之间不应连续编排单元号。

g）楼层号应按照由低到高的顺序编排。

h）户室号应以面向楼道入口处，自左至右依次编排。

i) 无院落的平房，以排为单位编排。

i) 旧房翻建、扩建或改建的院楼门，原号符合规定的应沿用原院楼/门址。

k）待建的城市空地，可根据建设规划预留院门/楼址。

## 參 考 文 献

[1] GB/T 7408—2005 数据元和交换格式 信息交换 日期和时间表示法(ISO 8601:2000, IDT)

[2] GB/T 18521—2001 地名分类与类别代码编制规则

[3] GB/T 23705—2009 数字城市地理信息公共平台 地名/地址编码规则

[4] YZ/T 0127—2006 邮政地址信息数据结构

[5] DB11/T 856—2012 门牌、楼牌 设置规范

[6] ISO 19160—1:2015 Addressing—Part 1: Conceptual model