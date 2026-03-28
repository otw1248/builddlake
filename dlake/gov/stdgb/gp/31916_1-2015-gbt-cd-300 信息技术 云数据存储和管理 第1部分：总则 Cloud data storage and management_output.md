

# 中华人民共和国国家标准

GB/T 31916.1—2015

# 信息技术 云数据存储和管理 第 1 部分: 总则

# Information technology—Cloud data storage and management—Part 1: General

2015-09-11 发布

2016-05-01 实施

## 前言

GB/T 31916《信息技术 云数据存储和管理》分为六个部分：

——第1部分：总则；

——第2部分：基于对象的云存储应用接口；

——第3部分：分布式文件存储应用接口；

——第 4 部分: 基于块的云存储应用接口;

——第 5 部分: 基于键值 (Key-Value) 的云数据管理应用接口;

——第6部分：分布式关系数据库应用接口。

本部分为 GB/T 31916 的第 1 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别这些专利的责任。

本部分由全国信息技术标准化技术委员会(SAC/TC 28)提出并归口。

本部分起草单位：中国电子技术标准化研究院、中国移动通信有限公司研究院、东北大学软件学院、上海计算机软件技术开发中心、北京邮电大学。

本部分主要起草人：王洁萍、李海波、杜宇健、宋杰、蔡立志、吴涛、王枞、陈志峰、王卫国、杨丽蕴。

# 信息技术 云数据存储和管理

# 第 1 部分: 总则

<div style="text-align: center;"><img src="imgs/img_in_image_box_218_324_255_360.jpg" alt="Image" width="3%" /></div>


## 1 范围

GB/T 31916 的本部分给出了云数据存储和管理框架，规定了云数据存储和管理应用接口通用要求。

本部分适用于云存储和管理应用接口的规范。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

RFC 2616 超文本传输协议(HTTP)1.1(Hypertext Transfer Protocol HTTP/1.1)

## 3 术语、定义和缩略语

### 3.1 术语和定义

下列术语和定义适用于本文件。

#### 3.1.1 

数据存储服务 data storage as a service

## 云存储 cloud storage

按照指定的具有可扩展性的服务水平，通过网络将虚拟的存储和数据服务以按需使用、按量计费的方式提供的服务交付方式。该交付方式无需配置或以自服务方式配置。

[ISO/IEC 17826:2012, 定义 3.7]

#### 3.1.2 

## 元数据 metadata

定义和描述其他数据的数据。

[GB/T 18391.1—2009, 定义 3.2.16]

#### 3.1.3 

## 对象 object

记录用户数据的数据单元。

注：对象由对象名、对象标识、元数据和用户数据组成。通过对象标识可唯一定位到该对象。

#### 3.1.4 

基于对象的云存储 object-based cloud storage

## 对象存储

以对象作为存储单元，并提供对象级访问接口的云存储。

### 3.2 缩略语

下列缩略语适用于本文件。

ACL 访问控制列表(Access Control List)

API 应用编程接口(Application Programming Interface)

HTTP 超文本传输协议(Hypertext Transfer Protocol)

URI 统一资源标识符(Uniform Resource Identifier)

XML 可扩展置标语言(Extensible Markup Language)

## 4 云数据存储和管理框架

云数据存储和管理框架如图 1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_262_495_965_925.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 1 云数据存储和管理框架</div>


云数据存储和管理框架包括三层：存储层、应用接口层和应用层。其中，存储层包括数据和对数据的存储和管理。应用接口层包括各类应用接口。应用层包括各类信息系统。应用层通过统一的应用接口访问和管理存储层的各类存储资源。

根据数据的结构化程度不同，存储层提供对非结构化数据、半结构化数据和结构化数据的存储和管理。其中，非结构化数据的存储和管理方式包括基于对象、基于文件和基于块的云数据存储和管理等。半结构化数据的存储和管理方式包括基于键值（Key-Value）的云数据存储和管理等。结构化数据的存储和管理方式包括基于关系数据库的云数据存储和管理等。

## 5 云数据存储和管理应用接口通用要求

### 5.1 接口协议

云数据存储和管理应用接口应支持 HTTP 协议(RFC 2616)。

### 5.2 身份安全管理

云数据存储和管理应用接口应提供对用户的身份安全管理机制。身份安全管理可通过用户身份（AccessKeyID）和签名（Signature）实现。

### 5.3 状态码信息描述

云数据存储和管理应用接口应提供的状态码见表1。

<div style="text-align: center;">表 1 状态码及描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>状态码</td><td style='text-align: center;'>信息</td><td style='text-align: center;'>信息描述</td></tr><tr><td style='text-align: center;'>200</td><td style='text-align: center;'>OK</td><td style='text-align: center;'>资源获取成功</td></tr><tr><td style='text-align: center;'>201</td><td style='text-align: center;'>Created</td><td style='text-align: center;'>资源创建成功</td></tr><tr><td style='text-align: center;'>202</td><td style='text-align: center;'>Accepted</td><td style='text-align: center;'>已经接受处理</td></tr><tr><td style='text-align: center;'>204</td><td style='text-align: center;'>No Content</td><td style='text-align: center;'>操作成功,但无数据</td></tr><tr><td style='text-align: center;'>205</td><td style='text-align: center;'>Reset Content</td><td style='text-align: center;'>操作成功,无响应数据,客户端需要重置表单</td></tr><tr><td style='text-align: center;'>206</td><td style='text-align: center;'>Partial Content</td><td style='text-align: center;'>操作成功,仅返回部分数据</td></tr><tr><td style='text-align: center;'>400</td><td style='text-align: center;'>Bad Request</td><td style='text-align: center;'>请求内容缺失或无效的请求内容</td></tr><tr><td style='text-align: center;'>401</td><td style='text-align: center;'>Unauthorized</td><td style='text-align: center;'>权限无效</td></tr><tr><td style='text-align: center;'>403</td><td style='text-align: center;'>Forbidden</td><td style='text-align: center;'>禁止执行当前请求</td></tr><tr><td style='text-align: center;'>404</td><td style='text-align: center;'>Not Found</td><td style='text-align: center;'>请求的资源没有找到</td></tr><tr><td style='text-align: center;'>405</td><td style='text-align: center;'>Method Not Allowed</td><td style='text-align: center;'>对资源的操作不允许</td></tr><tr><td style='text-align: center;'>406</td><td style='text-align: center;'>Not Acceptable</td><td style='text-align: center;'>请求的资源的内容特性无法满足请求头中的条件,无法生成响应实体</td></tr><tr><td style='text-align: center;'>408</td><td style='text-align: center;'>Request Timeout</td><td style='text-align: center;'>数据库系统处理当前请求时间超时</td></tr><tr><td style='text-align: center;'>409</td><td style='text-align: center;'>Conflict</td><td style='text-align: center;'>由于与被请求的资源的当前状态之间存在冲突,请求无法完成</td></tr><tr><td style='text-align: center;'>411</td><td style='text-align: center;'>Missing Content-Length</td><td style='text-align: center;'>请求的报文中缺少 http content-length 头域</td></tr><tr><td style='text-align: center;'>413</td><td style='text-align: center;'>Request Entity Too Large</td><td style='text-align: center;'>服务器拒绝处理当前请求,因为该请求提交的实体数据大小超过了服务器能处理的范围</td></tr><tr><td style='text-align: center;'>415</td><td style='text-align: center;'>Unsupported Media Type</td><td style='text-align: center;'>请求资源不支持该请求实体格式</td></tr><tr><td style='text-align: center;'>416</td><td style='text-align: center;'>Requested range not satisfiable</td><td style='text-align: center;'>如果请求中包含了范围(Range)请求头,并且 Range 中指定的任何数据范围都与当前资源的可用范围不重合,同时请求中没有定义 If-Range 请求头,则服务器就应当返回 416 状态码</td></tr><tr><td style='text-align: center;'>500</td><td style='text-align: center;'>Internal Server Error</td><td style='text-align: center;'>服务器遇到未曾预料的状况,导致无法完成对请求的处理</td></tr><tr><td style='text-align: center;'>501</td><td style='text-align: center;'>Not Implemented</td><td style='text-align: center;'>系统未实现请求中所涉及到的操作和元数据,不能处理</td></tr><tr><td style='text-align: center;'>503</td><td style='text-align: center;'>Service Unavailable</td><td style='text-align: center;'>用户发起请求过于频繁,系统暂时不能为该用户提供服务</td></tr></table>

### 5.4 出错信息描述要求

对 HTTP 请求的处理如果出现错误，除了在响应消息中给出标识相应错误的代码外，还宜在响应消息中描述出错信息。出错信息描述见表 2。

<div style="text-align: center;">表 2 出错信息描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>选择状态</td></tr><tr><td style='text-align: center;'>Error</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>包含 Name、Message、Resource 和 Action 组成的出错信息描述。父标签: 无</td><td style='text-align: center;'>必选</td></tr></table>

<div style="text-align: center;">表 2 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>选择状态</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>出错名称，对错误的简短描述。父标签：Error</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>Message</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>出错消息，对错误的具体描述。父标签：Error</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>Resource</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>错误产生的资源，及请求的资源。父标签：Error</td><td style='text-align: center;'>必选</td></tr><tr><td style='text-align: center;'>Action</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>修正该错误的建议性行为。父标签：Error</td><td style='text-align: center;'>可选</td></tr></table>

软件中的出错信息用 XML 格式描述，文档类型 (Content-Type) 设为 text/xml，具体内容参见示例。

示例：

〈Error〉

Name>Invalid-AccountId</Name>

<Message>The AccountId does not exist</Message>

☑ Resource/MyAccount/Mytable/Row/Resource

☑Action Please provide a valid account☑

</Error>

## 参考文献

[1] GB/T 18391.1—2009 信息技术 元数据注册系统(MDR) 第1部分:框架

[2] ISO/IEC 17826:2012 Information technology—Cloud Data Management Interface (CDMI)