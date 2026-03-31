

JR/T 0293—2023

# 期货公司监管数据采集规范 第 1 部分：基本信息和经纪业务

# Specification for supervision data acquisition of futures companies—Part 1: General information and brokerage

2023-07-28 发布

2023-07-28 实施

Powered by TCPDF (www.tcpdf.org)

## 目 次

前言..... III    
引言..... IV    
1 范围..... 1    
2 规范性引用文件..... 1    
3 术语和定义..... 1    
4 数据类型..... 1    
5 期货公司基本信息采集..... 1    
5.1 期货公司基础信息采集..... 2    
5.2 期货公司业务范围信息采集..... 3    
5.3 期货公司股东基本信息采集..... 3    
5.4 分支机构信息采集..... 4    
5.5 董事、监事、高级管理人员信息采集..... 4    
6 期货公司风险监管报表数据采集..... 5    
6.1 期货公司风险监管指标汇总表..... 5    
6.2 最低限额结算准备金计算表..... 5    
6.3 期货公司净资本计算表..... 6    
6.4 期货公司风险资本准备计算表..... 8    
6.5 分离资产报表..... 9    
6.6 客户权益变动表..... 11    
7 期货公司财务监管报表主表数据采集..... 12    
7.1 资产负债表..... 12    
7.2 利润表..... 15    
7.3 所有者权益变动表..... 16    
7.4 境内分支机构报表..... 18    
7.5 介绍业务经营情况表..... 19    
7.6 现金流量表..... 20    
8 期货公司财务监管报表附表数据采集..... 22    
8.1 货币资金..... 22    
8.2 自有资金银行存款..... 22    
8.3 存出保证金..... 23    
8.4 交易性金融资产..... 23    
8.5 应收风险损失款..... 23    
8.6 其他应收款..... 23    
8.7 长期股权投资..... 24    
8.8 固定资产..... 24    
8.9 资产及信用减值准备..... 24    
8.10 所有权受限的资产..... 25    
8.11 其他资产..... 25    
8.12 交易性金融负债..... 25    
8.13 其他应付款..... 25    
8.14 预计负债..... 26    
8.15 其他负债..... 26

8.16 次级债.....26    
8.17 手续费及佣金净收入.....27    
8.18 公允价值变动收益.....27    
8.19 业务及管理费.....28    
8.20 资产及信用减值损失.....28    
8.21 营业外事项.....29    
8.22 或有事项.....29    
8.23 资产负债表日后事项.....29    
8.24 关联方关系及交易.....29    
8.25 应收关联方款项.....30    
8.26 应付关联方款项.....30    
8.27 所有者权益附注.....31    
8.28 应付职工薪酬.....31    
8.29 其他附注.....32    
参考文献.....33

## 前言

本文件按照GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

本文件是JR/T 0293《期货公司监管数据采集规范》的第1部分。JR/T 0293已经发布了以下部分：

——第1部分：基本信息和经纪业务。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国金融标准化技术委员会证券分技术委员会（SAC/TC 180/SC4）提出。

本文件由全国金融标准化技术委员会（SAC/TC 180）归口。

本文件起草单位：中国证券监督管理委员会科技监管局、中国证券监督管理委员会期货监管部、中国期货市场监控中心有限责任公司、中证信息技术服务有限责任公司、中国证券监督管理委员会北京监管局、中国证券监督管理委员会上海监管局、中国证券监督管理委员会江苏监管局、中国证券监督管理委员会浙江监管局、中国证券监督管理委员会山东监管局、中国证券监督管理委员会广东监管局、中国证券监督管理委员会陕西监管局、中国证券监督管理委员会深圳监管局、中国期货业协会、中信期货有限公司、永安期货股份有限公司、南华期货股份有限公司、银河期货有限公司、光大期货有限公司、平安期货有限公司、海通期货股份有限公司、一德期货有限公司。

本文件主要起草人：姚前、蒋东兴、陈炜、杨晓东、李志成、侯智杰、余薇、李宁宁、黄璐、杜琳钰、郭宇星、高玉光、高姗、卫雅茜、路一、刘彬、侯雪峰、赵欣、王琦、张艳影、唐丹彤、计玮、刘璐璐、王凌、许凯文、肖皓月、李建萍、王小梦、唐丹凤、李艳婷、王晓冰、周丽、郑涵秋、潘丹霞。

## 引言

随着期货市场业务快速发展，监管部门对期货公司的数据采集需求不断增加，为规范、统一以期货公司为主体的监管数据的业务定义、采集和应用口径，提升期货公司监管数据采集和应用的标准化程度，提高监管数据采集的时效性和准确性，特制订本文件。本文件以行业法律法规、业务规则、制度及流程等为依据，按照JR/T0176.1-2019中规定的行业数据模型方法论，结合期货公司监管综合信息系统采集数据的实践经验，总结数据特征与数据共性，形成具有通用性和可扩展性的期货公司监管数据采集行业标准。

《期货公司监管数据采集规范》金融行业标准分为2部分内容：

——第 1 部分：基本信息和经纪业务。分别围绕期货公司基本信息、风险监管指标、财务监管报表

主表和附表的数据采集情况，形成行业可参考的数据要素业务定义规范；

——第2部分：资产管理业务。拟对监管部门集中关注的与期货公司资产管理业务相关的监管数据要素，通过规范数据要素的业务定义，形成具有通用性和可扩展性的期货公司监管数据采集行业标准。

## 期货公司监管数据采集规范 第 1 部分：基本信息和经纪业务

## 1 范围

本文件规定了期货公司基本信息、经纪业务相关的监管数据采集范围和数据要素业务口径。

本文件适用于以期货公司为主体的监管数据采集和应用。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2659—2000 世界各国和地区名称代码

GB/T 4658—2006 学历代码

GB/T 4754—2017 国民经济行业分类

GB/T 6864—2003 中华人民共和国学位代码

GB/T 12402—2000 经济类型分类与代码

GB/T 12406—2008 表示货币和资金的代码

GB 32100—2015 法人和其他组织统一社会信用代码

## 3 术语和定义

GB/T 7408—2005界定的以及下列术语和定义适用于本文件。

### 3.1 

期货公司风险监管报表 risk-based regulation statements

期货公司编制的反映各项风险监管指标计算过程及计算结果的报表。

### 3.2 

日历日期 calendar date

由日历年、日历月以及其在日历月中的顺序数表示的特定日历日的标识。

[来源：GB/T 7408—2005，3.3]

## 4 数据类型

期货公司监管数据的数据类型包括字符型、数值型、日期型、枚举型、布尔型：

a）字符型是指由中文和英文的文字、数字、符号组合形式体现的数据项；

b) 数值型是指以整数或、小数形式体现的形式体现的数据项，适用于各类以数量反映的信息，可参与计算；

c） 日期型是指以日历日期形式体现的数据项，格式：YYYYMMDD；

d）枚举型是指由两个或两个以上的枚举值组成的数据项；

e）布尔型是技术角度常用的数据类型，通常用来判断条件是否成立。布尔型数据只有两个值，false（0）和true（1）。

## 5 期货公司基本信息采集

### 5.1 期货公司基础信息采集

期货公司基础信息采集的数据应符合表1的要求。对于数据字段有多个值时，如无特殊说明，多个值用顿号分隔。

<div style="text-align: center;">表 1 期货公司基础信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>期货公司名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“名称”保持一致。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>期货公司简称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>期货公司英文名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>公司类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：有限责任公司/股份有限公司。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>成立日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>与营业执照“成立日期”保持一致。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>注册资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>与营业执照“注册资本”数额保持一致，单位：元，保留两位小数。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>法定代表人姓名</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“法定代表人”保持一致。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>住所地址</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“住所”保持一致。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“统一社会信用代码”保持一致，按照GB 32100-2015 4.2代码及说明描述的。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>住所地所属监管辖区</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：北京证监局/天津证监局/河北证监局/山西证监局/内蒙古证监局/辽宁证监局/吉林证监局/黑龙江证监局/上海证监局/江苏证监局/浙江证监局/安徽证监局/福建证监局/江西证监局/山东证监局/河南证监局/湖北证监局/湖南证监局/广东证监局/广西证监局/海南证监局/重庆证监局/四川证监局/贵州证监局/云南证监局/西藏证监局/陕西证监局/甘肃证监局/青海证监局/宁夏证监局/新疆证监局/深圳证监局/大连证监局/宁波证监局/厦门证监局/青岛证监局。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>SHFE会员代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>CZCE会员代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>DCE会员代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>CFFEX会员类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：交易结算会员/全面结算会员/交易会员/无。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>CFFEX会员代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>如期货公司不是会员，可不填列。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>INE会员代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>如期货公司不是会员，可不填列。</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>GFEX会员代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>如期货公司不是会员，可不填列。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>SSE交易参与人代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>如期货公司不是交易参与人，可不填列。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>SZSE交易参与人代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>如期货公司不是交易参与人，可不填列。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>经营证券期货业务许可证流水号</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与经营证券期货业务许可证“流水号”保持一致。</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>外商投资期货公司标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>是指单一或有关联关系的多个境外股东直接持有或间接控制公司5%以上股权的期货公司。</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>委托证券公司开展介绍业务标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>是指证券公司接受期货公司委托，为期货公司介绍客户参与期货交易并提供其他相关服务的业务活动。</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>控股参股其他公司标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>是指期货公司是否控股或参股其他公司。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>获准开展境外代理业务标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>营业期限自</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>与营业执照“营业期限自”保持一致。</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>营业期限至</td><td style='text-align: center;'>字符或日期</td><td style='text-align: center;'>与营业执照“营业期限至”保持一致，填列字符或日期。</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>工商登记状态</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“登记状态”保持一致。</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>实际控制人名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>控股类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：中央国有控股/地方国有控股/社团集体控股/自然人控股/外商控股/控股主体性质不明确/无控股主体/其他。控股类型根据实际控制人的性质进行分类，没有实际控制人的，根据控股股东的性质进行分类。</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>上市或挂牌场所</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：上海证券交易所/深圳证券交易所/北京证券交易所/全国中小企业股份转让系统/香港交易所/区域股权市场/其他/无。</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>办公地址</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>客户服务及投诉电话</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>公司网址</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>电子邮箱</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr></table>

<div style="text-align: center;">表1 期货公司基础信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>员工数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指与期货公司存在劳动关系的劳动者数量，包含未取得从业资格的公司员工，可按照月末值采集，单位：人。</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>从业人员数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指通过从业资格考试并取得从业资格的员工数量，可按照月末值采集，单位：人。</td></tr><tr><td colspan="4">注：SHFE（上海期货交易所）、CZCE（郑州商品交易所）、DCE（大连商品交易所）、CFFEX（中国金融期货交易所）、INE（上海国际能源交易中心）、GFEX（广州期货交易所）、SSE（上海证券交易所）、SZSE（深圳证券交易所）</td></tr></table>

### 5.2 期货公司业务范围信息采集

期货公司业务范围信息采集的数据应符合表2的要求。对于数据字段有多个值时，如无特殊说明，多个值用顿号分隔。

<div style="text-align: center;">表 2 期货公司业务范围信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>业务种类</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：商品期货经纪/金融期货经纪/境外期货经纪/期货交易咨询/期货做市交易/资产管理/基金销售/股票期权经纪/与股票期权备兑开仓以及行权相关的证券现货经纪/其他。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>核准或登记备案单位</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>核准或登记备案文号</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>核准或登记备案日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>展业日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>是指期货公司首次开展上述业务种类的日期。</td></tr><tr><td colspan="4">注：该表内数据是指以期货公司为主体的业务范围，不包括期货公司的各类子公司的业务范围。</td></tr></table>

### 5.3 期货公司股东基本信息采集

期货公司股东基本信息采集的数据应符合表3的要求。期货公司为公众公司的，依据《期货公司监督管理办法》采集持股5%及以上的股东基本信息。对于数据字段有多个值时，如无特殊说明，多个值用顿号分隔。

<div style="text-align: center;">表 3 期货公司股东基本信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>股东名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>股东类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：法人股东/非法人组织股东/自然人股东。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>国籍或注册地</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用GB/T 2659—2000表1中界定的中文简称。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：统一社会信用代码/身份证/护照/公司注册证书编号/纳税证明号/其他。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>股权变更登记日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>是指期货公司的股东首次出资或持股，以及股东出资或持股发生变化时，在公司登记机关办理变更登记的日期。依法不需要办理公司变更登记的，为相关确权登记的日期。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>持股比例</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：%，保留两位小数。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>主要股东标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>是指持有期货公司5%以上股权的法人、非法人组织或者自然人。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>控股股东标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>第一大股东标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>上市公司标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>是指股东是否为上市公司。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>金融机构标志</td><td style='text-align: center;'>布尔</td><td style='text-align: center;'>是指股东是否为金融机构。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>股东自身控股类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：中央国有控股/地方国有控股/社团集体控股/自然人控股/外商控股/控股主体性质不明确/无控股主体/其他。控股类型根据实际控制人的性质进行分类，没有实际控制人的，根据控股股东的性质进行分类。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>股东注册资本币种</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用GB/T 12406—2008表A.1中界定的货币名称。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>股东注册资本金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：元，保留两位小数。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>股东法定代表人姓名</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr></table>

<div style="text-align: center;">表3 期货公司股东基本信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>股东所属行业</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用 GB/T 4754—2017 表 1 中界定的类别名称。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>股东所属经济类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用 GB/T 12402—2000 经济类型分类与代码表中界定的经济类型名称。</td></tr></table>

### 5.4 分支机构信息采集

分支机构信息采集的数据应符合表4的要求。对于数据字段有多个值时，如无特殊说明，多个值用顿号分隔。

<div style="text-align: center;">表 4 分支机构信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：营业部/分公司/总部/其他。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>分支机构名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“名称”保持一致。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“统一社会信用代码”保持一致，按照GB 32100—2015 4.2代码及说明描述的。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>住所地所属监管辖区</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：北京证监局/天津证监局/河北证监局/山西证监局/内蒙古证监局/辽宁证监局/吉林证监局/黑龙江证监局/上海证监局/江苏证监局/浙江证监局/安徽证监局/福建证监局/江西证监局/山东证监局/河南证监局/湖北证监局/湖南证监局/广东证监局/广西证监局/海南证监局/重庆证监局/四川证监局/贵州证监局/云南证监局/西藏证监局/陕西证监局/甘肃证监局/青海证监局/宁夏证监局/新疆证监局/深圳证监局/大连证监局/宁波证监局/厦门证监局/青岛证监局。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>住所地址</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与营业执照“住所”保持一致。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>成立日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>停业日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>以营业执照注销日期为准。当期货公司分支机构为正常营业状态时，此字段为空。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>业务及客服电话</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>负责人姓名</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>负责人联系电话</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>业务种类</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：商品期货经纪/金融期货经纪/境外期货经纪/期货交易咨询/基金销售/其他。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>展业日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>是指该分支机构首次开展上述业务种类的日期。</td></tr></table>

### 5.5 董事、监事、高级管理人员信息采集

董事、监事、高级管理人员信息采集表包括改人员的全部历史任职和离职信息，所采集的数据应符合表5的要求。对于数据字段有多个值时，如无特殊说明，多个值用顿号分隔。

<div style="text-align: center;">表 5 董事、监事、高级管理人员信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>所任职务</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：董事长/董事/独立董事/监事会主席/监事/总经理/副总经理/首席风险官/财务负责人/其他。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>董监高姓名</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：身份证/护照/其他。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>证件号码</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>任职日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>离职日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>期货公司董事、监事、高级管理人员任职状态下不填列该字段。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>国籍</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用GB/T 2659—2000表1中界定的中文简称。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>学历</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用GB/T 4658—2006表1中界定的学历。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>学位</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值使用GB/T 6864—2003表1中界定的学位。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>联系电话</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr></table>

## 6 期货公司风险监管报表数据采集

### 6.1 期货公司风险监管指标汇总表

期货公司风险监管指标汇总表采集的数据应符合表6的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 6 期货公司风险监管指标汇总表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>净资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是在净资产基础上，按照变现能力对资产负债项目及其他项目进行风险调整后得出的综合性风险监管指标。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>风险资本准备总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司在开展各项业务过程中，为应对可能发生的风险损失所需要的资本。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>净资本与风险资本准备总额的比例</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：%，保留两位小数。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>净资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>净资本与净资产的比例</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：%，保留两位小数。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>扣除客户保证金的流动资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包含货币资金（不含期货保证金存款）、存出保证金、交易性金融资产、应收结算担保金、应收风险损失款、应收手续费及佣金、应收股利、应收利息、其他应收款、结算备付金、买入返售金融资产、持有待售资产。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>扣除客户权益的流动负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包含短期借款、交易性金融负债、期货风险准备金、应付期货投资者保障基金、应付职工薪酬、应交税费、应付利息、应付股利、其他应付款、应付手续费及佣金、持有待售负债、其他负债。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>流动资产与流动负债的比例</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>为扣除客户保证金的流动资产与扣除客户权益的流动负债的比例。单位：%，保留两位小数。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>负债（扣除客户权益）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>为扣除公司应付货币保证金与应付质押保证金、代理买卖证券款后的负债。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>负债与净资产的比例</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：%，保留两位小数。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>结算准备金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>结算准备金是指结算会员在交易所专用结算账户中预先准备的资金，是未被占用的自有资金。</td></tr></table>

### 6.2 最低限额结算准备金计算表

最低限额结算准备金计算表采集的数据应符合表7的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 7 最低限额结算准备金计算表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>拥有结算会员资格的结算机构家数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司拥有结算会员资格的结算机构的家数，单位：家。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>拥有结算会员资格最低结算准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指拥有结算机构结算会员资格的期货公司按要求需缴纳的最低结算准备金额。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>拥有结算会员资格的结算机构名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>是指期货公司拥有结算会员资格的结算机构的名称，按照全称填列，多家结算机构用“，”分隔。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>代为本公司结算的结算机构家数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司拥有会员资格但不能直接参与结算的结算机构的家数，单位：家。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>代为本公司结算最低结算准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指拥有结算机构会员资格但不能直接参与结算的期货公司，按要求需缴纳的最低结算准备金额。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>代为本公司结算的结算机构名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>是指期货公司拥有会员资格但不能直接参与结算的结算机构的名称，按照全称填列，多家结算机构用“，”分隔。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>接受境外经纪机构委托交易结算的结算机构家数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司接受境外经纪机构的委托进行交易结算的结算机构的家数，单位：家。</td></tr></table>

<div style="text-align: center;">表 7 最低限额结算准备金计算表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>接受境外经纪机构委托交易结算最低结算准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司接受境外经纪机构的委托进行交易结算需缴纳的最低结算准备金额。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>接受境外经纪机构委托交易结算的结算机构名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>是指期货公司接受境外经纪机构的委托进行交易结算的结算机构的名称，按照全称填列，多家结算机构用“，”分隔。</td></tr></table>

### 6.3 期货公司净资本计算表

期货公司净资本计算表采集的数据应符合表8的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 8 公司净资本计算表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>净资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>金融资产调整合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指金融资产按照资产属性不同进行调整后的合计值。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>股票</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>上证180、深证100、沪深300成分股</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指构成上证180、深证100、沪深300指数的样本股票，具体样本股票以沪深交易所公布为准。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>沪深交易所一般上市股票</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是在沪深交易所上市的，除了上证180、深证100、沪深300成分股之外的一般股票。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>全国股份转让系统挂牌的做市转让股票</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指在全国股份转让系统挂牌的做市转让股票。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>流通受限的股票</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>流通受限情形包括新股发行但暂未上市流通、股票处于禁售期或被锁定、股票停牌且剩余停牌期超过1个月、股票在股转系统协议转让及其他限制股票流动性的情形。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>持有股票市值超过股票总市值5%的部分</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司持有的单一股票市值超过该股票总市值5%的，列示超额5%的部分。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>其他股票</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>固定收益证券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>国债、中央银行票据、国开债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>中央银行票据是指人民银行为调节商业银行超额准备金而向银行发行的短期债务凭证；国开债是指国家开发银行在全国银行间市场、沪深证券交易所市场、商业银行柜台市场等公开交易所发行的、按约定还本付息的金融债券。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>政策性银行金融债、政府支持机构债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>政策性银行金融债指政策性银行发行的金融债券。政府支持机构债券指由中央政府支持的公司或金融机构发行并由中央政府提供担保的债券。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>地方政府债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指地方政府作为发行主体发行的债券。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>信用评级AAA级的信用债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指在沪深交易所或银行间市场公开交易的公司信用债、资产支持证券、可转换债券、可交换债券等。信用评级以长期信用评级为基准，短期信用评级A-1归入AAA级信用债券。债券信用评级信息以中央结算公司公布的信息为准。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>信用评级AAA级以下、AA级（含）以上的信用债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>短期信用评级A-2归入AAA级以下、AA级（含）以上的信用债券。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>信用评级AA级以下、BBB级（含）以上的信用债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>短期信用评级A-3归入AA级以下、BBB级（含）以上的信用债券。</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>信用评级BBB以下的信用债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>短期信用评级B级（含）以下归入信用评级BBB级以下的信用债券，未评级的信用债券参照债券发行主体评级，发行主体无评级的归入BBB级以下信用债券。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>出现违约风险的信用债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>流通受限的信用债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指信用债券因发行人、交易场所等原因导致不能公开交易或转让的债券。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>公开募集证券投资基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

<div style="text-align: center;">表8 期货公司净资本计算表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>货币基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指仅投资于货币市场工具，每个交易日可办理基金份额申购、赎回的基金。</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>债券基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>股票基金、混合基金、权益类ETF及分级基金中优先级基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>股票基金是指80%以上基金资产投资于股票的基金；混合基金为投资于股票、债券、货币市场工具或其他基金份额，并且各项投资份额均不超过80%的；权益类ETF是指股票指数基金；分级基金中优先级基金是指结构型基金中享有优先分配权的基金。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>商品基金（包括黄金ETF）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>分级基金中的非优先级基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>处于封闭期或暂停赎回的开放式基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>其他公募基金（在附注中说明）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>单一、集合及信托等资产管理产品</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>资产管理产品包括证券公司、期货公司、基金公司及其子公司发行的资产管理计划，信托产品，商业银行理财产品等。</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>剩余存续期在7天以内（含）的封闭型集合产品或距离最近一次产品开放日7天以内（含）的定期开放型集合产品</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>剩余存续期在7天以上30天以内（含）的封闭型集合产品或距离最近一次产品开放日7天以上30天以内（含）的定期开放型集合产品</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>剩余存续期在30天以上的封闭型集合产品或距离最近一次产品开放日30天以上的定期开放型集合产品</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>集合产品的劣后级份额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>劣后级份额的认定标准为，该类份额的风险收益水平高于产品整体风险收益水平，或在合同中约定承担超过所持份额比例的亏损并获得相应比例的收益。</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>单一产品</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>其他金融资产投资（在附注中说明）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>不能明确归类为以上金融资产明细项目的，按照审慎监管原则，暂按100%比例进行调整，且需在附注中说明投资项目的具体内容。</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>长期股权投资调整合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指在净资本中需进行调整的长期股权投资。</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>应收款项调整合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指与期货经纪业务无关的，一般计入其他应收款科目进行会计核算的各类应收款与预付款。</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>应收非关联方款项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>除应收关联方款项之外的其他各项应收款之和。</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>账龄一年以内（含一年）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指账龄一年以内（含一年）的应收非关联方款项。</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>账龄一年以上</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指账龄一年以上的应收非关联方款项。</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>应收关联方款项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>与期货公司有关联交易的各项应收款项之和，其中关联方包含但不限于母公司、子公司及同受母公司控制的其他公司。</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>其他资产调整合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指除以上各类资产以外的其他资产按照一定比例进行调整后的合计值。</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>货币资金、应收货币保证金、应收质押担保金、应收结算担保金、结算备付金合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指货币资金、应收货币保证金、应收质押担保金、应收结算担保金、结算备付金的金额合计值。</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>沪深交易所或银行间市场债券逆回购</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>存出保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司因履约或办理业务需要存出或缴纳的除期货、期权保证金以外的保证金款项。</td></tr></table>

<div style="text-align: center;">表8 期货公司净资本计算表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>应收利息、股利、佣金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包括未在表格中提及的其他类资产，包括但不限于应收风险损失款、期货会员资格投资、投资性房地产、固定资产、无形资产、商誉、递延所得税资产及其他资产。不包含所有权资产。</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>负债调整合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指在净资本中调增的负债项，包括次级债务和期货风险准备金。</td></tr><tr><td style='text-align: center;'>48</td><td style='text-align: center;'>次级债务</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司借入次级债务、向股东或者其关联企业借入具有次级债务性质的长期借款以及其他清偿顺序在普通债之后的债务。</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>剩余到期期限1年至2年（含2年）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指剩余到期期限1-2年（含2年）的长期次级债务。</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>剩余到期期限2年至3年（含3年）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指剩余到期期限2-3年（含3年）的长期次级债务。</td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>剩余到期期限3年至5年（含5年）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指剩余到期期限3-5年（含5年）的长期次级债务。</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>剩余到期期限5年以上</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指剩余到期期限在5年以上的长期次级债务。</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>次级债务（不含次级债务净资本30%）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映次级债务计入的净资本数额的上限，不应超过净资本（不含次级债务累计计入净资本的数额）的30%。</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>期货风险准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司按规定提取的期货风险准备金。</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>经中国证监会认可的其他可调增项目</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>其他调减项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>或有负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司存在可能导致经济利益流出的或有事项，不包括期货公司按照企业会计准则的规定已确认的预计负债。</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>所有权受限等无法变现的资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>所有权受限无法变现的资产，如资产被冻结、资产用于抵债等。</td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>客户和代理非结算会员未足额追加的保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指按交易所规定的保证金标准计算的客户未足额追加的保证金和分级结算制度下代理的其他非结算会员未足额追加的保证金，不包括客户因穿仓损失形成的已经计入“应收风险损失款”科目的对期货公司的债务，也不包括因客户穿仓等原因导致代理的非结算会员在期货公司权益为负时已经计入“其他应收款”的期货公司的垫付款项。</td></tr><tr><td style='text-align: center;'>60</td><td style='text-align: center;'>其他调减项目（在附注中说明）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>净资本金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是在净资产基础上，按照变现能力对资产负债项目及其他项目进行风险调整后得出的综合性风险监管指标。</td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>[附注1]：其他股票</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>[附注1]：其他公募基金</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>[附注1]：其他金融资产投资</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>65</td><td style='text-align: center;'>[附注1]：其他调减项目</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>66</td><td style='text-align: center;'>[附注2]：其他需要说明的内容</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr></table>

### 6.4 期货公司风险资本准备计算表

期货公司风险资本准备计算表的数据应符合表9的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 9 期货公司风险资本准备计算表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>期货期权经纪业务风险资本准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司从事期货期权经纪业务的，应按客户权益总额的一定比例计算风险资本准备。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>期货期权经纪业务客户保证金总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>为资产负债表中应付货币保证金、应付质押保证金之和。</td></tr></table>

<div style="text-align: center;">表 9 期货公司风险资本准备计算表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>资产管理业务风险资本准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包括资产管理业务收入、单一资产管理业务规模、非结构化集合资产管理业务规模、结构化集合资产管理业务规模之和计算的风险资本准备。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>资产管理业务收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司及子公司向客户收取的管理费及提取的业绩报酬。开展业务不足1年的，以业务开展日截至报告期累计收入为基础计算；满1年但未跨越1个完整自然年度的，以上一自然年度收入的年化值计算；跨越1-3个完整自然年度的，以业务开展以来跨越完整自然年度的年收入的平均值计算；跨越3个以上完整自然年度的，以业务开展以来近三个自然年度的年收入的平均值计算。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>单一资产管理业务规模</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司及子公司为单一客户设立的资产管理产品规模，按照单个产品的受托资金余额与净值孰高计算。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>非结构化集合资产管理业务规模</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>结构化集合资产管理业务规模</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>其他风险资本准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>资产管理子公司净资本可抵扣部分</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>资产管理子公司净资本可抵扣期货公司风险资本准备，但抵扣金额不应超过以子公司资产管理业务数据为基础计算的风险资本准备。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>公司风险资本准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司在开展各项业务过程中，为应对可能发生的风险损失所需要的资本。</td></tr></table>

### 6.5 分离资产报表

分离资产报表的数据应符合表10的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 10 分离资产报表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>客户权益总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应与资产负债表中应付货币保证金、应付质押保证金之和相等。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>分离资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映客户分离资产的分布情况，包括“在本公司保证金专用银行账户余额”、“在结算机构的账户余额”和“分离资产账户中的公司自有资金”。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>在本公司保证金专用银行账户余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金以及期货公司存入期货保证金账户的款项。包括“货币保证金”、“质押保证金”。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>货币保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金以及期货公司存入期货保证金账户的款项。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>质押保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司代客户或分级结算制度下全面结算会员代非结算会员办理以有价证券冲抵保证金业务形成的可用于期货交易的保证金。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>在结算机构的账户余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>分别按“货币保证金”、“质押保证金”分行次据实填列。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>货币保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货交易所或登记结算机构收到客户以及期货公司存入交易所或登记结算机构专用结算账户的货币保证金。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>质押保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司代客户或分级结算制度下，全面结算会员代非结算会员办理以有价证券冲抵保证金业务形成的可用于期货交易的保证金。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>分离资产账户中的公司自有资金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映客户分离资产账户中的公司自有资金余额及其本期增减变动情况。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>期初余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>为上期分离资产账户中的自有资金期末余额与以自有资金代垫客户和代理非结算会员未足额追加的保证金之和。</td></tr></table>

<div style="text-align: center;">表10 分离资产报表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>本期增加</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映客户分离资产账户中公司自有资金的增加构成，包括“手续费净收入”、“交易所手续费返还及减收”、“利息收入”、“自有资金调入”、“代收增值税—手续费收入”、“代收增值税—交易所手续费返还及减收”、“其他调增项目”。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>手续费及佣金净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司收取的手续费及佣金扣除代交易所收取的手续费后的净额（不含税）。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>交易所手续费返还及减收净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映交易所对期货公司返还的手续费或交易所直接减收期货公司的手续费减去相应支出后的净额（不含税）。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>利息净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映结算银行向期货公司支付的期货保证金存款利息以及结算机构向期货公司支付的存款利息等。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>自有资金调入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司从自有资金账户划入保证金专用银行账户或结算机构账户的金额。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>代收增值税—手续费及佣金收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司代收的手续费及佣金收入增值税。</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>代收增值税—交易所手续费返还及减收</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司代收的交易所手续费返还及减收增值税。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>其他调增项目</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映未在上述项目中反映的需要调增分离资产账户中公司自有资金余额的其他业务。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>本期减少</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包括“年会费/席位费”、“银行手续费等各类杂费”、“自有资金调出”、“以风险准备金弥补错单损失”、“以自有资金弥补客户穿仓损失”、“以自有资金代垫客户和代理非结算会员未足额追加的保证金”、“投资者保障基金”、“其他调减项目。”</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>年会费/席位费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>交易所从结算机构账户里扣取的年会费和席位使用费。</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>银行手续费等各类杂费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司通过期货结算银行划转保证金时形成的费用或向银行函证费用等相关费用。</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>自有资金调出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司从保证金专用银行账户或结算机构账户划出至自有资金账户的金额。</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>以风险准备金弥补错单损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司出现错单造成损失时，动用风险准备金弥补的金额。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>以自有资金弥补客户穿仓损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司出现客户穿仓而不能追回时，以自有资金弥补的金额，包括在本公司开户的客户、代理非结算会员（期货公司）客户和代理非结算会员（非期货公司）客户。</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>以自有资金代垫客户和代理非结算会员未足额追加的保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司以自有资金垫付的按交易所保证金比例计算的客户未足额追加的保证金和分级结算制度下代理的非结算会员未足额追加的保证金。不包括客户因穿仓损失形成的已经记入“应收风险损失款”科目的对期货公司的债务，以及因客户穿仓等原因导致代理的非结算会员在期货公司权益为负时已经记入“其他应收款”的期货公司的垫付款项。一般情况下，金额应与本表“客户和代理非结算会员未足额追加的保证金”项目金额相等。</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>投资者保障基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司严重违法违规或者风险控制不力等导致保证金出现缺口，可能严重危及社会稳定和期货市场安全时，补偿投资者保证金损失的专项基金。期货公司从其收取的交易手续费中按照代理交易额的一定比例缴纳。</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>其他调减项目</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映未在上述项目中反映的需要调减分离资产账户中公司自有资金余额的其他业务。</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>客户和代理非结算会员未足额追加的保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映按交易所保证金比例计算的客户未足额追加的保证金和分级结算制度下代理的其他非结算会员未足额追加的保证金。不包括客户因穿仓损失形成的已经记入“应收风险损失款”科目的对期货公司的债务，也不包括因客户穿仓等原因导致代理的非结算会员在期货公司权益为负时已经记入“其他应收款”的期货公司的垫付款项。</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>各结算机构要求的最低结算准备金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司按照交易所要求缴纳的最低结算准备金金额。</td></tr></table>

<div style="text-align: center;">表10 分离资产报表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>未达账项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映因保证金划转与期货公司结算系统确认客户权益在时间上的差异导致应当相等的有关项目出现差额的未达账项。</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>权益已减，资产未减</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>权益已增，资产未增</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>资产已减，权益未减</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>资产已增，权益未增</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>分离资产与权益差额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映保证金封闭管理的情况。通常情况下，客户分离资产应等于客户权益，若两者存在差额则表明期货公司可能挪用了客户保证金，或存在以下情况：1、期货公司未按本表填列要求对客户分离资产账户的余额进行调整；2、客户和代理非结算会员未足额追加保证金时，期货公司未及时以自有资金垫付，或客户发生穿仓损失时，期货公司未能及时用自有资金补足；3、其他人为原因造成的错误。</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>其他调增项目</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>分离资产账户中公司自有资金增加的其他调增项目的具体说明。</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>其他调减项目</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>分离资产账户中公司自有资金减少的其他调减项目的具体说明。</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>未达账项</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>详细说明未达账项的情况，包括客户或代理的非结算会员名称、金额、形成原因等信息。</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>错单次数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司在报告期内发生的错单次数，单位：次。</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>错单亏损金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司在报告期内发生的因错单导致的亏损金额，期货公司如盈利应填报负数。</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>诉讼次数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司在报告期内发生的诉讼次数（包含未决诉讼）。同一案件发生两次审理的情况按照一次诉讼次数进行统计，单位：次。</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>诉讼金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司在报告期内发生诉讼涉及的相关诉讼金额。</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>裁决结果</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司在报告期内的诉讼结果，按照胜诉次数和败诉次数分别披露（不包含撤诉、调解），单位：次。</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>通知追保次数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映在报告期内交易所基于每日无负债结算对期货公司下发追加保证金通知的次数，单位：次。</td></tr></table>

### 6.6 客户权益变动表

客户权益变动表的数据应符合表11的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 11 客户权益变动表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>客户货币保证金期初余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金本期期初余额。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>保证金入金（或存入结算资金）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司客户本期存入的货币形态的保证金（或分级结算制度下全面结算会员收到非结算会员存入的货币形态的结算资金）。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>处置充抵保证金的有价证券增加的货币保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司处置客户质押物所得中用以增加（弥补）该客户货币保证金的部分。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>权利金收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期权业务（含期货交易所期权业务和证券交易所期权业务）权利金收入，以正数填列。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>交易盈亏</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映客户本期期货交易的盈亏情况，包括持仓盈亏、平仓盈亏和行权盈亏。交易盈利以正数填列，交易亏损以负数填列。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>穿仓损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期期货公司以自有资金为客户垫付的穿仓损失。在本表计算客户货币保证金总额时，穿仓损失已包含在交易盈亏中，从而减少了客户的货币保证金总额，因此，对于期货公司垫付的与穿仓损失等量的货币资金需要加回。根据资产负债表中“应收风险损失款”明细科目分析计算填列。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>保证金出金（或转出结算资金）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映报告期内客户从期货公司取出的货币保证金（或分级结算制度下非结算会员从全面结算会员取出货币形态的结算资金），以正数填列。</td></tr></table>

<div style="text-align: center;">表11 客户权益变动表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>权利金支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期权业务（含期货交易所期权业务和证券交易所期权业务）权利金支出。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>手续费支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映客户在本期向期货公司付出的手续费，包括交易手续费、仓储费、质押手续费和交割手续费等。按照三部分填列：1. “期货公司代交易所收取的手续费”；2. “期货公司代结算机构收取的手续费”（反映分级结算制度下不具备结算业务资格的期货公司代结算机构收取的手续费）；3. “期货公司收取的手续费”（反映期货公司向客户收取的含税手续费净额）。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>期货公司代交易所收取的手续费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司代交易所收取的手续费。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>期货公司代结算机构收取的手续费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映分级结算制度下不具备结算业务资格的期货公司代结算机构收取的手续费。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>期货公司收取的手续费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司向客户收取的含税手续费净额。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>客户货币保证金期末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期期末期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>客户质押保证金期初余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期期初期货公司代客户向期货交易所办理有价证券作为保证金业务形成的可用于期货交易的保证金。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>客户质押保证金期末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期期末期货公司代客户向期货交易所办理有价证券作为保证金业务形成的可用于期货交易的保证金。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>客户权益期末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指截至期末期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金本期期末余额以及期货公司存入期货保证金账户的货币保证金。与资产负债表中的“应付货币保证金”与“应付质押保证金”之和相等。</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>期初穿仓损失金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期初期货公司以自有资金为客户垫付的穿仓损失。本表所称穿仓损失是指某个客户的权益因亏损（包括持仓亏损）而出现负数。穿仓发生时，期货公司为保证其他投资者客户分离资产的安全完整，需要在保证金账户中垫付与穿仓金额等量的自有货币资金，以保证其他客户资产和客户权益的总额不因穿仓而减少。应根据“应收风险损失款”明细科目分析计算填列。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>本期发生穿仓损失金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期发生的穿仓损失。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>本期收回穿仓损失金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期收回的穿仓损失。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>本期核销穿仓损失金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映按规定对难以收回的客户穿仓损失在本期进行核销处理的金额。</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>期末穿仓损失金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映本期期末期货公司以自有资金为客户垫付的穿仓损失。本表所称穿仓损失是指某个客户的权益因亏损（包括持仓亏损）而出现负数。穿仓发生时，期货公司为保证其他投资者客户分离资产的安全完整，需要在保证金账户中垫付与穿仓金额等量的自有货币资金，以保证其他客户资产和客户权益的总额不因穿仓而减少。应根据“应收风险损失款”明细科目分析计算填列。</td></tr></table>

## 7 期货公司财务监管报表主表数据采集

### 7.1 资产负债表

资产负债表采集的数据应符合表 12 的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 12 资产负债表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>货币资金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>货币资金指期货公司持有的库存现金和存入银行或者其他金融机构的各种款项。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>期货保证金存款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货保证金存款指期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金以及期货公司存入期货保证金账户的款项。</td></tr></table>

<div style="text-align: center;">表12 资产负债表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>应收质押保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应收质押保证金指期货公司代客户或非结算会员向期货交易所办理有价证券充抵保证金业务形成的可用于期货交易的保证金。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>存出保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映企业因履约或办理业务需要存出或缴纳的除期货、期权保证金以外的保证金款项。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>交易性金融资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司分类为以公允价值计量且其变动计入当期损益的金融资产，以及期货公司持有的指定为以公允价值计量且其变动计入当期损益的金融资产期末账面价值。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>应收结算担保金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应收结算担保金指分级结算制度下结算会员（包括全面结算会员和交易结算会员）按照规定向期货交易所缴纳的结算担保金。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>应收风险损失款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应收风险损失款指期货公司为客户垫付尚未收回的风险损失款。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>应收手续费及佣金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>核算期货公司应收未收的与其经营活动相关的手续费及佣金。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>其他应收款（合计）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据“应收利息”、“应收股利”和“其他应收款”科目的期末余额合计数，减去“坏账准备”科目中相关坏账准备期末余额后的金额填列。对于已执行新金融准则的期货公司，“应收利息”仅反映相关金融工具已到期可收取但于资产负债表日尚未收到的利息，基于实际利率法计提的金融工具的利息应包含在相应金融工具的账面余额中。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>应收股利</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应收股利指期货公司应收取的现金股利和应收取其他单位分配的利润。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>应收利息</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应收利息指期货公司相关金融工具已到期可收取但于资产负债表日尚未收到的利息。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>其他应收款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他应收款指除应收货币保证金、应收质押保证金、存出保证金、应收结算担保金、应收风险损失款、应收佣金、应收股利、应收利息等以外的其他各种应收及暂付款项。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>结算备付金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本科目核算期货公司为证券交易的资金清算与交收而存入指定清算代理机构的款项，向客户收取的结算手续费、向证券交易所支付的结算手续费，也通过本科目核算。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>债权投资</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司以摊余成本计量的债权投资的期末账面价值。由已执行新金融准则的期货公司填报。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>其他权益工具投资</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司指定为以公允价值计量且其变动计入其他综合收益的非交易性权益工具投资的期末账面价值。由已执行新金融准则的期货公司填报。</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>其他债权投资</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司分类为以公允价值计量且其变动计入其他综合收益的债权投资的期末账面价值。由已执行新金融准则的期货公司填报。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>买入返售金融资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司按照返售协议约定先买入再按固定价格返售的票据、证券、贷款等金融资产所融出的资金。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>长期股权投资</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>长期股权投资指期货公司持有的采用成本法和权益法核算的长期股权投资。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>期货会员资格投资</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货会员资格投资指期货公司为取得会员制期货交易所会员资格以交纳会员资格费形式对期货交易所的投资。</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>持有待售资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司划分为持有待售类别的非流动资产及划分为持有待售类别的处置组中的流动资产和非流动资产。</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>固定资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>固定资产指期货公司持有的固定资产。</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>使用权资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映资产负债表日承租人企业持有使用权资产的期末账面价值。由已执行新租赁准则的期货公司填报。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>无形资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>无形资产指期货公司持有的无形资产。</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>递延所得税资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>递延所得税资产指期货公司确认的可抵扣暂时性差异产生的递延所得税资产。</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>其他资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他资产指期货公司持有的除上述资产以外的资产。</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>资产总计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>短期借款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>短期借款指期货公司向银行或其他金融机构等借入的期限在1年以下（含1年）的各种借款。</td></tr></table>

<div style="text-align: center;">表12 资产负债表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>应付货币保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付货币保证金指期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金，以及期货业务交易手续费、盈亏结算后形成的货币保证金。</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>应付质押保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付质押保证金指期货公司代客户向期货交易所办理有价证券充抵保证金业务形成的可用于期货交易的保证金。</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>交易性金融负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映资产负债表日企业承担的交易性金融负债，以及企业持有的直接指定为以公允价值计量且其变动计入当期损益的金融负债的期末账面价值。</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>期货风险准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货风险准备金指期货公司按规定提取的期货风险准备金。</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>应付期货投资者保障基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付期货投资者保障基金指期货公司按规定提取的期货投资者保障基金。</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>应付职工薪酬</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付职工薪酬指期货公司根据有关规定应付给职工的各种薪酬。</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>应交税费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应交税费指期货公司按照税法等规定计算应交纳的各种税费。</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>其他应付款（合计）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据“应付利息”、“应付股利”和“其他应付款”科目的期末余额合计数填列。对于已执行新金融准则的期货公司，其中的“应付利息”仅反映相关金融工具已到期应支付但于资产负债表日尚未支付的利息，基于实际利率法计提的金融工具的利息应包含在相应金融工具的账面余额中。</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>应付利息</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付利息指期货公司相关金融工具已到期应支付但于资产负债表日尚未支付的利息。</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>应付股利</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付股利指期货公司已分配但尚未实际支付的现金股利或利润。</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>其他应付款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他应付款指企业除预收款项、应付职工薪酬、应付利息、应付股利、应交税费、长期应付款等以外的其他各项应付、暂收的款项。</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>代理买卖证券款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本科目核算期货公司接受客户委托，代理客户买卖与股票期权备兑开仓以及行权相关标的有价证券而收到的款项。</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>应付手续费及佣金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付手续费及佣金指期货公司为期货结算机构代收尚未支付的手续费以及期货公司应支付的与其经营活动相关的佣金，如应付IB佣金。</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>预计负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>预计负债指期货公司确认的对外提供担保、未决诉讼、产品质量保证、重组义务、亏损性合同等预计负债。</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>持有待售负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司处置组中与划分为持有待售类别的资产直接相关的负债的期末账面价值。</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>应付债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司为筹集（长期）资金而发行债券的本金和利息，包括可转换公司债券、优先股等。长期次级债在本科目核算，反映期货公司借入或发行的期限在1年以上（不含1年）的次级债务或次级债券。</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>优先股</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指应付债券中的优先股指期货公司分类为金融负债的优先股。</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>长期次级债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司借入或发行的期限在1年以上（不含1年）的次级债务或次级债券。</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>长期借款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>长期借款指期货公司向银行或其他金融机构借入的期限在1年以上（不含1年）的各项借款。</td></tr><tr><td style='text-align: center;'>48</td><td style='text-align: center;'>递延所得税负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>递延所得税负债指期货公司确认的应纳税暂时性差异产生的所得税负债。</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>租赁负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>租赁负债指已执行新租赁准则的期货公司尚未支付的租赁付款额。</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>其他负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他负债指期货公司承担的除上述负债以外的负债。</td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>负债合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>实收资本（或股本）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>实收资本（或股本）指期货公司接受投资者投入的实收资本（股份有限公司本指标称为股本）。</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>其他权益工具</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司发行在外的除普通股以外分类为权益工具的金融工具的期末账面价值。对于资产负债表日企业发行的金融工具，分类为权益工具的，应在“其他权益工具”项目填列，对于优先股和永续债，还应在“其他权益工具”项目下的“优先股”项目和“永续债”项目分别填列。</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>优先股</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他权益工具中的优先股指期货公司分类为权益工具的优先股。</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>永续债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他权益工具中的永续债指期货公司分类为权益工具的永续债。</td></tr></table>

<div style="text-align: center;">表12 资产负债表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>资本公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>资本公积指期货公司收到投资者出资额超出其在注册资本或股本中所占份额的部分以及直接计入所有者权益的利得和损失。</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>库存股</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>库存股指期货公司收购、转让或注销的本公司股份金额。</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>其他综合收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司根据其他企业会计准则规定，未在损益中确认的各项利得和损失扣除所得税影响后的净额。</td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>盈余公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>盈余公积指期货公司从净利润中提取的盈余公积。</td></tr><tr><td style='text-align: center;'>60</td><td style='text-align: center;'>一般风险准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>一般风险准备指期货公司按规定从税后利润提取的一般风险准备金。</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>未分配利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>未分配利润在指企业留存待以后年度分配或待分配的利润。</td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>所有者权益(或股东权益)合计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>负债和所有者权益(或股东权益)总计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 7.2 利润表

利润表采集的数据应符合表13的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 13 利润表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>营业收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>营业收入包含手续费及佣金净收入、利息净收入、投资收益、公允价值变动收益、汇兑收益、资产处置收益、其他收益和其他业务收入。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>手续费及佣金净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司应按照经纪业务、资产管理业务、交易咨询业务、基金销售业务及其他手续费及佣金收入分别填报。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>经纪业务净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司接受客户委托、按照客户的指令、为客户进行期货交易收取的服务型费用，包括交易手续费收入、代理结算手续费收入、交割手续费收入、有价证券充抵保证金手续费收入、行权手续费收入、其他手续费收入及交易所手续费返还、减收收入。经纪业务手续费收入是指期货公司扣除上交交易所手续费后的留存手续费收入部分。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>资产管理业务净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司作为资产管理人，对客户的资金进行经营运作，为客户提供期货及其他金融资产的投资管理服务，并按照合同约定向客户收取的管理费、业绩报酬等净收入。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>交易咨询业务净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司接受客户委托，向客户提供风险管理顾问，研究分析、交易咨询等服务的净收入。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>基金销售业务净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司代理基金公司向客户销售基金产品时，按照协议约定收取的代理净收入。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>其他手续费及佣金净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司除上述业务收入以外的手续费及佣金收入。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>利息净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司利息收入减去利息支出后的净值。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>利息收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映企业确认的利息收入。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>利息支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映公司为筹集生产经营所需资金等而发生的利息支出。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>投资收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司确认的投资收益或投资损失，期货公司应按照自有资金投资方向明细分别填报。损失以负数填列。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>其中：对联营企业和合营企业的投资收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的对联营企业和合营企业的投资收益或投资损失。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>对子公司的投资收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的对子公司的投资收益或投资损失。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>交易性金融工具的投资收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的划分为交易性金融工具产生的投资收益或投资损失。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>债权投资收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>债权投资收益指未计入利息收入的债权投资收益；由已执行新金融工具准则的期货公司填报。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>公允价值变动收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>在估值日按照当日投资公允价值与期初账面价值的差额。损失以负数填列。</td></tr></table>

<div style="text-align: center;">表13 利润表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>汇兑收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>外币交易因汇率变动而产生的损益以及外汇衍生金融工具产生的损益。损失以负数填列。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>资产处置收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司出售划分为持有待售的非流动资产（金融工具、长期股权投资和投资性房地产除外）或处置组（子公司和业务除外）时确认的处置利得或损失，以及处置未划分为持有待售的固定资产、在建工程及无形资产而产生的处置利得或损失。债务重组中因处置非流动资产产生的利得或损失和非货币性资产交换中换出非流动资产产生的利得或损失也包括在内。损失以负数填列。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>其他收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司计入其他收益的政府补助，以及其他与日常活动相关且计入其他收益的项目。与日常活动无关的政府补助计入营业外收支。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>其他业务收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的除主营业务活动以外的其他经营活动实现的收入，包括出租固定资产、出租无形资产、非货币性交换（非货币性资产交换具有商业实质且公允价值能够可靠计量）或债务重组等实现的收入。</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>营业支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>提取期货风险准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>提取期货风险准备金指期货公司按规定以手续费收入的一定比例提取的期货风险准备金。</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>税金及附加</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>企业经营活动发生的消费税、城市维护建设税、资源税和教育费附加等相关税费。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>业务及管理费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司在业务经营和管理过程中所发生的各项费用。</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>信用减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司计提的各项金融工具信用减值准备所确认的信用损失。</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>资产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映除“信用减值损失”外，期货公司按照相关企业会计准则的规定计提其他资产的减值准备所确认的减值损失。</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>其他业务成本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>企业确认的除主营业务活动以外的其他经营活动所发生的支出。</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>营业利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>亏损以负数填列。</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>加：营业外收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司发生的除营业利润以外的收益，主要包括与企业日常活动无关的政府补助、盘盈利得、捐赠利得。</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>减：营业外支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司发生的除营业利润以外的支出，主要包括公益性捐赠支出、非常损失、盘亏损失、非流动资产毁损报废损失。</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>利润总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>亏损以负数填列。</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>减：所得税费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的应从当期利润总额中扣除的所得税费用。</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>净利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>净亏损以负数填列。</td></tr></table>

### 7.3 所有者权益变动表

所有者权益变动表采集的数据应符合表14的要求，该表的数据仅使用于年报。对于数据类型为数值的数据要素，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 14 所有者权益变动表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>实收资本（或股本）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>其他权益工具（优先股、永续债、其他）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>资本公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>库存股</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>其他综合收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>一般风险准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>盈余公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>未分配利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>上年年末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>上年年末余额，应根据上年资产负债表中“实收资本（或股本）”、“其他权益工具”、“资本公积”、“其他综合收益”、“一般风险准备”、“盈余公积”、“未分配利润”等项目的年末余额填列。</td></tr></table>

<div style="text-align: center;">表14 所有者权益变动表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>会计政策变更</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据“盈余公积”、“利润分配”、“以前年度损益调整”等科目的发生额分析填列。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>前期差错更正</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据“盈余公积”、“利润分配”、“以前年度损益调整”等科目的发生额分析填列。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>本年年初余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>在“上年年末余额”的基础上，根据“会计政策变更”、“前期差错更正”和“其他”项目调整得出“本年年初金额”。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>本年增减变动金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>减少以负数填列。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>净利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据利润表中的净利润填列。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>直接计入所有者权益的利得和损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>其他权益工具投资公允价值变动净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司指定为以公允价值计量且其变动计入其他综合收益的非交易性权益工具投资发生的公允价值变动。</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>计入所有者权益的金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>转入当期损益的金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>其他债权投资公允价值变动净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司分类为以公允价值计量且其变动计入其他综合收益的债权投资发生的公允价值变动。</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>计入所有者权益的金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>转入当期损益的金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>权益法下被投资单位其他所有者权益变动的影响</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指除净损益、其他综合收益和利润分配外的其他原因导致被投资单位其他所有者权益变动带来的利得和损失。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>与计入所有者权益项目相关的所得税影响</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指因计入所有者权益项目（其他综合收益）产生的递延所得税。</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>所有者投入和减少资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>所有者投入资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>所有者投入资本反映期货公司接受投资者投入形成的实收资本（或股本）和资本公积。</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>其他权益工具持有者投入资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映企业发行的除普通股以外分类为权益工具的金融工具的持有者投入资本的金额。该项目应根据金融工具类科目的相关明细科目的发生额分析填列。</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>股份支付计入所有者权益的金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司处于等待期中的权益结算的股份支付当年计入资本公积的金额。</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>利润分配</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>提取盈余公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司按照规定提取的盈余公积。</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>对所有者（或股东）的分配</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>对所有者（或股东）的分配反映期货公司对普通股东以及企业发行的除普通股以外分类为权益工具的金融工具持有者的股利分配。</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>所有者权益内部结转</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>“所有者权益内部结转”下各项目，反映不影响当年所有者权益总额的所有者权益各组成部分之间当年的增减变动，包括资本公积转增资本（或股本）、盈余公积转增资本（或股本）、盈余公积弥补亏损等。</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>资本公积转增资本（或股本）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司以资本公积转增资本或股本的金额。</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>盈余公积转增资本（或股本）</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司以盈余公积转增资本或股本的金额。</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>盈余公积弥补亏损</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司以盈余公积弥补亏损的金额。</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>设定受益计划变动额结转留存收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司对于重新计量设定受益计划净负债或者净资产的变动计入其他综合收益，在原设定受益计划终止时在权益范围内将原计入其他综合收益的部分全部结转至未分配利润。</td></tr></table>

<div style="text-align: center;">表14 所有者权益变动表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>其他综合收益结转留存收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>主要反映：1. 期货公司指定为以公允价值计量且其变动计入其他综合收益的非交易性权益工具投资终止确认时，之前计入其他综合收益的累计利得或损失从其他综合收益中转入留存收益的金额；2. 期货公司指定为以公允价值计量且其变动计入当期损益的金融负债终止确认时，之前由企业自身信用风险变动引起而计入其他综合收益的累计利得或损失从其他综合收益中转入留存收益的金额等。</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>本年年末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 7.4 境内分支机构报表

境内分支机构报表采集的数据应符合表15的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 15 境内分支机构报表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>营业收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>手续费及佣金净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司根据收入准则确认的手续费及佣金净收入，包括办理期货经纪业务、资产管理业务、交易咨询业务、基金销售业务等收入。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>利息净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司利息收入减去利息支出后的净值。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>投资收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司确认的投资收益或投资损失。损失以负数填列。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>公允价值变动收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>在估值日按照当日投资公允价值与期初账面价值的差额。损失以负数填列。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>汇兑收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>公司的外币货币性项目和非货币性项目因汇率变动，在折算成本币时造成的损益。损失以负数填列。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>资产处置收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>其他收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>其他业务收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的除主营业务活动以外的其他经营活动实现的收入。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>营业费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>提取期货风险准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指期货公司按规定以手续费收入的一定比例提取的期货风险准备金。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>税金及附加</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>企业经营活动发生的增值税、消费税、城市维护建设税、资源税和教育费附加等相关税费。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>业务及管理费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司在业务经营和管理过程中所发生的各项费用。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>信用减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司计提的各项金融工具信用减值准备所确认的信用损失。本项目由已执行新金融准则的期货公司填报。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>资产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>对于已执行新金融准则的期货公司，本项目反映除“信用减值损失”外，期货公司按照相关企业会计准则的规定计提其他资产的减值准备所确认的减值损失。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>其他业务成本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>企业确认的除主营业务活动以外的其他经营活动所发生的支出。</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>营业利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>营业外收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司发生的除营业利润以外的收益，主要包括与企业日常活动无关的政府补助、盘盈利得、捐赠利得。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>营业外支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司发生的除营业利润以外的支出，主要包括公益性捐赠支出、非常损失、盘亏损失、非流动资产毁损报废损失。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>利润总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>所得税费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司确认的应从当期利润总额中扣除的所得税费用。</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>净利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>成交量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>成交量-商品期货、期权</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：万手，保留两位小数。</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>成交量-金融期货、期权</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：万手/万张，保留两位小数。</td></tr></table>

<div style="text-align: center;">表15 境内分支机构报表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>成交量-股票现货</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：万手，保留两位小数。</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>成交金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>成交金额-商品期货、期权</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>成交金额-金融期货、期权</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>成交金额-股票现货</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>统计期内新开账户数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指统计期内期货公司各分支机构新开设的账户数量（按内部资金账号统计，如果某一客户存在多个内部资金账号，按一个客户计算），单位：户。</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>统计期内新开账户数-自然人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：户。</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>统计期内新开账户数-一般法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：户。</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>统计期内新开账户数-特殊法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：户。</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>资产总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>负债总额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>负债总额-应付货币保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>负债总额-应付质押保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>统计期末账户数</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指截至统计期末按期货公司内部资金账号计算的账户数量（如果某一客户存在多个内部资金账号，按一个客户计算），单位：户。</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>统计期末账户数-自然人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：户。</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>统计期末账户数-一般法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：户。</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>统计期末账户数-特殊法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：户。</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>员工数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指与期货公司存在劳动关系的劳动者数量，包含未取得从业资格的公司员工，单位：人。</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>从业人员数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指通过从业资格考试并取得从业资格的员工数量，单位：人。</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>居间人数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期货公司居间人总数，单位：人。</td></tr><tr><td colspan="4">注：总部独立开展经纪业务的，将总部作为一个单独的业务单元上报，总部未独立开展经纪业务的，除员工数量外，可不填列或填零。</td></tr></table>

### 7.5 介绍业务经营情况表

证券公司为期货公司提供中间介绍业务（以下简称介绍业务）时，通常以证券公司营业部的形式开展，也称为IB营业部。IB营业部经营情况表采集的数据应符合表16的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 16 IB 营业部经营情况表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>IB 营业部名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>与 IB 营业部营业执照上的全称保持一致。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>总客户数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户数量总额，单位：户。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>客户数量—自然人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“自然人”客户的数量，单位：户。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>客户数量—法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“法人”客户的数量，单位：户。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>总客户权益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户权益总额。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>客户权益—自然人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“自然人”客户的权益总额。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>客户权益—法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“法人”客户的权益总额。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>当期总成交金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户成交金额总额，单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>当期成交金额—自然人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“自然人”客户的成交金额总额，单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>当期成交金额—法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“法人”客户的成交金额总额，单位：亿元，保留两位小数。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>当期总成交量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户成交量总额，单位：万手，保留两位小数。</td></tr></table>

<div style="text-align: center;">表16 IB营业部经营情况表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>当期成交量—自然人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“自然人”客户的成交量总额，单位：万手，保留两位小数。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>当期成交量—法人</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>各 IB 营业部介绍的客户，其中“法人”客户的成交量总额，单位：万手，保留两位小数。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>留存手续费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司留存的经 IB 营业部中间介绍的客户手续费收入，按照扣除增值税后的不含税金额填报。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>IB 介绍费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司从手续费收入中返还给 IB 营业部的中间介绍费用。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>IB 留存比例</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司 IB 业务中留存手续费占全部手续费收入的比例，单位：%，保留两位小数。</td></tr></table>

### 7.6 现金流量表

现金流量表采集的数据应符合表17的要求，该表的数据仅使用于年报。对于数据类型为数值的数据要素，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 17 现金流量表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>处置交易性金融资产净增加额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司处置交易性金融资产所取得的现金，减去相关处置费用后的净额。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>收取利息、手续费及佣金的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本期收取的利息、手续费及佣金收入现金数。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>收到的其他与经营活动有关的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他与经营活动有关，但不属于“处置交易性金融资产净增加额”和“收取利息、手续费及佣金的现金”这两项的现金流入。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>经营活动现金流入小计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>支付利息及佣金的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>支付给客户的利息和佣金现金数。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>支付给职工以及为职工支付的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>实际支付给职工以及为职工支付的现金，包含工资、奖金、津贴、劳动保险、社会保险、住房公积金、其他福利费等。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>以现金支付的业务及管理费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>支付的各种税费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>按规定支付的各项税费。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>支付的其他与经营活动有关的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>经营活动现金流出小计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>经营活动产生的现金流量净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>收回投资收到的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>出售、转让和到期收回的除现金等价物以外的交易性金融资产、长期股权投资而收到的现金，以及收回持有至到期投资本金收到的现金。</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>取得投资收益收到的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>因股权性投资而分得的现金股利、和分回利润所收到的现金，以及债权性投资取得的现金利息收入。</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>处置固定资产、无形资产和其他长期资产收回的现金净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>收到的其他与投资活动有关的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他与投资活动有关，但不属于上述项目的现金流入。</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>投资活动现金流入小计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>投资支付的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>在现金等价物以外进行交易性金融资产、长期股权投资、持有至到期投资所实际支付的现金。</td></tr></table>

<div style="text-align: center;">表17 现金流量表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>购建固定资产、无形资产和其他长期资产支付的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>购买、建造固定资产，取得无形资产和其他长期资产所支付的现金。</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>支付的其他与投资活动有关的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他与投资活动有关，但不属于上述项目的现金流出。</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>投资活动现金流出小计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>投资活动产生的现金流量净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>吸收投资收到的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>收到投资者投入的现金，包括以发行股票、债券等方式筹集资金实际收到的款项净额。</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>取得借款收到的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>举借各种短期借款、长期借款而收到的现金。</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>发行债券收到的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>收到其他与筹资活动有关的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他与筹资活动有关，但不属于上述项目的现金流入。</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>筹资活动现金流入小计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>偿还债务支付的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>以现金偿还债务的本金，包括偿还金融机构的借款本金、偿还到期的债券本金等，不包括偿还的借款利息、债券利息。</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>分配股利、利润或偿付利息支付的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>实际支付的现金股利、支付给投资人的利润或用现金支付的借款利息、债券利息等。</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>支付的其他与筹资活动有关的现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他与筹资活动有关，但不属于上述项目的现金流出。</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>筹资活动现金流出小计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>筹资活动产生的现金流量净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>汇率变动对现金及现金等价物的影响额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>外币现金流量发生日所采用的汇率与期末汇率的差额对现金的影响数额。</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>现金及现金等价物净增加额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>期初现金及现金等价物余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>期末现金及现金等价物余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>净利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>提取期货风险准备金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>资产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司按照相关企业会计准则规定计提的金融资产和其他资产的减值准备所确认的损失。</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>固定资产折旧</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本年度计提的固定资产折旧。</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>无形资产摊销</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本年度计提的无形资产摊销。</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>长期待摊费用摊销</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本年度计提的长期待摊费用摊销。</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>处置固定资产、无形资产和其他长期资产的损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映期货公司出售、报废固定资产、无形资产和其他长期资产所取得的现金（包括因资产毁损而收到的保险赔偿收入），减去处置这些资产而支付的有关费用后的净额，但现金净额为负数的除外。收益以负数填列。</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>固定资产报废损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>当期固定资产盘亏后的净损失，或盘盈后的净收益。收益以负数填列。</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>公允价值变动损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>持有交易性金融资产、交易性金融负债、采用公允价值模式计量的投资性房地产等公允价值变动形成的净损失。收益以负数填列。</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>投资损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>发生的投资损益。收益以负数填列。</td></tr></table>

<div style="text-align: center;">表17 现金流量表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>递延所得税资产减少</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>资产负债表“递延所得税资产”项目的期初余额与期末余额的差额。增加以负数填列。</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>递延所得税负债增加</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>资产负债表“递延所得税资产”项目的期初余额与期末余额的差额。减少以负数填列。</td></tr><tr><td style='text-align: center;'>48</td><td style='text-align: center;'>经营性应收项目的</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>经营性应收项目的减少，包括应收货币保证金、应收结算担保金、应收票据、其他应收款。减少以负数填列。</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>经营性应付项目的</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>经营性应付项目的增加，包括应付货币保证金、应付期货投资者保障基金、期货风险准备金、应付职工薪酬、应交税费、应付手续费及佣金、其他应付款。增加以负数填列。</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他与经营活动有关、不涉及现金流入流出的，不属于上述项目变动。</td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>经营活动产生的现金流量净额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>债务转为资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>债务人将债务转为资本。</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>一年内到期的可转换公司债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>融资租入固定资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>借助租赁公司或其他金融机构的资金而租入的固定资产。</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>现金的年末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>货币资金年末余额。</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>减：现金的年初余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>货币资金年初余额。</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>加：现金等价物的年末余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>现金等价物年末余额。</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>减：现金等价物的年初余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>现金等价物年初余额。</td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>现金及现金等价物净增加额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

## 8 期货公司财务监管报表附表数据采集

### 8.1 货币资金

期货公司财务监管报表附表-货币资金采集的数据应符合表18的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 18 货币资金</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>库存现金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指存放于期货公司财务部门、由出纳人员经管的、用于日常零星支出的自有资金。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>银行存款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司存放于商业银行的自有资金存款。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>期货保证金存款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司收到客户或分级结算制度下全面结算会员收到非结算会员缴存的货币保证金及期货公司存入期货保证金账户的款项。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>应收利息</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司由于银行存款等货币资金产生的、应收取的利息。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>其他货币资金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>其他货币资金是指期货公司除库存现金和银行存款以外的货币资金。包括存出投资款、银行汇票存款、银行本票存款、在途货币资金、信用证存款等。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>其他货币资金-证券账户资金余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司存放于证券结算账户，用于认申购相关证券的货币资金。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司存放于证券结算账户以外的其他货币资金，如主动扣划的相关预存款。</td></tr></table>

### 8.2 自有资金银行存款

期货公司财务监管报表附表-自由资金银行存款采集的数据应符合表19的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 19 自有资金银行存款</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>自有资金银行存款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司日常经营中产生的、所有权归属于期货公司且存放于商业银行的货币资金，该要素应当按照存放机构类别、存放机构名称进行明细列示。</td></tr></table>

### 8.3 存出保证金

期货公司财务监管报表附表-存出保证金采集的数据应符合表20的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 20 存出保证金</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>存出保证金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司因认购新股资金和办理认购新股以外的业务需要而存出或缴纳的各种保证金款项。该要素应当按照存放机构名称进行明细列示。</td></tr></table>

### 8.4 交易性金融资产

期货公司财务监管报表附表-交易性金融资产采集的数据应符合表21的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 21 交易性金融资产</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>交易性金融资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指分类为以摊余成本计量的金融资产和分类为以公允价值计量且其变动计入其他综合收益的金融资产之外的金融资产，包括债券、公募基金、股票、银行理财产品、资产管理计划、信托计划及其他金融资产。该要素应当区分具体金融资产类别，分别列示期初公允价值和期末公允价值。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>债券</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司持有的到期日固定、回收金额固定或可确定，且期货公司有明确意图和能力持有至到期的债权性证券，如购入的国债和公司债券等。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司持有的到期日固定、回收金额固定或可确定，且期货公司有明确意图和能力持有至到期的其他非衍生性金融资产。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>债权投资减值准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司基于债权投资的预期信用损失，采用适当的会计估计计量方式预计的现实或潜在信用风险损失而提取的减值准备金。</td></tr></table>

### 8.5 应收风险损失款

期货公司财务监管报表附表-应收风险损失款采集的数据应符合表22的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 22 应收风险损失款</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>应收风险损失款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司为客户垫付，尚未收回的风险损失款。该要素应当按照账龄结构、客户类别进行明细列示。</td></tr></table>

### 8.6 其他应收款

期货公司财务监管报表附表-其他应收款采集的数据应符合表23的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 23 其他应收款</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>租金押金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>租金是指期货公司为获得相应资产使用权而按双方约定支付的补偿款；押金是指根据合同约定，一方当事人存放于对方处保证自己的行为不会对对方利益造成损害，且在合同关系终止后将收回的资金。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>金融资产投资款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指基金、资产管理计划等成立之前，期货公司为认购相关产品而存放于募集专用账户内的认购款项，以及赎回基金、资产管理计划后，公司尚未收到的款项。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>员工借支/代垫</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指在日常经营管理中，员工向期货公司借用的资金或期货公司代员工支付而有权向其收取的各种款项，包括备用金借款、代垫社保公积金款项等。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指除了上述项目外，期货公司在日常经营活动中产生的其他应收款。该要素应当将金额占比前五名的往来对象进行明细列示。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>外币保证金调整项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>反映以外币作保证金进行折算时形成的差额。</td></tr></table>

### 8.7 长期股权投资

期货公司财务监管报表附表-长期股权投资的数据应符合表24的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 24 长期股权投资</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>长期股权投资</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指投资方对被投资单位实施控制、重大影响的权益性投资，以及对其合营企业的权益性投资。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>长期股权投资减值准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指因期末长期股权投资可回收金额低于账面价值而提取的减值损失准备金，该项损失准备未来不得转回。</td></tr></table>

### 8.8 固定资产

期货公司财务监管报表附表-固定资产的数据应符合表25的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 25 固定资产</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>固定资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>固定资产是指期货公司日常经营管理、为客户提供期货等衍生品业务服务而持有的且使用寿命超过一个会计年度的有形资产，包括房屋及建筑物、电子设备、办公设备、交通运输设备等。该要素应当区分固定资产类别对原价、累计折旧、资产减值准备、账面价值进行明细列示。</td></tr></table>

### 8.9 资产及信用减值准备

期货公司财务监管报表附表-资产及信用减值准备的数据应符合表26的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 26 资产及信用减值准备</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>资产减值准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司出于谨慎性原则考虑，因资产可回收金额低于账面价值而预先提取的减值损失准备金，包括长期股权投资减值准备、投资性房地产减值准备、固定资产减值准备、在建工程减值准备、无形资产减值准备、商誉减值准备等，不包括适用于新金融工具准则的金融资产减值准备。该要素应当按照具体的减值准备类别进行明细列示。</td></tr></table>

<div style="text-align: center;">表 26 资产及信用减值准备（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>信用减值准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司基于金融工具预期信用损失模型，采用适当的会计估计计量方式预计的现实或潜在信用风险损失而提取的减值准备金，包括坏账准备、债权投资减值准备、其他权益工具减值准备、其他债权投资减值准备、买入返售金融资产减值准备等。该要素应当按照具体的减值准备类别进行明细列示。</td></tr></table>

### 8.10 所有权受限的资产

期货公司财务监管报表附表-所有权受限的资产的数据应符合表27的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 27  所有权受限的资产</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>冻结的资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指在民事诉讼或者刑事侦查过程中被保全处分的或在日常经营过程中为满足特定交易需求而限制使用权但未转移所有权的资产。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>其他原因造成所有权受到限制的资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>除冻结的资产外，由于物权法或其他法律法规施加的限制，导致期货公司无法实施控制，或虽然实施了控制但并不具备完整所有权和收益权的资产。</td></tr></table>

### 8.11 其他资产

期货公司财务监管报表附表-其他资产的数据应符合表28的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 28 其他资产</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>其他资产</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指未在财务监管报表上提及的其他类资产，包括但不限于存货、投资性房地产、在建工程、长期应收款、长期待摊费用、待摊费用、预付账款、商誉及其他资产。该要素应当按照具体的资产类别进行明细列示。</td></tr></table>

### 8.12 交易性金融负债

期货公司财务监管报表附表-交易性金融负债的数据应符合表29的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 29 交易性金融负债</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>交易性金融负债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>交易性金融负债是指期货公司采用短期获利模式进行融资所形成的负债，包括以公允价值计量且其变动计入当期损益的金融负债和指定为以公允价值计量且其变动计入当期损益的金融负债，如期货公司发行短期债券等所形成的金融负债。</td></tr></table>

### 8.13 其他应付款

期货公司财务监管报表附表-其他应付款的数据应符合表30的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 30 其他应付款</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>按账龄结构</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>按照对应的账龄年限填列账面余额，期末余额合计数应等于资产负债表其他应付款的期末数。</td></tr></table>

<div style="text-align: center;">表 30 其他应付款（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>按款项类型</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据款项类型进行填列，如公司有外币业务，则需填列外币保证金调整项。期末余额合计数应等于资产负债表其他应付款的期末数。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>按关联关系</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>按照关联方及非关联方填列账面余额。“关联方”依据《企业会计准则第36号-关联方披露》执行。无关联关系的填非关联方项目。期末余额合计数应等于资产负债表的其他应付款的期末数。</td></tr><tr><td colspan="4">注：其他应付款指除应付票据、应付账款、预收账款、应付职工薪酬、应付利息、应付股利、应交税费、长期应付款等以外的其他各项应付、暂收的款项。</td></tr></table>

### 8.14 预计负债

期货公司财务监管报表附表-预计负债的数据应符合表31的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。期货公司没有预计负债事项的，无需填列。

<div style="text-align: center;">表 31 预计负债</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>预计负债的种类</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>对外提供担保、未决诉讼、产品质量保证、重组义务、亏损性合同等。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>形成原因</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>经济利益流出不确定性的说明</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>年初账面余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>本期变动</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>本年累计变动</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>期末账面余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末账面余额等于资产负债表预计负债期末数。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>预期补偿金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>本期已确认的预期补偿金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 8.15 其他负债

期货公司财务监管报表附表-其他负债的数据应符合表32的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。期货公司未发生其他负债事项无需填列。

<div style="text-align: center;">表 32 其他负债</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>长期应付款</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>短期次级债</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>预收款项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>递延收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td colspan="4">注: 其他负债期末账面余额合计数等于资产负债表其他负债的期末数。</td></tr></table>

### 8.16 次级债

期货公司财务监管报表附表-次级债的数据应符合表33的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。期货公司依据报告期无存续状态的次级债情况的，无需填列。

<div style="text-align: center;">表 33 次级债</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>债务名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>填列格式为“公司简称-次级债名称”，“次级债名称”应当与对外披露和报告内容一致，与财务明细账名称一致。每笔债务的名称一经确定即成为唯一识别标识，除分期发行外，不同债务不得共用债务名称，且次级债存续期内不许更改。</td></tr></table>

<div style="text-align: center;">表 33 次级债（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>发行期号</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>一次发行次级债的“发行期号”填列数字“1”；分期发行次级债“发行期号”按实际发行情况填列。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>债务性质</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>次级债务/次级债券</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>主要发行对象</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>股东及关联方（含发行的产品）/非关联方金融机构（含发行的产品）/非关联方企业法人及合伙企业/其他机构投资者</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>债务规模</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>应计利息</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>投资者数量</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>单位：人。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>合同生效日</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>日期格式为日历日期。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>资金到账日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>日期格式为日历日期。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>到期偿还日期</td><td style='text-align: center;'>日期</td><td style='text-align: center;'>次级债务附带投资者回售选择权的，期货公司应填列投资者可执行选择权的日期；若投资者到期放弃回售选择权，期货公司在可执行选择权日后填列合同到期偿还日期，日期格式为日历日期。</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>债券承销机构</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>债券交易所</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td colspan="4">注：期货公司及子公司为单一客户设立的资产管理产品规模，按照单个产品的受托资金余额与净值孰高计算。</td></tr></table>

### 8.17 手续费及佣金净收入

期货公司财务监管报表附表-手续费及佣金净收入的数据应符合表34的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 34 手续费及佣金净收入</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>经纪业务手续费收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>主要包括期货、期权或证券现货的交易手续费收入、代理结算手续费收入、交割手续费收入、有价证券充抵保证金业务手续费收入、行权手续费收入、申报费收入等，按照商品期货、期权，金融期货、期权，股票现货进行分类填列。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>经纪业务手续费支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>核算期货公司经纪业务产生的手续费及佣金支出。主要包括上交期货、期权和证券现货的交易手续费及佣金支出等。按照商品期货、期权，金融期货、期权，股票现货进行分类填列。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>交易所手续费返还、减收收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指不含税的交易所手续费返还、减收金额。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>交易所手续费返还、减收支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>主要包括期货公司给客户的交易所手续费返还、减收金额。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>交易咨询业务收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>按风险管理顾问服务、研究分析业务、交易咨询业务及其他分别填列。没有交易咨询业务的可不填列。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>交易咨询业务支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>资产管理业务收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>按管理费、业绩报酬、其他收入各项填列。没有资产管理业务的可不填列。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>资产管理业务支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>主要包括向代销机构支付的手续费及佣金支出等。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>基金销售业务收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>没有基金销售收入的可不填列。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>基金销售业务支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>其他手续费及佣金收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>没有其他手续费及佣金收入的可不填列。</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>其他手续费及佣金支出</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 8.18 公允价值变动收益

期货公司财务监管报表附表-公允价值变动收益的数据应符合表35的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。期货公司未发生公允价值变动收益的可不填列。

<div style="text-align: center;">表 35 公允价值变动收益</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>交易性金融资产公允价值变动收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>交易性金融负债公允价值变动收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td colspan="4">注：该表的本期发生额合计数等于利润表公允价值变动收益的本期数。</td></tr></table>

### 8.19 业务及管理费

期货公司财务监管报表附表-业务及管理费的数据应符合表36的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 36 业务及管理费</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>职工费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包括工资及福利费。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>居间人费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司按签订的居间合同支付给居间人的居间报酬。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>IB介绍费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>是指期货公司按签订的居间合同支付中间介绍业务的介绍费。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>差旅费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>业务招待费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>咨询费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>劳务费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>IT费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指期货公司为信息系统运维、开发、测试等产生的软硬件及相关人员的费用支出。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>租赁费/物业费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>包括房租、物业管理费。</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>固定资产折旧</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>无形资产摊销</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>长期待摊费用摊销</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>期货投资者保障基金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>投资者教育经费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>指期货公司为投资者教育而发生的各项费用，包括会议费、宣传费、印刷费、差旅费等。</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>其他业务及管理费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>除上述项目外的其他业务及管理费。</td></tr><tr><td colspan="4">注:该表本期发生合计数等于利润表业务及管理费本期数。</td></tr></table>

### 8.20 资产及信用减值损失

期货公司财务监管报表附表-资产及信用减值损失的数据应符合表37的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。未发生资产及信用减值损失的可不填列。

<div style="text-align: center;">表 37 资产及信用减值损失</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>坏账减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应收账款、其他应收款及应收风险损失的减值损失。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>买入返售金融资产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>债权投资减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>其他债权投资减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>长期股权投资减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>投资性房地产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>固定资产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>在建工程减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>无形资产减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>商誉减值损失</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 8.21 营业外事项

期货公司财务监管报表附表-营业外事项的数据应符合表38的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 38 营业外事项</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>营业外收入统计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>项目分为债务重组利得、与企业日常活动无关的政府补助、盘盈利得、捐赠利得等。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>营业外支出统计</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>项目分为债务重组损失、公益性捐赠支出、非常损失、盘亏损失、非流动资产毁损报废损失等。</td></tr><tr><td colspan="4">注：未发生营业外收入或支出的该表。营业外收入本期发生额合计数等于利润表营业外收入的本期数，营业外支出本期发生合计数等于利润表营业外支出的本期数。</td></tr></table>

### 8.22 或有事项

期货公司财务监管报表附表-或有事项的数据应符合表39的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 39 或有事项</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>或有负债金额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>如没有发生，可不填列。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>或有负债的种类及其形成原因</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>包括已贴现商业承兑汇票、未决诉讼、未决仲裁、对外提供担保等形成的或有负债。如没有发生，可不填列。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>经济利益流出不确定性的说明</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>如没有发生，可不填列。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>或有负债预计产生的财务影响，以及获得补偿的可能性</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>无法预计的，应当说明原因。如没有发生，可不填列。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>或有资产相关事项</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>企业通常不应当披露或有资产，但或有资产很可能会给企业带来经济利益的，应当披露其形成的原因、预计产生的财务影响等。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>未披露以上信息的事实和原因</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>在涉及未决诉讼、未决仲裁的情况下，按照前述规定披露全部或部分信息预期对企业造成重大不利影响的，企业无须披露这些信息，但应当披露该未决诉讼、未决仲裁的性质，以及没有披露这些信息的事实和原因。</td></tr></table>

### 8.23 资产负债表日后事项

期货公司财务监管报表附表-资产负债表日后事项的数据应符合表40的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 40 资产负债表日后事项</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>每项重要的资产负债表日后非调整事项的性质、内容，及其对财务状况和经营成果的影响</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>资产负债表日后非调整事项包括资产负债表日后发生重大诉讼、仲裁、承诺、资产价格、税收政策、外汇汇率发生重大变化、因自然灾害导致资产发生重大损失、发行股票和债券以及其他巨额举债、资本公积转增资本、发生巨额亏损、发生企业合并或者处置子公司。如没有资产负债表日后非调整事项发生，该内容可不填列。无法做出估计的，应当说明原因。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>拟分配的以及审议批准宣告发放的股利或利润</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>资产负债表日后，企业利润分配方案中拟分配的以及审议批准宣告发放的股利或利润。</td></tr></table>

### 8.24 关联方关系及交易

期货公司财务监管报表附表-关联方关系及交易的数据应符合表41的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。关联方、关联方交易依据《企业会计准则第36号——关联方披露》执行。未发生的可不填列。

<div style="text-align: center;">表 41 关联方关系及交易</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>关联方名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>关联方性质</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：该企业的母公司/该企业的子公司/与该企业受同一母公司控制的其他企业/对该企业实施共同控制的投资方/对该企业施加重大影响的投资方/该企业的合营企业/该企业的联营企业/该企业的主要投资者个人及与其关系密切的家庭成员/该企业或其母公司的关键管理人员及与其关系密切的家庭成员/该企业主要投资者个人、关键管理人员或与其关系密切的家庭成员控制/共同控制或施加重大影响的其他企业/其他。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>关联方交易类型</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：期货经纪业务收支/IB业务收支/交易咨询业务收支/资产管理业务收支/基金销售业务收支/利息收支/股利分红/劳务收支/代理/保险/税费/租金押金/员工薪酬福利/业务管理费用/其他。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>定价政策</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>本期净收入</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 8.25 应收关联方款项

期货公司财务监管报表附表-应收关联方款项的数据应符合表42的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。关联方、关联方交易按照《企业会计准则第36号——关联方披露》相关定义和分类要求执行。未发生的可不填列。

<div style="text-align: center;">表 42 应收关联方款项</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>关联方名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>关联方性质</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：该企业的母公司/该企业的子公司/与该企业受同一母公司控制的其他企业/对该企业实施共同控制的投资方/对该企业施加重大影响的投资方/该企业的合营企业/该企业的联营企业/该企业的主要投资者个人及与其关系密切的家庭成员/该企业或其母公司的关键管理人员及与其关系密切的家庭成员/该企业主要投资者个人、关键管理人员或与其关系密切的家庭成员控制/共同控制或施加重大影响的其他企业/其他</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>应收款项性质</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：银行存款/存出保证金/金融产品投资款/员工借支、代垫/租金押金/罚款或赔偿/其他。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>期初账面余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期初账面余额=上期的期末账面余额。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>期末坏账准备</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>期末账面余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>期末账面价值</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末账面价值=期末账面余额-期末坏账准备。</td></tr></table>

### 8.26 应付关联方款项

期货公司财务监管报表附表-应付关联方款项的数据应符合表43的要求。对于数据类型为数值的数据，如无特殊说明，单位为元，保留两位小数。关联方、关联方交易按照《企业会计准则第36号——关联方披露》相关定义和分类要求执行。未发生的可不填列。

<div style="text-align: center;">表 43 应付关联方款项</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>关联方名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr></table>

<div style="text-align: center;">表 43 应付关联方款项（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>关联方性质</td><td style='text-align: center;'>枚举</td><td style='text-align: center;'>枚举值包括：该企业的母公司/该企业的子公司/与该企业受同一母公司控制的其他企业/对该企业实施共同控制的投资方/对该企业施加重大影响的投资方/该企业的合营企业/该企业的联营企业/该企业的主要投资者个人及与其关系密切的家庭成员/该企业或其母公司的关键管理人员及与其关系密切的家庭成员/该企业主要投资者个人、关键管理人员或与其关系密切的家庭成员控制/共同控制或施加重大影响的其他企业/其他</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>应付款项性质</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>期初账面余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>枚举值包括：期初账面余额=上期的期末账面余额。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>期末账面余额</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>—</td></tr></table>

### 8.27 所有者权益附注

期货公司财务监管报表附表-所有者权益附注的数据应符合表44的要求，该表的数据仅使用于年报。对于数据类型为数值的数据要素，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 44 所有者权益附注</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>盈余公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>根据审计后的数据填列法定盈余公积及任意盈余公积，年初余额为上年末审计后的法定盈余公积和任意盈余公积。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>未分配利润</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>年初未分配利润为上年审计后的年末未分配利润，年末未分配利润公式已设定。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>资本公积</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>分为资本溢价及其他资本公积，年初余额为上年末资本公积余额。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>股东名称</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>原始股股东，二级市场的流通股股东为其他股东，按照持股比例前10名的股东进行填报。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>实收资本</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>年初余额为上年年末余额。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>不能重分类进损益的其他综合收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>年初余额为上年度不能重分类进损益的其他综合收益的年末余额，本年增加及本年减少数为利润表本期数。没有其他综合收益发生的可不填列。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>将重分类进损益的其他综合收益</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>年初余额为上年度将重分类进损益的其他综合收益的年末余额，本年增加及本年减少数为利润表本期数。没有其他综合收益发生的可不填列。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>除不能重分类进损益的及将重分类进损益的其他综合收益外的其他综合收益。未发生的可不填列。</td></tr><tr><td colspan="4">注：所有者权益附注表所填的数据均为审计后的年报数据。</td></tr></table>

### 8.28 应付职工薪酬

期货公司财务监管报表附表-应付职工薪酬的数据应符合表45的要求，该表的数据仅适用于年报审计后的数据。对于数据类型为数值的数据要素，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 45 应付职工薪酬</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>工资、奖金、津贴和补贴</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为未支付的工资、奖金、津贴和补贴，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>职工福利费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为未支付的福利费，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>社会保险费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为未支付的员工基本社会保险费，包括养老、医疗、大病、生育、失业险，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>住房公积金</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为未支付的住房公积金，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>工会经费和职工教育经费</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为公司未付的工会经费和职工教育经费，期初余额为上年度期末余额。</td></tr></table>

<div style="text-align: center;">表 45 应付职工薪酬（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>因解除劳动关系给予的补偿</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为应付职工而未付的补偿款，期初余额为上年度期末余额，该项没有应付未付的可不填列。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应付职工薪酬的其他项目，没有其他项目可不填列。</td></tr><tr><td colspan="4">注：应付职工薪酬期末余额合计数等于资产负债表应付职工薪酬的期末数。</td></tr></table>

### 8.29 其他附注

期货公司财务监管报表附表-其他附注的数据应符合表46的要求，该表的数据仅适用于年报审计后的数据。对于数据类型为数值的数据要素，如无特殊说明，单位为元，保留两位小数。

<div style="text-align: center;">表 46 其他附注</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>数据说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>应交税费-所得税</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为本年度期末应交未交的所得税，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>应交税费-城市维护建设税</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为本年度期末应交未交的城市维护建设税，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>应交税费-教育费附加</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>期末余额为本年度期末应交未交的教育费附加包括地方教育费附加，期初余额为上年度期末余额。</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>应交税费-其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>应交的其他税费。</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>税金及附加-城市维护建设税</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本期发生额为本年损益类科目税金及附加-城市维护建设税的借方金额，上期发生额为上年度发生额。</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>税金及附加-教育费附加</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本期发生额为本年损益类科目税金及附加-教育费附加及地方教育费附加借方金额，上期发生额为上年度发生额。</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>税金及附加-其他</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>除城市维护建设税及教育费附加以外的税金及附加。</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>所得税费用-当期所得税费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本期发生额为当期应交的所得税，上期发生额为上年度的本期发生额。</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>所得税费用-递延所得税费用</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>本期发生额为本期递延的所得税费用，上期发生额为上年度的本期发生额。</td></tr><tr><td colspan="4">注：应交税费期末余额合计数等于本年度资产负债表应交税费的期末数，期初余额为应交税费的期初数；税金及附加本期发生额的合计数为年度利润表税金及附加的本期数，上期发生额合计数等于上年同期数；所得税费用本期发生额合计数为年度利润表所得税费用的本期数，上期发生额合计数为上年同期数。</td></tr></table>

## 参考文献

[1] JR/T 0176.1-2019 证券期货业数据模型 第1部分：抽象模型设计方法

[2] 全国人民代表大会常务委员会. 中华人民共和国公司法（主席令第8号）, 2013年12月28日

[3] 全国人民代表大会常务委员会. 中华人民共和国期货和衍生品法, 2022年8月1日

[4] 国务院. 期货交易管理条例（国务院令第676号）, 2017年3月1日

[5] 中华人民共和国财政部.《企业会计准则第36号-关联方披露》（财会〔2006〕3号），2006年3月9日

[6] 中华人民共和国财政部. 关于修订印发2019年度一般企业财务报表格式的通知（财会〔2019〕6号），2019年4月20日

[7] 中国证券监督管理委员会. 证券公司为期货公司提供中间介绍业务试行办法（证监发〔2007〕56号）, 2007年4月20日

[8] 中国证券监督管理委员会. 关于印发《期货公司财务监管报备表》的通知（证监会计字〔2007〕17号），2007年6月4日

[9] 中国证券监督管理委员会. 关于进一步部加强期货公司信息技术管理工作的指导意见(证监会公告〔2009〕15号), 2009年7月3日

[10] 中国证券监督管理委员会. 期货公司风险监管指标管理办法（证监会令第131号）, 2017年4月18日

[11] 中国证券监督管理委员会. 期货公司风险监管报表编制与报送指引（证监会公告〔2017〕8号）, 2017年4月18日

[12] 中国证券监督管理委员会. 外商投资期货公司管理办法（证监会令第149号）, 2018年8月24日

[13] 中国证券监督管理委员会. 期货公司分类监管规定（证监会公告（2019）5号）, 2019年2月15日

[14] 中国证券监督管理委员会. 期货公司监督管理办法（证监会令第155号）,2019年6月4日

[15] 中国期货业协会. 期货公司信息技术管理指引（中期协字（2019）94号）,2019年10月16日

[16] 中国期货业协会. 期货公司财务处理实施细则（中期协字〔2022〕96号）,2022年6月14日

[17] 中华人民共和国财政部. 企业会计准则应用指南2019年版, 2019年1月

[18] 李军. 期货会计实务, 2016年1月