

# 中华人民共和国国家标准

GB/T 40217—2021

# 财经信息技术 养老保险基金审计数据接口

# Financial information technology— Data interface of basic old-age insurance fund auditing

2021-05-21 发布

2021-12-01 实施

## 目次

前言 …… I    
引言 …… II    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 数据元 …… 2    
4.1 数据元的描述规则 …… 2    
4.2 数据元细目 …… 3    
5 接口文件的输出 …… 41    
5.1 输出文件的格式 …… 41    
5.2 输出文件的数据结构 …… 41    
5.3 输出文件的输出说明 …… 60    
5.4 输出文件的时间要求 …… 60    
6 符合性评价 …… 61    
附录 A（资料性附录） 养老保险基金审计数据接口的 XML 大纲 …… 62    
A.1 标准元素类型类 XML 大纲 …… 62    
A.2 单位信息类 XML 大纲 …… 83    
A.3 人员信息类 XML 大纲 …… 89    
A.4 参保信息类 XML 大纲 …… 104    
A.5 单位征缴类 XML 大纲 …… 129    
A.6 人员缴费类 XML 大纲 …… 146    
A.7 待遇支付类 XML 大纲 …… 171    
A.8 信息变更类 XML 大纲 …… 180    
A.9 参数类 XML 大纲 …… 189    
A.10 财务类 XML 大纲 …… 197    
附录 B（资料性附录） 养老保险基金审计数据接口的 XML 实例 …… 209    
B.1 单位信息类 XML 实例 …… 209    
B.2 人员信息类 XML 实例 …… 210    
B.3 参保信息类 XML 实例 …… 212    
B.4 单位缴费类 XML 实例 …… 215    
B.5 个人缴费类 XML 实例 …… 217    
B.6 待遇支付类 XML 实例 …… 220    
B.7 信息变更类 XML 实例 …… 221    
B.8 参数类 XML 实例 …… 222    
B.9 财务类 XML 实例 …… 224    
参考文献 …… 226

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由中华人民共和国审计署提出。

本标准由全国审计信息化标准化技术委员会(SAC/TC 341)归口。

本标准起草单位：中华人民共和国审计署、浙江省审计厅。

本标准主要起草人：文华宜、杨莉、吴星、陈焕昌、吕天阳、陈博、姜英杰、方宁、康延涛、刘晨赫、陈宁、邱文强、朱杰、金华振、童晓文、蒋晶波、陈康、徐康。

## 引言

党的十九大报告指出，“按照兜底线、织密网、建机制的要求，全面建成覆盖全民、城乡统筹、权责清晰、保障适度、可持续的多层次社会保障体系。全面实施全民参保计划。完善城镇职工基本养老保险和城乡居民基本养老保险制度，尽快实现养老保险全国统筹”。养老保险是我国社会保障体系的重要组成部分，近年来，我国全面深化养老保险制度改革，机关事业单位工作人员养老保险改革基本完成，城乡居民养老保险制度合并实施，企业年金制度不断完善，职业年金制度逐步推进，个人税收递延型商业养老保险制度加快试点，以基本养老保险为基础，包括企业年金、职业年金、商业保险等多层次养老保险体系加速形成。

职工基本养老保险、城乡居民基本养老保险、机关事业单位工作人员养老保险是我国基本养老保险制度的重要组成部分，对基本养老保险政策执行、业务管理、基金管理、信息系统管理等方面的监督检查，是审计工作的重要内容。目前，我国尚未建立统一的养老保险管理信息系统，各统筹区养老保险管理信息系统独立运行，数据库结构不完全统一，数据内容细节差异较大。全国审计信息化标准化技术委员会组织审计署社会保障审计司、审计署计算机技术中心、浙江省审计厅，系统梳理了全国各地养老保险基金管理信息系统数据结构和业务办理流程，构建了统一的数据元、数据表和数据接口输出文件，并在部分地区实地测试运行。养老保险基金审计数据接口的编制，既为审计机关开展养老保险基金审计提供数据采集和处理标准，满足养老保险基金审计业务的基本需要，对于提高信息化环境下养老保险基金监管工作的标准化、规范化，具有非常重要的现实意义，也可为其他需要提供参考。

# 财经信息技术 养老保险基金审计数据接口

## 1 范围

本标准规定了养老保险基金审计数据接口的要求，包括养老保险基金审计数据元和数据接口输出文件的格式、数据结构及时间要求。

本标准适用于养老保险基金审计数据交换和处理。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2260—2007 中华人民共和国行政区划代码

GB/T 2261.1—2003 个人基本信息分类与代码 第1部分：人的性别代码

GB/T 3304—1991 中国各民族名称的罗马字母拼写法和代码

GB/T 8563.2—2005 奖励、纪律处分信息分类与代码 第2部分：荣誉称号和荣誉奖章代码

GB/T 12402—2000 经济类型分类与代码

GB/T 18142—2017 信息技术 数据元素值表示 格式记法

GB/T 31594—2015 社会保险核心业务数据质量规范

GB 32100—2015 法人和其他组织统一社会信用代码编码规则

LD/T 92—2013 社会保险管理信息系统指标集与代码

## 3 术语和定义

<div style="text-align: center;"><img src="imgs/img_in_image_box_619_1034_658_1071.jpg" alt="Image" width="3%" /></div>


下列术语和定义适用于本文件。

### 3.1 

## 基本养老保险 basic old-age insurance

国家立法实施的，通过参保人、用人单位和政府等多方筹资形成基金，对参保并缴纳费用、达到待遇领取条件者依法提供物质帮助，在其因年老而退出劳动后，享有基本生活保障的一项社会保险制度。

注 $ ^{1} $ ：本标准中基本养老保险制度包括职工基本养老保险制度、城乡居民基本养老保险制度和机关事业单位工作人员养老保险制度。

注2：改写 GB/T 31596.2—2015，定义2.1。

### 3.2 

## 养老保险基金审计 basic old-age insurance fund auditing

国家审计机关依法对基本养老保险政策执行、业务管理、基金管理、信息系统管理等方面的真实性、合法性、效益性（包括安全性和发展的可持续性）进行审计监督检查的活动。

### 3.3 

## 数据接口 data interface

计算机软件系统之间传送数据、交换信息的接口，以电子文件的形式实现。

### 3.4 

## X ML 文件 extensible markup language file

用具有数据描述功能、高度结构性及可验证性的可扩展置标语言描述的数据文件。

### 3.5 

数据文件 data file

用于养老保险基金审计数据交换或处理的文件。

### 3.6 

## 数据元 data element

由一组属性规定其定义、标识、表示和允许值的数据单元。

注 $ ^{1} $ ：在本标准中是养老保险基金审计数据接口所输出数据的不可分割的基本单位。

注2：改写 GB/T 18391.1—2009，定义3.3.8。

### 3.7 

## 数据结构 data structure

养老保险基金审计数据接口所输出数据的内部构成，包含有若干个不同的数据元。

## 4 数据元

### 4.1 数据元的描述规则

数据元的描述格式如下：

a）数据元的标识符：在本标准中，是各个数据元的唯一标识，采用六位数字来标记；其中第1～3位表示为元素类别号，第4～6位为数据表中经过元素标准化合并后的顺序号，如果某表中出现了之前已经编号的元素则不重复编号。本标准中，第1～3位的表示按如下分类：

——001 表示公用信息类；

——002 表示单位信息类；

——003 表示人员信息类；

——004 表示参保信息类；

——005 表示单位缴费类；

——006 表示个人缴费类；

——007 表示待遇支付类；

——008 表示信息变更类；

——009 表示参数信息类；

——010 表示财务类。

b） 数据元的名称：数据元的字段名称。

c） 数据元的中文注释：数据元的字段对应的中文注释。

d）数据元的表示：数据元值的类型及长度的表示形式，按照 GB/T 18142—2017 的要求，具体表示如下：

——C 表示数字、字母、汉字及其他字符等；

——Cn 表示 n 位字符的固定长度；

——C..n 表示最多为 n 位字符的可变长度；

——I..n 表示最多为 n 位的整数可计算形式；

——Dw.d 表示十进制小数可计算形式，w 表示包含小数点前后字符位在内的整个字段最多字符位数，d 表示小数点后的最多字符位数。

e） 数据元的代码标识：数据元是否是代码，值为 Y 表示为代码，值为空表示为非代码。

f） 数据元的说明：数据元的含义描述。

g） 数据元的质量标准：与该数据元相关的其他说明。

### 4.2 数据元细目

#### 4.2.1 公用信息类数据元

标识符:001001

名 称:ZZZ001

中文注释: 时间属性

表 示: C16

代码标识：

说明：表示当前批次资源对应的时间信息

质量标准：其中前八位字符表示起始日期，后八位字符表示截止日期

标识符：001002

名 称:ZZZ002

中文注释: 地域属性

表 示: C6

代码标识：Y

说明: 表示当前批次资源所在省的省级行政区划代码

质量标准：按照 GB/T 2260—2007 表示

标识符:001003

名 称:AAB301

中文注释：行政区划代码

表 示: C6

代码标识：Y

说明：当前批次资源所在县（市、区）的行政区划代码

质量标准：按照 GB/T 2260—2007 表示

标识符：001004  

名称：AAA146  

中文注释：行政区划  

表示：C.128  

代码标识：  

说明：行政区划名称  

质量标准：按照 GB/T 2260—2007 表示

标识符:001005

名 称: AAB034

中文注释：经办机构编码

表 示:C..16

代码标识：

## 说明:社会保险经办机构编码

质量标准：

标识符:001006

名 称:AAB034N

中文注释：经办机构

表 示:C..128

代码标识：

说明：经办机构名称

质量标准：

标识符:001007

名 称:ZZZ003

中文注释: 修改时间

表 示: C8

代码标识：

说明：该行记录修改时间，仅用于数据管理维护

质量标准: 表示方式为 YYYYMMDD([Y]表示时间元素“年”所使用的数字, $ [M] $ 表示时间元素“月”所使用的数字, $ [D] $ 表示时间元素“日”所使用的数字)

#### 4.2.2 单位信息类数据元

标识符:002001

名 称:AAB001

中文注释: 单位编码

表 示:C..16

代码标识：

说明:社会保险参保单位编码,参保单位在系统中的唯一编码

质量标准：

标识符：002002

名 称:AAB004

中文注释: 单位名称

表 示:C..128

代码标识：

说明：参保单位的全称

质量标准：1. 不全为字母和数字；2. 应是全称，并与单位公章一致；3. 非空，无非法字符

标识符:002003

名 称:BAB010

中文注释：统一社会信用代码

表 示:C..18

代码标识：

说明：社会保险参保单位统一社会信用代码

质量标准：按照 GB 32100—2015 表示

标识符：002004

名 称:AAE045

中文注释:法定代表人姓名

表 示:C..64

代码标识：

说明：登记管理部门核发的有效证照或批文上的法定代表人姓名

质量标准：

标识符:002005

名 称:AAE046

中文注释:法定代表人证件号码

表 示:C..64

代码标识：

说明: 登记管理部门核发的有效证照或批文上的法定代表人证件号码

质量标准：

标识符:002006

名 称:EAC153

中文注释:法定代表人电话

表 示:C..64

代码标识：

说明:社会保险参保单位法定代表人电话

质量标准：

标识符:002007

名 称:AAB019

中文注释：单位类型代码

表 示:C..2

代码标识：Y

说明：参保单位的组织机构类型代码

质量标准：按照 GB/T 31594—2015，取值于表 A.5

标识符:002008

名 称:AAB019N

中文注释：单位类型

表 示:C..64

代码标识：

说明：参保单位的组织机构类型名称

质量标准：按照 GB/T 31594—2015，取值于表 A.5

标识符:002009

名 称:AAB020

中文注释: 经济类型代码

表 示:C..4

代码标识：Y

说明：参保单位所属的经济类型

质量标准：1. 按照 GB/T 12402—2000 表示；2. 非企业单位（机关、事业、社会团体等）此项为空

标识符:002010

名 称:AAB020N

中文注释：经济类型

表 示:C..64

代码标识：

说明：参保单位所属的经济类型

质量标准：1. 按照 GB/T 12402—2000 表示；2. 非企业单位（机关、事业、社会团体等）此项为空

标识符:002011

名 称:AAB021

中文注释:隶属关系代码

表 示:C..4

代码标识：Y

说明：隶属关系代码

质量标准：按照 GB/T 31594—2015，取值于表 A.6

标识符:002012

名 称:AAB021N

中文注释：隶属关系

表 示:C..16

代码标识：

说明：隶属关系名称，如中央、省、市、县等

质量标准：按照 GB/T 31594—2015，取值于表 A.6

标识符:002013

名 称:AAB022

中文注释: 行业代码

表 示:C..16

代码标识：Y

说明：社会保险参保单位的行业代码

质量标准：按照 LD/T 92—2013，取值于表 67

标识符:002014

名 称:AAB022N

中文注释：行业名称

表 示:C..64

代码标识：

说明：社会保险参保单位的行业名称

质量标准：按照 LD/T 92—2013，取值于表 67

标识符：002015

名 称: AAE005

中文注释:联系电话

表 示:C..32

代码标识：

说明：联系电话

质量标准：

标识符：002016

名称：AAE006

中文注释: 地址

表 示:C..128

代码标识：

说明：通信地址

质量标准：

#### 4.2.3 人员信息类数据元

标识符:003001

名称：AAC001

中文注释:人员编码

表 示:C..20

代码标识：

说明：指系统内人员的唯一标识

质量标准：

标识符:003002

名称：AAC002

中文注释: 社会保障号码

表 示:C..32

代码标识：

说明:对中国籍参保人员为其公民身份号码,对非中国籍参保人员为按照国家有关规定的编码规则编制的社会保障号码,包括国家或地区代码、预留位和有效证件号码

质量标准：1.首位为数字的，长度为18位；2.首位为数字的，应符合公民身份号码国家标准制定的编码规则；3.非空

标识符:003003

名称：AAC003

中文注释：姓名

表 示:C..64

代码标识：

说明:参保人员的现用姓名,外国人应采用护照等有效证件上标识的英文姓名

质量标准：1. 全称，并与有效身份证件上的姓名一致；2. 非空

标识符：003004

名 称:AAA029

中文注释: 证件类型代码

表 示:C..4

代码标识：Y

说明:公民的证件类型

质量标准：按照 LD/T 92—2013，取值于表 97

标识符:003005

名 称:AAA029N

中文注释：证件类型

表 示:C..32

代码标识：

说明:公民的证件类型

质量标准：按照 LD/T 92—2013，取值于表 97

标识符:003006

名 称:AAE135

中文注释：证件号码

表 示:C..32

代码标识：

说明：公民的证件号码，如：身份证号码、军官证号码

质量标准：非空

<div style="text-align: center;"><img src="imgs/img_in_image_box_8_1137_44_1172.jpg" alt="Image" width="3%" /></div>


标识符:003007

名 称:EAZ049

中文注释：开户银行名称

表 示:C..128

代码标识：

说明:社会保险参保人员在社保经办机构登记的有效个人银行卡开户的银行名称

质量标准：

标识符:003008

名 称:AAE010

中文注释：银行账号

表 示:C..64

代码标识：

说明:社会保险参保人员在社保经办机构登记的有效个人银行卡号

质量标准：

标识符:003009

名 称:AAE009

中文注释:银行账户名称

表 示:C..64

代码标识：

说明：银行账户名称

质量标准：

标识符:003010

名 称:AAC004

中文注释: 性别代码

表 示:C..1

代码标识：Y

说明：参保人员的性别

质量标准：按照 GB/T 2261.1—2003 表示

标识符:003011

名 称: AAC004N

中文注释: 性别

表 示:C..8

代码标识：

说明：参保人员的性别

质量标准：按照 GB/T 2261.1—2003 表示

标识符:003012

名 称: AAC005

中文注释: 民族代码

表 示:C..2

代码标识：Y

说明：人员的民族代码

质量标准：按照 GB/T 3304—1991 表示

标识符:003013

名 称:AAC005N

中文注释：民族

表 示:C..64

代码标识：

说明:人员的民族名称

质量标准：按照 GB/T 3304—1991 表示

## GB/T 40217—2021

标识符:003014

名 称:AAC010

中文注释：户籍所在地

表 示:C..128

代码标识：

说明:社会保险参保人员户籍所在地

质量标准：

标识符:003015

名 称:AAC087

中文注释：荣誉称号级别代码

表 示:C..1

代码标识：Y

说明：荣誉称号级别代码

质量标准：按照 GB/T 8563.2—2005 表示

标识符:003016

名 称:AAC087N

中文注释: 荣誉称号级别

表 示:C..32

代码标识：

说明：荣誉称号级别名称

质量标准：按照 GB/T 8563.2—2005 表示

标识符:003017

名 称:AAC148

中文注释:困难人员类别代码

表 示:C..1

代码标识：Y

说明：享受特殊财政补助的人员类别

质量标准：按照 GB/T 31594—2015，取值于表 A.25

标识符:003018

名 称:AAC148N

中文注释:困难人员类别

表 示:C..32

代码标识：

说明：享受特殊财政补助的人员类别

质量标准：按照 GB/T 31594—2015，取值于表 A.25

标识符:003019

名 称:AAC012

中文注释:个人身份代码

表 示:C..4

代码标识：Y

说明:个人身份代码

质量标准：按照 GB/T 31594—2015，取值于表 A.15

标识符:003020

名 称: AAC012N

中文注释:个人身份

表 示:C..64

代码标识：

说明:个人身份名称

质量标准：按照 GB/T 31594—2015，取值于表 A.15

标识符:003021

名 称:AAF013

中文注释：街道或乡镇编码

表 示:C..16

代码标识：

说明:参保人员所在地的乡镇或街道编码

质量标准：

标识符:003022

名 称:AAF031

中文注释:街道或乡镇

表 示:C..128

代码标识：

说明:参保人员所在地的乡镇或街道名称

质量标准：

标识符:003023

名 称:AAF030

中文注释: 社区或村编码

表 示:C..16

代码标识：

说明:参保人员所属村社区编码

质量标准：

标识符:003024

名 称:AAF030N

中文注释：社区或村

表 示:C..128

代码标识：

说明：参保人员所属村社区名称

质量标准：

标识符:003025

名 称: AAC016

中文注释: 就业状态代码

表 示:C..4

代码标识：Y

说明：就业状态，包括在业、离休、退休、退职、失业等

质量标准：按照 LD/T 92—2013，取值于表 89

标识符:003026

名 称: AAC016N

中文注释: 就业状态名称

表 示:C..32

代码标识：

说明：就业状态，包括在业、离休、退休、退职、失业等

质量标准：按照 LD/T 92—2013，取值于表 89

标识符:003027

名 称: AAC006

中文注释: 出生日期

表 示: C8

代码标识：

说明:参保人员的出生日期,以中华人民共和国居民身份证或其他有效证件记载,与社会保障号码的第7~14位相匹配

质量标准：1\. 表示方式为 YYYYMMDD；2\. 应早于“参加工作日期”项；3\. 非空

标识符:003028

名 称: AAC007

中文注释: 参加工作日期

表 示: C8

代码标识：

说明：社会保险参保人员参加工作日期

质量标准: 表示方式为 YYYYMMDD, 当原始数据仅能精确到月份, 而无法确定到日时, 统一设为当月第一天

标识符:003029

名 称:AIC162

中文注释：离退休日期

表 示: C8

代码标识：

说明：由人力资源和社会保障部门、组织部门批准的参保人员离休、退休、退职等的时间

质量标准：1\. 表示方式为 YYYYMMDD；2\. 应晚于“参加工作日期”项

标识符:003030

名 称: AAE138

中文注释:死亡日期

表 示: C8

代码标识：

说明：参保人员发生与变更原因中情况相符的日期

质量标准：1\. 表示方式为 YYYYMMDD；2\. 前 6 位大于或等于“首次参保年月”

标识符:003031

名 称: AAC014

中文注释:专业技术职务级别代码

表 示:C..3

代码标识：Y

说明：专业技术职务级别代码

质量标准：按照 GB/T 31594—2015，取值于表 A.16

标识符:003032

名 称:AAC014N

中文注释：专业技术职务级别

表 示:C..64

代码标识：

说明：专业技术职务级别名称

质量标准：按照 GB/T 31594—2015，取值于表 A.16

标识符:003033

名 称: AAC015

中文注释：国家职业资格等级代码

表 示:C..4

代码标识：Y

说明：对从事某一职业所必备的学识、技术和能力的编码

质量标准：按照 GB/T 31594—2015，取值于表 A.17

标识符:003034

名 称:AAC015N

中文注释：国家职业资格等级

表 示:C..64

代码标识：

说明：对从事某一职业所必备的学识、技术和能力的名称

质量标准：按照 GB/T 31594—2015，取值于表 A.17

标识符:003035

名 称: AAC020

中文注释: 行政职务级别代码

## GB/T 40217—2021

表 示:C..3

代码标识：Y

说明：行政职务级别代码

质量标准：按照 GB/T 31594—2015，取值于表 A.18

标识符:003036

名 称: AAC020N

中文注释: 行政职务级别

表 示:C..64

代码标识：

说明：行政职务级别名称

质量标准：按照 GB/T 31594—2015，取值于表 A.18

标识符:003037

名 称: AAC064

中文注释:退役军人类别代码

表 示:C..2

代码标识：Y

说明：参加社会保险的退役军人类别代码

质量标准：按照 GB/T 31594—2015，取值于表 A.22

标识符:003038

名 称: AAC064N

中文注释: 退役军人类别

表 示:C..64

代码标识：

说明：参加社会保险的退役军人类别

质量标准：按照 GB/T 31594—2015，取值于表 A.22

#### 4.2.4 参保信息类数据元

标识符:004001

名 称:AAB050

中文注释: 单位参保日期

表 示: C6

代码标识：

说明: 单位参加与险种类型相对应的社会保险险种的日期

质量标准: 表示方式为 YYYYMM

标识符:004002

名 称:AAC049

中文注释：首次参保年月

表 示: C6

代码标识：

说明:参保人员全国范围内首次参加某一险种社会保险的年月或参保人员首次缴纳某一险种社会保险费的年月

质量标准：1\. 表示方式为 YYYYMM；2\. 不早于“参加工作日期”项；3\. 非空

标识符：004003

名 称: AAC008

中文注释:个人参保状态

表 示:C..10

代码标识：

说明：社会保险参保人员个人参保状态，未参保、正常参保、终止参保

质量标准：按照 LD/T 92—2013，取值于表 82

标识符:004004

名 称: AAC031

中文注释:个人缴费状态代码

表 示:C..1

代码标识：Y

说明:标注参保人员的与险种类型相对应的社会保险缴费状态编码

质量标准：按照 GB/T 31594—2015，取值于表 A.19

标识符:004005

名 称:AAC031N

中文注释:个人缴费状态

表 示:C..16

代码标识：

说明:标注参保人员的与险种类型相对应的社会保险缴费状态名称

质量标准：按照 GB/T 31594—2015，取值于表 A.19

标识符:004006

名 称: AAE030

中文注释：本次开始日期

表 示: C8

代码标识：

说明：当前参保记录的开始时间

质量标准: 表示方式为 YYYYMMDD

标识符:004007

名 称:AAE031

中文注释：本次终止日期

表 示: C8

代码标识：

说明: 当前参保记录的社保结束时间, 如个人缴费状态是参保缴费状态则为空

质量标准: 表示方式为 YYYYMMDD

#### 4.2.5 单位缴费类数据元

标识符:005001

名 称:AAB051

中文注释：单位缴费状态代码

表 示:C..1

代码标识：Y

说明：参保单位当前缴费情况代码

质量标准：按照 GB/T 31594—2015，取值于表 A.9

标识符:005002

名 称:AAB051N

中文注释: 单位缴费状态

表 示:C..32

代码标识：

说明：参保单位当前缴费情况名称

质量标准：按照 GB/T 31594—2015，取值于表 A.9

标识符：005003

名 称:EAZ058

中文注释:结算单号

表 示:C..20

代码标识：

说明: 缴费结算单号(ID)

质量标准：

标识符:005004

名 称:AAE002

中文注释:结算年月

表 示:C6

代码标识：

说明：养老保险业务的结算年月

质量标准: 表示方式为 YYYYMM

标识符:005005

名 称:AAE003

中文注释：应缴年月

表 示: C6

代码标识：

说明：养老保险业务的对应费款所属期

质量标准: 表示方式为 YYYYMM

标识符:005006

名 称: EAD131

中文注释:到账日期

表 示: C8

代码标识：

说明：到账日期

质量标准: 表示方式为 YYYYMMDD

标识符:005007

名 称:AAB033

中文注释: 征缴方式代码

<div style="text-align: center;"><img src="imgs/img_in_image_box_618_494_655_531.jpg" alt="Image" width="3%" /></div>


表 示:C..1

代码标识：Y

说明:社会保险经办机构收取与险种类型相对应的缴费方式代码

质量标准：按照 GB/T 31594—2015，取值于表 A.8

标识符:005008

名 称:AAB033N

中文注释: 征缴方式

表 示:C..32

代码标识：

说明:社会保险经办机构收取与险种类型相对应的缴费方式名称

质量标准：按照 GB/T 31594—2015，取值于表 A.8

标识符:005009

名 称:AAE078

中文注释: 足额到账标志代码

表 示:C..1

代码标识：Y

说明：足额到账标志代码

质量标准：按照 GB/T 31594—2015，取值于表 A.62

标识符:005010

名 称:AAE078N

中文注释：足额到账标志

表 示:C..16

代码标识：

说明：足额到账标志名称

质量标准：按照 GB/T 31594—2015，取值于表 A.62

标识符:005011

名 称:AAA115

中文注释：应缴类型代码

## GB/T 40217—2021

表 示:C..2

代码标识：Y

说明：参保人员个人应缴费对应的缴费类型

质量标准：按照 GB/T 31594—2015，取值于表 A.3

标识符:005012

名 称:AAA115N

中文注释：应缴类型

表 示:C..40

代码标识：

说明：参加社会保险的应缴类型

质量标准：按照 GB/T 31594—2015，取值于表 A.3

标识符:005013

名 称:AAE140

中文注释：险种代码

表 示:C..3

代码标识：Y

说明：参加社会保险的险种类型

质量标准：按照 GB/T 31594—2015，取值于表 A.28

标识符:005014

名 称:AAE140N

中文注释：险种名称

表 示:C..32

代码标识：

说明：参加社会保险的险种名称

质量标准：按照 GB/T 31594—2015，取值于表 A.28

标识符:005015

名 称:AAB119

中文注释:应征人数

表 示:I..6

代码标识：

说明:缴费人数

质量标准：

标识符:005016

名 称:AAE058

中文注释：应缴总金额

表 示:D16.2

代码标识：

说明：应缴总金额，单位为元

质量标准：

标识符:005017

名 称:AAB121

中文注释：单位缴费基数总额

表 示:D16.2

代码标识：

说明:社会保险单位应缴核定单位缴费基数总额,通常是指截至核定日期前单位缴费基数的总和,单位为元

质量标准：

标识符:005018

名 称:AAB120

中文注释:个人缴费基数总额

表 示:D16.2

代码标识：

说明:社会保险单位应缴核定个人缴费基数总额,通常是指截至核定日期前个人缴费基数的总和,单位为元

质量标准：

标识符:005019

名 称:AAE020

中文注释: 单位应缴金额

表 示:D16.2

代码标识：

说明：单位缴费金额，单位为元

质量标准：

标识符:005020

名 称:AAE022

中文注释:个人应缴金额

表 示:D16.2

代码标识：

说明：参保人员按规定本次应当缴纳的养老保险金额，单位为元

质量标准：应大于或等于0

标识符:005021

名 称:AAB204

中文注释：滞纳金金额

表 示:D16.2

代码标识：

说明：滞纳金缴纳金额

质量标准：

标识符：005022

名 称:AAE021

中文注释：单位划账金额

表 示:D16.2

代码标识：

说明：单位划账金额，单位划入个人账户金额，单位为元

质量标准：

标识符:005023

名 称: AAE023

中文注释：个人划账金额

表 示:D16.2

代码标识：

说明:社会保险单位核定本期单位缴费划入个人账户总额,是指本月按规定由单位缴费部分划入基本养老保险个人账户的金额,单位为元

质量标准：

标识符:005024

名 称:AAE101

中文注释: 应缴年度

表 示: C4

代码标识：

说明：年度

质量标准: 表示方式为 YYYY

标识符:005025

名 称:AAE080

中文注释: 单位实缴金额

表 示:D16.2

代码标识：

说明：当前业务周期参保单位按应缴当月金额实际缴纳的金额，单位为元

质量标准：应小于或等于“单位应缴当月金额”

标识符:005026

名 称:AAE081

中文注释：单位实缴划入个人账户金额

表 示:D16.2

代码标识：

说明：当前业务周期单位缴费部分中，实际划入个人账户的金额，单位为元

质量标准：应小于或等于“单位实缴金额”

标识符:005027

名 称: AAE082

中文注释: 个人实缴金额

表 示:D16.2

代码标识：

说明：当前业务周期参保人员按应缴当月金额实际缴纳的基本养老保险费金额，单位为元

质量标准：应小于或等于“个人应缴当月金额”

标识符：005028

名 称: AAE083

中文注释:个人实缴划入个人账户金额

表 示:D16.2

代码标识：

说明：当前业务周期个人缴费中，实际划入个人账户的金额，单位为元

质量标准：应小于或等于“个人实缴金额”

#### 4.2.6 个人缴费类数据元

标识符:006001

名 称:AAE201

中文注释: 实际缴费月数

表 示:I..3

代码标识：

说明:参保人员足额缴纳某一险种养老保险费所形成的累计月数

质量标准：

标识符：006002

名 称:AIC268

中文注释:个人账户累计本息

表 示:D16.2

代码标识：

说明：指参保人员个人账户中个人缴费部分累计本息与单位划入部分累计本息之和（指上年末本息和当年本金），单位为元

质量标准：

标识符:006003

名 称: AAF027

中文注释: 划入个人账户金额

表 示:D16.2

代码标识：

说明：个人应缴划入个人账户金额，单位为元

质量标准：

标识符:006004

名 称:AAE034

中文注释:中央财政补贴

表 示:D16.2

代码标识：

说明：中央财政补贴，单位为元

质量标准：

标识符:006005

名 称:AAE024

中文注释：省级财政补贴

表 示:D16.2

代码标识：

说明：省级财政补贴，单位为元

质量标准：

标识符:006006

名 称:AAE026

中文注释:市级财政补贴

表 示:D16.2

代码标识：

说明：市级财政补贴，单位为元

质量标准：

标识符:006007

名 称:AAE028

中文注释：县区财政补贴

表 示:D16.2

代码标识：

说明：县（区）财政补贴，单位为元

质量标准：

标识符:006008

名 称:AIC079

中文注释:本年缴费月数

表 示:I..3

代码标识：

说明：本年缴费月数

质量标准：

<div style="text-align: center;"><img src="imgs/img_in_image_box_44_1467_79_1503.jpg" alt="Image" width="2%" /></div>


标识符:006009

名 称:AAE180

中文注释：缴费基数

表 示:D16.2

代码标识：

说明:社会保险经办机构按规定核定的计算参保人员用于缴纳某一险种社会保险费所使用的基数

质量标准：1.个人缴费状态为“参保缴费”时，个人缴费基数大于0，取值范围应符合国家有关规定；2.个人缴费状态为“暂停缴费（中断）”“终止缴费”时，为空

标识符:006010

名 称:AAA042

中文注释: 单位缴费比例

表 示:D16.4

代码标识：

说明：单位缴费比例

质量标准：

标识符:006011

名 称:AAA041

中文注释:个人缴费比例

表 示:D16.4

代码标识：

说明：指当地政府规定的参保职工缴纳基本养老保险费的比例，以小数方式表示，如“0.08”质量标准：

标识符:006012

名 称: AAE025

中文注释：财政划账金额

表 示:D16.2

代码标识：

说明：其中财政划账金额，单位为元

质量标准：

标识符:006013

名 称:ZZB004

中文注释：其他补充金额

表 示:D16.2

代码标识：

说明：其他补充金额，单位为元

质量标准：

标识符:006014

名 称:AAE027

中文注释：其他划账金额

表 示:D16.2

代码标识：

说明：其中其他划账金额，单位为元

质量标准：

标识符:006015

名 称:AAE017

中文注释:核销标志

表 示:C..10

代码标识：

说明：核销标志（已核销、未核销）

质量标准：未核销，已核销

标识符:006016

名 称:AAE011

中文注释：经办人

表 示:C..64

代码标识：

说明：经办人员姓名

质量标准：

标识符:006017

名 称:AAE036

中文注释: 经办日期

表 示: C8

代码标识：

说明：该笔业务的经办日期

质量标准: 表示方式为 YYYYMMDD

#### 4.2.7 待遇支付类数据元

标识符:007001

名 称:AIC249

中文注释: 养老丧葬补助金

表 示:D16.2

代码标识：

说明:参保人员死亡后按国家规定给予的养老丧葬补助金,单位为元

质量标准：

标识符:007002

名 称:AIC250

中文注释：养老抚恤金

表 示:D16.2

代码标识：

说明：参保人员死亡后按国家规定给予的抚恤金，单位为元

质量标准：应大于或等于0；上限值执行国家有关规定

标识符:007003

名 称:EAZ048

中文注释: 待遇支付明细序号

表 示:C..32

代码标识：

说明：支付明细流水号

质量标准：

标识符:007004

名 称:AAA036

中文注释: 待遇项目代码

表 示: C6

代码标识：Y

说明:社会保险待遇项目的代码

质量标准：按照 GB/T 31594—2015，取值于表 A.1

标识符:007005

名 称:AAA037

中文注释: 待遇项目名称

表 示:C..50

代码标识：

说明:社会保险待遇项目的名称

质量标准：按照 GB/T 31594—2015，取值于表 A.1

标识符:007006

名 称:AIC160

中文注释：待遇享受开始年月

表 示: C6

代码标识：

说明:参保人员开始享受待遇的时间

质量标准: 表示方式为 YYYYMM

标识符:007007

名 称:EIC013

中文注释：个账支付金额

表 示:D16.2

代码标识：___

说明：从个人账户中支付的金额，单位为元



<div style="text-align: center;"><img src="imgs/img_in_image_box_476_1416_514_1449.jpg" alt="Image" width="3%" /></div>


质量标准：

标识符:007008

名 称:AAE019

中文注释:待遇金额

表 示:D16.2

代码标识：

说明：发放待遇的总额，单位为元

质量标准：

标识符:007009

名 称:AAE133

中文注释:领取人姓名

表 示:C..64

代码标识：

说明：基本养老保险待遇领取人

质量标准：

标识符:007010

名 称:EAE021

中文注释:领取关系

表 示:C..8

代码标识：

说明：与参保人关系

质量标准：

标识符:007011

名 称:AAE136

中文注释:领取人证件号码

表 示:C..64

代码标识：

说明：基本养老保险待遇领取人证件号码

质量标准：

标识符:007012

名 称:AAE145

中文注释: 待遇发放方式代码

表 示:C..2

代码标识：Y

说明：社会保险待遇发放方式的分类

质量标准：按照 GB/T 31594—2015，取值于表 A.29

标识符:007013

名 称:AAE145N

中文注释：待遇发放方式

表 示:C..32

代码标识：

说明：社会保险待遇发放方式的分类

质量标准：按照 GB/T 31594—2015，取值于表 A.29

标识符:007014

名 称:EAE004

中文注释: 待遇项目支付类型代码

表 示:C..2

代码标识：Y

说明：待遇项目支付类型代码：0——固定，1——临时

质量标准：

标识符:007015

名 称: EAE004N

中文注释：待遇项目支付类型

表 示:C..16

代码标识：

说明：待遇项目支付类型名称

质量标准：

<div style="text-align: center;"><img src="imgs/img_in_image_box_45_875_81_911.jpg" alt="Image" width="3%" /></div>


标识符:007016

名 称:EAE005

中文注释:统筹类型代码

表 示:C..4

代码标识：Y

说明：1——统筹内，2——统筹外

质量标准：

标识符:007017

名 称:EAE005N

中文注释:统筹类型

表 示:C..16

代码标识：

说明：统筹内，统筹外

质量标准：

标识符:007018

名 称:AIC161

中文注释:离退休类别代码

表 示:C..2

代码标识：Y

说明：离退休类型

质量标准：按照 GB/T 31594—2015，取值于表 A.37

标识符:007019

名 称:AIC161N

中文注释:离退休类别

表 示:C..32

代码标识：

说明：离退休类型

质量标准：按照 GB/T 31594—2015，取值于表 A.37

标识符:007020

名 称:AAE211

中文注释：核定年月

表 示: C6

代码标识：

说明：养老保险数据核定时间

质量标准：表示方式为 YYYYMM

标识符:007021

名 称: AAE200

中文注释: 视同缴费月数

表 示:I..3

代码标识：

说明: 经人力资源社会保障部门审核确定的参保人员在实行企业职工基本养老保险个人缴费之前按照国家有关规定计算的连续工龄的月数

质量标准：

标识符：007022

名 称:EAE027

中文注释: 中断月数

表 示:I..3

代码标识：

说明：基本养老保险中断缴费月数

质量标准：

标识符:007023

名 称: EAC047

中文注释：累计缴费月数

表 示:I..3

代码标识：

说明：基本养老保险累计缴费月数

质量标准：

标识符：007024

名称：AAC019

中文注释: 特殊工种类型代码

表 示:C..6

代码标识：Y

说明:社会保险参保人员特殊工种类型

质量标准：按照 LD/T 92—2013，取值于表 91

标识符:007025

名 称:AAC019N

中文注释: 特殊工种类型

<div style="text-align: center;"><img src="imgs/img_in_image_box_488_488_525_524.jpg" alt="Image" width="3%" /></div>


表 示:C..20

代码标识：

说明:社会保险参保人员特殊工种类型

质量标准：按照 LD/T 92—2013，取值于表 91

标识符:007026

名 称:EAC065

中文注释: 特殊工种月数

表 示:I..3

代码标识：

说明：养老保险人员累计从事特殊工种月数

质量标准：

标识符:007027

名 称:AIC165

中文注释：离退休时账户总金额

表 示:D16.2

代码标识：

说明：参保人员截至当前业务周期末基本养老保险个人账户金额，单位为元

质量标准：

标识符:007028

名 称:EIC009

中文注释：退休时核定养老金

表 示:D16.2

代码标识：

说明：离退休时核定的养老金金额，单位为元

质量标准：

标识符:007029

名 称:AAC158

中文注释：低保对象标识

## GB/T 40217—2021

表 示:C..1

代码标识：Y

说明：标注由民政部门核准的享受最低生活保障的人员

质量标准：按照 GB/T 31594—2015，取值于表 A.62

标识符:007030

名 称:EAC062

中文注释：补发月数

表 示:I..3

代码标识：

说明：退休核定时，基本养老保险补发月数

质量标准：

标识符:007031

名 称:EAC063

中文注释：补发总金额

表 示:D16.2

代码标识：

说明：退休核定时，基本养老保险补发总金额，单位为元

质量标准：

标识符:007032

名 称:AAE001

中文注释:年度

表 示: C4

代码标识：

说明：年度

质量标准: 表示方式为 YYYY

标识符:007033

名 称:AIC200

中文注释：年初账户金额

表 示:D16.2

代码标识：

说明：年初账户本息，单位为元

质量标准：

标识符:007034

名 称:ZZB001

中文注释：当年账户本金划入

表 示:D16.2

代码标识：

说明：当年本金划入，单位为元

质量标准：

标识符:007035

名 称:ZZB002

中文注释：当年账户利息划入

表 示:D16.2

代码标识：

说明:当年账户利息划入(包括历年账户当年利息),2006年前包括单位账户利息和个人利息,单位为元

质量标准：

标识符:007036

名 称:AIC340

中文注释:本年账户支出

表 示:D16.2

代码标识：

说明：离退休账户冲减额（当年离退休待遇领取金额中从个人账户中支付的部分），单位为元  

质量标准：

标识符:007037

名 称:ZZB005

<div style="text-align: center;"><img src="imgs/img_in_image_box_669_796_706_831.jpg" alt="Image" width="3%" /></div>


中文注释：年末账户金额

表 示:D16.2

代码标识：

说明：年末账户本息（含利息的利息），单位为元

质量标准：

标识符:007038

名 称:AIC042

中文注释:历年缴纳月数

表 示:I..3

代码标识：

说明：截至上年末累计缴费月数

质量标准：

标识符:007039

名 称:EAC039

中文注释：账户记息日期

表 示: C8

代码标识：

说明：账户记息日期

质量标准：表示方式为 YYYYMMDD

标识符:007040

名 称: EAC040

中文注释: 养老账户状态代码

表 示:C..3

代码标识：Y

说明：0——初始，1——正常结息，2——终止，3——异地转出，4——退休，5——封存质量标准：

标识符:007041

名 称: EAC040N

中文注释：养老账户状态

表 示:C..32

代码标识：

说明：养老账户状态名称

质量标准：与 EAC040 说明的标志对应

标识符:007042

名 称:AAA157

中文注释：基金列支类型代码

表 示:C..4

代码标识：Y

说明：基金列支类型（基金款项代码）

质量标准：按照 LD/T 92—2013，取值于表 53

标识符:007043

名 称:AAA157N

中文注释：基金列支类型

表 示:C..16

代码标识：

说明：基金列支类型名称

质量标准：按照 LD/T 92—2013，取值于表 53

标识符：007044

名 称:EAC064

中文注释: 待遇年月

表 示: C6

代码标识：

说明：待遇发放所属年月（应支付年月）

质量标准: 表示方式为 YYYYMM

#### 4.2.8 信息变更类数据元

标识符:008001

名 称: EAC071N

中文注释:转移方向

表 示:C..16

代码标识：

说明:社会保险参保人员转移方向,例如转出、转入等

质量标准：按照 LD/T 92—2013，取值于表 105

标识符:008002

名 称: EAC071

中文注释:转移方向代码

表 示:C..2

代码标识：Y

说明:社会保险参保人员转移方向,例如转出、转入等

质量标准：按照 LD/T 92—2013，取值于表 105

标识符:008003

名 称: AAC077

中文注释：对方社会保险机构名称

表 示:C..100

代码标识：

说明:社会保险参保人员转移后社会保险机构名称

质量标准：

标识符:008004

名 称: AAC076

中文注释：对方所在单位名称

表 示:C..100

代码标识：

## 说明:社会保险参保人员转移后所在参保单位名称

质量标准：

标识符:008005

名 称:AIC099

中文注释：转移个人划转金额

表 示:D16.2

代码标识：

说明：转移个人划转金额，单位为元

质量标准：

标识符:008006

名 称:AIC100

中文注释:转移单位划转金额

表 示:D16.2

代码标识：

说明：转移单位划转金额，单位为元

质量标准：

标识符:008007

名 称:AIC102

中文注释:基本养老保险基金转移总额

表 示:D16.2

代码标识：

说明：基本养老保险基金转移总额，单位为元

质量标准：

标识符:008008

名 称:AIC103

中文注释：统筹部分转移金额

表 示:D16.2

代码标识：

说明：统筹部分转移金额，单位为元

质量标准：

标识符:008009

名 称: OAA027

中文注释：对方行政区划代码

表 示: C6

代码标识：Y

说明：对方行政区划代码

质量标准：按照 GB/T 2260—2007 表示

标识符:008010

名 称: OAA027N

中文注释:对方行政区划

表 示:C..64

代码标识：

说明：对方行政区划名称

质量标准：按照 GB/T 2260—2007 表示

标识符:008011

名 称:AAB100

中文注释: 单位变更类型代码

表 示:C..10

代码标识：Y

说明：单位变更类型代码

质量标准：按照 LD/T 92—2013，取值于表 75

标识符:008012

名 称:AAB100N

中文注释: 单位变更类型

表 示:C..32

代码标识：

说明：单位变更类型名称

质量标准：按照 LD/T 92—2013，取值于表 75

标识符:008013

名 称:AAE123

中文注释：变更前信息

表 示:C..64

代码标识：

说明：变更前信息

质量标准：

标识符:008014

名 称:AAE124

中文注释: 变更后信息

表 示:C..64

代码标识：

说明：变更后信息

质量标准：

标识符:008015

名 称:AAE160

中文注释：变更原因代码

表 示:C..4

代码标识：Y

<div style="text-align: center;"><img src="imgs/img_in_image_box_738_1060_774_1094.jpg" alt="Image" width="3%" /></div>


说明：变更原因代码

质量标准：按照 GB/T 31594—2015，取值于表 A.32

标识符:008016

名 称:AAE160N

中文注释：变更原因

表 示:C..64

代码标识：

说明：变更原因名称

质量标准：按照 GB/T 31594—2015，取值于表 A.32

标识符:008017

名 称:AAE035

中文注释:变更日期

## GB/T 40217—2021

表 示: C8

代码标识：

说明：经办机构核定变更事项的日期及时间

质量标准：1\. 表示方式为 YYYYMMDD；2\. 非空

标识符:008018

名 称: AAZ308

中文注释：人员变更流水号

表 示:C..32

代码标识：

说明：养老保险人员变更信息的流水号

质量标准：

标识符:008019

名 称: AAC050

中文注释:个人变更类型代码

表 示:C..10

代码标识：Y

说明：个人变更类型代码

质量标准：按照 LD/T 92—2013，取值于表 96

标识符：008020

名 称: AAC050N

中文注释:个人变更类型

表 示:C..10

代码标识：

说明:个人变更类型名称

质量标准：按照 LD/T 92—2013，取值于表 96

#### 4.2.9 参数信息类数据元

标识符:009001

名 称:AAA002

中文注释：参数类别编码

表 示:C..50

代码标识：Y

说明：用于标识社保系统中出现的每一类参数的类别编码，如基金列支类型的编码为 AAA157

质量标准：

标识符:009002

名 称:AAA101

中文注释：参数类别名称

表 示:C..128

代码标识：

说明：用于标识社保系统中出现的每一类参数的类别名称

质量标准：

标识符：009003

名称：AAA102

中文注释: 参数值

表 示:C..128

代码标识：

说明：参数值

质量标准：

标识符:009004

名 称:EAA023

中文注释: 参数名称

表 示:C..128

代码标识：

说明：参数名称

质量标准：

标识符：009005

名称：AAE100

中文注释：有效标志

表示：C..2

代码标识：

说明：当前有效标志

质量标准：按照 GB/T 31594—2015，取值于表 A.62

#### 4.2.10 财务类数据元

标识符：010001

名 称:ZZA101

中文注释: 账套号

表 示: C..32

代码标识：

说明：账套号

质量标准：

标识符:010002

名 称:ZZA101N

中文注释: 账套名称

表 示: C..32

代码标识：

## GB/T 40217—2021

说 明:账套名称

质量标准：

标识符:010003

名 称: AAD081

中文注释:会计年度

表 示: C4

代码标识：

说明:会计年度

质量标准: 表示方式为 YYYY

标识符:010004

名 称: EAD004

中文注释:科目编码

表 示:C..60

代码标识：

说明：科目编码

质量标准：

标识符:010005

名 称: EAD006

中文注释:科目名称

表 示:C..64

代码标识：

说明: 使用全称, 并使用“--”作为分隔符

质量标准：

标识符:010006

名 称:EAD011

中文注释:余额方向

表 示:C..4

代码标识：

说明:余额方向

质量标准：“借”“贷”或“借方”“贷方”

标识符:010007

名 称: AAD082

中文注释:会计期间

表 示:C..15

代码标识：

说明:会计期间

质量标准：

标识符:010008

名 称: AAD087

中文注释:期初余额

表 示:D20.2

代码标识：

说明：期初余额

质量标准：

标识符:010009

名 称: AAD088

中文注释：本期借方发生额

表 示:D20.2

代码标识：

说明：本期借方发生额

质量标准：

标识符:010010

名 称: AAD089

中文注释:本期贷方发生额

表 示:D20.2

代码标识：

说明：本期贷方发生额

质量标准：

标识符:010011

名 称: AAD092

中文注释:期末余额

表 示:D20.2

代码标识：

说明：期末余额

质量标准：

标识符:010012

<div style="text-align: center;"><img src="imgs/img_in_image_box_848_1187_883_1223.jpg" alt="Image" width="2%" /></div>


名 称:AAD131

中文注释:凭证编号

表 示:C..60

代码标识：

说明:凭证编号

质量标准：

标识符:010013

名 称: AAD138

中文注释:凭证日期

## GB/T 40217—2021

表 示: C8

代码标识：

说明：凭证日期

质量标准:表示方式为 YYYYMMDD

标识符:010014

名 称: AAD128

中文注释：摘要

表 示:C..300

代码标识：

说 明: 摘要

质量标准：

标识符:010015

名 称:EAD143

中文注释:借方金额

表 示:D20.2

代码标识：

说明：借方金额

质量标准：

标识符:010016

名 称:EAD144

中文注释:贷方金额

表 示:D20.2

代码标识：

说明:贷方金额

质量标准：

标识符:010017

名 称:ZZA001

中文注释：制单人

表 示:C..30

代码标识：

说 明: 制单人

质量标准：

标识符:010018

名 称:ZZA002

中文注释:审核人

表 示:C..30

代码标识：

说 明:审核人

质量标准：

标识符:010019

名 称:ZZA003

中文注释: 记账人

表 示：C..30

代码标识：

说 明: 记账人

质量标准：

## 5 接口文件的输出

### 5.1 输出文件的格式

输出的接口文件应采用 XML 格式，具体格式参见附录 A，实例参见附录 B。

### 5.2 输出文件的数据结构

#### 5.2.1 总则

本标准要求输出文件的数据结构按照表1～表21中的规定输出，其中“标识符”栏中的编号对应4.2中所描述的数据元。

#### 5.2.2 单位信息类数据结构

单位信息类数据结构，见表1。

<div style="text-align: center;">表 1 养老保险单位基本信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>002003</td><td style='text-align: center;'>BAB010</td><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>C..18</td></tr><tr><td style='text-align: center;'>002004</td><td style='text-align: center;'>AAE045</td><td style='text-align: center;'>法定代表人姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002005</td><td style='text-align: center;'>AAE046</td><td style='text-align: center;'>法定代表人证件号码</td><td style='text-align: center;'>C..64</td></tr></table>

<div style="text-align: center;">表 1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>002006</td><td style='text-align: center;'>EAC153</td><td style='text-align: center;'>法定代表人电话</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002007</td><td style='text-align: center;'>AAB019</td><td style='text-align: center;'>单位类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>002008</td><td style='text-align: center;'>AAB019N</td><td style='text-align: center;'>单位类型</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002009</td><td style='text-align: center;'>AAB020</td><td style='text-align: center;'>经济类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>002010</td><td style='text-align: center;'>AAB020N</td><td style='text-align: center;'>经济类型</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002011</td><td style='text-align: center;'>AAB021</td><td style='text-align: center;'>隶属关系代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>002012</td><td style='text-align: center;'>AAB021N</td><td style='text-align: center;'>隶属关系</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002013</td><td style='text-align: center;'>AAB022</td><td style='text-align: center;'>行业代码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002014</td><td style='text-align: center;'>AAB022N</td><td style='text-align: center;'>行业名称</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002015</td><td style='text-align: center;'>AAE005</td><td style='text-align: center;'>联系电话</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>002016</td><td style='text-align: center;'>AAE006</td><td style='text-align: center;'>地址</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005001</td><td style='text-align: center;'>AAB051</td><td style='text-align: center;'>单位缴费状态代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005002</td><td style='text-align: center;'>AAB051N</td><td style='text-align: center;'>单位缴费状态</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>004001</td><td style='text-align: center;'>AAB050</td><td style='text-align: center;'>单位参保日期</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.3 人员信息类数据结构

人员信息类数据结构，见表 2 和表 3。

<div style="text-align: center;">表 2 养老保险个人基本信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003007</td><td style='text-align: center;'>EAZ049</td><td style='text-align: center;'>开户银行名称</td><td style='text-align: center;'>C..128</td></tr></table>

## 表 2（续）


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>003008</td><td style='text-align: center;'>AAE010</td><td style='text-align: center;'>银行账号</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003009</td><td style='text-align: center;'>AAE009</td><td style='text-align: center;'>银行账户名称</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003010</td><td style='text-align: center;'>AAC004</td><td style='text-align: center;'>性别代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>003011</td><td style='text-align: center;'>AAC004N</td><td style='text-align: center;'>性别</td><td style='text-align: center;'>C..8</td></tr><tr><td style='text-align: center;'>003012</td><td style='text-align: center;'>AAC005</td><td style='text-align: center;'>民族代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>003013</td><td style='text-align: center;'>AAC005N</td><td style='text-align: center;'>民族</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003014</td><td style='text-align: center;'>AAC010</td><td style='text-align: center;'>户籍所在地</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003015</td><td style='text-align: center;'>AAC087</td><td style='text-align: center;'>荣誉称号级别代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>003016</td><td style='text-align: center;'>AAC087N</td><td style='text-align: center;'>荣誉称号级别</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003017</td><td style='text-align: center;'>AAC148</td><td style='text-align: center;'>困难人员类别代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>003018</td><td style='text-align: center;'>AAC148N</td><td style='text-align: center;'>困难人员类别</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003019</td><td style='text-align: center;'>AAC012</td><td style='text-align: center;'>个人身份代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003020</td><td style='text-align: center;'>AAC012N</td><td style='text-align: center;'>个人身份</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002015</td><td style='text-align: center;'>AAE005</td><td style='text-align: center;'>联系电话</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>002016</td><td style='text-align: center;'>AAE006</td><td style='text-align: center;'>地址</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003021</td><td style='text-align: center;'>AAF013</td><td style='text-align: center;'>街道或乡镇编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>003022</td><td style='text-align: center;'>AAF031</td><td style='text-align: center;'>街道或乡镇</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003023</td><td style='text-align: center;'>AAF030</td><td style='text-align: center;'>社区或村编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>003024</td><td style='text-align: center;'>AAF030N</td><td style='text-align: center;'>社区或村</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003025</td><td style='text-align: center;'>AAC016</td><td style='text-align: center;'>就业状态代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003026</td><td style='text-align: center;'>AAC016N</td><td style='text-align: center;'>就业状态名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003027</td><td style='text-align: center;'>AAC006</td><td style='text-align: center;'>出生日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>003028</td><td style='text-align: center;'>AAC007</td><td style='text-align: center;'>参加工作日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>007021</td><td style='text-align: center;'>AAE200</td><td style='text-align: center;'>视同缴费月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>003029</td><td style='text-align: center;'>AIC162</td><td style='text-align: center;'>离退休日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>003030</td><td style='text-align: center;'>AAE138</td><td style='text-align: center;'>死亡日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>003031</td><td style='text-align: center;'>AAC014</td><td style='text-align: center;'>专业技术职务级别代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>003032</td><td style='text-align: center;'>AAC014N</td><td style='text-align: center;'>专业技术职务级别</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003033</td><td style='text-align: center;'>AAC015</td><td style='text-align: center;'>国家职业资格等级代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003034</td><td style='text-align: center;'>AAC015N</td><td style='text-align: center;'>国家职业资格等级</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003035</td><td style='text-align: center;'>AAC020</td><td style='text-align: center;'>行政职务级别代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>003036</td><td style='text-align: center;'>AAC020N</td><td style='text-align: center;'>行政职务级别</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003037</td><td style='text-align: center;'>AAC064</td><td style='text-align: center;'>退役军人类别代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>003038</td><td style='text-align: center;'>AAC064N</td><td style='text-align: center;'>退役军人类别</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 3 养老保险死亡人员信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003010</td><td style='text-align: center;'>AAC004</td><td style='text-align: center;'>性别代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>003011</td><td style='text-align: center;'>AAC004N</td><td style='text-align: center;'>性别</td><td style='text-align: center;'>C..8</td></tr><tr><td style='text-align: center;'>003030</td><td style='text-align: center;'>AAE138</td><td style='text-align: center;'>死亡日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>006001</td><td style='text-align: center;'>AAE201</td><td style='text-align: center;'>实际缴费月数</td><td style='text-align: center;'>I..3</td></tr><tr><td style='text-align: center;'>006002</td><td style='text-align: center;'>AIC268</td><td style='text-align: center;'>个人账户累计本息</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007001</td><td style='text-align: center;'>AIC249</td><td style='text-align: center;'>养老丧葬补助金</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007002</td><td style='text-align: center;'>AIC250</td><td style='text-align: center;'>养老抚恤金</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.4 参保信息类数据结构

参保信息类数据结构，见表 4～表 7。

<div style="text-align: center;">表 4 养老保险人员参保信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr></table>

<div style="text-align: center;">表 4 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>004002</td><td style='text-align: center;'>AAC049</td><td style='text-align: center;'>首次参保年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>004003</td><td style='text-align: center;'>AAC008</td><td style='text-align: center;'>个人参保状态</td><td style='text-align: center;'>C..10</td></tr><tr><td style='text-align: center;'>004004</td><td style='text-align: center;'>AAC031</td><td style='text-align: center;'>个人缴费状态代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>004005</td><td style='text-align: center;'>AAC031N</td><td style='text-align: center;'>个人缴费状态</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>006009</td><td style='text-align: center;'>AAE180</td><td style='text-align: center;'>缴费基数</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>004006</td><td style='text-align: center;'>AAE030</td><td style='text-align: center;'>本次开始日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>004007</td><td style='text-align: center;'>AAE031</td><td style='text-align: center;'>本次终止日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>006017</td><td style='text-align: center;'>AAE036</td><td style='text-align: center;'>经办日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 5 养老保险离退休人员基本信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr></table>

<div style="text-align: center;">表 5（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>003010</td><td style='text-align: center;'>AAC004</td><td style='text-align: center;'>性别代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>003011</td><td style='text-align: center;'>AAC004N</td><td style='text-align: center;'>性别</td><td style='text-align: center;'>C..8</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>007018</td><td style='text-align: center;'>AIC161</td><td style='text-align: center;'>离退休类别代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>007019</td><td style='text-align: center;'>AIC161N</td><td style='text-align: center;'>离退休类别</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>007020</td><td style='text-align: center;'>AAE211</td><td style='text-align: center;'>核定年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>003028</td><td style='text-align: center;'>AAC007</td><td style='text-align: center;'>参加工作日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>003029</td><td style='text-align: center;'>AIC162</td><td style='text-align: center;'>离退休日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>007006</td><td style='text-align: center;'>AIC160</td><td style='text-align: center;'>待遇享受开始年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>007021</td><td style='text-align: center;'>AAE200</td><td style='text-align: center;'>视同缴费月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>006001</td><td style='text-align: center;'>AAE201</td><td style='text-align: center;'>实际缴费月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>007022</td><td style='text-align: center;'>EAE027</td><td style='text-align: center;'>中断月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>007023</td><td style='text-align: center;'>EAC047</td><td style='text-align: center;'>累计缴费月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>007024</td><td style='text-align: center;'>AAC019</td><td style='text-align: center;'>特殊工种类型代码</td><td style='text-align: center;'>C..6</td></tr><tr><td style='text-align: center;'>007025</td><td style='text-align: center;'>AAC019N</td><td style='text-align: center;'>特殊工种类型</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>007026</td><td style='text-align: center;'>EAC065</td><td style='text-align: center;'>特殊工种月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>007027</td><td style='text-align: center;'>AIC165</td><td style='text-align: center;'>离退休时账户总金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007028</td><td style='text-align: center;'>EIC009</td><td style='text-align: center;'>退休时核定养老金</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007029</td><td style='text-align: center;'>AAC158</td><td style='text-align: center;'>低保对象标识</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>007030</td><td style='text-align: center;'>EAC062</td><td style='text-align: center;'>补发月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>007031</td><td style='text-align: center;'>EAC063</td><td style='text-align: center;'>补发总金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 6 养老保险个人账户明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr></table>

<div style="text-align: center;">表 6（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003025</td><td style='text-align: center;'>AAC016</td><td style='text-align: center;'>就业状态代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003026</td><td style='text-align: center;'>AAC016N</td><td style='text-align: center;'>就业状态名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>007032</td><td style='text-align: center;'>AAE001</td><td style='text-align: center;'>年度</td><td style='text-align: center;'>C4</td></tr><tr><td style='text-align: center;'>007033</td><td style='text-align: center;'>AIC200</td><td style='text-align: center;'>年初账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007034</td><td style='text-align: center;'>ZZB001</td><td style='text-align: center;'>当年账户本金划入</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007035</td><td style='text-align: center;'>ZZB002</td><td style='text-align: center;'>当年账户利息划入</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007036</td><td style='text-align: center;'>AIC340</td><td style='text-align: center;'>本年账户支出</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007037</td><td style='text-align: center;'>ZZB005</td><td style='text-align: center;'>年末账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007038</td><td style='text-align: center;'>AIC042</td><td style='text-align: center;'>历年缴纳月数</td><td style='text-align: center;'>L..3</td></tr><tr><td style='text-align: center;'>007039</td><td style='text-align: center;'>EAC039</td><td style='text-align: center;'>账户记息日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>007040</td><td style='text-align: center;'>EAC040</td><td style='text-align: center;'>养老账户状态代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>007041</td><td style='text-align: center;'>EAC040N</td><td style='text-align: center;'>养老账户状态</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 7 养老保险人员转移信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr></table>

表 7 (续)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>008001</td><td style='text-align: center;'>EAC071N</td><td style='text-align: center;'>转移方向</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>008002</td><td style='text-align: center;'>EAC071</td><td style='text-align: center;'>转移方向代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>008003</td><td style='text-align: center;'>AAC077</td><td style='text-align: center;'>对方社会保险机构名称</td><td style='text-align: center;'>C..100</td></tr><tr><td style='text-align: center;'>008004</td><td style='text-align: center;'>AAC076</td><td style='text-align: center;'>对方所在单位名称</td><td style='text-align: center;'>C..100</td></tr><tr><td style='text-align: center;'>007021</td><td style='text-align: center;'>AAE200</td><td style='text-align: center;'>视同缴费月数</td><td style='text-align: center;'>I..3</td></tr><tr><td style='text-align: center;'>006001</td><td style='text-align: center;'>AAE201</td><td style='text-align: center;'>实际缴费月数</td><td style='text-align: center;'>I..3</td></tr><tr><td style='text-align: center;'>008005</td><td style='text-align: center;'>AIC099</td><td style='text-align: center;'>转移个人划转金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>008006</td><td style='text-align: center;'>AIC100</td><td style='text-align: center;'>转移单位划转金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>008007</td><td style='text-align: center;'>AIC102</td><td style='text-align: center;'>基本养老保险基金转移总额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>008008</td><td style='text-align: center;'>AIC103</td><td style='text-align: center;'>统筹部分转移金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>006017</td><td style='text-align: center;'>AAE036</td><td style='text-align: center;'>经办日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>008009</td><td style='text-align: center;'>OAA027</td><td style='text-align: center;'>对方行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>008010</td><td style='text-align: center;'>OAA027N</td><td style='text-align: center;'>对方行政区划</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.5 单位缴费类数据结构

单位缴费类数据结构，见表 8 和表 9。

<div style="text-align: center;">表 8 职工基本养老保险单位征缴明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005003</td><td style='text-align: center;'>EAZ058</td><td style='text-align: center;'>结算单号</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>002007</td><td style='text-align: center;'>AAB019</td><td style='text-align: center;'>单位类型代码</td><td style='text-align: center;'>C..2</td></tr></table>

## 表 8 (续)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>002008</td><td style='text-align: center;'>AAB019N</td><td style='text-align: center;'>单位类型</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002009</td><td style='text-align: center;'>AAB020</td><td style='text-align: center;'>经济类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>002010</td><td style='text-align: center;'>AAB020N</td><td style='text-align: center;'>经济类型</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002011</td><td style='text-align: center;'>AAB021</td><td style='text-align: center;'>隶属关系代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>002012</td><td style='text-align: center;'>AAB021N</td><td style='text-align: center;'>隶属关系</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005004</td><td style='text-align: center;'>AAE002</td><td style='text-align: center;'>结算年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005005</td><td style='text-align: center;'>AAE003</td><td style='text-align: center;'>应缴年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005006</td><td style='text-align: center;'>EAD131</td><td style='text-align: center;'>到账日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>005007</td><td style='text-align: center;'>AAB033</td><td style='text-align: center;'>征缴方式代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005008</td><td style='text-align: center;'>AAB033N</td><td style='text-align: center;'>征缴方式</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005009</td><td style='text-align: center;'>AAE078</td><td style='text-align: center;'>足额到账标志代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005010</td><td style='text-align: center;'>AAE078N</td><td style='text-align: center;'>足额到账标志</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005011</td><td style='text-align: center;'>AAA115</td><td style='text-align: center;'>应缴类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>005012</td><td style='text-align: center;'>AAA115N</td><td style='text-align: center;'>应缴类型</td><td style='text-align: center;'>C..40</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005015</td><td style='text-align: center;'>AAB119</td><td style='text-align: center;'>应征人数</td><td style='text-align: center;'>L..6</td></tr><tr><td style='text-align: center;'>005016</td><td style='text-align: center;'>AAE058</td><td style='text-align: center;'>应缴总金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005017</td><td style='text-align: center;'>AAB121</td><td style='text-align: center;'>单位缴费基数总额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005018</td><td style='text-align: center;'>AAB120</td><td style='text-align: center;'>个人缴费基数总额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005019</td><td style='text-align: center;'>AAE020</td><td style='text-align: center;'>单位应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005020</td><td style='text-align: center;'>AAE022</td><td style='text-align: center;'>个人应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005021</td><td style='text-align: center;'>AAB204</td><td style='text-align: center;'>滞纳金金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005022</td><td style='text-align: center;'>AAE021</td><td style='text-align: center;'>单位划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005023</td><td style='text-align: center;'>AAE023</td><td style='text-align: center;'>个人划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005025</td><td style='text-align: center;'>AAE080</td><td style='text-align: center;'>单位实缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005026</td><td style='text-align: center;'>AAE081</td><td style='text-align: center;'>单位实缴划入个人账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005027</td><td style='text-align: center;'>AAE082</td><td style='text-align: center;'>个人实缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005028</td><td style='text-align: center;'>AAE083</td><td style='text-align: center;'>个人实缴划入个人账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 9 机关事业单位养老保险单位征缴明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005003</td><td style='text-align: center;'>EAZ058</td><td style='text-align: center;'>结算单号</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>002007</td><td style='text-align: center;'>AAB019</td><td style='text-align: center;'>单位类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>002008</td><td style='text-align: center;'>AAB019N</td><td style='text-align: center;'>单位类型</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002011</td><td style='text-align: center;'>AAB021</td><td style='text-align: center;'>隶属关系代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>002012</td><td style='text-align: center;'>AAB021N</td><td style='text-align: center;'>隶属关系</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005004</td><td style='text-align: center;'>AAE002</td><td style='text-align: center;'>结算年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005005</td><td style='text-align: center;'>AAE003</td><td style='text-align: center;'>应缴年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005006</td><td style='text-align: center;'>EAD131</td><td style='text-align: center;'>到账日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>005007</td><td style='text-align: center;'>AAB033</td><td style='text-align: center;'>征缴方式代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005008</td><td style='text-align: center;'>AAB033N</td><td style='text-align: center;'>征缴方式</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005009</td><td style='text-align: center;'>AAE078</td><td style='text-align: center;'>足额到账标志代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005010</td><td style='text-align: center;'>AAE078N</td><td style='text-align: center;'>足额到账标志</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005011</td><td style='text-align: center;'>AAA115</td><td style='text-align: center;'>应缴类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>005012</td><td style='text-align: center;'>AAA115N</td><td style='text-align: center;'>应缴类型</td><td style='text-align: center;'>C..40</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005015</td><td style='text-align: center;'>AAB119</td><td style='text-align: center;'>应征人数</td><td style='text-align: center;'>I..6</td></tr><tr><td style='text-align: center;'>005016</td><td style='text-align: center;'>AAE058</td><td style='text-align: center;'>应缴总金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005017</td><td style='text-align: center;'>AAB121</td><td style='text-align: center;'>单位缴费基数总额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005018</td><td style='text-align: center;'>AAB120</td><td style='text-align: center;'>个人缴费基数总额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005019</td><td style='text-align: center;'>AAE020</td><td style='text-align: center;'>单位应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005020</td><td style='text-align: center;'>AAE022</td><td style='text-align: center;'>个人应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005021</td><td style='text-align: center;'>AAB204</td><td style='text-align: center;'>滞纳金金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005022</td><td style='text-align: center;'>AAE021</td><td style='text-align: center;'>单位划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005023</td><td style='text-align: center;'>AAE023</td><td style='text-align: center;'>个人划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005025</td><td style='text-align: center;'>AAE080</td><td style='text-align: center;'>单位实缴金额</td><td style='text-align: center;'>D16.2</td></tr></table>

表 9 (续)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>005026</td><td style='text-align: center;'>AAE081</td><td style='text-align: center;'>单位实缴划入个人账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005027</td><td style='text-align: center;'>AAE082</td><td style='text-align: center;'>个人实缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005028</td><td style='text-align: center;'>AAE083</td><td style='text-align: center;'>个人实缴划入个人账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.6 个人缴费类数据结构

个人缴费类数据结构，见表 10～表 12。

<div style="text-align: center;">表 10 城乡居民基本养老保险个人征缴明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003021</td><td style='text-align: center;'>AAF013</td><td style='text-align: center;'>街道或乡镇编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>003022</td><td style='text-align: center;'>AAF031</td><td style='text-align: center;'>街道或乡镇</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003023</td><td style='text-align: center;'>AAF030</td><td style='text-align: center;'>社区或村编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>003024</td><td style='text-align: center;'>AAF030N</td><td style='text-align: center;'>社区或村</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>005011</td><td style='text-align: center;'>AAA115</td><td style='text-align: center;'>应缴类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>005012</td><td style='text-align: center;'>AAA115N</td><td style='text-align: center;'>应缴类型</td><td style='text-align: center;'>C..40</td></tr><tr><td style='text-align: center;'>005024</td><td style='text-align: center;'>AAE101</td><td style='text-align: center;'>应缴年度</td><td style='text-align: center;'>C4</td></tr><tr><td style='text-align: center;'>005004</td><td style='text-align: center;'>AAE002</td><td style='text-align: center;'>结算年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005020</td><td style='text-align: center;'>AAE022</td><td style='text-align: center;'>个人应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005027</td><td style='text-align: center;'>AAE082</td><td style='text-align: center;'>个人实缴金额</td><td style='text-align: center;'>D16.2</td></tr></table>

<div style="text-align: center;">表 10 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>006003</td><td style='text-align: center;'>AAF027</td><td style='text-align: center;'>划入个人账户金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006004</td><td style='text-align: center;'>AAE034</td><td style='text-align: center;'>中央财政补贴</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006005</td><td style='text-align: center;'>AAE024</td><td style='text-align: center;'>省级财政补贴</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006006</td><td style='text-align: center;'>AAE026</td><td style='text-align: center;'>市级财政补贴</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006007</td><td style='text-align: center;'>AAE028</td><td style='text-align: center;'>县区财政补贴</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005009</td><td style='text-align: center;'>AAE078</td><td style='text-align: center;'>足额到账标志代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005010</td><td style='text-align: center;'>AAE078N</td><td style='text-align: center;'>足额到账标志</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005006</td><td style='text-align: center;'>EAD131</td><td style='text-align: center;'>到账日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>006008</td><td style='text-align: center;'>AIC079</td><td style='text-align: center;'>本年缴费月数</td><td style='text-align: center;'>L.3</td></tr><tr><td style='text-align: center;'>005007</td><td style='text-align: center;'>AAB033</td><td style='text-align: center;'>征缴方式代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005008</td><td style='text-align: center;'>AAB033N</td><td style='text-align: center;'>征缴方式</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 11 职工基本养老保险个人征缴明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005003</td><td style='text-align: center;'>EAZ058</td><td style='text-align: center;'>结算单号</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>005004</td><td style='text-align: center;'>AAE002</td><td style='text-align: center;'>结算年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005005</td><td style='text-align: center;'>AAE003</td><td style='text-align: center;'>应缴年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005011</td><td style='text-align: center;'>AAA115</td><td style='text-align: center;'>应缴类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>005012</td><td style='text-align: center;'>AAA115N</td><td style='text-align: center;'>应缴类型</td><td style='text-align: center;'>C..40</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr></table>

<div style="text-align: center;">表 11（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005016</td><td style='text-align: center;'>AAE058</td><td style='text-align: center;'>应缴总金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006009</td><td style='text-align: center;'>AAE180</td><td style='text-align: center;'>缴费基数</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006010</td><td style='text-align: center;'>AAA042</td><td style='text-align: center;'>单位缴费比例</td><td style='text-align: center;'>D16.4</td></tr><tr><td style='text-align: center;'>005019</td><td style='text-align: center;'>AAE020</td><td style='text-align: center;'>单位应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005022</td><td style='text-align: center;'>AAE021</td><td style='text-align: center;'>单位划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006011</td><td style='text-align: center;'>AAA041</td><td style='text-align: center;'>个人缴费比例</td><td style='text-align: center;'>D16.4</td></tr><tr><td style='text-align: center;'>005020</td><td style='text-align: center;'>AAE022</td><td style='text-align: center;'>个人应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005027</td><td style='text-align: center;'>AAE082</td><td style='text-align: center;'>个人实缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005023</td><td style='text-align: center;'>AAE023</td><td style='text-align: center;'>个人划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006012</td><td style='text-align: center;'>AAE025</td><td style='text-align: center;'>财政划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006013</td><td style='text-align: center;'>ZZB004</td><td style='text-align: center;'>其他补充金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006014</td><td style='text-align: center;'>AAE027</td><td style='text-align: center;'>其他划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006015</td><td style='text-align: center;'>AAE017</td><td style='text-align: center;'>核销标志</td><td style='text-align: center;'>C..10</td></tr><tr><td style='text-align: center;'>005009</td><td style='text-align: center;'>AAE078</td><td style='text-align: center;'>足额到账标志代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005010</td><td style='text-align: center;'>AAE078N</td><td style='text-align: center;'>足额到账标志</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005006</td><td style='text-align: center;'>EAD131</td><td style='text-align: center;'>到账日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>006017</td><td style='text-align: center;'>AAE036</td><td style='text-align: center;'>经办日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 12 机关事业单位养老保险个人征缴明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005003</td><td style='text-align: center;'>EAZ058</td><td style='text-align: center;'>结算单号</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>005004</td><td style='text-align: center;'>AAE002</td><td style='text-align: center;'>结算年月</td><td style='text-align: center;'>C6</td></tr></table>

<div style="text-align: center;">表 12（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>005005</td><td style='text-align: center;'>AAE003</td><td style='text-align: center;'>应缴年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>005011</td><td style='text-align: center;'>AAA115</td><td style='text-align: center;'>应缴类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>005012</td><td style='text-align: center;'>AAA115N</td><td style='text-align: center;'>应缴类型</td><td style='text-align: center;'>C..40</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005016</td><td style='text-align: center;'>AAE058</td><td style='text-align: center;'>应缴总金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006009</td><td style='text-align: center;'>AAE180</td><td style='text-align: center;'>缴费基数</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006010</td><td style='text-align: center;'>AAA042</td><td style='text-align: center;'>单位缴费比例</td><td style='text-align: center;'>D16.4</td></tr><tr><td style='text-align: center;'>005019</td><td style='text-align: center;'>AAE020</td><td style='text-align: center;'>单位应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005022</td><td style='text-align: center;'>AAE021</td><td style='text-align: center;'>单位划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006011</td><td style='text-align: center;'>AAA041</td><td style='text-align: center;'>个人缴费比例</td><td style='text-align: center;'>D16.4</td></tr><tr><td style='text-align: center;'>005020</td><td style='text-align: center;'>AAE022</td><td style='text-align: center;'>个人应缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005027</td><td style='text-align: center;'>AAE082</td><td style='text-align: center;'>个人实缴金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>005023</td><td style='text-align: center;'>AAE023</td><td style='text-align: center;'>个人划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006012</td><td style='text-align: center;'>AAE025</td><td style='text-align: center;'>财政划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006013</td><td style='text-align: center;'>ZZB004</td><td style='text-align: center;'>其他补充金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006014</td><td style='text-align: center;'>AAE027</td><td style='text-align: center;'>其他划账金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>006015</td><td style='text-align: center;'>AAE017</td><td style='text-align: center;'>核销标志</td><td style='text-align: center;'>C..10</td></tr><tr><td style='text-align: center;'>005009</td><td style='text-align: center;'>AAE078</td><td style='text-align: center;'>足额到账标志代码</td><td style='text-align: center;'>C..1</td></tr><tr><td style='text-align: center;'>005010</td><td style='text-align: center;'>AAE078N</td><td style='text-align: center;'>足额到账标志</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>005006</td><td style='text-align: center;'>EAD131</td><td style='text-align: center;'>到账日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>006017</td><td style='text-align: center;'>AAE036</td><td style='text-align: center;'>经办日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.7 待遇支付类数据结构

待遇支付类数据结构，见表 13。

<div style="text-align: center;">表 13 养老保险待遇支付明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>007003</td><td style='text-align: center;'>EAZ048</td><td style='text-align: center;'>待遇支付明细序号</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>002002</td><td style='text-align: center;'>AAB004</td><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>005004</td><td style='text-align: center;'>AAE002</td><td style='text-align: center;'>结算年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>007044</td><td style='text-align: center;'>EAC064</td><td style='text-align: center;'>待遇年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>007004</td><td style='text-align: center;'>AAA036</td><td style='text-align: center;'>待遇项目代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>007005</td><td style='text-align: center;'>AAA037</td><td style='text-align: center;'>待遇项目名称</td><td style='text-align: center;'>C..50</td></tr><tr><td style='text-align: center;'>007006</td><td style='text-align: center;'>AIC160</td><td style='text-align: center;'>待遇享受开始年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>007007</td><td style='text-align: center;'>EIC013</td><td style='text-align: center;'>个账支付金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007008</td><td style='text-align: center;'>AAE019</td><td style='text-align: center;'>待遇金额</td><td style='text-align: center;'>D16.2</td></tr><tr><td style='text-align: center;'>007009</td><td style='text-align: center;'>AAE133</td><td style='text-align: center;'>领取人姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>007010</td><td style='text-align: center;'>EAE021</td><td style='text-align: center;'>领取关系</td><td style='text-align: center;'>C..8</td></tr><tr><td style='text-align: center;'>007011</td><td style='text-align: center;'>AAE136</td><td style='text-align: center;'>领取人证件号码</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003007</td><td style='text-align: center;'>EAZ049</td><td style='text-align: center;'>开户银行名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>003009</td><td style='text-align: center;'>AAE009</td><td style='text-align: center;'>银行账户名称</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003008</td><td style='text-align: center;'>AAE010</td><td style='text-align: center;'>银行账号</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>007012</td><td style='text-align: center;'>AAE145</td><td style='text-align: center;'>待遇发放方式代码</td><td style='text-align: center;'>C..2</td></tr></table>

<div style="text-align: center;">表 13 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>007013</td><td style='text-align: center;'>AAE145N</td><td style='text-align: center;'>待遇发放方式</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>007014</td><td style='text-align: center;'>EAE004</td><td style='text-align: center;'>待遇项目支付类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>007015</td><td style='text-align: center;'>EAE004N</td><td style='text-align: center;'>待遇项目支付类型</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>007016</td><td style='text-align: center;'>EAE005</td><td style='text-align: center;'>统筹类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>007017</td><td style='text-align: center;'>EAE005N</td><td style='text-align: center;'>统筹类型</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>006017</td><td style='text-align: center;'>AAE036</td><td style='text-align: center;'>经办日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.8 信息变更类数据结构

信息变更类数据结构，见表 14 和表 15。

<div style="text-align: center;">表 14 养老保险单位变更信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>002001</td><td style='text-align: center;'>AAB001</td><td style='text-align: center;'>单位编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>008011</td><td style='text-align: center;'>AAB100</td><td style='text-align: center;'>单位变更类型代码</td><td style='text-align: center;'>C..10</td></tr><tr><td style='text-align: center;'>008012</td><td style='text-align: center;'>AAB100N</td><td style='text-align: center;'>单位变更类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>008013</td><td style='text-align: center;'>AAE123</td><td style='text-align: center;'>变更前信息</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008014</td><td style='text-align: center;'>AAE124</td><td style='text-align: center;'>变更后信息</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008015</td><td style='text-align: center;'>AAE160</td><td style='text-align: center;'>变更原因代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>008016</td><td style='text-align: center;'>AAE160N</td><td style='text-align: center;'>变更原因</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008017</td><td style='text-align: center;'>AAE035</td><td style='text-align: center;'>变更日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 15 养老保险人员参保情况变更信息表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>006016</td><td style='text-align: center;'>AAE011</td><td style='text-align: center;'>经办人</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008018</td><td style='text-align: center;'>AAZ308</td><td style='text-align: center;'>人员变更流水号</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003001</td><td style='text-align: center;'>AAC001</td><td style='text-align: center;'>人员编码</td><td style='text-align: center;'>C..20</td></tr><tr><td style='text-align: center;'>003003</td><td style='text-align: center;'>AAC003</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>003002</td><td style='text-align: center;'>AAC002</td><td style='text-align: center;'>社会保障号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003005</td><td style='text-align: center;'>AAA029N</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>003004</td><td style='text-align: center;'>AAA029</td><td style='text-align: center;'>证件类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>003006</td><td style='text-align: center;'>AAE135</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>004002</td><td style='text-align: center;'>AAC049</td><td style='text-align: center;'>首次参保年月</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>008019</td><td style='text-align: center;'>AAC050</td><td style='text-align: center;'>个人变更类型代码</td><td style='text-align: center;'>C..10</td></tr><tr><td style='text-align: center;'>008020</td><td style='text-align: center;'>AAC050N</td><td style='text-align: center;'>个人变更类型</td><td style='text-align: center;'>C..10</td></tr><tr><td style='text-align: center;'>008015</td><td style='text-align: center;'>AAE160</td><td style='text-align: center;'>变更原因代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>008016</td><td style='text-align: center;'>AAE160N</td><td style='text-align: center;'>变更原因</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008013</td><td style='text-align: center;'>AAE123</td><td style='text-align: center;'>变更前信息</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008014</td><td style='text-align: center;'>AAE124</td><td style='text-align: center;'>变更后信息</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>008017</td><td style='text-align: center;'>AAE035</td><td style='text-align: center;'>变更日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.9 参数信息类数据结构

参数信息类数据结构，见表 16 和表 17。

<div style="text-align: center;">表 16 参数表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr></table>

<div style="text-align: center;">表 16（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>009001</td><td style='text-align: center;'>AAA002</td><td style='text-align: center;'>参数类别编码</td><td style='text-align: center;'>C..50</td></tr><tr><td style='text-align: center;'>009002</td><td style='text-align: center;'>AAA101</td><td style='text-align: center;'>参数类别名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>009003</td><td style='text-align: center;'>AAA102</td><td style='text-align: center;'>参数值</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>009004</td><td style='text-align: center;'>EAA023</td><td style='text-align: center;'>参数名称</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>008017</td><td style='text-align: center;'>AAE035</td><td style='text-align: center;'>变更日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>009005</td><td style='text-align: center;'>AAE100</td><td style='text-align: center;'>有效标志</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 17 养老待遇类型表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>005013</td><td style='text-align: center;'>AAE140</td><td style='text-align: center;'>险种代码</td><td style='text-align: center;'>C..3</td></tr><tr><td style='text-align: center;'>005014</td><td style='text-align: center;'>AAE140N</td><td style='text-align: center;'>险种名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>007004</td><td style='text-align: center;'>AAA036</td><td style='text-align: center;'>待遇项目代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>007005</td><td style='text-align: center;'>AAA037</td><td style='text-align: center;'>待遇项目名称</td><td style='text-align: center;'>C..50</td></tr><tr><td style='text-align: center;'>007014</td><td style='text-align: center;'>EAE004</td><td style='text-align: center;'>待遇项目支付类型代码</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>007015</td><td style='text-align: center;'>EAE004N</td><td style='text-align: center;'>待遇项目支付类型</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>007016</td><td style='text-align: center;'>EAE005</td><td style='text-align: center;'>统筹类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>007017</td><td style='text-align: center;'>EAE005N</td><td style='text-align: center;'>统筹类型</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>007042</td><td style='text-align: center;'>AAA157</td><td style='text-align: center;'>基金列支类型代码</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>007043</td><td style='text-align: center;'>AAA157N</td><td style='text-align: center;'>基金列支类型</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>009005</td><td style='text-align: center;'>AAE100</td><td style='text-align: center;'>有效标志</td><td style='text-align: center;'>C..2</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

#### 5.2.10 财务类数据结构

财务类数据结构，见表 18～表 20。

<div style="text-align: center;">表 18 会计科目表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>010001</td><td style='text-align: center;'>ZZA101</td><td style='text-align: center;'>账套号</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>010002</td><td style='text-align: center;'>ZZA101N</td><td style='text-align: center;'>账套名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>010003</td><td style='text-align: center;'>AAD081</td><td style='text-align: center;'>会计年度</td><td style='text-align: center;'>C4</td></tr><tr><td style='text-align: center;'>010004</td><td style='text-align: center;'>EAD004</td><td style='text-align: center;'>科目编码</td><td style='text-align: center;'>C..60</td></tr><tr><td style='text-align: center;'>010005</td><td style='text-align: center;'>EAD006</td><td style='text-align: center;'>科目名称</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>010006</td><td style='text-align: center;'>EAD011</td><td style='text-align: center;'>余额方向</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

<div style="text-align: center;">表 19 科目余额表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>010001</td><td style='text-align: center;'>ZZA101</td><td style='text-align: center;'>账套号</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>010002</td><td style='text-align: center;'>ZZA101N</td><td style='text-align: center;'>账套名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>010004</td><td style='text-align: center;'>EAD004</td><td style='text-align: center;'>科目编码</td><td style='text-align: center;'>C..60</td></tr><tr><td style='text-align: center;'>010005</td><td style='text-align: center;'>EAD006</td><td style='text-align: center;'>科目名称</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>010003</td><td style='text-align: center;'>AAD081</td><td style='text-align: center;'>会计年度</td><td style='text-align: center;'>C4</td></tr><tr><td style='text-align: center;'>010007</td><td style='text-align: center;'>AAD082</td><td style='text-align: center;'>会计期间</td><td style='text-align: center;'>C..15</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>010006</td><td style='text-align: center;'>EAD011</td><td style='text-align: center;'>余额方向</td><td style='text-align: center;'>C..4</td></tr><tr><td style='text-align: center;'>010008</td><td style='text-align: center;'>AAD087</td><td style='text-align: center;'>期初余额</td><td style='text-align: center;'>D20.2</td></tr><tr><td style='text-align: center;'>010009</td><td style='text-align: center;'>AAD088</td><td style='text-align: center;'>本期借方发生额</td><td style='text-align: center;'>D20.2</td></tr><tr><td style='text-align: center;'>010010</td><td style='text-align: center;'>AAD089</td><td style='text-align: center;'>本期贷方发生额</td><td style='text-align: center;'>D20.2</td></tr><tr><td style='text-align: center;'>010011</td><td style='text-align: center;'>AAD092</td><td style='text-align: center;'>期末余额</td><td style='text-align: center;'>D20.2</td></tr></table>

<div style="text-align: center;">表 20 凭证明细表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>标识符</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>中文注释</td><td style='text-align: center;'>表示</td></tr><tr><td style='text-align: center;'>001001</td><td style='text-align: center;'>ZZZ001</td><td style='text-align: center;'>时间属性</td><td style='text-align: center;'>C16</td></tr><tr><td style='text-align: center;'>001002</td><td style='text-align: center;'>ZZZ002</td><td style='text-align: center;'>地域属性</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001003</td><td style='text-align: center;'>AAB301</td><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>C6</td></tr><tr><td style='text-align: center;'>001004</td><td style='text-align: center;'>AAA146</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>001005</td><td style='text-align: center;'>AAB034</td><td style='text-align: center;'>经办机构编码</td><td style='text-align: center;'>C..16</td></tr><tr><td style='text-align: center;'>001006</td><td style='text-align: center;'>AAB034N</td><td style='text-align: center;'>经办机构</td><td style='text-align: center;'>C..128</td></tr><tr><td style='text-align: center;'>010001</td><td style='text-align: center;'>ZZA101</td><td style='text-align: center;'>账套号</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>010002</td><td style='text-align: center;'>ZZA101N</td><td style='text-align: center;'>账套名称</td><td style='text-align: center;'>C..32</td></tr><tr><td style='text-align: center;'>010003</td><td style='text-align: center;'>AAD081</td><td style='text-align: center;'>会计年度</td><td style='text-align: center;'>C4</td></tr><tr><td style='text-align: center;'>010007</td><td style='text-align: center;'>AAD082</td><td style='text-align: center;'>会计期间</td><td style='text-align: center;'>C..15</td></tr><tr><td style='text-align: center;'>010012</td><td style='text-align: center;'>AAD131</td><td style='text-align: center;'>凭证编号</td><td style='text-align: center;'>C..60</td></tr><tr><td style='text-align: center;'>010013</td><td style='text-align: center;'>AAD138</td><td style='text-align: center;'>凭证日期</td><td style='text-align: center;'>C8</td></tr><tr><td style='text-align: center;'>010004</td><td style='text-align: center;'>EAD004</td><td style='text-align: center;'>科目编码</td><td style='text-align: center;'>C..60</td></tr><tr><td style='text-align: center;'>010005</td><td style='text-align: center;'>EAD006</td><td style='text-align: center;'>科目名称</td><td style='text-align: center;'>C..64</td></tr><tr><td style='text-align: center;'>010014</td><td style='text-align: center;'>AAD128</td><td style='text-align: center;'>摘要</td><td style='text-align: center;'>C..300</td></tr><tr><td style='text-align: center;'>010015</td><td style='text-align: center;'>EAD143</td><td style='text-align: center;'>借方金额</td><td style='text-align: center;'>D20.2</td></tr><tr><td style='text-align: center;'>010016</td><td style='text-align: center;'>EAD144</td><td style='text-align: center;'>贷方金额</td><td style='text-align: center;'>D20.2</td></tr><tr><td style='text-align: center;'>010017</td><td style='text-align: center;'>ZZA001</td><td style='text-align: center;'>制单人</td><td style='text-align: center;'>C..30</td></tr><tr><td style='text-align: center;'>010018</td><td style='text-align: center;'>ZZA002</td><td style='text-align: center;'>审核人</td><td style='text-align: center;'>C..30</td></tr><tr><td style='text-align: center;'>010019</td><td style='text-align: center;'>ZZA003</td><td style='text-align: center;'>记账人</td><td style='text-align: center;'>C..30</td></tr><tr><td style='text-align: center;'>001007</td><td style='text-align: center;'>ZZZ003</td><td style='text-align: center;'>修改时间</td><td style='text-align: center;'>C8</td></tr></table>

### 5.3 输出文件的输出说明

本标准要求按照 5.2 数据结构的各项数据内容全部输出。

### 5.4 输出文件的时间要求

本标准规定的养老保险审计数据接口数据文件的输出时间要求见表21。

<div style="text-align: center;">表 21 养老保险审计数据接口数据文件的输出时间要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>分类</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>数据表名称</td><td style='text-align: center;'>输出时间要求</td></tr><tr><td style='text-align: center;'>单位信息</td><td style='text-align: center;'>表1</td><td style='text-align: center;'>养老保险单位基本信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="2">人员信息</td><td style='text-align: center;'>表2</td><td style='text-align: center;'>养老保险个人基本信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表3</td><td style='text-align: center;'>养老保险死亡人员信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="4">参保信息</td><td style='text-align: center;'>表4</td><td style='text-align: center;'>养老保险人员参保信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表5</td><td style='text-align: center;'>养老保险离退休人员基本信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表6</td><td style='text-align: center;'>养老保险个人账户明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表7</td><td style='text-align: center;'>养老保险人员转移信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="2">单位缴费</td><td style='text-align: center;'>表8</td><td style='text-align: center;'>职工基本养老保险单位征缴明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表9</td><td style='text-align: center;'>机关事业单位养老保险单位征缴明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="3">个人缴费</td><td style='text-align: center;'>表10</td><td style='text-align: center;'>城乡居民基本养老保险个人征缴明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表11</td><td style='text-align: center;'>职工基本养老保险个人征缴明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表12</td><td style='text-align: center;'>机关事业单位养老保险个人征缴明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>待遇支付</td><td style='text-align: center;'>表13</td><td style='text-align: center;'>养老保险待遇支付明细表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="2">信息变更</td><td style='text-align: center;'>表14</td><td style='text-align: center;'>养老保险单位变更信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表15</td><td style='text-align: center;'>养老保险人员参保情况变更信息表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="2">参数信息</td><td style='text-align: center;'>表16</td><td style='text-align: center;'>参数表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表17</td><td style='text-align: center;'>养老待遇类型表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td rowspan="3">财务类</td><td style='text-align: center;'>表18</td><td style='text-align: center;'>会计科目表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表19</td><td style='text-align: center;'>科目余额表</td><td style='text-align: center;'>一次性输出</td></tr><tr><td style='text-align: center;'>表20</td><td style='text-align: center;'>凭证明细表</td><td style='text-align: center;'>一次性输出</td></tr></table>

## 6 符合性评价

声称符合本标准的产品应符合第 4 章和第 5 章的要求。均应获得指定机构的标准符合性证明。

# 附录 A （资料性附录） 养老保险基金审计数据接口的 XML 大纲

### A.1 标准元素类型类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:attribute name="locID">
        <xs:annotation>
            <xs:documentation>数据标识符</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:attribute>
    <xs:simpleType name="时间属性类型">
        <xs:restriction base="xs:string">
            <xs:Length value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="地域属性类型">
        <xs:restriction base="xs:string">
            <xs:Length value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="行政区划代码类型">
        <xs:restriction base="xs:string">
            <xs:Length value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="行政区划类型">
        <xs:restriction base="xs:string">
            <xs:maxLength value="128"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="经办机构编码类型">

<xs:restriction base="xs:string">
    <xs:maxLength value="16"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="经办机构类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="修改时间类型">
    <xs:restriction base="xs:string">
        <xs:Length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位编码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="统一社会信用代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="18"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="法定代表人姓名类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="法定代表人证件号码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

</xs:simpleType>

<xs:simpleType name="单位类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="经济类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="经济类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="隶属关系代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="隶属关系类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="行业代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="行业名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="联系电话类型">
    <xs:restriction base="xs:string">

<xs:maxLength value="32"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="地址类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="人员编码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="20"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="社会保障号码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="姓名类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="证件类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="证件类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="证件号码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="开户银行名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="银行账号类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="银行账户名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="性别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="1"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="性别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="民族代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="民族类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="户籍所在地类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="荣誉称号级别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="1"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="荣誉称号级别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="困难人员类别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="1"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="困难人员类别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个人身份代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个人身份类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="街道或乡镇编码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="街道或乡镇类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="社区或村编码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="社区或村类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:restriction base="xs:string">
    <xs:maxLength value="4"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="就业状态名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="出生日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="参加工作日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="离退休日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="死亡日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="专业技术职务级别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="3"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="专业技术职务级别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="国家职业资格等级代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

</xs:simpleType>

<xs:simpleType name="国家职业资格等级类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="行政职务级别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="3"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="行政职务级别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="退役军人类别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="退役军人类别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位参保日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="首次参保年月类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个人参保状态类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="10"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个人缴费状态代码类型">
    <xs:restriction base="xs:string">

<xs:maxLength value="1"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="个人缴费状态类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="本次开始日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="本次终止日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位缴费状态代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="1"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位缴费状态类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="结算单号类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="20"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="结算年月类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="应缴年月类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="到账日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="征缴方式代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="1"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="征缴方式类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="足额到账标志代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="1"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="足额到账标志类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="应缴类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="应缴类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="40"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="险种代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="3"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="险种名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="应征人数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="应缴总金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="单位缴费基数总额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="个人缴费基数总额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="单位应缴金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="个人应缴金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="滞纳金金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="单位划账金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="个人划账金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="应缴年度类型">
    <xs:restriction base="xs:string">
        <xs:length value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位实缴金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="单位实缴划入个人账户金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="个人实缴金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="个人实缴划入个人账户金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="实际缴费月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="个人账户累计本息类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="划入个人账户金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="中央财政补贴类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="省级财政补贴类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="市级财政补贴类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="县区财政补贴类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="本年缴费月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="缴费基数类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="单位缴费比例类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="财政划账金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="其他补充金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="其他划账金额类型">

<xs:restriction base="xs:decimal"/>

</xs:simpleType>

<xs:simpleType name="核销标志类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="10"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="经办人类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="经办日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="养老丧葬补助金类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="养老抚恤金类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="待遇支付明细序号类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇项目代码类型">
    <xs:restriction base="xs:string">
        <xs:Length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇项目名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="50"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇享受开始年月类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个账支付金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="待遇金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="领取人姓名类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="领取关系类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="领取人证件号码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇发放方式代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇发放方式类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇项目支付类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇项目支付类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="统筹类型代码类型">
    <xs:restriction base="xs:string">
        <xs:restriction base="xs:string">

<xs:maxLength value="4"/>
</xs:restriction>

<xs:simpleType name="统筹类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="离退休类别代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="离退休类别类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="核定年月类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="视同缴费月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="中断月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="累计缴费月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="特殊工种类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="特殊工种类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="20"/>
    </xs:restriction>
</xs:simpleType>

<xs:restriction base="xs:int"/>

</xs:simpleType>

<xs:simpleType name="离退休时账户总金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="退休时核定养老金类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="低保对象标识类型">
    <xs:restriction base="xs:string"/>
    <xs:maxLength value="1"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="补发月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="补发总金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="年度类型">
    <xs:restriction base="xs:string"/>
    <xs:length value="4"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="年初账户金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="当年账户本金划入类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="当年账户利息划入类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="本年账户支出类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="年末账户金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="历年缴纳月数类型">
    <xs:restriction base="xs:int"/>
</xs:simpleType>

<xs:simpleType name="账户记息日期类型">

<xs:restriction base="xs:string">
    <xs:length value="8"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="养老账户状态代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="3"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="养老账户状态类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="基金列支类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="基金列支类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="待遇年月类型">
    <xs:restriction base="xs:string">
        <xs:length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="转移方向类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="16"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="转移方向代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="对方社会保险机构名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="100"/>
    </xs:restriction>
</xs:simpleType>

</xs:simpleType>

<xs:simpleType name="对方所在单位名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="100"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="转移个人划转金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="转移单位划转金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="基本养老保险基金转移总额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="统筹部分转移金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="对方行政区划代码类型">
    <xs:restriction base="xs:string">
        <xs:Length value="6"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="对方行政区划类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位变更类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="10"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="单位变更类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="变更前信息类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="变更后信息类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="变更原因代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="变更原因类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="变更日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="人员变更流水号类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个人变更类型代码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="10"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="个人变更类型类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="10"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="参数类别编码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="50"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="参数类别名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="参数值类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="参数名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="128"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="有效标志类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="2"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="账套号类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="账套名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="32"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="会计年度类型">
    <xs:restriction base="xs:string">
        <xs:length value="4"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="科目编码类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="60"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="科目名称类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="64"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="余额方向类型">

<xs:restriction base="xs:string">
    <xs:maxLength value="4"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="会计期间类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="15"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="期初余额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="本期借方发生额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="本期贷方发生额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="期末余额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="凭证编号类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="60"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="凭证日期类型">
    <xs:restriction base="xs:string">
        <xs:length value="8"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="摘要类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="300"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="借方金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="贷方金额类型">
    <xs:restriction base="xs:decimal"/>
</xs:simpleType>

<xs:simpleType name="制单人类型">

<xs:restriction base="xs:string">
    <xs:maxLength value="30"/>
</xs:restriction>

</xs:simpleType>

<xs:simpleType name="审核人类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="30"/>
    </xs:restriction>
</xs:simpleType>

<xs:simpleType name="记账人类型">
    <xs:restriction base="xs:string">
        <xs:maxLength value="30"/>
    </xs:restriction>
</xs:simpleType>

</xs:schema>

### A.2 单位信息类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="单位信息">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="养老保险单位基本信息表"/>
            </xs:sequence>
            <xs:attribute ref="locID" use="optional" fixed="U01"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="养老保险单位基本信息表">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="时间属性">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="时间属性类型">
                                <xs:attribute ref="locID" use="optional" fixed="001001"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:schema>

</xs:complexType>

</xs:element>

<xs:element name="地域属性">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="地域属性类型">

<xs:attribute ref="locID" use="optional" fixed="001002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划代码类型">

<xs:attribute ref="locID" use="optional" fixed="001003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构类型">

<xs:attribute ref="locID" use="optional" fixed="001006"/>
</xs:extension>

</xs:complexType>

</xs:element>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位编码类型">

<xs:attribute ref="locID" use="optional" fixed="002001"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位名称类型">

<xs:attribute ref="locID" use="optional" fixed="002002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="统一社会信用代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="统一社会信用代码类型">

<xs:attribute ref="locID" use="optional" fixed="002003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="法定代表人姓名">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="法定代表人姓名类型">

<xs:attribute ref="locID" use="optional" fixed="002004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="法定代表人证件号码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="法定代表人证件号码类型">
    <xs:attribute ref="locID" use="optional" fixed="002005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="法定代表人电话">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="法定代表人电话类型">
                <xs:attribute ref="locID" use="optional" fixed="002006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位类型类型">
                <xs:attribute ref="locID" use="optional" fixed="002008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经济类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经济类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经济类型">
    <xs:extension base="经济类型代码类型">
        <xs:attribute ref="locID" use="optional" fixed="002009"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经济类型">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="经济类型类型">
            <xs:attribute ref="locID" use="optional" fixed="002010"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="隶属关系代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="隶属关系代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="隶属关系">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="隶属关系类型">
                <xs:attribute ref="locID" use="optional" fixed="002012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="行业代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行业代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="行业名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行业名称类型">
                <xs:attribute ref="locID" use="optional" fixed="002014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="联系电话">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="联系电话类型">
                <xs:attribute ref="locID" use="optional" fixed="002015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="地址">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="地址类型">
                <xs:attribute ref="locID" use="optional" fixed="002016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位缴费状态代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位缴费状态代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位缴费状态">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位缴费状态类型">
                <xs:attribute ref="locID" use="optional" fixed="005002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位参保日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位参保日期类型">
                <xs:attribute ref="locID" use="optional" fixed="004001"/>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">

<xs:attribute ref="locID" use="optional" fixed="001007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

### A.3 人员信息类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="人员信息">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="养老保险个人基本信息表"/>
                <xs:element name="养老保险死亡人员信息表"/>
            </xs:sequence>
            <xs:attribute ref="locID" use="optional" fixed="U02"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="养老保险个人基本信息表">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="时间属性">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="时间属性类型">
                                <xs:attribute ref="locID" use="optional" fixed="001001"/>
                            </xs:extension>
                        </xs:complexType>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:complexType>
    </xs:element>
</xs:schema>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

<xs:element name="地域属性">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="地域属性类型">

<xs:attribute ref="locID" use="optional" fixed="001002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划代码类型">

<xs:attribute ref="locID" use="optional" fixed="001003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构类型">
    <xs:attribute ref="locID" use="optional" fixed="001006"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型">
    <xs:extension base="证件类型代码类型">
        <xs:attribute ref="locID" use="optional" fixed="003004"/>
    </xs:extension>
</xs:simpleContent>

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="证件类型类型">
            <xs:attribute ref="locID" use="optional" fixed="003005"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="开户银行名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="开户银行名称类型">
                <xs:attribute ref="locID" use="optional" fixed="003007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="银行账号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="银行账号类型">
                <xs:attribute ref="locID" use="optional" fixed="003008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="银行账户名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="银行账户名称类型">
                <xs:attribute ref="locID" use="optional" fixed="003009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="性别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="性别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

    <xs:element name="性别">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="性别类型">
                    <xs:attribute ref="locID" use="optional" fixed="003011"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="民族代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="民族代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="003012"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="民族">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="民族类型">
                    <xs:attribute ref="locID" use="optional" fixed="003013"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="户籍所在地">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="户籍所在地类型">
                    <xs:attribute ref="locID" use="optional" fixed="003014"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:element>

</xs:simpleContent>
</xs:complexType>

<xs:element name="荣誉称号级别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="荣誉称号级别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="荣誉称号级别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="荣誉称号级别类型">
                <xs:attribute ref="locID" use="optional" fixed="003016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="困难人员类别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="困难人员类别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003017"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="困难人员类别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="困难人员类别类型">
                <xs:attribute ref="locID" use="optional" fixed="003018"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="个人身份代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人身份代码类型">
                <xs:extension base="个人身份代码类型">
                </xs:extension>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="003019"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人身份">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人身份类型">

<xs:attribute ref="locID" use="optional" fixed="003020"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="联系电话">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="联系电话类型">

<xs:attribute ref="locID" use="optional" fixed="002015"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="地址">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="地址类型">

<xs:attribute ref="locID" use="optional" fixed="002016"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="街道或乡镇代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="街道或乡镇编码类型">

<xs:attribute ref="locID" use="optional" fixed="003021"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="街道或乡镇">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="街道或乡镇类型">
        <xs:attribute ref="locID" use="optional" fixed="003022"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="社区或村编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社区或村编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003023"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社区或村">
    <xs:complexType>
        <xs:extension base="社区或村类型">
            <xs:attribute ref="locID" use="optional" fixed="003024"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="就业状态代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="就业状态代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003025"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="就业状态名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="就业状态名称类型">
                <xs:attribute ref="locID" use="optional" fixed="003026"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="出生日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="出生日期类型">
                <xs:attribute ref="locID" use="optional" fixed="003027"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="参加工作日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="参加工作日期类型">
                <xs:attribute ref="locID" use="optional" fixed="003028"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="视同缴费月数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="视同缴费月数类型">
                <xs:attribute ref="locID" use="optional" fixed="007021"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="离退休日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="离退休日期类型">
                <xs:attribute ref="locID" use="optional" fixed="003029"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="死亡日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="死亡日期类型">
                <xs:attribute ref="locID" use="optional" fixed="003030"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="专业技术职务级别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="专业技术职务级别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003031"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

<xs:element name="专业技术职务级别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="专业技术职务级别类型">
                <xs:attribute ref="locID" use="optional" fixed="003032"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="国家职业资格等级代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="国家职业资格等级代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003033"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="国家职业资格等级">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="国家职业资格等级类型">
                <xs:attribute ref="locID" use="optional" fixed="003034"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="行政职务级别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政职务级别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003035"/>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政职务级别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政职务级别类型">
                <xs:attribute ref="locID" use="optional" fixed="003036"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="退役军人类别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="退役军人类别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003037"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="退役军人类别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="退役军人类别类型">
                <xs:attribute ref="locID" use="optional" fixed="003038"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:sequence>

</xs:complexType>

<xs:element name="养老保险死亡人员信息表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
            <xs:element name="地域属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="地域属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001002"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
            <xs:element name="行政区划代码">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="行政区划代码类型">
                            <xs:attribute ref="locID" use="optional" fixed="001003"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
            <xs:element name="行政区划">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="行政区划类型">
                            <xs:attribute ref="locID" use="optional" fixed="001004"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="001005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构类型">

<xs:attribute ref="locID" use="optional" fixed="001006"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="人员编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="人员编码类型">

<xs:attribute ref="locID" use="optional" fixed="003001"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="社会保障号码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="社会保障号码类型">

<xs:attribute ref="locID" use="optional" fixed="003002"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="姓名">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="姓名类型">

<xs:attribute ref="locID" use="optional" fixed="003003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件类型代码">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="证件类型代码类型">
        <xs:attribute ref="locID" use="optional" fixed="003004"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:element name="证件号码">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="证件号码类型">
                            <xs:attribute ref="locID" use="optional" fixed="003006"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element>
    </xs:complexType>
    <xs:element name="性别代码">
        <xs:simpleContent>
            <xs:extension base="性别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="性别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="性别类型">
                <xs:attribute ref="locID" use="optional" fixed="003011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="死亡日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="死亡日期类型">
                <xs:attribute ref="locID" use="optional" fixed="003030"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="实际缴费月数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="实际缴费月数类型">
                <xs:attribute ref="locID" use="optional" fixed="006001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人账户累计本息">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人账户累计本息类型">
                <xs:attribute ref="locID" use="optional" fixed="006002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="养老丧葬补助金">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="养老丧葬补助金类型">
                <xs:attribute ref="locID" use="optional" fixed="007001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="养老抚恤金">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="养老抚恤金类型">
                <xs:attribute ref="locID" use="optional" fixed="007002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">

<xs:attribute ref="locID" use="optional" fixed="001007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

### A.4 参保信息类 XML 大纲

<xs:element name="养老保险人员参保信息表">

<xs:attribute ref="locID" use="optional" fixed="001001"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="地域属性">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="地域属性类型">

<xs:attribute ref="locID" use="optional" fixed="001002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划代码类型">

<xs:attribute ref="locID" use="optional" fixed="001003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="经办机构类型">
        <xs:attribute ref="locID" use="optional" fixed="001006"/>
    </xs:extension>
    <xs:simpleContent>
        <xs:complexType>
            <xs:element>
                <xs:element name="险种代码">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="险种代码类型">
                                <xs:attribute ref="locID" use="optional" fixed="005013"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
                <xs:element name="险种名称">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="险种名称类型">
                                <xs:attribute ref="locID" use="optional" fixed="005014"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
                <xs:element name="单位编码">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="单位编码类型">
                                <xs:attribute ref="locID" use="optional" fixed="002001"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
                <xs:element name="单位名称">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="单位名称类型">
                                <xs:attribute ref="locID" use="optional" fixed="002002"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
            </xs:element>
        </xs:complexType>
    </xs:element>
</xs:simpleContent>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="证件号码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="证件号码类型">

<xs:attribute ref="locID" use="optional" fixed="003006"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="首次参保年月">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="首次参保年月类型">

<xs:attribute ref="locID" use="optional" fixed="004002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人参保状态">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人参保状态类型">

<xs:attribute ref="locID" use="optional" fixed="004003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人缴费状态代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人缴费状态代码类型">

<xs:attribute ref="locID" use="optional" fixed="004004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人缴费状态">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人缴费状态类型">

<xs:attribute ref="locID" use="optional" fixed="004005"/>
</xs:extension>

</xs:complexType>

</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="缴费基数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="缴费基数类型">

<xs:attribute ref="locID" use="optional" fixed="006009"/>
</xs:extension>

</xs:simpleContent>

</xs:element>

<xs:element name="本次开始日期">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="本次开始日期类型">

<xs:attribute ref="locID" use="optional" fixed="004006"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="本次终止日期">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="本次终止日期类型">

<xs:attribute ref="locID" use="optional" fixed="004007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办人">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办人类型">

<xs:attribute ref="locID" use="optional" fixed="006016"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办日期">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办日期类型">
    <xs:attribute ref="locID" use="optional" fixed="006017"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:sequence>

</xs:complexType>

<xs:element name="养老保险离退休人员基本信息表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element name="地域属性">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="地域属性类型">
                    <xs:attribute ref="locID" use="optional" fixed="001002"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="行政区划代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="行政区划代码类型">
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:extension>

<xs:attribute ref="locID" use="optional" fixed="001003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构类型">

<xs:attribute ref="locID" use="optional" fixed="001006"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="人员编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="人员编码类型">

<xs:attribute ref="locID" use="optional" fixed="003001"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件类型">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="证件类型类型">
        <xs:attribute ref="locID" use="optional" fixed="003005"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="性别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="性别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="性别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="性别类型">
                <xs:attribute ref="locID" use="optional" fixed="003011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="离退休类别代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="离退休类别代码类型">
                <xs:attribute ref="locID" use="optional" fixed="007018"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="离退休类别">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="离退休类别类型">
                <xs:attribute ref="locID" use="optional" fixed="007019"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

    <xs:element name="核定年月">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="核定年月类型">
                    <xs:attribute ref="locID" use="optional" fixed="007020"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="参加工作日期">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="参加工作日期类型">
                    <xs:attribute ref="locID" use="optional" fixed="003028"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="离退休日期">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="离退休日期类型">
                    <xs:attribute ref="locID" use="optional" fixed="003029"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="待遇享受开始年月">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="待遇享受开始年月类型">
                    <xs:attribute ref="locID" use="optional" fixed="007006"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:complexType>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="视同缴费月数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="视同缴费月数类型">

<xs:attribute ref="locID" use="optional" fixed="007021"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="实际缴费月数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="实际缴费月数类型">

<xs:attribute ref="locID" use="optional" fixed="006001"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="中断月数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="中断月数类型">

<xs:attribute ref="locID" use="optional" fixed="007022"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="累计缴费月数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="累计缴费月数类型">

<xs:attribute ref="locID" use="optional" fixed="007023"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="特殊工种类型代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="特殊工种类型代码类型">
    <xs:attribute ref="locID" use="optional" fixed="007024"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="特殊工种类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="特殊工种类型类型">
                <xs:attribute ref="locID" use="optional" fixed="007025"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="特殊工种月数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="特殊工种月数类型">
                <xs:attribute ref="locID" use="optional" fixed="007026"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="离退休时账户总金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="离退休时账户总金额类型">
                <xs:attribute ref="locID" use="optional" fixed="007027"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="退休时核定养老金">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="退休时核定养老金类型">
                <xs:attribute ref="locID" use="optional" fixed="007028"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="低保对象标识">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="低保对象标识类型">
            <xs:attribute ref="locID" use="optional" fixed="007029"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="补发月数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="补发月数类型">
                <xs:attribute ref="locID" use="optional" fixed="007030"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="补发总金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="补发总金额类型">
                <xs:attribute ref="locID" use="optional" fixed="007031"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

<xs:element name="养老保险个人账户明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>

<xs:simpleContent>
    <xs:extension base="时间属性类型">
        <xs:attribute ref="locID" use="optional" fixed="001001"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="地域属性">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="地域属性类型">
                <xs:attribute ref="locID" use="optional" fixed="001002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划代码类型">
                <xs:attribute ref="locID" use="optional" fixed="001003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="就业状态代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="就业状态代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003025"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="就业状态名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="就业状态名称类型">
                <xs:attribute ref="locID" use="optional" fixed="003026"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:complexType>
    </xs:complexType>
</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="年度">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="年度类型">

<xs:attribute ref="locID" use="optional" fixed="007032"/>
</xs:extension>

</xs:simpleContent>

</xs:element>

<xs:element name="年初账户金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="年初账户金额类型">

<xs:attribute ref="locID" use="optional" fixed="007033"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="当年账户本金划入">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="当年账户本金划入类型">

<xs:attribute ref="locID" use="optional" fixed="007034"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="当年账户利息划入">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="当年账户利息划入类型">

<xs:attribute ref="locID" use="optional" fixed="007035"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="本年账户支出">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="本年账户支出类型">
    <xs:attribute ref="locID" use="optional" fixed="007036"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="年末账户金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="年末账户金额类型">
                <xs:attribute ref="locID" use="optional" fixed="007037"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="历年缴纳月数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="历年缴纳月数类型">
                <xs:attribute ref="locID" use="optional" fixed="007038"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="账户记息日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="账户记息日期类型">
                <xs:attribute ref="locID" use="optional" fixed="007039"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="养老账户状态代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="养老账户状态代码类型">
                <xs:attribute ref="locID" use="optional" fixed="007040"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="养老账户状态">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="养老账户状态类型">
            <xs:attribute ref="locID" use="optional" fixed="007041"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:sequence>

<xs:complexType>
    <xs:element name="养老保险人员转移信息表">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="时间属性">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="时间属性类型">
                                <xs:attribute ref="locID" use="optional" fixed="001001"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="地域属性类型">
                <xs:attribute ref="locID" use="optional" fixed="001002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划代码">
                <xs:attribute ref="locID" use="optional" fixed="001002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:sequence>

<xs:simpleContent>
    <xs:extension base="行政区划代码类型">
        <xs:attribute ref="locID" use="optional" fixed="001003"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="险种名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="险种名称类型">

<xs:attribute ref="locID" use="optional" fixed="005014"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="转移方向">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="转移方向类型">

<xs:attribute ref="locID" use="optional" fixed="008001"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="转移方向代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="转移方向代码类型">

<xs:attribute ref="locID" use="optional" fixed="008002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="对方社会保险机构名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="对方社会保险机构名称类型">

<xs:attribute ref="locID" use="optional" fixed="008003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="对方所在单位名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="对方所在单位名称类型">

<xs:attribute ref="locID" use="optional" fixed="008004"/>
</xs:extension>

</xs:complexType>

</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="视同缴费月数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="视同缴费月数类型">

<xs:attribute ref="locID" use="optional" fixed="007021"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="实际缴费月数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="实际缴费月数类型">

<xs:attribute ref="locID" use="optional" fixed="006001"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="转移个人划转金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="转移个人划转金额类型">

<xs:attribute ref="locID" use="optional" fixed="008005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="转移单位划转金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="转移单位划转金额类型">

<xs:attribute ref="locID" use="optional" fixed="008006"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="基本养老保险基金转移总额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="基本养老保险基金转移总额类型">
    <xs:attribute ref="locID" use="optional" fixed="008007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="统筹部分转移金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="统筹部分转移金额类型">
                <xs:attribute ref="locID" use="optional" fixed="008008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办人">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办人类型">
                <xs:attribute ref="locID" use="optional" fixed="006016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办日期类型">
                <xs:attribute ref="locID" use="optional" fixed="006017"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="对方行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="对方行政区划代码类型">
                <xs:attribute ref="locID" use="optional" fixed="008009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="对方行政区划">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="对方行政区划类型">
            <xs:attribute ref="locID" use="optional" fixed="008010"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

### A.5 单位征缴类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="单位缴费">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="职工基本养老保险单位征缴明细表"/>
                <xs:element name="机关事业单位养老保险单位征缴明细表"/>
            </xs:sequence>
            <xs:attribute ref="locID" use="optional" fixed="U04"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="职工基本养老保险单位征缴明细表">
        <xs:complexType>
            <xs:sequence>

<xs:element name="时间属性">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="时间属性类型">
                <xs:attribute ref="locID" use="optional" fixed="001001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="地域属性">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="地域属性类型">
                <xs:attribute ref="locID" use="optional" fixed="001002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划代码类型">
                <xs:attribute ref="locID" use="optional" fixed="001003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>
    <xs:element name="结算单号">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="结算单号类型">
                    <xs:attribute ref="locID" use="optional" fixed="005003"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="单位编码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="单位编码类型">
                    <xs:attribute ref="locID" use="optional" fixed="002001"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="单位名称">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="单位名称类型">
                    <xs:attribute ref="locID" use="optional" fixed="002002"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="单位类型代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="单位类型代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="002007"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:complexType>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

<xs:element name="单位类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位类型类型">
                <xs:attribute ref="locID" use="optional" fixed="002008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经济类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经济类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经济类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经济类型类型">
                <xs:attribute ref="locID" use="optional" fixed="002010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="隶属关系代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="隶属关系代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="隶属关系">
    <xs:complexType>
        <xs:simpleContent>

<xs:extension base="隶属关系类型">
    <xs:attribute ref="locID" use="optional" fixed="002012"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="结算年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="结算年月类型">
                <xs:attribute ref="locID" use="optional" fixed="005004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴年月类型">
                <xs:attribute ref="locID" use="optional" fixed="005005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="到账日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="到账日期类型">
                <xs:attribute ref="locID" use="optional" fixed="005006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="征缴方式代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="征缴方式代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="征缴方式">
    <xs:extension base="征缴方式代码类型">
        <xs:attribute ref="locID" use="optional" fixed="005007"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="征缴方式">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="征缴方式类型">
            <xs:attribute ref="locID" use="optional" fixed="005008"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="足额到账标志代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="足额到账标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志类型">
                <xs:attribute ref="locID" use="optional" fixed="005010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型类型">
                <xs:attribute ref="locID" use="optional" fixed="005012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应征人数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应征人数类型">
                <xs:attribute ref="locID" use="optional" fixed="005015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴总金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴总金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位缴费基数总额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位缴费基数总额类型">
                <xs:attribute ref="locID" use="optional" fixed="005017"/>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="个人缴费基数总额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人缴费基数总额类型">
                <xs:attribute ref="locID" use="optional" fixed="005018"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005019"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="个人应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005020"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="滞纳金金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="滞纳金金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005021"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位划账金额类型">
                <xs:extension base="个人缴费基数总额类型">
                    <xs:attribute ref="locID" use="optional" fixed="005018"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="005022"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人划账金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人划账金额类型">

<xs:attribute ref="locID" use="optional" fixed="005023"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位实缴金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位实缴金额类型">

<xs:attribute ref="locID" use="optional" fixed="005025"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位实缴划入个人账户金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位实缴划入个人账户金额类型">

<xs:attribute ref="locID" use="optional" fixed="005026"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人实缴金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人实缴金额类型">

<xs:attribute ref="locID" use="optional" fixed="005027"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人实缴划入个人账户金额">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="个人实缴划入个人账户金额类型">
        <xs:attribute ref="locID" use="optional" fixed="005028"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:sequence>

</xs:complexType>

<xs:element name="机关事业单位养老保险单位征缴明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element name="地域属性">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="地域属性类型">
                    <xs:attribute ref="locID" use="optional" fixed="001002"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
</xs:element>

<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>

<xs:extension base="行政区划代码类型">
    <xs:attribute ref="locID" use="optional" fixed="001003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="结算单号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="结算单号类型">
                <xs:attribute ref="locID" use="optional" fixed="005003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位编码">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="单位编码类型">
            <xs:attribute ref="locID" use="optional" fixed="002001"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="单位名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位名称类型">
                <xs:attribute ref="locID" use="optional" fixed="002002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位类型类型">
                <xs:attribute ref="locID" use="optional" fixed="002008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="隶属关系代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="隶属关系代码类型">
                <xs:attribute ref="locID" use="optional" fixed="002011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="隶属关系">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="隶属关系类型">
                <xs:attribute ref="locID" use="optional" fixed="002012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

    <xs:element name="结算年月">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="结算年月类型">
                    <xs:attribute ref="locID" use="optional" fixed="005004"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="应缴年月">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="应缴年月类型">
                    <xs:attribute ref="locID" use="optional" fixed="005005"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="到账日期">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="到账日期类型">
                    <xs:attribute ref="locID" use="optional" fixed="005006"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="征缴方式代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="征缴方式代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="005007"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:element>

</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="征缴方式">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="征缴方式类型">
                <xs:attribute ref="locID" use="optional" fixed="005008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="足额到账标志代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="足额到账标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志类型">
                <xs:attribute ref="locID" use="optional" fixed="005010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型类型">
                <xs:extension base="征缴方式类型">
                    <xs:attribute ref="locID" use="optional" fixed="005008"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="005012"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="险种代码类型">

<xs:attribute ref="locID" use="optional" fixed="005013"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="险种名称类型">

<xs:attribute ref="locID" use="optional" fixed="005014"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="应征人数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="应征人数类型">

<xs:attribute ref="locID" use="optional" fixed="005015"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="应缴总金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="应缴总金额类型">

<xs:attribute ref="locID" use="optional" fixed="005016"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位缴费基数总额">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="单位缴费基数总额类型">
        <xs:attribute ref="locID" use="optional" fixed="005017"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人缴费基数总额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人缴费基数总额类型">
                <xs:attribute ref="locID" use="optional" fixed="005018"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005019"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="个人应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005020"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="滞纳金金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="滞纳金金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005021"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005022"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005023"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="单位实缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位实缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005025"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="单位实缴划入个人账户金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位实缴划入个人账户金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005026"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人实缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人实缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005027"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="个人实缴划入个人账户金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人实缴划入个人账户金额类型">

<xs:attribute ref="locID" use="optional" fixed="005028"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">

<xs:attribute ref="locID" use="optional" fixed="001007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

### A.6 人员缴费类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="人员缴费">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="城乡居民基本养老保险个人征缴明细表"/>
                <xs:element name="职工基本养老保险个人征缴明细表"/>
                <xs:element name="机关事业单位养老保险个人征缴明细表"/>
            </xs:sequence>
            <xs:attribute ref="locID" use="optional" fixed="U05"/>
        </xs:complexType>
    </xs:sequence>
</xs:schema>

</xs:element>

<xs:element name="城乡居民基本养老保险个人征缴明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element name="地域属性">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="地域属性类型">
                    <xs:attribute ref="locID" use="optional" fixed="001002"/>
                </xs:extension>
                <xs:simpleContent>
                    <xs:complexType>
                        <xs:element name="行政区划代码">
                            <xs:element name="行政区划">
                                <xs:complexType>
                                    <xs:simpleContent>
                                        <xs:extension base="行政区划代码类型">
                                            <xs:attribute ref="locID" use="optional" fixed="001003"/>
                                        </xs:extension>
                                    </xs:simpleContent>
                                </xs:complexType>
                            </xs:element>
                        </xs:element name="行政区划">
                    </xs:complexType>
                </xs:simpleContent>
            </xs:extension base="行政区划类型">
            <xs:attribute ref="locID" use="optional" fixed="001004"/>
        </xs:extension>
    </xs:element>
    <xs:element name="经办机构编码">
        <xs:complexType>
            <xs:simpleContent>

<xs:extension base="经办机构编码类型">
    <xs:attribute ref="locID" use="optional" fixed="001005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="街道或乡镇编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="街道或乡镇编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003021"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="街道或乡镇">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="街道或乡镇类型">
            <xs:attribute ref="locID" use="optional" fixed="003022"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="社区或村编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社区或村编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003023"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社区或村">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社区或村类型">
                <xs:attribute ref="locID" use="optional" fixed="003024"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

    <xs:element name="证件类型代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="证件类型代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="003004"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="证件号码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="证件号码类型">
                    <xs:attribute ref="locID" use="optional" fixed="003006"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="姓名">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="姓名类型">
                    <xs:attribute ref="locID" use="optional" fixed="003003"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>

    <xs:element name="应缴类型代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="应缴类型代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="005011"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:element>

</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="应缴类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型类型">
                <xs:attribute ref="locID" use="optional" fixed="005012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴年度">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴年度类型">
                <xs:attribute ref="locID" use="optional" fixed="005024"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="结算年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="结算年月类型">
                <xs:attribute ref="locID" use="optional" fixed="005004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="个人应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005020"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="个人实缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人实缴金额类型">
                <xs:extension base="个人实缴金额类型">
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="005027"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="划入个人账户金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="划入个人账户金额类型">

<xs:attribute ref="locID" use="optional" fixed="006003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="中央财政补贴">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="中央财政补贴类型">

<xs:attribute ref="locID" use="optional" fixed="006004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="省级财政补贴">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="省级财政补贴类型">

<xs:attribute ref="locID" use="optional" fixed="006005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="市级财政补贴">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="市级财政补贴类型">

<xs:attribute ref="locID" use="optional" fixed="006006"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="县区财政补贴">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="县区财政补贴类型">
        <xs:attribute ref="locID" use="optional" fixed="006007"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="足额到账标志代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="足额到账标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志类型">
                <xs:attribute ref="locID" use="optional" fixed="005010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="到账日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="到账日期类型">
                <xs:attribute ref="locID" use="optional" fixed="005006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="本年缴费月数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="本年缴费月数类型">
                <xs:attribute ref="locID" use="optional" fixed="006008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="征缴方式代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="征缴方式代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="征缴方式">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="征缴方式类型">
                <xs:attribute ref="locID" use="optional" fixed="005008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>

<xs:element name="职工基本养老保险个人征缴明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="地域属性类型">
            <xs:attribute ref="locID" use="optional" fixed="001002"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划代码类型">
                <xs:attribute ref="locID" use="optional" fixed="001003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="结算单号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="结算单号类型">
                <xs:attribute ref="locID" use="optional" fixed="005003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

    <xs:element name="结算年月">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="结算年月类型">
                    <xs:attribute ref="locID" use="optional" fixed="005004"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>

        <xs:element name="应缴年月">
            <xs:complexType>
                <xs:simpleContent>
                    <xs:extension base="应缴年月类型">
                        <xs:attribute ref="locID" use="optional" fixed="005005"/>
                    </xs:extension>
                </xs:simpleContent>
            </xs:complexType>
        </xs:element>
    </xs:element>

    <xs:element name="应缴类型代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="应缴类型代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="005011"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>

    </xs:element>

    <xs:element name="应缴类型">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="应缴类型类型">
                    <xs:attribute ref="locID" use="optional" fixed="005012"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:element>

</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:extension base="人员编码类型">
                    <xs:attribute ref="locID" use="optional" fixed="003001"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="003006"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="姓名">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="姓名类型">

<xs:attribute ref="locID" use="optional" fixed="003003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位编码类型">

<xs:attribute ref="locID" use="optional" fixed="002001"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位名称类型">

<xs:attribute ref="locID" use="optional" fixed="002002"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="险种代码类型">

<xs:attribute ref="locID" use="optional" fixed="005013"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种名称">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="险种名称类型">
        <xs:attribute ref="locID" use="optional" fixed="005014"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="应缴总金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴总金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="缴费基数">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="缴费基数类型">
                <xs:attribute ref="locID" use="optional" fixed="006009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位缴费比例">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位缴费比例类型">
                <xs:attribute ref="locID" use="optional" fixed="006010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005019"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="单位划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005022"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人缴费比例">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人缴费比例类型">
                <xs:attribute ref="locID" use="optional" fixed="006011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人应缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人应缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005020"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人实缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人实缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005027"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005023"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="财政划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="财政划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="006012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

<xs:element name="其他补充金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="其他补充金额类型">
                <xs:attribute ref="locID" use="optional" fixed="006013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="其他划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="其他划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="006014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="核销标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="核销标志类型">
                <xs:attribute ref="locID" use="optional" fixed="006015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="足额到账标志代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005009"/>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="足额到账标志">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="足额到账标志类型">

<xs:attribute ref="locID" use="optional" fixed="005010"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="到账日期">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="到账日期类型">

<xs:attribute ref="locID" use="optional" fixed="005006"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办人">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办人类型">

<xs:attribute ref="locID" use="optional" fixed="006016"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办日期">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办日期类型">

<xs:attribute ref="locID" use="optional" fixed="006017"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">
    <xs:attribute ref="locID" use="optional" fixed="001007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:element name="机关事业单位养老保险个人征缴明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
            <xs:element name="地域属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="地域属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001002"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element name="行政区划代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="行政区划代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="001003"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="行政区划">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="行政区划类型">
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:extension>

<xs:attribute ref="locID" use="optional" fixed="001004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构类型">

<xs:attribute ref="locID" use="optional" fixed="001006"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="结算单号">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="结算单号类型">

<xs:attribute ref="locID" use="optional" fixed="005003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="结算年月">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="结算年月类型">

<xs:attribute ref="locID" use="optional" fixed="005004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="应缴年月">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="应缴年月类型">
        <xs:attribute ref="locID" use="optional" fixed="005005"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="应缴类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="应缴类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="应缴类型类型">
                <xs:attribute ref="locID" use="optional" fixed="005012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="单位编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位编码类型">
                <xs:attribute ref="locID" use="optional" fixed="002001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="单位名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位名称类型">

<xs:attribute ref="locID" use="optional" fixed="002002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="险种代码类型">

<xs:attribute ref="locID" use="optional" fixed="005013"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="险种名称类型">

<xs:attribute ref="locID" use="optional" fixed="005014"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="应缴总金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="应缴总金额类型">

<xs:attribute ref="locID" use="optional" fixed="005016"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="缴费基数">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="缴费基数类型">

<xs:attribute ref="locID" use="optional" fixed="006009"/>
</xs:extension>

</xs:complexType>

</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位缴费比例">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位缴费比例类型">

<xs:attribute ref="locID" use="optional" fixed="006010"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位应缴金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位应缴金额类型">

<xs:attribute ref="locID" use="optional" fixed="005019"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位划账金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="单位划账金额类型">

<xs:attribute ref="locID" use="optional" fixed="005022"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人缴费比例">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人缴费比例类型">

<xs:attribute ref="locID" use="optional" fixed="006011"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人应缴金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="个人应缴金额类型">
    <xs:attribute ref="locID" use="optional" fixed="005020"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="个人实缴金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人实缴金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005027"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="个人划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="005023"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="财政划账金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="财政划账金额类型">
                <xs:attribute ref="locID" use="optional" fixed="006012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="其他补充金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="其他补充金额类型">
                <xs:attribute ref="locID" use="optional" fixed="006013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="其他划账金额">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="其他划账金额类型">
            <xs:attribute ref="locID" use="optional" fixed="006014"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="核销标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="核销标志类型">
                <xs:attribute ref="locID" use="optional" fixed="006015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="足额到账标志代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="足额到账标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="足额到账标志类型">
                <xs:attribute ref="locID" use="optional" fixed="005010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="到账日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="到账日期类型">
                <xs:attribute ref="locID" use="optional" fixed="005006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="经办人">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办人类型">
                <xs:attribute ref="locID" use="optional" fixed="006016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办日期类型">
                <xs:attribute ref="locID" use="optional" fixed="006017"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

<xs:schema>

### A.7 待遇支付类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="待遇支付">
    </xs:include>
</xs:schema>

<xs:complexType>
    <xs:sequence>
        <xs:element name="养老保险待遇支付明细表" />
    </xs:sequence>
    <xs:attribute ref="locID" use="optional" fixed="U06" />
</xs:complexType>

<xs:element name="养老保险待遇支付明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001" />
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element name="地域属性">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="地域属性类型">
                    <xs:attribute ref="locID" use="optional" fixed="001002" />
                </xs:extension>
                <xs:simpleContent>
                    <xs:complexType>
                        <xs:element name="行政区划代码">
                            <xs:element name="行政区划">
                                <xs:element name="行政区划">
                                    <xs:complexType>
                                        <xs:simpleContent>
                                            <xs:extension base="行政区划代码类型">
                                                    <xs:attribute ref="locID" use="optional" fixed="001003" />
                                                </xs:extension>
                                            </xs:simpleContent>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:complexType>
                            </xs:element>
                        </xs:element>
                    </xs:complexType>
                </xs:element>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:complexType>

</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="待遇支付明细序号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇支付明细序号类型">
                <xs:attribute ref="locID" use="optional" fixed="007003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:extension base="社会保障号码类型">
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="003002"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件类型">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="证件类型类型">

<xs:attribute ref="locID" use="optional" fixed="003005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件类型代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="证件类型代码类型">

<xs:attribute ref="locID" use="optional" fixed="003004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="证件号码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="证件号码类型">

<xs:attribute ref="locID" use="optional" fixed="003006"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="姓名">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="姓名类型">

<xs:attribute ref="locID" use="optional" fixed="003003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位编码">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="单位编码类型">
        <xs:attribute ref="locID" use="optional" fixed="002001"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="单位名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="单位名称类型">
                <xs:attribute ref="locID" use="optional" fixed="002002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="结算年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="结算年月类型">
                <xs:attribute ref="locID" use="optional" fixed="005004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="待遇年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇年月类型">
                <xs:attribute ref="locID" use="optional" fixed="007044"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="待遇项目代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇项目代码类型">
                <xs:attribute ref="locID" use="optional" fixed="007004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="待遇项目名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇项目名称类型">
                <xs:attribute ref="locID" use="optional" fixed="007005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="待遇享受开始年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇享受开始年月类型">
                <xs:attribute ref="locID" use="optional" fixed="007006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个账支付金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个账支付金额类型">
                <xs:attribute ref="locID" use="optional" fixed="007007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="待遇金额">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇金额类型">

<xs:attribute ref="locID" use="optional" fixed="007008"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="领取人姓名">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="领取人姓名类型">

<xs:attribute ref="locID" use="optional" fixed="007009"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="领取关系">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="领取关系类型">

<xs:attribute ref="locID" use="optional" fixed="007010"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="领取人证件号码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="领取人证件号码类型">

<xs:attribute ref="locID" use="optional" fixed="007011"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="开户银行名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="开户银行名称类型">

<xs:attribute ref="locID" use="optional" fixed="003007"/>
</xs:extension>

</xs:complexType>

</xs:element>

</xs:element>

</xs:complexType>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="银行账户名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="银行账户名称类型">

<xs:attribute ref="locID" use="optional" fixed="003009"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="银行账号">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="银行账号类型">

<xs:attribute ref="locID" use="optional" fixed="003008"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇发放方式代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇发放方式代码类型">

<xs:attribute ref="locID" use="optional" fixed="007012"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇发放方式">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇发放方式类型">

<xs:attribute ref="locID" use="optional" fixed="007013"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇项目支付类型代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇项目支付类型代码类型">
    <xs:attribute ref="locID" use="optional" fixed="007014"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇项目支付类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇项目支付类型类型">
                <xs:attribute ref="locID" use="optional" fixed="007015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="统筹类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="统筹类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="007016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="统筹类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="统筹类型类型">
                <xs:attribute ref="locID" use="optional" fixed="007017"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办人">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办人类型">
                <xs:attribute ref="locID" use="optional" fixed="006016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办日期">

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="经办日期类型">
            <xs:attribute ref="locID" use="optional" fixed="006017"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

### A.8 信息变更类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="变更转移">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="养老保险单位变更信息表"/>
                <xs:element name="养老保险人员参保情况变更信息表"/>
            </xs:sequence>
            <xs:attribute ref="locID" use="optional" fixed="U07"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="养老保险单位变更信息表">
        <xs:complexType>
            <xs:sequence>

<xs:element name="时间属性">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="时间属性类型">
                <xs:attribute ref="locID" use="optional" fixed="001001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="地域属性">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="地域属性类型">
                <xs:attribute ref="locID" use="optional" fixed="001002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划代码类型">
                <xs:attribute ref="locID" use="optional" fixed="001003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>
    <xs:element name="经办人">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="经办人类型">
                    <xs:attribute ref="locID" use="optional" fixed="006016"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="单位编码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="单位编码类型">
                    <xs:attribute ref="locID" use="optional" fixed="002001"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="单位变更类型代码">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="单位变更类型代码类型">
                    <xs:attribute ref="locID" use="optional" fixed="008011"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="单位变更类型">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="单位变更类型类型">
                    <xs:attribute ref="locID" use="optional" fixed="008012"/>
                </xs:extension>
            </xs:complexType>
        </xs:element>
    </xs:element>
</xs:complexType>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="变更前信息">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="变更前信息类型">

<xs:attribute ref="locID" use="optional" fixed="008013"/>
</xs:extension>

</xs:simpleContent>

</xs:element>

<xs:element name="变更后信息">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="变更后信息类型">

<xs:attribute ref="locID" use="optional" fixed="008014"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="变更原因代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="变更原因代码类型">

<xs:attribute ref="locID" use="optional" fixed="008015"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="变更原因">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="变更原因类型">

<xs:attribute ref="locID" use="optional" fixed="008016"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="变更日期">

<xs:complexType>

<xs:simpleContent>

<xs:element name="行政区划代码">

<xs:attribute ref="locID" use="optional" fixed="001003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:element name="经办人">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办人类型">

<xs:attribute ref="locID" use="optional" fixed="006016"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="人员变更流水号">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="人员变更流水号类型">
        <xs:attribute ref="locID" use="optional" fixed="008018"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="人员编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="人员编码类型">
                <xs:attribute ref="locID" use="optional" fixed="003001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="姓名">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="姓名类型">
                <xs:attribute ref="locID" use="optional" fixed="003003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="社会保障号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="社会保障号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型类型">
                <xs:attribute ref="locID" use="optional" fixed="003005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="证件类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="003004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="证件号码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="证件号码类型">
                <xs:attribute ref="locID" use="optional" fixed="003006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="首次参保年月">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="首次参保年月类型">
                <xs:attribute ref="locID" use="optional" fixed="004002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人变更类型代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人变更类型代码类型">
                <xs:attribute ref="locID" use="optional" fixed="008019"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="个人变更类型">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="个人变更类型类型">
                <xs:attribute ref="locID" use="optional" fixed="008020"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="变更原因代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="变更原因代码类型">
                <xs:attribute ref="locID" use="optional" fixed="008015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="变更原因">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="变更原因类型">
                <xs:attribute ref="locID" use="optional" fixed="008016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="变更前信息">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="变更前信息类型">
                <xs:attribute ref="locID" use="optional" fixed="008013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="变更后信息">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="变更后信息类型">
                <xs:attribute ref="locID" use="optional" fixed="008014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="变更日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="变更日期类型">
                <xs:attribute ref="locID" use="optional" fixed="008017"/>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">

<xs:attribute ref="locID" use="optional" fixed="001007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

### A.9 参数类 XML 大纲

<xs:element name="参数表">

<xs:attribute ref="locID" use="optional" fixed="001001"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="地域属性">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="地域属性类型">

<xs:attribute ref="locID" use="optional" fixed="001002"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划代码类型">

<xs:attribute ref="locID" use="optional" fixed="001003"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="经办机构类型">
        <xs:attribute ref="locID" use="optional" fixed="001006"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="参数类别编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="参数类别编码类型">
                <xs:attribute ref="locID" use="optional" fixed="009001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="参数类别名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="参数类别名称类型">
                <xs:attribute ref="locID" use="optional" fixed="009002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="参数值">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="参数值类型">
                <xs:attribute ref="locID" use="optional" fixed="009003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="参数名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="参数名称类型">
                <xs:attribute ref="locID" use="optional" fixed="009004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="变更日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="变更日期类型">
                <xs:attribute ref="locID" use="optional" fixed="008017"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="有效标志">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="有效标志类型">
                <xs:attribute ref="locID" use="optional" fixed="009005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="修改时间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="修改时间类型">
                <xs:attribute ref="locID" use="optional" fixed="001007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

<xs:element name="养老待遇类型表">

<xs:complexType>

<xs:sequence>

<xs:element name="时间属性">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="时间属性类型">

<xs:attribute ref="locID" use="optional" fixed="001001"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="地域属性">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="地域属性类型">

<xs:attribute ref="locID" use="optional" fixed="001002"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="行政区划代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划代码类型">

<xs:attribute ref="locID" use="optional" fixed="001003"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种代码类型">
                <xs:attribute ref="locID" use="optional" fixed="005013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="险种名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="险种名称类型">
                <xs:attribute ref="locID" use="optional" fixed="005014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="待遇项目代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="待遇项目代码类型">
                <xs:attribute ref="locID" use="optional" fixed="007004"/>
            </xs:extension>
        </xs:complexType>
    </xs:extension>
</xs:element>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇项目名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇项目名称类型">

<xs:attribute ref="locID" use="optional" fixed="007005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇项目支付类型代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇项目支付类型代码类型">

<xs:attribute ref="locID" use="optional" fixed="007014"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="待遇项目支付类型">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="待遇项目支付类型类型">

<xs:attribute ref="locID" use="optional" fixed="007015"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="统筹类型代码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="统筹类型代码类型">

<xs:attribute ref="locID" use="optional" fixed="007016"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="统筹类型">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="统筹类型类型">

</xs:extension>

</xs:complexType>

</xs:element>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

<xs:attribute ref="locID" use="optional" fixed="007017"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="基金列支类型代码">

<xs:complexType>

<xs:simpleContent>

<xs:element name="基金列支类型">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="基金列支类型类型">

<xs:attribute ref="locID" use="optional" fixed="007042"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="有效标志">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="有效标志类型">

<xs:attribute ref="locID" use="optional" fixed="009005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">

<xs:attribute ref="locID" use="optional" fixed="001007"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

〈/xs:element〉
〈/xs:schema〉

### A.10 财务类 XML 大纲

<?xml version="1.0" encoding="GB 18030"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:养老保险基金="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" targetNamespace="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="标准数据元类型.xsd"/>
    <xs:element name="财务信息">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="会计科目表"/>
                <xs:element name="科目余额表"/>
                <xs:element name="凭证明细表"/>
            </xs:sequence>
            <xs:attribute ref="locID" use="optional" fixed="U09"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="会计科目表">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="时间属性">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="时间属性类型">
                                <xs:attribute ref="locID" use="optional" fixed="001001"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
                <xs:element name="地域属性">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="地域属性类型">
                                <xs:attribute ref="locID" use="optional" fixed="001002"/>
                            </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
            </xs:complexType>
        </xs:element>
    </xs:complexType>
</xs:schema>

<xs:element name="行政区划代码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划代码类型">
                <xs:attribute ref="locID" use="optional" fixed="001003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="行政区划">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="行政区划类型">
                <xs:attribute ref="locID" use="optional" fixed="001004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
<xs:element name="账套号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="账套号类型">
                <xs:attribute ref="locID" use="optional" fixed="010001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:complexType>

</xs:element>

<xs:element name="账套名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="账套名称类型">
                <xs:attribute ref="locID" use="optional" fixed="010002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:element>

<xs:element name="会计年度">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="会计年度类型">
                <xs:attribute ref="locID" use="optional" fixed="010003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="科目编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="科目编码类型">
                <xs:attribute ref="locID" use="optional" fixed="010004"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="科目名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="科目名称类型">
                <xs:attribute ref="locID" use="optional" fixed="010005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

</xs:element>

<xs:element name="余额方向">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="余额方向类型">
                <xs:attribute ref="locID" use="optional" fixed="010006"/>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

</xs:element>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="行政区划">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="行政区划类型">

<xs:attribute ref="locID" use="optional" fixed="001004"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构编码类型">

<xs:attribute ref="locID" use="optional" fixed="001005"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="经办机构">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="经办机构类型">

<xs:attribute ref="locID" use="optional" fixed="001006"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="账套号">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="账套号类型">

<xs:attribute ref="locID" use="optional" fixed="010001"/>
</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="账套名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="账套名称类型">

</xs:extension>

</xs:complexType>

</xs:element>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</xs:complexType>

</xs:element>

</

<xs:attribute ref="locID" use="optional" fixed="010002"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="科目编码">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="科目编码类型">

<xs:attribute ref="locID" use="optional" fixed="010004"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="科目名称">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="科目名称类型">

<xs:attribute ref="locID" use="optional" fixed="010005"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="会计年度">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="会计年度类型">

<xs:attribute ref="locID" use="optional" fixed="010003"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="会计期间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="会计期间类型">

<xs:attribute ref="locID" use="optional" fixed="010007"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>
    <xs:extension base="修改时间类型">
        <xs:attribute ref="locID" use="optional" fixed="001007"/>
    </xs:extension>
</xs:simpleContent>

</xs:complexType>

</xs:element>

<xs:element name="余额方向">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="余额方向类型">
                <xs:attribute ref="locID" use="optional" fixed="010006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="期初余额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="期初余额类型">
                <xs:attribute ref="locID" use="optional" fixed="010008"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="本期借方发生额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="本期借方发生额类型">
                <xs:attribute ref="locID" use="optional" fixed="010009"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="本期贷方发生额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="本期贷方发生额类型">
                <xs:attribute ref="locID" use="optional" fixed="010010"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="期末余额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="期末余额类型">
                <xs:attribute ref="locID" use="optional" fixed="010011"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:sequence>

</xs:complexType>

<xs:element name="凭证明细表">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="时间属性">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="时间属性类型">
                            <xs:attribute ref="locID" use="optional" fixed="001001"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
        </xs:element name="地域属性">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="地域属性类型">
                    <xs:attribute ref="locID" use="optional" fixed="001002"/>
                </xs:extension>
                <xs:simpleContent>
                    <xs:complexType>
                        <xs:element name="行政区划代码">
                            <xs:element name="行政区划代码类型">
                                <xs:extension base="行政区划代码类型">
                                    <xs:attribute ref="locID" use="optional" fixed="001003"/>
                                </xs:extension>
                            </xs:simpleContent>
                        </xs:complexType>
                    </xs:element>
                </xs:complexType>
            </xs:element>
        </xs:element name="行政区划代码">
    </xs:complexType>
</xs:sequence>

<xs:complexType>
    <xs:simpleContent>
        <xs:extension base="行政区划类型">
            <xs:attribute ref="locID" use="optional" fixed="001004"/>
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>

<xs:element name="经办机构编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构编码类型">
                <xs:attribute ref="locID" use="optional" fixed="001005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="经办机构">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="经办机构类型">
                <xs:attribute ref="locID" use="optional" fixed="001006"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="账套号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="账套号类型">
                <xs:attribute ref="locID" use="optional" fixed="010001"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="账套名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="账套名称类型">
                <xs:attribute ref="locID" use="optional" fixed="010002"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:element>

<xs:element name="会计年度">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="会计年度类型">
                <xs:attribute ref="locID" use="optional" fixed="010003"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="会计期间">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="会计期间类型">
                <xs:attribute ref="locID" use="optional" fixed="010007"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="凭证编号">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="凭证编号类型">
                <xs:attribute ref="locID" use="optional" fixed="010012"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="凭证日期">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="凭证日期类型">
                <xs:attribute ref="locID" use="optional" fixed="010013"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="科目编码">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="科目编码类型">
                <xs:attribute ref="locID" use="optional" fixed="010004"/>
            </xs:extension>
        </xs:complexType>
    </xs:complexType>
</xs:element>

</xs:simpleContent>
</xs:complexType>

</xs:element>

<xs:element name="科目名称">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="科目名称类型">
                <xs:attribute ref="locID" use="optional" fixed="010005"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="摘要">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="摘要类型">
                <xs:attribute ref="locID" use="optional" fixed="010014"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="借方金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="借方金额类型">
                <xs:attribute ref="locID" use="optional" fixed="010015"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="贷方金额">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="贷方金额类型">
                <xs:attribute ref="locID" use="optional" fixed="010016"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

<xs:element name="制单人">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="制单人类型">
                <xs:extension base="制单人类型">
                </xs:extension>
            </xs:extension>
        </xs:complexType>
    </xs:element>
</xs:element>

<xs:attribute ref="locID" use="optional" fixed="010017"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

<xs:element name="审核人">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="审核人类型">

<xs:attribute ref="locID" use="optional" fixed="010018"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

<xs:element name="记账人">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="记账人类型">

<xs:attribute ref="locID" use="optional" fixed="010019"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

<xs:element name="修改时间">

<xs:complexType>

<xs:simpleContent>

<xs:extension base="修改时间类型">

<xs:attribute ref="locID" use="optional" fixed="001007"/>

</xs:extension>

</xs:simpleContent>

</xs:complexType>

</xs:element>

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>

# 附 录 B （资料性附录） 养老保险基金审计数据接口的 XML 实例

### B.1 单位信息类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

<单位信息

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

XMLSchema 单位信息.xsd"xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

〈养老保险单位基本信息表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈/经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈/经办机构〉

〈单位编码〉10 $ ^{***} $ 01〈/单位编码〉

〈单位名称〉杭州市 *** 科技有限公司〈/单位名称〉

〈统一社会信用代码〉91330100*****1111X〈/统一社会信用代码〉

〈法定代表人姓名〉张**〈/法定代表人姓名〉

〈法定代表人证件号码〉330102*****1111〈/法定代表人证件号码〉

〈法定代表人电话〉138****1234〈/法定代表人电话〉

〈单位类型代码〉10〈/单位类型代码〉

〈单位类型〉企业〈/单位类型〉

〈经济类型代码〉173〈/经济类型代码〉

〈经济类型〉私营有限责任(公司)〈/经济类型〉

〈隶属关系代码〉40〈/隶属关系代码〉

（隶属关系）市、地区（隶属关系）

〈行业代码〉0761〈/行业代码〉

〈行业名称〉计算机服务业〈/行业名称〉

〈联系电话〉0571****5678〈/联系电话〉

〈地址〉杭州市 *** 111 号〈/地址〉

〈单位缴费状态代码〉1〈/单位缴费状态代码〉

〈单位缴费状态〉参保缴费〈/单位缴费状态〉

〈单位参保日期〉200101〈/单位参保日期〉

〈修改时间〉20190101〈/修改时间〉

〈/养老保险单位基本信息表〉

XMLSchema 人员信息.xsd"xmlns:养老保险基金

〈户籍所在地〉浙江省杭州市〈户籍所在地〉

〈民族代码〉01〈/民族代码〉

〈/单位信息〉

### B.2 人员信息类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

人员信息

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

〈养老保险个人基本信息表〉

〈时间属性〉2018010120181231〈/时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈人员编码〉10 $ ^{***} $ 001〈/人员编码〉

〈社会保障号码〉330102*****1111〈/社会保障号码〉

〈姓名〉李 $ ^{**} $ 〈/姓名〉

〈证件类型代码〉01〈证件类型代码〉

〈证件类型〉居民身份证〈/证件类型〉

〈证件号码〉330102*****1111〈/证件号码〉

〈开户银行名称〉工商银行杭州市**支行〈/开户银行名称〉

〈银行账号〉120*****1111111〈/银行账号〉

〈银行账户名称〉李**〈/银行账户名称〉

〈性别代码〉1〈/性别代码〉

〈性别〉男性〈/性别〉

〈民族〉汉族〈/民族〉

〈荣誉称号级别代码〉1〈/荣誉称号级别代码〉

〈荣誉称号级别〉省级荣誉称号〈/荣誉称号级别〉

〈困难人员类别代码〉2〈困难人员类别代码〉

〈困难人员类别〉低保人员〈/困难人员类别〉

〈个人身份代码〉21〈个人身份代码〉

〈个人身份〉企业管理人员〈个人身份〉

〈联系电话〉138****11234〈/联系电话〉

〈地址〉杭州市 *** 号 ** 小区 1 幢 1 单元 301 室〈/地址〉

〈街道或乡镇编码〉330***013〈街道或乡镇编码〉

〈街道或乡镇〉西湖区 **街道〈街道或乡镇〉

〈社区或村编码〉330 $ ^{***} $ 013013〈/社区或村编码〉

〈社区或村〉**社区〈/社区或村〉

<就业状态代码>01</就业状态代码>

〈就业状态名称〉在业〈/就业状态名称〉

〈出生日期〉197 $ ^{***} $ 101〈/出生日期〉

〈参加工作日期〉199 $ ^{***} $ 01〈/参加工作日期〉

〈视同缴费月数〉3〈/视同缴费月数〉

〈离退休日期〉20180101〈/离退休日期〉

〈死亡日期〉20190101〈/死亡日期〉

〈专业技术职务级别代码〉420〈专业技术职务级别代码〉

〈专业技术职务级别〉中级〈专业技术职务级别〉

〈国家职业资格等级代码〉4〈/国家职业资格等级代码〉

〈国家职业资格等级〉职业资格四级（中级）〈/国家职业资格等级〉

〈行政职务级别代码〉132〈/行政职务级别代码〉

〈行政职务级别〉县处级副职〈/行政职务级别〉

〈退役军人类别代码〉10〈/退役军人类别代码〉

〈退役军人类别〉军队转业干部〈/退役军人类别〉

修改时间20190101修改时间

〈/养老保险个人基本信息表〉

## 〈养老保险死亡人员信息表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

<经办机构编码>330199<经办机构编码>

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈人员编码〉10 $ ^{***} $ 0002〈/人员编码〉

〈社会保障号码〉330102*****1111〈/社会保障号码〉

〈姓名〉王**〈/姓名〉

<证件类型代码>01</证件类型代码>

〈证件类型〉居民身份证〈/证件类型〉

<证件号码>330102****1111</证件号码>

〈性别代码〉1〈/性别代码〉

<性别>男性</性别>

〈死亡日期〉20180101〈/死亡日期〉

〈实际缴费月数〉200〈/实际缴费月数〉

〈个人账户累计本息〉10100.01〈个人账户累计本息〉

〈养老丧葬补助金〉4000.00〈/养老丧葬补助金〉

（养老抚恤金）25000.00（养老抚恤金）

修改时间20190101修改时间

## 〈/养老保险死亡人员信息表〉

〈/人员信息〉

### B.3 参保信息类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

## （参保信息

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

XMLSchema 参保信息.xsd"xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

（养老保险人员参保信息表）

〈时间属性〉2018010120181231〈/时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈险种代码〉110〈/险种代码〉

〈险种名称〉企业职工基本养老保险〈/险种名称〉

〈单位编码〉10***001〈/单位编码〉

〈单位名称〉杭州市 *** 科技有限公司〈/单位名称〉

〈人员编码〉10***00001〈/人员编码〉

〈姓名〉李 $ ^{**} $ 〈/姓名〉

〈社会保障号码〉330102*****1111〈/社会保障号码〉

〈证件类型〉居民身份证〈/证件类型〉

〈证件类型代码〉01〈证件类型代码〉

〈证件号码〉330102*****1111〈/证件号码〉

〈首次参保年月〉19920701〈/首次参保年月〉

〈个人参保状态〉正常参保〈个人参保状态〉

〈个人缴费状态代码〉1〈个人缴费状态代码〉

〈个人缴费状态〉参保缴费〈个人缴费状态〉

〈缴费基数〉4000.00〈/缴费基数〉

〈本次开始日期〉19920701〈/本次开始日期〉

〈本次终止日期〉20181201〈/本次终止日期〉

〈经办人〉赵 $ ^{**} $ 〈经办人〉

〈经办日期〉20181201〈/经办日期〉

修改时间20190101修改时间

〈/养老保险人员参保信息表〉

〈养老保险离退休人员基本信息表〉

<时间属性>2018010120181231</时间属性>

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈人员编码〉10***00002〈/人员编码〉

<证件类型>居民身份证</证件类型>

〈证件类型代码〉01〈证件类型代码〉

<证件号码>330102*****1111</证件号码>

〈社会保障号码〉330102*****1111〈/社会保障号码〉

〈姓名〉王 $ ^{**} $ 〈/姓名〉

〈性别代码〉1〈/性别代码〉

〈性别〉男性〈/性别〉

<险种代码>110</险种代码>

〈险种名称〉企业职工基本养老保险〈/险种名称〉

〈离退休类别代码〉2〈/离退休类别代码〉

〈离退休类别〉正常退休〈/离退休类别〉

<核定年月>200001</核定年月>

〈参加工作日期〉19****01〈/参加工作日期〉

〈离退休日期〉20000101〈/离退休日期〉

〈待遇享受开始年月〉200002〈/待遇享受开始年月〉

〈视同缴费月数〉276〈/视同缴费月数〉

〈实际缴费月数〉84〈/实际缴费月数〉

〈中断月数〉0〈/中断月数〉

〈累计缴费月数〉360〈/累计缴费月数〉

〈特殊工种类型代码〉1〈/特殊工种类型代码〉

〈特殊工种类型〉有毒〈/特殊工种类型〉

〈特殊工种月数〉20〈/特殊工种月数〉

〈离退休时账户总金额〉12111.11〈/离退休时账户总金额〉

〈退休时核定养老金〉3000.00〈/退休时核定养老金〉

〈低保对象标识〉0〈/低保对象标识〉

〈补发月数〉1〈/补发月数〉

〈补发总金额〉3000.00〈/补发总金额〉

修改时间20190101修改时间

〈/养老保险离退休人员基本信息表〉

〈养老保险个人账户明细表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈人员编码〉10***00001〈/人员编码〉

〈姓名〉李 $ ^{**} $ 〈/姓名〉

〈证件类型〉居民身份证〈/证件类型〉

〈证件类型代码〉01〈证件类型代码〉

<证件号码>330102*****1111</证件号码>

〈就业状态代码〉01〈/就业状态代码〉

<就业状态名称>在业</就业状态名称>

<险种代码>110</险种代码>

<险种名称>企业职工基本养老保险</险种名称>

《年度》2018《/年度》

（年初账户金额）10000.00（/年初账户金额）

（当年账户本金划入）1000.00（/当年账户本金划入）

（当年账户利息划入）100.00（/当年账户利息划入）

（本年账户支出）500.00（本年账户支出）

（年末账户金额）10600.00（年末账户金额）

<历年缴纳月数>100</历年缴纳月数>

账户记息日期>20190501/账户记息日期>

<养老账户状态代码>1</养老账户状态代码>

〈养老账户状态〉正常结息〈/养老账户状态〉

修改时间20190101修改时间

〈/养老保险个人账户明细表〉

（养老保险人员转移信息表）

<时间属性>2018010120181231</时间属性>

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈人员编码〉10 $ ^{***} $ 00001〈/人员编码〉

〈姓名〉李**〈/姓名〉

<证件类型>居民身份证</证件类型>

<证件类型代码>01</证件类型代码>

<证件号码>330102*****1111</证件号码>

<险种代码>110</险种代码>

〈险种名称〉企业职工基本养老保险〈/险种名称〉

〈转移方向〉转出〈/转移方向〉

〈转移方向代码〉1〈/转移方向代码〉

〈对方社会保险机构名称〉**市社会保险事业管理中心**分中心〈/对方社会保险机构

## 名称>

〈对方所在单位名称〉上海市****有限公司〈/对方所在单位名称〉

〈视同缴费月数〉6〈/视同缴费月数〉

（实际缴费月数）311（实际缴费月数）

〈转移个人划转金额〉50000.00〈/转移个人划转金额〉

（转移单位划转金额）5000.00（/转移单位划转金额）

（基本养老保险基金转移总额）55000.00（/基本养老保险基金转移总额）

〈统筹部分转移金额〉0.00〈/统筹部分转移金额〉

〈经办人〉赵 $ ^{**} $ 〈经办人〉

〈经办日期〉20181201〈/经办日期〉

〈对方行政区划代码〉310106〈/对方行政区划代码〉

〈对方行政区划〉上海市静安区〈/对方行政区划〉

修改时间20190101修改时间

〈/养老保险人员转移信息表〉

〈/参保信息〉

### B.4 单位缴费类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

<div style="text-align: center;"><img src="imgs/img_in_image_box_82_516_119_556.jpg" alt="Image" width="3%" /></div>


## 〈单位缴费

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

XMLSchema 单位缴费.xsd"xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

〈职工基本养老保险单位征缴明细表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈/经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈结算单号〉100002〈/结算单号〉

〈单位编码〉10***001〈/单位编码〉

〈单位名称〉杭州市 *** 科技有限公司〈/单位名称〉

〈单位类型代码〉10〈/单位类型代码〉

〈单位类型〉企业〈/单位类型〉

〈经济类型代码〉173〈/经济类型代码〉

〈经济类型〉私营有限责任(公司)〈/经济类型〉

〈隶属关系代码〉40〈/隶属关系代码〉

（隶属关系）市、地区（隶属关系）

〈结算年月〉201812〈/结算年月〉

〈应繳年月〉201812〈/应繳年月〉

〈到账日期〉20190115〈/到账日期〉

〈征缴方式代码〉2〈/征缴方式代码〉

征缴方式>税务代征<征缴方式>

〈足额到账标志代码〉1〈/足额到账标志代码〉

〈足额到账标志〉是〈/足额到账标志〉

〈应缴类型代码〉10〈/应缴类型代码〉

〈应缴类型〉正常应缴〈/应缴类型〉

〈险种代码〉110〈/险种代码〉

〈险种名称〉企业职工基本养老保险〈/险种名称〉

〈应征人数〉10〈/应征人数〉

〈应缴总金额〉9900.00〈/应缴总金额〉

〈单位缴费基数总额〉45000.00〈单位缴费基数总额〉

〈个人缴费基数总额〉45000.00〈个人缴费基数总额〉

〈单位应缴金额〉6300.00〈单位应缴金额〉

〈个人应缴金额〉3600.00〈个人应缴金额〉

（滞纳金金额）0.00（滞纳金金额）

〈单位划账金额〉0.00〈单位划账金额〉

〈个人划账金额〉3600.00〈个人划账金额〉

〈单位实缴金额〉6300.00〈/单位实缴金额〉

〈单位实缴划入个人账户金额〉0.00〈单位实缴划入个人账户金额〉

〈个人实缴金额〉3600.00〈个人实缴金额〉

〈个人实缴划入个人账户金额〉3600.00〈个人实缴划入个人账户金额〉

修改时间20190101修改时间

〈/职工基本养老保险单位征缴明细表〉

机关事业单位养老保险单位征缴明细表

<时间属性>2018010120181231</时间属性>

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

<经办机构编码>330199</经办机构编码>

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈结算单号〉100003〈/结算单号〉

〈单位编码〉20***001〈/单位编码〉

〈单位名称〉杭州市 *** 管理中心〈/单位名称〉

〈单位类型代码〉55〈/单位类型代码〉

〈单位类型〉全额拨款事业单位〈/单位类型〉

〈隶属关系代码〉40〈/隶属关系代码〉

（隶属关系）市、地区（隶属关系）

〈结算年月〉201812〈/结算年月〉

〈应缴年月〉201812〈/应缴年月〉

〈到账日期〉20190120〈/到账日期〉

<征缴方式代码>2</征缴方式代码>

征缴方式>税务代征<征缴方式>

〈足额到账标志代码〉1〈/足额到账标志代码〉

〈足额到账标志〉是〈/足额到账标志〉

〈应缴类型代码〉10〈/应缴类型代码〉

〈应缴类型〉正常应缴〈/应缴类型〉

<险种代码>120</险种代码>

〈险种名称〉机关事业单位养老保险〈/险种名称〉

〈应征人数〉10〈/应征人数〉

〈应缴总金额〉16800.00〈/应缴总金额〉

〈单位缴费基数总额〉70000.00〈单位缴费基数总额〉

〈个人缴费基数总额〉70000.00〈个人缴费基数总额〉

〈单位应缴金额〉11200.00〈/单位应缴金额〉

〈个人应缴金额〉5600.00〈个人应缴金额〉

〈滞纳金金额〉0.00〈/滞纳金金额〉

〈单位划账金额〉0.00〈单位划账金额〉

〈个人划账金额〉5600.00〈个人划账金额〉

〈单位实缴金额〉11200.00〈单位实缴金额〉

〈单位实缴划入个人账户金额〉0.00〈单位实缴划入个人账户金额〉

〈个人实缴金额〉5600.00〈个人实缴金额〉

〈个人实缴划入个人账户金额〉5600.00〈个人实缴划入个人账户金额〉

修改时间20190101修改时间

〈/机关事业单位养老保险单位征缴明细表〉

〈/单位缴费〉

### B.5 个人缴费类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

〈人员缴费

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

XMLSchema 人员缴费.xsd"xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

〈城乡居民基本养老保险个人征缴明细表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈/经办机构〉

〈险种代码〉170〈/险种代码〉

〈险种名称〉城乡居民社会养老保险〈/险种名称〉

〈街道或乡镇编码〉330106013〈街道或乡镇编码〉

〈街道或乡镇〉西湖区文新街道〈街道或乡镇〉

〈社区或村编码〉330106013013〈/社区或村编码〉

〈社区或村〉阳光社区〈/社区或村〉

〈人员编码〉30***0001〈/人员编码〉

〈社会保障号码〉33010*****011111〈/社会保障号码〉

〈证件类型〉居民身份证〈/证件类型〉

〈证件类型代码〉01〈证件类型代码〉

〈证件号码〉33010*****1011111〈/证件号码〉

〈姓名〉李 $ ^{**} $ 〈/姓名〉

〈应缴类型代码〉10〈/应缴类型代码〉

〈应缴类型〉正常应缴〈/应缴类型〉

〈应缴年度〉2019〈/应缴年度〉

〈结算年月〉201812〈/结算年月〉

〈个人应缴金额〉100.00〈个人应缴金额〉

〈个人实缴金额〉100.00〈个人实缴金额〉

〈划入个人账户金额〉100.00〈/划入个人账户金额〉

〈中央财政补贴〉0.00〈/中央财政补贴〉

〈省级财政补贴〉0.00〈/省级财政补贴〉

<市级财政补贴>0.00</市级财政补贴>

〈县区财政补贴〉30.00〈/县区财政补贴〉

〈足额到账标志代码〉1〈/足额到账标志代码〉

〈足额到账标志〉是〈/足额到账标志〉

〈到账日期〉20181210〈到账日期〉

〈本年缴费月数〉12〈/本年缴费月数〉

<征缴方式代码>2</征缴方式代码>

征缴方式>税务代征<征缴方式>

修改时间20190101修改时间

〈/城乡居民基本养老保险个人征缴明细表〉

〈职工基本养老保险个人征缴明细表〉

<时间属性>2018010120181231</时间属性>

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

<经办机构编码>330199</经办机构编码>

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈结算单号〉100005〈/结算单号〉

〈结算年月〉201812〈/结算年月〉

〈应繳年月〉201812〈/应繳年月〉

〈应缴类型代码〉10〈/应缴类型代码〉

〈应缴类型〉正常应缴〈/应缴类型〉

〈人员编码〉100***0001〈/人员编码〉

〈社会保障号码〉3301021****1011111〈/社会保障号码〉

<证件类型>居民身份证</证件类型>

<证件类型代码>01</证件类型代码>

<证件号码>330102*****1111</证件号码>

〈姓名〉李 $ ^{**} $ 〈/姓名〉

〈单位编码〉100 $ ^{***} $ 01〈/单位编码〉

〈单位名称〉杭州市 *** 科技有限公司〈/单位名称〉

<险种代码>110</险种代码>

〈险种名称〉企业职工基本养老保险〈/险种名称〉

〈应缴总金额〉990.00〈/应缴总金额〉

（缴费基数）4500.00（缴费基数）

〈单位缴费比例〉0.1400〈单位缴费比例〉

〈单位应缴金额〉630.00〈单位应缴金额〉

〈单位划账金额〉0.00〈单位划账金额〉

〈个人缴费比例〉0.0800〈个人缴费比例〉

〈个人应缴金额〉360.00〈个人应缴金额〉

〈个人实缴金额〉360.00〈个人实缴金额〉

〈个人划账金额〉360.00〈个人划账金额〉

〈财政划账金额〉0.00〈/财政划账金额〉

〈其他补充金额〉0.00〈其他补充金额〉

〈其他划账金额〉0.00〈其他划账金额〉

<核销标志>未核销</核销标志>

〈足额到账标志代码〉1〈/足额到账标志代码〉

〈足额到账标志〉是〈/足额到账标志〉

〈到账日期〉20190120〈到账日期〉

〈经办人〉赵 $ ^{**} $ 〈/经办人〉

<经办日期>20181201</经办日期>

修改时间20190101修改时间

〈/职工基本养老保险个人征缴明细表〉

〈机关事业单位养老保险个人征缴明细表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈结算单号〉100005〈/结算单号〉

〈结算年月〉201812〈/结算年月〉

〈应缴年月〉201812〈/应缴年月〉

〈应缴类型代码〉10〈/应缴类型代码〉

〈应缴类型〉正常应缴〈/应缴类型〉

〈人员编码〉2000 $ ^{***} $ 001〈/人员编码〉

〈社会保障号码〉3301021****1011111〈/社会保障号码〉

<证件类型>居民身份证</证件类型>

〈证件类型代码〉01〈证件类型代码〉

<证件号码>3301021****1011111</证件号码>

〈姓名〉李 $ ^{**} $ 〈/姓名〉

〈单位编码〉20***001〈/单位编码〉

〈单位名称〉杭州市 *** 管理中心〈/单位名称〉

〈险种代码〉120〈/险种代码〉

〈险种名称〉机关事业单位养老保险〈/险种名称〉

〈应缴总金额〉1680.00〈/应缴总金额〉

（缴费基数）7000.00（缴费基数）

〈单位缴费比例〉0.1600〈/单位缴费比例〉

〈单位应缴金额〉1120.00〈/单位应缴金额〉

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

<单位划账金额>0.00<单位划账金额>

<个人缴费比例>0.0800<个人缴费比例>

<个人应缴金额>560.00<个人应缴金额>

<个人实缴金额>560.00<个人实缴金额>

<个人划账金额>560.00<个人划账金额>

<财政划账金额>0.00<财政划账金额>

<其他补充金额>0.00<其他补充金额>

<其他划账金额>0.00<其他划账金额>

<核销标志>未核销<核销标志>

<足额到账标志代码>1<足额到账标志代码>

<足额到账标志>是<足额到账标志>

<到账日期>20190120<到账日期>

<经办人>赵**<经办人>

<经办日期>20181201<经办日期>

<修改时间>20190101<修改时间>

事业单位养老保险个人征缴明细表

〈/人员缴费〉

### B.6 待遇支付类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

待遇支付

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

XMLSchema 待遇支付.xsd"xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

〈养老保险待遇支付明细表〉

〈时间属性〉2018010120181231〈/时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈/经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈/经办机构〉

〈待遇支付明细序号〉1000001〈/待遇支付明细序号〉

〈人员编码〉1000***002〈/人员编码〉

〈社会保障号码〉330102*****1111〈/社会保障号码〉

〈证件类型〉居民身份证〈/证件类型〉

〈证件类型代码〉01〈证件类型代码〉

〈证件号码〉330102*****1111〈/证件号码〉

〈姓名〉王**〈/姓名〉

〈单位编码〉10 $ ^{***} $ 003〈/单位编码〉

〈单位名称〉杭州市 *** 股份公司〈/单位名称〉

<险种代码>110</险种代码>

<险种名称>企业职工基本养老保险</险种名称>

<结算年月>201812</结算年月>

<待遇年月>201812</待遇年月>

<待遇项目代码>100011</待遇项目代码>

<待遇项目名称>基础养老金</待遇项目名称>

<待遇享受开始年月>200002</待遇享受开始年月>

<个账支付金额>211.11</个账支付金额>

<待遇金额>3500.11</待遇金额>

<领取人姓名>王**</领取人姓名>

<领取关系>本人</领取关系>

<领取人证件号码>330102****1111</领取人证件号码>

<开户银行名称>工商银行杭州市**支行</开户银行名称>

<银行账户名称>王**</银行账户名称>

<银行账号>120****11110001</银行账号>

<待遇发放方式代码>11</待遇发放方式代码>

<待遇发放方式>委托银行发放</待遇发放方式>

<待遇项目支付类型代码>0</待遇项目支付类型代码>

<待遇项目支付类型>固定</待遇项目支付类型>

<统筹类型代码>1</统筹类型代码>

<统筹类型>统筹内</统筹类型>

<经办人>赵**</经办人>

<经办日期>20181201</经办日期>

<修改时间>20190101</修改时间>

养老保险待遇支付明细表>

支付>

### B.7 信息变更类 XML 实例

## 〈变更转移

<?xml version="1.0" encoding="GB 18030"?>

〈养老保险单位变更信息表〉

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈经办人〉赵 $ ^{**} $ 〈经办人〉

〈单位编码〉10 $ ^{***} $ 001〈/单位编码〉

〈单位变更类型代码〉02〈单位变更类型代码〉

〈单位变更类型〉单位中断缴费〈/单位变更类型〉

〈变更前信息〉参保缴费〈/变更前信息〉

〈变更后信息〉暂停缴费（中断）〈/变更后信息〉

〈变更原因代码〉0020〈/变更原因代码〉

〈变更原因〉组织中断缴费〈/变更原因〉

〈变更日期〉20181201〈/变更日期〉

修改时间20190101修改时间

〈/养老保险单位变更信息表〉

（养老保险人员参保情况变更信息表）

〈时间属性〉2018010120181231〈/时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈经办人〉赵 $ ^{**} $ 〈经办人〉

〈人员变更流水号〉100001〈/人员变更流水号〉

〈人员编码〉100 $ ^{***} $  0001〈/人员编码〉

〈姓名〉李**〈/姓名〉

〈社会保障号码〉330102*****1111〈/社会保障号码〉

<证件类型>居民身份证</证件类型>

〈证件类型代码〉01〈证件类型代码〉

〈证件号码〉330102*****1111〈/证件号码〉

〈首次参保年月〉19930101〈/首次参保年月〉

〈个人变更类型代码〉22〈个人变更类型代码〉

〈个人变更类型〉中断缴费〈/个人变更类型〉

〈变更原因代码〉6301〈/变更原因代码〉

〈变更原因〉在职人员解除/终止劳动合同〈/变更原因〉

〈变更前信息〉参保缴费〈/变更前信息〉

〈变更后信息〉暂停缴费（中断）〈/变更后信息〉

〈变更日期〉20181201〈/变更日期〉

修改时间20190101修改时间

〈/养老保险人员参保情况变更信息表〉

〈/变更转移〉

### B.8 参数类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

## 参数信息

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/

XMLSchema 参数信息.xsd"xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns="http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

## 参数表

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

<经办机构编码>330199</经办机构编码>

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

<险种代码>110</险种代码>

<险种名称>企业职工基本养老保险</险种名称>

参数类别编码 AAB019 参数类别编码

参数类别名称单位类型参数类别名称

参数值>10/参数值>

〈参数名称〉企业〈参数名称〉

〈变更日期〉20010101〈/变更日期〉

〈有效标志〉是〈/有效标志〉

修改时间20190101修改时间

## 〈/参数表〉

养老待遇类型表

〈时间属性〉2018010120181231〈时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

<经办机构编码>330199</经办机构编码>

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

〈险种代码〉110〈/险种代码〉

〈险种名称〉企业职工基本养老保险〈/险种名称〉

〈待遇项目代码〉100011〈/待遇项目代码〉

〈待遇项目名称〉基础养老金〈/待遇项目名称〉

〈待遇项目支付类型代码〉0〈/待遇项目支付类型代码〉

〈待遇项目支付类型〉固定〈/待遇项目支付类型〉

〈统筹类型代码〉1〈/统筹类型代码〉

〈统筹类型〉统筹内〈/统筹类型〉

〈基金列支类型代码〉110100〈/基金列支类型代码〉

〈基金列支类型〉企业职工基本养老保险统筹基金〈/基金列支类型〉

〈有效标志〉是〈/有效标志〉

修改时间20190101修改时间

## 〈/养老待遇类型表〉

〈参数信息〉

### B.9 财务类 XML 实例

<?xml version="1.0" encoding="GB 18030"?>

财务信息

xsi: schemaLocation = "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema 财务信息.xsd" xmlns:养老保险基金

= "http://sxbw.audit.gov.cn/AppsDataInterfaceStandard/2019/Pension/XMLSchema" xmlns

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

〈会计科目表〉

〈时间属性〉2018010120181231〈/时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

<账套号>ZT001</账套号>

（账套名称）养老基金职工（/账套名称）

〈会计年度〉2018〈/会计年度〉

〈科目编码〉1002001〈科目编码〉

〈科目名称〉银行存款--工行〈/科目名称〉

〈余额方向〉借〈/余额方向〉

修改时间20190101修改时间

〈/会计科目表〉

〈科目余额表〉

〈时间属性〉2018010120181231〈/时间属性〉

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

〈经办机构编码〉330199〈经办机构编码〉

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

<账套号>ZT001</账套号>

（账套名称）养老基金职工（/账套名称）

〈科目编码〉1002001〈科目编码〉

〈科目名称〉银行存款--工行〈科目名称〉

〈会计年度〉2018〈/会计年度〉

〈会计期间〉1月〈/会计期间〉

修改时间20190101修改时间

〈余额方向〉借〈/余额方向〉

（期初余额）100000.00（期初余额）

〈本期借方发生额〉9000.00〈/本期借方发生额〉

（本期贷方发生额）8000.00（本期贷方发生额）

（期末余额）1010.00（/期末余额）

〈/科目余额表〉

（凭证明细表）

<时间属性>2018010120181231</时间属性>

〈地域属性〉330000〈/地域属性〉

〈行政区划代码〉330100〈行政区划代码〉

〈行政区划〉杭州市〈/行政区划〉

<经办机构编码>330199</经办机构编码>

〈经办机构〉**市社会保险管理服务中心〈经办机构〉

<账套号>ZT001</账套号>

<账套名称>养老基金职工</账套名称>

〈会计年度〉2018〈/会计年度〉

<会计期间>1月</会计期间>

凭证编号JZ01-001/凭证编号

<凭证日期>20180101</凭证日期>

〈科目编码〉1002001〈科目编码〉

〈科目名称〉银行存款——工行〈/科目名称〉

〈摘要〉支付养老金〈/摘要〉

借方金额>0.00（借方金额）

贷方金额>10000.00（贷方金额）

〈制单人〉王 **〈/制单人〉

〈审核人〉孙**〈/审核人〉

<记账人>马**</记账人>

修改时间20190101修改时间

《凭证明细表》

<财务信息>

## 参 考 文 献

[1] GB/T 18391.1—2009 信息技术 元数据注册系统(MDR) 第1部分:框架

[2] GB/T 31596.2—2015 社会保险术语 第2部分：养老保险

___