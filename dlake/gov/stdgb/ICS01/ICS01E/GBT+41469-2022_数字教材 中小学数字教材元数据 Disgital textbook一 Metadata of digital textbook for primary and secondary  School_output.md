

# 中华人民共和国国家标准

GB/T 41469—2022

# 数字教材 中小学数字教材元数据

# Digital textbook—Metadata of digital textbook for primary and secondary school

2022-04-15 发布

2022-11-01 实施

## 目次

前言 …… I  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 中小学数字教材元数据元素的描述结构、属性及扩展 …… 1  
  
4.1 元数据元素的描述结构 …… 1  
  
4.2 元数据元素的属性 …… 2  
  
4.3 元数据元素的扩展 …… 2  
  
5 中小学数字教材整体元数据 …… 3  
  
6 中小学数字教材内容对象元数据 …… 9  
  
参考文献 …… 14

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国新闻出版标准化技术委员会(SAC/TC 527)提出并归口。

本文件起草单位：人教数字出版有限公司、中国新闻出版研究院、河南众诚信息科技股份有限公司、华东师范大学、华南师范大学、河南教育电子音像出版社责任有限公司、人民教育出版社有限公司、中教云智数字科技有限公司、北京东田教育科技有限公司、浙江省教育技术中心、浙江学海教育科技有限公司。

本文件主要起草人：沙沙、钟岑岑、陈磊、钱冬明、王冬青、吴慧云、翟永勇、贺男、毕江峰、赵子莹、周靖、马兴专、禹丽锋、沈一峰。

# 数字教材 中小学数字教材元数据

## 1 范围

本文件规定了中小学数字教材元数据元素的描述结构、属性及扩展以及整体元数据和内容对象元数据。

本文件适用于中小学数字教材的开发、应用和管理，及中小学数字教材有关数据库的建设。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 7408 数据元和交换格式 信息交换 日期和时间表示法

GB 13000 信息技术 通用多八位编码字符集(UCS)

GB/T 33782—2017 信息技术 学习、教育和培训 教育管理基础代码

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 中小学数字教材 digital textbook for primary and secondary school

依据中小学课程规划或课程标准、教学大纲，系统编写、开发，适用于信息化环境下教学活动的电子图书。

### 3.2 

## 数字教材内容对象 content object of digital textbook

数字教材中允许被独立调用、使用的内容媒体。

注：本文件中的数字教材内容对象是数字教材的组成部分，可以是文本、图片、音频、视频等类型，但不包含数字教材自身。

### 3.3 

## 元数据 metadata

关于数据或数据元素的数据(可能包含其数据描述)，以及关于数据所有权、存取路径、访问权和数据易变性的数据。

[来源:GB/T 5271.17—2010,17.06.05]

## 4 中小学数字教材元数据元素的描述结构、属性及扩展

### 4.1 元数据元素的描述结构

中小学数字教材元数据元素包括复合元素和简单元素两种类型。复合元素是其子元素的集合，子元素还可包含子元素；简单元素不包含子元素，并且有自己的值。

在属性描述上，对于每个元数据元素，都定义了编号、中文名称、标签、解释、选择性、重复性、说明/示例等属性；对于简单元素，还定义了数据类型和值空间属性。

### 4.2 元数据元素的属性

#### 4.2.1 编号

元数据元素的序号，该编号也表示元素的层次结构。

#### 4.2.2 中文名称

元数据元素的中文描述性称谓。

#### 4.2.3 英文名称

元数据元素的英文描述性称谓。一般用小写英文全称，英文单词之间用“—”连接。

#### 4.2.4 解释

对元数据元素的简单释义。

#### 4.2.5 选择性

对元数据元素选取要求的描述。该描述符分别为：

a）M: 必选，表明该元数据元素应被选择；

b) O: 可选, 根据实际应用可选择也可不选择;

c） C: 条件必选，当满足一定条件时，该元数据元素应被选择。

#### 4.2.6 重复性

对元数据元素能否重复出现的描述，描述符为：

a）Y: 可重复，表明元数据元素可出现多次，如：数字教材的关键词可有多个；

b) N:不可重复,表明该元数据元素只能出现1次。对属于某个复合元素的元数据元素,当所属的复合元素可重复时,若该元素在重复出现的复合元素中分别出现1次,不视为该元素重复。

#### 4.2.7 数据类型

元数据元素的取值约束范畴，应是某同一类型的数据元集合。如：字符型、数值型、日期型等。

#### 4.2.8 值空间

元数据元素的取值范围。只有简单元素有值空间。

#### 4.2.9 说明/示例

关于元数据元素的其他必要描述信息或用于说明的例子。

### 4.3 元数据元素的扩展

中小学数字教材元数据的扩展应遵循以下原则：

a）元数据扩展的对象为元数据元素；

b）扩展的元数据元素，与已有元素之间无语义冲突，不应取代或重复已有元素。

## 中小学数字教材整体元数据

用于描述中小学数字教材整体的特征，包括10个复合元素和41个简单元素，见表1。

<div style="text-align: center;">表 1 中小学数字教材整体元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>题名</td><td style='text-align: center;'>title</td><td style='text-align: center;'>所描述数字教材的名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>正题名</td><td style='text-align: center;'>proper-title</td><td style='text-align: center;'>对数字教材内容的概括具有重要意义正式名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>在数字教材扉页上出现的题名</td></tr><tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>其他题名</td><td style='text-align: center;'>alternative-title</td><td style='text-align: center;'>正题名之外的其他名称</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>通常为另一种语言和/或文字的正题名，或者等同正题名的另一种语言和/或文字的题名，如拼音、英文等</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>用于标识数字教材的唯一代码</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>a）复合元素；b）数字教材标识符应以国家标准或行业标准为准</td></tr><tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>类别</td><td style='text-align: center;'>catalog</td><td style='text-align: center;'>数字教材标识方案或编目方案的名称或指示符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a）该类别指向一种命名方案；b）例如：“电子图书标识符”“ISBN”</td></tr><tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>表项</td><td style='text-align: center;'>entry</td><td style='text-align: center;'>在标识符类别方案中用于表示数字教材的标识值</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>标注格式取决于“2.1类别”中的规定</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>language</td><td style='text-align: center;'>用于描述数字教材内容所使用的语言类型的一组字符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(100个字符)</td><td style='text-align: center;'>宜采用GB/T 4880.1</td><td style='text-align: center;'>例如：ru（俄语）</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>description</td><td style='text-align: center;'>对数字教材的简要说明</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(2 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>根据实际应用需求，描述内容可包括数字教材的内容、特点、功能等方面</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>关键词</td><td style='text-align: center;'>keyword</td><td style='text-align: center;'>用于描述数字教材特征的主要词语</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>最能体现数字教材特征的一个或多个词语，不用于描述其他元素所描述的特征</td></tr></table>

<div style="text-align: center;">表 1 中小学数字教材整体元数据（第 2 页/共 6 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>type</td><td style='text-align: center;'>数字教材的一般范畴、功能、种属或聚类层次</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>数字教材的课程级别应使用GB/T 33782-2017中的课程级别代码，其他类型描述应使用GB 13000的字符及编码描述</td><td style='text-align: center;'>数字教材主要的类型优先被列出，至少应按照课程级别指出“国家课程数字教材”“地方课程数字教材”等类型</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>贡献者</td><td style='text-align: center;'>contributor</td><td style='text-align: center;'>在数字教材生存周期中为其发展做出贡献的实体及相关信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>a）复合元素；b）贡献者可以是人或单位</td></tr><tr><td style='text-align: center;'>7.1</td><td style='text-align: center;'>角色</td><td style='text-align: center;'>role</td><td style='text-align: center;'>实体所起的作用</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>至少应描述“主编”“责任编辑”“出版者”“制作者”4项，还可包括“编著者”“译者”“编辑加工者”等角色</td></tr><tr><td style='text-align: center;'>7.2</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>name</td><td style='text-align: center;'>即贡献实体的名字</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>当一个角色存在多个实体时，实体名称的排名存在先后</td></tr><tr><td style='text-align: center;'>7.3</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>date</td><td style='text-align: center;'>实体完成贡献的日期</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>应使用数字和GB/T 7408中列出的单位与符号</td><td style='text-align: center;'>至少应描述“出版者”对应的出版日期，还可根据角色包括制作日期等</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>版本</td><td style='text-align: center;'>version</td><td style='text-align: center;'>用于描述数字教材版本状态的一组字符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(50个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a）数字教材版本是指同一编制单位开发、采用同一技术实现方式、承载同一内容的数字教材；b）描述版本状态时，编辑性和技术性修改用“.”间隔，例如：“V2.2.1”</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>学科</td><td style='text-align: center;'>subject</td><td style='text-align: center;'>数字教材内容所属的、按相对独立的知识体系划分的类别</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB/T 33782-2017中的课程代码或GB 13000的字符及编码</td><td style='text-align: center;'>应优先采用GB/T 33782-2017中的课程代码。GB/T 33782-2017中无对应课程时，可用文字方式描述科目</td></tr></table>

<div style="text-align: center;">表 1 中小学数字教材整体元数据（第 3 页/共 6 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>依据</td><td style='text-align: center;'>basis</td><td style='text-align: center;'>表示数字教材编制依据的作品及相关信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>a）复合元素；b）通常指编写数字教材所依据的课程方案、课程标准、教学大纲、纸质教材等</td></tr><tr><td style='text-align: center;'>10.1</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>name</td><td style='text-align: center;'>所依据的作品的标识</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>通常指作为依据的出版物的主题名、文件的名称等</td></tr><tr><td style='text-align: center;'>10.2</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>所依据的作品的标识代码</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>a）复合元素；b）根据作品类型，选用相应的标识符方案</td></tr><tr><td style='text-align: center;'>10.2.1</td><td style='text-align: center;'>类别</td><td style='text-align: center;'>catalog</td><td style='text-align: center;'>作品标识方案或编目方案的名称或指示符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a）该类别指向一种命名方案；b）例如：“ISBN”“URI”</td></tr><tr><td style='text-align: center;'>10.2.2</td><td style='text-align: center;'>表项</td><td style='text-align: center;'>entry</td><td style='text-align: center;'>在标识符类方案中用于标识所依据作品的标识值</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>标注格式取决于“10.2.1类别”中的规定</td></tr><tr><td style='text-align: center;'>10.3</td><td style='text-align: center;'>版次</td><td style='text-align: center;'>edition-number</td><td style='text-align: center;'>用于表示作品版本次序的编号</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(50个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>当作品为文件等非正式出版物时，用发布日期表示版次</td></tr><tr><td style='text-align: center;'>10.4</td><td style='text-align: center;'>印次</td><td style='text-align: center;'>reprint-number</td><td style='text-align: center;'>同一版本纸质出版物的印刷次数</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>整数</td><td style='text-align: center;'>用整数表明印次</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>格式</td><td style='text-align: center;'>format</td><td style='text-align: center;'>数字教材在技术上的数据类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>数字教材的整体格式应采用GB 13000的字符及编码描述；数字教材的内容媒体格式、功能刚组建格式宜采用GB/T 28825—2012中给出的值</td><td style='text-align: center;'>用于确定数字教材所需要的运行环境，包含数字教材整体的文件格式及其包含内容的媒体格式、功能组件格式</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>版权说明</td><td style='text-align: center;'>copyright-statement</td><td style='text-align: center;'>对数字教材版权所有者、版权年份、版权形式、版权登记号等信息的简要说明</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>用文本形式注明数字教材的版权说明，至少应说明版权所有者</td></tr></table>

<div style="text-align: center;">表 1 中小学数字教材整体元数据（第 4 页/共 6 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>出版方式</td><td style='text-align: center;'>Publication-form</td><td style='text-align: center;'>对数字教材的出版形式(出版物类型)的描述</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>数字教材的出版形式通常包括数字出版、电子出版两类</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>出版地</td><td style='text-align: center;'>publication-place</td><td style='text-align: center;'>出版者所在地的城市名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>对同名异地或不为人们熟悉的城市名,宜在城市名后附省、州名或国名等限定语</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>审核</td><td style='text-align: center;'>audit</td><td style='text-align: center;'>对数字教材经相应级别的专门机构审核的情况的简要说明</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>a) 复合元素;b) 根据实际情况,应包括对数字教材经教育行政部门审定的情况描述</td></tr><tr><td style='text-align: center;'>15.1</td><td style='text-align: center;'>审核项</td><td style='text-align: center;'>audit-item</td><td style='text-align: center;'>审核内容的种类</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a) 可涉及内容审核、技术审核或政治审核、专业审核、专题审核等维度;b) 当存在审定时,应标记为“行政审定”</td></tr><tr><td style='text-align: center;'>15.2</td><td style='text-align: center;'>机构</td><td style='text-align: center;'>institute</td><td style='text-align: center;'>数字教材的审核机构的名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB/T 13000的字符</td><td style='text-align: center;'>应标注审核(或审定)机构正式完整的名称</td></tr><tr><td style='text-align: center;'>15.3</td><td style='text-align: center;'>通过时间</td><td style='text-align: center;'>date</td><td style='text-align: center;'>数字教材通过审核的时间</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>应使用数字和GB/T 7408中的单位与符号</td><td style='text-align: center;'>允许只标注年份</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>元-元数据</td><td style='text-align: center;'>meta-metadata</td><td style='text-align: center;'>用于描述元数据本身的信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>a) 复合元素;b) 元-元数据描述的元数据自身,而不是数字教材</td></tr><tr><td style='text-align: center;'>16.1</td><td style='text-align: center;'>贡献</td><td style='text-align: center;'>contribute</td><td style='text-align: center;'>对元数据实例的形成和发展做出贡献的实体</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>16.1.1</td><td style='text-align: center;'>角色</td><td style='text-align: center;'>role</td><td style='text-align: center;'>贡献的类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>所有贡献中只允许存在一个“创建者”贡献</td></tr><tr><td style='text-align: center;'>16.1.2</td><td style='text-align: center;'>实体</td><td style='text-align: center;'>entity</td><td style='text-align: center;'>对元数据实例做出贡献的具体人或组织</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>可以是实体的名称、代码、标识等信息</td></tr></table>

<div style="text-align: center;">表 1 中小学数字教材整体元数据（第 5 页/共 6 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>16.1.3</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>date</td><td style='text-align: center;'>做出贡献的时间</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>应使用数字和GB/T 7408 中的单位与符号</td><td style='text-align: center;'>例如:2021-05-23</td></tr><tr><td style='text-align: center;'>16.2</td><td style='text-align: center;'>元数据方案</td><td style='text-align: center;'>metadata-schema</td><td style='text-align: center;'>创建元数据实例的规范的名称和版本</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000 个字符)</td><td style='text-align: center;'>应使用 GB 13000 的字符及编码</td><td style='text-align: center;'>a) 直接采用本文件的元数据方案时, 可简写为本文件的标准号;b) 基于本文件规则扩展形成的元数据方案可通过文字描述</td></tr><tr><td style='text-align: center;'>16.3</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>language</td><td style='text-align: center;'>元数据实例所使用的语言</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(100 个字符)</td><td style='text-align: center;'>宜采用 GB/T 4880.1</td><td style='text-align: center;'>默认使用中文创建元数据实例, 即:zh</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>适用对象</td><td style='text-align: center;'>applicability</td><td style='text-align: center;'>数字教材所适用的对象和范围</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>17.1</td><td style='text-align: center;'>年级</td><td style='text-align: center;'>grade</td><td style='text-align: center;'>数字教材所适用的年级范围</td><td style='text-align: center;'>C</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000 个字符)</td><td style='text-align: center;'>应采用GB/T 33782-2017中的学段代码和年级代码</td><td style='text-align: center;'>a) 当“17 适用对象”元素被选用时, 该元素为必选元素;b) 用学段加年级的形式来描述列举;c) 例如: “初中八年级”“高中一年级”</td></tr><tr><td style='text-align: center;'>17.2</td><td style='text-align: center;'>地域</td><td style='text-align: center;'>region</td><td style='text-align: center;'>数字教材所适用的地区范围</td><td style='text-align: center;'>C</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000 个字符)</td><td style='text-align: center;'>应使用 GB 13000 的字符及编码</td><td style='text-align: center;'>a) 当“17 适用对象”元素被选用时, 该元素为必选元素;b) 用地名、地理坐标、区域等形式来描述列举</td></tr><tr><td style='text-align: center;'>17.3</td><td style='text-align: center;'>用户类型</td><td style='text-align: center;'>audience</td><td style='text-align: center;'>数字教材使用者的分类</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000 个字符)</td><td style='text-align: center;'>应使用 GB 13000 的字符及编码</td><td style='text-align: center;'>数字教材的用户类型可包括教师、学生、教研员等</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>册次</td><td style='text-align: center;'>volume</td><td style='text-align: center;'>用于表示数字教材内容在年级中的排列次序, 或分类别、分层次的内容模块的一组字符</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(100 个字符)</td><td style='text-align: center;'>应使用 GB 13000 的字符及编码</td><td style='text-align: center;'>例如: “七年级上”“高中必修1等”</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>size</td><td style='text-align: center;'>数字教材文件所包含的数据量的多少</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>整数</td><td style='text-align: center;'>以字节(Byte)为单位记录数字教材的大小</td></tr></table>

<div style="text-align: center;">表 1 中小学数字教材整体元数据（第 6 页/共 6 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>价格</td><td style='text-align: center;'>price</td><td style='text-align: center;'>数字教材的单位价格及相关信息</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>20.1</td><td style='text-align: center;'>计费方式</td><td style='text-align: center;'>charging-mode</td><td style='text-align: center;'>数字教材所采用的定价方式</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a) 当“20价格”元素被选用时，该元素为必选元素；b) 例如：“免费”“按册计费”“按账号计费”“按年计费”</td></tr><tr><td style='text-align: center;'>20.2</td><td style='text-align: center;'>数量单位</td><td style='text-align: center;'>quantity-unit</td><td style='text-align: center;'>在当前计费方式中规定单价的计费单位</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(100个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a) 当“20价格”元素被选用时，该元素为必选元素；b) 与“20.1计费方式”中的要求相一致；c) 例如：“册”“账号”“年”</td></tr><tr><td style='text-align: center;'>20.3</td><td style='text-align: center;'>金额</td><td style='text-align: center;'>amount</td><td style='text-align: center;'>表示数字教材单位价格的金额大小</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>数字</td><td style='text-align: center;'>a) 当“20价格”元素被选用时，该元素为必选元素；b) 以人民币“元”为单位，并精确到小数点后两位数字</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>位置</td><td style='text-align: center;'>location</td><td style='text-align: center;'>用于表明如何获取数字教材的一组字符</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>可用URI或类似地址模式来表示</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>使用限制</td><td style='text-align: center;'>usage-restrictions</td><td style='text-align: center;'>对数字教材的许可使用条件、使用范围等信息的简要说明</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>用文本形式注明用户可对数字教材做哪些事情及程度，如允许用户在购买前预览的次数、页码范围等</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>技术要求</td><td style='text-align: center;'>technical-requirement</td><td style='text-align: center;'>对使用数字教材所需要的软件、硬件等要求的简要说明</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(2 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a) 用文本形式注明使用该数字教材所需要的操作系统、硬件、网络环境、应用软件等技术条件的类型和具体要求；b) 例如：“操作系统：Windows 8、Android 4.0及以上；终端硬件：平板；网络带宽：最低10 Mbit/s；浏览器：any”</td></tr></table>

## 6 中小学数字教材内容对象元数据

用于描述中小学数字教材内容对象的特征，包括14个复合元素和32个简单元素，见表2。

<div style="text-align: center;">表 2 中小学数字教材内容对象元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>通用</td><td style='text-align: center;'>general</td><td style='text-align: center;'>该类别描述了内容对象的通用信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>内容对象的唯一标识</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>1.1.1</td><td style='text-align: center;'>类别</td><td style='text-align: center;'>catalog</td><td style='text-align: center;'>内容对象在数字教材中的标识方案或一种命名方案</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>一般应根据数字教材设计方案确定标识或命名方案</td></tr><tr><td style='text-align: center;'>1.1.2</td><td style='text-align: center;'>表项</td><td style='text-align: center;'>entry</td><td style='text-align: center;'>内容对象在数字教材中的具体标识</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如“RJ0305002”</td></tr><tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>标题</td><td style='text-align: center;'>title</td><td style='text-align: center;'>内容对象的名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>1.2.1</td><td style='text-align: center;'>正式标题</td><td style='text-align: center;'>proper-title</td><td style='text-align: center;'>内容对象的主要名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如“峨眉山月歌朗读音频”</td></tr><tr><td style='text-align: center;'>1.2.2</td><td style='text-align: center;'>其他标题</td><td style='text-align: center;'>alternative-title</td><td style='text-align: center;'>正式标题之外的其他名称或替代写法</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>language</td><td style='text-align: center;'>内容对象所载教学信息使用的语言类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(100个字符)</td><td style='text-align: center;'>宜采用GB/T 4880.1的代码</td><td style='text-align: center;'>例如：ru(俄语)</td></tr><tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>description</td><td style='text-align: center;'>以文本方式对内容对象的简介</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(2 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>关键字</td><td style='text-align: center;'>keyword</td><td style='text-align: center;'>用以描述内容对象所载教学信息的关键词语</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>生存期</td><td style='text-align: center;'>life-cycle</td><td style='text-align: center;'>该类别描述了对内容对象当前状态及发展过程发生作用的实体</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr></table>

<div style="text-align: center;">表 2 中小学数字教材内容对象元数据（第 2 页/共 5 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>版本</td><td style='text-align: center;'>version</td><td style='text-align: center;'>内容对象的版本状态</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(50个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如“V1.3.5”</td></tr><tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>贡献</td><td style='text-align: center;'>contribute</td><td style='text-align: center;'>对内容对象的当前版本状态做出贡献的实体(人或组织)</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2.2.1</td><td style='text-align: center;'>贡献者</td><td style='text-align: center;'>contributor</td><td style='text-align: center;'>对元数据实例做出贡献的实体</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>可以是人或组织的名称、代码、标识等</td></tr><tr><td style='text-align: center;'>2.2.2</td><td style='text-align: center;'>角色</td><td style='text-align: center;'>role</td><td style='text-align: center;'>贡献的类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>至少应该描述内容对象的作者</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>元-元数据</td><td style='text-align: center;'>meta-metadata</td><td style='text-align: center;'>该类别描述了元数据实例自身(不是元数据所描述的资源)的信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>3.1</td><td style='text-align: center;'>贡献</td><td style='text-align: center;'>contribute</td><td style='text-align: center;'>对元数据实例的形成和发展做出贡献的实体</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>3.1.1</td><td style='text-align: center;'>角色</td><td style='text-align: center;'>role</td><td style='text-align: center;'>贡献的类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>所有贡献中只允许存在一个“创建者”贡献</td></tr><tr><td style='text-align: center;'>3.1.2</td><td style='text-align: center;'>实体</td><td style='text-align: center;'>entity</td><td style='text-align: center;'>对元数据实例做出贡献的具体人或组织</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>可以是实体的名称、代码、标识等信息</td></tr><tr><td style='text-align: center;'>3.1.3</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>date</td><td style='text-align: center;'>做出贡献的时间</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>应为数字和GB/T 7408中列出的单位与符号</td><td style='text-align: center;'>例如2021-05-23</td></tr><tr><td style='text-align: center;'>3.2</td><td style='text-align: center;'>元数据方案</td><td style='text-align: center;'>metadata-schema</td><td style='text-align: center;'>创建元数据实例的规范的名称和版本</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>即为本文件的编号</td></tr><tr><td style='text-align: center;'>3.3</td><td style='text-align: center;'>语种</td><td style='text-align: center;'>language</td><td style='text-align: center;'>元数据实例所使用的语言</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>宜采用GB/T 4880.1的代码</td><td style='text-align: center;'>默认使用中文创建元数据实例,即:zh</td></tr></table>

<div style="text-align: center;">表 2 中小学数字教材内容对象元数据（第 3 页/共 5 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>技术</td><td style='text-align: center;'>technical</td><td style='text-align: center;'>该类别描述了资源的技术要求及其相关特征</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>4.1</td><td style='text-align: center;'>格式</td><td style='text-align: center;'>format</td><td style='text-align: center;'>资源在技术上的数据类型。该数据元素用于确定资源所需的运行软件</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>内容对象的式应使用GB 13000的字符及编码描述；小粒度的媒体资源宜采用GB/T 28825—2012中给出的值</td><td style='text-align: center;'>内容对象的结构较为复杂时，可能包含多种格式的媒体文件或功能模块</td></tr><tr><td style='text-align: center;'>4.2</td><td style='text-align: center;'>使用环境</td><td style='text-align: center;'>requirement</td><td style='text-align: center;'>使用资源所需要的技术条件</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>用一段文字描述内容对象运行所需的硬件、软件、网络等</td></tr><tr><td style='text-align: center;'>4.3</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>size</td><td style='text-align: center;'>内容对象所包含的数据量的多少</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>整数（用十进制数字“0”到“9”表示）</td><td style='text-align: center;'>以字节（Byte）为单位记录内容对象的大小</td></tr><tr><td style='text-align: center;'>4.4</td><td style='text-align: center;'>位置</td><td style='text-align: center;'>location</td><td style='text-align: center;'>用于表明如何获取内容对象的字符串</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如用URL方式给出内容对象在数字教材中的位置</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>教育</td><td style='text-align: center;'>educational</td><td style='text-align: center;'>该类别描述了资源在基础教育和教学方面的一些关键特征</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>5.1</td><td style='text-align: center;'>资源类型</td><td style='text-align: center;'>learning-resource-type</td><td style='text-align: center;'>内容对象按教育资源的分类类型，越主要的类型越先列出</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>可参考《基础教育教学资源元数据 第2部分：分类代码》中的资源类型代码表、DC.type、GEM“资源类型”分类代码等分类</td></tr><tr><td style='text-align: center;'>5.2</td><td style='text-align: center;'>适用对象</td><td style='text-align: center;'>applicability</td><td style='text-align: center;'>内容对象所适用的范围</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>5.2.1</td><td style='text-align: center;'>用户类型</td><td style='text-align: center;'>audience</td><td style='text-align: center;'>内容对象的主要使用者</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如教师、学生、教师和学生等</td></tr><tr><td style='text-align: center;'>5.2.2</td><td style='text-align: center;'>年级</td><td style='text-align: center;'>grade-level</td><td style='text-align: center;'>内容对象的适用者的年级特征描述</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应采用GB/T 33782—2017中的学段代码和年级代码</td><td style='text-align: center;'>用学段加年级的形式来描述列举。例如：“初中八年级”“高中一年级”</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>权利</td><td style='text-align: center;'>rights</td><td style='text-align: center;'>描述内容对象本身所有的或被赋予的权限信息</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>a）复合元素；b）即内容对象的著作权声明</td></tr></table>

<div style="text-align: center;">表 2 中小学数字教材内容对象元数据（第 4 页/共 5 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>6.1</td><td style='text-align: center;'>版权</td><td style='text-align: center;'>copyright</td><td style='text-align: center;'>内容对象的著作权所有者及权利形式</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>a）当“6权利”被选用时本项为必备；b）以文字形式描述著作权人及其权利类型</td></tr><tr><td style='text-align: center;'>6.2</td><td style='text-align: center;'>限制</td><td style='text-align: center;'>restrictions</td><td style='text-align: center;'>内容对象的使用限制条件和范围</td><td style='text-align: center;'>O</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>著作权人对内容对象的使用设有特殊限制时，可用文字方式描述</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>关联</td><td style='text-align: center;'>relation</td><td style='text-align: center;'>描述内容对象与其他资源的关系</td><td style='text-align: center;'>M</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>a）复合元素；b）至少应包含内容对象与数字教材之间的关联</td></tr><tr><td style='text-align: center;'>7.1</td><td style='text-align: center;'>关联类型</td><td style='text-align: center;'>relationship</td><td style='text-align: center;'>内容对象与关联资源之间的关系类型</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>可以是包含、所属、相关等类型</td></tr><tr><td style='text-align: center;'>7.2</td><td style='text-align: center;'>关联资源</td><td style='text-align: center;'>resource</td><td style='text-align: center;'>与内容对象关联的数字教材或其他教学资源的通用信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>7.2.1</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>identifier</td><td style='text-align: center;'>与内容对象关联的数字教材或其他教学资源的标识</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr><tr><td style='text-align: center;'>7.2.1.1</td><td style='text-align: center;'>类别</td><td style='text-align: center;'>catalog</td><td style='text-align: center;'>内容对象关联的数字教材或其他教学资源的标识方案或一种命名方案</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如“ISBN”“电子图书标识”等</td></tr><tr><td style='text-align: center;'>7.2.1.2</td><td style='text-align: center;'>表项</td><td style='text-align: center;'>entry</td><td style='text-align: center;'>在标识或命名方案中此数字教材或教学资源的教学资源的具体标识符</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如“ISBN 978-7-89448-289-1”“ISBN 978-7-107-48389-3.pdf”</td></tr><tr><td style='text-align: center;'>7.2.2</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>description</td><td style='text-align: center;'>与内容对象关联的数字教材或其他教学资源内容的简介</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>根据实际应用需求，描述内容可包括数字教材的内容、特点、功能等方面</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>分类系统</td><td style='text-align: center;'>classification-system</td><td style='text-align: center;'>该类信息描述的内容对象所属学科类别及课程教材信息</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>复合元素</td></tr></table>

<div style="text-align: center;">表 2 中小学数字教材内容对象元数据（第 5 页/共 5 页）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>解释</td><td style='text-align: center;'>选择性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>值空间</td><td style='text-align: center;'>说明/示例</td></tr><tr><td style='text-align: center;'>8.1</td><td style='text-align: center;'>学科名称</td><td style='text-align: center;'>curriculum-name</td><td style='text-align: center;'>内容对象关联学科名称</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB/T 33782—2017中的课程代码，或使用GB 13000的字符及编码</td><td style='text-align: center;'>应优先采用GB/T 33782—2017中的课程代码。GB/T 33782—2017中无内容对象的对应课程时，可用文字方式描述科目</td></tr><tr><td style='text-align: center;'>8.2</td><td style='text-align: center;'>课程标准</td><td style='text-align: center;'>curricular-standard</td><td style='text-align: center;'>描述内容对象与课程标准内容框架的对应关系</td><td style='text-align: center;'>M</td><td style='text-align: center;'>N</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>无对应课程标准的地方课程数字教材，可描述内容对象与相应课程方案或教学大纲的关系</td></tr><tr><td style='text-align: center;'>8.3</td><td style='text-align: center;'>教材目录</td><td style='text-align: center;'>textbook-code</td><td style='text-align: center;'>描述内容对象与教材内容框架的对应关系</td><td style='text-align: center;'>O</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>字符型(1 000个字符)</td><td style='text-align: center;'>应使用GB 13000的字符及编码</td><td style='text-align: center;'>例如“义务教育教科书七年级上册第2.3节”</td></tr></table>

## 参考文献

[1] GB/T 3792—2021 信息与文献 资源描述

[2] GB/T 4880.1 语种名称代码 第1部分：2字母代码

[3] GB/T 5271.17—2010 信息技术 词汇 第 17 部分: 数据库

[4] GB/T 13745—2009 学科分类与代码

[5] GB/T 21365—2008 信息技术 学习、教育和培训 学习对象元数据

[6] GB/T 25100—2010 信息与文献 都柏林核心元数据元素集

[7] GB/T 28825—2012 信息技术 学习、教育和培训 学习对象分类代码

[8] GB/T 30330 中国出版物在线信息交换 图书产品信息格式规范

[9] GB/T 36453—2018 信息技术 学习、教育和培训 电子课本信息模型

[10] CY/T 90.2—2013 出版元数据 第2部分：核心数据元素集

[11] CY/T 90.3—2013 出版元数据 第 3 部分: 通用数据元素集

[12] CY/T 97—2013 电子图书元数据

[13] JY/T 0607—2017 基础教育教学资源元数据 信息模型

[14] JY/T 0609—2017 基础教育教学资源元数据 XML 绑定

[15] JY/T 0610—2017 基础教育教学资源元数据 实施指南

[16] 曾杰. 基础教育教学资源元数据 第2部分: 分类代码 $$ M $$ //中央电化教育馆. 基础教育教学资源元数据标准 $$ M $$ . 北京: 中央广播电视大学出版社, 2017.