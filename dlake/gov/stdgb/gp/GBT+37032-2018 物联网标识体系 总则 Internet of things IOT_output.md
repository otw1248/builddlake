

# 中华人民共和国国家标准

GB/T 37032—2018

# Identification system for Internet of things—General principles

# 物联网标识体系 总则

2018-12-28 发布

2019-07-01 实施

## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 物联网标识体系框架 …… 1  
  
5 物联网标识体系的兼容性 …… 2  
  
6 物联网标识体系的开放性 …… 3  
  
7 物联网标识体系的安全性 …… 3  
  
参考文献 …… 4

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国物品编码标准化技术委员会（SAC/TC 287）和全国信息技术标准化技术委员会（SAC/TC 28）提出并归口。

本标准起草单位：中国物品编码中心、中国电子技术标准化研究院。

本标准主要起草人：李素彩、张旭、田娟、刘巍、李凯迪、马文静。

## 物联网标识体系 总则

## 1 范围

本标准规定了物联网标识体系的总体框架和所遵循的基本原则。

本标准适用于物联网系统的设计、建设与应用。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 29261.3—2012 信息技术 自动识别和数据采集技术 词汇 第3部分:射频识别

ISO/IEC 19762-1 信息技术 自动识别和数据采集技术（AIDC） 协调词汇 第1部分：与AIDC相关的一般术语 [Information technology—Automatic identification and data capture（AIDC）techniques—Harmonized vocabulary—Part 1: General terms relating to AIDC]

## 3 术语和定义

GB/T 29261.3—2012 和 ISO/IEC 19762-1 界定的术语和定义适用于本文件。

## 4 物联网标识体系框架

### 4.1 物联网标识体系组成

物联网标识体系是由编码、采集与识别、信息服务组成，见图1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_233_200_939_771.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 1 物联网标识体系框架</div>


### 4.2 编码

物联网统一编码通过赋予物联网中对象物理实体或虚拟实体全局唯一的代码，对现有系统提供建立全局唯一代码的兼容方案。

### 4.3 采集与识别

采集与识别是指按照数据协议将编码存入数据载体，通过读写设备对数据载体进行自动识别，读取编码信息并提供给信息服务进行处理。

数据载体包含但不限于条码、射频标签、NFC标签等。选择不同的数据载体要遵循不同的数据协议，如 ISO/IEC 15961、ISO/IEC 15962、ISO/IEC 15434 等。

无需数据载体的编码，可直接在信息服务进行编码相关的解析服务和发现服务操作，例如，统一资源标识符、IP 地址等。

### 4.4 信息服务

信息服务包括标识解析服务、信息发现服务和接口服务。标识解析服务提供编码对应实体的静态信息查询。信息发现服务提供实体在流通过程中对应的各个环节的动态信息查询。接口服务为其他行业应用或第三方应用平台提供接入服务。

## 5 物联网标识体系的兼容性

物联网标识体系应兼容各种编码，包括编码兼容、采集与识别兼容和信息服务兼容。编码兼容是通过赋予编码体系标识实现；采集与识别兼容是指通过识别数据载体的特征，从而判断是何种编码；信息

服务的兼容是指信息传输时附加编码体系标识。

## 6 物联网标识体系的开放性

开放性包括编码、标签通信协议和信息服务的开放性。编码应具有开放性，在不同应用中的同一编码可被识别；标签的通信协议应具有开放性，不同设备之间可互联互通；信息服务的开放性可保证不同应用之间的数据共享和交换。

## 7 物联网标识体系的安全性

物联网标识体系应具备必要的安全机制，保障标识编码在分配、注册、解析过程中的数据安全，同时标识体系所提供的信息服务也应具备安全机制。

## 参 考 文 献

[1] GB 12904 商品条码 零售商品编码与条码表示

[2] GB/T 17172—1997 四一七条码

[3] GB/T 18284—2000 快速响应矩阵码

[4] GB/T 18347 128 条码

[5] GB/T 21049—2007 汉信码

[6] GB/T 28925—2012 信息技术 射频识别 2.45 GHz 空中接口协议

[7] GB/T 29768—2013 信息技术 射频识别 800/900 MHz 空中接口协议

[8] ISO/IEC 15424:2008 Information technology—Automatic identification and data capture techniques—Data Carrier Identifiers (including Symbology Identifiers)

[9] ISO/IEC 15434:2006 Information technology—Automatic identification and data capture techniques—Syntax for high-capacity ADC media

[10] ISO/IEC 15961:2004 Information technology—Radio frequency identification (RFID) for item management—Data protocol—Application interface

[11] ISO/IEC 15962:2013 Information technology—Radio frequency identification (RFID) for item management—Data protocol: data encoding rules and logical memory functions

[12] ISO/IEC 18000-2:2009 Information technology—Radio frequency identification for item management—Part 2: Parameters for air interface communications below 135 kHz

[13] ISO/IEC 18000-3:2010 Information technology—Radio frequency identification for item management—Part 3: Parameters for air interface communications at 13.56 MHz

[14] ISO/IEC 18000-4:2015 Information technology—Radio frequency identification for item management—Part 4: Parameters for air interface communications at 2.45 GHz

[15] ISO/IEC 18000-61:2012 Information technology—Radio frequency identification for item management—Part 61: Parameters for air interface communications at 860 MHz to 960 MHz Type A

[16] ISO/IEC 18000-62:2012 Information technology—Radio frequency identification for item management—Part 62: Parameters for air interface communications at 860 MHz to 960 MHz Type B

[17] ISO/IEC 18000-63:2013 Information technology—Radio frequency identification for item management—Part 63: Parameters for air interface communications at 860 MHz to 960 MHz Type C

[18] ISO/IEC 18000-64:2012 Information technology—Radio frequency identification for item management—Part 64: Parameters for air interface communications at 860 MHz to 960 MHz Type D

[19] ISO/IEC 18000-7:2014 Information technology—Radio frequency identification for item management—Part 7: Parameters for active air interface communications at 433 MHz