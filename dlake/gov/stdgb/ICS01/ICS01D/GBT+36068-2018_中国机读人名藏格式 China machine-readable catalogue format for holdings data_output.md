

# 中华人民共和国国家标准

GB/T 36068—2018

# 中国机读馆藏格式

# China machine-readable catalogue format for holdings data

2018-03-15 发布

2018-10-01 实施

## 目次

前言 …… I    
引言 …… II    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 2    
4 格式结构 …… 2    
4.1 格式说明 …… 2    
4.2 总体结构 …… 2    
4.3 功能模块 …… 3    
4.4 数据字段设置原则 …… 3    
5 应用规则 …… 3    
5.1 必备字段 …… 3    
5.2 馆藏说明级别 …… 4    
5.3 字段和子字段的可重复性 …… 4    
5.4 子字段顺序 …… 4    
5.5 填充符 …… 4    
5.6 代码数据值 …… 5    
5.7 数字子字段 …… 5    
5.8 字段间连接数据 …… 5    
5.9 标识符号 …… 6    
5.10 格式应用 …… 6    
5.11 CN MARC 馆藏记录字段与 GB/T 24424—2009 著录项的对照 …… 7    
5.12 CN MARC 馆藏记录和 CN MARC 书目记录相关字段之间的对照 …… 8    
5.13 说明性附注 …… 8    
5.14 字段描述结构 …… 8    
5.15 国内使用字段 …… 9    
6 记录头标和数据字段——详细说明 …… 9    
6.1 记录头标(record label) …… 9    
6.2 标识块(identification block) …… 12    
6.3 编码信息块(coded information block) …… 15    
6.4 馆藏位置和检索块(location and access block) …… 23    
6.5 附注块(notes block) …… 30    
6.6 馆藏范围块(extent of holdings block) …… 34    
6.7 责任块(responsibility block) …… 43    
6.8 源信息块(source information block) …… 44    
附录 A（资料性附录） 完整样例 …… 46    
参考文献 …… 54

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国信息与文献标准化技术委员会(SAC/TC 4)提出并归口。

本标准起草单位：国家图书馆、北京大学图书馆、中国科学院文献情报中心、北京师范大学图书馆。本标准主要起草人：贺燕、曹迁、槐燕、刘春玥、朱学军、侯旭红。

## 引言

### 0.1 背景

机读目录(Machine-Readable Catalogue，简写为 MARC)，是随着计算机自动化的发展而研制出来的一种计算机可识别和处理的数据格式。MARC 的问世，标志着文献编目工作由传统的手工操作迈向计算机处理的自动化时代。我国对 MARC 的研究起步于 20 世纪 80 年代。目前，MARC 格式已成为我国图书馆及情报部门信息资源交流和交换必不可少的工具。机读目录已经成为图书馆及文献收藏单位必不可少的组成部分，其所包含的馆藏信息更是在文献的保存保护和读者服务中发挥着重要作用。国际图联（IFLA）UNIMARC 常设委员会（PUC）早在 1999 年就委任工作组进行 UNIMARC 馆藏格式的编制，并于 2007 年完成发布了《通用机读目录手册：馆藏格式（第 1 版）》[UNIMARC Manual: Holding Format (Version 1)]。由于我国长期缺乏馆藏数据机读目录格式的标准，致使各图书馆与文献收藏单位对馆藏数据机读目录格式的定义各有不同。为使我国具有统一规范的馆藏数据编制标准，为馆藏数据库的建立和馆藏数据处理提供参照或依据，特制定《中国机读馆藏格式（China machine-readable catalogue format for holdings data）》国家标准，本标准可与 GB/T 33286—2016 配套使用。

### 0.2 编制原则

本标准遵循 GB/T 24424—2009《馆藏说明（Holdings statements）》，参照国际图联（IFLA）2007 年发布的“UNIMARC Manual: Holdings format（Version 1）”与 GB/T 33286—2016《中国机读书目格式（China machine-readable catalogue format for bibliographic data）》，结合我国各类型文献特点与编目实践和用户需求，以及目前国内文献收藏机构馆藏揭示现状编制。

### 0.3 主要变化

本标准与《通用机读目录手册：馆藏格式（2007年第1版）》[UNIMARC Manual：Holdings Format (Version 1)]的主要差异为，《通用机读目录手册：馆藏格式（2007年第1版）》遵循ISO 10324的相关规定，只适用于3级及3级以下的馆藏描述，本标准遵循GB/T 24424—2009的相关规定，不仅能适用于3级及3级以下的馆藏描述，还适用于4级馆藏描述，并增加了有关4级馆藏描述的相关内容。

# 中国机读馆藏格式

## 1 范围

本标准规定了计算机可读馆藏记录的标准结构，包括字段标识符、字段指示符和子字段标识符，以及馆藏记录的内容标识在磁带、软盘、光盘等载体上的逻辑和物理格式。

本标准适用于揭示文献的收藏与管理信息。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 1988 信息技术 信息交换用七位编码字符集

GB/T 2312 信息交换用汉字编码字符集 基本集

GB/T 2659 世界各国和地区名称代码

GB/T 2901 信息与文献 信息交换格式

GB/T 4880.2 语种名称代码 第2部分：3字母代码

GB/T 7408 数据元和交换格式 信息交换 日期和时间表示法

GB/T 24424—2009 馆藏说明

GB/T 33286—2016 中国机读书目格式

ISO 646 信息技术 信息交换用 ISO7 位编码字符集(Information technology—ISO 7-bit coded character set for information interchange)

ISO 5426 书目信息交换用拉丁字母编码字符扩展集(Extension of the Latin alphabet coded character set for bibliographic information interchange)

ISO 5426-2 信息和文献 书目信息交换用拉丁字母编码字符扩展集 第2部分：用于欧洲小语种和旧印刷体的拉丁字符（Information and documentation—Extension of the Latin alphabet coded character set for bibliographic information interchange—Part 2: Latin characters used in minor European languages and obsolete typography）

ISO 5427 书目信息交换用斯拉夫字母编码字符扩展集(Extension of the Cyrillic alphabet coded character set for bibliographic information interchange)

ISO 5428 书目信息交换用希腊字母编码字符集(Greek alphabet coded character set for bibliographic information interchange)

ISO 6438 文献 书目信息交换用非洲字母编码字符集(Documentation—African coded character set for bibliographic information interchange)

ISO 8957 信息和文献 书目信息交换用希伯来字母编码字符集(Information and documentation—Hebrew alphabet coded character sets for bibliographic information interchange)

ISO 10586 信息和文献 书目信息交换用格鲁吉亚字母编码字符集(Information and documentation—Georgian alphabet coded character set for bibliographic information interchange)

ISO/IEC 10646 AMD 1 信息技术 通用多 8 位编码字符集(UCS) 附件 1:(古斯拉夫)格拉哥里字符、(古埃及)科普特字符、格鲁吉亚字符和其他字符[Information technology—Universal Multiple

Octet Coded Character Set (UCS)—Amendment 1: Glagolitic, Coptic, Georgian and other characters]

通用机读目录手册：馆藏格式（2007年第1版）[UNIMARC manual：holdings format（Version 1 2007）]

## 3 术语和定义

GB/T 24424—2009 和 GB/T 33286—2016 界定的以及下列术语和定义适用于本文件。

### 3.1 

## 集成单元 integrating unit

通过更新的方式增加或改变的基本书目单元或次要书目单元，它们不能处于分散的状态，而是被合成一个整体。

注：集成单元可以是有限的或是连续的。

### 3.2 

## 更新后的整体 iteration

第一次出版或是已被更新后出版的一个集成性资源的样例。

### 3.3 

## 非连续性资源 non-continuing resource

一种一次或在有限时间内发行完毕的文献资源。

### 3.4 

## 连续性资源 continuing resource

一种在发行时间上没有明确终止日期的资源。

注：连续性资源包括连续出版物和不断更新的集成性资源。

### 3.5 

## 集成性资源 integrating resource

通过更新进行增补或修改的一种书目资源，其更新部分并不离散于原资源，而是与原资源整合为一体。

注：集成性资源既可以是有限性资源，也可以是连续性资源。集成性资源的例子包括更新的活页/散页、更新的网页和更新的数据库等。

## 4 格式结构

### 4.1 格式说明

本格式系为数据交换而设计的通用格式，并不对各个系统的内部格式、内容或数据结构作出规定。各系统间的任何转换处理，其最终结果均应符合本标准规定。

为减少数据转换中可能产生的问题，数据交换机构系统内部格式的字段标识符、字段和子字段的定义宜与本标准的相应部分保持一致。

### 4.2 总体结构

<div style="text-align: center;"><img src="imgs/img_in_image_box_78_1399_114_1435.jpg" alt="Image" width="3%" /></div>


本格式是 GB/T 2901 的一个特定形式。它对每一个用于交换的馆藏记录规定了应遵循的标准记录结构，其构成为：

a）记录头标：由24个字符构成。

b）地址目次区：区内含有一个或多个目次项，每一目次项由3位数字的字段标识符（简称字段号）

以及字段长度和字段起始字符位置（从第一个数据字段算起）3部分构成。

c） 数据字段区：由若干定长和变长字段构成，每个字段之间由字段分隔符隔开。

d）记录结束符：用以标识该记录结束和与下一个记录的区分。

记录结构如下：


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>记录头标</td><td style='text-align: center;'>地址目次区</td><td style='text-align: center;'>数据字段区</td><td style='text-align: center;'>记录结束符</td></tr></table>

关于总体结构的格式说明见 GB/T 33286—2016 中的第 5 章。

### 4.3 功能模块

馆藏记录中的字段被划分为不同的功能模块，字段标识符的第一位（最左面）数字表示字段所属的模块。

0——标识块：包含用以标识记录或馆藏的编号。

1——编码信息块：包含描述记录或数据多个方面的定长数据元素（通常为编码）。

2——馆藏位置和检索块：包含标识书目单元的所属机构、物理位置或可利用的馆藏信息。

3——附注块：包含用以公共显示、有助于识别馆藏记录中所描述文献的附注。

5——馆藏范围块：包含用于获取馆藏的特定书目款目（基本或辅助单元）的标识说明、样式、编号与年代等信息。

7——责任块：包含与馆藏记录中所描述文献相关的责任标目形式。

8——信息来源块：包含记录来源，以及非公共显示的编目员对数据的相关注释。

9——国内使用块：包含记录创建人建立的本地数据，本标准没有定义用于系统内交换的字段标识符，但 CN MARC 书目格式中的某些国内使用字段可适用于本格式。

### 4.4 数据字段设置原则

4.4.1 字段标识符应从两方面标识一个字段：

a）字符串的类型(如馆藏位置和索取号);

b）字符串在记录中执行的功能(如级别)。

为字段标识符的字符位置分配特定值时，要能反映以上两方面内容。字段标识符可以是数字或字母。赋值时首选数值，如有需要可以扩展到字母值（小写优先）。

4.4.2 指示符应依据字段标识符而定，但在所有字段中的使用应尽可能保持一致。指示符可以是数字或字母。赋值时首选数字值，如需要可扩展到字母值（小写优先）。

4.4.3 子字段标识符要依据字段标识符而定，并尽可能在所有字段中用相同的子字段标识符来标识公共数据元素。子字段标识符可以是数字或字母。赋值时首选字母值（小写优先），如有需要也可扩展到数值。子字段标识符的赋值是用于标识，而非用于文档排序。除子字段$6$应作为第一个子字段出现外，子字段标识符没有特定顺序，应根据数据而定。GB/T24424—2009限定了数据元素的顺序和格式，以确保记录和解释的一致性；但并没有限定馆藏说明中数据区域的显示顺序。

4.4.4 附注中记载的描述性信息不用作检索点。

## 5 应用规则

### 5.1 必备字段

除记录头标和地址目次区外，以下字段为必备字段。

001 馆藏记录标识号

004 相关书目记录标识号

100 通用处理数据(仅包含特定数据元素)

252 馆藏位置和索取号或 256 电子资源地址与检索

801 记录来源

其他字段存在与否取决于馆藏记录的级别，该级别由创建记录的编目机构决定。但是，若某一数据元存在，就应依据本标准定义的规则对它进行完全的内容标识。

### 5.2 馆藏说明级别

依据 GB/T 24424—2009 的应用规则，馆藏说明包含如下 4 个级别：

a）1级馆藏：

标识文献的书目款目和收藏机构。此级别适合描述单部分文献，对于多部分文献和连续性资源此级别则无法表示馆藏的范围。不管馆藏的保存原则或完整性如何，此级别都应著录每一书目文献的机构标识。至少，它应包括记录馆藏的书目款目标识和馆藏地标识。书目款目标识可包含在相关书目记录标识号004字段中。馆藏地标识可包含在馆藏位置和索取号252字段的机构标识符$a子字段中。

b) 2 级馆藏：

2级馆藏比1级馆藏增加了一般馆藏说明，即，除了对1级馆藏的要求外，它至少还应包括：

1）接收或采访状态(170 $ a/0);

2）一般保存政策(171 $a/0);

3）完整性标识(171 $a/5)。

c）3级馆藏：

3级馆藏增加了馆藏范围的简要说明。简要馆藏说明可以是开放式或关闭式的，如果需要编次和/或年代，只著录最高级。

d）4级馆藏：

4级馆藏增加了馆藏范围的详细说明。详细的馆藏说明可以是逐条的或是压缩的，可以是开放式或关闭式的，编次和/或年代应著录最详细的级别（包括所有等级）。

### 5.3 字段和子字段的可重复性

若“可重复”这个词与一个字段相关联，则表示此字段在一条记录中可重复出现。若“可重复”与一个子字段相关联，则表示此子字段在一个字段中可重复出现。

### 5.4 子字段顺序

不以子字段标识符的值规定子字段的顺序。子字段标识符是按照标识的目的被分配值，而不是为了排序。

### 5.5 填充符

当编目机构无法确定一个内容标识或代码信息时可使用填充符。填充符是 GB/T 1988 中的一个图形字符“|”（竖线），在七位编码表中为 7/12 位。它避免了使用 0（零）或空位（#），因零和空位在本格式中均有特定含义。

填充符可在下列的情况下出现：

a） 编目机构不启用此内容标识或不给此信息分配代码；或

b） 编目机构虽然启用此内容标识或为此信息分配代码，但是在这条特定记录里无法知道准确的

值;或

c) 编目机构为此内容标识或代码信息使用相似的值，但是它们无法被转成 CN MARC 馆藏格式准确的等同值。

填充符不可用于记录头标、地址目次区、字段标识符或正文数据；不可用于取代必备编码数据元素、子字段标识符、著录用标识符或其他专用字符；不可用于代替供选择使用的编码字段中的全部代码（如遇此种情况应放弃选用该字段）。

### 5.6 代码数据值

以下规定用于填写记录头标和编码数据子字段中的代码值：

#一无信息提供。

u—不详。无法确定要填写代码的准确值时使用。

x—不适用。当一个特征不适用于所描述的实体类型时使用。

y—不存在。当代码不能代表所描述的实体时使用。

z—其他。当已知实体的特征，但所定义的代码值均不适合时使用。

|—填充符。当无意分配代码时使用。

### 5.7 数字子字段

本标准定义以下数字子字段可以在馆藏记录中使用：


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>$2</td><td style='text-align: center;'>系统代码或来源</td><td style='text-align: center;'>2—字段块</td></tr><tr><td style='text-align: center;'>$2</td><td style='text-align: center;'>连接文本</td><td style='text-align: center;'>256 字段</td></tr><tr><td style='text-align: center;'>$3</td><td style='text-align: center;'>规范记录号</td><td style='text-align: center;'>7—字段块</td></tr><tr><td style='text-align: center;'>$4</td><td style='text-align: center;'>关系词代码</td><td style='text-align: center;'>7—字段块</td></tr><tr><td style='text-align: center;'>$6</td><td style='text-align: center;'>内部字段间连接数据</td><td style='text-align: center;'>2—字段块；5—字段块</td></tr><tr><td style='text-align: center;'>$7</td><td style='text-align: center;'>字段的字母/文字</td><td style='text-align: center;'>2—字段块；3—字段块；5—字段块</td></tr></table>

### 5.8 字段间连接数据

#### 5.8.1 $6 内部字段间连接数据

$6 子字段包含该字段向本记录内其他字段连接的数据及说明连接原因的代码。子字段 $6$ 若被启用，则子字段的前两个元素（字符位置 0-2）必备，第三个元素（字符位置 3-5）可选用。所以子字段 $6$ 的长度可以是三个或者是六个字符。子字段 $6$ 总是字段中的第一子字段。

子字段 $6$ 中录入的数据按下列结构记录：


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>字符数</td><td style='text-align: center;'>字符位置</td></tr><tr><td style='text-align: center;'>（1）连接说明代码</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>（2）连接号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1-2</td></tr><tr><td style='text-align: center;'>（3）被连接字段标识符</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3-5</td></tr><tr><td style='text-align: center;'>数据元素说明如下：</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

1）连接说明代码(字符位置 0)

此代码说明字段间连接的原因。其值定义为：

a=交替文字

z=其他连接原因

2）连接号(字符位置 1-2)

用两位数字，记录相互连接的各自字段的$6$子字段。它的功能是用于匹配相互连接的字段，在任何情况下都不作为顺序号或地址号。只要分配的连接号在成对或成组的相互连接的每个字段中是一致的，并能与记录中分配给其他成对或成组的字段的连接号区分开，连接号就可以随机赋值。

3） 被连接字段标识符(字符位置 3-5)

本元素是由三个字符组成的用于字段连接的标识符。该元素可选用：若相互连接的两个字段的标识符一致，此元素通常被省略。

#### 5.8.2 $7 字段的字母/文字

本子字段含有表示字段主要内容的字母或文字的代码。

编目文字（馆藏位置、附注等）标识于记录的100字段（20-21字符位）。一些机构需要以多种文字形式记录馆藏位置、附注和馆藏说明，若语言有音译和另一种文字的表达形式（又称交替文字形式）（如汉字的简体与繁体形式；日语的假名和汉字体系）。馆藏位置、附注和馆藏说明的交替文字标识可在一条馆藏记录中同时存在。

馆藏位置说明的交替文字形式可记录于附加的2-馆藏位置字段中，用一个$7 编目文字子字段和基本馆藏位置子字段的形式与100字段中定义的文字加以区分。附注或馆藏说明的交替文字重复记录在它们各自字段块中的字段里。

相同馆藏位置、附注或馆藏说明的不同文字形式，通过一个$6$连接子字段进行连接，并将这些文字标识于$7$编目文字子字段及基本地址子字段内。当100字段20-21字符位的代码标识的字母/文字与含有$7$子字段标识的字母/文字相同时，字段中的$7$子字段通常可以省略。

示例：

001 163279

100 ## $ aYYYYMMDDenga03####ba0

252 # # $6a01$ a[机构标识符]$i[索取号]

252 # # $6a01$7ca$a[西里尔文字的机构标识符]$j[西里尔文字的索取号]

### 5.9 标识符号

GB/T 24424—2009 对一般馆藏项和馆藏范围项中的标识符号与分隔符作了规定，对各数据项之间使用的分隔符，以及馆藏地数据项、著录日期项和馆藏附注项中的标识符号未作规定。

为了 CN MARC 用户间的一致性，本标准推荐，除少量特例外，子字段间的标点可省略。记录中所有其他标点符号的使用可依据编目机构发行记录的实际情况而定。

### 5.10 格式应用

馆藏款目记录

此格式主要用于支持馆藏款目记录的信息交换。为此而创建的记录还可支持与馆藏位置和检索相关的交替馆藏款目。5—字段可用于说明馆藏的样式、标识说明、编次和年代。

书目款目模型

依据 GB/T 24424—2009 一个书目款目定义如下：

书目款目

基本书目单元(可重复)

非连续出版物

单一部分

多部分

连续出版物/集成性资源

辅助书目单元(可重复)

非连续出版物

单一部分

多部分

连续出版物/集成性资源

依据此模型，一个书目款目可由一个或多个书目单元组成。每个书目单元可以是一个基本单元或一个辅助单元，也可以是连续的、集成的或非连续的单元。

## 多个编次

每个连续性资源或多部分单元都带有自己的编次体系，适合于馆藏记录标识所规定的基本书目单元的编次应予记录。

对于交替编次，若除正规编次体系外，还存在一个不断增加的编次体系或其他编次体系，则分别用等同标识把交替编次体系和其他编次体系记录于正规编次体系之后。当交替编次存在时，不同编次体系之间必然存在相互关系。

示例 1:

v.1-5=总1-60

### 5.11 CN Marc 馆藏记录字段与 GB/T 24424—2009 著录项的对照


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>CNMARC 馆藏记录</td><td style='text-align: center;'>GB/T 24424—2009 著录项</td></tr><tr><td style='text-align: center;'>记录头标</td><td style='text-align: center;'>一般馆藏项,单元标识类型</td></tr><tr><td style='text-align: center;'>0—标识块</td><td style='text-align: center;'>款目标识项</td></tr><tr><td style='text-align: center;'>1—编码信息块</td><td style='text-align: center;'>一般馆藏项</td></tr><tr><td style='text-align: center;'>2—馆藏位置和检索块</td><td style='text-align: center;'>馆藏数据项</td></tr><tr><td style='text-align: center;'>3—附注块</td><td style='text-align: center;'>馆藏附注项</td></tr><tr><td style='text-align: center;'>5—馆藏范围块</td><td style='text-align: center;'>馆藏范围项</td></tr><tr><td style='text-align: center;'>7—知识责任块</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8—来源信息块</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>GB/T 24424—2009 项/数据元素</td><td style='text-align: center;'>CNMARC 馆藏记录字段/子字段</td></tr><tr><td style='text-align: center;'>款目标识项</td><td style='text-align: center;'>004</td></tr><tr><td style='text-align: center;'>馆藏数据项</td><td style='text-align: center;'>2--</td></tr><tr><td style='text-align: center;'>机构标识</td><td style='text-align: center;'>252  a</td></tr><tr><td style='text-align: center;'>分馆藏地标识</td><td style='text-align: center;'>252  b</td></tr><tr><td style='text-align: center;'>复本标识</td><td style='text-align: center;'>252  n</td></tr><tr><td style='text-align: center;'>索取号</td><td style='text-align: center;'>252  j</td></tr><tr><td style='text-align: center;'>报告日期项 $ ^{1)} $</td><td style='text-align: center;'>100  a/0-7</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>005</td></tr><tr><td style='text-align: center;'>一般馆藏项</td><td style='text-align: center;'>记录头标和 1--</td></tr><tr><td style='text-align: center;'>单元标识的类型</td><td style='text-align: center;'>记录头标字符位 7</td></tr><tr><td style='text-align: center;'>完整性标识</td><td style='text-align: center;'>171  a/5</td></tr><tr><td style='text-align: center;'>采访状态标识</td><td style='text-align: center;'>170  a/0</td></tr><tr><td style='text-align: center;'>保存原则标识</td><td style='text-align: center;'>171  a/0</td></tr><tr><td style='text-align: center;'>馆藏范围项</td><td style='text-align: center;'>5--</td></tr><tr><td style='text-align: center;'>单元名称</td><td style='text-align: center;'>50-  j</td></tr></table>

单元范围 50-\$k

编次

51-

年代                                                                                                      51-

特殊范围附注 50- $1

馆藏附注项                           3—

### 5.12 CNMARC 馆藏记录和 CNMARC 书目记录相关字段之间的对照

CNMARC 馆藏记录字段

CNMARC 书目记录字段

004 相关书目记录标识号



001 记录标识号

035 其他系统控制号

035 其他系统控制号

252 馆藏位置和索取号



852 馆藏位置和索取号

256 电子资源地址和检索

856 电子资源地址和检索

CNMARC 馆藏记录中有效的 CNMARC 书目记录字段

130 编码数据字段: 缩微制品

135 编码数据字段: 电子资源

141 编码数据字段: 外国古籍-藏本形态特征

194 编码数据字段: 中国古籍-藏本形态特征

300 一般性附注

301 标识号附注

302 编码信息附注

310 装订及获得方式附注

316 现有藏本的附注

317 出处附注

318 操作附注

345 采访信息附注

702 个人名称-次要知识责任（与藏本相关）

712 团体名称-次要知识责任（与藏本相关）

722 家族名称-次要知识责任（与藏本相关）

### 5.13 说明性附注

本标准采用下列约定符号：

a）用“$”代替 GB/T 1988 中的分隔符 IS1（字符集中 1/15 位），作为子字段标识的第一个符号；

b）字符“#”在样例中用于表示一个空位。

c）在样例中字段的分隔符不显示。

d）“未定义”，表示指示符所在位置没有定义赋值。该位置标识空位。

e）某些子字段需要使用由外部维护的代码表。这些代码表包含在 GB/T 33286—2016 的附录 A 中。

### 5.14 字段描述结构

第 6 章对各种数据字段的名称、定义、出现情况、指示符、子字段及内容等作详细说明，并提供应用示例。完整示例参见附录 A。本标准中的各数据字段均按照以下步骤描述：

a）字段说明：对每个字段的内容作简短说明；

b）出现情况：说明字段是否可以重复、是否为必备或选择使用字段。必要时对字段的出现情况作出限定和解释。格式对每一个字段、子字段均给出了是否重复的限定说明；

c) 指示符: 对指示符的赋值加以说明;

d）子字段：顺序列出各子字段，每个子字段之后是定义、适用范围以及是否重复和是否必备的说明；

e） 示例：通过举例，说明字段的具体应用。

### 5.15 国内使用字段

字段标识符中含有“9”的字段，即9—、9—、9等字段，或子字段$9，是本标准在UNIMARC基础上追加的适合中国使用的字段或子字段。

## 6 记录头标和数据字段——详细说明

### 6.1 记录头标(record label)

该部分包含根据 GB/T 2901 的规定所提供的对记录进行处理时所需的通用信息。

记录头标出现在每条记录的开头。必备，不可重复。

## 字段标识符、字段指示符和子字段

记录头标没有字段标识符、字段指示符和子字段。

## 定长数据元素

头标中的数据元素是由字符位置标识的。头标的总长度为 24 个字符。字符位置规定从 0 至 23。


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>字符数</td><td style='text-align: center;'>字符位置</td></tr><tr><td style='text-align: center;'>（1）记录长度</td><td style='text-align: center;'>5</td><td style='text-align: center;'>0-4</td></tr><tr><td style='text-align: center;'>（2）记录状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>（3）执行代码</td><td style='text-align: center;'>4</td><td style='text-align: center;'>6-9</td></tr><tr><td style='text-align: center;'>（4）指示符长度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>（5）子字段标识符长度</td><td style='text-align: center;'>1</td><td style='text-align: center;'>11</td></tr><tr><td style='text-align: center;'>（6）数据基地址</td><td style='text-align: center;'>5</td><td style='text-align: center;'>12-16</td></tr><tr><td style='text-align: center;'>（7）记录附加定义</td><td style='text-align: center;'>3</td><td style='text-align: center;'>17-19</td></tr><tr><td style='text-align: center;'>（8）地址目次区项目结构</td><td style='text-align: center;'>4</td><td style='text-align: center;'>20-23</td></tr></table>

## 数据元素说明如下：

## a） 记录长度(字符位置 0-4)

用五位十进制数字代码表示整个记录的字符总数，包括记录头标、地址目次区、数据字段区和记录结束符。右对齐，不足的字符位标识“0”（零）。当为了交换而组装成 MARC 记录时，该项数据通常由计算机自动生成。

## b) 记录状态(字符位置 5)

用一位字符，表示记录的处理状态。

c= 更正或修改过的记录

做过修改、更新、或删除过字段的馆藏记录。

## d= 被删除的记录

标识不再有效的馆藏记录。该馆藏记录可以仅包含头标、地址目次区和001（记录控制号）字段，也可以包含馆藏记录发行时的全部字段。无论哪种情况，均可在300一般性附注字段说明记录被删除的原因。

## n= 新记录

新的馆藏记录。

c) 执行代码(字符位置 6-9)

其所以称“执行代码”，是因为该组代码在 GB/T 2901 中未定义，但在其各个执行标准中都作出了具体规定。

b=多部分文献

全部或计划全部由数量有限的若干单独的物理部分组成的文献。

以独立部分连续发行的连续性资源，通常带有编号，但没有预定的结束期限。使用代码“c”的资料有：期刊、杂志、电子期刊、连续性指南、年度报告、报纸及专著丛编。

以更新方式补充或变更的书目文献/资源，更新的部分融入整体当中，不再保持独立性。集成性资源可以是有限的，或连续的。使用代码“d”的资料有：更新的活页资料、数据库和更新式网站。

u=未知的馆藏类型

2) 单元类型标识(字符位置 7)

一位字符代码表明适合下列一般性馆藏信息和/或馆藏范围的文献的特定组成部分。

# = 无信息提供

a= 基本书目单元

b= 辅助书目单元: 补充资料

c= 辅助书目单元: 索引

x= 不适用

3) 复本类型说明(字符位置 8)

a=特定复本说明

馆藏地单一复本的馆藏说明。

b=单一馆藏地/子馆藏地多复本的复合说明

对单一馆藏地或子馆藏地所藏两个或两个以上复本的馆藏说明。

c=两个或两个以上子馆藏地所藏复本的复合说明

将两个或两个以上子馆藏地所藏复本的说明整合为一个馆藏说明。

4）未定义(字符位置 9)

标识空位“#”

d） 指示符长度(字符位置 10)

用一位十进制数字代码表示字段指示符长度。格式中取值“2”。

e） 子字段标识符长度（字符位置 11）

用一位十进制数字代码表示子字段标识符(如$\mathrm{S a}$)的长度，格式中取值“2”。

f) 数据基地址(字符位置 12-16)

用 5 位十进制数字代码表示相对于记录开头的第一个数据字段的起始字符位置。右对齐，不足的字符位标识“0”（零）。由于记录的第一个字符位定义为“0”位，所以，记录的数据基地址代码等于记录头标和地址目次区（包括该区末尾的字段分隔符）字符数量的总和。在地址目次区中，每个字段的起始字符位置是相对于第一个数据字段的第一个字符的位置，并不是从记录的

首位算起。每个字段的位置都可根据基地址算出。该基地址数在组装 MARC 记录时自动生成。

g） 记录附加定义(字符位置 17-19)

## 用三个字符位表示处理记录所需的细节。

## 1 ）级别代码(字符位置 17)

级别代码包含一位字符的代码，标识馆藏说明特定的级次。单一部分文献的馆藏说明按1级要求著录。多部分文献、连续出版物或集成性资源的馆藏说明可以按任何级别的要求记录。

## 1 =1 级

标识文献及其收藏机构。该级别用以标识单一部分文献，但不能标识多部分文献或连续出版物的馆藏范围。

## 2 =2 级

在 1 级基础上增加有关收藏机构的一般馆藏总原则。

## 3 =3 级

包含馆藏范围的简要说明。

## 4 =4 级

对馆藏范围进行详细说明。

## m= 混合级

表明馆藏说明的级别是混合型的，例如用于回溯和现有馆藏的馆藏说明的级别不同时。

u=未知

## z=其他级别

## 2 ）记录中的单册信息(字符位置 18)

一位字符的代码，表明记录中是否含有单册信息，该信息可包含在一次或多次出现的530-532字段中。

0=无单册信息

1=有单册信息

x= 不适用

## 3 ）未定义(字符位置 19)

标识空位“#”。

## h）地址目次区项目结构(字符位置 20-23)

用 4 位字符代码为地址目次区中每一个地址目次项的结构提供说明。4 位字符的内容定义如下：

## 1 ）“字段长度”的长度(字符位置 20)

用一位十进制数字代码表示每个地址目次区内“字段长度”部分的字符位数。格式取值“4”。本标准允许的字段最大长度为9,999个字节。

## 2 ）“起始字符位置”长度(字符位置 21)

用一位十进制数字代码表示每个地址目次区内“起始字符位置”部分的字符位数。格式取值“5”。本标准允许的记录最大长度为99,999个字节。

## 3 ）“执行定义部分”长度(字符位置 22)

用一位十进制数字代码表示每个地址目次区内“执行定义部分”所占的字符位数。由于本格式的地址目次区中不含这部分内容，故取值“0”。

## 4 ）未定义(字符位置 23)

标识空位“#”。

字符位置 值 注释

0 0

1 1

2 8 记录长度为 1824，不足的字符位标识“0”

3 2

4 4

5 n 一条新的记录

6 a 单一部分文献

7 a 基本书目单元

8 a 馆藏地单一复本的馆藏说明

9 # 未定义

10 2 指示符长度（总为 2）

11 2 子字段标识符长度（总为 2）

12 0

13 0

14 4 头标和地址目次区的字符总数为 457，即数据基地址为 457

15 5

16 7

17 1 1 级馆藏

18 0 无单册信息

19 # 未定义

20 4 每个地址目次款目中的“字段长度”（总为 4）

21 5 每个地址目次款目中的“起始字符位置”（总为 5）

22 0 “执行定义部分”长度总为 0

23 # 未定义

示例 1:

01824naaa#220045710#450#

单一部分文献，单一复本，存放单一馆藏地，馆藏级别为1，无单册信息。

### 6.2 标识块 (identification block)

本标识块包含用以标识记录或文献藏本的编号。定义的字段如下：

001 馆藏记录标识号

004 相关书目记录标识号

005 记录处理时间标识

035 其他系统控制号

070 财产号

每条记录的 001 和 004 字段为必备字段。其他字段在具有有效数据时出现。

## 001 馆藏记录标识号(holdings record identifier)

本字段包含与记录唯一相关的标识号。即编制本馆藏记录机构分配给本记录的控制号。

对所有馆藏记录，本字段必备，不可重复。

指示符

遵照 GB/T 2901，本字段无指示符。

子字段

遵照 GB/T 2901，本字段不设子字段。

示例 1:

001 4331366

注：中国国家图书馆编制的一条馆藏记录标识号。

示例 2:

001 978-7-5013-4076-7

注：中文普通图书《图书馆馆藏组织与管理研究》的国际标准书号。

## 004 相关书目记录标识号(related bibliographic record identifier)

本字段包含被揭示馆藏文献的书目记录标识号。若该标识号是与馆藏记录相关的书目记录的记录标识号，建议在该标识号前冠以分配机构或系统的名称标识，并将该名称标识置于圆括号中。

对所有馆藏记录，本字段必备，不可重复。

## 指示符

遵照 GB/T 2901，本字段无指示符。

## 子字段

遵照 GB/T 2901，本字段不设子字段。

示例 1:

004 (NLC)002347490

注：本例是与馆藏记录相关的书目记录标识号，中国国家图书馆的标识置于前面的圆括号中。

示例 2:

004 ISBN 7-5013-3183-9

注：本例表示与馆藏记录相关的书目记录标识号，且书目记录标识号是文献的国际标准书号。

示例 3:

004 ISSN 0578-073X

注：本例表示与馆藏记录相关的书目记录标识号，且书目记录标识号是文献的国际标准连续出版物号。示例4：

004 B7512345

注：本例表示与馆藏记录相关的书目记录标识号，该号是英国国家书目记录标识号。

示例 5:

004 (PTBN)345231

注：本例是与馆藏记录相关的书目记录号，葡萄牙国家图书馆的标识置于前面的圆括号中。

## 005 记录处理时间标识(version identifier)

本字段包含记录的最后处理日期和时间，以便系统判断所处理记录的版本情况。

本字段选择使用，不可重复。

## 指示符

遵照 GB/T 2901，本字段无指示符。

## 子字段

遵照 GB/T 2901，本字段不设子字段。

本字段的数据元素长度为 16 位。日期和时间形式遵循 GB/T 7408（，其标准形式为 YYYYMMDDHHMMSS.T。其中，YYYY 表示年，MM 表示月，DD 表示日，HH 表示小时，MM 表示分，SS 表示秒，T 表示 1/10 秒。

各项数据均右对齐，不足的字符位标识“0”（零）。

示例 1:

005 20020712141236.0

注：最后一次处理日期是2002年7月12日14:12:36（即下午2:12:36）。为保持格式一致，“7月”输入为“07”而不是“7”。

示例 2:

005 20071022092345.0

注：最后一次处理日期是2007年10月22日9:23:45（即上午9:23:45）。为保持格式一致，“9点”输入为“09”而不

是“9”。

## 035 其他系统控制号(other systems control number)

本字段包含从其他来源获取的馆藏记录或书目记录的系统控制号。

本字段选择使用，可重复。

## 指示符

指示符 1:0 馆藏记录号

1 书目记录号

指示符2:空(未定义)

## 子字段

## 1 子字段表

子字段标识符 子字段内容 注释

$ a 

系统控制号 不可重复

$ z 

注销或无效的系统控制号 可重复

## 2 子字段说明

$a$ 系统控制号

系统控制号由源数据的记录标识号和产生该号的机构代码组成，机构代码前置，并置于圆括号括内。机构代码可以使用机构全称或是国家代码。若选用本字段，则$\$a$子字段必备，不可重复。

$ z$ 注销或无效的系统控制号

已被注销或无效的系统控制号。有则必备，可重复。

示例 1:

035 0$ a(PTBN)1003263

注：葡萄牙国家图书馆分配的原始馆藏记录控制号。

示例 2:

 $$ 035\ 1\neq\left(a\left(OCoLC\right)1553114\right)\left(z\left(OCoLC\right)153114\right) $$ 

注：OCLC 分配的书目记录控制号。原分配的记录号无效，并被取代，记录于 $z$ 子字段。

## 示例 3:

001 CAL#032000158426

035 1$ a(NII)BN1204045X

注：该记录的原始编目机构为日本文部省国立情报研究所（NII），其机构代码和所分配的记录标识号置于035字段。

示例 4:

035 0$ a(NLC)4168683

注：中国国家图书馆分配的原始馆藏记录控制号。

## 070 财产号(inventory number)

本字段包含馆藏机构分配的登录号、典藏号、借阅号或其他号码，以及卷册和复本标识，对文献管理起重要作用。

本字段选择使用，可重复。

指示符

指示符1：☑ 未指定编号类型

1 登录号

2 典藏号

3 借阅号

8 其他

指示符2：# 无定义关系

## 1 与排架号相同

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ b</td><td style='text-align: center;'>卷册标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ c</td><td style='text-align: center;'>复本标识</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 编号

包含文献的登录号、典藏号或借阅号，也可是其他能唯一标识文献的编号。不可重复。

$b$ 卷册标识

说明编号对应文献的卷册标识。有则必备，不可重复。

$c$ 复本标识

说明编号对应文献的复本标识。不可重复。

示例 1:

070 1≠ $ a43278

示例 2:

070 1$ a57823$ bv.1$ ccopy2

注：登录号标识第一卷的第二复本。

示例 3:

070 3$ aH316/15$ c 复本 4

注：索书号标识专著的第四复本。

### 6.3 编码信息块(coded information block)

本编码信息块包含与文献及其复本相关的定长编码数据元素。字段中的数据元素以字符位置定义。各子字段标识符后第一个字符位置为“0”位。若编目机构未给在编字段提供任何编码信息，该字段可省略（必备字段除外）。如果在一个字段中提供的数据不完整，则该字段相应的空缺位置应用填充符“|”标识。定义的字段如下：

100 通用处理数据

170 编码数据字段:采访状态

171 编码数据字段: 收藏管理

172 编码数据字段:信息服务政策

CNMARC 馆藏记录中有效的 CNMARC 书目记录字段

130 编码数据字段: 缩微品——形态特征

135 编码数据字段:电子资源

141 编码数据字段: 外国古籍——藏本形态特征

194 编码数据字段:中国古籍——藏本形态特征

100 字段为必备字段。其他字段根据馆藏说明的级别选择使用。

## 100 通用处理数据(general processing data)

本字段包含适用于所有类型馆藏记录的基本编码数据。

对所有馆藏记录，本字段必备，不可重复。

## 指示符

指示符1:空(未定义)

指示符2:空(未定义)

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>通用处理数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 通用处理数据

子字段 $a$ 以字符位置标识全部数据。字符位从 0-22 计数，总长度为 23 个。所有被定义的字符位应在该子字段中出现。不可重复。

## 子字段 $a$ 定长数据元素表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>字符数</td><td style='text-align: center;'>字符位置</td></tr><tr><td style='text-align: center;'>(1) 入档日期(必备)</td><td style='text-align: center;'>8</td><td style='text-align: center;'>0-7</td></tr><tr><td style='text-align: center;'>(2) 编目语种(必备)</td><td style='text-align: center;'>3</td><td style='text-align: center;'>8-10</td></tr><tr><td style='text-align: center;'>(3) 音译代码</td><td style='text-align: center;'>1</td><td style='text-align: center;'>11</td></tr><tr><td style='text-align: center;'>(4) 字符集(必备)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>12-15</td></tr><tr><td style='text-align: center;'>(5) 补充字符集</td><td style='text-align: center;'>4</td><td style='text-align: center;'>16-19</td></tr><tr><td style='text-align: center;'>(6) 编目文字</td><td style='text-align: center;'>2</td><td style='text-align: center;'>20-21</td></tr><tr><td style='text-align: center;'>(7) 编目文字书写方向</td><td style='text-align: center;'>1</td><td style='text-align: center;'>22</td></tr></table>

## 数据元素说明如下：

## a）入档日期(必备)(字符位置 0-7)

用八位数字代码表示日期。日期以 GB/T 7408（标准形式 YYYYMMDD 记入。其中 YYYY 表示年，MM 表示月，DD 表示日。月、日不足两位时前置“0”。未提供数据元素时以填充符“|”补充。入档时间通常是记录建立或以机读形式输入计算机文档的时间。该时间不因记录修改或参与交换而改变。

示例：

20000520

注：记录入档日期为2000年5月20日。

## b） 编目语种代码(必备)(字符位置 8-10)

用三位字符代码表示编目使用的语种。语种是指在2--馆藏位置和检索块中使用的语种，并且任何限定词、注释或其他说明性信息均使用该编目语种。该代码的选取与CNMARC书目格式所用语种代码表相同，均取自GB/T4880.2。

本格式没有对个别字段所用语种进行标识。

本格式没有对个别字段所用语种进行标识。

## c) 音译代码(字符位置 11)

用一位字符代码表示记录中 2--馆藏位置和检索块所采用的音译方案。

a=ISO 音译方案，包括汉语拼音方案

b=其他音译方案

c=多种音译体系:ISO或其他方案

d=由国家书目机构制定的音译表

e= 没有确定的音译表的音译方案

f=其他已确定的音译方案

y=未使用音译方案

## d) 字符集(必备)(字符位置 12-15)

用两组双位字符代码表示用于记录交换中的主要字符集。12-13 字符位标识 G0 集，14-15 字符位标识 G1 集。G1 集不需要时，14-15 字符位标识空位。有关字符集定义如下：

01 = ISO 646, IRV version(基本拉丁字符集)

02 = ISO Registration # 37(基本基里尔字符集)

03 = ISO 5426(扩充拉丁字符集)

04 = ISO 5427(扩充基里尔字符集)

05 = ISO 5428(希腊字符集)

06 = ISO 6438(非洲编码字符集)

07 = ISO 10586(格鲁吉亚字符集)

08 = ISO 8957-表 1(希伯莱字符集 1)

09 = ISO 8957-表 2(希伯莱字符集 2)

10 = GB/T 2312(信息交换用汉字编码字符集基本集)

11 = ISO 5426-2(扩充拉丁字符集 2 用于欧洲小文种和陈旧印刷形式的拉丁字符)

50 = ISO 10646 Level 3(Unicode 统一编码字符集)

## e） 补充字符集(字符位置 16-19)

用两组双位字符代码表示最多两个在记录交换中使用的补充字符集。其编码与上面列出的12-15字符位的编码相同。16-17字符位标识G2集，18-19字符位标识G3集。若不需要补充字符集，则上述四个字符位标识空位。

## f）编目文字(字符位置 20-21)

用一组双位字符代码表示文献编目所使用的文字。即2-字段中的记录信息、修饰词、注释和其他说明信息均使用的文字。

用一组双位字符代码表示文献编目所使用的文字。即2-字段中的记录信息、修饰词、注释和其他说明信息均使用的文字。
ba=所有使用拉丁字符的文种

ca=所有使用基里尔字符的文种

da=广义日文

db=日文——汉字

dc=日文——假名

ea=广义中文

fa=阿拉伯文

ga=希腊文

ha=希伯莱文

ia=泰文

ja=梵文

ka=朝鲜文

la=泰米尔文

ma=格鲁吉亚文

mb=亚美尼亚文

zz=其他

## g）编目文字书写方向(字符位置 22)

用单个字符编码表示编目文字的书写方向，该文字的编码记录在100字段的20-21字符位置。

示例 1:

100 ## $ a20090412pory0103##b0

注：编目语种为葡萄牙语，未使用音译，使用 ISO 646（基本拉丁字符集）、ISO 5426（扩充拉丁字符集），编目文字为拉丁文，编目文字书写方向为从左至右。

示例 2:

100 # # $ a20140714chiy50 # # # # # # ea0

注：编目语种为中文，未使用音译，使用 ISO 10646（Unicode 统一编码字符集）编目文字为广义中文，编目文字书写方向为从左至右。

## 130 编码数据字段: 缩微品——形态特征(coded data field: microforms-physical attributes)

本字段包含与缩微品相关的编码数据。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

若文献仅为缩微品形式，则 CN MARC 书目格式中的 130 字段必备。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 135 编码数据字段: 电子资源(coded data field: electronic resources)

本字段包含关于电子资源的编码数据。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

若文献仅为电子资源形式，则 CN MARC 书目格式中的 135 字段必备。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 141 编码数据字段: 外国古籍——藏本形态特征(coded data field: antiquarian-copy specific attributes)

本字段包含有关外国古籍藏本形态特征的编码数据。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 170 编码数据字段: 采访状态(coded data field: acquisition status)

本字段包含适用于所有类型馆藏记录的编码数据。该数据表示馆藏揭示机构是否已经或即将获取某种文献。

本字段选择使用，不可重复。

指示符

指示符1:空(未定义)

指示符2:空(未定义)

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>采访状态标识</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 采访状态标识,不可重复。

子字段 $a$ 以字符位置标识全部数据。字符位从 0-9 计数，共计 10 位字符表示馆藏揭示时文献特定采访状态。该数据表示馆藏揭示机构是否已经或即将获取的某种文献。

## 子字段 $a$ 定长数据元素表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>字符数</td><td style='text-align: center;'>字符位置</td></tr><tr><td style='text-align: center;'>（1）接收或采访状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>（2）获得方式</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>（3）计划删除的日期</td><td style='text-align: center;'>8</td><td style='text-align: center;'>2-9</td></tr></table>

数据元素说明如下：

a）接收或采访状态(字符位置 0)

## #=无信息提供

## a=收全或终止

用于已接收的单部分或完整的多部分文献，或用于已终止的连续性资源。

## b=订购中

用于已订购但未收到的连续或非连续性单元。

## c=定期接收

用于定期接收的连续性单元。

## d=尚未收到(当前未收到)

用于记录无论何种原因尚未收到的最新出版的连续性单元。

u=未知

z=其他

## b) 获得方式(字符位置 1)

a=购买

用购买方式获得。

b=赠品

以非购买方式获得。通常指随购买文献所附的赠品。

c=存放

未改变所有权将文献暂存到某一机构。

## d=呈缴

根据本国法或国际法缴送。

e=交换

以实物交换的方式获得。

## f= 国际交换

国际上以实物交换的方式获得。

g=免费

以赠品、捐赠或遗赠方式获得，非购买或交换。

## h=捐赠

文献以无偿或有偿方式赠与某机构。

i=合并

包含以上各种情况。

## j= 遗赠(捐赠)

由遗嘱指定捐赠对象机构。有时在特定条件下，机构会拒绝接受。

x= 不适用

z=其他

## c) 计划删除的日期(字符位置 2-9)

用八个字符表示计划注销的有效日期，或多部分、连续性资源最后一部分预期到达日期。该数据依据 GB/T 7408 的标准，其标准形式为 YYYYMMDD。任何未知部分以“00”记录，########表示无意删除或不适用。如：20010500 表示计划删除日期为 2001 年 5 月，20020707 表示计划删除日期为 2002 年 7 月 7 日，00000000 表示计划删除日期未知。

## 示例 1:

## 170 ## $ aaj ## ## ## ##

注：单一部分文献 $ \left(\mathrm{S}_{\mathrm{a}}/0=\mathrm{a}\right) $ ，获得方式为遗赠 $ \left(\mathrm{S}_{\mathrm{a}}/1=\mathrm{j}\right) $ ，“计划删除日期”为不适用 $ \left(\mathrm{S}_{\mathrm{a}}/2-9=\mathrm{j}\right) $ 

示例 2:

170 ## $ aba20030000

注：在订购中的多部分文献( $ S_{a/0}=b $ )，获得方式为购买( $ S_{a/1}=a $ )，预计最后一卷到馆日期为2003年( $ S_{a/2-9}=20030000 $ )。

## 171 编码数据字段: 收藏管理(coded data field: collection management)

本字段包含适用于所有类型馆藏记录的编码数据，该数据表示所描述文献的范围、利用与保存政策。

本字段选择使用，不可重复。

## 指示符

指示符1:空(未定义)

指示符2:空(未定义)

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>编码数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 编码数据,不可重复。

子字段 $a$ 以字符位置标识全部数据。字符位从 0-8 计数，共计 9 位字符表示馆藏文献的范围、利用与保存政策。

## 子字段 $a$ 定长数据元素表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>字符数</td><td style='text-align: center;'>字符位置</td></tr><tr><td style='text-align: center;'>（1）一般保存政策</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>（2）可获取性</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>（3）特定保存政策</td><td style='text-align: center;'>3</td><td style='text-align: center;'>2-4</td></tr><tr><td style='text-align: center;'>（4）完整性标识</td><td style='text-align: center;'>1</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>（5）所揭示的复本数量</td><td style='text-align: center;'>3</td><td style='text-align: center;'>6-8</td></tr></table>

数据元素说明如下：

## a）一般保存政策(字符位置 0)

#=无信息提供或不适用

a=永久保存

馆藏机构永久保存所揭示文献的全部册件。

b=保存到由其他替代品代替

c=保存到由累积本、置换卷或修订本替代

d=限制保存(非永久保存部分)

文献的部分内容保存一段时间(如保存三个月,当年保存)或保存文献的某些特定卷册(如每个第三期,最后两卷),文献限制保存的特定时间和部分单元可以记录在字段的2-4字符位中。

e= 样品保存

f=不保存

z=其他

## b） 可获取性(字符位置 1)

#=无信息提供

a=处理中

b=可获取

c= 在特定条件下可获取

d=不可获取

u=不详

z=其他

## c) 特定保存政策(字符位置 2-4)

当字段第1字符位置赋值为d时，用三位字符代码表示被保存文献的特定部分。 $ \#\#\# $ 表示无特定保存。

## 1 ）保存政策类型(字符位置 2)

a= 先前的

表示早期的或部分单元被保存(不包括现刊)。

b=最近的

表示近期的或部分单元被保存(包括现刊)。

2）单元号(字符位置 3)

用一位字符数字（1-9）表示需要保存的时间或单元的数量。当第2字符位保存政策代码为最近（代码b）时，该字符数字表明包括当前期的或部分文献被保存；当第2字符位保存政策代码为先前（代码a）时，该字符数字表明所保存的文献不包括当前期的或部分单元。

## 3 ） 时间或部分单元(字符位置 4)

a=周

b=月

c=年

d= 版本

e=期或卷

f= 补编

## d) 完整性标识(字符位置 5)

提供机构馆藏范围的有关信息，依据该机构自我评估的馆藏信息取值。

#=无信息提供

若馆藏揭示机构很难获得馆藏完整性的有效信息，则赋值“#”；当连续性资源已被限制保存时，亦赋值“#”。

a= 完整(95%-100%馆藏)

适用于连续性资源和多部分文献。

b= 不完整(50%-94%馆藏)

适用于连续性资源和多部分文献。

c= 非常不完整或分散(少于50%馆藏)

适用于连续性资源和多部分文献。

x= 不适用

适用于单部分文献。

e）所揭示的复本数量(字符位置 6-8)

三位字符标识被揭示的复本数量，右对齐，不足位用“0”补齐。

示例 1:

171 ## $ adba3a#001

注：此例表示保存的馆藏文献为已被限制保存的先前部分的连续性资源，保存期限为三周，文献可获取。限制保存 $ \left(\mathrm{a}/0=\mathrm{d}\right) $ 文献可获取 $ \left(\mathrm{a}/1=\mathrm{b}\right) $ 先前的 $ \left(\mathrm{a}/2=\mathrm{a}\right) $ 三 $ \left(\mathrm{a}/3=3\right) $ 周 $ \left(\mathrm{a}/4=\mathrm{a}\right) $ 。连续性资源已被限制保存

 $ \left( \\mathrm{a}/5 = \right) $ ，存有1个复本 $ \left( \\mathrm{a}/6 - 8 = 001 \right) $ 。

示例 2:

171 ## $ afb ## x001

注：此例表示不保存的单部分文献，可获取。文献不保存 $ \left(\mathrm{a}/0=\mathrm{f}\right) $ 可获取 $ \left(\mathrm{a}/1=\mathrm{b}\right) $ 无特殊保存要求 $ \left(\mathrm{a}/2-4=\right. $ 

 $ \left.\left.\begin{array}{l}\right.\right. $ 

 $ \left.\left.\begin{array}{l}\end{array}\right.\right) $ 

 $ \left(\mathrm{a}/5=\mathrm{x}\right) $ ，存有1个复本 $ \left(\mathrm{a}/6-8=001\right) $ 。

## 172 编码数据字段:信息服务政策(coded data field: information service policy)

本字段包含适用于所有类型馆藏记录的编码数据，表示馆藏记录中一个书目单元或其中的一个物理单元的咨询参考、外借或复制的一般政策。

本字段选择使用，不可重复。

指示符

指示符1:空(未定义)

指示符2:空(未定义)

子字段

1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>编码数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 编码数据,不可重复。

子字段 $a$ 以字符位置标识全部数据。字符位从 0-2 计数，共计 3 位字符表示馆藏文献的咨询参考、外借或复制的一般政策。

## 子字段 $a$ 定长数据元素表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>字符数</td><td style='text-align: center;'>字符位置</td></tr><tr><td style='text-align: center;'>(1) 咨询参考政策</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>(2) 外借政策</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>(3) 复制政策</td><td style='text-align: center;'>1</td><td style='text-align: center;'>2</td></tr><tr><td style='text-align: center;'>数据元素说明如下：</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>a) 咨询参考政策(字符位置 0)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'># = 无信息提供</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>a = 可获取</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>b = 有条件地获取</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>c = 不可获取</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>u = 不详</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>b) 外借政策(字符位置 1)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'># = 无信息提供</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>a = 可外借</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>b = 不可外借</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>c = 可外借数量限制</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>d = 限制外借政策(详见 371 字段)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>u = 不详</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>c) 复制政策(字符位置 2)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'># = 无信息提供</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>a = 可复制</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>b = 不可复制</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

c=有条件复制(详见371字段)

u=不详

示例 1:

172 ## $ aaaa

注：此例表示文献可用于咨询参考( $ S a/0=a $ )，可外借( $ S a/1=a $ )和可复制( $ S a/2=a $ )。

示例 2:

172 ## $ aabb

注：此例表示文献只可用于咨询参考( $ S_{a}/0=a $ )，不可外借( $ S_{a}/1=b $ )也不可复制( $ S_{a}/2=b $ )。

## 194 编码数据字段: 中国古籍——藏本形态特征 (coded data field: Chinese antiquarian-copy specific attributed)

本字段包含有关中国古籍藏本形态特征的编码数据。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

### 6.4 馆藏位置和检索块(location and access block)

本馆藏位置和检索块包含用以标识一个书目单元保存或可获取的机构、物理地址或馆藏地的信息。一条馆藏记录应包含一个252字段或256字段，用以标识其馆藏物理位置，该馆藏物理位置是由机构标识符和一个或多个馆藏子地址标识符共同组成。2—字段块中的其他字段需要时可选用。定义的字段如下：

252 馆藏位置和索取号

255 先前馆藏位置和索取号

256 电子资源地址与检索

## 252 馆藏位置和索取号(location and call number)

本字段用以标识收藏文献的机构或可获取该文献的机构，本字段可包含如何查找馆藏文献的详细信息。

对于有物理馆藏地的文献，本字段必备，可重复。

指示符

指示符1：排架体系

说明使用的分类或排架体系。

☑ 未提供信息

未提供分类或排架体系信息。

0 分类排架体系(详细说明著录在子字段 $2$ 中)

1 固定排架

指按馆藏文献到馆的先后顺序排架的一种方式，而不是采用分类标记的相对位置。该指示符值也适用于采用宽泛的大分类范畴的固定排架。完整的排架号记录在$j$子字段。

2 顺序号

图书馆按照文献登录顺序或其他顺序所给出的编号，或采用出版、发行者自有的编号系统对文献进行分类时使用该值，如缩微平片、音像制品、标准等。完整的顺序号记录在$j$子字段。

3 著者、题名、著者/题名

按照著者、题名或著者/题名部分的字母顺序排架。

4 单独排架部分

该值用于专著丛编的记录，表明丛编中的各卷册都是分别分类和排架的。每卷册的记录都包含各自的馆藏信息。

若图书馆希望将丛编集中收藏在一起提供服务，丛编书目记录可以有一个整体的分类号，但每个独立的丛编卷册则无馆藏地信息。

5 其他

未对排架原则做详细说明。

## 指示符2：排架顺序

表示文献是否按主要编号或交替编号体系排架。

# 无信息提供

0 无编号

文献未按编号体系排架。

1 主要编号

当只有一个编号体系时，也使用该值。

2 交替编号

文献有两个编号体系，并按照次要编号体系排架。

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>馆藏机构标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>子馆藏地标识</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>地址</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>馆藏地限定代码</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$e</td><td style='text-align: center;'>非编码馆藏地限定</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$g</td><td style='text-align: center;'>索取号前缀</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$j</td><td style='text-align: center;'>索取号</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$k</td><td style='text-align: center;'>著者、题名、著者/题名排架形式</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$l</td><td style='text-align: center;'>索取号后缀</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$m</td><td style='text-align: center;'>单册标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$n</td><td style='text-align: center;'>复本标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$p</td><td style='text-align: center;'>国家代码</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$t</td><td style='text-align: center;'>复本号</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$x</td><td style='text-align: center;'>非公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$y</td><td style='text-align: center;'>公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$2</td><td style='text-align: center;'>系统代码</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$6</td><td style='text-align: center;'>内部字段间连接数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

## $a$ 馆藏机构标识符

标识收藏文献或可提供文献的机构或个人。该子字段包含机构代码或机构名称或个人的名称。可采用机构名称的英文缩写形式，也可以采用机构的中文全称或国家规定的代码。使用国家代码的机构应在说明如何使用交换格式的文件中声明。必备，不可重复。

## $b$ 子馆藏地标识

标识收藏或获得文献的馆藏机构的具体部门、分馆、收藏地或架位信息。它可以指出在馆藏或子馆藏地中的物理位置，例如，参考资料、特大装，并可以给出全称或标准缩写词或代码等，

如“Ref.”。当子馆藏地下面还有下层馆藏地时，本子字段才可重复。

## $c$ 地址

标识街道地址、城市、州/县，邮递区号/邮政编码等，以及文献当前物理馆藏地的国家信息。在给出的当前子馆藏地址不同于主馆藏地址时，给出子馆藏地址（$b$）。不可重复。

## $d$ 馆藏地限定代码

用一个 2 位或 3 位的字符代码标识同一文献中被放置在与其主馆藏地点不同的特定卷期。子字段 $d$ 直接跟在子字段 $a$ 或 $b$ 之后作为限定。不可重复。

## 限定类型

## a= 先前的

先前的(不包括当前的)时间单元或部分单元被放置在不同的馆藏地。

## b=最新的

最新的(包括当前的)时间单元或部分单元被放置在不同的馆藏地。

## 单元数量及其类型

## 1 -9 单元数量

当不需要用数量来识别特殊单元时，该单元数量可以被省略。当限定类型为最新时（代码b），该数量包括当前时间单元或部分单元。当限定类型为先前时（代码a），该数量不包括当前时间单元或部分单元。

## 单元类型

时间

a=周

b=月

c=年

部分

d=版

e=期

f=补编

## $ e 非编码馆藏地限定

当子字段$\$d$中的代码无法充分描述同一文献中被放置在与其主馆藏地点不同的特定卷期单元时，可采用自由行文的方式加以描述。子字段$\$e$直接跟在子字段$\$a$或$\$b$之后作为限定。不可重复。

## $g$ 索取号前缀

在索取号之前的术语。不可重复。

## $j$ 索取号

本子字段包含由文献收藏机构标识的包括标点符号、空格和大写在内的索取号。索取号也可以包括隐含的或明确的复本标识，或复本号，或卷期号，或排架或保管位置。当索取号采用独立成分的形式时，可选择适用的子字段。不可重复。

## $k$ 著者、题名、著者/题名排架形式

未分类的文献按题名部分、著者名称或著者/题名排架（第1指示符取3）。不可重复。

## $1 索取号后缀

跟在索取号后面的术语。可重复。

## $m$ 单册标识

本子字段包含一个独立册件的标识，也就是一个物理上分离的书目文献，该标识可作为识别号，如条码号或登录号。不可重复。

## $n$ 复本标识

具有相同馆藏地的复本数或复本数范围。若使用$n$子字段，复本标识数据元素应与子馆藏地标识和/或馆藏机构标识同时使用。在某些情况下，复本标识可以明确或者隐含地作为索取号的一部分。当复本标识采用独立的数据元素时，使用子字段$n$，在这种情况下没有必要在$j$子字段中重复复本标识。复合馆藏说明可用于记录书目文献在单一馆藏地或子馆藏地收藏的两个或多个复本的信息。不可重复。另外，单独的特定复本馆藏说明可用于记录每个复本的馆藏。

## $p$ 国家代码

包含子字段 $a$ 中标识的主馆藏地的国家代码。该代码取自 ISO 3166 的两位字符代码。不可重复。

## $t$ 复本号

具有相同馆藏地的复本数或复本数范围。某些情况下，复本号可明确作为索取号的一部分。当复本号采用独立的数据元素时，使用子字段$t$，在这种情况下没有必要在$j$子字段中重复复本号。复合馆藏说明可用于记录书目文献在单一馆藏地或子馆藏地收藏的两个或多个复本的信息。不可重复。另外，单独的特定复本馆藏说明可用于记录每个复本的馆藏。

## $x$ 非公共附注

不适合公共显示的信息。可重复。

## $y$ 公共附注

适合公共显示的信息。可重复。

## $2 系统代码

按特定分类或其他排架体系和版本排列文献的标识。当第1指示符为0时，应使用本子字段。不可重复。

## $6 内部字段间连接数据

子字段 $6$ 用于连接标识说明及样式字段（500）、编号与年代字段（510）、文字性馆藏字段（520）和单册信息字段（530）。有则必备，不可重复。

## 示例 1:

## 2524 $6z02aNLC$b中文图书基藏库

注：$a$ 馆藏机构代码“NLC”表示中国国家图书馆，$b$ 子馆藏地标识采用文字表述。该馆藏文献是专著丛编，按专著单独排架，指示符1的值选择“4”，其排架顺序未提供信息，指示符2的值选择“#”。

## 示例 2:

252 0$ 6z01$ aPUL$ bWL$ c北京大学物理楼物理学院分馆，邮编 100871$j04-43（上）$2clc

注：收藏机构和子馆藏地标识均采用代码，分别为“北京大学图书馆”和“物理学院分馆”，$c$ 记录馆藏地的详细地址，包括邮政编码。

## 示例 3:

252 11 $ 6z01 $ pPT $ aBN $ bReservados $ jRES 2678 A

255 11 $ 6z01 $ pPT $ aBN $ bFundo Geral $ jS.A.1130 A

注：带有一个先前的馆藏地址

## 示例 4:

252 51 $ 6z01 $ aNLR $ j2003-8/2905 $ t1 $ n560203

252 51 $ 6z02 $ aNLR $ j2003-8/2905 $ t2 $ n578374

注：在具有相同馆藏地的两个复本中，每个复本有自己的复本标识符（$n$）。同时在馆藏地中每个复本都带有自己的复本号（$t$）。复本号作为一个明确部分包含在索取号中。

2003-8

2003-8

-----/1

-----/2

2905

2905

## 255 先前馆藏位置和索取号(past location and call number)

本字段包含所收藏文献先前馆藏地的详细信息。
本字段选择使用，可重复。

本字段选择使用，可重复。
指示符
同 252 字段。
子字段
同 252 字段。
示例 1:
255 11 $6z01$ pPT $aBN$ bFundo Geral $jS.A.1130 A
注：新馆藏地为 RES 2678 A（见 252 例 11）

## 256 电子资源地址与检索(electronic location and access)

本字段包含定位书目记录所描述的电子文献地址所必需的信息。该信息用来标识文献或获取该文献的电子地址，还包括由指示符1定义的获取文献检索方法的信息。本字段包含的信息足以实现电子文件的传送，电子期刊的订购，或登录网上电子资源。在一些情况下，仅记录唯一的数据元素，该数据元素可以允许用户访问一个在远程主机中的地址列表，该列表包含访问这一资源所需要的其余信息。

本字段选择使用。当馆藏地数据元素（$a，$b，$d 子字段）不同和使用了多于一种的检索方法时，本字段可重复。当电子文件名（$f 子字段）不同时，本字段也可重复，但当单一部分文献作为网络存储或检索被划分成不同部分时，本字段不可重复。

## 指示符

指示符1：检索方法

☑ 未提供信息

0 电子邮件(Email)

1 文件传输协议(FTP)

2 远程登录(Telnet)

3 拨号入网(Dial-up)

4 超文本传输协议(HTTP)

<div style="text-align: center;"><img src="imgs/img_in_image_box_715_990_752_1026.jpg" alt="Image" width="3%" /></div>


7 在子字段 $y$ 说明检索方法

指示符2:空(未定义)

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>主机名称</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>检索号</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>压缩信息</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>路径</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$e</td><td style='text-align: center;'>咨询与检索的日期和时间</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$f</td><td style='text-align: center;'>电子文件名称</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$h</td><td style='text-align: center;'>用户名或处理器要求</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$i</td><td style='text-align: center;'>指令</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$j</td><td style='text-align: center;'>位/秒</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$k</td><td style='text-align: center;'>口令</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$l</td><td style='text-align: center;'>登录/注册</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$m</td><td style='text-align: center;'>协助检索的联系途径</td><td style='text-align: center;'>可重复</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>$n</td><td style='text-align: center;'>记录在 $a 的主机地址名称</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$o</td><td style='text-align: center;'>操作系统</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$p</td><td style='text-align: center;'>端口</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$q</td><td style='text-align: center;'>电子文件格式类型</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$r</td><td style='text-align: center;'>设置</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$s</td><td style='text-align: center;'>文件大小</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$t</td><td style='text-align: center;'>模拟终端</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$u</td><td style='text-align: center;'>统一资源标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$v</td><td style='text-align: center;'>有效检索时间</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$w</td><td style='text-align: center;'>记录控制号</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$x</td><td style='text-align: center;'>非公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$y</td><td style='text-align: center;'>检索方法</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$z</td><td style='text-align: center;'>公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$2</td><td style='text-align: center;'>链接文本</td><td style='text-align: center;'>可重复</td></tr></table>

## 2 子字段说明

## $a$ 主机名称

电子资源地址的合法域名。可重复。

## $b$ 检索号

包含与主机相关的检索号。若文献是一个互联网资源，该子字段包含互联网地址（IP），若通过电话拨号上网，则包含一个电话号码。该数据不是静态存储，而是经常改变且可由系统自动生成。电话号码的记录方式为：[国家代码]-[地区代码]-[电话号码]。若该电话号码带有分机号，在电话号码与分机号之间使用“x”。例如：1-703-3589800x515（带有分机号的电话号码）。可重复。

## $c$ 压缩信息

包含文件的压缩信息，说明是否需要一个特定的程序对文件进行解压。可重复。

## $d$ 路径

说明文件存储位置的逻辑目录与子目录名称。可重复。

## $ e$ 咨询与检索的日期与时间

记载电子文献最近一次被检索的时间，其形式为 YYYYMMDDHHMM，其中 YY 表示年，MM 表示月，DD 表示日，HH 表示小时，MM 表示分。不可重复。

## $f$ 电子文件名称

包含文件的电子名称，该名称存在于$\mathrm{S a}$ 子字段中标识的主机所属的由$\mathrm{S d}$ 子字段指明的目录/子目录中。若一个逻辑上的单独文件被划分成几部分或存储在不同的名称下时，$\mathrm{S f}$ 子字段可重复。在这种情况下，每一部分将构成一个单一的书目文献。而在其他情况下，可以在不同文件名下重复找到文件，它们包含在多次出现的256字段中，每个都有相应的在$\mathrm{S f}$ 子字段中说明的电子名称，一个文件名在必要时可以包含通配符（如“*”或“?”），如果需要，可在子字段$\mathrm{S z}$ 中说明文件命名的方法。某些系统文件名可能区分大小写。该子字段也可能包含电子出版物或会议的名称。可重复。

## $h$ 用户名或处理器要求

指用户名或对处理器的要求，通常指主机地址“@”之前的数据。不可重复。

## $i$ 指令

向远程主机请求处理信息所需要的指令或命令。可重复。

## $i 每秒传输的比特数

连接到主机的每秒可传输数据的最低或最高比特数（二进制单位）。记录每秒比特数（BPS）的语法为：[最低 BPS]-[最高 BPS]。若只提供最低值：用[最低 BPS]—。若只提供最高值：用[最高 BPS]。不可重复。

## $k$ 口令

用于记载一般使用的口令，不包括那些要求安全保密的口令。不可重复。

## $1 登录/注册

用于记载无安全保密的登录/注册用的字符串。不可重复。

## $ m$ 协助检索的联系途径

检索 $a$ 子字段标识的主机中的电子资源的有关联系信息。可重复。

## $n$ 记录在 $a$ 的主机地址名称

记录在 $a$ 的主机所在的地址名称或地理名称的完整形式。不可重复。

## $o 操作系统

记录在  $ \ $  a 的主机所用的操作系统。不可重复。

## $p$ 端口

用于标识主机的处理或服务的地址部分。不可重复。

## $q$ 电子文件格式类型

包含一个电子文件格式类型标识，格式类型决定了数据如何通过网络传输。通常文本文件可以作为字符数据来传输，一般限定文本文件为 ASCII（信息交换美国国家标准代码）字符集（即：基础拉丁字母，数字 0-9，少数特殊字符和多数标点符号）。带有 ASCII 字符集以外字符的文本文件或非文本数据（例如，计算机程序，影像数据）应使用其他文件传输模式，通常为二进制模式。电子文件格式类型可以取自列表，如注册的因特网媒体类型（MIME 类型）。不可重复。

## $r$ 设置

用于传输数据的设置,设置包括:

1） 数据比特数(每个字符的比特数);

2）间隔比特数（发出信号结束一个字节的比特数）；

3）奇偶校验位（使用奇偶校验技术）。这些数据元素的语法是：[奇偶校验位]-[数据比特数]-[间隔比特数]。若只给出了奇偶校验位，则省略其他元素设置以及元素之间的连字符（即：[奇偶校验位]。若给出了其他两个元素之一，则省略的元素的连字符记录在适当的位置上（即：[奇偶校验位]-[间隔比特数]或[奇偶校验位]-[数据比特数]）。奇偶校验位是O（奇数），E（偶数），S（空格），M（符号）。不可重复。

## $s 文件大小

是指储存在子字段$f文件名下文件的大小。通常用8位字节(octets)表示。当文件名重复时，本子字段可以重复，并直接置于子字段$f之后。由于256字段对应整个题名，而不对应特定的卷期，所以本信息不适合于期刊。可重复。

## $t$ 模拟终端

系统所支持的终端仿真。终端仿真通常在远程登录时使用。可重复。

## $u$ 统一资源标识

统一资源标识(URI)提供利用现有互联网协议检索的标准语句。256 字段的构成允许从其他链接的独立的 256 字段的子字段中创建一个统一资源地址（URL）。子字段 $u 可以替代那些分离的子字段或在这些内容中增补一些信息。若需要记录多个 URL 可重复 256 字段。不可重复。

## $v$ 有效检索时间

包含用本字段提供的地址访问电子资源的有效时间。可重复。

## $w$ 记录控制号

电子资源的控制号。可重复。

## $x$ 非公共附注

与 256 字段标识的电子资源地址相关的附注。附注的形式不完整或不用于公共显示。可重复。

## $y$ 检索方法

当第1指示符的值为7（用子字段$y$说明其检索方法）时，本子字段包含该检索方法。本子字段包含除在第1指示符定义的TCP/IP协议之外的其他检索方法。该字段中的数据与统一资源定位（URL）检索体系（RFC 1738）一致，（RFC 1738）是IETF统一资源标识工作组（Uniform Resource Identifiers Working Group of the IETF）的产品。国际互联网编号管理局（IANA）负责维护URL体系的注册，并定义语法和新体系的使用。不可重复。

## $z$ 公共附注

与 256 字段标识的电子资源地址相关的附注。附注的形式完整或用于公共显示。可重复。

## $2 链接文本

用于替代子字段 $u(统一资源标识) 中的 URL 的显示。当出现子字段 $2$ 时，应该用它的内容作为链接替代子字段 $u$ 中的目标文件。可重复。

## 示例 1:

256 4$\$$uhttp://purl.pt/441

示例 2:

256 1# $ uftp://path.net/pub/docs/urn2urc.ps

256 4# $ uhttp://lcweb.loc.gov/catdir/semdigdocs/seminar.html

注：重复256字段。分别记录符合文件传输协议(ftp)的统一资源标识(URI)(指示符1置值“1”)和符合超文本传输协议的URI(指示符1置值“4”)。

## 示例 3:

256 3$ alocis.loc.gov $ b140.147.254.3$ mlconline@loc.gov $ t3270$ tline mode (e.g., vt100) $ vM-F 06:00-21:30 USA EST, Sat.08:30-17:00 USA EST, Sun.13:00-17:00 USA EST

注：该电子资源利用电话拨号入网方式获取，指示符1置值“3”。包含主机域名（$a$）、IP地址（$b$）、资源提供者的邮件联系地址（$m$）、仿真终端型号（$t$）和有效的电子资源访问时间（$v$）等信息。

### 6.5 附注块(notes block)

本附注块包含以自由行文方式对在编文献或藏本作进一步描述的附注信息。包括检索限定、物理条件等方面的信息。所有附注都是文字形式，并适用于公共显示。与文献正式书目记录描述的相关信息不记录在附注块中，除非需要说明含糊不清的问题。记录编目员的附注著录在830字段（编目员一般附注）。定义的字段如下：

300 一般性附注

301 标识号附注

302 编码信息附注

371 信息服务政策附注

372 文献物理特征附注

373 藏本历史附注

375 复本与版本识别附注

CNMARC 馆藏记录中有效的 CNMARC 书目字段

310 装订及获得方式附注

316 现有藏本附注

317 出处附注

318 操作附注

345 采访信息附注

## 300 一般性附注(general notes)

本字段包含馆藏或与其相关的任何方面的附注。它可以代替任何一个附注字段，或当源格式没有提供与本格式相同的附注类型，300字段还包含那些不能分配在更为专指的附注字段的任何附注。

本字段选择使用，可重复。

指示符

指示符 1: 空(未定义)

指示符 2: 空(未定义)

子字段

子字段表

子字段标示符                           子字段内容                          注释

$ a                                         附注内容                          不可重复

## 301 标识号附注(notes pertaining to identification numbers)

本字段包含有关单册或记录中出现的任何标识号的附注。

本字段选择使用，可重复。

指示符

指示符 1: 空(未定义)

指示符 2: 空(未定义)

子字段表

子字段标示符                           子字段内容                          注释

$ a                                         附注内容                          不可重复

## 302 编码信息附注(notes pertaining to coded information)

本字段包含与1-编码信息块字段中编码数据元素有关的附注。

本字段选择使用，可重复。

指示符

指示符 1: 空(未定义)

指示符 2: 空(未定义)

子字段

子字段表

子字段标示符 子字段内容 注释

$a$ 附注内容 不可重复

示例 1:

302 ## $aAcquired in 2001 at Silva's auction

注：本例表示该文献 2001 年在 Silva 拍卖会上获取。

示例 2:

302 ## $a 捐赠文献，但支付人民币 5,000 元的奖励。

310 装订及获得方式附注(notes pertaining to binding and availability) 本字段包含与文献装订及获得方式有关的附注。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 316 现有藏本附注(notes pertaining to the copy in hand)

本字段包含有关古籍等现有藏本的附注，例如：缺叶、藏本的特征、装订、某个版本的复本数等。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 317 出处附注(provenance note)

本字段包含有关文献出处的附注，例如：藏书票、著者和/或拥有者的签名、图章印记等。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 318 操作附注(action note)

本字段记录文献保存信息和处理的附注。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 345 采访信息附注(acquisition information note)

本字段包含出版者、发行者或其他采访源的名称和地址，也可包括订购号、物理载体形式、获得方式或该文献的另一不同物理载体版本等附注。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 371 信息服务政策附注(notes on information service policy)

本字段包含检索、使用限制和复制政策的附注。

本字段选择使用，可重复。

指示符

指示符1:空(未定义)

指示符2:空(未定义)

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>使用和复制的限制条件</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>权限</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>授权</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>授权用户</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$z</td><td style='text-align: center;'>专指资料</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 使用和复制的限制条件

指法律或官方有关限制使用和复制的说明条文。不可重复。

## $b$ 权限

包含使用、复制，以及能申请实施权限的个人名称、团体名称或在机构中的职位、职务。不可重复。

## $c$ 授权

包含限定权限的授权来源。不可重复。

## $d$ 授权用户

<div style="text-align: center;"><img src="imgs/img_in_image_box_141_1515_176_1548.jpg" alt="Image" width="2%" /></div>


$a$ 子字段未规定的用户级别和特定个人。不可重复。

## $z$ 专指资料

表示一个字段限定范围的方式，该字段用于所描述该文献的一部分。不可重复。

示例 1:

371 ## $ aReproduction only for non-profit projects

注：本例表示该文献仅限于非营利性机构复制。

示例 2:

371 ## $ aReproduction forbidden $ cLei do Direito de Autor

注：本例表示该文献未经 Lei do Direito de Autor 授权禁止复制。

示例 3:

371 ## $ aRestricted reproduction $ dresearchers with author's permission

注：本例表示该文献经作者许可，研究人员可以有限制的复制。

示例 4:

371 # # $a 仅限局域网内阅读

注：本例表示该电子文献经授权许可限制使用。

## 372 文献物理特征附注(notes on physical characteristics of an item)

本字段包含有关文献的物理载体、资料形式或类型的附注。

本字段选择使用，可重复。

指示符

指示符1:空(未定义)

指示符2：空（未定义）

子字段

子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>附注内容</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>示例 1：</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>372 # # $ aText, Braille</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>注：本例表示该文献正文是盲文。</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>示例 2：</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>372 # # $ a 电子资源</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

## 373 藏本历史附注(notes pertaining to copy history)

本字段包含有关文献从出现到登记入藏，包括流通管理和收集期间内的所有权和保存历史的附注。

本字段选择使用，可重复。

指示符

指示符 1: 空(未定义)

指示符 2: 空(未定义)

子字段

子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>历史</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>年代</td><td style='text-align: center;'>不可重复</td></tr></table>

示例 1:

373 ## $ aOriginally collected by Duarte de Sousa

注：本例表示该文献由 Duarte de Sousa 最初收藏。

示例 2:

373 # # $ aOriginally collected by Cordeiro Pereira and bequeathed to Biblioteca Nacional in 2000

注：本例表示该文献 Cordeiro Pereira 是最初的收藏者，2000 年他遗赠给 Biblioteca Nacional。

示例 3:

373 # # $ a2005 年吕正操捐赠

## 375 复本与版本识别附注(notes pertaining to copy and version identification)

当文献存在或可能存在多个复本或版本时，本字段包含用于区分所保存的复本或版本的信息。

本字段选择使用，可重复。

指示符

指示符1:空(未定义)

指示符2:空(未定义)

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>识别标记</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ b</td><td style='text-align: center;'>复本标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ c</td><td style='text-align: center;'>版本标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ d</td><td style='text-align: center;'>存在形式</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ e</td><td style='text-align: center;'>复本数</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a 识别标记。

不可重复。

$b$ 复本标识。

用于区分在编文献不同复本的信息。不可重复。

$c$ 版本标识

标识版本的信息。不可重复。

$d$ 存在形式

在编文献使用、观看及收听的形式。不可重复。

$e复本数。

不可重复。

示例 1:

375 ## $ aManuscripts annotations

注：本例表示该文献是原稿注释。

示例 2:

375 ## $ bAuthor's autograph

注：本例表示该文献是作者手稿。

示例 3:

375 # # $ cASCⅡ文本

### 6.6 馆藏范围块(extent of holdings block)

本馆藏范围块定义了记录文献范围的数据元素信息字段，这些文献由标识于252字段中的机构所保存。数据元素分为四组字段，分别描述标识说明及样式、编号与年代、文字性馆藏信息和单册信息。尽管这些字段主要应用于连续性和集成性资源馆藏方面，但它们也可应用于头标区定义的四种文献类型，即单部分文献、多部分文献、连续性文献和集成性资源。每组字段中分别定义了三种类别的字段，即基本书目单元、补充资料和索引。定义字段如下：

500 标识说明及样式——基本书目单元

502 标识说明及样式——辅助书目单元：索引

## 500 标识说明及样式——基本书目单元(captions and pattern-basic bibliographic unit)

本字段包含 510 字段（编号与年代——基本书目单元）中记录的编号与年代的标识说明及样式信息。

本字段选择使用，可重复。

## 指示符

指示符1：压缩和展开

# 无信息提供

0 不能压缩或展开

1 可以压缩但不能展开

2 可以压缩或展开

指示符2：标识说明评价

无信息提供

0 未核实标识说明: 可能不出现所有级别

1 未核实标识说明: 出现所有级别

2 已核实标识说明: 出现所有级别

3 已核实标识说明: 可能不出现所有级别

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>编号第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>编号第二级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>编号第三级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>交替编号体系,编号第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$e</td><td style='text-align: center;'>交替编号体系,编号第二级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$f</td><td style='text-align: center;'>年代第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$g</td><td style='text-align: center;'>年代第二级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$h</td><td style='text-align: center;'>年代第三级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$i</td><td style='text-align: center;'>交替年代体系,年代第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$j</td><td style='text-align: center;'>单元名称</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$k</td><td style='text-align: center;'>单元范围</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$l</td><td style='text-align: center;'>特殊范围附注</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$6</td><td style='text-align: center;'>内部字段间连接数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 编号第一级

包含与编号相关的标识说明及样式。有则必备。不可重复。

$b$ 编号第二级

不可重复。

$c$ 编号第三级

不可重复

$d$ 交替编号体系，编号第一级

有则必备。不可重复。

$e 交替编号体系,编号第二级

不可重复。

$f$ 年代第一级

包含与年代相关的标识说明及样式。有则必备。不可重复。

$g$ 年代第二级

不可重复。

$h$ 年代第三级

不可重复。

$i 交替年代体系,年代第一级

有则必备。不可重复。

## $i$ 单元名称

用于记录一个基本或辅助书目单元的馆藏范围，如配套资料的一部分、附件资料、或是需要识别的特殊单元的补充资料。本子字段主要用于可能仅有一个标识名称的非连续单元。不可重复。

## $k$ 单元范围

用于记录缺少连续标识的文献，主要用于非连续单元。连续单元通常带有连续标识（或为编号或为年代）。被报道的范围作为文献所有部分的总数量，其后紧跟表示资料特定类别的术语。对于含有大量单册的单元可给出总量的估数。若该单元是单一册件，并已给出了单元名称，则不需要再给出范围。不可重复。

## $1 特殊范围附注

本子字段由用于阐明或扩大馆藏数据元素范围的信息组成。它可以出现在任意子字段之后，可与其紧跟的子字段有关，也可与整个字段有关。不可重复。

## $6 内部字段间连接数据

子字段 $6$ 用于连接馆藏位置和索取号字段（252）、编号与年代字段（510）、文字性馆藏字段（520）和单册信息字段（530）。有则必备，不可重复。

## 示例 1:

500 23 $ 6z01 $ av. $ bno. $ f(year)

510 11 $ 6z01 $ a1-2 $ f1998-1999

510 11 $ 6z01 $ a3 $ b1-4 $ f2000

注：子字段$a、$b和$f$是在510字段中描述的连续编号数据级别的标识说明。数值2（第1指示符）表明在510-512字段中的信息可以通过计算机算法压缩或展开，数值3（第2指示符）表明标识说明已核实，但可能不出现所有级别。依据GB/T24424—2009显示为：v.1-2（1998-1999）and v.3：no.1-4（2000）。

## 示例 2:

500 22 $ 6z01 $ a(year)

510 # # $ 6z01 $ a2000

注：无编号文献。数值2（第1指示符）表明在510-512字段中的信息可以通过计算机算法压缩或展开，数值2（第2指示符）表明标识说明已核实，并且在书目单元中出现所有级别。依据GB/T24424—2009显示为：2000。

## 示例 3:

500 03 $ 6z01 $ afasc.

510 11 $ 6z01 $ a1-30

注：数值 0（第 1 指示符）表明在 510-512 字段中的信息不能通过计算机算法压缩或展开。依据 GB/T 24424—2009 显示为：fasc.1-30。

## 示例 4:

500 22 $ 6z01 $ av. $ bno. $ f(year) $ g(month)

510 10 $ 6z01 $ a1 $ b1 $ f1993 $ gJan./Feb.

注：数值2（第1指示符）表明在510-512字段中的信息可以通过计算机算法压缩或展开，数值2（第2指示符）表明标识说明信息已核实，并且在书目单元中出现所有级别。依据GB/T24424—2009显示为：v.1：no.1（Jan./Feb.1993）。

## 示例 5:

500 10 $ 6z01 $ av. $ f(year)

510 11 $ 6z01 $ a1-12 $ f2002

注：数值1（第1指示符）表明在510-512字段中的信息可以通过计算机算法压缩但不能展开，数值0（第2指示符）表明标识说明未核实，并且在书目单元中可能不出现所有级别。依据GB/T24424—2009显示为：v.1-12（2002）。

## 示例 6:

500 23 $ 6z01 $ av. $ bno. $ dv. $ eno. $ f(year) $ g(month)

510 10 $ 6z01 $ a6 $ b2 $ d13 $ e3 $ f1969 $ gMar.

注：带有交替标识系统的编号。数值2（第1指示符）表明在510-512字段中的信息可以通过计算机算法压缩或展开，数值3（第2指示符）表明标识说明已核实，但可能不出现所有级别。依据GB/T24424—2009显示为：v.6：no.2=v.13:no.3(Mar.1969)。

## 501 标识说明及样式——辅助书目单元: 补充资料 (captions and pattern-secondary bibliographic unit: supplementary materials)

本字段包含在 511 字段(编号与年代——辅助书目单元:补充资料)中记录的编号与年代数据的标识说明及样式信息。

本字段选择使用，可重复。

指示符

同 500 字段。

## 子字段

同 500 字段。

## 502 标识说明及样式——辅助书目单元: 索引 (captions and pattern-secondary bibliographic unit: indexes)

本字段包含在 512 字段(编号与年代——辅助书目单元:索引)中记录的编号与年代数据的标识说明及样式信息。

本字段选择使用，可重复。

指示符

同 500 字段。

子字段

同 500 字段。

## 510 编号与年代——基本书目单元(enumeration and chronology-basic bibliographic unit)

本字段包含编号与年代，其标识说明及样式记录在500字段（标识说明及样式——基本书目单元）。本字段有则必备，可重复。

## 指示符

指示符1:馆藏说明

# 无信息提供

0 概要级

概要馆藏仅记录年代数据的最高级“年”。

1 详细级

第一级以下的级别仅用于记录有详细编号的文献；若无详细编号，则用于明确记录馆藏。

指示符2：压缩说明

# 无信息提供

0 不压缩

每个字段与一个卷期相关。

1 压缩

压缩数据可以产生可读说明。

2 未压缩

不能产生合理的显示。附注显示是必要的。

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>编号第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>编号第二级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>编号第三级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>交替编号体系，编号第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$e</td><td style='text-align: center;'>交替编号体系，编号第二级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$f</td><td style='text-align: center;'>年代第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$g</td><td style='text-align: center;'>年代第二级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$h</td><td style='text-align: center;'>年代第三级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$i</td><td style='text-align: center;'>交替年代体系，年代第一级</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$w</td><td style='text-align: center;'>缺藏标识</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$x</td><td style='text-align: center;'>非公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$z</td><td style='text-align: center;'>公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$6</td><td style='text-align: center;'>内部字段间连接数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

## $a$ 编号第一级

包含一个编号的连续标识。有则必备，不可重复。

$b$ 编号第二级不可重复。

$c$ 编号第三级

不可重复。

$d 交替编号体系，编号第一级有则必备，不可重复。

$e 交替编号体系，编号第二级不可重复。

$f$ 年代第一级

包含年代的连续标识。当仅有年代标识时，年代指明馆藏。有则必备，不可重复。

$g$ 年代第二级

不可重复。

$h$ 年代第三级不可重复。

$i 交替年代体系，年代第一级有则必备，不可重复。

$w$ 缺藏标识

不可重复。

a=缺藏中断

b=非缺藏中断

$x$ 非公共附注

可重复。

$z$ 公共附注

$6 内部字段间连接数据

子字段 $6$ 用于连接馆藏位置和索取号字段（252）、标识说明及样式字段（500）、文字性馆藏字段（520）和单册信息字段（530）。有则必备，不可重复。

## 示例 1:

500 23 $ 6z01 $ av.(year)

510 11 $ 6z01 $ a1(1950)-10(1959)

注：编号与年代记录在一起。依据 GB/T 24424—2009 显示为：v.1（1950）-v.10（1959）。

示例 2:

500 23 $ 6z01 $ av. $ f(year)

510 11 $ 6z01 $ a1-5 $ f1970-1975

注：依据 GB/T 24424—2009 显示为：v.1-5（1970-1975）。

示例 3:

500 23 $ 6z01 $ av. $ f(year)

510 11 $ 6z01 $ a1-2 $ f1950-1951

510 11 $ 6z01 $ a4-5 $ f1953-1954

注：缺藏一年的连续出版物。依据 GB/T 24424—2009 显示为：v.1-2（1950-1951），v.4-5（1953-1954）。

示例 4:

500 23 $ 6z01 $ ano.

510 12 $ 6z01 $ a569,590,592,595 $ wa

注：依据 GB/T 24424—2009 显示为：缺藏中断 no.569,590,592,595。

示例 5:

500 23 $ 6z01 $ av. $ bno. $ f(year) $ g(month)

510 10 $ 6z01 $ a1 $ b1 $ f2002 $ gJan.

510 10 $ 6z01 $ a1 $ b2 $ f2002 $ gMar.

510 10 $ 6z01 $ a1 $ b3 $ f2002 $ gJun.

注：依据 GB/T 24424—2009 显示为：v.1:no.1(Jan.2002)，v.1:no.2(Mar.2002)，v.1:no.3(Jun.2002)。

示例 6:

500 23 $ 6z01 $ a(year)

510 10 $ 6z01 $ a1996

510 10 $6z01 $ a1999
510 10 $6z01 $ a2000
510 10 $6z01 $ a2001
520 01 $6z01 $ a1996-2001 $ zsome missing
注：依据 GB/T 24424—2009 显示为：1996, 1999, 2000, 2001 或 1996-2001（部分丢失）。

## 511 编号和年代——辅助书目单元：补充资料（enumeration and chronology-secondary bibliographic unit: supplementary materials）

本字段包含编号与年代，其标识说明及样式记录在501字段（标识说明及样式——辅助书目单元：补充资料）。

本字段选择使用，可重复。

## 指示符

同 510 字段。

## 子字段

同 510 字段。

## 512 编号与年代——辅助书目单元：索引（enumeration and chronology-secondary bibliographic unit: indexes）

本字段包含编号与年代，其标识说明及样式记录在502字段（标识说明及样式——辅助书目单元：索引）。

本字段选择使用，可重复。

## 指示符

同 510 字段。

## 子字段

同 510 字段。

## 520 文字性馆藏——基本书目单元(textual holdings-basic bibliographic unit)

本字段用于记录下列文献馆藏的文字性描述：a) 单一部分文献；b) 代替或补充记录多部分文献和连续出版物标识说明及样式和编号与年代以外的信息。

本字段选择使用，可重复。

## 指示符

指示符1:字段编码等级

# 无信息提供

0 概要级

概要馆藏仅记录年代数据的最高级“年”。

1 详细级

包含详细的编号与年代信息，即仅用于记录编号和年代第一级及所有后续级别；无编号时，则是为了更清晰的描述馆藏。

## 指示符2：符号类型

该指示符的值表示在$\$a$子字段中的文字性馆藏描述是否依据标准进行。

# 无信息提供

0 非标准

1 ISO 10324

2 ANSI Z39.42

9 GB/T 24424—2009

示例 2:

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>文字性馆藏</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$x</td><td style='text-align: center;'>非公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$z</td><td style='text-align: center;'>公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$6</td><td style='text-align: center;'>内部字段间连接数据</td><td style='text-align: center;'>不可重复</td></tr></table>

## 2 子字段说明

$a$ 文字性馆藏

有则必备，不可重复。

$x$ 非公共附注

可重复。

$ z 公共附注

可重复。

$6 内部字段间连接数据

子字段 $6$ 用于馆藏位置和索取号字段（252）、标识说明及样式字段（500）和编号与年代字段（510）与单册信息字段（530）之间的连接。有则必备，不可重复。

示例 1:

520 11 $ 6z01 $ afasc.30-40 $ zsome missing

520 11 $ 6z01 $ av.1-10 $ zv.8 not published

## 521 文字性馆藏——辅助书目单元: 补充资料 (textual holdings-secondary bibliographic unit: supplementary materials)

本字段包含单一部分文献馆藏的文字性描述，也可用于代替或补充记录多部分文献和连续出版物标识说明及样式和编号与年代以外的信息。

本字段选择使用，可重复。

指示符

同 520 字段。

## 子字段

同 520 字段。

<div style="text-align: center;"><img src="imgs/img_in_image_box_576_1088_615_1125.jpg" alt="Image" width="3%" /></div>


## 522 文字性馆藏——辅助书目单元：索引（textual holdings-secondary bibliographic unit: indexes）

本字段包含单一部分文献馆藏的文字性描述，也可用于代替或补充记录多部分文献和连续出版物标识说明及样式和编号与年代以外的信息。

本字段选择使用，可重复。

指示符

同 520 字段。

子字段

同 520 字段。

## 530 单册信息——基本书目单元(item information-basic bibliographic unit)

本字段包含馆藏记录中有关文献册件的信息，这些数据元素可以应用于采访或流通。

本字段选择使用，可重复。

指示符

指示符1:空(未定义)

指示符2:空(未定义)

## 子字段


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>内部文献号</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>无效或删除的内部文献号</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>费用</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>获得日期</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$e</td><td style='text-align: center;'>采访来源</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$h</td><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$j</td><td style='text-align: center;'>单册状态</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$l</td><td style='text-align: center;'>临时馆藏地</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$p</td><td style='text-align: center;'>单册标识</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$r</td><td style='text-align: center;'>无效或删除的文献标识</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$t</td><td style='text-align: center;'>复本号</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$x</td><td style='text-align: center;'>非公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$z</td><td style='text-align: center;'>公共附注</td><td style='text-align: center;'>可重复</td></tr><tr><td style='text-align: center;'>$6</td><td style='text-align: center;'>内部字段间连接数据</td><td style='text-align: center;'>不可重复</td></tr><tr><td colspan="3">2 子字段说明</td></tr><tr><td style='text-align: center;'>$a</td><td style='text-align: center;'>内部文献号</td><td style='text-align: center;'></td></tr><tr><td colspan="3">不可重复。</td></tr><tr><td style='text-align: center;'>$b</td><td style='text-align: center;'>无效或删除的内部文献号</td><td style='text-align: center;'></td></tr><tr><td colspan="3">不可重复。</td></tr><tr><td style='text-align: center;'>$c</td><td style='text-align: center;'>费用</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$d</td><td style='text-align: center;'>获得日期</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$e</td><td style='text-align: center;'>采访来源</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$h</td><td style='text-align: center;'>使用限制</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$j</td><td style='text-align: center;'>单册状态</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$l</td><td style='text-align: center;'>临时馆藏地</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$p</td><td style='text-align: center;'>单册标识</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$r</td><td style='text-align: center;'>无效或删除的文献标识</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr><tr><td style='text-align: center;'>$t</td><td style='text-align: center;'>复本号</td><td style='text-align: center;'></td></tr><tr><td colspan="3">不可重复。</td></tr><tr><td style='text-align: center;'>$x</td><td style='text-align: center;'>非公共附注</td><td style='text-align: center;'></td></tr><tr><td colspan="3">可重复。</td></tr></table>

## $z$ 公共附注

可重复。

## $6 内部字段间连接数据

子字段 $6$ 用于馆藏位置和索取号字段（252）、标识说明及样式字段（500）和编号与年代字段（510）与文字性馆藏字段（520）之间的连接。有则必备，不可重复。

示例 1:

530 # # $ 6z01 $ a214537 $ c20,50€ $ d20041003 $ hUse only in the Reading Room

示例 2:

530 ## $ 6z01 $ a\langle internal item number\rangle $ lExhibition room

示例 3:

530 ##  6z01  a $ \langle $ internal item number $ \rangle $   jLost

## 531 单册信息——辅助书目单元: 补充资料(item information-secondary bibliographic unit: supplementary materials)

本字段包含馆藏记录中有关文献册件的信息，这些数据元素可以用于采访或流通。

本字段选择使用，可重复。

指示符

同 530 字段。

子字段

同 530 字段。

## 532 单册信息——辅助书目单元：索引（item information-secondary bibliographic unit: indexes）

本字段包含馆藏记录中有关文献册件的信息，这些数据元素可应用于采访或流通。

本字段选择使用，可重复。

指示符

同 530 字段。

子字段

同 530 字段。

### 6.7 责任块(responsibility block)

本责任块包含对保存历史和所有权负有某种责任的个人名称、团体名称和家族名称。

CNMARC 馆藏记录中有效的 CNMARC 书目字段：

702 个人名称——次要责任(与藏本相关)

712 团体名称——次要责任(与藏本相关)

722 家族名称——次要责任(与藏本相关)

## 702 个人名称——次要责任（与藏本相关）[personal name-secondary responsibility(related to copy)]

本字段包含以检索点形式出现的对文献馆藏负有次要责任的个人名称。该字段可以在没有主要责任或等同责任字段的情况下出现。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 712 团体名称——次要责任（与藏本相关）[corporate body name-secondary responsibility（related to copy）]

本字段包含以检索点形式出现的对文献馆藏负有次要责任的团体名称。

根据书目机构的用法，本字段可用于CNMARC书目记录和CNMARC馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

## 722 家族名称——次要责任（与藏本相关）[family name-secondary responsibility(related to copy)]

本字段包含以检索点形式出现的对文献馆藏负有次要责任的家族名称。

根据书目机构的用法，本字段可用于 CNMARC 书目记录和 CNMARC 馆藏记录。

本字段在本标准中的用法详见 GB/T 33286—2016 中此字段的用法。

### 6.8 源信息块(source information block)

本源信息块包含国际上一致约定的不适合在之前功能块（0-7 功能块）处理的字段。定义字段如下：

801 记录来源

830 编目员一般附注

## 801 记录来源(originating source)

本字段包含记录原始来源的标识，包括下列机构之一：创建数据的机构、将数据转换成机读形式的机构、修改原始记录或数据的机构，以及发行当前记录的机构。

本字段必备，可重复。

指示符

指示符1:空(未定义)

指示符2：功能指示符

0 原始编目机构

1 转录机构

2 修改机构

3 发行机构

## 子字段

## 1 子字段表


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>子字段标识符</td><td style='text-align: center;'>子字段内容</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>$ a</td><td style='text-align: center;'>国家</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ b</td><td style='text-align: center;'>机构</td><td style='text-align: center;'>不可重复</td></tr><tr><td style='text-align: center;'>$ c</td><td style='text-align: center;'>处理日期</td><td style='text-align: center;'>可重复</td></tr></table>

## 2 子字段说明

$ a$ 国家

用两位字符代码标识发行机构所属的国家。国家代码采用 GB/T 2659 的两位大写字母代码。不可重复。

$b$ 机构

可采用机构名称的英文缩写形式，也可以采用机构的中文全称或国家规定的代码。不可重复。

## $c$ 处理日期

本子字段用于记录修改或发行的日期，依据 GB/T 7408 标准形式著录，即 YYYYMMDD。不可重复。

## 830 编目员一般附注(general cataloguer note)

本字段包含记录演变过程、历史以及其他方面的信息。

本字段选择使用。可重复。

## 指示符

指示符1:空(未定义)

指示符2：空（未定义）

44

## 2 子字段说明

## $a$ 附注内容

涉及该记录演变过程、历史以及其他方面的信息。不可重复。示例：

830 # # $a 本藏本正在借展，待展览结束藏本归还后，记录可能要作修改。

附录 A

(资料性附录)

完整样例

### A.1 单一部分文献馆藏记录样例

示例 1：单一馆藏地单一复本，1 级馆藏说明（头标 /6=a 头标 /8=a 头标 /17=1 头标 /18=0）记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ###a a a #2 2 #### 1 0 #4 5 0 #

001 0021764

004 (PTBN)0007291

005 20030320161200.0

100 ## $ a20020104pory0103 ## ## ba0

252 11 $ pPT $ aBN $ bFundo Geral $ jL. 574397 V. $ mEFG0914567028

702 #1 $ aPereira $ bCordeiro $ 4390

801 #0 $ aPT $ bBN

## 示例 2：单一馆藏地单一复本，2 级馆藏说明（头标 /6=a 头标 /8=a 头标 /17=2 头标 /18=0）记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ##### a a a #2 2 ##### 2 0 #4 5 0 #

001 00000001

004 (NLC) 003438101

005 20070608153350.0

100 # # $ a20070605chiy50 # # # # # # ea0

170 ## $ aaa ## ## ## ## ##

171 ## $ aac ## x001

172  $ \# \# $   abdc

252 01 $ pCN $ aNLC $ bSKBC $ cJ13 $ j2007/Z121.6/1 $ m3160179028 $ t1 $ 2CLC

371 #\#a 该复本作为国家图书馆的保存本，按有关保存本服务政策提供服务。

712 02 $a 中国国家图书馆 $4 收藏

801 #0 $ aCN $ bNLC $ c20070608

示例 3：单一馆藏地单一复本，2 级馆藏说明（头标 /6=a 头标 /8=a 头标 /17=2 头标 /18=0）记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 #####a a a #2 2 #####2 0 #4 5 0 #

001 0021764

004 (PTBN)0007291

005 20030320161200.0

070 1$ a4523

100 ## $ a20020104pory0103## ## ba0

170 ## $ aaj ## ## ## ## ##

171 ## $ afb ## x001

172 ## $ aaaa

252 11 $ pPT $ aBN $ bFundo Geral$ jL. 574397 V. $ mEFG0914567028

373 ## $ aOriginal collected by Cordeiro Pereira and bequested to Biblioteca Nacional in 2000

702 #1 $ aPereira $ bCordeiro $ 4390

801 #0 $ aPT $ bBN

## 示例 4：单一馆藏地的两个复本，建两个单独 2 级馆藏说明记录，一个复本提供检索，另一个复本作为保存记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 #### a a b # 2 2 #### 2 0 # 4 5 0 #

001 0967364

004 (PTBN)06010557

005 20030320161200.0

070 1 ## a128351

101 ## $ a20020104pory0103 ## ## ba0

170 ## $ aad ## ## ## ##

171 ## $ afb ## ## x001

172 ## $ aaac

252 11 $ pPT $ aBN $ bFundo Geral $ jL. 53113V. $ mEFG0000037794

371 ## $ aRestricted reproduction: only 1/3 $ cAuthor's Code

801 #0 $ aPT $ bBN

## 记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 #### 2 a b 2 2 #### 2 1 # 4 5 0 #

001 0967365

004 (PTBN)06010557

005 20030320161200.0

070 1 ## a128351

100 ## $ a20020104pory0103 ## ## ba0

170 ## $ aad ## ## ## ##

171 ## $ aad ## ## x001

172 ## $ acba

252 11 $ 6z01 $ pPT $ aBN $ bFundo Geral $ jL. 53113 V. $ mmq00009673652

530 ## $ 6z01 $ a128351 $ pmq00009673652 $ hPreservation copy

801 #0 $ aPT $ bBN

## 示例 5：单一馆藏地的两个复本，按馆藏地建一条 2 级馆藏说明记录

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 #####a a b #2 2 #####2 0 #4 5 0 #

001 00000002

004 (NLC) 003458901

005 20070608163350.0

100 ## $ a20070605chiy50 ## ## ## # ea0

170 ## $ aaa ## ## ## ##

171 ## $ aab ## x001

172  $ \# \# \ aad a $ 

252 01 $ pCN $ aNLC $ bZWJC $ cJ14S $ j2007/Z121.6/1 $ m3060502949 $ t2 $ 2CLC

252 01 $ pCN $ aNLC $ bZWJC $ cJ14S $ j2007/Z121.6/1 $ m3060502980 $ t3 $ 2CLC

371 #$a该2个复本均作为国家图书馆的基藏本，按有关基藏本服务政策提供服务。

712 02 $ a 中国国家图书馆 $ 4 收藏

801 #0 $ aCN $ bNLC $ c20070608

## 示例 6: 多个子馆藏地所藏复本整合为一条 2 级馆藏说明记录 (头标 /6 = a 头标 /8 = c 头标 /18 = 0)

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ####a a c #2 2 ####2 0 #4 5 0 #

001 00000003

004 (NLC) 003458901

005 20070608133350.0

100 ## $ a20070605chiy50 ## ## ## ## ea0

170 ## $ aaa ## ## ## ## ##

171 ## $ aab ## x003

172  $ \# \# \ aad a $ 

252 01 $ pCN $ aNLC $ bSKBC $ cJ13 $ j2007/Z121.6/11 $ m3160179028 $ t1 $ 2CLC

252 01 $ pCN $ aNLC $ bZWJC $ cJ14S $ j2007/Z121.6/26 $ m3060502949 $ t2 $ 2CLC

252 01 $ pCN $ aNLC $ bZWJC $ cJ14S $ j2007/Z121.6/48 $ m3060502980 $ t3 $ 2CLC

371  $ \#\# $  a $  复本 1 作为国家图书馆的保存本，复本 2、3 作为国家图书馆的基藏本，分别按有关保存本、基藏本服务政策提供服务。

712 02 $ a 中国国家图书馆 $ 4 收藏

801 #0 $ aCN $ bNLC $ c20070608

### A.2 多部分文献馆藏记录样例

示例 7：多部分文献，单一馆藏地单一复本，2 级馆藏说明记录

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23
对应值 ####b a a #2 2 ####2 0 #4 5 0 #001 0147252

004 (PTBN) 0009528

005 20030320161300.0

070 1 ## a7827 $b1 v.

100 ## $ a20020104pory0103 ## ## ba0

170 ## $ aaa ####b

171 ## $ afb ## a001

172 ## $ aaaa

252 11 $ pPT $ aBN $ bFundo Geral $ jC.G.781397 V. $ mEFG7810034817
801 #0 $ aPT $ bBN

示例 8：多部分文献，单一馆藏地单一复本的 4 级馆藏说明记录（头标 /6=b 头标 /8=a 头标 /18=1）记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ####b a b #2 2 ####4 1 #4 5 0 #

001 00000005

004 (NLC) 003458901

005 20070608163350.0

100 ## $ a20070605 chiy50 ## ## ## ea0

170 ## $ aaa ## ## ## ## ##

171 ## $ aab ## ## x002

172 ## $ aada

252 01 $6z01 $pCN $6z01 $aNLC $bZWJC $cJ14S $j2007/F121.6/123 $m3060502949 $t2 $2CLC

252 01 $6z02 $pCN $6z02 $aNLC $bZWJC $cJ14S $j2007/F121.6/137 $m3060502980 $t3 $2CLC

371 ## $a 该 2 个复本均作为国家图书馆的基藏本，按有关基藏本服务政策提供服务。

500 23 $6z01 $av.

500 23 $6z02 $av.

510 10 $6z01001 $a1

510 10 $6z01002 $a2

510 10 $6z02001 $a1

510 10 $6z02002 $a2

530 ## $6z01001 $p3003056214 $h 长期保存 $j 在架 $t2

530 ## $6z01002 $p3003056215 $h 长期保存 $j 在架 $t2

530 ## $6z02001 $p3003056216 $h 长期保存 $j 在架 $t3

530 ## $6z02002 $p3003056217 $h 长期保存 $j 在架 $t3

712 02 $a 中国国家图书馆 $4 收藏

801 #0 $aCN $bNLC $c20070608

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 #### 6 b a a # 2 2 #### 4 1 # 4 5 0 #

001 00000004

004 (NLC) 003489603

005 20070609093350.0

100 ## $ a20070606chiy50######ea0

170 ## $ aaa######

171 ## $ aab###x001

172 ## $ aada

252 01 $6z01$ pCN$ aNLC$ bSKBC$ cJ13$ j2007/Z121.6/1$ t1$ 2CLC

371 ## $ a 该复本作为国家图书馆的保存本，按有关保存本服务政策提供服务。

500 23$6z01$ av.

510 10$6z01001$ a1

510 10$6z01002$ a2

530 ## $6z01001$ p3003056785$ h长期保存$j在架$ t1

530 ## $6z01002$ p3003056786$ h长期保存$j在架$ t1

712 02$a中国国家图书馆$4收藏

801 #0$ aCN$ bNLC$ c20070609

## 示例 9：多部分文献，单一馆藏地多复本的 4 级馆藏说明记录（头标 /6=b 头标 /8=b 头标 /18=1）记录头标

示例 10：多个子馆藏地所藏复本整合为一条 4 级馆藏说明记录（头标/6=b 头标/8=c 头标/18=1）

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23
对应值 ####b a c #2 2 ####4 1 #4 5 0 #
001 00000006
004 (NLC) 003458901
005 20070608133350.0
100 ## $ a20070605chiy50 ####ea0
170 ## $ aaa ####
171 ## $ aab ####x003
172 ## $ aada
252 01 $6z01$pCN $aNLC$bSKBC$cJ13$j2007/G121.6/5$m3160179028$t1$2CLC
252 01 $6z02$pCN $aNLC$bZWJC$cJ14S$j2007/G121.6/41$m3060502949$t2$2CLC
252 01 $6z03$pCN $aNLC$bZWJC$cJ14S$j2007/G121.6/56$m3060502980$t3$2CLC
371 ## $a 复本1作为国家图书馆的保存本，复本2、3作为国家图书馆的基藏本，分别按有关保存本、基藏本服
政策提供服务。
500 23 $6z01$av.
500 23 $6z02$av.
500 23 $6z03$av.
510 10 $6z01001$a1
510 10 $6z01002$a2
510 10 $6z02001$a1
510 10 $6z02002$a2
510 10 $6z03001$a1
510 10 $6z03002$a2
530 ## $6z01001$p3003078563$h长期保存$j在架$t1
530 ## $6z01002$p3003078564$h长期保存$j在架$t1
530 ## $6z02001$p3003078565$h长期保存$j在架$t2
530 ## $6z02002$p3003078567$h长期保存$j在架$t2
530 ## $6z03001$p3003078568$h长期保存$j在架$t3
530 ## $6z03002$p3003078569$h长期保存$j在架$t3
712 02$a中国国家图书馆$4收藏
801 #0$aCN$bNLC$c20070608

### A.3 连续性文献馆藏记录样例

示例 11：连续出版物，单一馆藏地单一复本 4 级馆藏说明记录

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23
对应值 #### 6 a a # 2 2 #### 4 0 # 4 5 0 #
001 0312187

004 (PTBN)0017631

005 20030320161400.0

070 1 ## $ a7827

100 ## $ a20000804 pory0103 ## ## ba0

170 ## $ acd ## ## ## ##

171 ## $ afb ## a001

172 ## $ aaba

252 11 $ 6z01 $ pPT $ aBN $ bSérie Geral $ jP.P.17611 V.

500 23 $ 6z01 $ aV. $ f(Month year)

510 11 $ 6z01 $ a1-11 $ fJan/Maio 1985-Jul./Dez.1995

510 11 $ 6z01 $ a12 $ fJan.1999-Jun.1999

520 11 $ 6z01 $ aV.10, no.2 (Jul./Dez.1994) $ zmissing

801 #0 $ aPT $ bBN

## 示例 12：连续出版物，单一馆藏地单一复本的 4 级馆藏说明记录(头标/6=c 头标/8=a 头标/18=1)

## 记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ###### c a a #2 2 ###### 4 1 #4 5 0 #

001 00000007

004 (NLC)112001004311

005 20070429171350.0

100 # # $ a20070428chiy50 # # # # # # ea0

170 ## $ aca ## ## ## ## ##

171 ## $ aac ## ## 001

172  $ \# \# \ aadc $ 

252 01 $ 6z01 $ pCN $ aNLC $ bSKBC $ cJ-1N $ jQ/C913/052 $ t1 $ 2CLC

500 23 $ 6z01 $ av. $ bno. $ f(year)

510 11 $ 6z01001 $ a2001 $ b1-12 $ f2001

510 11 $ 6z01002 $ a2002 $ b1-6 $ f2002

530 # # $ 6z01001 $ p3785692145 $ h 长期保存 $ j 在架 $ t1

530 # $ 6z01002 $ p3785692146 $ h 长期保存 $ j 在架 $ t1

712 02 $ a 中国国家图书馆 $ 4 收藏

801 #0 $ aCN $ bNLC $ c20070430

## 示例 13：连续出版物，单一馆藏地多复本的 3 级馆藏说明记录（头标/6=c 头标/8=b 头标/18=1）

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 #####c a b #2 2 #####3 1 #4 5 0 #

001 0000008

004 (NLC)112001004311

005 20070429131350.0

100 # # $ a20070428chiy50 # # # # # # ea0

170 # # $ acd # # # # # # # #

171 ## $ adba2c#002(限制保存-阅览室期刊只保存2年)

172 ## $ aaaa

252 01 $ 6z01 $ pCN $ aNLC $ bZSQK $ jQ/C913/052 $ t1-2 $ 2CLC

500 23 $ 6z01 $ ayear, $ bno. $ f(year)

510 11 $ 6z01001 $ a2003 $ b1-12 $ f2003

510 11 $ 6z01002 $ a2003 $ b1-12 $ f2003

510 11 $ 6z01003 $ a2004 $ b1-6 $ f2004

510 11 $ 6z01004 $ a2004 $ b1-6 $ f2004

530 # # $ 6z01001 $ p3894562583 $ h 可借阅 $ j 在架 $ t1

530 # # $ 6z01002 $ p3894562584 $ h 可借阅 $ j 在架 $ t2

530 # # $ 6z01003 $ p3894562585 $ h 可借阅 $ j 在架 $ t1

530 # # $ 6z01004 $ p3894562586 $ h 可借阅 $ j 在架 $ t2

712 02 $ a 中国国家图书馆 $ 4 收藏

801 #0 $ aCN $ bNLC $ c20070430

#### 示例 14：馆藏期刊保存本合订册 2003, no.1-2004, no.6, 3 级馆藏说明记录

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ######c a b #2 2 ######3 1 #4 5 0 #

001 00000100

004 (NLC)112011005313

005 20150610131350.0

100 # # $ a20150428chiy50 # # # # # # ea0

170 ## $ aca ## ## ## ##

171 ## $ aad ## # a001

172  $ \# \# \ acbb $ 

252 01 $ 6z01 $ pCN $ aNLC $ bSKBC $ jQ/C913/052 $ t1 $ 2CLC

500 23 $ 6z01 $ a(year)

510 11 $ 6z01 $ a2003-2004

530 # $ 6z01 $ p3894562583 $ h 可借阅 $ j 在架 $ t1

## 示例 15：多个子馆藏地所藏复本整合为一个4级馆藏说明记录(头标/6=c 头标/8=c 头标/18=1)

记录头标

字符位 0-4 5 6 7 8 9 10 11 12-16 17 18 19 20 21 22 23

对应值 ######c a c #2 2 ###### 4 1 #4 5 0 #

001 00000009

004 (NLC)112001004311

005 20070429171350.0

100 # # $ a20070428chiy50 # # # # # # ea0

170 ## $ aca ## ## ## ## ##

171 ## $ aac ## x004(无限制保存)

172  $ \# \# \ abcc $ 

252 01 $ 6z01 $ pCN $ aNLC $ bSKBC $ cJ-1N $ jQ/C913/052 $ t1 $ 2CLC

252 01 $ 6z02 $ pCN $ aNLC $ bQKJC $ cJ06N $ jQ/C913/052 $ t2 $ 2CLC

252 01 $ 6z03 $ pCN $ aNLC $ bZSQK $ jQ/C913/052 $ t3-4 $ 2CLC

500 23 $ 6z01 $ av. $ bno. $ f(year)

500 23 $ 6z02 $ av. $ bno. $ f(year)

500 23 $ 6z03 $ av. $ bno. $ f(year)

510 11 $ 6z01001 $ a1 $ b1-12 $ f2001

510 11 $ 6z02001 $ a1 $ b1-12 $ f2001

510 11 $ 6z01002 $ a2 $ b1-6 $ f2002

510 11 $ 6z02002 $ a2 $ b1-6 $ f2002

510 11 $ 6z03001 $ a1 $ b1-12 $ f2001

510 11 $ 6z03002 $ a1 $ b1-12 $ f2001

510 11 $ 6z03003 $ a2 $ b1-6 $ f2002

510 11 $ 6z03004 $ a2 $ b1-6 $ f2002

530 # $ 6z01001 $ p3568792162 $ j 在架 $ t1

530 # $ 6z02001 $ p3568792163 $ j 在架 $ t2

530 # $ 6z01002 $ p3568792164 $ j 在架 $ t1

530 # # $6z02002$ p3568792165$j 在架 $t2

530 # $ 6z03001 $ p3568792166 $ j 在架 $ t3

530 # # $6z03002$ p3568792167$i 在架 $t3

530 # $ 6z03003 $ p3568792168 $ j 在架 $ t4

530 # # $ 6z03004 $ p3568792169 $ j 在架 $ t4

712 02 $ a 中国国家图书馆 $ 4 收藏

801 #0 $ aCN $ bNLC $ c20070430

## 參 考 文 献

[1] 国家图书馆. 新版中国机读目录格式使用手册 [M]. 北京: 北京图书馆出版社, 2004.

[2] 美国国会图书馆网络发展与 MARC 标准办公室，加拿大国家图书馆标准规范办公室合作制定；国家图书馆文献馆藏数据格式研究课题组翻译. MARC21 馆藏数据格式 [M]. 北京：科学技术文献出版社，2003.

___