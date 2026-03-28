

# 中华人民共和国国家标准

GB/T 35397—2017

# 科技人才元数据元素集

# Research and development talent metadata element set

2017-12-29 发布

2018-04-01 实施

## 目 次

前言 …… III    
引言 …… IV    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 科技人才元数据元素集 …… 2    
4.1 概述 …… 2    
4.2 科技人才元数据核心元素集 …… 2    
4.3 科技人才元数据扩展元素集 …… 3    
4.4 科技人才元数据元素集扩展规则 …… 4    
4.5 科技人才元数据元素集扩展方法 …… 4    
附录 A（规范性附录） 科技人才元数据元素集数据字典 …… 5    
附录 B（规范性附录） 元数据元素扩展规则 …… 14    
附录 C（规范性附录） 元数据元素扩展方法 …… 15    
参考文献 …… 16

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国信息与文献标准化技术委员会(SAC/TC 4)提出并归口。

本标准起草单位：中国科学技术信息研究所、科技部科技人才交流开发服务中心、北京万方软件有限公司、山东省科学技术信息研究所、重庆科技信息研究所、天津市科学技术信息研究所。

本标准主要起草人：王运红、彭洁、吴广印、潘云涛、明正杰、曹凯、吴晓莉、苏成、赵筱媛、马峥、刘春燕、王莹、严利、李大玲、赵雪吉、王坚、曾令果。

## 引言

科技人才信息的开发和利用是科技人才管理的重要辅助手段。国外对于科技人才的信息化管理比较规范，我国的人才信息化管理起步比较晚，多是以省市、机构出于本单位的需求独自生产和管理，由此产生的科技人才数据有很大的差别。科技人才信息存在数据结构不统一，没有规范和标准等问题，这对于科技人才信息的开发、利用、共享都造成了一定的困难，需要对科技人才数据的描述进行规范。

本标准规范了科技人才必需要管理的信息项目和内容，是对科技人才信息最为基础的描述，并可以将本标准作为基础项目进行内容扩展。依照本标准建立的科技人才数据库，可以进行信息共享、交换和集成等业务。

本标准的目标是提供描述科技人才特征的结构，期望科技人才管理人员、科技人才信息分析人员能够有效地利用科技人才信息系统。本标准定义了元数据元素，提供了元数据模式，并确定了一组通用的元数据术语、定义和扩展方法。当科技人才数据生产者执行本标准时将：

——为数据生产者提供适当的说明科技人才数据的有关信息；

——简化科技人才数据元数据的组织和管理；

——使用户了解数据的基本特征，从而能够最有效地应用科技人才数据；

——使数据发现、检索和重复使用变得容易；

——用户能更好地访问、评价、共享和使用科技人才数据；

——使用户能够决定他们是否使用已有的科技人才数据。

本标准中的数据表结构和标识符的使用，都基于国家现行有关标准，并尽量满足作为数据交换、共享、存储和维护的需要，是提高科技人才信息服务能力的重要基础。

# 科技人才元数据元素集

## 1 范围

本标准规定了科技人才数据库的基本元数据元素，并扩展其他必要的表结构和数据项。本标准仅仅是科技人才元数据的元素集合，基于特定项目或应用的需要明确规定这些元素的使用。

本标准适用于不同领域的科技人才信息资源描述，也适用于不同层次的科技人才信息资源描述。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2260 中华人民共和国行政区划代码

GB/T 2261.1 个人基本信息分类与代码 第1部分：人的性别代码

GB/T 2659 世界各国和地区名称代码

GB/T 3792.2 普通图书著录规则

GB/T 4658 学历代码

GB/T 6864 中华人民共和国学位代码

GB/T 7408—2005 数据元和交换格式 信息交换 日期和时间表示法

GB/T 8561 专业技术职务代码

GB/T 8563.1 奖励、纪律处分信息分类与代码 第 1 部分: 奖励代码

GB/T 8563.2 奖励、纪律处分信息分类与代码 第2部分：荣誉称号和荣誉奖章代码

GB/T 8563.3 奖励、纪律处分信息分类与代码 第 3 部分: 纪律处分代码

GB/T 13745 学科分类与代码

GB/T 25100 信息与文献 都柏林核心元数据元素集

JB/DM-BZKZY-2006 高等学校本、专科专业代码

JB/DM-HSSZY-2006 授予博士、硕士学位和培养研究生的学科、专业代码

ZC 0009—2012 专利文献著录项目标准

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

数据类型 data type

允许对域内的值进行操作的数据取值类型。

注：包括字符型、数值型、日期型、布尔型等。

3.2

## 元数据 metadata

关于数据的数据，主要是描述数据属性(property)的信息。

### 3.3 

元数据元素 metadata element

元数据的基本单元。

### 3.4 

## 科技人才 research and development talent; RDT

具有较高的专业知识、技术和才能，能够胜任某个指定的职责、工作或者角色的人。

[ISO 30400:2016, 定义 13.1]

注：“科技人才”是我国独有的概念，国际上与科技人才较为相关的概念主要包括“科技活动人员”“科学家”“工程师”“R&D人员”以及“科学工作者”等。

### 3.5 

## 科技人才信息 information of research and development talent

描述科技人才实体的信息集合。

注：科技人才信息包括：（1）科技人才的基本信息，包括姓名、性别、出生日期、国籍、学历、学位、研究方向、技术职称、联系方式等；（2）履历信息：包括工作履历、教育经历、职务、培训交流、奖励、荣誉、惩罚、科研项目等；（3）科研产出信息，主要包括出版专著、论文、专利情况等；（4）其他相关信息，包括专长、学术道德及科研信用信息等。

### 3.6 

## 科技人才 ID talentID

科技人才的唯一身份标识。

注：在本标准中是全局变量，是对科技人才重名的解决机制。

## 4 科技人才元数据元素集

### 4.1 概述

科技人才元数据元素集包括核心元素集和扩展元素集。核心元素描述了科技人才实体具有的公共属性和特有特征，扩展元素描述科技人才可以扩展的特征。

在表 1 和表 2 的元素描述中，每一个元素均有一个用于使用者阅读的描述性标签（“label”）和一个用于计算机处理的唯一标记（“name”，即元素名）。

### 4.2 科技人才元数据核心元素集

表 1 是科技人才元数据核心元素集，表 1 中的核心元素集在附录 A 的表 A.1 中详细说明。

在本标准中，元素名用小写英文字符表示，以便于计算机标记和编码，并保证与其他语种的应用保持语义一致性；标签为中文，便于人们阅读。本标准中的标签只是元素名称的一个语义属性，在具体的应用领域，为突出科技人才资源的个性和元数据的专指性，更好的体现该元素名称在具体应用中的语义，允许赋予其适合的标签，但语义上与原始定义不允许有冲突，不允许扩大原始的语义。

<div style="text-align: center;">表 1 科技人才元数据核心元素描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素名</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>talentID</td><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>赋予科技人才的唯一标识符</td><td style='text-align: center;'>建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则。必选项</td></tr><tr><td style='text-align: center;'>name</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>科技人才的姓名全称</td><td style='text-align: center;'>科技人才的姓名全称，可以是中文，也可以是外文姓名。描述可以包括但不限于以下内容：姓名、曾用名、外文名、或者关于科技人才的多姓名描述。必选项</td></tr></table>

<div style="text-align: center;">表 1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素名</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>gender</td><td style='text-align: center;'>性别</td><td style='text-align: center;'>科技人才的性别属性</td><td style='text-align: center;'>采用国标编码体系：见 GB/T 2261.1，必选项</td></tr><tr><td style='text-align: center;'>birthdate</td><td style='text-align: center;'>出生日期</td><td style='text-align: center;'>科技人才出生日期</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD。信息不全的日期建议采集到年份。必选项</td></tr><tr><td style='text-align: center;'>nationality</td><td style='text-align: center;'>国籍</td><td style='text-align: center;'>科技人才的国籍</td><td style='text-align: center;'>指科技人才持有护照的国家，科技人才为该国的合法公民。可以包括但不限于以下内容：目前国籍、曾经国籍、以及科技人才的双重国籍身份描述。见 GB/T 2659，必选项</td></tr><tr><td style='text-align: center;'>researchField</td><td style='text-align: center;'>研究方向</td><td style='text-align: center;'>研究方向</td><td style='text-align: center;'>包括描述科技人才学习或者从事的研究方向，可以多值，用“；”分隔。可以自建受控词表，用于检索、分类统计和同行识别。必选项</td></tr><tr><td style='text-align: center;'>degree</td><td style='text-align: center;'>最高学位</td><td style='text-align: center;'>获得的最高学位</td><td style='text-align: center;'>科技人才获得的最高学位，见 GB/T 6864。可选项</td></tr><tr><td style='text-align: center;'>educationalLevel</td><td style='text-align: center;'>最高学历</td><td style='text-align: center;'>获得的最高学历</td><td style='text-align: center;'>科技人才获得的最高学历，见 GB/T 4658。可选项</td></tr><tr><td style='text-align: center;'>professionalTitle</td><td style='text-align: center;'>专业技术职称</td><td style='text-align: center;'>科技人才目前获得的专业技术职称</td><td style='text-align: center;'>指经国务院人事主管部门授权的部门、行业或中央企业、省级专业技术职称评审机构评审的工程系列专业技术职称。见 GB/T 8561。可选项</td></tr><tr><td style='text-align: center;'>contact</td><td style='text-align: center;'>联系方式</td><td style='text-align: center;'>科技人才的联系方式</td><td style='text-align: center;'>科技人才的当前有效联系方式，包括：通讯地址、邮政编码、电话、传真和电子信箱。可选项</td></tr><tr><td style='text-align: center;'>dataSource</td><td style='text-align: center;'>数据来源</td><td style='text-align: center;'>科技人才信息的起始来源</td><td style='text-align: center;'>科技人才数据的来源，如数据库地址或者 URL 地址，以便数据交换、信息共享和即时更新。可选项</td></tr></table>

### 4.3 科技人才元数据扩展元素集

科技人才元数据元素集标准扩展集描述了科技人才学习、工作和进修经历、参与科研项目、发表论文、发明专利等情况，是对人才管理和科研能力记录、评价、考核等应有和专有的内容。

表 2 是科技人才元数据元素集的扩展元素集，表 2 的元数据扩展元素已经对应到附录 A 的数据字典表号。

<div style="text-align: center;">表 2 科技人才元数据扩展元素描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素名</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>注释</td><td style='text-align: center;'>对应附录A的表号</td></tr><tr><td style='text-align: center;'>workExperience</td><td style='text-align: center;'>工作履历</td><td style='text-align: center;'>科技人才的工作经历</td><td style='text-align: center;'>描述科技人才的工作经历，包括但不限于以下内容：任职机构、开始时间、结束时间、职务、工作描述。（含海外）</td><td style='text-align: center;'>表A.2</td></tr><tr><td style='text-align: center;'>parttimeJob</td><td style='text-align: center;'>社会/学术任职</td><td style='text-align: center;'>科技人才在学术组织、社会团体等任职情况</td><td style='text-align: center;'>描述科技人才在重要的学术机构或社会团体的任职情况。包括但不限于以下内容：国家、组织/团体名称、开始时间、结束时间、职务、工作描述</td><td style='text-align: center;'>表A.3</td></tr><tr><td style='text-align: center;'>education</td><td style='text-align: center;'>教育经历</td><td style='text-align: center;'>指科技人才的教育经历</td><td style='text-align: center;'>描述科技人才获得学历学位的教育经历，建议大专以上教育起点。包括但不限于以下内容：就读院校、开始时间、结束时间、学习专业、获得学位。（含海外）</td><td style='text-align: center;'>表A.4</td></tr></table>

## 表 2（续）


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>元素名</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>注释</td><td style='text-align: center;'>对应附录A的表号</td></tr><tr><td style='text-align: center;'>training</td><td style='text-align: center;'>培训交流经历</td><td style='text-align: center;'>指科技人才的培训交流经历</td><td style='text-align: center;'>描述科技人才未获得学历学位的教育经历，包括但不限于以下内容：就读院校、开始时间、结束时间、学习专业或者内容、获得证书或者资质。（含海外）</td><td style='text-align: center;'>表A.5</td></tr><tr><td style='text-align: center;'>specialty</td><td style='text-align: center;'>专长</td><td style='text-align: center;'>指科技人才的技术等专长</td><td style='text-align: center;'>描述科技人才工作中的技术等专长，包括但不限于以下内容：专业技术、语言、水平等级</td><td style='text-align: center;'>表A.6</td></tr><tr><td style='text-align: center;'>prize</td><td style='text-align: center;'>奖励信息</td><td style='text-align: center;'>科技人才获得的奖励信息</td><td style='text-align: center;'>包括但不限于：奖励名称、授奖单位、等级、时间。见GB/T8563.1，自建词表可用于特定的科技奖励</td><td style='text-align: center;'>表A.7</td></tr><tr><td style='text-align: center;'>honor</td><td style='text-align: center;'>荣誉信息</td><td style='text-align: center;'>指科技人才获得的荣誉信息</td><td style='text-align: center;'>包括但不限于：荣誉名称、授予单位、时间。见GB/T8563.2，自建词表用于特定的科技奖荣誉</td><td style='text-align: center;'>表A.8</td></tr><tr><td style='text-align: center;'>punishment</td><td style='text-align: center;'>惩罚信息</td><td style='text-align: center;'>科技人才获得的惩罚信息</td><td style='text-align: center;'>包括但不限于：惩罚名称、授奖单位、等级、时间。见GB/T8563.3，可使用自建词表</td><td style='text-align: center;'>表A.9</td></tr><tr><td style='text-align: center;'>project</td><td style='text-align: center;'>参与课题项目</td><td style='text-align: center;'>科技人才参与或主持的项目信息</td><td style='text-align: center;'>包括但不限于：项目名称、级别、分类、参与角色</td><td style='text-align: center;'>表A.10</td></tr><tr><td style='text-align: center;'>book</td><td style='text-align: center;'>出版专著</td><td style='text-align: center;'>科技人才出版的专著或者编著图书信息</td><td style='text-align: center;'>见GB/T3792.2进行描述</td><td style='text-align: center;'>表A.11</td></tr><tr><td style='text-align: center;'>paper</td><td style='text-align: center;'>发表论文</td><td style='text-align: center;'>科技人才在国内刊物发表文献信息</td><td style='text-align: center;'>指在国内学术期刊上发表的文献信息，见GB/T25100，并可进行扩展</td><td style='text-align: center;'>表A.12</td></tr><tr><td style='text-align: center;'>patent</td><td style='text-align: center;'>发明专利</td><td style='text-align: center;'>科技人才发明专利情况</td><td style='text-align: center;'>描述科技人才发明的专利，包括中国专利局获得的专利。中国专利项目见ZC0009-2012。描述科技人才在海外获得审批的专利，包括欧专局和美专局等机构获得的专利。可参照WIPO ST.36，或者美专局的标准</td><td style='text-align: center;'>表A.13</td></tr><tr><td style='text-align: center;'>STReport</td><td style='text-align: center;'>科技报告</td><td style='text-align: center;'>科技人才参与撰写的科技报告</td><td style='text-align: center;'>科技人才参与撰写的科技报告</td><td style='text-align: center;'>表A.14</td></tr><tr><td style='text-align: center;'>researchIntegrity</td><td style='text-align: center;'>科研诚信</td><td style='text-align: center;'>科技人才在科研活动和学术研究中的诚信记录</td><td style='text-align: center;'>描述科技人才在科学研究、项目申报、学术活动中的诚信情况记录，主要记录学术道德上发生的不端行为和结果，为科技人才在科研活动中的管理和其他工作提供参考</td><td style='text-align: center;'>表A.15</td></tr></table>

### 4.4 科技人才元数据元素集扩展规则

用户定义的元数据按照附录 B 和附录 C 进行扩展定义和描述。

附录 B 提供定义和应用补充元数据元素的规则，以便更好地满足特殊用户的需求。

任何与本标准一致的专用标准应当与附录 B 中的规则一致。

为使元数据元素能准确地描述元素实体，在附录 B 的数据字典中说明其域值的类型和约束。

任何扩展应用考虑在标准中说明元数据实体和元素是必选、条件必选或是可选。

### 4.5 科技人才元数据元素集扩展方法

附录 C 提供元数据元素扩展指导。应按照附录 C 说明的规则定义扩展的元数据元素。

## 附录 A

(规范性附录)

科技人才元数据元素集数据字典

科技人才元数据元素集数据字典见表 A.1～表 A.15。

<div style="text-align: center;">表 A.1 RDT_ResearcherInfo（基本信息表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则。科技人才ID为全局变量</td></tr><tr><td style='text-align: center;'>ORCID标识符</td><td style='text-align: center;'>ORCID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>ORCID注册系统里的标识符，用于和国际学术数据关联，可以将科技人才ID和ORCID标识符合并其一</td></tr><tr><td style='text-align: center;'>中文姓名</td><td style='text-align: center;'>A01_CnName</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>人才中文姓名，可能重名</td></tr><tr><td style='text-align: center;'>外文姓名</td><td style='text-align: center;'>A01_EnName</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>外文名，可能重名，可以多值，用“；”分隔</td></tr><tr><td style='text-align: center;'>性别</td><td style='text-align: center;'>A01_Gender</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>该人基本生理特征，见GB/T2261.1—2003，取值：0—未知；1—男；2—女；9—不确定</td></tr><tr><td style='text-align: center;'>出生日期</td><td style='text-align: center;'>A01_Birthdate</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见GB/T7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>国籍</td><td style='text-align: center;'>A01_Nationality</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才持有护照的国家，科技人才为该国的合法公民。可以包括但不限于以下内容：目前国籍、曾经国籍、以及科技人才的双重国籍身份描述。见GB/T2659</td></tr><tr><td style='text-align: center;'>研究方向</td><td style='text-align: center;'>A01_ResearchField</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>包括描述科技人才学习或者从事的研究方向，可以多值，用“；”分隔。可以自建受控词表，用于检索、分类统计和同行识别</td></tr><tr><td style='text-align: center;'>最高学位</td><td style='text-align: center;'>A01_Degree</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才获得的最高学位，见GB/T6864</td></tr><tr><td style='text-align: center;'>最高学历</td><td style='text-align: center;'>A01_EducationalLevel</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才获得的最高学历，见GB/T4658</td></tr><tr><td style='text-align: center;'>专业技术职称</td><td style='text-align: center;'>A01_ProfessionalTitle</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>专业技术职称，记录最高职称，可以多值，用“；”分隔；见GB/T8561</td></tr><tr><td style='text-align: center;'>人才简介</td><td style='text-align: center;'>A01_Introduction</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>人才简介</td></tr><tr><td style='text-align: center;'>技术类型</td><td style='text-align: center;'>A01_Type</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>根据知识、技术或工作性质划分的科技人才类型，如：基础研究型、应用研发型、工程技术型、财务专家、法律专家、战略专家、管理专家等。可以多值，用“；”分隔。可以自建受控词表，用于检索、分类统计和同行识别</td></tr><tr><td style='text-align: center;'>生存状态</td><td style='text-align: center;'>A01_Survival</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>1—在世，0—已故，NULL—未知</td></tr><tr><td style='text-align: center;'>个人主页</td><td style='text-align: center;'>A01_website</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才的个人网页</td></tr></table>

<div style="text-align: center;">表 A.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>通讯地址</td><td style='text-align: center;'>A01_Address</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>通讯地址，可以多值，用“；”分隔</td></tr><tr><td style='text-align: center;'>邮编</td><td style='text-align: center;'>A01_ZipCode</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才通讯地址所在地的邮政编码</td></tr><tr><td style='text-align: center;'>电话</td><td style='text-align: center;'>A01_Tel</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>电话，可以多值，用“；”分隔</td></tr><tr><td style='text-align: center;'>传真</td><td style='text-align: center;'>A01_Fax</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>传真，可以多值，用“；”分隔</td></tr><tr><td style='text-align: center;'>E-mail</td><td style='text-align: center;'>A01_Email</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>电子邮箱，可以多值，用“；”分隔</td></tr><tr><td style='text-align: center;'>数据来源</td><td style='text-align: center;'>A01_DataSource</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才数据的来源，如数据库地址或者URL地址，以便数据交换、信息共享和即时更新。自建数据库建议用特殊字符标识，如“自建”</td></tr></table>

<div style="text-align: center;">表 A.2 RDT WorkExperience（工作履历表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A02_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>工作履历记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则。可作为外键关联</td></tr><tr><td style='text-align: center;'>工作单位</td><td style='text-align: center;'>A02_Organization</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>服务工作单位</td></tr><tr><td style='text-align: center;'>工作内容</td><td style='text-align: center;'>A02_Responsibility</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>工作内容</td></tr><tr><td style='text-align: center;'>职务</td><td style='text-align: center;'>A02_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>职务</td></tr><tr><td style='text-align: center;'>工作所在国家</td><td style='text-align: center;'>A02_Country</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>条件可选</td><td style='text-align: center;'>工作单位所在国家，见GB/T 2659；当为国外机构时，可标明</td></tr><tr><td style='text-align: center;'>国内地区</td><td style='text-align: center;'>A02_Area</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>工作单位所在国内地区，见GB/T 2260</td></tr><tr><td style='text-align: center;'>工作单位类型</td><td style='text-align: center;'>A02_OrgType</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>是</td><td style='text-align: center;'>工作单位类型，可以自建受控词表，用于检索和分类统计，如：高等学校、研究机构、企业、其他</td></tr><tr><td style='text-align: center;'>入职时间</td><td style='text-align: center;'>A02_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>离职时间</td><td style='text-align: center;'>A02_DismissionTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>技术领域</td><td style='text-align: center;'>A02_Field</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>从事工作和研究的技术领域，可以多值，用“；”分隔。可以自建受控词表，用于检索和分类统计</td></tr></table>

<div style="text-align: center;">表 A.3 RDT_PartTimeJob（社会/学术任职表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A03_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>社会/学术任职信息记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>任职单位</td><td style='text-align: center;'>A03_Organization</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>兼任学术机构或社会团体的单位名称，含学会和协会</td></tr><tr><td style='text-align: center;'>职务</td><td style='text-align: center;'>A03_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>该人担任的社会职务或者学术任职的具体名称</td></tr><tr><td style='text-align: center;'>起始时间</td><td style='text-align: center;'>A03_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>A03_DismissionTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.4 RDT_Educaiton（教育经历表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A04_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>学习经历记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>毕业院校名称</td><td style='text-align: center;'>A04_Institute</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>毕业院校名称</td></tr><tr><td style='text-align: center;'>毕业院系名称</td><td style='text-align: center;'>A04_Department</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>毕业院校的院系名称</td></tr><tr><td style='text-align: center;'>学科</td><td style='text-align: center;'>A04_Subject</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>学科编码，可以多值，用分号（中英文均可）分隔；见GB/T 13745</td></tr><tr><td style='text-align: center;'>专业名称</td><td style='text-align: center;'>A04_CnSpecialty</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>该人取得学历所学专业的分类，见JB/DM-BZKZY-2006或JB/DM-HSSZY-2006</td></tr><tr><td style='text-align: center;'>学位名称</td><td style='text-align: center;'>A04_Degree</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>获得学位，见GB/T 6864</td></tr><tr><td style='text-align: center;'>学历名称</td><td style='text-align: center;'>A04_Education</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>由国家认可的该人在国内、外各类教育机构接受正式教育并取得学历证书的学习经历名称。见GB/T 4658</td></tr><tr><td style='text-align: center;'>入学时间</td><td style='text-align: center;'>A04_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>该人取得学历学习的起始日期，见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>毕业时间</td><td style='text-align: center;'>A04_GraduateTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>该人完成学历教育并获得证书的日期，见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.5 RDT_Training（培训交流经历表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A05_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>进修经历记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>培训内容</td><td style='text-align: center;'>A05_Content</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>参与培训或者进修的学习内容</td></tr><tr><td style='text-align: center;'>培训机构</td><td style='text-align: center;'>A05_Organization</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>进修机构</td></tr><tr><td style='text-align: center;'>开始时间</td><td style='text-align: center;'>A05_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>培训开始时间，见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>A05_EndTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>培训结束时间，见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>证书名称</td><td style='text-align: center;'>A05_Certificate</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>获取证书</td></tr></table>

<div style="text-align: center;">表 A.6 RDT_Specialty（专长表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A06_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专长的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>专长名称</td><td style='text-align: center;'>A06_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专长名称，包括计算机、外语等能力</td></tr><tr><td style='text-align: center;'>熟练程度</td><td style='text-align: center;'>A06_Level</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>掌握熟练程度，取值范围：精通、熟练、一般或等级</td></tr></table>

<div style="text-align: center;">表 A.7 RDT_Prize(奖励信息表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A07_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>奖励记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>奖励名称</td><td style='text-align: center;'>A07_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>奖励的全称</td></tr><tr><td style='text-align: center;'>授予机构</td><td style='text-align: center;'>A07_Organization</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>授予机构</td></tr><tr><td style='text-align: center;'>获得时间</td><td style='text-align: center;'>A07_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.7 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>A07_EndTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD, 例如: 1980-01-01。信息不全的日期建议采集到年份, 采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>奖励级别</td><td style='text-align: center;'>A07_Level</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>奖励级别</td></tr><tr><td style='text-align: center;'>奖励原因</td><td style='text-align: center;'>A07_Reason</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>获奖原因</td></tr><tr><td style='text-align: center;'>内容</td><td style='text-align: center;'>A07_Content</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>奖励内容</td></tr></table>

<div style="text-align: center;">表 A.8 RDT_Honor（荣誉信息表）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A08_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>荣誉记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>荣誉名称</td><td style='text-align: center;'>A08_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>荣誉名称</td></tr><tr><td style='text-align: center;'>授予机构</td><td style='text-align: center;'>A08_Organization</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>荣誉授予机构</td></tr><tr><td style='text-align: center;'>获得时间</td><td style='text-align: center;'>A08_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>A08_EndTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.9 RDT_Punishment(惩罚信息表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A07_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>惩罚记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>惩罚名称</td><td style='text-align: center;'>A07_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>惩罚的全称</td></tr><tr><td style='text-align: center;'>惩罚原因</td><td style='text-align: center;'>A07_Reason</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>惩罚的原因</td></tr><tr><td style='text-align: center;'>惩罚机构</td><td style='text-align: center;'>A07_Organization</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>惩罚的机构</td></tr></table>

<div style="text-align: center;">表 A.9 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>获得时间</td><td style='text-align: center;'>A07_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD, 例如: 1980-01-01。信息不全的日期建议采集到年份, 采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>A07_EndTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD, 例如: 1980-01-01。信息不全的日期建议采集到年份, 采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.10 RDT Project(参与课题项目表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A10_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>项目唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>项目名称</td><td style='text-align: center;'>A10_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>项目或课题的规范名称</td></tr><tr><td style='text-align: center;'>项目编号</td><td style='text-align: center;'>A10_Number</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>项目或课题编号</td></tr><tr><td style='text-align: center;'>委托单位</td><td style='text-align: center;'>A10_Principal</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>委托单位</td></tr><tr><td style='text-align: center;'>承担单位</td><td style='text-align: center;'>A10_CommitUnit</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>承担单位</td></tr><tr><td style='text-align: center;'>项目类别</td><td style='text-align: center;'>A10_Type</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>可以自建受控词表，用于检索、分类统计</td></tr><tr><td style='text-align: center;'>项目简介</td><td style='text-align: center;'>A10_Introduction</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>项目或课题简介</td></tr><tr><td style='text-align: center;'>项目领域</td><td style='text-align: center;'>A10_Fields</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>项目或课题所在的领域，多领域可用“；”分割</td></tr><tr><td style='text-align: center;'>承担角色</td><td style='text-align: center;'>A10_Role</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>该人项目或课题中所负责任和所起的实际作用</td></tr><tr><td style='text-align: center;'>排序</td><td style='text-align: center;'>A10_Order</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>承担该项目或课题的承担人排序号</td></tr><tr><td style='text-align: center;'>开始时间</td><td style='text-align: center;'>A10_StartTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>A10_EndTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.11 RDT Book(专著表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A11_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专著唯一标识</td></tr><tr><td style='text-align: center;'>DOI</td><td style='text-align: center;'>A11_DOI</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>数字对象标识，如果没有则不填写</td></tr></table>

<div style="text-align: center;">表 A.11(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>专著名称</td><td style='text-align: center;'>A11_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专著名称</td></tr><tr><td style='text-align: center;'>内容简介</td><td style='text-align: center;'>A11_Introduction</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>内容简介</td></tr><tr><td style='text-align: center;'>作者</td><td style='text-align: center;'>A11_Author</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>作者姓名，多个作者用“；”分割</td></tr><tr><td style='text-align: center;'>作者次序</td><td style='text-align: center;'>A11_AuthorOrder</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才的署名次序</td></tr><tr><td style='text-align: center;'>出版时间</td><td style='text-align: center;'>A11_PublishDate</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>出版语言</td><td style='text-align: center;'>A11_PublishLanguage</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>出版语言</td></tr><tr><td style='text-align: center;'>出版单位</td><td style='text-align: center;'>A11_Publisher</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>出版单位</td></tr><tr><td style='text-align: center;'>页数</td><td style='text-align: center;'>A11_Pages</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>页数</td></tr><tr><td style='text-align: center;'>ISBN</td><td style='text-align: center;'>A11_ISBN</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>出版书籍的ISBN号</td></tr></table>

<div style="text-align: center;">表 A.12 RDT_Paper(论文表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A12_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>论文表唯一标识</td></tr><tr><td style='text-align: center;'>DOI</td><td style='text-align: center;'>A12_DOI</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>数字对象标识，如果没有则不填写</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>作者</td><td style='text-align: center;'>A12_Author</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>作者的姓名，多个作者用“；”分割</td></tr><tr><td style='text-align: center;'>作者次序</td><td style='text-align: center;'>A12_AuthorOrder</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才的作者署名次序</td></tr><tr><td style='text-align: center;'>刊名</td><td style='text-align: center;'>A12_JournalName</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>刊名</td></tr><tr><td style='text-align: center;'>题名</td><td style='text-align: center;'>A12_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>发表的论文的题名</td></tr><tr><td style='text-align: center;'>中文摘要</td><td style='text-align: center;'>A12_AbstractCN</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>论文的中文摘要</td></tr><tr><td style='text-align: center;'>英文摘要</td><td style='text-align: center;'>A12_AbstractEN</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>论文的英文摘要</td></tr><tr><td style='text-align: center;'>关键词</td><td style='text-align: center;'>A12_Keyword</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>关键词</td></tr><tr><td style='text-align: center;'>年</td><td style='text-align: center;'>A12_Year</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>刊物出版的年份，见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr></table>

<div style="text-align: center;">表 A.12 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>卷</td><td style='text-align: center;'>A12_Volume</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>刊物卷号</td></tr><tr><td style='text-align: center;'>期</td><td style='text-align: center;'>A12_Period</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>刊物期号</td></tr><tr><td style='text-align: center;'>页码</td><td style='text-align: center;'>A12_Pages</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>论文的页码</td></tr><tr><td style='text-align: center;'>中图分类号</td><td style='text-align: center;'>A12_CLCNumber</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>中图分类号</td></tr><tr><td style='text-align: center;'>基金项目</td><td style='text-align: center;'>A12_FoundProject</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>支持论文的基金项目</td></tr><tr><td style='text-align: center;'>被引频次</td><td style='text-align: center;'>A12_TotalCites</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>该篇论文的总被引频次</td></tr></table>

<div style="text-align: center;">表 A.13 RDT_Patent(专利表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A13_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专利唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>专利名称</td><td style='text-align: center;'>A13_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>获取专利证书签发的专利名称</td></tr><tr><td style='text-align: center;'>专利简介</td><td style='text-align: center;'>A13_Introduction</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专利简介</td></tr><tr><td style='text-align: center;'>专利类型</td><td style='text-align: center;'>A13_Type</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专利类型，建议取值范围：发明专利、实用新型专利、外观设计专利</td></tr><tr><td style='text-align: center;'>专利分类</td><td style='text-align: center;'>A13_classification</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>申请的专利分类，中国专利采用IPC。在海外获得审批的专利，包括欧专局和美专局等机构获得的专利，可参照WIPO ST.36，或者美专局的标准</td></tr><tr><td style='text-align: center;'>专利号</td><td style='text-align: center;'>A13_Code</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>申请(专利)号</td></tr><tr><td style='text-align: center;'>专利权人</td><td style='text-align: center;'>A13_Patentee</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>享有该项专利权的所有专利权人姓名，多人用“；”隔开</td></tr><tr><td style='text-align: center;'>排序</td><td style='text-align: center;'>A13_Order</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>在该项专利中的专利权人中的排序号</td></tr><tr><td style='text-align: center;'>签发日期</td><td style='text-align: center;'>A13_CertificateDate</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>专利证书的签发日期，见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>批准机构</td><td style='text-align: center;'>A13_Authority</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>批准该专利的机构名称</td></tr><tr><td style='text-align: center;'>批准国别</td><td style='text-align: center;'>A13_AuthorityCountry</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>批准该专利的国家或地区代码，参照标准</td></tr><tr><td style='text-align: center;'>被引频次</td><td style='text-align: center;'>A13_TotalCites</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>该专利的总被引频次</td></tr></table>

<div style="text-align: center;">表 A.14 RDT_STReport(科技报告表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A14_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>科技报告的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>报告名称</td><td style='text-align: center;'>A14_Title</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>科技报告名称</td></tr><tr><td style='text-align: center;'>报告作者</td><td style='text-align: center;'>A14_Author</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>作者的姓名，多个作者用“；”分割</td></tr><tr><td style='text-align: center;'>作者次序</td><td style='text-align: center;'>A14_AuthorOrder</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技人才在该报告中的署名次序</td></tr><tr><td style='text-align: center;'>中文摘要</td><td style='text-align: center;'>A14_AbstractCN</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>中文摘要</td></tr><tr><td style='text-align: center;'>英文摘要</td><td style='text-align: center;'>A14_AbstractEN</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>英文摘要</td></tr><tr><td style='text-align: center;'>关键词</td><td style='text-align: center;'>A14_Code</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>科技报告的关键词</td></tr><tr><td style='text-align: center;'>编制时间</td><td style='text-align: center;'>A14_Date</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>专利证书的签发日期，见 GB/T 7408—2005 中 5.2.1.1 扩展表示法 YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>全文页数</td><td style='text-align: center;'>A14_Pageno</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>该科技报告的全文页数</td></tr><tr><td style='text-align: center;'>项目课题名称</td><td style='text-align: center;'>A14_Project</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>产生该科技报告的依托课题或者项目名称</td></tr></table>

<div style="text-align: center;">表 A.15 RDT_ResearchIntegrity(科研诚信表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>标识符</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>是否必选</td><td style='text-align: center;'>注释</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>A15_ID</td><td style='text-align: center;'>数值型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>诚信记录的唯一标识</td></tr><tr><td style='text-align: center;'>科技人才ID</td><td style='text-align: center;'>TalentID</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>指科技人才的唯一身份标识，是对科技人才重名的解决机制。建议采用符合规范标识体系的字符串进行标识，并使用全局统一的编码规则</td></tr><tr><td style='text-align: center;'>行为内容</td><td style='text-align: center;'>A15_Content</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>在科研和学术活动中发生的诚信问题的内容说明</td></tr><tr><td style='text-align: center;'>行为类型</td><td style='text-align: center;'>A15_Type</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>在科研和学术活动中发生的诚信问题的类型</td></tr><tr><td style='text-align: center;'>经办单位</td><td style='text-align: center;'>A15_HandlingOrg</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>对诚信问题进行处理的经办单位</td></tr><tr><td style='text-align: center;'>处理结果</td><td style='text-align: center;'>A15_Result</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>诚信问题的处理结果</td></tr><tr><td style='text-align: center;'>处理时间</td><td style='text-align: center;'>A15_ResultTime</td><td style='text-align: center;'>日期型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>处理结果发布时间，见GB/T 7408—2005中5.2.1.1扩展表示法YYYY-MM-DD，例如：1980-01-01。信息不全的日期建议采集到年份，采集不到信息用“9999”表示</td></tr><tr><td style='text-align: center;'>行为态度</td><td style='text-align: center;'>A15_manner</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>对诚信问题的后续态度</td></tr><tr><td style='text-align: center;'>有效期</td><td style='text-align: center;'>A15_ValidityPeriod</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>处理结果有效期限</td></tr></table>

# 附录 B

(规范性附录)

# 元数据元素扩展规则

### B.1 背景

本标准附录 A 的数据字典定义和域值尽可能通用，以满足不同学科对元数据元素的需求。然而，数据的多样性意味着通用元数据元素可能适应不了所有的应用。本附录提供定义和应用扩展元数据元素的规则，以更好地满足特殊用户的需求。

### B.2 扩展类型

允许下列扩展的类型：

a）增加新元数据元素子集；

b）建立新的元数据元素代码表，代替域值为“字符型”的现有元数据元素的域；

c） 创建新元数据代码表元素（扩展代码表）；

d）增加新元数据元素；

e） 对现有元数据元素施加更加严格的约束/条件；

f）对现有元数据元素的域施加更多限制。

### B.3 扩展的实施

在扩展元数据元素之前，应仔细地查阅本标准中现有的元数据元素，确认合适的元数据元素尚不存在。对于扩展的每一个元数据元素，应定义其名称、标识符、数据类型、定义、约束/条件等。

### B.4 扩展规则

a）扩展的元数据元素不应用来改变现有元数据元素的名称、定义或数据类型；

b）扩展的元数据元素可以定义为实体，可以包含扩展的和现有的元数据元素，作为其组成部分；

c) 允许对现有元数据元素施加比本标准要求更加严格的约束/条件（如：在本标准中是可选的元数据元素，在扩展后可以是必选的）；

d) 允许对元数据元素的域施加比本标准更严格的限制（如：本标准中域为“字符型”的元数据元素，在专用标准中可以限定为适当值的列表）；

e）允许对本标准认可的域值的使用加以限制（如：在本标准中现有元数据元素的域值有五个值，在扩展后可以规定它的域只包含其中三个值，要求用户从这三个域值中选择一个）；

f）允许对代码表中值的数目进行扩展；

g）不得扩展本标准不允许的任何内容。

# 附录 C

# (规范性附录)

# 元数据元素扩展方法

### C.1 元数据元素扩展方法

应按照以下 4 步骤定义扩展的元数据元素。

### C.2 现有元数据元素分析(步骤1)

扩展的第1步是保证只对本标准定义的标准集进行有效的扩展。应全面地分析元数据标准集和任何专用标准的正式文档/出版物。这种分析不仅要针对元数据元素的名称，还应分析定义、数据类型、约束/条件、域。现有的元素有可能满足要求而不需要新的元素。

如果能确认一个合适的元素，则应检查该元素与附录 A 的元素的关系，以保证该候选元素不被其他元素的排斥组合所排除。

方法：

如果

a）确认一个现有的元数据元素满足要求，则采用该现有元数据元素，无需扩展元数据；

b）确认一个现有的元数据元素的域，逻辑上可以通过对其现有的域“字符型”进行限定，以满足确定的需求，则进入步骤2；

c) 确认一个现有的元数据元素的域，逻辑上可以通过增加现有代码表的值进行扩展，以满足确定的需求，则进入步骤 3；

d）需要一个新的元数据元素以满足需求，且不能将现有元数据元素进行修改来满足该需求，则进入步骤4。

### C.3 定义新元数据元素代码表(步骤 2)

一个现有元数据元素是适合的，对其标识元素的域“字符型”加以限制，元数据标准现有的元数据代码表不能满足需求。在这种情况下，可以定义新的元数据元素代码表，以满足专用标准的特殊需求。

定义的新元数据元素代码表应与本标准规定的要求一致。

### C.4 扩展新元数据元素代码表（步骤 3）

对一个现有元数据元素的代码表进行扩展。新元数据代码表元素的定义应当与现有的元素集合相关。扩展的元数据代码表应是现有标准代码的逻辑扩展。

如果拟扩展的新元数据元素的域在逻辑上不是建立在原有域的基础上，标识的元素可能不适合扩展，应回到步骤1。

### C.5 定义新元数据元素(步骤 4)

元数据标准中现有的元数据元素不能满足需求。在这种情况下，可以定义新元数据元素，以满足专用标准的特殊需求。定义的新元数据元素应与本标准规定的要求一致。

## 參 考 文 献

[1] SL 453—2009 人才管理数据库表结构及标识符标准

[2] Jie PENG, Baoqiang QU, Haiyun CAO, et al. Construction and Application of Academic Identifier for Science and Technology Talent[C]. the proceeding of 2011 ICSTI public conference, Scientific Research Publishing, USA, 2011, 89-94

[3] 肖珑, 陈凌, 冯项云, 等. 中文元数据标准框架及其应用 [J]. 大学图书馆学报, 2001, 19(5): 29-35

[4] 毕强，朱亚玲．元数据标准及其互操作研究信息系统[J]，情报理论与实践，2007(5)，666-670

[5] 张晓林．开放元数据机制：理念与原则[J]．中国图书馆学报[J].2003,No.3.p9-14

[6] 肖珑, 冯项云, 沈芸芸. 描述元数据结构及其扩展规则研究 [J]. 现代图书情报技术, 2004 (9), 37(2): 5-7

[7] 黄如花，邱春艳．国内外科学数据元数据研究进展[J]，图书与情报，2014(6)102-108

[8] 刘飞, 黎建辉, 阎保平. XML 和 RDF 在科学数据库元数据标准建设中的应用 [J]. 微电子学与计算机, 2004(7): 127-131

[9] 金更达,何嘉荪. 电子文件元数据标准设计框架研究[J]. 档案与建设,2005(9),4-7

[10] 曹蓟光，王申康．元数据管理策略的比较研究[J]．计算机应用，2001(2)：2-5

[11] ISO 30400:2016 Human resource management—Vocabulary