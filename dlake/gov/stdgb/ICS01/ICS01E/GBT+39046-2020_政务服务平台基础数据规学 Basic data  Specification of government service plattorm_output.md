

# 中华人民共和国国家标准

GB/T 39046—2020

# 政务服务平台基础数据规范

# Basic data specification of government service platform

2020-07-21 发布

2020-10-01 实施

## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 数据分类 …… 1  
  
5 数据项表示 …… 2  
  
5.1 概述 …… 2  
  
5.2 数据项名称 …… 2  
  
5.3 数据类型及格式 …… 2  
  
5.4 备注 …… 3  
  
6 数据集 …… 3  
  
6.1 事项管理 …… 3  
  
6.2 办事申请 …… 5  
  
6.3 事项受理 …… 5  
  
6.4 事项办理 …… 6  
  
6.5 事项办结 …… 7  
  
6.6 政务服务绩效评价 …… 7  
  
6.7 办事互动 …… 8  
  
6.8 电子监察 …… 9  
  
6.9 公共支撑 …… 10  
  
附录 A（规范性附录） 代码集 …… 13  
  
参考文献 …… 16

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国行政审批标准化工作组(SAC/SWG 14)提出并归口。

本标准起草单位：国务院办公厅电子政务办公室、中国标准化研究院、山东省标准化研究院、山东省计算中心（国家超级计算济南中心）、南京市政务服务管理办公室（南京市行政审批局）、浙江省大数据发展管理局、江西省信息中心、广东省政务服务数据管理局、四川省大数据中心、公安部第一研究所、国泰新点软件股份有限公司、东软集团股份有限公司、浙江非线数联科技有限公司、北京国脉信安科技有限公司、鲸数科技（北京）有限公司、佛山市顺德区质量技术监督标准与编码所、山东省大数据局。

本标准主要起草人：许潇文、巫小波、张媛、冯蕾、卢向东、尹智刚、管晋华、李三群、陈治佳、孙富安、姜舟、徐云、李景曦、钱学文、常立丽、王曙光、赵硕、史丛丛、逄锦山、王赟萃、孙杨、李松渊、张军、李恒训、袁勋、肖学文、徐欢、张立圆、徐起、刘辉、赵文慧、李春、侯军霞、孙战峰、王俊人。

## 政务服务平台基础数据规范

## 1 范围

本标准规定了政务服务平台基础数据分类、分类下的数据项集合，以及具体数据项的属性。

本标准适用于政务服务平台的建设及数据交换共享等工作。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2261.1 个人基本信息分类与代码 第1部分:人的性别代码

GB 2312 信息交换用汉字编码字符集 基本集

GB/T 7408 数据元和交换格式 信息交换 日期和时间表示法

GB/T 19488.2—2008 电子政务数据 第2部分：公共数据元目录

GB 32100—2015 法人和其他组织统一社会信用代码编码规则

GB/T 36902—2018 电子证照 目录信息规范

GB/T 39047—2020 政务服务平台基本功能规范

GA/T 2000.156 公安信息代码 第 156 部分: 常用证件代码

## 3 术语和定义

GB/T 39047—2020 界定的术语和定义适用于本文件。

## 4 数据分类

政务服务平台基础数据分类见表1，实际使用时可在现有分类及数据项基础上进行扩展。

<div style="text-align: center;">表 1 数据分类</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据分类</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>事项管理</td><td style='text-align: center;'>包括但不限于事项分类信息、基本目录信息、实施清单信息</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>办事申请</td><td style='text-align: center;'>包括但不限于申请登记信息、申请材料信息、中介服务信息</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>事项受理</td><td style='text-align: center;'>包括但不限于事项受理信息、材料目录信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>事项办理</td><td style='text-align: center;'>包括但不限于办理过程信息、办理进度信息、特别程序信息</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>事项办结</td><td style='text-align: center;'>包括但不限于办结信息</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>服务评价</td><td style='text-align: center;'>包括但不限于线上线下评价信息</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>办事互动</td><td style='text-align: center;'>包括但不限于咨询信息、投诉信息</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>电子监察</td><td style='text-align: center;'>包括但不限于督办基本信息、督办过程信息、督办结果信息</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>公共支撑</td><td style='text-align: center;'>包括但不限于统一身份认证信息、电子印章信息、电子证照信息、支付信息、物流信息、目录信息</td></tr></table>

## 5 数据项表示

### 5.1 概述

采用如下属性描述数据项：

——数据项名称：

——数据类型及格式；

——备注。

### 5.2 数据项名称

数据项的中文名称，是赋予数据项的单个或多个中文字词的指称。

### 5.3 数据类型及格式

数据项的数据类型见表2。

<div style="text-align: center;">表 2 数据类型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>字符型</td><td style='text-align: center;'>通过字符形式表达的值的类型</td></tr><tr><td style='text-align: center;'>数字型</td><td style='text-align: center;'>通过从“0”到“9”数字形式表达的值的类型</td></tr><tr><td style='text-align: center;'>日期型</td><td style='text-align: center;'>通过 YYYYMMDD 的形式表达的值的类型，符合 GB/T 7408</td></tr><tr><td style='text-align: center;'>日期时间型</td><td style='text-align: center;'>通过 YYYYMMDDhhmmss 的形式表达的值的类型，符合 GB/T 7408</td></tr><tr><td style='text-align: center;'>布尔型</td><td style='text-align: center;'>两个且只有两个表明条件的值，如 On/Off、True/False</td></tr><tr><td style='text-align: center;'>二进制</td><td style='text-align: center;'>上述无法表示的其他数据类型，如图像、音频、视频、文件等</td></tr></table>

数据项长度的表示格式使用表 3 中的字符来描述。

<div style="text-align: center;">表 3 数据格式的表示</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>符号</td><td style='text-align: center;'>符号说明</td></tr><tr><td style='text-align: center;'>a</td><td style='text-align: center;'>字母字符</td></tr><tr><td style='text-align: center;'>n</td><td style='text-align: center;'>数字字符</td></tr><tr><td style='text-align: center;'>an</td><td style='text-align: center;'>字母数字字符</td></tr><tr><td style='text-align: center;'>m(m为自然数)</td><td style='text-align: center;'>定长m个字符(字符集默认为GB 2312)</td></tr><tr><td style='text-align: center;'>ul</td><td style='text-align: center;'>长度不确定的文本</td></tr><tr><td style='text-align: center;'>p,q(p,q均为自然数)</td><td style='text-align: center;'>最长p个字符,小数点后q位</td></tr><tr><td style='text-align: center;'>..</td><td style='text-align: center;'>从最小长度到最大长度,前面附加最小长度,后面附加最大长度</td></tr><tr><td style='text-align: center;'>YYYYMMDDhhmmss</td><td style='text-align: center;'>&quot;YYYY&quot;表示年份,&quot;MM&quot;表示月份,&quot;DD&quot;表示日期,&quot;hh&quot;表示小时,&quot;mm&quot;表示分钟,&quot;ss&quot;表示秒,可以视实际情况组合使用</td></tr></table>

示例 1: an5(aannn) 表示定长 5 个字母数字字符, 前 2 个为字母字符, 后 3 个为数字字符。

示例 2: n..17,2 表示最长 17 个数字字符, 小数点后两位。

示例 3: an3..8 表示最大长度为 8, 最小长度为 3 的不定长的字母数字字符。

### 5.4 备注

数据项其他方面的说明。

## 6 数据集

### 6.1 事项管理

事项管理基础数据集见表4。

<div style="text-align: center;">表 4 事项管理基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>事项名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>基本编码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'>政务服务事项目录清单中事项的唯一标识代码</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>实施编码</td><td style='text-align: center;'>字符型 an..24</td><td style='text-align: center;'>政务服务事项实施清单中事项的唯一标识代码</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>事项类型</td><td style='text-align: center;'>字符型 an..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>事项类型代码</td><td style='text-align: center;'>字符型 n2</td><td style='text-align: center;'>见附录A的A.1</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>设定依据</td><td style='text-align: center;'>字符型 a..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>行使层级</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>行使层级代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>见A.2</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>权限划分</td><td style='text-align: center;'>字符型 a..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>行使内容</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>实施主体</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008中机构名称</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>实施主体代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>符合GB 32100—2015的编码规则</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>实施主体性质</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>实施主体性质代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>见A.3</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>法定办结时限</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>法定办结时限单位</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>法定办结时限说明</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>承诺办结时限</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>承诺办结时限单位</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>承诺办结时限说明</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>受理条件</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>办理流程</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>共同实施部门</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>联办机构</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>共同实施部门代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>符合GB 32100—2015的编码规则</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>承办机构</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008中机构名称</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>承办机构代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>符合GB 32100—2015的编码规则</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>中介服务</td><td style='text-align: center;'>字符型 an..2000</td><td style='text-align: center;'>事项办理法定中介服务</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>数量限制</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">表 4（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>结果名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>结果样本</td><td style='text-align: center;'>二进制</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>是否收费</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>收费依据</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>通办范围代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>全国、跨省、跨市、跨县</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>服务对象</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>服务对象代码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'>见 A.4</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>服务主题</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>法人服务主题代码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>自然人服务主题代码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>办理形式</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>明确窗口办理或网上办理</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>办理形式代码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'>见 A.5</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>特别程序</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>行政管辖</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>行政管辖代码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>是否支持预约办理</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>是否支持网上支付</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>是否支持物流快递</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>是否网办</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>48</td><td style='text-align: center;'>网办地址</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>运行系统层级</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>国家级/省级/市级</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>办理地点</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>办理时间</td><td style='text-align: center;'>字符型 an..150</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>咨询方式</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>电话、信件、邮件等多种投诉方式</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>咨询电话</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>GB/T 19488.2-2008 中联系电话</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>监督电话</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>GB/T 19488.2-2008 中联系电话</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>常见问题</td><td style='text-align: center;'>字符型 an..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>材料名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>出具机构</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2-2008 中机构名称</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>出具时间要求</td><td style='text-align: center;'>字符型 an..150</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>材料办理说明</td><td style='text-align: center;'>字符型 an..500</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>60</td><td style='text-align: center;'>材料办理地点</td><td style='text-align: center;'>字符型 an..400</td><td style='text-align: center;'>GB/T 19488.2-2008 中详细地址</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>材料使用说明</td><td style='text-align: center;'>字符型 an..500</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>原件份数</td><td style='text-align: center;'>数字型 n..2</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>复印件份数</td><td style='text-align: center;'>数字型 n..2</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>是否必备材料</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr></table>

### 6.2 办事申请

办事申请基础数据集见表5。

<div style="text-align: center;">表 5 办事申请基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>实施编码</td><td style='text-align: center;'>字符型 an..24</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>事项名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>办件类型</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>办件类型代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>见 A.6</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>申请者名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中姓名或机构名称</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>申请者证件类型代码</td><td style='text-align: center;'>字符型 n3</td><td style='text-align: center;'>GA/T 2000.156 中证件类型代码</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>申请者证件号码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>GB/T 19488.2—2008 中身份证件号码</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>联系人/代理人姓名</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'>GB/T 19488.2—2008 中姓名</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>联系人/代理人证件类型代码</td><td style='text-align: center;'>字符型 n3</td><td style='text-align: center;'>GA/T 2000.156 中证件类型代码</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>联系人/代理人证件号码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>GB/T 19488.2—2008 中身份证件号码</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>联系人手机号码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>GB/T 19488.2—2008 中移动号码</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>邮政编码</td><td style='text-align: center;'>字符型 n6</td><td style='text-align: center;'>GB/T 19488.2—2008 中邮政编码</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>通讯地址</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中通信地址</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>法定代表人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'>企业申请人的法定代表人</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>申报来源代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>办理形式</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>申请时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'>GB/T 19488.2—2008 中时间</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>投资项目编号</td><td style='text-align: center;'>字符型 an..24</td><td style='text-align: center;'>国家投资项目编号</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>字符型 n..9</td><td style='text-align: center;'>申报者所在地的行政区划代码</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>材料名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>是否收取</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>0-否,1-是</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>收取方式</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>收取数量</td><td style='text-align: center;'>字符型 n..2</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>收取时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'>GB/T 19488.2—2008 中日期时间</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>附件实体</td><td style='text-align: center;'>二进制</td><td style='text-align: center;'>文件数据流</td></tr></table>

### 6.3 事项受理

事项受理基础数据集见表6。

<div style="text-align: center;">表 6 事项受理基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>基本编码</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>实施编码</td><td style='text-align: center;'>字符型 an..24</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>事项名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>受理单位名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中机构名称</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>受理单位统一社会信用代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>符合 GB 32100—2015 的编码规则</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>受理人员</td><td style='text-align: center;'>字符型 an..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>受理时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'>GB/T 19488.2—2008 中日期时间</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>受理文书编号</td><td style='text-align: center;'>字符型 an..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>承诺办结时间</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>办件类型</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>办件类型代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>见 A.6</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>字符型 n..9</td><td style='text-align: center;'>受理地的行政区划代码</td></tr></table>

### 6.4 事项办理

事项办理基础数据集见表7。

<div style="text-align: center;">表 7 事项办理基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>业务动作</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>通过、退回、其他</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>环节名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>环节处理人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>环节处理意见</td><td style='text-align: center;'>字符型 an..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>环节开始时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>环节结束时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'>如没有结束时间，则填写开始时间</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>处理单位名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中机构名称</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>处理单位统一社会信用代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>符合 GB 32100—2015 的编码规则</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>环节办理状态代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-待办，2-已办</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>特别程序种类名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr></table>

表 7 (续)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>特别程序种类代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>见 A.7</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>特别程序开始时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>特别程序启动理由或依据</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>申请人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'>提出特别规定申请的人</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>特别程序结束时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>特别程序结果</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'>进入特别规定后得出的结论，如实地核查、听证、检验、检测、检疫、鉴定结果等</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>特别程序办理意见</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'>审批办理意见</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>办理单位名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中机构名称</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>办理单位统一社会信用代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'>符合 GB 32100—2015 的编码规则</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>办理人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'>GB/T 19488.2—2008 中姓名</td></tr></table>

### 6.5 事项办结

事项办结基础数据集见表8。

<div style="text-align: center;">表 8 事项办结基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>办理人姓名</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>办结时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDhh:mm:ss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>结果证照名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>结果证照编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>办件结果描述</td><td style='text-align: center;'>字符型 an..1000</td><td style='text-align: center;'>证照照面信息描述</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>证照有效期限</td><td style='text-align: center;'>字符型 an..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>发证/盖章单位</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中机构名称</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>字符型 n..9</td><td style='text-align: center;'>办结地的行政区划代码</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>是否快递寄送结果</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>是否收费</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr></table>

### 6.6 政务服务绩效评价

政务服务绩效评价基础数据集见表9。

<div style="text-align: center;">表 9 政务服务绩效评价基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>评价渠道</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'>PC端、移动服务端、二维码、政务大厅平板电脑、政务大厅其他终端、电话、短信</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>评价人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>评价时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>评价次数</td><td style='text-align: center;'>数字型 n..2</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>满意度</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>满意度代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>见 A.8</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>文字评价</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>字符型 n..9</td><td style='text-align: center;'>办件评价地的行政区划代码</td></tr></table>

### 6.7 办事互动

办事互动基础数据集见表10。

<div style="text-align: center;">表 10 办事互动基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>咨询编码</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>咨询人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>咨询标题</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>咨询内容</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'>咨询问题的主要内容</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>咨询时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>处理时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>处理人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>处理意见</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'>针对咨询问题的答复意见</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>延期时限</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>延期原因</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>超期天数</td><td style='text-align: center;'>数字型 n..3</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>字符型 n..9</td><td style='text-align: center;'>咨询地行政区划代码</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>投诉标题</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>投诉人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>被投诉单位</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">表 10（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>被投诉人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>投诉内容</td><td style='text-align: center;'>字符型 an..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>投诉来源</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>投诉时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>承办单位代码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>承办单位名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>承办人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>承办时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>反馈信息</td><td style='text-align: center;'>字符型 an..500</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>反馈时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDThhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>承诺时限</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>投诉办理的承诺时限</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>延期时限</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>延期原因</td><td style='text-align: center;'>字符型..ul</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>超期天数</td><td style='text-align: center;'>数字型 n..3</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>字符型 n..9</td><td style='text-align: center;'>投诉地的行政区划代码</td></tr></table>

### 6.8 电子监察

电子监察基础数据集见表11。

<div style="text-align: center;">表 11 电子监察基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'>521C</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>督办内容</td><td style='text-align: center;'>字符型 an..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>机构名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>被督办机构的名称</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>事项类型代码</td><td style='text-align: center;'>字符型 n2</td><td style='text-align: center;'>见 A.1</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>督办发出时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDhhmmss</td><td style='text-align: center;'>督办内容发出的时间</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>监察编号</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>业务在监察系统中的唯一标识</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>监察规则编号</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>监察规则的唯一标识</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>监察预警类型代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>状态产生时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDhhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>监察结果描述</td><td style='text-align: center;'>字符型 an..1000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>责任部门</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr></table>

### 6.9 公共支撑

#### 6.9.1 统一身份认证

统一身份认证基础数据集见表 12。

<div style="text-align: center;">表 12 统一身份认证基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>用户编码</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'>自然人用户在平台的唯一编码</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>姓名</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'>GB/T 19488.2—2008 中姓名</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>证件类型</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>身份证件号码</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>民族</td><td style='text-align: center;'>字符型 a..10</td><td style='text-align: center;'>GB/T 19488.2—2008 中民族</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>职务</td><td style='text-align: center;'>字符型 a..12</td><td style='text-align: center;'>GB/T 19488.2—2008 中职务</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>用户名</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'>统一账号的用户名</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>密码</td><td style='text-align: center;'>字符型 an..60</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>移动电话</td><td style='text-align: center;'>字符型 an..18</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>邮箱</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>是否实名认证</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-已认证,0-未认证</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>性别代码</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>GB/T 2261.1 中代码</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>工作单位</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>机构地址</td><td style='text-align: center;'>字符型 an..400</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>机构名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>GB/T 19488.2—2008 中机构名称</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>法定代表人/负责人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>字符型 an18</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>是否实名认证</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>注册地址</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>注册日期</td><td style='text-align: center;'>日期型 YYYYMMDD</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>经营范围</td><td style='text-align: center;'>字符型 a..1000</td><td style='text-align: center;'>GB/T 19488.2—2008 中经营范围</td></tr></table>

#### 6.9.2 电子印章信息

电子印章信息基础数据集见表 13。

<div style="text-align: center;">表 13 电子印章基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>电子签章版本</td><td style='text-align: center;'>字符型 an..10</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>签章人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'>印章使用人</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>签章时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDhhmmss</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">表 13 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>印章类型</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>印章名称</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>制作日期</td><td style='text-align: center;'>日期型 YYYYMMDD</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>发放日期</td><td style='text-align: center;'>日期型 YYYYMMDD</td><td style='text-align: center;'></td></tr></table>

#### 6.9.3 电子证照信息

电子证照信息基础数据集应符合 GB/T 36902—2018 的规定。

#### 6.9.4 支付信息

支付信息基础数据集见表 14。

<div style="text-align: center;">表 14 支付信息基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>缴款单号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>收费单位</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>收费人员</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>收费金额</td><td style='text-align: center;'>数字型 n..16,2</td><td style='text-align: center;'>计量单位为元</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>收费时间</td><td style='text-align: center;'>日期时间型 YYYYMMDDhhmmss</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>缴款人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr></table>

#### 6.9.5 物流信息

物流信息基础数据集见表 15。

<div style="text-align: center;">表 15 物流信息基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>办件编号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>物流单号</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>寄送单位</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>寄送日期</td><td style='text-align: center;'>日期型 YYYYMMDD</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>寄送人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>接收单位</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>接收人</td><td style='text-align: center;'>字符型 a..30</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>接收日期</td><td style='text-align: center;'>日期型 YYYYMMDD</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">表 15 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>评估指标</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>评估项目</td><td style='text-align: center;'>字符型 an..200</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>评估时间</td><td style='text-align: center;'>日期型 YYYYMMDD</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>评估等级</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>评估结果</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr></table>

#### 6.9.6 数据目录信息

政务服务数据目录信息基础数据集见表16。

<div style="text-align: center;">表 16 政务服务数据目录信息基础数据集</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型及格式</td><td style='text-align: center;'>其他要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>事项名称</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>事项办结结果名称</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'>办理事项产生的结果名称</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>是否电子证照</td><td style='text-align: center;'>字符型 n1</td><td style='text-align: center;'>1-是,0-否</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>应用场景</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>政务服务数据提供方</td><td style='text-align: center;'>字符型 an..100</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>政务服务数据摘要</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>提供渠道</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>所属领域</td><td style='text-align: center;'>字符型 an..50</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>更新周期</td><td style='text-align: center;'>字符型 an..20</td><td style='text-align: center;'></td></tr></table>

# 附录 A

(规范性附录)

代码集

### A.1 事项类型代码

事项类型代码见表 A.1。

<div style="text-align: center;">表 A.1 事项类型代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>事项类型</td></tr><tr><td style='text-align: center;'>00</td><td style='text-align: center;'>行政权力事项</td></tr><tr><td style='text-align: center;'>01</td><td style='text-align: center;'>行政许可</td></tr><tr><td style='text-align: center;'>02</td><td style='text-align: center;'>行政处罚</td></tr><tr><td style='text-align: center;'>03</td><td style='text-align: center;'>行政强制</td></tr><tr><td style='text-align: center;'>04</td><td style='text-align: center;'>行政征收</td></tr><tr><td style='text-align: center;'>05</td><td style='text-align: center;'>行政给付</td></tr><tr><td style='text-align: center;'>06</td><td style='text-align: center;'>行政检查</td></tr><tr><td style='text-align: center;'>07</td><td style='text-align: center;'>行政确认</td></tr><tr><td style='text-align: center;'>08</td><td style='text-align: center;'>行政奖励</td></tr><tr><td style='text-align: center;'>09</td><td style='text-align: center;'>行政裁决</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>其他类别事项</td></tr><tr><td style='text-align: center;'>11……</td><td style='text-align: center;'>可根据情况进行扩展，如政府内部审批等</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>公共服务事项</td></tr><tr><td style='text-align: center;'>21……</td><td style='text-align: center;'>可根据情况进行扩展</td></tr></table>

### A.2 行使层级代码

行使层级代码见表 A.2。

<div style="text-align: center;">表 A.2 行使层级代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>行使层级</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>国家级/局(署、会)</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>省级/直属</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>市级/隶属</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>县级</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>镇(乡、街道)级</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>村(社区)级</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>分级管理</td></tr></table>

### A.3 实施主体性质代码

实施主体性质代码见表 A.3。

<div style="text-align: center;">表 A.3 实施主体性质代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>实施主体性质</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>法定机关</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>授权组织</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>受委托组织</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>其他</td></tr></table>

### A.4 服务对象代码

服务对象代码见表 A.4。

<div style="text-align: center;">表 A.4 服务对象代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>服务对象</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>自然人</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>企业法人</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>事业法人</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>社会组织法人</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>行政机关</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>其他组织</td></tr></table>

### A.5 办理形式代码

办理形式代码见表 A.5。

<div style="text-align: center;">表 A.5 办理形式代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>办理形式</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>窗口办理</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>电脑端网上办理</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>移动端网上申请</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>快递申请</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>其他</td></tr></table>

### A.6 办件类型代码

办件类型代码见表 A.6。

<div style="text-align: center;">表 A.6 办件类型代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>办件类别</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>即办件</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>承诺件</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>其他</td></tr></table>

### A.7 特别程序种类代码

特别程序种类代码见表 A.7。

<div style="text-align: center;"><img src="imgs/img_in_image_box_129_692_166_726.jpg" alt="Image" width="3%" /></div>


<div style="text-align: center;">表 A.7 特别程序种类代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>特别程序种类</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>延长审批</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>除延长审批之外的情况</td></tr></table>

### A.8 满意度代码

满意度代码见表 A.8。

<div style="text-align: center;">表 A.8 满意度代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>满意度</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>非常满意</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>满意</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>基本满意</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>不满意</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>非常不满意</td></tr></table>

## 參 考 文 献

[1] ZWFW C0109.1—2018 国家政务服务平台政务服务事项基本目录及实施清单 第1部分：编码要求

[2] ZWFW C0109.2—2018 国家政务服务平台政务服务事项基本目录及实施清单 第2部分：要素要求

[3] 国务院办公厅转发国家发展改革委、财政部等10部门推进“互联网+政务服务”开展信息惠民试点实施方案(国办发 $$ 2016 $$ 23号)

[4] 国务院办公厅关于印发“互联网+政务服务”技术体系建设指南的通知(国办函〔2016〕108号)

[5] 国务院关于加快推进全国一体化在线政务服务平台建设的指导意见(国发 $$ 2018 $$ 27号)

[6] 全国一体化在线政务服务平台建设和管理协调小组办公室关于印发全国一体化在线政务服务平台数据共享服务管理暂行办法的通知(国办电政函 $$ 2019 $$ 235号)