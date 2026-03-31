

# 中华人民共和国金融行业标准

JR/T 0294.3—2024

# 金融市场交易报告数据要素指南   第 3 部分：其他关键数据要素

# Guide on data elements of financial market trade reporting— Part 3: Other critical data elements

2024-09-03 发布

2024-09-03 实施

发布

Powered by TCPDF (www.tcpdf.org)

## 目 次

前言.....II    
引言.....III    
1 范围.....1    
2 规范性引用文件.....1    
3 术语和定义.....1    
4 其他关键数据要素数据格式说明.....2    
5 其他关键数据要素.....3    
参考文献.....28

## 前言

本文件按照GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

本文件是JR/T 0294—2024《金融市场交易报告数据要素指南》的第3部分，JR/T 0294—2024已经发布了以下部分：

——第1部分：全球唯一产品识别码；

——第2部分：全球唯一交易识别码：

——第3部分：其他关键数据要素。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国金融标准化技术委员会（SAC/TC 180）提出并归口。

本文件起草单位：中国人民银行科技司、中国证券监督管理委员会科技监管司、中国外汇交易中心（全国银行间同业拆借中心）、中国人民银行湖北省分行、成方金融科技有限公司、北京国家金融标准化研究院有限责任公司、银行间市场清算所股份有限公司、中国期货市场监控中心有限责任公司。

本文件主要起草人：李伟、杨富玉、李兴锋、蒋东兴、杨帆、杨冬华、朱迪恺、冯蕾、刘子群、周云晖、王蕾蕾、姜才康、茅廷、胡冰冰、靳亚茹、林茜濛、刘晓、刘彼洋、周夕崇、谢彦丽、张晋钰、贺宇、唐卓、薄舜添、何鹏、卢欢、狄休、李钟、张小雪。

## 引言

2008年金融危机后，在二十国集团支持下，金融稳定理事会（FSB）推动主要国家建设场外衍生品交易报告库，并针对交易主体、产品和交易识别构建一套全球统一的识别编码体系，以实现全球场外衍生品交易数据的互联互通。

为了更好地为我国金融市场交易报告制度建设提供数据标准支持，现根据支付与市场基础设施委员会（CPMI）和国际证监会组织（IOSCO）发布的《关键数据要素（CDE）协调技术指引》制定本文件，指导交易报告数据要素字段的设计和使用，为金融市场交易报告库的数据建设提供标准支撑，并提高报告库数据标准的国际化接轨水平。

Powered by TCPDF (www.tcpdf.org)

# 金融市场交易报告数据要素指南   第 3 部分：其他关键数据要素

## 1 范围

本文件提供了除全球唯一交易识别码(UTI)与全球唯一产品识别码(UPI)之外向交易报告库(TR)报告所必要的其他关键数据要素的定义、格式和允许值等相关内容。

本文件适用于中华人民共和国境内法人机构及私募基金产品等非法人机构向TR报告的场外衍生品交易。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

JR/T 0294.1—2024 金融市场交易报告数据要素指南 第1部分：全球唯一产品识别码

JR/T 0294.2—2024 金融市场交易报告数据要素指南 第2部分：全球唯一交易识别码

ISO 3166-1:2020 世界各国和地区及其行政区划名称代码 第1部分：国家和地区代码（Codes for the representation of names of countries and their subdivisions—Part 1: Country code）

注：GB/T 2659.1—2022 世界各国和地区及其行政区划名称代码 第1部分：国家和地区代码（ISO 3166-1:2020，MOD）。

ISO 4217 表示货币的代码（Codes for the representation of currencies）

注：GB/T 12406—2022 表示货币的代码（ISO 4217:2015，MOD）。

ISO 8601-1:2019 日期和时间 信息交换表示法 第1部分：基本原则（Date and time—Representations for information interchange—Part 1: Basic rules）

ISO 10383 证券和相关金融工具 交易所和市场识别码（Securities and related financial instruments—Codes for exchanges and market identification (MIC))

ISO 17442-1 金融服务 全球法人识别编码 第1部分：编码说明（Financial service—Legal entity identifier (LEI)—Part 1: Assignment）

ISO 20022-1 金融服务 金融业通用报文方案 第1部分：元模型（Financial services—Universal financial industry message scheme—Part 1: Metamodel）

注：GB/T 27926.1 金融服务 金融业通用报文方案 第1部分：元模型（ISO 20022-1，IDT）。

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

全球唯一交易识别码 global unique transaction identifier; UTI

在交易主体和（或）在该交易发生的管理体系的认可下，分配给一笔金融交易的全球唯一字符串。

[来源：JR/T 0294.2—2024，3.1]

### 3.2 

全球唯一产品识别码 global unique product identifier; UPI

在交易过程中唯一识别每个场外衍生品的代码。

[来源：JR/T 0294.1—2024，3.1]

### 3.3 

其他关键数据要素 other critical data elements

除UTI和UPI以外其他向交易报告库报告所必要的关键数据要素。

### 3.4 

法定实体 legal entity

法人

根据法律成立的组织。

[来源：GB/T 42495.1—2023，3.1]

### 3.5 

全球法人识别编码 global legal entity identifier; LEI

法定实体的全球唯一识别码。

### 3.6 

协调世界时 universal time coordinated; UTC

以原子时秒长为基础，在时刻上尽量接近于世界时的一种时间计量系统。

注：协调世界时又称世界统一时间、世界标准时间、国际协调时间。

## 4 其他关键数据要素数据格式说明

其他关键数据要素数据格式细节见表1。

<div style="text-align: center;">表 1 其他关键数据要素数据格式细节</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>概述</td><td style='text-align: center;'>补充说明</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>YYYY-MM-DD</td><td style='text-align: center;'>日期。</td><td style='text-align: center;'>“YYYY”是4位数的年。“MM”是2位数的月份。“DD”是2位数的日期。</td><td style='text-align: center;'>2015-07-06（对应2015年7月6日）</td></tr></table>

<div style="text-align: center;">表 1 其他关键数据要素格式细节（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>概述</td><td style='text-align: center;'>补充说明</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>YYYY-MM-DDThh:mm:ssC</td><td style='text-align: center;'>日期和时间。</td><td style='text-align: center;'>“YYYY”“MM”“DD”同上。“hh”是2位数的时（取值为00至23，不允许am或者pm格式）。“mm”是2位数的分（取值为00至59）。“ss”是2位数的秒（取值为00至59）。“T”是固定的，表示时间要素的开始。“C”是固定的，表示时间以UTC+8表示（对应中国北京时间，不是当地时间。）</td><td style='text-align: center;'>2014-11-05T13:15:30C（对应中国北京时间2014年11月5日下午1:15:30）</td></tr><tr><td style='text-align: center;'>Num(M,D)</td><td style='text-align: center;'>最长M位的数字，包括小数点后D位。</td><td style='text-align: center;'>长度不固定，但整数部分仅限于M个数字字符内，包括小数点后面最多D个字符，例如Num(10,5)。如果该值的小数点后超过D位数，则报告交易对手可四舍五入。</td><td style='text-align: center;'>1352.6715667.6768817857087690-20000.25-0.257</td></tr><tr><td style='text-align: center;'>Num(M)</td><td style='text-align: center;'>最长M位的数字，不允许有小数点。</td><td style='text-align: center;'>长度不固定，但最多M个数字字符，例如Num(5)。</td><td style='text-align: center;'>1234512320</td></tr><tr><td style='text-align: center;'>Char(M)</td><td style='text-align: center;'>M个字母或数字字符。</td><td style='text-align: center;'>长度固定，M个字母或数字字符。输入不足M个字母或者数字时，由空格填充，例如Char(3)。</td><td style='text-align: center;'>CNYX1X999</td></tr><tr><td style='text-align: center;'>Varchar(M)</td><td style='text-align: center;'>最多M个字母或数字字符。</td><td style='text-align: center;'>长度不固定，但最多M个字母或数字字符，例如Varchar(10)。</td><td style='text-align: center;'>asgGEF2643aaaaaaaaax</td></tr><tr><td style='text-align: center;'>Boolean</td><td style='text-align: center;'>布尔字符。</td><td style='text-align: center;'>包括“True”或“False”。</td><td style='text-align: center;'>True（是）False（否）</td></tr><tr><td colspan="4">注：1.以Num(10,5)、Num(5)、Char(3)和Varchar(10)格式给出的数字只是示例；可使用相同的逻辑生成类似的格式（具有不同的字符数）。2.am指上午，pm指下午。</td></tr></table>

## 5 其他关键数据要素

### 5.1 与日期和时间戳相关的数据要素

#### 5.1.1 生效日期（Effective date）

生效日期数据格式见表2。

<div style="text-align: center;">表 2 生效日期数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，生效的未调整日期。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr></table>

<div style="text-align: center;">表 2 生效日期数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DD，基于UTC+8时间。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效日期。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>到期日期、提前终止日期。</td></tr></table>

#### 5.1.2 到期日期（Expiration date）

到期日期数据格式见表3。

<div style="text-align: center;">表 3 到期日期数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，停止生效的未调整日期。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DD，基于UTC+8时间。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效日期。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>生效日期、提前终止日期、执行时间戳。到期日期可与执行时间相等或在其之后。</td></tr><tr><td colspan="2">注：提前终止不影响本数据要素。</td></tr></table>

#### 5.1.3 提前终止日期（Early termination date）

提前终止日期数据格式见表4。

<div style="text-align: center;">表 4 提前终止日期数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>报告交易提前终止（到期）的生效日期。若1个交易对手（或多个交易对手）在交易到期日之前临时终止交易，则该日期为提前终止日期。场景示例如下。a）协商提前终止。b）根据可选的提前终止条款提前终止（相互看跌）。c）更新。d）抵消（净额结算）交易。e）期权行使。f）交易压缩。g）原合同中规定的提前终止条款，即可赎回互换。h）信用违约。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DD，基于UTC+8时间。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效日期。</td></tr></table>

<div style="text-align: center;">表 4 提前终止日期数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>有效日期、到期日期、执行时间。提前终止日期（如果适用的话）可与执行时间戳相等或在其之后，并且早于到期日期。</td></tr></table>

#### 5.1.4 报告时间戳（Reporting timestamp）

报告时间戳数据格式见表5。

<div style="text-align: center;">表 5 报告时间戳数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>向TR提交报告的日期和时间。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DDThh:mm:ssC，基于UTC+8时间。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效的日期和时间。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>执行时间戳、报告时间戳。报告时间戳可与执行时间戳相等或在其之后。</td></tr></table>

#### 5.1.5 执行时间戳（Execution timestamp）

执行时间戳数据格式见表6。

<div style="text-align: center;">表 6 执行时间戳数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>最初执行事务的日期和时间。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DDThh:mm:ssC，基于UTC+8时间。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效的日期和时间。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>报告时间戳。执行时间戳可在报告时间之前或与其相等。</td></tr><tr><td colspan="2">注：该数据在UTI的整个生命周期内保持不变。</td></tr></table>

### 5.2 与交易对手方和受益人相关的数据要素

#### 5.2.1 交易对手方 1（交易报告方）（Counterparty 1（reporting counterparty））

交易对手方1数据格式见表7。

<div style="text-align: center;">表 7 交易对手方 1 数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，履行报告义务的对手方的标识符。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (20)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>全球LEI基金会公布的LEI数据编码，包含20个字母或数字字符。</td></tr></table>

<div style="text-align: center;">表 7 交易对手方 1 数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>买方标识符和卖方标识符（方向1）、付款方标识符和接收方标识符（方向2）、其他支付付款方、其他付款接收方和受益人1。</td></tr><tr><td colspan="2">注：1. 在由基金经理代表基金执行分配的场外衍生品交易的情况下，交易对手方是该基金而不是基金经理。2. 如果交易对手方1是交易的受益人，则交易对手方的标识符将同时在2个数据要素（交易对手方1和受益人1）中体现。</td></tr></table>

#### 5.2.2 交易对手方 2（Counterparty 2）

交易对手方2数据格式见表8。

<div style="text-align: center;">表 8 交易对手方 2 数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，第二交易对手方的标识符。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>交易对手方2数据格式分成法定实体和非法定实体2种情况，具体内容如下。a）当交易对手方2为法定实体时，数据格式为Char(20)。b）当交易对手方2为非法定实体时，数据格式为Varchar(72)。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>交易对手方2允许值分成法定实体和非法定实体2种情况，具体内容如下。a）当交易对手方2为法定实体时，允许值为全球LEI基金会公布的LEI数据编码，包含20个字母或数字字符。b）当交易对手方2为非法定实体时，允许值为交易对手方1（交易报告方）的LEI后跟交易对手方1（交易报告方）为交易对手方2指定和维护的唯一标识符，最多72个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>方向1、方向2、其他支付付款方、其他付款接收方和受益人2。</td></tr><tr><td colspan="2">注：1. 在由基金经理代表基金执行分配的衍生品交易的情况下，交易对手方是该基金而不是基金经理。2. 如果交易对手方2是交易的受益人，则交易对手方的标识符将同时在2个数据要素（交易对手方2和受益人2）中体现。</td></tr></table>

#### 5.2.3 交易对手方 2 标识类型（Counterparty 2 identifier type）

交易对手方2标识类型数据格式见表9。

<div style="text-align: center;">表 9 交易对手方 2 标识类型数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示是否使用LEI来识别交易对手方2的标识。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Boolean</td></tr></table>

<div style="text-align: center;">表 9 交易对手方 2 标识类型数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>交易对手方2标识类型允许值为布尔字符，具体内容如下。a）“True”代表交易对手方2为法定实体，使用LEI识别。b）“False”代表交易对手方2为非法定实体，不使用LEI识别。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易对手方2。</td></tr></table>

#### 5.2.4 方向（Direction）

##### 5.2.4.1 概述

报告对手方应使用买方标识符和卖方标识符（方向1）来标识报告对手方的交易方向，指交易方向为“买”或“卖”，该方法称为“模式1”；使用付款方标识符和接收方标识符（方向2）来标识每个交易对手方，指交易对手方的“付款方”或“接收方”，该方法称为“模式2”。

报告对手方不宜同时使用上述 2 种模式，可根据相应金融工具的类型采取适当的模式。

注：模式2将识别每个交易对手方的付款方或接收方，且每个交易对手方将关联1组数据要素，其中一些要素可能仅针对某一个交易对手方，有关利率互换的数据要素包括但不限于以下内容。

a）方向2。

b）名义货币。

c）名义金额。

d）固定利率（不适用于浮动利率交易对手方）。

e）价差（不适用于固定利率交易对手方）。

f）支付频率周期。

g）支付频率周期乘数。

h）计息天数惯例。

##### 5.2.4.2 买方标识符和卖方标识符(方向1)(Direction 1 or Buyer identifier and Seller identifier)

买方标识符和卖方标识符（方向1）数据格式见表10。

<div style="text-align: center;">表 10 买方标识符和卖方标识符（方向 1）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交易时确定报告对手是买方还是卖方的标识或交易时确定买方的对手方标识符和作为卖方的对手方标识符。以下是适用示例清单。a）大多数远期和类似远期合同（外汇远期和差额交割远期（NDF）除外）。b）大多数期权和类似期权的合约，包括掉期、上限和下限。c）信用违约互换（信用保护买方或信用保护卖方）。d）方差、波动性相关互换合约。e）点差合约和差价合约。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>方向1的数据格式包含以下3种。a）当未强调方向1为法定实体或非法定实体时，数据格式为Char(4)。b）当方向1为法定实体时，数据格式为Char(20)。c）当方向1为非法定实体时，数据格式为Varchar(72)。</td></tr></table>

<div style="text-align: center;">表 10 买方标识符和卖方标识符（方向 1）数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>方向1的允许值包含以下3种。
a）当未强调方向1为法定实体或非法定实体时，允许值“BYER”代表买方，“SLLR”代表卖方。
b）当方向1为法定实体时，允许值为全球LEI基金会公布的LEI数据编码，包含20个字母或数字字符。
c）当方向1为非法定实体时，允许值为交易对手方1（交易报告方）的LEI后跟交易对手方1（交易报告方）为方向1指定和维护的唯一标识符，最多72个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易对手方1、交易对手方2。</td></tr><tr><td colspan="2">注：本数据要素不适用于方向2或方向2所涵盖的金融工具类型。</td></tr></table>

##### 5.2.4.3 付款方标识符和接收方标识符（方向2）（Direction 2 or Payer identifier and Receiver identifier）

付款方标识符和接收方标识符（方向2）数据格式见表11。

<div style="text-align: center;">表 11 付款方标识符和接收方标识符（方向 2）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在交易时确定报告对手方是付款方还是接收方的标识或在交易时确定的付款方交易对手方和接收方交易对手方的标识符。以下是适用示例清单。a）大多数互换和类似互换的合约，包括利率互换、信用总回报互换和股权互换（信用违约互换、方差、波动性和相关性互换除外）。b）外汇掉期、远期、无本金交割远期。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>方向2的数据格式包含以下3种。a）当未强调方向2为法定实体或非法定实体时，数据格式为Char(4)。b）当方向2为法定实体时，数据格式为Char(20)。c）当方向2为非法定实体时，数据格式为Varchar(72)。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>方向2的允许值包含以下3种。a）当未强调方向2为法定实体或非法定实体时，允许值“MAKE”代表付款方，“TAKE”代表接收方。b）当方向2为法定实体时，允许值为全球LEI基金会公布的LEI数据编码，包含20个字母或数字字符。c）当方向2为非法定实体时，允许值为交易对手方1（交易报告方）的LEI后跟交易对手方1（交易报告方）为方向2指定和维护的唯一标识符，最多72个字母或数字字</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易对手方1、交易对手方2。</td></tr><tr><td colspan="2">注：本数据要素不适用于方向1或方向1所涵盖的金融工具类型。</td></tr></table>

#### 5.2.5 受益人 1（Beneficiary 1）

受益人1数据格式见表12。

<div style="text-align: center;">表 12 受益人 1 数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，为交易对手方1受益人的标识符，表示受合同产生的权利和义务约束的一方，而不是执行合同的任意一方代表或其他方。如果受益人是例如信托或集体投资等组织，则受益人标识符将标识该组织，而不是标识在该组织中持有所有权权益的实体。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>受益人1数据格式分成法定实体以及非法定实体2种情况，具体内容如下。a）当受益人1为法定实体时，数据格式为Char(20)。b）当受益人1为非法定实体时，数据格式为Varchar(72)。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>受益人1允许值分成法定实体和非法定实体2种情况，具体内容如下。a）当受益人1为法定实体时，允许值为全球LEI基金会公布的LEI数据编码，包含20个字母或数字字符。b）当受益人1为非法定实体时，允许值为交易对手方1（交易报告方）的LEI后跟交易对手方1（交易报告方）为受益人1指定和维护的唯一标识符，最多72个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易对手方1、方向1、方向2。</td></tr><tr><td colspan="2">注：1.如果受益人1是交易对手方，则受益人的标识将同时在2个数据要素（交易对手方1和受益人1）中体现。2.如果受益人1是有责任支付的实体，则受益人1和方向数据要素（方向1或方向2）中使用相同的标识符。</td></tr></table>

#### 5.2.6 受益人 1 标识类型（Beneficiary 1 type）

受益人1标识类型数据格式见表13。

<div style="text-align: center;">表 13 受益人 1 标识类型数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示是否使用LEI来识别受益人1。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Boolean</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>受益人1标识类型允许值为布尔字符，具体内容如下。a）“True”代表受益人1为法定实体，使用LEI识别。b）“False”代表受益人1为非法定实体，不使用LEI识别。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>受益人1。</td></tr></table>

#### 5.2.7 受益人 2（Beneficiary 2）

受益人2数据格式见表14。

<div style="text-align: center;">表 14 受益人 2 数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，交易对手方2受益人的标识符，可以成为约束合同中规定的权利和义务的第二方，而不是代表或以其他方式代表进行交易的任意一方。如果受益人是例如信托或集体投资等的组织，则受益人标识符将标识该组织，而不是标识在该组织中持有所有权权益的实体。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>受益人2数据格式分成法定实体和非法定实体2种情况，主要包括以下内容。a）当受益人2为法定实体时，数据格式为Char(20)。b）当受益人2为非法定实体时，数据格式为Varchar(72)。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>受益人2允许值分成法定实体和非法定实体2种情况，主要包括以下内容。a）当受益人2为法定实体时，允许值为全球LEI基金会公布的LEI数据编码，包含20个字母或数字字符。b）当受益人2为非法定实体时，允许值为交易对手方1（交易报告方）的LEI后跟交易对手方1（交易报告方）为受益人2指定和维护的唯一标识符，最多72个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易对手方2、方向1、方向2。</td></tr><tr><td colspan="2">注：1.如果受益人2是交易对手方，则受益人2的标识符将同时在2个数据要素（交易对手方2和受益人2）中体现。2.如果受益人2是有责任支付的实体，则受益人2和方向数据要素（方向1或方向2）中使用相同的标识符。</td></tr></table>

#### 5.2.8 受益人 2 标识类型（Beneficiary 2 type）

受益人2标识类型数据格式见表15。

<div style="text-align: center;">表 15 受益人 2 标识类型数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示是否使用LEI来识别受益人2。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Boolean</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>受益人2标识类型允许值为布尔字符，主要内容如下。a）“True”代表受益人2为法定实体，使用LEI识别。b）“False”代表受益人2为非法定实体，不使用LEI识别。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>受益人2。</td></tr></table>

### 5.3 与清算、交易、确认和结算相关的数据要素

#### 5.3.1 清算标识符（Cleared）

清算标识符数据格式见表 16。

<div style="text-align: center;">表 16 清算标识符数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>关于交易是否已纳入中央对手方清算或将提交中央对手方清算的标识。</td></tr></table>

<div style="text-align: center;">表 16 清算标识符数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(1)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>清算标识符的允许值包括“Y”“N”“I”3种，具体内容如下。a）“Y”代表是，已纳入中央对手方清算，用于β和γ交易（指中央对手方合同替代后生成的2笔新交易）。b）“N”代表否，未纳入中央对手方清算。c）“I”代表预备清算，将提交中央对手方清算，对于计划提交清算的α交易。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>中央对手方、清算成员。</td></tr><tr><td colspan="2">注：α交易指纳入中央对手方清算前的原双边交易。</td></tr></table>

#### 5.3.2 中央对手方（Central counterparty）

中央对手方数据格式见表17。

<div style="text-align: center;">表 17 中央对手方数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>清算交易的中央对手方（CCP）的识别码。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (20)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>全球LEI基金会公布的LEI数据编码，包含20个字母或数字。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>清算标识符、交易对手方1、交易对手方2。</td></tr><tr><td colspan="2">注：1.本数据要素不适用于清算标识符为“N”或“I”的交易。
2.中央对手方的识别码在交易对手方和中央对手方数据要素项下均要报告。</td></tr></table>

#### 5.3.3 清算会员（Clearing member）

清算会员数据格式见表18。

<div style="text-align: center;">表 18 清算会员数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，代表中央对手方提交清算的清算会员识别码。本数据要素适用于代理商清算模式和委托人清算模式下的交易，具体内容如下。a）在委托人清算模式下，清算会员既被识别为清算会员，又被识别为交易对手方，在清算过程中产生两笔交易：中央对手方与清算会员之间的交易，清算会员与交易对手之间的原a交易。b）在代理商清算模式下，清算会员仅被识别为清算代理人，而不被识别为清算产生的交易对手方。在这种模式下，交易对手方是中央对手方和客户。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 17442-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(20)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>全球LEI基金会公布的LEI数据编码，包含20个字母或数字。</td></tr></table>

<div style="text-align: center;">表 18 清算会员数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>清算标识符、交易对手方1、交易对手方2。</td></tr><tr><td colspan="2">注：1.本数据要素不适用于清算标识符为“N”或“I”的交易。2.如果清算会员是交易的对手方（委托人清算模式），则在2个数据要素（交易对手方和清算会员）中报告清算会员识别码。</td></tr></table>

#### 5.3.4 平台识别码（Platform identifier）

平台识别码数据格式见表19。

<div style="text-align: center;">表 19 平台识别码数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，用于识别交易工具所在的交易平台。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 10383</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(4)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>数据要素允许值分为以下2种类型。
a）如果涉及交易平台时，使用ISO 10383部分MIC码。
b）如果交易不涉及交易平台，则使用以下允许值。
——当使用的交易工具已上市，则允许值为“XOFF”。
——当使用的交易工具未上市，则允许值为“XXXX”。
——如果交易报告方无法根据管理要求确定该交易工具是否已上市，则允许值为“BILT”。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>无。</td></tr><tr><td colspan="2">注：ISO 10383已采标为GB/T 23696—2017。</td></tr></table>

#### 5.3.5 确认标识符（Confirmed）

确认标识符数据格式见表20。

<div style="text-align: center;">表 20 确认标识符数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>对于由JR/T 0294.2—2023规定的新的可报告交易，明确场外衍生品合约的法律约束条款是否已确认（记录并达成）。如果已记录并达成，明确是否进行了以下确认。a）通过共享的确认设施、平台或专用或双边电子系统（电子）。b）通过人工可读的书面文档，例如传真、文件或手动处理的电子邮件（非电子）。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(4)</td></tr></table>

<div style="text-align: center;">表 20 确认标识符数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>确认标识符的允许值分为“NCNF”“ECNF”“YCNF”3种，其中包括以下内容。a）“NCNF”代表法律约束条款未记录或未达成。b）“ECNF”代表法律约束条款记录并达成，且经电子化确认。c）“YCNF”代表法律约束条款记录并达成，且未经电子化确认。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>无。</td></tr><tr><td colspan="2">注：ISO 20022-1已采标为GB/T 27926.1。对于国际范围内通用的库概念存放于ISO 20022库；对于区域范围内适用的库概念存放于区域库，中国的区域库称为中国金融业通用报文库，公开访问途径为https://www.cufir.org.cn/cufir/index.html。</td></tr></table>

#### 5.3.6 最终合同结算日期（Final contractual settlement date）

最终合同结算日期数据格式见表21。

<div style="text-align: center;">表 21 最终合同结算日期数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>根据合同未调整的日期，所有现金或资产的转移在该日期之前完成，且交易对手方在该合同下不再对彼此承担任何未清偿的义务。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DD，基于UTC+8。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效日期。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>到期日期。最终合同结算日期在到期日期之后。</td></tr><tr><td colspan="2">注：对于可能没有最终合同结算日期的产品（例如美式期权），如果合同终止发生在到期日期，则该数据要素表示现金或资产的转移日期。</td></tr></table>

#### 5.3.7 结算货币（Settlement currency）

结算货币数据格式见表22。

<div style="text-align: center;">表 22 结算货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示用于交易现金结算的货币，对于多币种非净额的货币产品，表示交易对手方的结算货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (3)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>货币结算交割类型由JR/T 0294.1—2023规定。</td></tr><tr><td colspan="2">注：本数据要素不适用于以实物方式结算的产品（例如以实物方式结算的掉期期权交易）。</td></tr></table>

#### 5.3.8 结算地（Settlement location）

结算地数据格式见表23。

<div style="text-align: center;">表 23 结算地数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>合约规定的交易结算地点。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 3166-1:2020</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>按照GB/T 2659.1—2022的规定。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>GB/T 2659.1—2022中规定的国家代码。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>名义货币、买入货币、卖出货币。</td></tr><tr><td colspan="2">注:1.本数据要素仅适用于涉及离岸货币的交易(即不在ISO 4217货币列表上的货币,例如离岸人民币(CNH))。2.ISO 3166-1:2020已采标为GB/T 2659.1—2022。</td></tr></table>

### 5.4 与定期支付相关的数据要素

#### 5.4.1 计息天数惯例（Day count convention）

计息天数惯例数据格式见表24。

<div style="text-align: center;">表 24 计息天数惯例数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>计息周期的年分数，为计息周期中的天数除以相应年度天数。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(4)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>计息天数惯例包括以下允许值。A001、A002、A003、A004、A005、A006、A007、A008、A009、A010、A011、A012、A013、A014、A015、A016、A017、A018、A019、A020、NARR。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>与价格和支付有关的数据要素。</td></tr><tr><td colspan="2">注: 计息天数惯例允许值的含义见全国金融标准化技术委员会官方网站（https://cfstc.pbc.gov.cn/）下载专区“金融市场交易报告其他关键数据要素”。</td></tr></table>

#### 5.4.2 支付频率周期（Payment frequency period）

支付频率周期数据格式见表25。

<div style="text-align: center;">表 25 支付频率周期数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在场外衍生品交易中，合约中的支付频率或与支付频率相关的时间单位。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr></table>

<div style="text-align: center;">表 25 支付频率周期数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(4)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>支付频率周期允许值分为“DAIL”“WEEK”“MNTH”“YEAR”“ADHO”“TERM”6种，其中包括以下内容。a）“DAIL”代表“每日”。b）“WEEK”代表“每周”。c）“MNTH”代表“每月”。d）“YEAR”代表“每年”。e）“ADHO”代表“不定期支付”。f）“TERM”代表“按期付款”。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>支付频率周期系数。</td></tr></table>

#### 5.4.3 支付频率周期乘数（Payment frequency period multiplier）

支付频率周期乘数数据格式见表26。

<div style="text-align: center;">表 26 支付频率周期乘数数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>适用于每个交易对手方，决定周期性付款日期出现频率的时间单位数量（以支付频率周期倍数计）。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(18)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0，且最多18个数字。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>支付频率周期。</td></tr><tr><td colspan="2">注：每2个月进行1次支付的交易用支付频率周期“M NTH”（每月）和支付频率周期乘数2表示。如果支付频率周期为“ADHO”，则本数据要素不适用；如果支付频率周期为“TERM”，则支付频率周期乘数为1；如果支付频率周期为日间，则支付频率周期为“DAIL”，支付频率周期乘数为0。</td></tr></table>

### 5.5 与估值相关的数据要素

#### 5.5.1 估值金额（Valuation amount）

估值金额数据格式见表27。

<div style="text-align: center;">表 27 估值金额数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>在合约存续期间内的现值。估值金额以合约或合约组成部分的退出成本表示，即出售该合约将收到的价格。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr></table>

<div style="text-align: center;">表 27 估值金额数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意值且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>估值货币、估值时间戳、估值方法。</td></tr><tr><td colspan="2">注：估值金额宜结合估值货币与估值方法以及估值金额计算的时间信息，以更有意义的方式汇总估值金额。</td></tr></table>

#### 5.5.2 估值货币（Valuation currency）

估值货币数据格式见表28。

<div style="text-align: center;">表 28 估值货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>估值金额的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (3)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>估值金额、估值时间戳、估值方法。</td></tr></table>

#### 5.5.3 估值时间戳（Valuation timestamp）

估值时间戳数据格式见表29。

<div style="text-align: center;">表 29 估值时间戳数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由中央对手方（CCP）提供或使用当前或最近可用市场价格计算的日期和时间。例如如果货币汇率是交易估值的基础，则估值时间戳指的是用于估值计算汇率的时间点。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 8601-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>YYYY-MM-DDThh:mm:ssC，基于UTC+8。</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>任意有效的日期和时间。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>估值金额、估值货币、估值方法。估值时间戳在生效日期当日或之后。</td></tr></table>

#### 5.5.4 估值方法（Valuation method）

估值方法数据格式见表30。

<div style="text-align: center;">表 30 估值方法数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交易报告方用于交易估值的数据源和方法。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (4)</td></tr></table>

<div style="text-align: center;">表 30 估值方法数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>估值方法的允许值有“MTMA”“MTMO”“CCPV”3种，其中包括以下内容。a）“MTMA”代表按市值计量。b）“MTMO”代表按模型计量。c）“CCPV”代表中央对手方估值。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>估值金额、估值货币、估值时间戳。估值时间戳在生效日期当日或之后。</td></tr><tr><td colspan="2">注：1.如果使用表31中被归类为按模型计算的估值输入，则整个估值方法将归类为按模型计量。2.如果仅使用表31中被归类为按市值计价的估值输入，则整个估值方法将被分类为按市值计量。</td></tr></table>

估值输入信息的分类见表31。

<div style="text-align: center;">表 31 估值输入信息的分类</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类型</td><td style='text-align: center;'>所使用的输入信息</td><td style='text-align: center;'>估值方法</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>估值方在计量日可获取的活跃市场中相同资产或相同负债的报价。活跃市场中的报价提供了最可靠的公允价值依据，只要可获取，无需调整即可用于计量公允价值，鲜有情况例外。活跃市场指资产或负债交易产生的频率和数量足以持续提供定价信息的市场。</td><td style='text-align: center;'>按市值计量。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>活跃市场中相同资产或相同负债的报价（不含类型1中可直接或间接观测到的资产或负债的市场报价）。</td><td style='text-align: center;'>按市值计量。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>不活跃市场中相同资产或相同负债的报价（不含类型1中可直接或间接观测到的资产或负债的市场报价）。</td><td style='text-align: center;'>按模型计量—不宜直接使用不活跃市场中的历史价格。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>除资产或负债报价以外其他可观测的输入信息，例如常用期限的可观测利率和收益率曲线、隐含波动率、信用利差（不含类型1中可直接或间接观测到的资产或负债的市场报价）。</td><td style='text-align: center;'>按市值计量。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>主要通过相关性或其他方式从可观测的市场数据获得的输入信息（不含类型1中可直接或间接观测到的资产或负债的市场报价）。</td><td style='text-align: center;'>按模型计量—输入信息主要从可观测的市场数据获得，也可使用不可观测的输入信息。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>资产或负债的不可观测的输入信息。当无法获得相关可观测的输入信息时，使用不可观测的输入信息计量公允价值，从而考虑资产或负债在计量日市场活动不活跃的情况。在此情形下，估值方可利用可得信息构建不可观测输入信息，其中可能包括估值方自身掌握的数据，并考虑市场参与者合理假设的所有可用信息。</td><td style='text-align: center;'>按模型计量—使用不可观测的输入信息。</td></tr><tr><td colspan="3">注：资产或负债的报价参见IFRS 13/ASC 820国际财务报告准则第13号—公允价值计量（IFRS13—Fair Value Measurement）。</td></tr></table>

### 5.6 与抵押品和保证金相关的数据要素

#### 5.6.1 抵押品基于投资组合的标识符（Collateral portfolio indicator）

抵押品基于投资组合的标识符数据格式见表32。

<div style="text-align: center;">表 32 抵押品基于投资组合的标识符数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>表示抵押品是否基于投资组合的标识符。抵押品基于投资组合指的是在投资组合下，1组保证金的交易集（以净额或总额为基础），非单笔交易。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Boolean</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>抵押品基于投资组合的标识符允许值为布尔字符，具体内容如下。a）“True”代表抵押品基于投资组合。b）“False”代表抵押品不基于投资组合。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>抵押品基于投资组合的代码。</td></tr></table>

#### 5.6.2 抵押品基于投资组合的代码（Collateral portfolio code）

抵押品基于投资组合的代码数据格式见表33。

<div style="text-align: center;">表 33 抵押品基于投资组合的代码数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>若抵押品是基于投资组合的，则本数据要素为交易报告方分配给投资组合的唯一代码。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Varchar(52)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>最多52个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>抵押品基于投资组合的标识符。</td></tr><tr><td colspan="2">注：本数据要素不适用于基于单笔交易层面计算保证金、无抵押品协议或无抵押品交收的情况。</td></tr></table>

#### 5.6.3 交易报告方交付的初始保证金（估值折扣前）（Initial margin posted by the reporting counterparty (pre-haircut)）

交易报告方交付的初始保证金（估值折扣前）数据格式见表34。

<div style="text-align: center;">表 34 交易报告方交付的初始保证金（估值折扣前）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方交付的初始保证金的数额，包括所有在划转中和待结算的保证金（除非管理要求不得包括此类保证金），具体内容如下。a）如果抵押品基于投资组合，则交付的初始保证金与整个组合相关联。b）如果抵押品基于单笔交易，则交付的初始保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr></table>

<div style="text-align: center;">表 34 交易报告方交付的初始保证金（估值折扣前）数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交付的初始保证金的货币、交易报告方交付的初始保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：1.本数据要素指初始保证金的总现值，不指每日变动保证金的总现值。2.本数据要素适用于非集中清算的交易以及集中清算的交易。对于集中清算的交易，本数据要素不包括交付的清算基金以及根据中央对手方流动性提供要求而交付的抵押品，即承诺的授信额度。3.若交付的初始保证金是以1种以上货币计价的，交易报告方选定1种货币，并将所有交付的初始保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.4 交易报告方交付的初始保证金（估值折扣后）（Initial margin posted by the reporting counterparty (post-haircut)）

交易报告方交付的初始保证金（估值折扣后）数据格式见表35。

<div style="text-align: center;">表 35 交易报告方交付的初始保证金（估值折扣后）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方交付的初始保证金的数额，是估值折扣后初始保证金的总现值，包括所有在划转中和待结算的保证金（除非管理要求不得包括此类保证金）、应用估值折扣后（若适用）的当前总价值，具体内容如下。a）如果抵押品基于投资组合，则交付的初始保证金与整个组合相关联。b）如果抵押品基于单笔交易，则交付的初始保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交付的初始保证金的货币、交易报告方交付的初始保证金（估值折扣前）。</td></tr><tr><td colspan="2">注：1.本数据要素适用于所有非集中清算。对于集中清算的交易，不包括交付的清算基金以及根据中央对手方流动性要求而交付的抵押品，即承诺的授信额度。2.若交付的初始保证金是以1种以上货币计价的，交易报告方选定1种货币，并将所有交付的初始保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.5 交付的初始保证金的货币（Currency of initial margin posted）

交付的初始保证金的货币数据格式见表36。

<div style="text-align: center;">表 36 交付的初始保证金的货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交付初始保证金的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (3)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr></table>

<div style="text-align: center;">表 36 交付的初始保证金的货币数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易报告方交付的初始保证金（估值折扣前）、交易报告方交付的初始保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：若交付的初始保证金是以1种以上货币计价的，交易报告方选定1种货币，并将所有交付的初始保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.6 交易报告方收取的初始保证金（估值折扣前）（Initial margin collected by the reporting counterparty (pre-haircut)）

交易报告方收取的初始保证金（估值折扣前）数据格式见表37。

<div style="text-align: center;">表 37 交易报告方收取的初始保证金（估值折扣前）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方收取的初始保证金的数额，包括所有在划转中和待结算的保证金（除非有管理要求不得包括此类保证金），具体内容如下。
a）如果抵押品是基于投资组合，则收取的初始保证金与整个组合相关联。
b）如果抵押品是基于单笔交易，则收取的初始保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>收取初始保证金的货币、交易报告方收取的初始保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：1.本数据要素指初始保证金的总现值，不指每日变动保证金的总现值。
2.本数据要素适用于非集中清算的以及集中清算的交易。对于集中清算的交易，本数据要素不包括中央对手方在其投资活动中收取的抵押品。
3.若收取的初始保证金是以1种以上货币计价的，交易报告方选定1种货币，并将所有收取的初始保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.7 交易报告方收取的初始保证金（估值折扣后）（Initial margin collected by the reporting counterparty（post-haircut））

交易报告方收取的初始保证金（估值折扣后）数据格式见表38。

<div style="text-align: center;">表 38 交易报告方收取的初始保证金（估值折扣后）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方收取的初始保证金的数额，包括所有在划转中和待结算的保证金（除非有管理要求不得包括此类保证金）、应用估值折扣后（若适用）的当前总价值，具体内容如下。a）如果抵押品是基于投资组合，则收取的初始保证金与整个组合相关联。b）如果抵押品是基于单笔交易，则收取的初始保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr></table>

<div style="text-align: center;">表 38 交易报告方收取的初始保证金（估值折扣后）数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>收取初始保证金的货币、交易报告方收取的初始保证金（估值折扣前）。</td></tr><tr><td colspan="2">注：1.本数据要素指估值折扣后初始保证金的总现值，不指每日变动保证金的总现值。2.本数据要素适用于非集中清算的交易以及集中清算的交易，对于集中清算的交易，不包括中央对手方在其投资活动中收取的抵押品。3.若收取的初始保证金是以1种以上货币计价的，交易报告方选定1种货币，并将所有收取的初始保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.8 收取初始保证金的货币（Currency of initial margin collected）

收取初始保证金的货币数据格式见表39。

<div style="text-align: center;">表 39 收取初始保证金的货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>收取初始保证金的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(3)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易报告方收取的初始保证金（估值折扣前）、交易报告方收取的初始保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：若收取的初始保证金以1种以上货币计价，交易报告方选定1种货币，并将所有收取的初始保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.9 交易报告方交付的变动保证金（估值折扣前）（Variation margin posted by the reporting counterparty (pre-haircut)）

交易报告方交付的变动保证金（估值折扣前）数据格式见表40。

<div style="text-align: center;">表 40 交易报告方交付的变动保证金（估值折扣前）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方交付的变动保证金的数额（包括以现金结算的保证金），包括所有在划转中和待结算的保证金（除非有管理要求不得包括此类保证金），具体内容如下。
a）如果抵押品是基于投资组合，则交付的变动保证金与整个组合相关联。
b）如果抵押品是基于单笔交易，则交付的变动保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr></table>

<div style="text-align: center;">表 40 交易报告方交付的变动保证金（估值折扣前）数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交付的变动保证金的货币、交易报告方交付的变动保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：1.本数据要素指折扣前变动保证金的总现值，自交付的投资组合或单笔交易变动保证金首次报告时开始累计。
2.本数据要素不包括可能有浮动的保证金。
3.若交付的变动保证金以1种以上货币计价，则交易报告方选定1种货币，并将所有交付的变动保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.10 交易报告方交付的变动保证金（估值折扣后）（Variation margin posted by the reporting counterparty(post-haircut)）

交易报告方交付的变动保证金（估值折扣后）数据格式见表41。

<div style="text-align: center;">表 41 交易报告方交付的变动保证金（估值折扣后）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方交付的变动保证金的数额（包括以现金结算的保证金），包括所有在划转中和待结算的保证金（除非有管理要求不得包括此类保证金）、应用估值折扣后（若适用）的当前总价值，具体内容如下。
a）如果抵押品是基于投资组合，则交付的变动保证金与整个组合相关联。
b）如果抵押品是基于单笔交易，则交付的变动保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交付的变动保证金的货币、交易报告方交付的变动保证金（估值折扣前）。</td></tr><tr><td colspan="2">注：1.本数据要素指折扣后变动保证金的总现值（若适用），自交付的组合或单笔交易变动保证金首次报告时开始累计。
2.本数据要素不包括可能有浮动的保证金。
3.若交付的变动保证金以1种以上货币计价，则由交易报告方选定其中1种货币，并将所有交付的变动保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.11 交付的变动保证金的货币（Currency of variation margin posted）

交付的变动保证金的货币数据格式见表42。

<div style="text-align: center;">表 42 交付的变动保证金的货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交付变动保证金的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (3)</td></tr></table>

<div style="text-align: center;">表 42 交付的变动保证金的货币数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易报告方交付的变动保证金（估值折扣前）、交易报告方交付的变动保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：若交付的变动保证金以1种以上货币计价，则由交易报告方选定其中1种货币，并将所有交付的变动保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.12 交易报告方收取的变动保证金（估值折扣前）（Variation margin collected by the reporting counterparty（pre-haircut））

交易报告方收取的变动保证金（估值折扣前）数据格式见表43。

<div style="text-align: center;">表 43 交易报告方收取的变动保证金（估值折扣前）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方收取的变动保证金的数额（包括以现金结算的保证金），包括所有在划转中和待结算的保证金（除非有管理要求不得包括此类保证金），具体内容如下。
a）如果抵押品是基于投资组合的，则收取的变动保证金与整个组合相关联。
b）如果抵押品是基于单笔交易的，则收取的变动保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要</td><td style='text-align: center;'>收取变动保证金的货币、交易报告方收取的变动保证金（估值折扣后）。</td></tr><tr><td colspan="2">注：1.本数据要素指估值折扣前变动保证金的总现值，自收取的组合或单笔交易变动保证金首次报告时开始累计。
2.本数据要素不包括可能有浮动的保证金。
3.若收取的变动保证金以1种以上货币计价，则由交易报告方选定其中1种货币，并将所收取的变动保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.13 交易报告方收取的变动保证金（估值折扣后）（Variation margin collected by the reporting counterparty(post-haircut)）

交易报告方收取的变动保证金（估值折扣后）数据格式见表44。

<div style="text-align: center;">表 44 交易报告方收取的变动保证金（估值折扣后）数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>由交易报告方收取的变动保证金的数额（包括以现金结算的保证金），包括所有在划转中和待结算的保证金（除非有管理要求不得包括此类保证金）、应用估值折扣后（若适用）的当前总价值，具体内容如下。
a）如果抵押品是基于投资组合的，则收取的变动保证金与整个组合相关联。
b）如果抵押品是基于单笔交易的，则收取的变动保证金与该笔交易相关联。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 20022-1</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr></table>

<div style="text-align: center;">表 44 交易报告方收取的变动保证金（估值折扣后）数据格式(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>收取变动保证金的货币、交易报告方收取的变动保证金（估值折扣前）。</td></tr><tr><td colspan="2">注：1. 本数据要素指估值折扣后变动保证金的总现值，自收取的组合或单笔交易变动保证金首次报告时开始累计。
2. 本数据要素不包括可能有浮动的保证金。
3. 若收取的变动保证金以1种以上货币计价，则由交易报告方选定其中1种货币，并将所有收取的变动保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.14 收取变动保证金的货币（Currency of variation margin collected）

收取变动保证金的货币数据格式见表45。

<div style="text-align: center;">表 45 收取变动保证金的货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>收取的变动保证金的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(3)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易报告方收取的变动保证金（估值折扣前）、交易报告方收取的变动保证金（估值折扣后）</td></tr><tr><td colspan="2">注：若收取的变动保证金以1种以上货币计价，则由交易报告方选定其中1种货币，并将所有收取的变动保证金换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.15 交易报告方交付的超额抵押品（Excess collateral posted by the reporting counterparty）

交易报告方交付的超额抵押品数据格式见表46。

<div style="text-align: center;">表 46 交易报告方交付的超额抵押品数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交易报告方交付的与初始保证金及变动保证金相分离和独立的额外抵押品的数额，即超额抵押品估值折扣前的总现值（若适用），而不是每日变化的数额。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交付超额抵押品的货币</td></tr><tr><td colspan="2">注：1.超额交付的初始保证金或变动保证金，在报告时视为交付的初始保证金或变动保证金的一部分，不包括在交付的超额抵押品。
2.对于集中清算的交易，仅在可以分配给特定投资组合或交易的范围内报告超额抵押品。</td></tr></table>

#### 5.6.16 交付超额抵押品的货币（Currency of excess collateral posted）

交付超额抵押品的货币数据格式见表47。

<div style="text-align: center;">表 47 交付超额抵押品的货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交付的超额抵押品的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(3)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易报告方交付的超额抵押品</td></tr><tr><td colspan="2">注: 若交付的超额抵押品以1种以上货币计价，则由交易报告方选定其中1种货币，并将所有交付超额抵押品的价值换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.17 交易报告方收取的超额抵押品（Excess collateral collected by the reporting counterparty）

交易报告方收取的超额抵押品数据格式见表48。

<div style="text-align: center;">表 48 交易报告方收取的超额抵押品数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>交易报告方收取的与初始保证金及变动保证金相分离和独立的额外抵押品的数额，即超额抵押品折扣前的总现值（若适用），而不是每日变化的数额。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Num(25,5)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>大于或等于0且最多25个数字，包括小数点后5位。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>收取超额抵押品的货币</td></tr><tr><td colspan="2">注：1. 超额收取的初始保证金或变动保证金，在报告时视为收取的初始保证金或变动保证金的一部分，不能包括在收取的超额抵押品中。2. 对于集中清算的交易，仅在可以分配给特定投资组合或交易范围内报告超额抵押品。</td></tr></table>

#### 5.6.18 收取超额抵押品的货币（Currency of excess collateral collected）

收取超额抵押品的货币数据格式见表49。

<div style="text-align: center;">表 49 收取超额抵押品的货币数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>收取的超额抵押品的计价货币。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>ISO 4217</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char (3)</td></tr></table>

<div style="text-align: center;">表 49 收取超额抵押品的货币数据格式（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>ISO 4217中包含的所有货币代码，3个字母或数字字符。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易报告方收取的超额抵押品。</td></tr><tr><td colspan="2">注: 若收取的超额抵押品以1种以上货币计价，则由交易报告方选定其中1种货币，并将所有收取的超额抵押品的价值换算成该种货币加总后进行报告。</td></tr></table>

#### 5.6.19 抵押类别（Collateralisation category）

抵押类别数据格式见表50。

<div style="text-align: center;">表 50 抵押类别数据格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>反映交易对手方之间是否有抵押品协议的标识符（包括无担保、部分担保或单向担保或完全担保）。</td></tr><tr><td style='text-align: center;'>可参考的国际标准</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>格式</td><td style='text-align: center;'>Char(4)</td></tr><tr><td style='text-align: center;'>允许值</td><td style='text-align: center;'>4个字母或数字字符，详见表51。</td></tr><tr><td style='text-align: center;'>相关数据要素及数据要素之间的依赖关系</td><td style='text-align: center;'>交易对手方1、交易对手方2。</td></tr><tr><td colspan="2">注：根据抵押品是基于单笔交易还是投资组合，本数据要素说明每个交易或组合的抵押类别，且适用于清算的和非清算的交易。</td></tr></table>

抵押类别允许值的名称和定义见表51。

<div style="text-align: center;">表 51 抵押类别允许值的名称和定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>值</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>定义</td></tr><tr><td style='text-align: center;'>UNCL</td><td style='text-align: center;'>无抵押</td><td style='text-align: center;'>交易双方之间没有抵押品协议或交易双方之间的抵押品协议规定场外衍生品交易无需交付抵押品（包括初始保证金及变动保证金）。</td></tr><tr><td style='text-align: center;'>PRC1</td><td style='text-align: center;'>部分抵押：仅交易对手方1</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，对于场外衍生品交易，交易对手方1（交易报告方）只定期交付变动保证金，交易对手方2不交付任何保证金。</td></tr><tr><td style='text-align: center;'>PRC2</td><td style='text-align: center;'>部分抵押：仅交易对手方2</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，对于场外衍生品交易，交易对手方1（交易报告方）不交付任何保证金，交易对手方2只定期交付变动保证金。</td></tr><tr><td style='text-align: center;'>PACL</td><td style='text-align: center;'>部分抵押</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，双方只定期交付变动保证金。</td></tr></table>

<div style="text-align: center;">表 51 抵押类别允许值的名称和定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>OWC1</td><td style='text-align: center;'>单向抵押：仅交易对手方1</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，交易对手方1（交易报告方）交付初始保证金、定期交付变动保证金，交易对手方2不交付任何保证金。</td></tr><tr><td style='text-align: center;'>OWC2</td><td style='text-align: center;'>单向抵押：仅交易对手方2</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，对于场外衍生品交易，交易对手方1（交易报告方）不交付任何保证金，交易对手方2交付初始保证金、定期交付变动保证金。</td></tr><tr><td style='text-align: center;'>OWP1</td><td style='text-align: center;'>单向/部分抵押：交易对手方1</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，交易对手方1（交易报告方）交付初始保证金、定期交付变动保证金，交易对手方2只定期交付变动保证金。</td></tr><tr><td style='text-align: center;'>OWP2</td><td style='text-align: center;'>单向/部分抵押：交易对手方2</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，交易对手方1（交易报告方）只定期交付变动保证金，交易对手方2交付初始保证金、定期交付变动保证金。</td></tr><tr><td style='text-align: center;'>FLCL</td><td style='text-align: center;'>完全抵押</td><td style='text-align: center;'>交易双方之间的抵押品协议规定，交易双方都对场外衍生品交易交付初始保证金、定期交付变动保证金。</td></tr></table>

注：本文件仅包含部分其他关键数据要素，与触发交易对手评级相关的数据要素、与价格相关的数据要素、与名义金额和数量相关的数据要素、与其他支付相关的数据要素、与一揽子和链接相关的数据要素、与自定义篮子相关的数据要素的定义、格式和允许值等内容详见全国金融标准化技术委员会官方网站（https://cfstc.pbc.gov.cn/）下载专区“金融市场交易报告其他关键数据要素”。

## 参 考 文 献

[1] GB/T 7408—2005 数据元和交换格式 信息交换 日期和时间表示法

[2] GB/T 12406—2022 表示货币的代码

[3] GB/T 23696—2017 证券及相关金融工具 交易所和市场识别码

[4] GB/T 42495.1—2023 金融服务 全球法人识别编码 第1部分：编码说明

[5] ISO 4914:2021 金融服务 唯一产品识别码（Financial services—Unique product identifier(UPI)）

[6] ISO 20022（所有部分） 金融服务 金融业通用报文方案（Financial services—Universal financial industry message scheme）

[7] ISO 23897:2020 金融服务 唯一交易识别码（Financial services—Unique transaction identifier(UTI)）

[8] 《全球统一的场外衍生品关键数据要素（UTI和UPI除外）》（CPMI-IOSCO Technical Guidance: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI))

[9] IFRS 13/ASC 820 国际财务报告准则第13号—公允价值计量（IFRS13—Fair Value Measurement）