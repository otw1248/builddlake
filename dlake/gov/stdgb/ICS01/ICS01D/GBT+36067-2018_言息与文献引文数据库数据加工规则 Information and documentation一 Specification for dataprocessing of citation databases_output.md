

# 中华人民共和国国家标准

GB/T 36067—2018

# 信息与文献 引文数据库数据加工规则

# Information and documentation—Specification for data processing of citation databases

2018-03-15 发布

2018-10-01 实施

## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 引文数据加工原则 …… 2  
  
4.1 完整性原则 …… 2  
  
4.2 准确性原则 …… 2  
  
4.3 客观性原则 …… 2  
  
4.4 扩展与关联原则 …… 2  
  
4.5 先进性原则 …… 2  
  
5 引文数据著录总则 …… 2  
  
5.1 著录信息源 …… 2  
  
5.2 著录文字与符号 …… 2  
  
5.3 引文数据关联 …… 3  
  
6 引文加工要求及基本元素名称表 …… 3  
  
6.1 引文加工的要求 …… 3  
  
6.2 引文加工基本元素的可扩展性 …… 3  
  
6.3 引文加工基本元素表 …… 3  
  
7 元素的数据加工规则 …… 4  
  
7.1 引文列表(ref-list) …… 4  
  
7.2 引文原始信息(ref) …… 4  
  
7.3 并列语种引文(citation-parallel) …… 5  
  
7.4 引文库唯一标识符(ref-id) …… 5  
  
7.5 文献类型标识(ref-type) …… 5  
  
7.6 责任者(name) …… 6  
  
7.7 题名(title) …… 7  
  
7.8 来源(source) …… 7  
  
7.9 会议名称(conf-name) …… 8  
  
7.10 会议主办者(conf-sponsor) …… 8  
  
7.11 会议地点(conf-loc) …… 8  
  
7.12 会议日期(conf-date) …… 9  
  
7.13 出版日期(publish-date) …… 9  
  
7.14 卷(volume) …… 10  
  
7.15 期(issue) …… 10  
  
7.16 起页(fpage) …… 10  
  
7.17 止页(lpage) …… 11

7.18 数字对象唯一标识(id) ..... 11  
7.19 出版地(publisher-loc) ..... 12  
7.20 出版者(publisher) ..... 12  
8 引文加工基本元素属性及其定义 ..... 12  
8.1 引文元素集属性简表 ..... 12  
8.2 属性定义 ..... 13  
8.2.1 并列语种引文关联唯一标识符(parallel-id) ..... 13  
8.2.2 版本(edition) ..... 13  
8.2.3 数字资源唯一标识类型(id-type) ..... 13  
8.2.4 语种(lang) ..... 14  
8.2.5 责任者序号(name-seq) ..... 14  
8.2.6 责任者类型(name-type) ..... 15  
8.2.7 来源文献唯一标识符(source-art-id) ..... 15  
附录 A（资料性附录） 文献类型和文献载体标识代码 ..... 16  
A.1 文献类型和标识代码 ..... 16  
A.2 电子资源载体和标识代码 ..... 16

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国信息与文献标准化技术委员会(SAC/TC 4)提出并归口。

本标准起草单位：中国科学技术信息研究所、中国科学院文献情报中心、中国社会科学院、南京大学、北京万方数据股份有限公司、中国学术期刊（光盘版）电子杂志社有限公司。

本标准主要起草人：赵捷、刘筱敏、王星、马学良、苏金燕、王文军、武军红、刘春燕、李旭林、富平、白光武。

# 信息与文献 引文数据库数据加工规则

## 1 范围

本标准规定了期刊论文、专著、学位论文、科技报告等文献类型中的引文数据加工要素和著录规则以及引文数据加工规范。

本标准适用于文献信息机构及相关机构进行引文数据加工与引文数据库建设。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改版）适用于本文件。

GB/T 4880.2 语种名称代码 第2部分：3字母代码

GB/T 7408 数据元和交换格式 信息交换 日期和时间表示法

GB/T 7714—2015 信息与文献 参考文献著录规则

ANSI/NISO Z39.9 期刊文章标签集(Journal Article Tag Suite 1.1)

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 参考文献 reference

对一个信息资源或其中一部分进行准确和详细著录的数据，位于文末或文中的信息源。

[GB/T 7714—2015, 定义 3.1]

### 3.2 

引文 citation

参考文献中的单一条目。

### 3.3 

引文数据库 citation database

为满足用户多种需要，利用计算机存储设备按一定组织方式存放的相互关联的引文数据的集合。

### 3.4 

引用文献 citing paper

存在引用和被引用关系的两篇文献中的施引方，又称“来源文献”。

### 3.5 

顺序编码制 numeric references method

一种参考文献的标注体系，即引文采用序号标注，参考文献列表按引文的序号排序。

### 3.6 

著者-出版年制 first element and date method

一种参考文献的标注体系，即引文采用“著者-出版年”标注，参考文献列表按著者字顺和出版年

排序。

## 4 引文数据加工原则

### 4.1 完整性原则

引文包括文内注、脚注、尾注。最基本著录元素应包括引文的责任者、题名、文献类型标识、来源、出版日期、卷、期、起页、止页和数字对象唯一标识，但可以不局限于这些内容。在引文数据加工中，应遵循作者引用文献的客观事实，保留数据原始形态，全面地揭示引文数据的主体内容数据，以保证引文数据的完整性。

### 4.2 准确性原则

在引文数据加工过程中，应避免在数据中出现符号、文字、格式、数字、索引等错误，确保引文著录元素文字、元素著录项目、唯一标识符、数据库文件命名、检索点设置、索引等引文数据库构建元素的内容准确。

### 4.3 客观性原则

在引文数据加工过程中，应最大程度保留引文原始信息并客观著录。若出现引文数据中内容、文字表达错误或引文信息不完整，应根据被引文文献的实际状态进行相应处理。同时，需对所采取的修改和处理措施加以说明。若需选择部分信息进行加工，应保证选择信息的内容能够表达原始引文的特征属性。

### 4.4 扩展与关联原则

引文数据加工需遵循第7章元素的数据加工原则的有关规定。当本标准的加工元素集不能满足数据处理方对数据处理的需要时，可相应扩展元素集。扩展元素推荐采用ANSI/NISO Z39.9或其他描述标准。为了确保引文数据的唯一性，引文数据须确保与其来源文献的隶属关系。在引文数据库创建前应先制定明确的加工细则。

### 4.5 先进性原则

引文数据加工应选择成熟的、先进的技术手段，适合的硬件设备、软件系统和其他相关设备，还应充分采用计算机技术手段，实现引文数据加工等参考数据的自动获取，提高数据加工的效率和引文数据库的质量。

## 5 引文数据著录总则

### 5.1 著录信息源

引文数据的著录信息源主要是位于文末或文中的参考文献。若参考文献中的电子资源信息不足，必要时可依据已知电子资源通过互联网等途径获取完整引文数据。

### 5.2 著录文字与符号

引文数据使用的文字应采用 GB/T 7714—2015 规定的参考文献著录用文字。引文中出现希腊或拉丁字母、韩国文或朝鲜文、俄文、日文以及特殊符号时，建议优先采用输入法中的字符处理。引文中出现在字段首尾两端没有特定意义或者不具有识别引文唯一性特征的标点符号不予著录。

### 5.3 引文数据关联

引文数据加工中，应明确标记引文与其来源文献的对应关系，以便确保引文数据与来源文献之间的关联。

## 6 引文加工要求及基本元素名称表

### 6.1 引文加工的要求

根据第7章规定的著录或加工引文内容，以满足引文数据的再利用。本标准规定了引文切分的基本规则，并给出用于数据交换的元素名称，即字段名称。

### 6.2 引文加工基本元素的可扩展性

引文加工在保留原始数据形态的同时，需详细著录一条引文的主体内容，以便支持基于引文内容的各种数据服务。在6.3中规定了引文加工基本元素，但是使用单位可根据自身的实际需要，在符合本框架的情况下加以扩展。

### 6.3 引文加工基本元素表

引文加工基本元素表见表1。

<div style="text-align: center;">表 1 引文加工基本元素表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>可重复性</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>ref-list</td><td style='text-align: center;'>引文列表</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>ref</td><td style='text-align: center;'>引文原始信息</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>citation-parallel</td><td style='text-align: center;'>并列语种引文</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>ref-id</td><td style='text-align: center;'>引文库唯一识别符</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>ref-type</td><td style='text-align: center;'>文献类型标识</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>name</td><td style='text-align: center;'>责任者</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>title</td><td style='text-align: center;'>题名</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>source</td><td style='text-align: center;'>来源</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>conf-name</td><td style='text-align: center;'>会议名称</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>conf-sponsor</td><td style='text-align: center;'>会议主办者</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>conf-loc</td><td style='text-align: center;'>会议地点</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>conf-date</td><td style='text-align: center;'>会议日期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>publish-date</td><td style='text-align: center;'>出版日期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>volume</td><td style='text-align: center;'>卷</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>issue</td><td style='text-align: center;'>期</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>fpage</td><td style='text-align: center;'>起页</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>lpage</td><td style='text-align: center;'>止页</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>id</td><td style='text-align: center;'>数字对象唯一标识</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>publisher-loc</td><td style='text-align: center;'>出版地</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>publisher</td><td style='text-align: center;'>出版者</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>不可重复</td></tr></table>

## 7 元素的数据加工规则

### 7.1 引文列表(ref-list)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>ref-list</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>引文列表</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>引文列表</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>本元素用于数据交换或数据结构化描述，无须著录</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>source-art-id</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>〈ref-list source-art-id=&quot;14527&quot;〉〈ref id=&quot;100170&quot;〉...〈/ref〉〈ref id=&quot;100171&quot;〉...〈/ref〉...〈/ref-list〉</td></tr></table>

### 7.2 引文原始信息(ref)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>ref</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>引文原始信息</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>一条引文的原始信息</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>根据参考文献原有的组织方法（如，顺序编码制、著者-出版年制），逐条如实获取原文中的引文</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 李炳穆.韩国图书馆法[J].图书情报工作,2008,52(6):6-21(ref)李炳穆.韩国图书馆法[J].图书情报工作,2008,52(6):6-21(ref)2) 丁文详.数字革命与竞争国际化[N].中国青年报,2000-11-20(15)(ref)丁文详.数字革命与竞争国际化[N].中国青年报,2000-11-20(15)(ref)3) 常森,2013.《五行》学说与《荀子》[J].北京大学学报(哲学社会科学版),50(1):75(ref)常森,2013.《五行》学说与《荀子》[J].北京大学学报(哲学社会科学版),50(1):75(ref)4) 王临惠,等2010a.天津方言的源流关系刍议[J].山西师范大学学报(社会科学版),37(4):147(ref)王临惠,等2010a.天津方言的源流关系刍议[J].山西师范大学学报(社会科学版),37(4):147(ref)5) 王临惠,2010b.从几组声母的演变看天津方言形成的自然条件和历史条件[C]//曹志耘.汉语方言的地理语言学研究：首届中国地理语言学国际学术研讨会论文集.北京：北京语言大学出版社：138(ref)王临惠,2010b.从几组声母的演变看天津方言形成的自然条件和历史条件[C]//曹志耘.汉语方言的地理语言学研究：首届中国地理语言学国际学术研讨会论文集.北京：北京语言大学出版社：138(ref)6) 曹苗苗.2016.太赫兹波段Smith-Purcell辐射的介质加载光栅高频特性[J].物理学报,65(1):014101-1-014101-8.DOI:10.7498/aps.65.014101(ref)曹苗苗.2016.太赫兹波段Smith-Purcell辐射的介质加载光栅高频特性[J].物理学报,65(1):014101-1-014101-8.DOI:10.7498/aps.65.014101(ref)</td></tr></table>

### 7.3 并列语种引文(citation-parallel)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>citation-parallel</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>并列语种引文</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>用另一种语言文字表示的同一条引文</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>同一引文用不同的语种表达时，可依据参考文献著录并列语种引文</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>langparallel-id:用于定义不同语种引文的唯一标识符</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 邹为雷，李光明，张连昌.2010.胶东大庄子构造角砾岩型金矿床地质地球化学特征及成矿流体来源探讨.矿床地质，29(3):541-552ZOU Weilei, LI Guangming, ZHANG Lianchang.2010.Geological and geochemical characteristics and origin of ore-forming fluids in Dazhuangzi tectonic breccia type gold deposit, eastern Shandong Peninsula. Mineral Deposits, 29(3):541-552 (in Chinese with English abstract)〈citation-parallel parallel-id=&quot;11010702&quot; lang=&quot;eng&quot;&gt;〈name name-seq=&quot;1&quot;&gt;ZOU Weilei&lt;/name&gt;......〈/citation-parallel〉2) 韩国图书馆协会.韩国图书馆协会60年史.首尔：韩国图书馆协会，2006（原文韩文）〈citation-parallel parallel-id=&quot;4052346&quot; lang=&quot;chi&quot;&gt;〈name name-seq=&quot;1&quot;&gt;韩国图书馆协会&lt;/name&gt;......〈/citation-parallel〉</td></tr></table>

### 7.4 引文库唯一标识符(ref-id)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>ref-id</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>引文库唯一标识符</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>引文数据库记录唯一标识</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>引文数据库按一定的规则自动生成标识</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>〈ref-id〉100190110〈/ref-id〉</td></tr></table>

### 7.5 文献类型标识(ref-type)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>ref-type</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>文献类型标识</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示一条引文所属的某一特定文献类别</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）依据顺序编码制或著者-出版年制中的引文，从引文的方括号中获取文献类型标识。2）引文中无文献类型标识时，可根据文献的实际情况，参见附录A。其中，著录文献类型标识参见表A.1，电子资源载体类型标识参见表A.2</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）于潇，刘义，柴跃廷，等.互联网药品可信交易环境中主体资质审核备案模式[J].清华大学学报（自然科学版），2012，52（11）：1518-1523（ref-type）J&lt;/ref-type&gt;2）张凯军.轨道火车及高速轨道火车紧急安全制动辅助装置：201220158825.2[P].2012-04-05（ref-type）P&lt;/ref-type&gt;3）张伯伟.全唐五代诗格会考[M].南京：江苏古籍出版社，2002：288（ref-type）M&lt;/ref-type&gt;</td></tr></table>

### 7.6 责任者(name)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>name</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>责任者</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>对文献的知识内容负责的个人或团体，包括著者、编者、学位论文撰写者、专利申请者或专利权人、报告撰写者、标准提出者、析出文献的著者等</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）从引文获取个人责任者或机关团体责任者。倘若参考文献提供的责任者信息不完整，必要时可依据被引文献著录责任者。2）姓名表示方法依据GB/T 7714—2015有关规定。3）引文数据有责任者时，必须著录其属性</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>name-type：用于定义不同文献类型的责任者name-seq：用于定义责任者的顺序</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）胡承正，周详，缪灵.理论物理概论：上[M].武汉：武汉大学出版社，2010：112（name-name-type=&quot;article-name&quot; name-seq=&quot;1&quot;&gt;胡承正&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;2&quot;&gt;周详&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;3&quot;&gt;缪灵&lt;/name&gt;2）石艳龙，李建峰，周永刚，等.建筑工程施工技术管理水平有效提升策略分析[A]//旭日华夏（北京）国际科学技术研究院.首届国际信息化建设学术研讨会论文集（二）[C].旭日华夏（北京）国际科学技术研究院，2016：1（name-name-type=&quot;article-name&quot; name-seq=&quot;1&quot;&gt;石艳龙&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;2&quot;&gt;李建峰&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;3&quot;&gt;周永刚&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;4&quot;&gt;魏杰熙&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;5&quot;&gt;王军航&lt;/name&gt;（name-name-type=&quot;source-name&quot; name-seq=&quot;1&quot;&gt;旭日华夏（北京）国际科学技术研究院&lt;/name&gt;3）熊平，吴颉.从交易费用的角度谈如何构建药品流通的良性机制[J].中国物价，2005（8）：42-45（name-name-type=&quot;article-name&quot; name-seq=&quot;1&quot;&gt;熊平&lt;/name&gt;（name-name-type=&quot;article-name&quot; name-seq=&quot;2&quot;&gt;吴颉&lt;/name&gt;</td></tr></table>

### 7.7 题名(title)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>title</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>题名</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>文献的主要名称</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）从引文中获取文献题名，并按引文中的形式如实著录。2）题名中出现的上、下角标，可用“-”表示下标，用“-”表示上标。上、下角标同时存在时，先著录下标，再著录上标</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）美国妇产科医师学会.新生儿脑病和脑性瘫痪发病机制与病理生理[M].段涛，杨慧霞，译.北京：人民卫生出版社，2010：38-39（title）新生儿脑病和脑性瘫痪发病机制与病理生理（/title）2）吴云芳.面向中文信息处理的现代汉语并列结构研究[D].北京：北京大学，2003：2（title）面向中文信息处理的现代汉语并列结构研究（/title）3）于潇，刘义，柴跃廷，等.互联网药品可信交易环境中主体资质审核备案模式[J].清华大学学报（自然科学版），2012，52（11）：1518-1523（title）互联网药品可信交易环境中主体资质审核备案模式（/title）4）张凯军.轨道火车及高速轨道火车紧急安全制动辅助装置：201220158825.2[P].2012-04-05（title）轨道火车及高速轨道火车紧急安全制动辅助装置（/title）</td></tr></table>

### 7.8 来源(source)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>source</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>来源</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>一条引文的出处</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>当引文为析出文献时，将引文的出处著录在“来源”元素中。来源包括刊载论文的专著、期刊以及网络资源的网址等</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>edition:用于定义来源的版本</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 丁文详.数字革命与竞争国际化[N].中国青年报,2000-11-20(15)    (source)中国青年报( /source)2) 杨永峰.班主任工作的艺术在于读懂学生因材施教[C]//百川利康(北京)国际医学研究院.2016年1月全国教育科学学术交流会论文集.北京:百川利康(北京)国际医学研究院,2016:1    (source)2016年1月全国教育科学学术交流会论文集( /source)3) 李炳穆.韩国图书馆法[J].图书情报工作,2008,52(6):6-21    (source)图书情报工作( /source)4) 李强.化解医患矛盾需釜底抽薪[EB/OL].(2012-05-03)[2013-03-25].http://wenku.baidu.com/view/47e4f206b52acfc789ebc92f.html    (source) http://wenku.baidu.com/view/47e4f206b52acfc789ebc92f.html    (source)5) 国家图书馆《中国文献编目规则》修订组.中国文献编目规则[M].2版.北京:北京图书馆出版社,2005:105    (source edition=&quot;2 版&quot;)中国文献编目规则( /source)</td></tr></table>

### 7.9 会议名称(conf-name)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>conf-name</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>会议名称</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>引文中的会议名称</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>从引文中获取会议名称</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1） 钟以琛，钟训.路面裂缝填封技术在农村公路预防性养护中的应用探讨[C]//中国公路学会养护与管理分会.中国公路学会养护与管理分会第六届学术年会论文集（上卷）.北京：中国公路学会养护与管理分会，2016：6（conf-name）中国公路学会养护与管理分会第六届学术年会（/conf-name）2） 雷光春.综合湿地管理：综合湿地管理国际研讨会论文集[C].北京：海洋出版社，2012（conf-name）综合湿地管理国际研讨会（/conf-name）</td></tr></table>

### 7.10 会议主办者(conf-sponsor)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>conf-sponsor</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>会议主办者</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>会议主办的团体机构名称</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>从引文中获取会议主办者信息</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>吴洪涛,戴建旺.耕地保护国家监管系统建设概述[C]//中国土地学会.土地信息技术的创新与土地科学技术发展:2006年中国土地学会学术年会论文集.北京:地质出版社,2007:10-20(conf-name)2006年中国土地学会学术年会(/conf-name)(conf-sponsor)中国土地学会(/conf-sponsor)</td></tr></table>

### 7.11 会议地点(conf-loc)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>conf-loc</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>会议地点</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>会议召开地点的城市名称</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）从引文中获取会议召开的城市名称。2）会议地点著录召开会议所在地的城市名称。对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语，并冠逗号</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>吴洪涛，戴建旺.耕地保护国家监管系统建设概述[C]//中国土地学会.土地信息技术的创新与土地科学技术发展：2006年中国土地学会学术年会论文集.北京：地质出版社，2007：10-20（conf-name）2006年中国土地学会学术年会（conf-name）（conf-sponsor）中国土地学会（conf-sponsor）（conf-loc）重庆（conf-loc）</td></tr></table>

<div style="text-align: center;">7.12 会议日期(conf-date)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>conf-date</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>会议日期</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>会议召开的日期</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>依据引文提供的信息，按照GB/T 7408有关规定著录会议日期，著录格式为“YYYY-MM-DD”</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>吴洪涛，戴建旺.耕地保护国家监管系统建设概述[C]//中国土地学会.土地信息技术的创新与土地科学技术发展：2006年中国土地学会学术年会论文集.北京：地质出版社，2007：10-20（conf-name）2006年中国土地学会学术年会（conf-name）（conf-sponsor）中国土地学会（conf-sponsor）（conf-loc）重庆（conf-loc）（conf-date）2006-11-14（conf-date）</td></tr></table>

### 7.13 出版日期(publish-date)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>publish-date</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>出版日期</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>文献的出版日期</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）一条引文的出版日期、网络资源的获取或更新日期。2）公元纪年的出版日期按照GB/T 7408的有关规定著录，著录格式为“YYYY-MM-DD”。3）非公元纪年的出版日期须著录文献原有的纪年形式。如：康熙四十四年</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）中国职工教育研究会.职工教育研究论文集[G].北京：人民教育出版社，1985（publish-date）1985（publish-date）2）杨洪升.四库馆私家抄校书考略[J].文献，2013（1）56-75（publish-date）2013（/publish-date）3）吴洪涛，戴建旺.耕地保护国家监管系统建设概述[C]//中国土地学会.土地信息技术的创新与土地科学技术发展：2006年中国土地学会学术年会论文集.北京：地质出版社，2007：10-20（publish-date）2007（/publish-date）4）张蓓莉，2006.系统宝石学[M].2版.北京：地质出版社：365-373（publish-date）2006（/publish-date）5）刘彻东，1998.中国的青年刊物：个性特色为本[J].中国出版（5）：38-39（publish-date）1998（/publish-date）6）王临惠，等2010a.天津方言的源流关系刍议[J].山西师范大学学报（社会科学版），37（4）：147（publish-date）2010（/publish-date）7）王临惠，2010b.从几组声母的演变看天津方言形成的自然条件和历史条件[C]//曹志耘.汉语方言的地理语言学研究：首届中国地理语言学国际学术研讨会论文集.北京：北京语言大学出版社：138（publish-date）2010（/publish-date）</td></tr></table>

### 7.14 卷(volume)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>volume</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>卷</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>连续出版物年卷期标识与页码中的卷次</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>从引文的连续出版物年卷期标识中获取卷次</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）于潇，刘义，柴跃廷，等.互联网药品可信交易环境中主体资质审核备案模式[J].清华大学学报（自然科学版），2012，52（11）：1518-1523（volume）52（/volume）2）DES MARAIS D J, STRAUSS H, SUMMONS R E, et al. Carbon isotope evidence for the stepwise oxidation of the Proterozoic environment[J]. Nature, 1992, 359: 605-609（volume）359（/volume）</td></tr></table>

### 7.15 期(issue)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>issue</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>期</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>连续出版物年卷期标识与页码中的期次</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>从引文的连续出版物年卷期标识中获取期次</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）杨洪升.四库馆私家抄校书考略[J].文献,2013(1):56-75(issue)1/(issue)2）李炳穆.韩国图书馆法[J].图书情报工作,2008,52(6):6-21(issue)6/(issue)</td></tr></table>

### 7.16 起页(fpage)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>fpage</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>起页</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>期刊论文、会议论文等析出文献在来源中的起始页码</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）从引文中获取起始页码。2）将报纸的版次著录于此</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 杨洪升.四库馆私家抄校书考略[J].文献,2013(1):56-75  (fpage)56(/fpage)2) 李炳穆.韩国图书馆法[J].图书情报工作,2008,52(6):6-21  (fpage)6(/fpage)3) 丁文详.数字革命与竞争国际化[N].中国青年报,2000-11-20(15)  (fpage)15(/fpage)4) 曹苗苗.2016.太赫兹波段Smith-Purcell辐射的介质加载光栅高频特性[J].物理学报,65(1):014101-1-014101-8.DOI:10.7498/aps.65.014101  (fpage)014101-1(/fpage)</td></tr></table>

### 7.17 止页(lpage)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>lpage</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>止页</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>期刊论文、会议论文等析出文献在来源文献中的结束位置</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）从引文中获取该引文的结束页码。2）当论文在期刊中转页刊载时，必要时需根据被引文献如实著录转页</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）杨洪升.四库馆私家抄校书考略[J].文献,2013(1):56-75(lpage)75(/lpage)2）李炳穆.韩国图书馆法[J].图书情报工作,2008,52(6):6-21(lpage)21(/lpage)3）曹苗苗.2016.太赫兹波段Smith-Purcell辐射的介质加载光栅高频特性[J].物理学报,65(1):014101-1-014101-8.DOI:10.7498/aps.65.014101(lpage)014101-8(/lpage)</td></tr></table>

### 7.18 数字对象唯一标识(id)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>id</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>数字对象唯一标识</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>可识别文献唯一性的编码</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>从引文中获取指向该引文的数字对象唯一标识</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>Id-type:用于定义数字对象唯一标识的类型,如 DOI、ISBN 等</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 陈建军.从数字地球到智慧地球[J/OL].国图资源导刊,2010,7(10):93 [2013-03-20].http://d.g.wanfangdata.com.cn/Periodical_hunandz201010038.aspx.DOI:10.3969/j.issn.1672-5603.2010.10.038    (id id-type=&quot;DOI&quot;)10.3969/j.issn.1672-5603.2010.10.038&lt;/id&gt;2) WALLSSC,BARCHIVICHWJ,BROWNME.Drought,deluge and declines;the impact of precipitation extremes on amphibians in a changing climate[J/OL].Biology,2013,2(1):399-418 [2013-11-04].http://www.mdpi.com/2079-7737/2/1/399.DOI:10.3390/biology2010399    (id id-type=&quot;DOI&quot;)10.3390/biology2010399&lt;/id&gt;</td></tr></table>

### 7.19 出版地(publisher-loc)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>publisher-loc</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>出版地</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>出版者所在地</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）引文出版者所在的城市名称。2）对于同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语，并以逗号分隔</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）钱学森，宋健.工程控制论[M].北京：科学出版社，2011（publisher-loc）北京（publisher-loc）2）TAYLOR A G, JOUDREY D N. The organization of information[M]. Westport, Conn.: Libraries Unlimited, 2009（publisher-loc）Westport, Conn.（publisher-loc）</td></tr></table>

### 7.20 出版者(publisher)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>publisher</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>出版者</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>引文的出版实体</td></tr><tr><td style='text-align: center;'>著录规则</td><td style='text-align: center;'>1）出版者一般为图书、会议录、标准、连续出版物等文献的出版机构名称。2）学位论文从参考文献的出版项获取学位授予单位著录于此</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>文本</td></tr><tr><td style='text-align: center;'>属性</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）徐光宪，王祥云.物质结构[M].北京：科学出版社，2010（publisher）科学出版社（publisher）2）马欢.人类活动影响下海河流域典型区水循环变化分析[D].北京：清华大学，2011：27（publisher）清华大学（publisher）</td></tr></table>

## 8 引文加工基本元素属性及其定义

### 8.1 引文元素集属性简表

引文元素集属性简报见表2。

<div style="text-align: center;">表 2 引文元素集属性简表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>使用限制</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>parallel-id</td><td style='text-align: center;'>并列语种引文关联唯一标识符</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>edition</td><td style='text-align: center;'>版本项</td><td style='text-align: center;'>可选</td></tr></table>

<div style="text-align: center;">表 2 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>使用限制</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>id-type</td><td style='text-align: center;'>数字资源唯一标识类型</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>lang</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>可选</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>name-seq</td><td style='text-align: center;'>责任者序号</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>name-type</td><td style='text-align: center;'>责任者类型</td><td style='text-align: center;'>必备</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>source-art-id</td><td style='text-align: center;'>来源文献唯一标识</td><td style='text-align: center;'>必备</td></tr></table>

### 8.2 属性定义

#### 8.2.1 并列语种引文关联唯一标识符(parallel-id)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>parallel-id</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>并列语种引文关联唯一标识符</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在引文数据库内，与并列语种引文相对应的唯一标识符</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>数字或文本</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>必选属性</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>〈citation-parallel parallel-id=&quot;1101070&quot;&gt;…〈/citation-parallel〉</td></tr></table>

#### 8.2.2 版本(edition)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>edition</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>版本</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>引文的版本说明</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）库恩.科学革命的结构：第4版[M].金吾伦,胡新和,译.2版.北京：北京大学出版社,2012（source edition=&quot;2版&quot;)科学革命的结构&lt;/source&gt;2）O&#x27;BRIEN J A.Introduction to information systems[M].7th ed.Burr Ridge,Ⅲ:Irwin,1994（source edition=&quot;7th ed.&quot;)Introduction to information systems&lt;/source&gt;</td></tr></table>

#### 8.2.3 数字资源唯一标识类型(id-type)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>id-type</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>数字资源唯一标识类型</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>不同数字资源唯一标识类型</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>DOI、ISBN 等</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>必选属性</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 陈建军.从数字地球到智慧地球[J/OL].国图资源导刊,2010,7(10):93 [2013-03-20].http://d.g.wanfangdata.com.cn/Periodical_hunandz201010038.aspx. DOI:10.3969/j.issn.1672-5603.2010.10.038
    (id-type=&quot;DOI&quot;)10.3969/j.issn.1672-5603.2010.10.038&lt;/id&gt;
2) 曹苗苗.2016.太赫兹波段Smith-Purcell辐射的介质加载光栅高频特性[J].物理学报,65(1):014101-1-014101-8.DOI:10.7498/aps.65.014101
    (id-type=&quot;DOI&quot;)10.7498/aps.65.014101&lt;/id&gt;</td></tr></table>

#### 8.2.4 语种(lang)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>lang</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>语种</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>引文使用的语言文字</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>chi(汉语)、eng(英语)、fre(法语)、ger(德语)、rus(俄语)、kor(韩国语或朝鲜语)、jpn(日语)等。列举的语种属性值不足时,须根据GB/T 4880.2《语种名称代码 第2部分:3个字母代码》国家标准扩展</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>无默认值</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1) 邹为雷,李光明,张连昌.2010.胶东大庄子构造角砾岩型金矿床地质地球化学特征及成矿流体来源探讨.矿床地质,29(3):541-552ZOU Weilei, LI Guangming, ZHANG Lianchang. 2010. Geological and geochemical characteristics and origin of ore-forming fluids in Dazhuangzi tectonic breccia type gold deposit, eastern Shandong Peninsula. Mineral Deposits, 29(3):541-552 (in Chinese with English abstract)〈citation-parallel parallel-id=&quot;11010702&quot; lang=&quot;eng&quot;&gt;〈name name-seq=&quot;1&quot;&gt;ZOU Weilei&lt;/name&gt;......〈/citation-parallel〉2) 韩国图书馆协会. 韩国图书馆协会60年史.首尔:韩国图书馆协会,2006(原文韩国文)〈citation-parallel parallel-id=&quot;4052346&quot; lang=&quot;chi&quot;&gt;〈name name-seq=&quot;1&quot;&gt;韩国图书馆协会&lt;/name&gt;......〈/citation-parallel〉</td></tr></table>

#### 8.2.5 责任者序号(name-seq)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>name-seq</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>责任者序号</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示引文责任者顺序的编号</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>数字</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>必选属性</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>$ name\ name-seq=&quot;1&quot; $  钱学森 $ /name $</td></tr></table>

<div style="text-align: center;">8.2.6 责任者类型(name-type)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>name-type</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>责任者类型</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>不同引文类型责任者的属性</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>article-name:篇、章节等析出文献责任者、专著的责任者source-name:引文出处的文献责任者</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>必备属性</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>1）程根伟.1998年长江洪水的成因与减灾对策[M]//许厚泽,赵其国.长江流域洪涝灾害与科技对策.北京:科学出版社,1999:32-36    〈name name-type=&quot;article-name&quot;〉程根伟(／name)    〈name name-type=&quot;source-name&quot; name-seq=&quot;1&quot;〉许厚泽(／name)    〈name name-type=&quot;source-name&quot; name-seq=&quot;2&quot;〉赵其国(／name)2）汪学军.中国农业转基因生物研发进展与安全管理[C]//国家环境保护总局生物安全管理办公室.中国国家生物安全框架实施国际合作项目研讨会论文集.北京:中国环境科学出版社,2002:22-25    〈name name-type=&quot;article-name&quot;〉汪学军(／name)    〈name name-type=&quot;source-name&quot;〉国家环境保护总局生物安全管理办公室(／name)</td></tr></table>

#### 8.2.7 来源文献唯一标识符(source-art-id)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>source-art-id</td></tr><tr><td style='text-align: center;'>标签</td><td style='text-align: center;'>来源文献唯一标识符</td></tr><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>来源文献的唯一标识符,数据库自动生成</td></tr><tr><td style='text-align: center;'>属性值</td><td style='text-align: center;'>数字或文本</td></tr><tr><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>必选属性</td></tr><tr><td style='text-align: center;'>示例</td><td style='text-align: center;'>〈ref-list source-art-id=&quot;14527&quot;&gt;…〉〈ref-list〉</td></tr></table>

附录 A

(资料性附录)

文献类型和文献载体标识代码

### A.1 文献类型和标识代码

文献类型和标识代码见表 A.1。

<div style="text-align: center;">表 A.1 文献类型和标识代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考文献类型</td><td style='text-align: center;'>文献类型标识代码</td></tr><tr><td style='text-align: center;'>普通图书</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>会议录</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>汇编</td><td style='text-align: center;'>G</td></tr><tr><td style='text-align: center;'>报纸</td><td style='text-align: center;'>N</td></tr><tr><td style='text-align: center;'>期刊</td><td style='text-align: center;'>J</td></tr><tr><td style='text-align: center;'>学位论文</td><td style='text-align: center;'>D</td></tr><tr><td style='text-align: center;'>报告</td><td style='text-align: center;'>R</td></tr><tr><td style='text-align: center;'>标准</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>专利</td><td style='text-align: center;'>P</td></tr><tr><td style='text-align: center;'>数据库</td><td style='text-align: center;'>DB</td></tr><tr><td style='text-align: center;'>计算机程序</td><td style='text-align: center;'>CP</td></tr><tr><td style='text-align: center;'>电子公告</td><td style='text-align: center;'>EB</td></tr><tr><td style='text-align: center;'>档案</td><td style='text-align: center;'>A</td></tr><tr><td style='text-align: center;'>舆图</td><td style='text-align: center;'>CM</td></tr><tr><td style='text-align: center;'>数据集</td><td style='text-align: center;'>DS</td></tr><tr><td style='text-align: center;'>其他</td><td style='text-align: center;'>Z</td></tr></table>

### A.2 电子资源载体和标识代码

电子资源载体和标识代码见表 A.2。

<div style="text-align: center;">表 A.2 电子资源载体和标识代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>电子资源的载体类型</td><td style='text-align: center;'>载体类型标识代码</td></tr><tr><td style='text-align: center;'>磁带(magnetic tape)</td><td style='text-align: center;'>MT</td></tr><tr><td style='text-align: center;'>磁盘(disk)</td><td style='text-align: center;'>DK</td></tr><tr><td style='text-align: center;'>光盘(CD-ROM)</td><td style='text-align: center;'>CD</td></tr><tr><td style='text-align: center;'>联机网络(online)</td><td style='text-align: center;'>OL</td></tr></table>