

# 中华人民共和国国家标准

GB/T 37149—2018

# 统一社会信用代码地理信息采集规范

# Specification for data collection of unified social credit identifier geographic information

2018-12-28 发布

2019-07-01 实施

## 目次

前言 …… III  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语、定义和缩略语 …… 1  
  
4 参考系统及标识方法 …… 3  
  
5 技术指标 …… 4  
  
6 统一社会信用代码地理信息数据及格式 …… 4  
  
7 采集内容和要求 …… 5  
  
8 统一社会信用代码地理信息采集与更新技术 …… 9  
  
9 质量要求与符合性检查 …… 15  
  
附录 A（规范性附录） 组织机构所处地貌代码 …… 16  
  
附录 B（规范性附录） 基本地点名称优先级 …… 17  
  
附录 C（规范性附录） 组织机构院落分类及代码 …… 18  
  
附录 D（规范性附录） 地面照片属性定义及采集要求 …… 19  
  
参考文献 …… 21

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国信息分类与编码标准化委员会(SAC/TC 353)提出并归口。

本标准主要起草单位: 全国组织机构统一社会信用代码数据服务中心、中国测绘科学研究院、辽宁省标准化研究院、哈尔滨市标准化研究院、江苏省质量和标准化研究院、黑龙江省标准化研究院、武汉市测绘研究院、济南市技术监督局。

本标准起草人：孙立坚、孙镇、苏德国、赵捷、刘纪平、孙泰、柯志勇、袁辉、金江、司琳华、钱晓东、李晟飞、宫政、孟炬、施晓琳、董春、朱峰、罗名海、甄云鹏、徐胜华、朱钰、徐一鸣、李一峰、贺佳。

# 统一社会信用代码地理信息采集规范

## 1 范围

本标准规定了统一社会信用代码地理信息采集的技术指标、采集内容和方法、质量控制等要求，同时也规定了采集统一社会信用代码地理信息的作业流程。

本标准适用于建立统一社会信用代码地理信息数据库及相关地理信息系统时，对组织机构地理信息的采集、处理与更新。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2260 中华人民共和国行政区划代码

GB/T 10114 县级以下行政区划代码编制规则

GB/T 13977—2012 1:5 000 1:10 000 地形图航空摄影测量外业规范

GB/T 17798 地理空间数据交换格式

GB/T 18314—2009 全球定位系统(GPS)测量规范

GB/T 20257.2—2017 国家基本比例尺地图图式 第2部分：1:5000 1:10000地形图图式

GB/T 23705—2009 数字城市地理信息公共平台地名/地址编码规则

GB 32100—2015 法人和其他组织统一社会信用代码编码规则

GB/T 33179—2016 国家基本比例尺地图 1:25000 1:50000 1:100000 正射影像地图

GB/T 33182—2016 国家基本比例尺地图 1:5000 1:10000 正射影像地图

GB 50167 工程摄影测量规范

CH/Z 9010—2011 地理信息公共服务平台 地理实体与地名地址数据规范

CJ/T 215—2005 城市市政综合监管信息系统 地理编码

## 3 术语、定义和缩略语

### 3.1 术语和定义

下列术语和定义适用于本文件。

3.1.1

组织机构 organization

企业、事业单位、机关、社会团体及其他依法成立的单位的通称。

[GB/T 20091—2006, 定义 2.2]

3.1.2

统一社会信用代码 ___ unified social credit identifier

按照 GB 32100—2015 编制，由法人和其他组织登记管理部门、统一社会信用代码管理部门根据国家标准编制，每一个法人和其他组织在全国范围内唯一的、终身不变的法定身份识别码。

[GB 32100—2015, 定义 3.5]

#### 3.1.3 

## 地址 address

具有地名的某一空间位置上自然或人文地理实体位置的结构化描述，是人、建（构）筑物及其他空间物体的定位实现。

注：改写 CH/Z 9010—2011，定义 3.5。

#### 3.1.4 

## 组织机构地址 organization address

企业、事业单位、机关、社会团体及其他依法成立的单位登记的从事生产经营活动的地址。

#### 3.1.5 

## 组织机构地面照片 organization pictures

用通用数码相机在地面实地拍摄的能真实清晰反映组织机构实体特征的照片。

#### 3.1.6 

## 组织机构定位点 organization point

建立在国家大地坐标系统之上，综合描述组织机构空间位置特征的地理定位点。

#### 3.1.7 

## 统一社会信用代码地理实体 unified social credit identifier geo-entity

现实世界中独立存在、从地理空间角度可以唯一性标识的组织机构，以几何图元为空间表达和存储的数据。

注：统一社会信用代码地理实体包括点状统一社会信用代码地理实体和面状统一社会信用代码地理实体。

#### 3.1.8 

## 统一社会信用代码地理信息 organization code geographic information

以统一社会信用代码为标识的组织机构的地理空间信息。

注：统一社会信用代码地理信息包括反映组织机构及其相关自然和人文要素的位置、形态和分布关系等基本信息，以及地名/地址和地理空间参照信息等其他信息。

#### 3.1.9 

## 全球导航卫星系统 global navigation satellite system; GNSS

泛指卫星导航定位系统。

注：GNSS 涵盖了在建和以后要建设的卫星导航系统，如美国的 GPS、中国的 COMPASS（北斗）、俄罗斯的 Glonass、欧洲的 Galileo，以及相关的增强系统，如美国的 WAAS（广域增强系统）、欧洲的 EGNOS（欧洲静地导航重叠系统）和日本的 MSAS（多功能运输卫星增强系统）等。

#### 3.1.10 

## 大地坐标系 geodetic coordinate system

以参考椭球面为基准面，用以表示地面点位置的参考系。

[GB/T 14911—2008, 定义 2.27]

#### 3.1.11 

## WGS-84 大地坐标系 geodetic coordinate system WGS-84

美国全球定位系统(GPS)采用的地心坐标系。

[GB/T 14911—2008, 定义 2.68]

#### 3.1.12 

## 1985 国家高程基准 national vertical datum 1985

1987 年颁布命名的，采用青岛水准原点和根据由青岛验潮站从 1952 年～1979 年的验潮数据确定的黄海平均海水面所定义的高程基准，其水准原点的起算高程为 72.260 m。

[GB/T 14911—2008, 定义 2.24]

#### 3.1.13 

地片 zone

有地名意义的区域。

[GB/T 30428.3—2016, 定义 3.7]

#### 3.1.14 

区片 block

城镇居民点内部的区域。

[GB/T 30428.3—2016, 定义 3.8]

#### 3.1.15 

## 兴趣点 point of interest: POI

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_496_144_531.jpg" alt="Image" width="3%" /></div>


关注点

具有地理标识作用的建筑（物）、单位、公共设施或店铺等。

[GB/T 30428.3—2016, 定义 3.9]

### 3.2 缩略语

表 1 所列缩略语适用于本文件。

<div style="text-align: center;">表 1 缩略语对照表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>缩略语</td><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>英文名称</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>CGCS2000</td><td style='text-align: center;'>2000 国家大地坐标系统</td><td style='text-align: center;'>China Geodetic Coordinate System 2000</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>DOM</td><td style='text-align: center;'>数字正射影像</td><td style='text-align: center;'>Digital Orthophoto Map</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>ODBC</td><td style='text-align: center;'>开放数据库互连</td><td style='text-align: center;'>Open Database Connectivity</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>UTC</td><td style='text-align: center;'>世界标准时间、国际协调时间</td><td style='text-align: center;'>Coordinated Universal Time</td><td style='text-align: center;'>法语：Temps Universel Coordonné，由于英文（CUT）和法文（TUC）的缩写不同，作为妥协，简称 UTC</td></tr></table>

## 4 参考系统及标识方法

### 4.1 坐标系统

统一社会信用代码地理信息外业采集应按 GB/T 18314—2009 的规定，其原始数据存储采用 WGS-84 大地坐标系。

分幅数据处理采用平面直角坐标。

提供的成果数据采用 CGCS2000。

### 4.2 时间系统

GNSS 测量记录采用 UTC，提供的成果应采用北京时间。

除 GNSS 数据测量、采集记录外的其他数据日期采用公历纪年，时间采用北京时间。

### 4.3 空间参考系统的标识方法

#### 4.3.1 大地经纬度

经纬度值采用“度”为单位，用双精度浮点数表示，至少保留6位小数。其数字记录格式为：

a）纬度(B):××.××××××N;

b）经度(L): ×××.×××××× E。

其中纬度缺省为北纬(N)，经度缺省为东经(E)。

#### 4.3.2 平面直角坐标

分幅数据处理时的平面控制主要采用高斯-克吕格投影平面直角坐标系，按 $ 6^{\circ} $ 分带，投影带的中央经线与赤道的交点向西平移500 km后的点为投影带坐标原点，平面直角坐标单位采用“m”，标识符X表示纵轴坐标，Y表示横轴坐标，我国范围内其数字记录格式为：

a） X 坐标：××××××××；

b） Y 坐标：××××××××××。

#### 4.3.3 高程

高程基准采用 1985 国家高程基准，高程系统为正常高。高程值单位为“m”，其数字记录格式为：高程（H）： $ \pm\times\times\times $ .×××，其中“ $ \pm $ ”缺省为正值。

## 5 技术指标

### 5.1 几何数据精度

野外测量单点实测精度达到亚米级。地物点对附近野外布控点的平面位置中误差，平地、丘陵地不超过为 $ \pm5\ m $ ，山地、高山地不超过为 $ \pm7.5\ m $ 。

参照国家测绘地理信息部门规定的基本比例尺地形图的精度标准，统一社会信用代码空间参照系统使用的1:10 000比例尺地形图上的定位要素位置测量值，允许图上的移动中误差在平原和丘陵地区不超过 $ \pm0.5~mm $ 。

### 5.2 属性精度

长度、距离、面积等采用米制单位。获取的定量属性值保留的小数位及数量单位应按第7章、第8章的要求，取值与地物实际属性相符。

## 6 统一社会信用代码地理信息数据及格式

### 6.1 基本内容

统一社会信用代码地理信息数据包括统一社会信用代码基础地理空间数据、统一社会信用代码扩展地理空间数据和统一社会信用代码地理属性数据。

### 6.2 数据组织与格式

#### 6.2.1 数据组织

统一社会信用代码地理信息数据按采集区域(一般以县级行政区为最小采集任务区域)、按不同几何特征类型(点状、面状)、分图层存储。

#### 6.2.2 空间数据格式

空间数据格式采用 GB/T 17798 规定的空间数据交换格式或公开格式。

#### 6.2.3 属性数据格式

统一社会信用代码地理属性信息见第7章规定，数据格式一般为支持ODBC数据访问协议的通用数据库格式。属性数据中的影像数据，一般采用位图格式、支持JPEG或JPEG 2000标准的数据格式，按文件组织，文件编号、命名及数据存储格式等见第8章规定。

## 7 采集内容和要求

### 7.1 统一社会信用代码基础地理空间数据

#### 7.1.1 概述

统一社会信用代码基础地理空间数据包括面状统一社会信用代码地理实体和点状统一社会信用代码地理实体。

#### 7.1.2 面状统一社会信用代码地理实体

面状统一社会信用代码地理实体数据指组织机构地址所处院落外轮廓多边形，按组织机构地理实体进行采集，当机构由多个相对封闭与独立的空间组成时，应完整采集，构建多边形集合。

#### 7.1.3 点状统一社会信用代码地理实体

点状统一社会信用代码地理实体数据指组织机构定位点。定位点应定位在机构地址所在位置，优先定位在机构的地址门（楼）牌所在位置、主要出入口或大门口的中心处。如果机构位置空间分散，可定位在机构的主要办公地（面积较大或人数较多）或主体建筑地址门（楼）牌所在位置或主要出入口处。遇有使用地址门（楼）牌所在位置、主要入口以及大门口的中心处均可的情况时，地址门（楼）牌所在位置优先于主要出入口或大门口的中心处。

机构定位点的大地坐标可通过两种方式采集取得：

a） GNSS 直接测量（GPS 直接测量，其精度应按照 GB/T 18314—2009 规定的 D 等以上精度要求指标进行测算、控制；COMPASS 直接测量，其精度可参照 GB/T 18314—2009 规定的 D 等以上精度要求指标进行测算、控制）；

b）在比例尺不小于1:10 000的地形图上获取平面坐标，在相应比例尺不小于1:50 000的地形图上人工量取高程坐标。

机构定位点数据的属性结构见表2。

<div style="text-align: center;">表 2 机构定位点数据属性结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>必选/可选</td><td style='text-align: center;'>属性项说明</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>宽度/字节</td><td style='text-align: center;'>值域或说明</td></tr><tr><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>组织机构识别标识码</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>20</td><td style='text-align: center;'>见 GB 32100—2015</td></tr><tr><td style='text-align: center;'>B</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>定位点纬度</td><td style='text-align: center;'>双精度浮点型</td><td style='text-align: center;'>16</td><td style='text-align: center;'>小数点后6位，如“33.971 064”，单位： $ ^{\circ} $</td></tr><tr><td style='text-align: center;'>L</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>定位点经度</td><td style='text-align: center;'>双精度浮点型</td><td style='text-align: center;'>16</td><td style='text-align: center;'>小数点后6位，如“109.284 591”，单位： $ ^{\circ} $</td></tr><tr><td style='text-align: center;'>H</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>定位点高程</td><td style='text-align: center;'>浮点型</td><td style='text-align: center;'>16</td><td style='text-align: center;'>小数点后3位，如“756.118”，单位：m</td></tr></table>

### 7.2 统一社会信用代码扩展地理空间数据

#### 7.2.1 概述

统一社会信用代码扩展地理空间数据包括组织机构所处村镇、所处地貌等。

#### 7.2.2 机构所处村镇

机构所处村镇指符合 GB/T 2260 规定的省、地区、县级城市和符合 GB/T 10114 规定的县级以下乡镇、行政村及自然村。

机构所处村镇名称指用于非城市地区的组织机构地址中缺少所处行政村级行政区域地名时填写，按机构所处村镇名称的规范全称。

机构所处村镇数据可直接从已有的中小比例尺地形图、专题数据等得到。

机构所处村镇的属性结构见表3。

<div style="text-align: center;">表 3 机构所处村镇的属性结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>必选/可选</td><td style='text-align: center;'>属性项说明</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>宽度/字节</td><td style='text-align: center;'>值域或说明</td></tr><tr><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>组织机构识别标识码</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>20</td><td style='text-align: center;'>见 GB 32100—2015</td></tr><tr><td style='text-align: center;'>村镇名称</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>所处村镇名称</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>64</td><td style='text-align: center;'>中文名称</td></tr></table>

#### 7.2.3 机构所处地貌

机构所处地貌指机构所处的地形地貌要素。

机构所处地貌数据通过已有的中小比例尺地形图和调查采集数据相结合得到，多种地形地貌并存时可取主要类型表示。

机构所处地貌的属性结构见表4。

<div style="text-align: center;">表 4 机构所处地貌的属性结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段名称</td><td style='text-align: center;'>必选/可选</td><td style='text-align: center;'>属性项说明</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>宽度/字节</td><td style='text-align: center;'>值域或说明</td></tr><tr><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>组织机构识别标识码</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>20</td><td style='text-align: center;'>见 GB 32100—2015</td></tr><tr><td style='text-align: center;'>地貌代码</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>所处地形类型</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>2</td><td style='text-align: center;'>见附录 A</td></tr></table>

### 7.3 统一社会信用代码地理属性信息

#### 7.3.1 概述

统一社会信用代码地理属性数据包括统一社会信用代码、组织机构地址、院落名称、院落类型、建筑建成年份、地址现状、地面照片等属性、属性信息见表5。

<div style="text-align: center;">表 5 统一社会信用代码地理属性信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>属性项名称</td><td style='text-align: center;'>必选/可选</td><td style='text-align: center;'>属性项说明</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>宽度/字节</td><td style='text-align: center;'>值域或说明</td></tr><tr><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>组织机构别标识码</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>20</td><td style='text-align: center;'>见GB 32100-2015</td></tr><tr><td style='text-align: center;'>组织机构地址</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>从事生产经营活动的地址描述</td><td style='text-align: center;'>文本型</td><td style='text-align: center;'>255</td><td style='text-align: center;'>中文地址，如：“甘肃庆阳市西峰区长庆北路142号”</td></tr><tr><td style='text-align: center;'>院落名称</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>地址所在院落的名称</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>100</td><td style='text-align: center;'>中文名称，如：“蓝山小区”“长业大厦”</td></tr><tr><td style='text-align: center;'>院落类型</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>按照院落空间单元根据功能和权属分类</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>4</td><td style='text-align: center;'>属性值定义见7.3.4，如：“A”</td></tr><tr><td style='text-align: center;'>建筑建成年份</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>机构主建筑（区）的实际竣工年份</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>16</td><td style='text-align: center;'>如：“1980”“1949前”</td></tr><tr><td style='text-align: center;'>地址现状</td><td style='text-align: center;'>必选</td><td style='text-align: center;'>组织机构地址的实际利用情况</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>8</td><td style='text-align: center;'>代码、属性值定义见7.3.6</td></tr><tr><td style='text-align: center;'>地面照片</td><td style='text-align: center;'>可选</td><td style='text-align: center;'>用通用数码相机在地面实地拍摄的能真实清晰反映组织机构实体特征的照片</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>属性值定义见8.6.4</td></tr></table>

#### 7.3.2 组织机构地址

##### 7.3.2.1 地址描述

组织机构地址采用名称描述，按照附录 B 的优先级规范建立完整的地名/地址数据。

##### 7.3.2.2 地址组成

###### 7.3.2.2.1 行政区域地名

行政区域地名按照 GB/T 23705—2009 执行。

###### 7.3.2.2.2 地片与区片地名

地片与区片地名应包含地片名称、区片名称的信息。地片与区片的基本地点名称应为标准地名全称，是描述地片、区片的最小单元。地片与区片地名描述要符合以下规则：

a）地片与区片名称应使用标准名称全称，避免使用简称、别名；

b）当地片与区片同时明确的情况下，采用“地片（区片）”的形式表达。

###### 7.3.2.2.3 街巷地名

街巷地名应包含有地名标牌的街巷，名称应为街牌和巷牌标示的汉字名称，是描述街巷地名信息的最小单元。街巷地名应使用标准名称全称，避免使用简称、别名。

###### 7.3.2.2.4 门(楼)牌地址

门(楼)牌地址包括门牌地址和楼牌地址：

a）门牌地址的基本地点名称应为：[顺序号|号(院)];

b）楼牌地址的基本地点名称应为：[顺序号|号楼(栋)]。

门（楼）牌地址应使用标准名称全称，避免使用简称、别名。

门牌与楼牌地址应按基本地点名称优先级顺序排列。

###### 7.3.2.2.5 POI 与标识物地址

POI 与标识物地址应包括以下内容：

a）具有地名意义的自然地物，包括湖泊、山峰、河流等；

b）具有地名意义的单位与院落，包括医院、学校、单位、宗教设施（佛庙宇、道观、教堂、清真寺）等；

c) 具有地名意义的纪念地与建筑物，包括建筑物、广场、体育设施、公园绿地、纪念地、名胜古迹等；

d）具有地名意义的交通附属设施，包括桥梁、道路环岛、交通站场等；

e）具有地名意义的其他设施，包括闸、坝、微波塔、通信站、水塔等。

标识物地址的基本地点名称应为描述该标识物的标准名称，应能唯一标识特定地点。标识物地址的基本地点名称应使用标准名称全称，避免使用简称、别名。

##### 7.3.2.3 地址表达

地址表达包括方位描述和地址描述。

方位描述采用 CJ/T 215—2005 规定的方位描述格式。

地址采用附录 B 中各级基本地点信息描述，并符合以下组合规则：

a） $$ （1级名称）|（2级名称）|（3级名称）|（4级名称/5级名称/6级名称）|（7级名称）|8级名称/9级名称 $$ ；

b） $$ （1级名称）|（2级名称）|（3级名称）|（4级名称/5级名称/6级名称）|（7级名称）|8级名称/9级名称|（补充说明） $$ ；

c） $$ （1级名称）|（2级名称）|（3级名称）|（4级名称/5级名称/6级名称）|（7级名称）|10级名称 $$ ；

d） $$ （1级名称）|（2级名称）|（3级名称）|（4级名称/5级名称/6级名称）|（7级名称）|10级名称|（方位）|（补充说明） $$ ；

e） $$ （1级名称）|（2级名称）|（3级名称）|（4级名称/5级名称/6级名称）|（7级名称）|10级名称|（方位）|（10级名称）|（方位）|（补充说明） $$ 。

地点描述能具体到门（楼）牌地址的优先考虑具体到门（楼）牌地址，无法用门楼牌地址表示清楚的考虑使用标识物地址或POI地址表示。如果以上组合还不能清楚描述地点，再考虑使用标识物、方位组合说明。

补充说明包含对地址的补充性说明，包括支号、数量性说明等。

支号一般用于区分同一建筑物的组织机构。

数量性说明一般出现在地址建设不太规范的地区，例如“××南500米”，这种数量性说明仅作为定位参考，不作为定位依据。

##### 7.3.2.4 地址区域编码

组织机构地址区域的唯一标识码，由县级以上行政区域地名、乡镇级行政区域地名、类别标识码和行政村/小区/道路街巷编码四部分组成（如图1所示）。其中，县级及县级以上行政区域地名编码按照GB/T2260的规定执行，乡镇级行政区域地名的编制规则按GB/T10114的规定执行；类别标识码用于标识后三位表示的是非城市地区的行政村级行政区域地名或城市地区的居民小区名或道路街巷名，0表示非城市地区的行政村级行政区域地名，1表示城市地区的道路、街巷名，2表示城市地区的小区名。

其中，非城市地区的行政村级行政区域地名的编码采用自然顺序编号方式，即：

a）凡民政部门确认的村级单位，村级代码为001～399；

b）民政部门未确认的园区、工矿区、农场等类似村级单位，村级代码为400～599（498、598除外）。

城市地区道路、街巷的代码在本行政区域内按照起点由东向西和由南向北的顺序编号，参照GB/T21381—2008的规定执行；居民小区的代码在本行政区域内按照起点由东向西和由南向北的顺序编号，居民小区代码为001～999。在城市地区道路、街巷和居民小区都存在的情况下，按照基本地点名称优先级优先采用道路、街巷名编码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_323_417_879_592.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 1 要素模型编码结构示意图</div>


#### 7.3.3 院落名称

院落名称指地址所在院落的名称，例如“**小区”“**大厦”等，当组织机构分布于不同的院落单元时，选取主要的或最大的院落名称作为组织机构院落名称。

#### 7.3.4 院落类型

院落类型为院落空间单元根据功能和权属划分的类型，其代码、属性值及属性值定义见附录C。

#### 7.3.5 建筑建成年份

建筑建成年份指组织机构建筑物(多个建筑物时,以主要建筑物为采集对象)的实际竣工年份。拆除翻建的,按翻建竣工的年份计算。扩建的房屋,面积超原房屋面积的,按扩建竣工年份计算,未超过的按原房屋竣工年份填写。准确到年份,新中国成立前无法确定竣工年份的建筑建成年份标注“1949年前”。

#### 7.3.6 地址现状

地址现状指组织机构地址的实际利用情况。分“使用（OC）、废弃（AB）、不一致（IN）、无法确定（UN）”四类。“使用”表明注册该地址的机构实际使用该地址，并在进行生产经营。“废弃”表明该地址已经废弃，无其他组织机构在使用。“不一致”表明该地址虽然未废弃，但实际使用机构与登记使用机构不一致，登记机构并未实际使用该地址。“无法确定”表明无法确定该地址的实际利用现状。

## 8 统一社会信用代码地理信息采集与更新技术

### 8.1 技术流程

统一社会信用代码地理信息采集与更新优先采用航空摄影测量结合 GNSS 人工外业测量进行，若测区内采集或更新的组织机构数量较少时，也可以单独采用 GNSS 人工外业测量进行（采用 GPS 人工外业测量应按照 GB/T 18314—2009 和 GB/T 13977—2012 执行；采用 COMPASS 人工外业测量可参照 GB/T 18314—2009 和 GB/T 13977—2012 执行）。航空摄影测量采集统一社会信用代码地理信息应按照 GB 50167 执行。统一社会信用代码地理信息采集作业流程如图 2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_235_192_936_958.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">图 2 统一社会信用代码地理信息采集作业流程图</div>


### 8.2 资料收集

统一社会信用代码地理信息资料收集应包括以下内容和要求：

a）测区影像资料：测区最近高分辨率影像（航片或卫片）资料，用于数据采集或精度检查；

b）基础地理信息数据：1：10 000 或 1：5 000 或更大比例尺的地形图，用于数据采集或精度检查；1：50 000、1：100 000、1：250 000 地形图，用于制作工作计划和导航的中小比例尺地图资料；

c）统一社会信用代码数据：测区最近统一社会信用代码数据资料，用于确定采集对象及其属性；

d）其他专题资料：收集民政、工商、自然资源、住建、交通、卫生、教育、农业、规划等部门数据资料；

e）测区内控制点资料的收集按照按 GB/T 18314—2009 要求执行。

### 8.3 数据整合处理

将遥感影像进行正射纠正，形成正射影像。遥感影像正射纠正制作应按照 GB/T 33182—2016 和 GB/T 33179—2016 执行。

将专题数据与基础地理信息数据整合到正射影像上，形成统一社会信用代码地理信息采集的基础底图数据。

### 8.4 内业采集

内业采集流程如图 3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_275_286_923_1000.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 3 内业采集流程图</div>


内业采集采用人工判读与勾绘方法，对测区范围采取多个作业员分幅进行，按照组织机构地理要素的类型分别形成点图层、面图层。

统一社会信用代码地理信息采集基于组织机构地理实体进行，不考虑拓扑关系，即不同的组织机构地理实体在空间范围上可以具有重叠关系，不影响各自独立采集。

统一社会信用代码地理实体数据模型应符合 CH/Z 9010—2011 的规定。组织机构外轮廓多边形数据形成实体面图层，组织机构定位点数据形成实体点图层。

作业中可以利用基础地理信息数据中“居民地及设施”和“交通及设施”两大类中有关定位点、标注点数据作为参考。

县级及以上等级行政界线及行政区划，可直接从1:10 000、1:50 000基础地理信息地形图中提取；乡、镇界利用收集的其他资料进行采集；在元数据中应明确说明沿用界线数据的数据源。

### 8.5 外业底图制作

用正射影像、专题空间信息、内业采集信息，对矢量数据进行符号配置，符号配置按照GB/T 20257.2—2017执行。有选择性的对部门名称、属性进行标注，形成外业底图，用于外业采集与核

查。外业底图制作流程如图 4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_336_227_838_903.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图 4 外业底图制作流程图</div>


### 8.6 外业数据采集与属性调查

#### 8.6.1 调查流程

外业数据采集与属性调查流程如图 5 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_192_913_825.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 5 外业数据采集与属性调查流程图</div>


#### 8.6.2 基本要求

开展外业数据采集与属性调查的基本要求如下：

a）人员：充分考虑任务区域的工作量，根据区域内的地理环境、交通条件和组织机构的分布情况，合理编制外业工作组。高山、荒漠及其他困难地区，不得单人作业，每个小组至少需配备2名作业人员和1名司机。到达任务区后应及时与当地政府相关部门取得联系，了解当地的情况，并做好安全保障工作。

b）设备：根据具体任务要求，配备生产需要设备，包括交通工具（车辆）、通讯设备、笔记本电脑、导航定位设备、相机、望远镜等；具备条件的，应采用数字调查系统。高山、荒漠及其他困难地区，由于受交通状况和部分区域通讯困难限制，还需配备卫星电话、大功率电台等设备，以保障生产安全。

c) 采集工作计划：在 a)、b) 的基础上，根据外业任务书要求，在小比例尺图上制定每天的外业采集计划，人员分布，并形成每天的外业路线计划草图。同时，外业路线还要考虑环境、天气情况，尽量避免遮挡或雨雪天作业情况。

d）外业轨迹：外业采集工作中，应开启 GNSS 定位设备，记录外业工作行进轨迹，作为外业采集的工作依据和元数据基本来源。

e）外业工作中应对行进线路两侧的组织机构要素进行核对，并观察沿途周边的地表特征，遇需要重点关注或特殊的组织机构要素时，应及时开展地面照片数据采集工作。

#### 8.6.3 生产内容

外业数据采集与属性调查的生产内容规定如下：

a） 对内业采集工作中无法确定的组织机构要素边界、位置进行实地调查；

b） 对内业工作中专业资料内容不全的组织机构要素属性（如院落名称、地址现状等）进行采集调查；

c） 对内业解译的组织机构要素边界和属性，实地进行抽样调查核对。

#### 8.6.4 新增或变化的组织机构要素补测补调

对于实地新增或发生变化的组织机构要素，应按下列要求进行外业补调或补测：

a）新增或变化的图斑或要素，在底图上可以直接定位的，采用图上标绘和图外注记的形式进行调查；

b）当底图上无法对新增或变化的图斑或要素进行准确定位时，采用满足精度要求的测量手段和测量设备进行实地定位，采集变化范围。

#### 8.6.5 地面照片数据采集

##### 8.6.5.1 地面照片数据采集要求

地面照片数据采集要求如下：

a）地面照片与组织机构为一一对应关系，即一张地面照片原则上只对应一个组织机构实例；

b）考虑到清晰度与数据存储的要求，地面照片总像素数量应在200万像素以上，1000万像素以下；

c）拍摄点位置定位精度一般应控制在15 m以内。照片方位角的精度应在5°以内。

##### 8.6.5.2 地面照片数据文件命名要求

地面照片文件命名按以下规则生成：

a）一般由照片标识符、拍摄时间、拍摄点经度、拍摄点纬度、照片方位角五部分组成（地面照片命名规则如图6所示），共32位。其中，

b）照片标识符为“OP”，表示该文件为组织机构地面照片文件；

c）拍摄时间 14 位，使用图 6 中拍摄时间格式，记录到秒；

d）拍摄点经度7位，按度分秒记录；

e）拍摄点纬度6位，按度分秒记录；

f）照片方位角3位，记录到度；

g）以上不足部分用0填充。

<div style="text-align: center;"><img src="imgs/img_in_image_box_196_1090_982_1266.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 6 地面照片命名规则</div>


##### 8.6.5.3 地面照片属性定义及采集

地面照片属性定义及采集要求见附录D。

##### 8.6.5.4 地面照片属性采集方法

地面照片应采用以下方法进行属性采集：

a） 方法一：使用支持自动记录相机姿态参数和相机成像参数信息的一体化外业调绘核查系统，其他信息通过人工交互方式输入并同步记入数据库；

b）方法二：使用支持在照片 EXIF 信息中自动记录相机姿态参数和相机成像参数信息的照相机，其他属性信息由人工方式输入并同步记入数据库；

c) 方法三：若使用的相机不能自动记录相机姿态参数，可同时携带事先做好相机时间校准的GNSS接收机记录采集者的移动轨迹，拍摄照片同时记录其他属性信息。事后内业读取GNSS记录和地面照片EXIF信息中的拍摄时间，通过时间同步，把相应的位置信息挂接到地面照片属性上。

<div style="text-align: center;"><img src="imgs/img_in_image_box_87_455_123_494.jpg" alt="Image" width="3%" /></div>


## 9 质量要求与符合性检查

### 9.1 概述

应对采集或更新的统一社会信用代码地理信息进行质量检查，包括基本质量要求与符合性检查、几何数据质量检查、属性数据质量检查以及组织与实施过程质量检查。

### 9.2 基本质量要求与符合性检查

基本质量要求与符合性检查的内容及要求如下：

a）原始资料的质量：检查原始资料的正确性、现势性、权威性和完整性；

b）设备的质量：设备性能、参数的适用性、可靠性和输出的正确性；

c) 元数据的质量: 对元数据进行逐项检查, 看是否符合规定要求;

d）文档的质量：检查文档填写内容是否完整，是否符合规定要求；

e） 数据质量：数据的精度、格式、单位与完整性检查；

f) 产品归档检查：检查各种数据资料、图文资料是否齐全；检查存储数据的介质和规格是否符合要求；检查备份的数量；检查数据是否可用，文档组织、文件命名是否符合规定要求。

### 9.3 几何数据质量检查

几何数据质量检查的内容及要求如下：

a）精度检查：检查数学基础、平面精度是否满足要求；分幅数据检查与相邻图幅是否接边、有无缝隙；

b）图形质量检查：检查线划的光滑、粗细、清晰情况是否满足要求；要素间的关系是否合理，有无空间逻辑性矛盾；地图数据中符号配置、界面整饬、注记是否规范。

### 9.4 属性数据质量检查

属性数据质量检查的内容及要求如下：

a）属性结构检查：检查每一个属性表，检查属性项的名称、类型、长度、顺序是否符合规定要求，有无遗漏；检查属性值是否正确；

b）语义质量检查：将数据本身或者这个数据的抽样数据与现实数据相比或通过检查数据集的成果是否与规格书、设计书中所定义的标准相符合，来判断这个数据集的质量。

### 9.5 组织与实施过程质量检查

组织与实施过程质量检查的内容及要求如下：

a） 组织过程质量检查：对技术设计书的编制、审核、审批程序进行检查；

b）实施过程质量检查：对各工序所用主要仪器设备的检定情况进行检查；技术问题处理情况进行检查。

附录 A

(规范性附录)

组织机构所处地貌代码

组织机构所处地貌代码见表 A.1。

<div style="text-align: center;">表 A.1 组织机构所处地貌代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>属性值</td><td style='text-align: center;'>属性值定义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>山地</td><td style='text-align: center;'>是一种具有一定坡度、较大高差（相对高差大于200m）又互相连绵、突出于平原或台地之上的正地貌形态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>丘陵</td><td style='text-align: center;'>山坡平缓、山顶浑圆、高低起伏、连绵不断的低矮隆起高地</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>平原</td><td style='text-align: center;'>陆地上海拔高度较低，地表起伏平缓的开阔平地。指地面较平整（一般平均坡度小于7°），最高点一般在边缘，内部一般无坡度大于10°，高差大于30m的坡坎形态</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>草原</td><td style='text-align: center;'>中、低纬度半干旱、干旱环境下形成的以草本植物覆盖为主的地理景观</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>沙漠</td><td style='text-align: center;'>植被稀疏，地表径流少，表层干燥，裸露物以沙质为主的地貌形态。如各种沙丘，风蚀劣地等</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>戈壁</td><td style='text-align: center;'>地表布满大小砾石、石块的荒漠</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>湿地</td><td style='text-align: center;'>天然的或人工的，永久的或间歇性的沼泽地、泥炭地、水域地带，带有静止或流动、淡水或半咸水及咸水水体，包括低潮时水深不超过6m的海域</td></tr><tr><td style='text-align: center;'>90</td><td style='text-align: center;'>其他</td><td style='text-align: center;'>山地、丘陵、平原、草原、沙漠、戈壁、湿地之外的地貌</td></tr></table>

附录 B

(规范性附录)

基本地点名称优先级

基本地点名称优先级见表B.1。

<div style="text-align: center;">表 B.1 基本地点名称优先级</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>级别</td><td style='text-align: center;'>基本地点名称</td><td style='text-align: center;'>级别</td><td style='text-align: center;'>基本地点名称</td></tr><tr><td style='text-align: center;'>1级</td><td style='text-align: center;'>省、自治区、直辖市、特别行政区</td><td style='text-align: center;'>6级</td><td style='text-align: center;'>道路、街巷</td></tr><tr><td style='text-align: center;'>2级</td><td style='text-align: center;'>市、地区、自治州、盟</td><td style='text-align: center;'>7级</td><td style='text-align: center;'>地片、区片</td></tr><tr><td style='text-align: center;'>3级</td><td style='text-align: center;'>县、自治县、县级市、旗、自治旗、市辖区、林区、特区</td><td style='text-align: center;'>8级</td><td style='text-align: center;'>门牌号</td></tr><tr><td style='text-align: center;'>4级</td><td style='text-align: center;'>乡、民族乡、苏木、镇、街道、政企合一单位</td><td style='text-align: center;'>9级</td><td style='text-align: center;'>楼牌号</td></tr><tr><td style='text-align: center;'>5级</td><td style='text-align: center;'>村、社区、屯</td><td style='text-align: center;'>10级</td><td style='text-align: center;'>POI、标识物</td></tr></table>

附录 C

(规范性附录)

组织机构院落分类及代码

组织机构院落分类及代码见表C.1。

<div style="text-align: center;">表 C.1 组织机构院落分类及代码</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>代码</td><td style='text-align: center;'>属性值</td><td style='text-align: center;'>属性值定义</td></tr><tr><td style='text-align: center;'>R</td><td style='text-align: center;'>居住区</td><td style='text-align: center;'>被城市道路或自然分界线所围合，并与居住人口规模相对应，配建有公共服务设施的居住生活聚居区</td></tr><tr><td style='text-align: center;'>A</td><td style='text-align: center;'>公共管理与公共服务区</td><td style='text-align: center;'>行政、文化、教育、体育、卫生等机构和设施的区域（包括党政机关、社会团体、事业单位、高校、科研事业单位、图书、展览等公共文化区域、体育场馆、医疗、保健、卫生防疫、社会福利、文物古迹、外事机构及宗教活动场所），不包括居住用地中的服务设施区域</td></tr><tr><td style='text-align: center;'>B</td><td style='text-align: center;'>商业服务业区</td><td style='text-align: center;'>商业、商务、娱乐康体、公用设施营业网点（电信、邮政、加油、加气站）等设施区域，不包含居住区中的服务设施用地</td></tr><tr><td style='text-align: center;'>M</td><td style='text-align: center;'>工业区</td><td style='text-align: center;'>工矿企业的生产车间、库房及其附属设施区域，包括专用铁路、码头和附属道路、停车场，不包含露天矿区域</td></tr><tr><td style='text-align: center;'>W</td><td style='text-align: center;'>物流仓储区</td><td style='text-align: center;'>物资储备、中转、配送等区域，包括附属道路、停车场及货运公司车队的站场等区域</td></tr><tr><td style='text-align: center;'>U</td><td style='text-align: center;'>公用设施区</td><td style='text-align: center;'>供应（供水、供电、供燃气、供热等）、环境（雨水、污水、固体废物处理等环境保护设施及附属设施区域）、安全（消防、防洪等公共设施及其附属区域）、以及施工、养护、维修等设施区域</td></tr><tr><td style='text-align: center;'>Q</td><td style='text-align: center;'>其他区</td><td style='text-align: center;'>居住区、公共管理与公共服务区、商业服务业区、工业区、物流仓储区以及公用设施区之外的区域</td></tr></table>

## 附录 D

(规范性附录)

地面照片属性定义及采集要求

地面照片属性定义及采集要求见表 D.1。

<div style="text-align: center;">表 D.1 地面照片属性定义及采集要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>属性值</td><td style='text-align: center;'>获取说明</td><td style='text-align: center;'>采集要求</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>统一社会信用代码</td><td style='text-align: center;'>组织机构识别标识码</td><td style='text-align: center;'>见GB 32100-2015</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>地面照片标识符</td><td style='text-align: center;'>按规则生成</td><td style='text-align: center;'>标识符:“OP”</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>拍摄时间</td><td style='text-align: center;'>相机自动记录</td><td style='text-align: center;'>采用北京时间，格式为YYYY-MM-DDTHH:MM:SS；从照片EXIF信息的DateTimeOriginal标记中读取，如：2015-08-23T09:55:32</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>拍摄点经度</td><td style='text-align: center;'>部分相机自动记录；也可通过与GNSS设备同步提取</td><td style='text-align: center;'>相机自动记录模式下，从照片EXIF信息的经度标记（GPS测量为GPSLongitude）中读取；采用WGS84坐标系</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>拍摄点纬度</td><td style='text-align: center;'>部分相机自动记录；也可通过与GNSS设备同步提取</td><td style='text-align: center;'>相机自动记录模式下，从照片EXIF信息的纬度标记（GPS测量为GPSLatitude）中读取；采用WGS84坐标系</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>位置定位平面精度水平</td><td style='text-align: center;'>部分相机自动记录；也可通过与GNSS设备同步提取</td><td style='text-align: center;'>相机自动记录模式下，从照片EXIF信息的位置定位平面精度标记（GPS测量为GPSDOP）中读取；无法获取时可以不填写</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>拍摄点高程</td><td style='text-align: center;'>部分相机自动记录；也可通过与GNSS设备同步提取</td><td style='text-align: center;'>相机自动记录模式下，从照片EXIF信息的高程标记（GPS测量为GPSAltitude）中读取；为大地高</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>定位方法</td><td style='text-align: center;'>部分相机自动记录；也可通过与GNSS设备同步提取。非卫星定位时填写，手机定位填写“Phone”，无线网定位填写“Wifi”，不确定的填写“Unknown”</td><td style='text-align: center;'>相机自动记录模式下，从照片EXIF信息的定位方法标记（GPS测量为GPSMeasureMode）中读取</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>定位时观测到的卫星数量</td><td style='text-align: center;'>部分相机自动记录；也可通过与GNSS设备同步提取。卫星定位时填写</td><td style='text-align: center;'>相机自动记录模式下，从照片EXIF信息的定位时观测到的卫星数量标记（GPS测量为GPSSatellite）中读取；无法获取时可以不确定</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>照片方位角</td><td style='text-align: center;'>部分相机自动记录</td><td style='text-align: center;'>从照片EXIF信息的照片方位角标记（GPS测量为GPSImgDirection）中读取</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>照片方位角的参照方向</td><td style='text-align: center;'>部分相机自动记录，字母G表示磁北；字母T表示真北。</td><td style='text-align: center;'>从照片EXIF信息的照片方位角的参照方向标记（GPS测量为GPSImgDirectionRef）中读取</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>照片方位角的准确程度</td><td style='text-align: center;'>部分相机或一体化系统自动记录</td><td style='text-align: center;'>无法获取时可以不确定</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>拍摄距离</td><td style='text-align: center;'>估测填写</td><td style='text-align: center;'>当距离被拍摄对象在200m以上时，需填写，单位为m</td></tr></table>

<div style="text-align: center;">表 D.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>属性值</td><td style='text-align: center;'>获取说明</td><td style='text-align: center;'>采集要求</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>相机俯仰角</td><td style='text-align: center;'>部分相机或一体化系统自动记录</td><td style='text-align: center;'>当镜头俯仰角大于 $ 10^{\circ} $ 时需要填写</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>相机横滚角</td><td style='text-align: center;'>部分相机或一体化系统自动记录</td><td style='text-align: center;'>当镜头横滚角大于 $ 10^{\circ} $ 时需要填写</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>样点地理环境描述</td><td style='text-align: center;'>需人工填写</td><td style='text-align: center;'>对样点处被拍摄范围的地理环境进行直观、简要说明，起到准确传递照片中拍摄对象包含的信息即可。可包括所在地地名或实体名（尽可能贴近样点小范围的本地地名，如松果岭、萌水村）、周围情况（如位于居民区、厂区、公园、河滩、山坡、田野、高速公路、国道等）、样点类型（如麦田、温室大棚）以及对样点的直观描述（如废弃建筑区、水产养殖区等）</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>拍摄者</td><td style='text-align: center;'>需人工填写</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>35 mm等效焦距</td><td style='text-align: center;'>相机自动记录</td><td style='text-align: center;'>从照片EXIF信息的FocalLengthIn35mmFilm标记中读取</td></tr></table>

## 参考文献

[1] GB/T 14911—2008 测绘基本术语

[2] GB 17733—2008 地名标志

[3] GB/T 18521—2001 地名分类与类别代码编码规则

[4] GB/T 20091—2006 组织机构类型

[5] GB/T 21381—2008 交通管理地理信息实体标识编码规则 城市道路

[6] GB/T 30170—2013 地理信息 基于坐标的空间参照

[7] GB/T 30428.3—2016 数字化城市管理信息系统 第3部分：地理编码

[8] GB/T 31286—2014 全国组织机构代码与名称

[9] 北京市人民政府令 第 254 号. 北京市门楼牌管理办法. 2014.05.21.

[10] 深圳市人民政府令 第226号.深圳市门楼牌管理办法.2011.01.30.

[11] 成都市人民政府令 第 119 号. 成都市门(楼)牌管理办法. 2005.08.16.