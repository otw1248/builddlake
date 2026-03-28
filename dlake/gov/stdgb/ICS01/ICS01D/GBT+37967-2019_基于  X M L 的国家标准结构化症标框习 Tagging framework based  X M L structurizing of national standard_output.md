

# 中华人民共和国国家标准

GB/T 37967—2019

# 基于 XML 的国家标准结构化置标框架

# Tagging framework based XML structurizing of national standard

2019-08-30 发布

2020-03-01 实施

## 目 次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 命名空间前缀惯例 …… 1  
  
4 结构化处理基本架构 …… 1  
  
5 元素和标签定义 …… 3  
  
5.1 标准内容结构化模块 …… 3  
  
5.2 起草信息结构化 …… 5  
  
5.3 标准实施信息 …… 5  
  
附录 A（资料性附录） 国家标准结构化处理 XML 模式文件说明 …… 7  
  
附录 B（资料性附录） 国家标准结构化处理 XML 元素表 …… 12  
  
附录 C（资料性附录） 国家标准结构化标注实例 …… 14  
  
参考文献 …… 25

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国术语与语言内容资源标准化技术委员会(SAC/TC 62)提出并归口。

本标准起草单位：中国标准化研究院、国家标准化管理委员会标准信息中心、北京语言大学、军事科学院系统工程研究院军用标准研究中心、中国科学技术信息研究所、中国质检出版社、内蒙古自治区标准化院、华南师范大学、上海对外经贸大学、北京悦尔信息技术有限公司、厦门鼎标企业管理服务有限公司、中国电信股份有限公司。

本标准主要起草人：程永红、王海涛、马志远、荀恩东、曹馨宇、赵建国、刘耀、刘晓东、蒋碧蓉、蒙永业、郝天永、刘亮亮、贾仰理、贾双文、张文辉、周长青、肖玉敬、杨震、杨茂初、陈晓玲。

# 基于 XML 的国家标准结构化置标框架

## 1 范围

本标准规定了对国家标准文本进行结构化处理和表示时用到的命名空间前缀惯例、结构化处理基本架构以及元素和标准定义的要求。

本标准适用于国家标准结构化的数字化加工以及相关开发与应用，其他标准可参照使用。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 24639 元数据的 XML Schema 置标规则

## 3 命名空间前缀惯例

本标准在描述元素和属性时采用一系列命名空间前缀，如表1所示。

<div style="text-align: center;">表 1 命名空间前缀</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>命名空间前缀</td><td style='text-align: center;'>命名空间 URI</td></tr><tr><td style='text-align: center;'>content</td><td style='text-align: center;'>http://www.xmlgb.org/xcontent</td></tr><tr><td style='text-align: center;'>edit</td><td style='text-align: center;'>http://www.xmlgb.org/xedit</td></tr><tr><td style='text-align: center;'>execute</td><td style='text-align: center;'>http://www.xmlgb.org/xexecute</td></tr></table>

## 4 结构化处理基本架构

按 GB/T 24639 的规定，采用基于 XML 的方法在对国家标准进行结构化处理时，主要分为以下 3 个模块，即：

a）标准内容信息结构化；

b) 标准编制起草信息结构化；

c）标准贯彻实施信息结构化。

国家标准结构化模块内容如图 1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_121_212_1042_1401.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 1 国家标准结构化模块内容</div>


国家标准结构化处理 XML 模式文件说明参见附录 A。所有 XML 元素及描述参见附录 B。结构化标注实例参见附录 C。

## 5 元素和标签定义

### 5.1 标准内容结构化模块

#### 5.1.1 基本信息结构化

基本信息结构化主要指对标准文献封面中给出的标准文件描述性信息进行处理。描述基本信息的元素见表2。

<div style="text-align: center;">表 2 基本信息元素</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>basic_info</td><td style='text-align: center;'>标准内容基本信息的根元素</td><td style='text-align: center;'></td><td style='text-align: center;'>〈basic_info〉</td></tr><tr><td style='text-align: center;'>cn</td><td style='text-align: center;'>标准中文名称</td><td style='text-align: center;'></td><td style='text-align: center;'>〈cn〉标准中文名称〈/cn〉</td></tr><tr><td style='text-align: center;'>en</td><td style='text-align: center;'>标准英文译名</td><td style='text-align: center;'>lang=&quot;en&quot;</td><td style='text-align: center;'>〈en lang=&quot;en&quot;〉标准英文译名〈/en〉</td></tr><tr><td style='text-align: center;'>ics</td><td style='text-align: center;'>国际标准分类号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈ics〉ICS 分类号〈/ics〉</td></tr><tr><td style='text-align: center;'>ccs</td><td style='text-align: center;'>中国标准文献分类号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈ccs〉中国标准文献分类号〈/ccs〉</td></tr><tr><td style='text-align: center;'>gbn</td><td style='text-align: center;'>国标号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈gbn〉国标号〈/gbn〉</td></tr><tr><td style='text-align: center;'>isd</td><td style='text-align: center;'>发布日期</td><td style='text-align: center;'></td><td style='text-align: center;'>〈isd〉发布日期〈/isd〉</td></tr><tr><td style='text-align: center;'>efd</td><td style='text-align: center;'>实施日期</td><td style='text-align: center;'></td><td style='text-align: center;'>〈efd〉实施日期〈/efd〉</td></tr></table>

#### 5.1.2 辅助信息结构化

标准辅助描述信息结构化主要是对前言、目录等内容进行处理，置标所需元素见表3。

<div style="text-align: center;">表 3 辅助信息元素</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>auxiliary_info</td><td style='text-align: center;'>标准辅助信息根元素</td><td style='text-align: center;'></td><td style='text-align: center;'>(auxiliare-info)</td></tr><tr><td style='text-align: center;'>catalogue</td><td style='text-align: center;'>目次</td><td style='text-align: center;'></td><td style='text-align: center;'>(catalogue)</td></tr><tr><td style='text-align: center;'>clg_item</td><td style='text-align: center;'>目次条目</td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_item)</td></tr><tr><td style='text-align: center;'>clg_id</td><td style='text-align: center;'>目次条目编号</td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_id) 目次条目编号(clg_id)</td></tr><tr><td style='text-align: center;'>clg_name</td><td style='text-align: center;'>目次条目内容</td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_name) 目次条目内容(clg_name)</td></tr><tr><td style='text-align: center;'>s2C</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_item)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_id) 目次条目编号(clg_id)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_name) 目次条目内容(clg_name)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_item)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_id) 目次条目编号(clg_id)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_name) 目次条目内容(clg_name)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_item)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_id) 目次条目编号(clg_id)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_name) 目次条目内容(clg_name)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_item)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_id) 目次条目编号(clg_id)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_name) 目次条目内容(clg_name)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_item)</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>(clg_id) 目次条目编号(clg_id)</td></tr></table>

<div style="text-align: center;">表 3（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>preface</td><td style='text-align: center;'>前言</td><td style='text-align: center;'></td><td style='text-align: center;'>〈preface〉前言〈/preface〉</td></tr><tr><td style='text-align: center;'>introduction</td><td style='text-align: center;'>引言</td><td style='text-align: center;'></td><td style='text-align: center;'>〈introduction〉引言〈/introduction〉</td></tr><tr><td style='text-align: center;'>scope</td><td style='text-align: center;'>范围</td><td style='text-align: center;'></td><td style='text-align: center;'>〈scope〉使用范围〈/scope〉</td></tr><tr><td style='text-align: center;'>normativereference</td><td style='text-align: center;'>规范性引用文件</td><td style='text-align: center;'></td><td style='text-align: center;'>〈normativereference〉</td></tr><tr><td rowspan="4">n_docum</td><td rowspan="4">规范性引用文件条目</td><td rowspan="4"></td><td style='text-align: center;'>〈n_docum〉文件一〈/n_docum〉</td></tr><tr><td style='text-align: center;'>〈n_docum〉文件二〈/n_docum〉</td></tr><tr><td style='text-align: center;'>〈n_docum〉文件三〈/n_docum〉</td></tr><tr><td style='text-align: center;'>〈/normativereference〉</td></tr><tr><td style='text-align: center;'>appendix</td><td style='text-align: center;'>附录</td><td style='text-align: center;'></td><td style='text-align: center;'>〈appendix〉</td></tr><tr><td style='text-align: center;'>apd_item</td><td style='text-align: center;'>附录条目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈apd_item〉</td></tr><tr><td rowspan="2">apd_id</td><td rowspan="2">附录条目编号</td><td rowspan="2"></td><td style='text-align: center;'>〈apd_id〉附录A〈/apd_id〉</td></tr><tr><td style='text-align: center;'>〈apd_body〉附录内容〈/apd_body〉</td></tr><tr><td rowspan="6">apd_body</td><td rowspan="6">附录条目内容</td><td rowspan="6"></td><td style='text-align: center;'>〈/apd_item〉</td></tr><tr><td style='text-align: center;'>〈apd_item〉</td></tr><tr><td style='text-align: center;'>〈apd_id〉附录B〈/apd_id〉</td></tr><tr><td style='text-align: center;'>〈apd_body〉附录内容〈/apd_body〉</td></tr><tr><td style='text-align: center;'>〈/apd_item〉</td></tr><tr><td style='text-align: center;'>〈/appendix〉</td></tr><tr><td style='text-align: center;'>reference</td><td style='text-align: center;'>参考文献</td><td style='text-align: center;'></td><td style='text-align: center;'>〈reference〉</td></tr><tr><td rowspan="4">ref_item</td><td rowspan="4">参考文献条目</td><td rowspan="4"></td><td style='text-align: center;'>〈ref_item〉文献一〈/ref_item〉</td></tr><tr><td style='text-align: center;'>〈ref_item〉文献二〈/ref_item〉</td></tr><tr><td style='text-align: center;'>〈ref_item〉文献三〈/ref_item〉</td></tr><tr><td style='text-align: center;'>〈/reference〉</td></tr></table>

#### 5.1.3 术语信息结构化

标准中定义的术语在结构化时用到的元素见表4。

<div style="text-align: center;">表 4 术语信息元素</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>term</td><td style='text-align: center;'>术语信息根元素</td><td style='text-align: center;'></td><td style='text-align: center;'>〈term〉</td></tr><tr><td style='text-align: center;'>t_item</td><td style='text-align: center;'>术语条目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈t_item〉</td></tr><tr><td style='text-align: center;'>t_id</td><td style='text-align: center;'>条目编号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈t_id〉条目编号〈/t_id〉</td></tr><tr><td style='text-align: center;'>t_cn</td><td style='text-align: center;'>术语名称</td><td style='text-align: center;'></td><td style='text-align: center;'>〈t_cn〉术语名称〈/t_cn〉</td></tr><tr><td style='text-align: center;'>t_en</td><td style='text-align: center;'>术语英文名称</td><td style='text-align: center;'>lang=&quot;en&quot;</td><td style='text-align: center;'>〈t_en lang=&quot;en&quot;〉英文名称〈/t_en〉</td></tr><tr><td style='text-align: center;'>t_def</td><td style='text-align: center;'>术语定义</td><td style='text-align: center;'></td><td style='text-align: center;'>〈t_def〉〈! [CDATA[术语定义]]〉〈/t_def〉</td></tr><tr><td style='text-align: center;'>t_note</td><td style='text-align: center;'>注</td><td style='text-align: center;'></td><td style='text-align: center;'>〈t_note〉注〈/t_note〉</td></tr><tr><td style='text-align: center;'>t_exp</td><td style='text-align: center;'>例</td><td style='text-align: center;'></td><td style='text-align: center;'>〈pic src=&quot;./image.jpg&quot;〉</td></tr><tr><td style='text-align: center;'>pic</td><td style='text-align: center;'>图表</td><td style='text-align: center;'></td><td style='text-align: center;'>〈/term〉</td></tr></table>

#### 5.1.4 主体内容部分结构化

标准主体内容结构化主要是对标准正文信息进行处理，主要包括表 5 中的元素。

<div style="text-align: center;">表 5 可扩展部分内容元素</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>technology</td><td style='text-align: center;'>技术内容根元素</td><td style='text-align: center;'></td><td style='text-align: center;'>〈technology〉</td></tr><tr><td style='text-align: center;'>tech_item</td><td style='text-align: center;'>章节条目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_item〉</td></tr><tr><td style='text-align: center;'>tech_itid</td><td style='text-align: center;'>章节编号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_itid〉4〈/tech_itid〉</td></tr><tr><td style='text-align: center;'>tech_itname</td><td style='text-align: center;'>章节标题</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_itname〉题目〈/tech_itname〉</td></tr><tr><td style='text-align: center;'>tech_paragraph</td><td style='text-align: center;'>二级条目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_paragraph〉</td></tr><tr><td style='text-align: center;'>tech_paraid</td><td style='text-align: center;'>二级编号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_paraid〉4.1〈/tech_paraid〉</td></tr><tr><td style='text-align: center;'>tech_paraname</td><td style='text-align: center;'>二级题目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_paraname〉题目〈/tech_paraname〉</td></tr><tr><td style='text-align: center;'>tech_part</td><td style='text-align: center;'>三级条目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_part〉</td></tr><tr><td style='text-align: center;'>tech_ptid</td><td style='text-align: center;'>三级编号</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_ptid〉4.1.1〈/tech_ptid〉</td></tr><tr><td style='text-align: center;'>tech_ptname</td><td style='text-align: center;'>三级题目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_ptname〉题目〈/tech_ptname〉</td></tr><tr><td style='text-align: center;'>tech_ptbody</td><td style='text-align: center;'>技术内容</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_ptbody〉</td></tr><tr><td style='text-align: center;'>pic</td><td style='text-align: center;'>图表</td><td style='text-align: center;'></td><td style='text-align: center;'>〈tech_item〉</td></tr></table>

### 5.2 起草信息结构化

起草信息结构化主要是描述起草制定人员信息、标准起草阶段过程以及成果信息等。结构化处理所需元素见表6。

<div style="text-align: center;">表 6 其他起草相关元素</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>edit</td><td style='text-align: center;'>标准编制信息根元素</td><td style='text-align: center;'></td><td style='text-align: center;'>〈edit〉</td></tr><tr><td rowspan="3">mode</td><td rowspan="3">编制修改类型(草案、征求意见、终稿)</td><td rowspan="3"></td><td style='text-align: center;'>〈mode〉编制修改类型(草案、征求意见、终稿)</td></tr><tr><td style='text-align: center;'>〈/mode〉</td></tr><tr><td style='text-align: center;'>〈time〉编制修改时间〈/time〉</td></tr><tr><td style='text-align: center;'>time</td><td style='text-align: center;'>编制修改时间</td><td style='text-align: center;'></td><td style='text-align: center;'>〈expert〉</td></tr><tr><td rowspan="2">expert</td><td rowspan="2">专家信息</td><td rowspan="2"></td><td style='text-align: center;'>〈ep_name〉专家姓名〈/ep_name〉</td></tr><tr><td style='text-align: center;'>〈ep_company〉单位〈/ep_company〉</td></tr><tr><td style='text-align: center;'>ep_name</td><td style='text-align: center;'>专家姓名</td><td style='text-align: center;'></td><td style='text-align: center;'>〈ep_contact〉联系方式〈/ep_contact〉</td></tr><tr><td style='text-align: center;'>ep_company</td><td style='text-align: center;'>专家单位</td><td style='text-align: center;'></td><td style='text-align: center;'>......</td></tr><tr><td style='text-align: center;'>ep_contact</td><td style='text-align: center;'>专家联系方式</td><td style='text-align: center;'></td><td style='text-align: center;'>〈/edit〉</td></tr></table>

### 5.3 标准实施信息

对描述标准实施信息的结构化所需元素如见表7。

<div style="text-align: center;">表 7 标准实施信息元素</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>属性</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>execute</td><td style='text-align: center;'>标准实施信息根元素</td><td style='text-align: center;'></td><td style='text-align: center;'>〈execute〉</td></tr><tr><td style='text-align: center;'>feedback</td><td style='text-align: center;'>标准实施反馈条目</td><td style='text-align: center;'></td><td style='text-align: center;'>〈feedback〉</td></tr><tr><td style='text-align: center;'>fb_source</td><td style='text-align: center;'>标准实施反馈来源</td><td style='text-align: center;'></td><td style='text-align: center;'>〈fb_source〉反馈来源〈/fb_source〉</td></tr><tr><td rowspan="7">fb_info</td><td rowspan="7">标准实施反馈内容</td><td style='text-align: center;'></td><td style='text-align: center;'>〈fb_info〉反馈信息〈/fb_info〉</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>〈/feedback〉</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>〈feedback〉</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>〈fb_source〉反馈来源〈/fb_source〉</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>〈fb_info〉反馈信息〈/fb_info〉</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>〈/feedback〉</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>〈/execute〉</td></tr></table>

## 附录 A

## （资料性附录）  国家标准结构化处理 XML 模式文件说明

<?xml version=1.0 encoding="GB 2312"?>

〈standard〉

<content>

〈basic_info〉

〈cn〉标准中文名称〈/cn〉

〈en lang="en"〉标准英文译名〈/en〉

icsICS 分类号（ics）

〈ccs〉中国标准文献分类号〈/ccs〉

<gbn>国标号</gbn>

<isd>发布日期</isd>

<efd>实施日期</efd>

</basic_info>

⟨auxiliary_info⟩

<catalogue>

<clg_item>

<clg_id> 目次条目编号</clg_id>

〈clg_name〉目次条目内容〈/clg_name〉

</clg_item>

<clg_item>

<clg_id> 目次条目编号</clg_id>

〈clg_name〉目次条目内容〈/clg_name〉

 $ </clg\_item> $ 

<clg_item>

<clg_id> 目次条目编号</clg_id>

<clg_name>目次条目内容</clg_name>

 $ </clg\_item> $ 

</catalogue>

〈preface〉前言〈/preface〉

<introduction> 引言</introduction>

〈scope〉使用范围〈/scope〉

<normativereference>

〈n_docum〉文件一〈/n_docum〉

〈n_docum〉文件二〈/n_docum〉

〈n_docum〉文件三〈/n_docum〉

</normativereference>

(appendix)

<apd item>

〈apd_id〉附录 A〈/apd_id〉

<apd_body>附录内容</apd_body>
</apd_item>
<apd_item>
<apd_id>附录 B</apd_id>
<apd_body>附录内容</apd_body>
</apd_item>
</appendix>
<reference>
<ref_item>文献一</ref_item>
<ref_item>文献二</ref_item>
<ref_item>文献三</ref_item>
</reference>
</auxiliary_info>
<term>
<t_item>
<t_id>条目编号</t_id>
<t_cn>术语名称</t_cn>
<t_en_lang="en">英文名称</t_en>
<t_def></t_def>
<t_note>注</t_note>
<t_exp>例</t_exp>
<pic src="./image.jpg"/>
</t_item>
<t_item>
<t_id>条目编号</t_id>
<t_cn>术语名称</t_cn>
<t_en_lang="en">英文名称</t_en>
<t_def></t_def>
<t_note>注</t_note>
<t_exp>例</t_exp>
<pic src="./image.jpg"/>
</t_item>
<t_item>
<t_id>条目编号</t_id>
<t_cn>术语名称</t_cn>
<t_en_lang="en">英文名称</t_en>
<t_def></t_def>
<t_note>注</t_note>
<t_exp>例</t_exp>
<pic src="./image.jpg"/>
</term>
<technology>

<tech_item>

    <tech_itid>4</tech_itid>

    <tech_itname>题目</tech_itname>

    <tech_paragraph>

        <tech_paraid>4.1</tech_paraid>

        <tech_paraname>题目</tech_paraname>

        <tech_part>

            <tech_ptid>4.1.1</tech_ptid>

            <tech_ptname>题目</tech_ptname>

            <tech_ptbody>

                <!-- [CDATA[内容]] -->

                <pic src="./image.jpg"/>

                <tech_ptbody>

                    <tech_part>

                        <tech_ptid>4.1.2</tech_ptid>

                        <tech_ptname>题目</tech_ptname>

                        <tech_ptbody>

                            <!-- [CDATA[内容]] -->

                            <pic src="./image.jpg"/>

                            <tech_ptbody>

                                <tech_part>

                                    <tech_paragraph>

                                        <tech_paragraph>

                                            <tech_paraid>4.2</tech_paraid>

                                        <tech_paraname>题目</tech_paraname>

                                        <tech_part>

                                            <tech_ptid>4.2.1</tech_ptid>

                                            <tech_ptname>题目</tech_ptname>

                                            <tech_ptbody>

                                                <tech_part>

                                                    <!-- [CDATA[内容]] -->

                                                    <pic src="./image.jpg"/>

                                                </tech_ptbody>

                                                </tech_part>

                                                <tech_part>

                                                    <tech_ptid>4.2.2</tech_ptid>

                                                    <tech_ptname>题目</tech_ptname>

                                                    <tech_ptbody>

                                                    <!-- [CDATA[内容]] -->

                                                    <pic src="./image.jpg"/>

                                                </tech_ptbody>

                                                </tech_part>

                                                </tech_paragraph>

                                            </tech_part>

                                        </tech_ptid>

                                    </tech_ptbody>

                                </tech_part>

            </tech_ptid>

        </tech_ptname>

    </tech_ptbody>

</tech_item>

</tech_item>

<tech_item>

<tech_itid>5</tech_itid>

<tech_itname>题目</tech_itname>

<tech_paragraph>

<tech_paraid>5.1</tech_paraid>

<tech_paraname>题目</tech_paraname>

<tech_part>

<tech_ptid>5.1.1</tech_ptid>

<tech_ptname>题目</tech_ptname>

<tech_ptbody>

！[CDATA[内容]]>

<pic src="./image.jpg"/>

</tech_ptbody>

</tech_part>

<tech_part>

<tech_ptid>5.1.2</tech_ptid>

<tech_ptname>题目</tech_ptname>

<tech_ptbody>

！[CDATA[内容]]>

<pic src="./image.jpg"/>

</tech_ptbody>

</tech_part>

</tech_paragraph>

<tech_paragraph>

<tech_paraid>5.2</tech_paraid>

<tech_paraname>题目</tech_paraname>

<tech_part>

<tech_ptid>5.2.1</tech_ptid>

<tech_ptname>题目</tech_ptname>

<tech_ptbody>

！[CDATA[内容]]>

<pic src="./image.jpg"/>

</tech_ptbody>

</tech_part>

<tech_part>

<tech_ptid>5.2.2</tech_ptid>

<tech_ptname>题目</tech_ptname>

<tech_ptbody>

！[CDATA[内容]]>

<pic src="./image.jpg"/>

</tech_ptbody>

</tech_part>

</tech_paragraph>

</tech_item>

</technology>

</content>

〈edit〉

〈mode〉编制修改类型（草案、征求意见、终稿）〈/mode〉

〈time〉编制修改时间〈/time〉

<expert>

〈ep_name〉专家姓名〈/ep_name〉

〈ep_company〉单位〈/ep_company〉

〈ep_contact〉联系方式〈/ep_contact〉

<expert>

<expert>

〈ep_name〉专家姓名〈/ep_name〉

〈ep company〉单位〈/ep company〉

〈ep_contact〉联系方式〈/ep_contact〉

〈/expert〉

</edit>

<execute>

<feedback>

〈fb_source〉反馈来源〈/fb_source〉

<fb_info>反馈信息</fb_info>

</feedback>

<feedback>

〈fb_source〉反馈来源〈/fb_source〉

〈 o 〉

</feedback>

\\执行程序

</standard>

附录 B

(资料性附录)

国家标准结构化处理 XML 元素表

国家标准结构化处理中所有 XML 元素及描述见表 B.1 所示。

<div style="text-align: center;">表 B.1 国家标准结构化处理 XML 元素表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>basic_info</td><td style='text-align: center;'>标准内容基本信息的根元素</td></tr><tr><td style='text-align: center;'>cn</td><td style='text-align: center;'>标准中文名称</td></tr><tr><td style='text-align: center;'>en</td><td style='text-align: center;'>标准英文译名</td></tr><tr><td style='text-align: center;'>ics</td><td style='text-align: center;'>国际标准分类号(ICS 分类号)</td></tr><tr><td style='text-align: center;'>ccs</td><td style='text-align: center;'>中国标准文献分类号</td></tr><tr><td style='text-align: center;'>gbn</td><td style='text-align: center;'>国标号</td></tr><tr><td style='text-align: center;'>isd</td><td style='text-align: center;'>发布日期</td></tr><tr><td style='text-align: center;'>efd</td><td style='text-align: center;'>实施日期</td></tr><tr><td style='text-align: center;'>auxiliary_info</td><td style='text-align: center;'>标准辅助信息根元素</td></tr><tr><td style='text-align: center;'>catalogue</td><td style='text-align: center;'>目次</td></tr><tr><td style='text-align: center;'>clg_item</td><td style='text-align: center;'>目次条目</td></tr><tr><td style='text-align: center;'>clg_id</td><td style='text-align: center;'>目次条目编号</td></tr><tr><td style='text-align: center;'>clg_name</td><td style='text-align: center;'>目次条目内容</td></tr><tr><td style='text-align: center;'>preface</td><td style='text-align: center;'>前言</td></tr><tr><td style='text-align: center;'>introduction</td><td style='text-align: center;'>引言</td></tr><tr><td style='text-align: center;'>scope</td><td style='text-align: center;'>范围</td></tr><tr><td style='text-align: center;'>normative_reference</td><td style='text-align: center;'>规范性引用文件</td></tr><tr><td style='text-align: center;'>n_docum</td><td style='text-align: center;'>规范性引用文件条目</td></tr><tr><td style='text-align: center;'>appendix</td><td style='text-align: center;'>附录</td></tr><tr><td style='text-align: center;'>apd_item</td><td style='text-align: center;'>附录条目</td></tr><tr><td style='text-align: center;'>apd_id</td><td style='text-align: center;'>附录条目编号</td></tr><tr><td style='text-align: center;'>apd_body</td><td style='text-align: center;'>附录条目内容</td></tr><tr><td style='text-align: center;'>reference</td><td style='text-align: center;'>参考文献</td></tr><tr><td style='text-align: center;'>ref_item</td><td style='text-align: center;'>参考文献条目</td></tr><tr><td style='text-align: center;'>term</td><td style='text-align: center;'>术语信息根元素</td></tr><tr><td style='text-align: center;'>t_item</td><td style='text-align: center;'>术语条目</td></tr><tr><td style='text-align: center;'>t_id</td><td style='text-align: center;'>条目编号</td></tr><tr><td style='text-align: center;'>t_cn</td><td style='text-align: center;'>术语名称</td></tr><tr><td style='text-align: center;'>t_en</td><td style='text-align: center;'>术语英文名称</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>t_def</td><td style='text-align: center;'>术语定义</td></tr><tr><td style='text-align: center;'>t_note</td><td style='text-align: center;'>注</td></tr><tr><td style='text-align: center;'>t_exp</td><td style='text-align: center;'>例</td></tr><tr><td style='text-align: center;'>technology</td><td style='text-align: center;'>技术内容根元素</td></tr><tr><td style='text-align: center;'>tech_item</td><td style='text-align: center;'>章节条目</td></tr><tr><td style='text-align: center;'>tech_itid</td><td style='text-align: center;'>章节编号</td></tr><tr><td style='text-align: center;'>tech_itname</td><td style='text-align: center;'>章节标题</td></tr><tr><td style='text-align: center;'>tech_paragraph</td><td style='text-align: center;'>二级条目</td></tr><tr><td style='text-align: center;'>tech_paraid</td><td style='text-align: center;'>二级编号</td></tr><tr><td style='text-align: center;'>tech_paraname</td><td style='text-align: center;'>二级题目</td></tr><tr><td style='text-align: center;'>tech_part</td><td style='text-align: center;'>三级条目</td></tr><tr><td style='text-align: center;'>tech_ptid</td><td style='text-align: center;'>三级编号</td></tr><tr><td style='text-align: center;'>tech_ptname</td><td style='text-align: center;'>三级题目</td></tr><tr><td style='text-align: center;'>tech_ptbody</td><td style='text-align: center;'>技术内容</td></tr><tr><td style='text-align: center;'>pic</td><td style='text-align: center;'>图表</td></tr><tr><td style='text-align: center;'>edit</td><td style='text-align: center;'>标准编制信息根元素</td></tr><tr><td style='text-align: center;'>mode</td><td style='text-align: center;'>编制修改类型（草案、征求意见、终稿）</td></tr><tr><td style='text-align: center;'>time</td><td style='text-align: center;'>编制修改时间</td></tr><tr><td style='text-align: center;'>expert</td><td style='text-align: center;'>专家信息</td></tr><tr><td style='text-align: center;'>ep_name</td><td style='text-align: center;'>专家姓名</td></tr><tr><td style='text-align: center;'>ep_company</td><td style='text-align: center;'>单位</td></tr><tr><td style='text-align: center;'>ep_contact</td><td style='text-align: center;'>联系方式</td></tr><tr><td style='text-align: center;'>execute</td><td style='text-align: center;'>标准实施信息根元素</td></tr><tr><td style='text-align: center;'>feedback</td><td style='text-align: center;'>标准实施反馈条目</td></tr><tr><td style='text-align: center;'>fb_source</td><td style='text-align: center;'>标准实施反馈来源</td></tr><tr><td style='text-align: center;'>fb_info</td><td style='text-align: center;'>标准实施反馈内容</td></tr></table>

附录 C

(资料性附录)

国家标准结构化标注实例

以下是对 GB/T 15799 结构化标注实例。

<?xml version="1.0" encoding="GB2312"?>
<standard>
<content>
<basic_info>
<cn>棉蚜测报技术规范</cn>
<en lang="en">
</cn>
</DATA>
<Rules for monitoring and forecast of the cotton aphid (Aphis gossypii Glover)
</DAT>
</en>
</ics>
</basic_info>
<auxiliary_info>
<preface>
<!-- [CDATA]
本标准代替 GB/T 15799—1995《棉蚜测报调查规范》。
a) 增加了棉蚜预测预报方法，标准名称《棉蚜测报调查规范》改为《棉蚜测报技术规范》；
b) 增加了“术语和定义”部分，其中定义了卷叶株和油斑株；
c) 以有翅蚜的调查代替原有翅成蚜和有翅若蚜的分别调查；
d) 早春基数调查中，减少草本寄主的调查数量，将“50 株～100 株”改为“50 株”；
e) “苗期蚜虫系统调查和伏期蚜虫系统调查”合并为“系统调查”；
f) “苗期蚜虫大田普查和伏期蚜虫大田普查”合并为“大田普查”；
g) 删除了苗期棉蚜种群结构调查；
h) 增加了系统调查田块数量；
i) 减少了普查苗期棉蚜的取样数量，将200 株改为100 株；
j) 删除了蚜害指数概念；
k) 增加了附录 B、附录 D、附录 E 和附录 G。
本标准的附录 A、附录 F、附录 G 为规范性附录，附录 B、附录 C、附录 D 和附录 E 为资料性附录。
本标准由中华人民共和国农业部提出并归口。
本标准起草单位：农业部全国农业技术推广服务中心。
本标准主要起草人：夏冰、姜京宇、姜玉英、赵文新、张祝华、朱先敏。
本标准所代替标准的历次版本发布情况为：
—— GB/T 15799—1995。

</preface>
</scope>
</CDATA>
本标准规定了早春虫源基数调查、系统调查、大田普查、天敌调查、预测方法、发生程度和为害损失的统计和历年测报资料统计汇总汇报方法等方面的技术和方法。
本标准适用于棉蚜测报调查和预报。

]]>

</scope>

<appendix>

<apd_item>

<apd_id>附录 A</apd_id>

<apd_body>

<!-- [CDATA]

（规范性附录）

农作物病虫调查资料表册

】>

</apd_body>

<pic src="./pic/001.jpg" />

<pic src="./pic/002.jpg" />

<pic src="./pic/003.jpg" />

<pic src="./pic/004.jpg" />

<pic src="./pic/005.jpg" />

<pic src="./pic/006.jpg" />

<pic src="./pic/007.jpg" />

<pic src="./pic/008.jpg" />

</apd_item>

<apd_item>

<apd_id>附录 B</apd_id>

<apd_body>

<!-- [CDATA] 格式统一

（资料性附录）--（进行技术性处理，避免歧义）

棉蚜发生为害期的划分

棉蚜全年的发生危害期统一划分为两个阶段，即苗期棉蚜和伏期棉蚜，简称苗蚜伏蚜；苗期棉蚜又分为三叶前期和四叶后期（三叶期过后至现蕾前）。

】>

</apd_body>

</apd_item>

<apd_item>

<apd_id>附录 C</apd_id>

<apd_body>

<!-- [CDATA]

（资料性附录）

棉蚜天敌单位的换算

异色瓢虫（Leis axyridis（pallas））、七星瓢虫（Coccinella septempunctata L.）、

十三星瓢虫（Hippodamia tridecipunctata（L.））等，食蚜量大的瓢虫成、幼虫都以1个虫体作为1个天敌单位。

龟纹瓢虫（Propylaea japonica Thunberg）、多异瓢虫（Adonia rariegata Goeze）的成、幼虫，大草蛉（Chrysopa septempunctata Wesmael）、中华草蛉（Chrysopa sinica Tjeder）的幼虫，食蚜蝇（Epistrophe balteata De Geer）的幼虫，拟环纹狼蛛（Lycosa pseudoannulata Boer, et str.）以2个虫体为1个天敌单位。

黑襟毛瓢虫（Scymnus（Neopullus）hoffmanni Weise）成、幼虫，草间小黑蛛[Erigonidium graminicolum（Sundevall）]等一般食蚜量的蜘蛛以4个虫体为1个天敌单位。

小花蝽（Orius minutus Linnaeus）、大眼长蝽（Geocoris pallidipennis Costa）以10个虫体为1个天敌单位。

被寄生蜂寄生的蚜虫以120头僵蚜为1个天敌单位。

】>

</apd_body>

</apd_item>

〈apd_item〉
〈apd_id〉附录 D〈/apd_id〉
〈apd_body〉
〈! [DATA[(资料性附录)

气候影响指标

7月上、中旬降雨次数少。旬降雨量为20 mm以下，晴雨次数频繁，相对湿度为55%~85%时，伏蚜将高速增殖，猖獗发生。

7月上、中旬无雨，温度持续高达30℃以上；或旬内降雨日数多于晴天数，旬雨量约为60 mm，相对湿度达90%左右时；伏蚜增殖下降，不会形成猖獗发生。

7月上、中旬连续降雨达5天，旬雨量60 mm以上，相对湿度80%~90%时，蚜霉菌开始侵染流行，伏蚜群体基数下降。

▶▶
〈/apd_body〉
〈/apd_item〉
〈apd_item〉
〈apd_id〉附录 E〈/apd_id〉
〈apd_body〉
〈! [DATA[(资料性附录)

部分省份棉花产量损失率计算公式

▶▶〉
〈/apd_body〉
〈pic src=. /pic/009.jpg" /〉
〈/apd_item〉
〈apd_item〉
〈apd_id〉附录 F〈/apd_id〉
〈apd_body〉
〈! [DATA[(资料性附录)

农作物病虫测报资料统计(汇总)表册

▶▶〉
〈/apd_body〉
〈pic src=. /pic/010.jpg" /〉
〈pic src=. /pic/011.jpg" /〉
〈pic src=. /pic/012.jpg" /〉
〈pic src=. /pic/013.jpg" /〉
〈pic src=. /pic/014.jpg" /〉
〈pic src=. /pic/015.jpg" /〉
〈pic src=. /pic/016.jpg" /〉
〈pic src=. /pic/017.jpg" /〉
〈/apd_item〉
〈apd_item〉
〈apd_id〉附录 E〈/apd_id〉
〈apd_body〉
〈! [DATA[(资料性附录)

部分省份棉花产量损失率计算公式

▶▶〉

</apd_body>

<pic src=.//pic/009.jpg" />

</apd_item>

<apd_item>

<apd_id>附录 G</apd_id>

<apd_body>

<!-- [DATA]

（资料性附录）

棉蚜发生情况模式报表

】>

</apd_body>

<pic src=.//pic/018.jpg" />

<pic src=.//pic/019.jpg" />

<pic src=.//pic/020.jpg" />

</apd_item>

</appendix>

</auxiliary_info>

<term>

<t_item>

<t_id>2.1</t_id>

<t_cn>卷叶株</t_cn>

<t_en lang="en">leaf roll plant</t_en>

<t_def>

<!-- [DATA]

因蚜虫为害，造成叶片内卷 1/2 的棉株为卷叶株。

】>

</t_def>

</t_item>

<t_item>

<t_id>2.2</t_id>

<t_cn>油斑株</t_cn>

<t_en lang="en">oil spot plant</t_en>

<t_def>

<!-- [DATA]

因蚜虫为害，造成植株中上部叶片有油斑的棉株为油斑株。

】>

</t_def>

</t_item>

</term>

<technology>

<tech_item>

<tech_itid>3</tech_itid>

<tech_itname>早春虫源基数调查</tech_itname>

<tech_paragraph>

<tech_paraid>3.1</tech_paraid>

<tech_paraname>调查时间</tech_paraname>

<tech_part>

<tech_ptid />

<tech_ptname />

</tech_part>

</tech_itid>

</tech_item>

</tech_part>

</term>

</cata>

<tech_ptbody>
    <!-- CDATA[
        棉花播种和有翅蚜大量出现以前分别调查一次，共调查两次。
    ]-->
    <tech_ptbody>
        <tech_part>
            <tech_paragraph>
                <tech_paragraph>
                    <tech_paraid>3.2</tech_paraid>
                    <tech_paraname>调查寄主</tech_paraname>
                    <tech_part>
                        <tech_ptid />
                    </tech_ptname />
                </tech_ptbody>
            </tech_paraname>
        </tech_paraname>
    </tech_part>
</tech_ptbody>

在以木本寄主为主的地区，选择花椒、石榴、木槿等越冬寄主进行调查；在以草本寄主为主的地区，主要对夏至草进行调查。

</tech_ptbody>

</tech_part>

</tech_paragraph>

<tech_paragraph>
    <tech_paraid>3.3</tech_paraid>
    <tech_paraname>调查方法</tech_paraname>
    <tech_part>
        <tech_ptid />
        <tech_ptname />
    </tech_ptbody>
</tech_paraname>

调查木本寄主，每种寄主固定两株，每株在东、西、南、北、中五个部位，各选15cm枝条一个，记载有蚜枝数、有翅蚜和无翅蚜，计算有蚜枝率、平均单枝蚜量，结果记入表A.1。调查草本寄主，共调查50株，计算有蚜株率和平均每株蚜量，结果记入表A.2。

</tech_ptbody>

</tech_part>

</tech_paragraph>

</tech_item>

<tech_item>
    <tech_itid>4</tech_itid>
    <tech_itname>系统调查</tech_itname>
    <tech_paragraph>
        <tech_paraid>4.1</tech_paraid>
        <tech_paraname>苗期棉蚜系统调查</tech_paraname>
        <tech_part>
            <tech_ptid>4.1.1</tech_ptid>
            <tech_ptname>调查时间</tech_ptname>
            <tech_ptbody>
                <!-- CDATA[
                    棉苗出土后至苗期棉蚜（参见附录B）为害末期。
                </tech_ptbody>
            </tech_paraname>
        </tech_part>
    </tech_ptid>
    <tech_ptname>调查时间</tech_ptname>
    <tech_ptbody>
        <!-- CDATA[
            棉苗出土后至苗期棉蚜（参见附录B）为害末期。
            </tech_ptbody>
        </tech_paraname>
    </tech_part>
</tech_part>

]]>

</tech_ptbody>

</tech_part>

<tech_part>

<tech_ptid>4.1.2</tech_ptid>

<tech_ptname>调查田块</tech_ptname>

<tech_ptbody>

<!-- [CDATA]

结合棉花前茬作物，选择具代表性的一类、二类、三类棉田各三块，发生期不施药或很少施药。

-->

</tech_ptbody>

</tech_part>

<tech_part>

<tech_ptid>4.1.3</tech_ptid>

<tech_ptname>调查方法</tech_ptname>

<tech_ptbody>

<!-- [CDATA]

每块田采取5点取样法，定苗前每点查40株，定苗后每点查20株，每5天调查一次全株蚜量，计算蚜株率和百株蚜量。当出现棉花卷叶时，同时调查卷叶株数，计算卷叶株率。调查结果记入表A.3。

-->

</tech_ptbody>

</tech_part>

<tech_part>

</tech_ptid>

<tech_ptname>调查时间</tech_ptname>

<tech_ptbody>

<!-- [CDATA]

自伏期棉蚜（参见附录B）为害期开始至伏期棉蚜为害末期。

-->

</tech_ptbody>

</tech_part>

<tech_part>

<tech_ptid>4.2.2</tech_ptid>

<tech_ptname>调查田块</tech_ptname>

<tech_ptbody>

<!-- [CDATA]

一类、二类棉田各三块，发生期不施药或很少施药。

-->

</tech_ptbody>

</tech_part>

<tech_part>

<tech_ptid>4.2.3</tech_ptid>

<tech_ptname>调查方法</tech_ptname>

<tech_ptbody>

<!-- [CDATA]

每块田采取5点取样，每点10株，每5天调查一次。调查每株查主茎的上、中、下3片叶蚜量、蚜霉菌寄生情况、油斑株数、卷叶株，并计算蚜株率、百株三叶蚜量、百株三叶感染蚜霉菌蚜虫数，油斑株率和卷叶株率。结果记入表A.4。

</tech_ptbody>
</tech_part>
</tech_paragraph>
</tech_item>
<tech_item>
<tech_itid>5</tech_itid>
<tech_itname>大田普查</tech_itname>
<tech_paragraph>
<tech_paraid>5.1</tech_paraid>
<tech_paraname>普查时间</tech_paraname>
<tech_part>
<tech_ptid/>
<tech_ptname/>
<tech_ptbody>
</tech_ptbody>
</DATA>

在苗期和伏期系统调查田蚜量达到防治指标时开展普查，未防治棉田在棉蚜高峰期进行普查。

</tech_ptbody>
</tech_part>
</tech_paragraph>
<tech_paragraph>
<tech_paraid>5.2</tech_paraid>
<tech_paraname>普查田块</tech_paraname>
<tech_part>
<tech_ptid/>
<tech_ptname/>
<tech_ptbody>
</tech_ptbody>
</DATA>

根据当地栽培情况，按一类、二类、三类棉田比例选择有代表性的棉田10块以上。

</tech_ptbody>
</tech_part>
</tech_paragraph>
<tech_paragraph>
<tech_paraid>5.3</tech_paraid>
<tech_paraname>普查方法</tech_paraname>
<tech_part>
<tech_ptid/>
<tech_ptname/>
<tech_ptbody>
</tech_ptbody>
</DATA>

随机取样，苗期每块田调查100株，伏期每块田调查50株；调查计算有蚜株数、卷叶株数、油斑数、蚜株率、卷叶株率、油斑率和蚜田率。结果记入表A.5和表A.6。

</tech_ptbody>
</tech_part>

</tech_itid>

</tech_part>
<tech_part>
<tech_ptid>7.1.2</tech_ptid>
<tech_ptname>四叶后预测</tech_ptname>
<tech_ptbody>
</tech_ptbody>
</tech_part>
</tech_paragraph>
<tech_paragraph>
<tech_paraid>7.2</tech_paraid>
<tech_paraname>伏期棉蚜预测</tech_paraname>
<tech_part>
<tech_ptid/>
<tech_ptname/>
<tech_ptbody>
！[CDATA]
根据7月~8月份气象预报，对比历年资料，应用多种预报方法做出预报。
</tech_ptid>
</tech_part>
</tech_paragraph>
</tech_item>
<tech_item>
<tech_itid>8</tech_itid>
<tech_itname>发生程度和为害损失的统计</tech_itname>
<tech_paragraph>
<tech_paraid>8.1</tech_paraid>
<tech_paraname>发生量的表示</tech_paraname>
<tech_part>
<tech_ptid/>
<tech_ptname/>
<tech_ptbody>
！[CDATA]
早春数量以木本寄主平均15cm枝长蚜量和平均每株杂草蚜量表示。其他各期以平均最高百株蚜量和平均最高卷叶株率表示。
</tech_ptid>
</tech_part>
</tech_paragraph>
<tech_paraid>8.2</tech_paraid>
<tech_paraname>发生程度的划分原则</tech_paraname>
<tech_part>
<tech_ptid/>

<tech_ptname />
<tech_ptbody>
    <!-- [CDATA[
        发生程度分为 5 级，分别为轻发生（1 级）、偏轻发生（2 级）、中发生（3 级）、偏重发生（4 级）、大发生（5 级）。应以平均最高卷叶株率为主，结合百株蚜量进行统一划分。分级原则为：
—— 1 级：指受害密度以下的平均最高卷叶株率和百株蚜量；
—— 2 级：指介于 1 级和 3 级之间的卷叶株率和百株蚜量，上限一般是防治指标；
—— 3 级：指多年发生的卷叶株率和百株蚜量的平均值；
—— 4 级：指介于 3 级和 5 级之间的卷叶株率和百株蚜量；
—— 5 级：指该地区历史上一些最高年份卷叶株率和百株蚜量。
以平均最高卷叶株率和百株蚜量为基础，划分发生程度的其他方面还包括：平均最高百株蚜量、发生危害期持续时间的长短、应用农药防治面积占棉田总面积的比率、应防棉田平均用药次数。
</tech_ptbody>
</tech_part>
</tech_paragraph>
<tech_paragraph>
    <tech_paraid>8.3</tech_paraid>
    <tech_paraname>危害损失</tech_paraname>
    <tech_part>
        <tech_ptid>8.3.1</tech_ptid>
        <tech_ptname>皮棉危害产量损失率</tech_ptname>
    </tech_ptbody>
    <!-- [CDATA[
        即若不防治时，各期棉蚜所造成的皮棉产量损失率。本地建立产量损失计算模型的，可利用本地模型；本地没有建立产量损失计算模型的，可参照棉蚜发生情况相似地区的损失率模型。山东、河南省、河北省、安徽省、辽宁省测定公式参见附录 E。
    ]]>
    </tech_ptbody>
    </tech_part>
    <tech_ptid>8.3.2</tech_ptid>
    <tech_ptname>实际皮棉产量损失率</tech_ptname>
    <tech_ptbody>
        <!-- [CDATA[
            即统计防治后皮棉产量损失值，将防治后调查的棉田平均最高卷叶率（或平均单株蚜量）代入产量损失模型，求得实际皮棉产量损失率。
        ]]>
        </tech_ptbody>
    </tech_part>
    <tech_ptid>8.3.3</tech_ptid>
    <tech_ptname>挽回皮棉产量损失率</tech_ptname>
    <tech_ptbody>
        <!-- [CDATA[
            用不防治皮棉产量损失率减去防治田皮棉产量损失率求得。
        ]]>
        </tech_ptbody>
    </tech_part>
</tech_part>

<tech_part>
    <tech_ptid>8.3.4</tech_ptid>
    <tech_ptname>全年皮棉产值损失率</tech_ptname>
    <tech_ptbody>
        <!-- [DATA]
        全年皮棉产值损失率为各期皮棉产值损失率之和。以上结果记入表 A.8。
    -->
    <tech_ptbody>
        <tech_part>
            <tech_paragraph>
                <tech_item>
                    <tech_item>
                        <tech_itid>9</tech_itid>
                        <tech_itname>测报资料汇总和汇报</tech_itname>
                    </tech_itid>
                    <tech_paragraph>
                        <tech_paraid />
                        <tech_paraname />
                    </tech_part>
                    <tech_ptid />
                    <tech_ptname />
                </tech_ptid>
            </tech_ptbody>
        </tech_ptbody>
    </tech_part>
</tech_part>

## 參 考 文 献

[1] GB/T 15799 棉蚜测报技术规范