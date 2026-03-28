

# 中华人民共和国国家标准

GB/T 35430—2017

# 信息与文献 期刊描述型元数据元素集

# Information and documentation—Descriptive metadata element set for periodical

2017-12-29 发布

2018-04-01 实施

## 目次

前言 …… III    
引言 …… IV    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 元数据设计原则 …… 2    
4.1 一致性原则 …… 2    
4.2 深度与广度原则 …… 2    
4.3 实用性原则 …… 2    
4.4 可扩展性原则 …… 2    
5 描述单位 …… 2    
6 描述对象间的关系 …… 2    
7 期刊元数据集内容 …… 3    
8 元素及修饰词的定义属性 …… 8    
9 元素与修饰词设置 …… 8    
9.1 标识符中的元素及修饰词 …… 8    
9.2 名称中的元素及修饰词 …… 12    
9.3 卷期标识元素 …… 12    
9.4 责任者中的元素及修饰词 …… 13    
9.5 类型元素 …… 14    
9.6 出版中的元素及修饰词 …… 14    
9.7 日期中的元素及修饰词 …… 15    
9.8 格式中的元素及修饰词 …… 16    
9.9 描述中的元素及修饰词 …… 17    
9.10 主题中的元素及修饰词 …… 21    
9.11 语种元素 …… 22    
9.12 来源中的元素及修饰词 …… 22    
9.13 关联中的元素及修饰词 …… 24    
9.14 馆藏信息中的元素及修饰词 …… 27    
附录 A（资料性附录） 期刊描述型元数据示例 …… 29    
A.1 期刊 …… 29    
A.2 期刊卷期 …… 30    
A.3 期刊论文 …… 30    
A.4 期刊论文中析出的图 …… 32    
A.5 期刊论文中析出的表 …… 32    
A.6 科研项目 …… 32

A.7 个人作者 …… 33  
  
附录 B（资料性附录） 文献类型和文献载体标识代码 …… 34  
  
B.1 文献类型和标识代码 …… 34  
  
B.2 电子资源载体和标识代码 …… 34  
  
参考文献 …… 35

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国信息与文献标准化技术委员会(SAC/TC 4)提出并归口。

本标准起草单位:中国科学技术信息研究所、北京大学信息管理系、中国科学院文献情报中心、中国医学科学院医学信息研究所。

本标准主要起草人：段明莲、赵捷、张建勇、葛红梅、白光武、王星、李学惠。

## 引言

本标准是一部专门供信息资源产出和利用机构、图书馆、信息服务机构以及期刊杂志社等创建期刊数据库使用的国家标准。

本标准主要参考了 GB/T 25100—2010《信息与文献 都柏林核心元数据元素集》，同时也参考了 NISO Z39.96—2015 Journal Archiving and Interchange Tag Library NISO，在元素及属性的设置、定义等方面尽量与 GB/T 25100—2010 保持一致，以达到共建共享期刊书目数据库及期刊全文数据库的目的。

本标准从集合层、个体层以及分析层三个层次描述期刊资源。不仅可以为一种期刊编制集合层记录，为一篇期刊论文编制个体层记录，也可以为期刊论文中析出的任何片段资源编制分析层记录。本标准根据目前用户的需求，将分析层描述对象定为期刊论文中析出的图表。实践中，分析层的描述对象可根据实际需要进一步加以扩展。

# 信息与文献 期刊描述型元数据元素集

## 1 范围

本标准规定了电子期刊、印本期刊、期刊论文、期刊中析出的图或表的描述单位，电子期刊及印本期刊元数据集、期刊论文及图表元数据集、科研项目元数据集以及个人作者元数据集的元素及修饰词设置，本标准确立了期刊、期刊论文、期刊中析出的图或表、参考文献、个人作者、科研项目等描述对象间的关系。

本标准适用于基于原生电子期刊、数字化电子期刊以及印本期刊创建的期刊书目数据库或全文数据库。本标准不对电子期刊的技术信息做专门规定。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改版）适用于本文件。

GB/T 2260 中华人民共和国行政区划代码

GB/T 2659 世界各国和地区名称代码

GB/T 3792.3—2009 文献著录 第 3 部分: 连续性资源

GB/T 4880.2—2000 语种名称代码 第2部分：3字母代码

GB/T 6864—2003 中华人民共和国学位代码

GB/T 7408—2005 数据元和交换格式 信息交换 日期和时间表示法

GB/T 8561 专业技术职务代码

GB/T 25100—2010 信息与文献 都柏林核心元数据元素集

## 3 术语和定义

下列术语和定义适用于本文件。

3.1

描述型元数据 descriptive metadata

对信息资源本身的内容、属性、外在特征进行描述的元数据。

3.2

期刊 periodical

一种定期的、出版频率在每年一次以上的连续出版物。通常期刊的内容为各自独立的论文。

[GB/T 3792.3—2009, 定义 3.22]

### 3.3 

数据库 database

用于指定目的或指定数据处理系统的相关数据的集合。

[GB/T 4894—2009, 定义 4.1.1.4.11]

3.4

修饰词 qualifier

对期刊元数据语义单位的细化，是某一语义单位的属性的描述。修饰词包括元素修饰词和编码体

系修饰词。元素修饰词限定元素含义的范围，使其更具有专指性；编码体系修饰词说明元素值所属的编码体系，编码体系是一类特殊的修饰词，说明元素或修饰词的取值或编码所遵循的规范体系。

### 3.5 

## 元数据 metadata

关于数据的数据。

### 3.6 

## 元素 element

元数据的基本语义单位，描述期刊元数据框架内的基本实体。

## 4 元数据设计原则

### 4.1 一致性原则

在元素和修饰词的设置、定义等方面，应与 GB/T 25100—2010、GB/T 3792.3—2009 等有关标准协调一致。在期刊、期刊卷期以及期刊论文等之间，凡是具有共性特征的元素和修饰词保持横向间的一致性。

### 4.2 深度与广度原则

在深度上，本标准不仅为一种期刊编制集合层记录，为一篇期刊论文编制个体层记录，而且为期刊论文中析出的图表编制分析层记录。分析层的描述对象可根据实际需要进一步加以扩展。在广度上，根据目前的用户需求将描述对象由期刊、期刊论文扩展至期刊论文中析出的图表、期刊作者以及与期刊论文有关的科研项目，以便开展期刊的数据加工、描述、揭示、检索及评价。

### 4.3 实用性原则

根据期刊和期刊论文的特点和用户需求，设计简便易行，具有科学性和可操作性的期刊描述型元数据集。

### 4.4 可扩展性原则

本标准允许使用者在不改变已规定的基本框架和标准内容(如,元素的语义注释)的条件下,适当地扩充一些元素或修饰词。

## 5 描述单位

描述单位可以是期刊中析出的论文或图表，也可以是一种期刊。成套期刊以“种”为单位进行描述。电子期刊中析出的论文以一个具有独立标识（如：一个唯一名称、DOI等）的“文件”为单位进行描述。印本期刊中析出的论文以“篇”为单位进行描述。期刊论文中析出的图或表以“个”为单位进行描述。

## 6 描述对象间的关系

6.1 在期刊、期刊卷期、个人作者、科研项目（包括基金项目）以及期刊中析出的论文、图、表、参考文献之间，存在继承关系、创建关系、资助关系、从属关系或者引用关系，见图1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_204_215_1001_612.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">图 1 期刊、期刊论文等关系框架图</div>


6.2 从属关系。一种期刊与其所含的各卷期之间、一期期刊与其析出的论文之间、单篇论文与其析出的图或表之间存在从属关系。存在从属关系的资源可采用多层次著录法，并用“包含”或“包含于”关联方式予以连接。

6.3 继承关系。期刊是一种连续出版物，由于合并或分开，或从主刊派生出另一种新刊，或编辑出版宗旨发生变化等原因出现刊名变更问题，在旧刊与新刊之间存在继承关系。存在继承关系的资源，可用“继承”或“被继承”关联方式予以连接。

6.4 创建关系。在作者和期刊论文之间存在创建关系。存在创建关系的资源，可用“创建”或“被创建”关联方式予以连接。

6.5 资助关系。资助作者从事科学研究、发表学术论文的科研项目与所发表的研究成果之间存在资助关系。存在资助关系的资源，可用“资助”或“被资助”关联方式予以连接。

6.6 引用关系。期刊论文与参考文献之间存在引用关系。存在引用或参考关系的资源，可用“引用”或“被引用”关联方式予以连接。

## 7 期刊元数据集内容

7.1 印本期刊、电子期刊（包括原生电子期刊和数字化电子期刊）或期刊卷期（即一期期刊），按表1中的元素及修饰词创建期刊书目数据库，其示例参见附录A的A.1。

<div style="text-align: center;">表 1 电子期刊及印本期刊元数据集一览表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">元素</td><td colspan="2">修饰词</td><td rowspan="2">电子期刊</td><td rowspan="2">印本期刊</td><td rowspan="2">期刊卷期</td><td rowspan="2">可重复性</td><td rowspan="2">数据类型</td></tr><tr><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>编码体系修饰词</td></tr><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>来源标识符</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>期标识符</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>ISSN</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr></table>

<div style="text-align: center;">表 1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">元素</td><td colspan="2">修饰词</td><td rowspan="2">电子期刊</td><td rowspan="2">印本期刊</td><td rowspan="2">期刊卷期</td><td rowspan="2">可重复性</td><td rowspan="2">数据类型</td></tr><tr><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>编码体系修饰词</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>EISSN</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>ISSN-L</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>CN</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>CODEN</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>URL</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>并列名称</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>其他名称信息</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>卷期标识</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>责任者</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>个人名称</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>团体名称</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>责任方式</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>出版</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>出版地</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>国别</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>地区代码</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>出版者</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>出版者地址</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>日期</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>日期型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>出版年</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>日期型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>日期型</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>数量</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>尺寸</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>文件格式</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>期刊简介</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>出版频率</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>价格</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>目次</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>编辑部地址</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr></table>

表 1 (续)


<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">元素</td><td colspan="2">修饰词</td><td rowspan="2">电子期刊</td><td rowspan="2">印本期刊</td><td rowspan="2">期刊卷期</td><td rowspan="2">可重复性</td><td rowspan="2">数据类型</td></tr><tr><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>编码体系修饰词</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>邮编</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>电话</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>E-mail</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>传真</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>主题</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>中图法</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>关键词</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>语种</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>枚举型</td></tr><tr><td style='text-align: center;'>关联</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>继承</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>被继承</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>部分继承</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>被部分继承</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>吸收</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>并入</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>包含</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>馆藏信息</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>馆藏地</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>馆藏单位</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>索取号</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td colspan="8">注1：在元素和修饰词的必备性方面，“M”表示必备(Mandatory),“A”表示有则必备(Mandatory if Applicable),“O”表示可选(Optional)。注2：在元素和修饰词的重复性方面，“R”表示可重复(Repeatable),“NR”表示不可重复(Not Repeatable)。</td></tr></table>

7.2 从印本期刊、电子期刊中析出的论文、图或表，按表2中的元素及修饰词创建期刊全文数据库或期刊图表数据库，其示例参见附录A的A.3～A.5。

<div style="text-align: center;">表 2 期刊论文及图表元数据集一览表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">元素</td><td colspan="2">修饰词</td><td rowspan="2">期刊论文</td><td rowspan="2">图</td><td rowspan="2">表</td><td rowspan="2">可重复性</td><td rowspan="2">数据类型</td></tr><tr><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>编码体系修饰词</td></tr><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>论文标识符</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>图标识符</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr></table>

<div style="text-align: center;">表 2（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">元素</td><td colspan="2">修饰词</td><td rowspan="2">期刊论文</td><td rowspan="2">图</td><td rowspan="2">表</td><td rowspan="2">可重复性</td><td rowspan="2">数据类型</td></tr><tr><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>编码体系修饰词</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>表标识符</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>DOI</td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>并列名称</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>其他名称信息</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>责任者</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>个人名称</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>团体名称</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>责任方式</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>工作单位</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>摘要</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>项目来源</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>类型</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>枚举型</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>文件格式</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>主题</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>中图法</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>关键词</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>M</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>汉语主题词表</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>语种</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>枚举型</td></tr><tr><td style='text-align: center;'>来源</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>来源名称</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>年</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>日期型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>卷</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>期</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>页</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>关联</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>包含于</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>被创建</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>被资助</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>引用</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr></table>

7.3 基金或机关团体资助科学研究的项目，按表 3 中的元素及修饰词创建科研项目数据库，其示例参见附录 A 的 A.6。

<div style="text-align: center;">表 3 科研项目元数据集一览表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>可重复性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>项目标识符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>项目编号</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>项目名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>其他名称信息</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>项目来源</td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>资助机构</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>附注</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>关联</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>资助</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr></table>

7.4 个人作者按表 4 中的元素及修饰词创建个人作者数据库，其示例参见附录 A 的 A.7。

<div style="text-align: center;">表 4 个人作者元数据集一览表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>元素修饰词</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>可重复性</td><td style='text-align: center;'>数据类型</td></tr><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>个人标识符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>责任者</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>个人名称</td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>个人并列名称</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>工作单位</td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>邮编</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>学位</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>职称</td><td style='text-align: center;'>O</td><td style='text-align: center;'>NR</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>研究方向</td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>E-mail</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>附注</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'>关联</td><td style='text-align: center;'></td><td style='text-align: center;'>A</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>创建</td><td style='text-align: center;'>O</td><td style='text-align: center;'>R</td><td style='text-align: center;'>字符型</td></tr></table>

## 8 元素及修饰词的定义属性

为规范元素及修饰词等术语的定义，本标准通过名称、标签、定义、注释、术语类型、数据类型、必备性以及可重复性这几个属性对元素及修饰词进行定义，见表5。

<div style="text-align: center;">表 5 期刊元数据集规范术语定义属性表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>属性名</td><td style='text-align: center;'>属性定义</td><td style='text-align: center;'>必备性</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>赋予术语的唯一标记，一般为英文小写</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>描述术语的可读标签一般为中文，可随资源不同选择不同的描述术语</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>对术语概念与内涵的说明</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>注释</td><td style='text-align: center;'>关于术语或其应用的其他说明，如特殊的用法等</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>术语类型</td><td style='text-align: center;'>术语的类型，其值为：元素、元素修饰词和编码体系修饰词</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>术语允许取值的数据类型</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>必备性包括必备、有则必备、可选</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>可重复性</td><td style='text-align: center;'>可重复性包括可重复和不可重复</td><td style='text-align: center;'>必备</td></tr></table>

本标准中元素的“名称”为英文，以便于计算机标记和编程。为了便于人们阅读，“标签”为中文。本标准定义的所有元素及元素修饰词与排列顺序有一定关系，但使用单位可根据自身的实际需要决定元素、元素修饰词以及编码体系修饰词的排列次序。

## 9 元素与修饰词设置

### 9.1 标识符中的元素及修饰词

#### 9.1.1 标识符

名称:identifier

标签:标识符

定义: 在特定上下文环境中, 给予资源的一个明确的标识。

注释：一般采用字符串或数字代码。建议采用符合正式标识体系的字符串进行标识。

术语类型:元素

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.2 来源标识符

名称:sourceId

标签: 来源标识符

定义: 出版物来源的唯一标识符。

注释：本标准中的来源标识符用于标识一种特定的期刊。

术语类型:元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.3 期标识符

名称:issueId

标签: 期标识符

定义: 识别特定一期期刊的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.4 论文标识符

名称：articleId

标签: 论文标识符

定义: 识别期刊中特定论文的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.5 图标识符

名称：figureId

标签: 图标识符

定义:识别期刊论文中特定图的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.6 表标识符

名称: tableId

标签: 标识符

定义:识别期刊论文中特定表的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.7 ISSN

名称：issn

标签:ISSN

定义: 国际标准连续出版物号(International Standard Serial Number)。

## GB/T 35430—2017

术语类型: 编码体系修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9 \.1\.8 EISSN

名称：eissn

标签:EISSN

定义: 电子期刊的国际标准连续出版物号。

术语类型: 编码体系修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.1.9 ISSN-L

名称: linkingIssn

标签:ISSN-L

<div style="text-align: center;"><img src="imgs/img_in_image_box_40_753_78_791.jpg" alt="Image" width="3%" /></div>


定义:由 ISSN 网络指定启用配置或链接连续性资源不同媒介版本的国际标准连续出版物号。

术语类型: 编码体系修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9 \.1\.10 CN

名称：cn

标签:CN

定义：国内期刊统一编号。

术语类型:编码体系修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9 \.1\.11 CODEN

名称: coden

标签: CODEN

定义: 国际 CODEN 组织分配给连续出版物题名的唯一且无二义性的缩写代码。

术语类型: 编码体系修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.1.12 DOI

名称：___ doi：___

标签:DOI

定义: 数字对象唯一标识符 (Digital Object Identifier, 简称 DOI)。

术语类型：编码体系修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.1.13 个人标识符

名称: personalId

标签:个人标识符

定义: 识别特定个人名称记录的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.14 项目标识符

名称: projectId

标签: 项目标识符

定义:识别特定科研项目记录的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.1.15 项目编号

名称: projectNumber

标签: 项目编号

定义:资助机构分配给科研项目的正式编号。

术语类型：元素修饰词

数据类型: 字符型

必备性: 必备

可重复性：不可重复

#### 9.1.16 URL

名称: URL

标签: URL

定义:统一资源定位符(Uniform Resource Locator,简称URL)是互联网上用来标识某一特定信息页所用的一个短的字符串。

术语类型：编码体系修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

### 9.2 名称中的元素及修饰词

#### 9.2.1 名称

名称：title

标签:名称

定义：赋予资源的名称。

注释：一般指资源正式公开的名称，如，刊名、期刊论文的篇名等。

术语类型：元素

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.2.2 并列名称

名称:parallelTitle

标签: 并列名称

定义: 用另一种语言文字表示的名称。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.2.3 项目名称

名称: projectName

标签: 项目名称

定义: 获取资助的科研项目名称。

注释：包括基金或其他渠道获得资助的科研项目名称。

术语类型:元素修饰词

数据类型: 字符型

必备性：必备

可重复性:不可重复

#### 9.2.4 其他名称信息

名称: otherTitleInformation

标签:其他名称信息

定义：用来限定、补充、解释、说明正式名称的文字。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

### 9.3 卷期标识元素

名称：numericDesignation

标签: 卷期标识

定义：期刊的年卷期标识。

注释：建议采用“年，卷（期）-年，卷（期）”格式，标识成套期刊首卷与末卷的卷期标识。

术语类型：元素

数据类型: 字符型

必备性：可选

可重复性：不可重复

### 9.4 责任者中的元素及修饰词

#### 9.4.1 责任者

名称: ___

标签: 责任者

定义: 对资源的知识内容或艺术内容负责的个人或团体。

术语类型：元素

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.4.2 个人名称

名称: personalName

标签:个人名称

定义: 对资源的知识内容或艺术内容负责的个人。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.4.3 个人并列名称

名称:parallelName

标签:个人并列名称

定义: 用另一种语言文字表示的个人名称。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.4.4 团体名称

名称:corporateName

标签:团体名称

定义: 对资源的知识内容或艺术内容负责的团体。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.4.5 责任方式

名称：role

标签:责任方式

定义: 对资源的知识内容或艺术内容进行创作、整理的方式。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

### 9.5 类型元素

名称:type

标签: 类型

定义:资源的特征或类型。

注释：建议本元素中文献类型标识按附录 B 取值。

术语类型：元素

数据类型: 枚举型

必备性：有则必备

可重复性：不可重复

### 9.6 出版中的元素及修饰词

#### 9.6.1 出版

名称：publication

标签: 出版

定义：与资源的出版、发行等活动有关的数据。

术语类型：元素

数据类型: 字符型

必备性:有则必备

可重复性：可重复

#### 9.6.2 出版地

名称: placeOfPublication

标签: 出版地

定义: 出版者所在地的城市名称。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.6.3 国别

名称：country

标签: 国别

定义：出版者所在地的国别。

注释：本元素修饰词的取值建议采用 GB/T 2659，用三个字符代码标识期刊出版地的国别。

术语类型：元素修饰词

数据类型: 字符型

必备性: 有则必备

可重复性：不可重复

#### 9.6.4 地区代码

名称：areaCode

标签: 地区代码

定义: 出版者所在地的地区代码。

注释：本元素修饰词的取值建议采用 GB/T 2260。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

<div style="text-align: center;"><img src="imgs/img_in_image_box_64_757_102_796.jpg" alt="Image" width="3%" /></div>


#### 9.6.5 出版者

名称：___

标签: 出版者

定义:使资源可以获得和利用的责任实体。

术语类型: 元素修饰词

数据类型: 字符型

必备性: 有则必备

可重复性：不可重复

#### 9.6.6 出版者地址

名称：___

标签: 出版者地址

定义：出版者的通信地址。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

### 9.7 日期中的元素及修饰词

#### 9 \.7\.1 日期

名称:date

标签: 日期

定义:与资源生命周期中的一个事件相关的时刻或一段时间。

术语类型：元素

数据类型: 日期型

必备性：有则必备

可重复性：不可重复

#### 9.7.2 出版年

名称: published

标签: 出版年

定义:资源正式出版的日期。

注释:本元素修饰词的取值建议采用 GB/T 7408—2005, 按照“YYYY-MM-DD”的格式标识出版年。

<div style="text-align: center;"><img src="imgs/img_in_image_box_93_516_130_549.jpg" alt="Image" width="3%" /></div>


术语类型: 元素修饰词

数据类型：日期型

必备性：有则必备

可重复性：不可重复

#### 9.7.3 发布日期

名称:issued

标签：发布日期

定义:资源正式发布的日期。

注释：电子期刊的发布日期取值建议采用 GB/T 7408—2005，按照“YYYY-MM-DD”的格式标识发布日期。

术语类型: 元素修饰词

数据类型: 日期型

必备性：有则必备

可重复性：不可重复

### 9.8 格式中的元素及修饰词

#### 9.8.1 格式

名称:format

标签: 格式

定义: 资源的文件格式、物理媒体或尺寸规格。

术语类型：元素

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.8.2 数量

名称：extent

标签:数量

定义: 资源的数量及其特定资源标识的单位。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.8.3 尺寸

名称:dimension

标签:尺寸

定义: 印本资源的尺寸。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.8.4 文件格式

名称: fileFormat

标签: 文件格式

定义：一种文件结构，用以确定文件存储方式和文件在屏幕上或打印时表示方式。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：可重复

### 9.9 描述中的元素及修饰词

#### 9.9.1 描述

名称:description

标签: 描述

定义: 资源的说明解释。

术语类型：元素

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.9.2 期刊简介

名称: synopsis

标签: 期刊简介

定义: 简要介绍期刊内容的文字。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.9.3 出版频率

名称：frequency

标签:出版频率

定义: 单位时间内期刊出版的次数。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：可重复

#### 9.9.4 价格

名称: price

标签:价格

定义:商品价值的货币表现。

注释：一种或一期期刊的价格。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.9.5 目次

名称: contents

标签: 目次

定义:资源组成单元的列表。

注释：一期期刊的内容目次单独存为一个文件，需标注特定目次的文件名，以便计算机通过目次文件名链接特定的目次。

术语类型: 元素修饰词标注

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.9.6 摘要

名称:abstract

标签:摘要

定义:论文内容的简要陈述,是一篇具有独立性和完整性的短文,一般以第三人称语气写成,不加评论和补充的解释。

术语类型: 元素修饰词

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.9.7 项目来源

名称: projectSource

标签:项目来源

定义:科研项目的来源。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性:不可重复

#### 9.9.8 资助机构

名称: supportBody

标签:资助机构

定义: 提供科研项目资金的机构。

术语类型：元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.9 工作单位

名称：aff

标签: 工作单位

定义: 论文责任者所属机构或组织的名称。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.9.10 邮编

名称: zipCode

标签:邮编

定义: 邮政部门为了分拣、投递方便、迅速, 按地区编程的号码。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.11 学位

名称: degree

标签:学位

定义:由高等院校、科研机构等按学科门类和专业学位类型授予受教育者的称号。

注释：本元素修饰词的取值建议采用 GB/T 6864—2003。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.12 职称

名称：academicTitle

标签: 职称

定义：专业技术职务的名称。

注释：本元素修饰词的取值建议采用 GB/T 8561。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：不可重复

#### 9.9.13 研究方向

名称：researchDirection

标签:研究方向

定义：作者科学研究的方向。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.9.14 编辑部地址

名称:address

标签:编辑部地址

定义：编辑部的通讯地址。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.15 E-mail

名称：E-mail

标签:e-mail

定义: 电子邮件。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.16 电话

名称: phone

标签:电话

定义：编辑部的电话号码。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.17 传真

名称：fax

标签:传真

定义: 传真号码。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.9.18 附注

名称:note

标签:附注

定义:用以揭示在其他元素或修饰词中不能涵盖的书目信息,以便进一步说明资源的性质、特征、用途以及范围等。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

### 9.10 主题中的元素及修饰词

#### 9.10.1 主题

名称：subject

标签:主题

定义: 资源的主题。

注释：一般采用关键词、关键词短语或分类号来标识。建议使用受控词表。

术语类型: 元素

数据类型: 字符型

必备性：必备

可重复性：不可重复

#### 9.10.2 中图法

名称：CLC

标签: 中图法

定义: 中国图书馆分类法。

注释:本编码体系修饰词的取值建议采用2010年国家图书馆出版社出版的《中国图书馆分类法》第五版。

术语类型：编码体系修饰词

数据类型: 字符型

必备性：必备

可重复性：可重复

#### 9.10.3 关键词

名称：___

标签: 关键词

定义: 直接以自然语言中未经控制或只作少量控制的语词标引资源的主题内容。

术语类型:元素修饰词

数据类型: 字符型

必备性：必备

可重复性：可重复

#### 9.10.4 汉语主题词表

名称：CT

标签: 汉语主题词表

定义：汉语主题词表。

术语类型: 编码体系修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

### 9.11 语种元素

名称：language

标签:语种

定义:资源正文的语种。

注释：正文语种的取值建议采用 GB/T 4880.2—2000，用“chi、eng、fre、gem、jpn、kor、rus”等分别表示“汉语、英语、法语、德语、日语、韩语、俄语”。

术语类型:元素

数据类型: 枚举型

必备性：必备

可重复性：可重复

### 9.12 来源中的元素及修饰词

#### 9.12.1 来源

名称:source

标签:来源

定义:与当前资源来源有关的资源。

术语类型：元素

数据类型: 字符型

必备性：有则必备

<div style="text-align: center;"><img src="imgs/img_in_image_box_33_1437_70_1473.jpg" alt="Image" width="3%" /></div>


可重复性：不可重复

#### 9.12.2 来源名称

名称:sourceTitle

标签: 来源名称

定义:本资源的来源名称。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9 \.12\.3 年

名称：year

标签:年

定义: 期刊卷期标识中的年。

术语类型: 元素修饰词

数据类型: 日期型

必备性：有则必备

可重复性：不可重复

#### 9.12.4 卷

名称: volume

<div style="text-align: center;"><img src="imgs/img_in_image_box_39_779_77_816.jpg" alt="Image" width="3%" /></div>


标签:卷

定义: 期刊卷期标识中的卷。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性:不可重复

#### 9.12.5 期

名称: issue

标签:期

定义: 期刊卷期标识中的期。

术语类型: 元素修饰词

数据类型: 字符型

必备性: 有则必备

可重复性：不可重复

#### 9.12.6 页

名称:page

标签:页

定义:本资源在来源资源中的页码。

注释：论文的页码包括特定论文在期刊中的起止页码、转页的页码等。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

### 9.13 关联中的元素及修饰词

#### 9 \.13\.1 关联

名称：relation

标签: 关联

定义: 相关资源。

注释：指明与本资源存在某种关系的其他资源。建议采用符合正式标识体系的字符串进行标识。

术语类型: 元素

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.2 继承

名称: continues

标签:继承

定义: 期刊更名后, 被新刊取代的旧刊。

注释：建议按旧刊的“名称.ISSN”格式提供连接信息，以便计算机自动获取旧刊的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.3 被继承

名称: continuedBy

标签：被继承

定义: 期刊更名后, 取代旧刊的新刊。

注释：建议按新刊的“名称.ISSN”格式提供连接信息，以便计算机自动获取新刊的唯一标识符。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.4 部分继承

名称: continuesInPart

标签:部分继承

定义：被新刊部分继承的期刊。

注释:建议按旧刊的“名称.ISSN”格式提供连接信息,以便计算机自动获取被部分取代的旧刊的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.5 被部分继承

名称: continuedInPartBy

标签：被部分继承

定义：部分继承旧刊的新刊。

注释:建议按新刊的“名称.ISSN”格式提供连接信息,以便计算机自动获取部分继承旧刊的新刊的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.6 吸收

名称:absorbed

标签: 吸收

定义: 被在编期刊吸收的期刊。

注释：建议按旧刊的“名称.ISSN”格式提供连接信息，以便计算机自动获取被在编期刊吸收的旧刊的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.7 并入

名称:absorbedBy

标签: 并入

定义: 吸收了在编期刊的另一期刊。

注释：建议按新刊的“名称.ISSN”格式提供连接信息，以便计算机自动获取吸收了在编期刊的新刊的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.8 包含

名称: hasPart

标签:包含

定义:本资源在物理上或逻辑上包含了另一资源。

注释:建议按期刊论文的“责任者的个人名称.论文名称”格式提供连接信息,以便计算机获取被包含的期刊论文的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.13.9 包含于

名称: isPartOf

标签:包含于

定义:本资源在物理上或逻辑上是另一资源的一个组成部分。

注释：建议按期刊的“刊名，年，卷（期）”格式提供连接信息，以便计算机获取特定一期期刊的唯一标识符。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9 \.13\.10 创建

名称：creats

标签: 创建

定义:作者撰写的期刊论文。

注释:建议按期刊论文的“责任者的个人名称.论文名称.刊名,年,卷(期):页”格式提供连接信息,以便计算机获取特定期刊论文的唯一标识符或DOI。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.13.11 被创建

名称: createdBy

标签: 被创建

定义：期刊论文被作者撰写。

注释:建议按“论文作者姓名.工作单位”格式提供连接信息,以便计算机获取特定期刊论文作者的唯一标识符。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.12 引用

名称: references

标签: 引用

定义：说明本资源参照、引用或以其他方式指向另一资源。

注释：用“引用”元素修饰词指向被本资源所引用的参考文献。建议按“责任者的个人名称.题名”格式提供连接信息，以便计算机获取被引资源的唯一标识符。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.13.13 资助

名称：funds

标签:资助

定义: 科研项目所资助的学术论文。

注释：建议按期刊论文的“责任者的个人名称.论文名称.刊名，年，卷（期）：页”格式提供连接信息，以便计算机获取科研项目资助的期刊论文的唯一标识符。

术语类型:元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.13.14 被资助

名称：fundedBy

标签: 被资助

定义: 学术论文源于被资助的科研项目。

注释：建议按科研项目的“名称.项目编号”格式提供连接信息，以便计算机获取特定科研项目的唯一标识符。

术语类型: 元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

### 9.14 馆藏信息中的元素及修饰词

#### 9.14.1 馆藏信息

名称：location

标签:馆藏信息

定义：资源的馆藏信息。

术语类型:元素

数据类型: 字符型

必备性：有则必备

可重复性：不可重复

#### 9.14.2 馆藏地

名称: placeOfHoldingAgency

标签:馆藏地

定义：资源馆藏单位所在地。

术语类型: 元素修饰词

数据类型: 字符型

必备性：可选

可重复性：可重复

#### 9.14.3 馆藏单位

名称: holdingAgency

标签:馆藏单位

定义: 资源的收藏单位。

注释：在本标准中指期刊收藏单位。

术语类型:元素修饰词

数据类型: 字符型

必备性：有则必备

可重复性：可重复

#### 9.14.4 索取号

名称: callNumber

标签:索取号

定义: 代表每一资源在收藏单位整个馆藏体系中特有位置的号码。

注释：在本标准中是指期刊收藏单位。

数据类型: 字符型

必备性：有则必备

可重复性：可重复

# 附 录 A （资料性附录） 期刊描述型元数据示例

### A.1 期刊

示例1：标识符[来源标识符]：112001365379

[ISSN]:1009-6337

[CN]:11-4542

名称：中国国家地理

卷期标识：2000（1）

责任者[个人名称]：单之蔷

[责任方式]：主编

[团体名称]：中国科学院地理科学与资源研究院

[责任方式]：主办

[团体名称]：中国地理学会

[责任方式]：主办

[团体名称]：中国科学院

[责任方式]：主管

出版[出版地]：北京

[出版者]：《中国国家地理》杂志社

[出版者地址]：北京市朝阳区安外大屯路甲11号地理科学馆

日期[出版年]：2000-

格式[数量]：v.

[尺寸]：26cm.

描述[期刊简介]：《中国国家地理》在秉承保护地球、探索未知、推进

物、人文、历史诸领域新近发生的有价值的事件及重

都市白领的生活方式，探险的经历，著名科学家的

的话题。

[出版频率]：月刊

[编辑部地址]：北京市朝阳区安外大屯路甲11号地理科学馆

[邮编]：100101

[电话]：010-64865566-376

[E-mail]：bjb@cng.com.cn

[传真]：010-64842217

主题[中图法]：P9

[关键词]：中国

[关键词]：地理

语种：chi

关联[继承]：地理知识.ISSN 0257-019X

示例2：标识符[来源标识符]：111999086549

[ISSN]:0257-019X

[CN]:11-1494

名称：地理知识

描述[期刊简介]:《中国国家地理》在秉承保护地球、探索未知、推进文明的基础上,又涉及了天文、地理、生物、人文、历史诸领域新近发生的有价值的事件及重大考古发现,后旅游时代出行的理由,都市白领的生活方式,探险的经历,著名科学家的人生轨迹,文化版图的胀缩等各种有趣的话题。

[并列名称]: Geographical knowledge

卷期标识: 1950(1)-2000(9)

责任者[个人名称]: 中国地理学会

[责任方式]: 主办

[团体名称]: 中国科学院

[责任方式]: 主办

[团体名称]: 国家计划委员会地理研究所

[责任方式]: 主办

出版[出版地]: 北京

[出版者]: 科学出版社

[出版者地址]: 北京东黄城根北街16号

日期[出版年]: 1950-2000

格式[数量]: 39 v.

[尺寸]: 26 cm.

描述[出版频率]: 月刊(1975,8-2000)

[出版频率]: 双月刊(1973-1975,7)

[出版频率]: 月刊(1950-1972)

[编辑部地址]: 北京市朝阳区安外大屯路甲11号地理科学馆

[邮编]: 100101

[电话]: 010-64865566-376

[E-mail]: bjb@cng.com.cn

[传真]: 010-64842217

主题[中图法]: P9

[关键词]: 中国

[关键词]: 地理

语种: chi

关联[被继承]: 中国国家地理.ISSN 1009-6337

### A.2 期刊卷期

示例:标识符[期标识符]:112016

名称:中国国家地理

卷期标识:2016(4)

描述[价格]:CNY 20.00

[目次]:zhongguoguojiadili201604.pdf

### A.3 期刊论文

<div style="text-align: center;"><img src="imgs/img_in_image_box_180_1339_215_1373.jpg" alt="Image" width="2%" /></div>


示例 1: 标识符[论文标识符]:

[DOI]:10.16509/j.georeview.2016.02.001

名称: 揭开南岭地壳形成演化之谜

责任者[个人名称]: 杨文采

[工作单位]: “大地构造与动力学”国家重点实验室

[工作单位]: 中国地质科学院地质研究所

类型: J/OL

格式[文件格式]: pdf

描述[摘要]: 南岭的形成演化目前尚不清楚, 作为板内造山的一个典型, 研究南岭地区的地壳构造对大陆动

力学有重要意义。本文对南岭地区重力异常进行了多尺度密度反演，首先利用小波变换对重力异常进行多尺度分解，接着利用功率谱分析方法估算各等效层场源的平均深度，然后利用广义线性反演方法进行各层密度反演，取得区域地壳多个深度上的密度扰动图像。用小波变换多尺度分析和三维密度结构反演确定了南岭中上地壳存在独立的构造单元，它具有低密度性质，反映区域规模的大花岗岩基。南岭中上地壳的构造单元于北纬 $ 24^{\circ}\sim26^{\circ} $ ，东经 $ 100^{\circ}\sim116^{\circ} $ ，深达22 km左右。深度22 km以下南岭地壳低密度带与武夷低密度带连通为武夷—云开构造带。南岭最终形成与100 Ma以前特提斯洋俯冲和亚欧板块与加里曼丹地体的陆岛碰撞直接有关。同期发生的区域规模的燕山晚期南岭花岗岩基对应特提斯洋向华南俯冲的第二岩浆带。基于地球物理资料提出的这个陆岛俯冲碰撞假说能否成立，还需要更多岩石学的直接证据证实。

[项目来源]: 国家自然科学基金资助项目(编码: 41574111)的成果。

主题[中图法]:P54

[关键词]: 小波多尺度分解

[关键词]: 密度反演

[关键词]: 地壳密度结构

[关键词]:中国南岭

[关键词]:形成演化

[关键词]:俯冲的第二岩浆带

语种: chi

来源[来源名称]:地质论评

[年]:2016

[卷]:62

 $$ 期 $$ :2

关联[包含于]:地质论评.ISSN 0371-5736

[被资助]: 国家自然科学基金资助项目.41574111

[被创建]: 杨文采.“大地构造与动力学”国家重点实验室

示例 2: 标识符 [论文标识符]:

名称：CCR5：抗 HIV-1 药物的新靶点

[并列名称]: CCR5, a new target of anti-HIV drugs

责任者[个人名称]:韩燕星

[工作单位]: 中国医学科学院中国协和医科大学医药生物技术研究所病毒室

[个人名称]: 蒋建东

类型：J/OL

格式[文件格式]:pdf

描述[摘要]：CCR5为细胞膜蛋白，属于G蛋白偶联受体家族的成员，是HIV-1入侵机体细胞的主要辅助受体之一。在过去的几年中，对CCR5的生物学特性以及在HIV感染过程中所起作用的研究取得了明显的进展，以CCR5为靶点的HIV受体拮抗剂倍受关注，主要有以下4种：（1）趋化因子衍生物；（2）低分子量非肽类；（3）单克隆抗体；（4）肽类化合物。本文综述了近年来CCR5和以其为靶点的HIV受体拮抗剂的研究进展。

[项目来源]: 国家自然科学基金资助项目(编码:39930190)的成果。

主题[中图法]: Q26

[关键词]:CCR5

[关键词]: 结构

[关键词]: 功能

[关键词]：手提拮抗剂
语种：chi
来源[来源名称]：中国医学科学院学报
[年]:2003
[卷]:25
[期]:5
[页]:635-639
关联[包含于]：中国医学科学院学报.ISSN1000-503X
[被资助]：国家自然科学基金资助项目.39930190
[被创建]：韩燕星.中国医学科学院中国协和医科大学医药生物技术研究所病毒室
[被创建]：蒋建东.中国医学科学院中国协和医科大学医药生物技术研究所病毒室

### A.4 期刊论文中析出的图

示例：标识符[图标识符]：
名称：南海100～5 Ma构造演化图解
[其他名称信息]：（a）100 Ma，（b）80 Ma，（c）30 Ma，（d）5 Ma
责任者[个人名称]：杨文采
格式[文件格式]：pdf
主题[中图法]：P54
[关键词]：南海
[关键词]：构造演化
来源[来源名称]：地质论评
[年]：2016
[卷]：62
[期]：2
[页]：263
关联[包含于]：杨文采.揭开南岭地壳形成演化之谜.DOI:10.16509/j.georeview.2016.02.001

### A.5 期刊论文中析出的表

示例：标识符[表标识符]：
名称：地壳结晶岩石密度 $ g/cm^{3} $  统计表
责任者[个人名称]：杨文采
格式[文件格式]：pdf
主题[中图法]：P58
[关键词]：地壳
[关键词]：岩石密度
来源[来源名称]：地质论评
[年]：2016
[卷]：62
[期]：2
[页]：260
关联[包含于]：杨文采.揭开南岭地壳形成演化之谜.DOI:10.16509/j.georeview.2016.02.001

### A.6 科研项目

示例：标识符[项目标识符]：

[项目编目]:39930190

名称[项目名称]：抗肿瘤、抗病毒与心血管药物筛选新模型的研究与应用

描述[项目来源]: 国家自然科学基金 1999 年度重点项目

关联[包含]：韩燕星，蒋建东.CCR5：抗HIV-1药物的新靶点.中国医学科学院学报，2003，25（5）：635-639

[包含]：刘晓辉，洪斌，王丽非，杨媛，司书毅，李元.人高密度脂蛋白受体表达上调剂筛选模型的建立.中国医学科学院学报，2004，26（4）：354-358

[包含]: 张忠兵.B族Ⅰ型清道夫受体及与动脉粥样硬化关系研究进展.中国分子心脏病学杂志,2005,5(3):553-556

[包含]: TIAN D F, HONG B, SI S Y. Development of a new high-throughput screening model for human high density lipoprotein receptor (CLA-1) agonists. Biomedical and environmental sciences, 2005, 18:265-272

### A.7 个人作者

示例 1: 标识符 [个人标识符]:

责任者[个人名称]：韩燕星

[个人并列名称]: Han Yan-xing

[工作单位]:中国医学科学院中国协和医学大学医药生物技术研究所病毒室

[邮编]:100050

描述 $$ E-mail $$ : hanyanxing@hotmail.com

关联[创建]：韩燕星，蒋建东.CCR5：抗HIV-1药物的新靶点

示例 2: 标识符 [个人标识符]:

责任者[个人名称]: 杨文采

[个人并列名称]: Yang Wen-cai

[工作单位]：“大地构造与动力学”国家重点实验室

[工作单位]:中国地质科学院地质研究所

[邮编]:100037

描述[学位]:博士

[职称]:研究员,中国科学院院士

[研究方向]: 固体地球物理学

[E-mail]: yangwencai@cashq.ac.cn

关联[创建]: 杨文采. 揭开南岭地壳形成演化之谜

附录 B

(资料性附录)

文献类型和文献载体标识代码

### B.1 文献类型和标识代码

文献类型和标识代码见表 B.1。

<div style="text-align: center;">表 B.1 文献类型和标识代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考文献类型</td><td style='text-align: center;'>文献类型标识代码</td></tr><tr><td style='text-align: center;'>普通图书</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>会议录</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>汇编</td><td style='text-align: center;'>G</td></tr><tr><td style='text-align: center;'>报纸</td><td style='text-align: center;'>N</td></tr><tr><td style='text-align: center;'>期刊</td><td style='text-align: center;'>J</td></tr><tr><td style='text-align: center;'>学位论文</td><td style='text-align: center;'>D</td></tr><tr><td style='text-align: center;'>报告</td><td style='text-align: center;'>R</td></tr><tr><td style='text-align: center;'>标准</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>专利</td><td style='text-align: center;'>P</td></tr><tr><td style='text-align: center;'>数据库</td><td style='text-align: center;'>DB</td></tr><tr><td style='text-align: center;'>计算机程序</td><td style='text-align: center;'>CP</td></tr><tr><td style='text-align: center;'>电子公告</td><td style='text-align: center;'>EB</td></tr><tr><td style='text-align: center;'>档案</td><td style='text-align: center;'>A</td></tr><tr><td style='text-align: center;'>舆图</td><td style='text-align: center;'>CM</td></tr><tr><td style='text-align: center;'>数据集</td><td style='text-align: center;'>DS</td></tr><tr><td style='text-align: center;'>其他</td><td style='text-align: center;'>Z</td></tr></table>

### B.2 电子资源载体和标识代码

电子资源载体和标识代码见表 B.2。

<div style="text-align: center;">表 B.2 电子资源载体和标识代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>电子资源的载体类型</td><td style='text-align: center;'>载体类型标识代码</td></tr><tr><td style='text-align: center;'>磁带(magnetic tape)</td><td style='text-align: center;'>MT</td></tr><tr><td style='text-align: center;'>磁盘(disk)</td><td style='text-align: center;'>DK</td></tr><tr><td style='text-align: center;'>光盘(CD-ROM)</td><td style='text-align: center;'>CD</td></tr><tr><td style='text-align: center;'>联机网络(online)</td><td style='text-align: center;'>OL</td></tr></table>

## 參 考 文 献

[1] GB/T 7714—2015 信息与文献 参考文献著录规则

[2] 国家图书馆. 新版中国机读目录格式使用手册 [M]. 北京: 北京图书馆出版社, 2004.

[3] 谢琴芳. CALIS 联机合作编目手册：上. 北京：北京大学出版社，2000.