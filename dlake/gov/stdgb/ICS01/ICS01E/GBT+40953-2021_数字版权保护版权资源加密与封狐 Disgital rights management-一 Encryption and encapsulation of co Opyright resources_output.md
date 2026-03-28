

# 中华人民共和国国家标准

GB/T 40953—2021

# 数字版权保护 版权资源加密与封装

# Digital rights management—Encryption and encapsulation of copyright resources

2021-11-26 发布

2022-06-01 实施

## 目次

前言 …… III    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 缩略语 …… 1    
5 加密 …… 1    
6 封装 …… 2    
6.1 概述 …… 2    
6.2 元数据的表达 …… 2    
6.3 元数据的结构 …… 2    
附录 A（规范性） 封装的 XML Schema …… 4    
附录 B（资料性） 封装的示例 …… 5    
B.1 封装元数据 …… 5    
B.2 最小封装元数据（必选）示例 …… 5

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国新闻出版标准化技术委员会(SAC/TC 527)归口。

本文件起草单位：中国科学院自动化研究所、中国新闻出版研究院、北京大学、北大方正信息产业集团有限公司、咪咕文化科技有限公司。

本文件主要起草人：崔晓瑜、俞银燕、刘杰、张树武、黄肖俊、韦玮、曾智、刘颖丽、张倩影、穆铮。

## 数字版权保护 版权资源加密与封装

## 1 范围

本文件规定了版权描述信息在版权资源中封装的元数据，并给出了具体的数据定义和扩展性说明以及数字内容加密的原则。

本文件适用于数字出版领域开展数字版权保护工作。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

IETF RFC 3986—2005 统一资源标识符[Uniform Resource Identifier（URI）：Generic Syntax]

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

数字内容 digital content

以数字形式存在的文本、图像、音频、视频等内容资源。

### 3.2 

版权资源 copyright resources

具有版权信息的数字内容资源。

### 3.3 

版权资源封装元数据 copyright resources encapsulation metadata

根据版权资源封装描述的共性需求确定的元数据。

### 3.4 

版权资源标识 copyright resources identification

版权资源的唯一标识符。

## 4 缩略语

下列缩略语适用于本文件。

CRI: 版权资源标识(Copyright Resources Identification)

DRM: 数字版权保护 (Digital Rights Management)

XML: 可扩展置标语言 (Extensible Markup Language)

## 5 加密

本文件涉及的数字内容通过数据加密实现访问控制，使用者通过授权文件获取使用权限，加密方案

分为标准与自定义两种。

## 6 封装

### 6.1 概述

版权资源封装规定版权描述信息在版权资源中封装的元数据。

### 6.2 元数据的表达

本文件涉及的版权资源封装元数据表达包括：中文名称、英文标签、数据类型、必备性以及说明，其中数据类型包括字符串和文件路径两种，相关说明见表1。

封装元数据采用 XML 文档表示，应符合附录 A 的规定，相关示例见附录 B。

<div style="text-align: center;">表 1 数据类型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类型标识</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>ST_String</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>采用 xs:string 定义,字符串的编码选择与当前 XML 文件编码一致。如“abc”</td></tr><tr><td style='text-align: center;'>ST_Loc</td><td style='text-align: center;'>文件路径</td><td style='text-align: center;'>包内路径不使用前缀,“..”表示当前路径,“..”表示父路径。包外路径的表示方法有两种:一种是用前缀@表示外部文件相对于包的路径,“..”表示文件所在路径,“..”表示文件所在的父路径;另一种是用前缀“file://”表示本机文件的绝对路径。对“file://”路径的解释符合IETF RFC 3986—2005。如:“/Pages/P1/Resource.xml”“./Res/Book1.jpg”“./Pages/P1/Res.xml”“file:///D:/Docs/Readme.txt”“@./Appendix.txt”</td></tr></table>

### 6.3 元数据的结构

#### 6.3.1 基础类元数据

基础类元数据用于描述版权资源的基本属性信息，包括系统代号、加密方案、版权资源标识、扩展项，具体内容见表2。

<div style="text-align: center;">表 2 基础类元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>取值</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>系统代号</td><td style='text-align: center;'>DRMSystemID</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>是</td><td style='text-align: center;'>DRM 系统代号，用以对 DRM 系统进行区分</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>加密方案</td><td style='text-align: center;'>EncryptMethod</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>是</td><td style='text-align: center;'>DRM 加密方案，默认值为“Standard”</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>版权资源标识</td><td style='text-align: center;'>CRI</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>否</td><td style='text-align: center;'>版权资源的唯一标识符</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>扩展项</td><td style='text-align: center;'>Object</td><td style='text-align: center;'>任意类型</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>否</td><td style='text-align: center;'>供扩展使用</td></tr></table>

#### 6.3.2 权利类元数据

权利类元数据用于描述版权资源的相关权利属性信息，包括权利引导地址、权利对象、扩展项，具体内容见表3。

<div style="text-align: center;">表 3 权利类元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文标签</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>取值</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>权利引导地址</td><td style='text-align: center;'>RightsIssuerURL</td><td style='text-align: center;'>字符串</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>否</td><td style='text-align: center;'>权利引导地址，即在版权资源未授权时，可通过该地址获取相关信息</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>权利对象</td><td style='text-align: center;'>RightsObject</td><td style='text-align: center;'>ST_Loc</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>否</td><td style='text-align: center;'>指向权利描述信息存储位置，表明对此版权资源的授权信息，即支持版权资源和使用证书合一的方案。用户在获得授权文件后将其保存在对应路径下，使用时可根据该权利对象授权进行相应的权限操作。在应用于诸如移动设备时，将权利对象打包于版权资源中，可使用户易用性得以增强</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>扩展项</td><td style='text-align: center;'>Object</td><td style='text-align: center;'>任意类型</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>不定</td><td style='text-align: center;'>否</td><td style='text-align: center;'>供扩展使用</td></tr></table>

#### 6.3.3 扩展性说明

若实际使用中需定义更多的封装支持项时，本文件支持扩展，可在扩展项中进行自定义。

## 附录 A   (规范性)   封装的 XML Schema

本附录给出封装的 XML Schema。

<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:dmml="http://219.141.187.20/DRMGC" elementFormDefault="qualified" attributeFormDefault="qualified">
    <xs:simpleType name="ST_String">
        <xs:annotation>
            <xs:documentation>字符串</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string"/>
    </xs:simpleType>
    <xs:simpleType name="ST_Loc">
        <xs:annotation>
            <xs:documentation>文件路径</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:anyURI"/>
    </xs:simpleType>
    <xs:complexType name="DRMSecurity">
        <xs:sequence>
            <xs:element name="DRMSystemID" type="ST_String"/>
            <xs:element name="EncryptMethod" type="ST_String"/>
            <xs:element name="CRI" type="ST_String" minOccurs="0"/>
            <xs:element name="RightsIssuerURL" type="ST_String" minOccurs="0"/>
            <xs:element name="RightsObject" type="ST_Loc" minOccurs="0"/>
            <xs:element name="Object" type="xs:anyType" minOccurs="0"/>
        </xs:sequence>
    </xs:complexType>
</xs:schema>

附录 B

(资料性)

# 封装的示例

### B.1 封装元数据

本示例描述封装元数据。

DRMSecurity

<DRMSystemID>DRMS</DRMSystemID>

 $ \langle $ EncryptionMethod $ \rangle $ Standard $ \langle $ /EncryptionMethod $ \rangle $ 

<CRI>CRI000A54S1069H02000A9T4120RN280FBHAY0754210850R20210115100238

 $ \langle/CRI\rangle $ 

(RightsIssuerURL)http://www.dctrc.com/GetRights?ci=A4543DFAE

</RightsIssuerURL>

 $ \langle $ RightsObject $ \rangle $ /Doc_1/RightsObject.xml $ \langle $ /RightsObject $ \rangle $ 

〈/DRMSecurity〉

### B.2 最小封装元数据（必选）示例

本示例描述最小封装元数据（必选）。

DRMSecurity

<DRMSystemID>DRMS</DRMSystemID>

<EncryptionMethod>Standard</EncryptionMethod>

</DRMSecurity>