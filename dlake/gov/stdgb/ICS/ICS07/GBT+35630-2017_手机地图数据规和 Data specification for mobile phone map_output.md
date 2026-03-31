

# 中华人民共和国国家标准

GB/T 35630—2017

# 手机地图数据规范

# Data specification for mobile phone map

2017-12-29 发布

2018-07-01 实施

## 目次

前言 …… III    
引言 …… IV    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 缩略语与符号 …… 1    
4.1 缩略语 …… 1    
4.2 符号 …… 2    
5 数据描述与构成 …… 2    
6 数据要求 …… 3    
6.1 坐标系 …… 3    
6.2 安全要求 …… 3    
6.3 数据内容 …… 3    
6.4 数据分层 …… 9    
6.5 属性结构 …… 10    
7 质量要求 …… 10    
7.1 POI 数据 …… 10    
7.2 路网数据 …… 10    
7.3 门址数据 …… 11    
7.4 公交数据 …… 11    
7.5 背景数据 …… 12    
7.6 实时交通数据 …… 12    
7.7 空间定位数据 …… 13    
7.8 室内地图数据 …… 13    
8 元数据 …… 13    
附录 A（规范性附录） 数据层表 …… 14    
附录 B（规范性附录） 基础属性表 …… 16    
附录 C（规范性附录） 元数据结构表 …… 24    
参考文献 …… 25

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由国家测绘地理信息局提出。

本标准由全国地理信息标准化技术委员会(SAC/TC 230)归口。

本标准起草单位:高德软件有限公司、国家基础地理信息中心、北京四维图新科技股份有限公司、天地图有限公司、中国测绘科学研究院。

本标准主要起草人：肖成才、李瑞方、杨明、王丹、孙旭、李迎、方晨兵、邓立娟、吕春艳、刘英爽、张红平、毛曦、吕艳玲、邢斌、唐德瑾、刘丽芬。

## 引言

随着互联网基础设施的完善和智能手机的普及，手机地图逐渐被广大用户所使用，在用户和产业规模不断壮大的背景下，社会各界对手机地图的需求日益迫切。手机地图由车载导航产品和互联网地图衍化而来，相比两者，手机地图更便携和个人化，并且可以提供实时在线的深度信息查询、多模式路线规划与引导、室内外定位等差异化服务。

本标准从手机地图核心功能所需的数据支撑出发，重点对兴趣点深度信息、人行路网、公交、室内地图、空间定位等手机地图特征数据内容和要求进行规定，同时引用现有标准对兴趣点基础信息、车行路网、门址等通用数据进行说明，保证了数据规范的结构完整性及与相关标准的一致性，便于理解、执行。影像数据在手机地图中更多起到增强地图可读性作用，属于非必要数据，本标准中不对此类数据作出要求。

# 手机地图数据规范

## 1 范围

本标准规定了手机地图数据的内容及要求，包括数据描述与构成、数据要求、质量要求和元数据。

本标准适用于手机地图数据的生产、共享以及应用服务的设计与开发。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB 20263—2006 导航电子地图安全处理技术基本要求

GB/T 20267—2006 车载导航电子地图产品规范

GB/T 35639—2017 地址模型

GB/T 35648—2017 地理信息兴趣点分类与编码

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 电子地图 electronic map

应用电子学和计算机技术建立起来的视屏显示地图。

[GB/T 16820—1997, 定义 7.76]

### 3.2 

## 手机地图 mobile phone map

以手机为载体提供电子地图服务的产品。

注：手机地图一般以电子地图数据和空间定位数据为核心数据资源，能够实现信息查询、地图浏览、空间定位、路线规划和引导等核心功能。

### 3.3 

## 兴趣点 point of interest: POI

能够标识特定服务与活动的点位。

[GB/T 35648—2017, 定义 3.1]

### 3.4 

## 兴趣面 area of interest: AOI

能够标识特定服务与活动的区域。

## 4 缩略语与符号

### 4.1 缩略语

下列缩略语适用于本文件。

CellID: 基站小区代码(Cell tower ID)

GDF: 地理数据文件 (Geographic Data Files)

GNSS: 全球卫星导航系统 (Global Navigation Satellite System)

GPS: 全球定位系统(Global Positioning System)

LAC: 地区区域码 (Location Area Code)

MCC: 移动国家码 (Mobile Country Code)

MNC: 移动网络码 (Mobile Network Code)

MAC:介质访问控制(Media Access Control)

UML: 统一建模语言 (Unified Modeling Language)

WiFi: 无线路由器(Wireless Fidelity)

### 4.2 符号

本标准出现的图用 UML 静态结构图表示，图 1 说明本标准使用的 UML 符号。

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_612_865_984.jpg" alt="Image" width="46%" /></div>


说明：

1——关联：表示一种拥有的关系，它使一个类知道另一个类的属性和方法。

2——继承：表示一般与特殊的关系，它指定了子类如何特化父类的所有特征和行为。

3——聚合：表示整体与部分的关系，且部分可以离开整体而单独存在。

<div style="text-align: center;">图 1 UML 中的关系符号</div>


## 5 数据描述与构成

5.1 手机地图数据是以点、线、面形式表达地理信息要素的矢量数据集。

5.2 手机地图数据包括 POI、路网、门址、公交、背景、实时交通、空间定位和室内地图 8 大类要素内容，应能够支撑手机地图浏览、实时信息检索、室内外定位及多模式路线规划与引导等手机地图核心功能实现。

5.3 手机地图数据应由矢量数据和元数据构成，如图 2 所示：

a）矢量数据存储8大类要素的空间坐标、属性信息和相互关系等。

b）元数据记录关于矢量数据的描述。

<div style="text-align: center;"><img src="imgs/img_in_image_box_154_204_1048_877.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2 手机地图数据构成</div>


## 6 数据要求

### 6.1 坐标系

符合 GB 20263—2006 中第 4 章要求的 WGS 84 坐标系。

### 6.2 安全要求

6.2.1 手机地图数据安全处理应按照 GB 20263—2006 执行。

6.2.2 手机地图数据审查应严格遵照国家及行业相关法律法规执行。

### 6.3 数据内容

#### 6.3.1 POI 数据

##### 6.3.1.1 概述

POI 数据包括 POI 基础信息和 POI 深度信息。POI 基础信息主要表达 POI 的地理实体特征，几何形状为点；POI 深度信息主要表达地理实体的商业和社会属性。

##### 6.3.1.2 POI 基础信息

包括 POI 的名称、电话、地址、类别、位置和所属行政区划。

POI 类别按照 GB/T 35648—2017 中附录 A 执行。

##### 6.3.1.3 POI 深度信息

POI 深度信息应按行业细分，各行业可选择包括图片、价格、简介、时间、评论、评分等通用深度信息：

a）图片：POI 的外景图、内部图、产品图等。

b) 价格: POI 的服务价格。

c） 简介：描述 POI 的特点或服务内容。

d） 时间：POI 的对外服务时间。

e）评论：用户对 POI 提供的服务、产品、环境等的体验感受和意见反馈，帮助其他用户决策参考。

f）评分：用户对 POI 的综合评分或分项评分。

#### 6.3.2 路网数据

##### 6.3.2.1 概述

路网数据包括车行道路、车行道路结点、交通规制、道路附属设施、人行道路与人行道路结点等信息，内容构成如图3所示。车行道路和人行道路几何形状为线；车行道路结点、交通规制、道路附属设施、人行道路结点几何形状为点。

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_754_1017_1324.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3 路网数据构成</div>


##### 6.3.2.2 车行道路

按照 GB/T 20267—2006 中 4.1.1 执行。

##### 6.3.2.3 车行道路结点

按照 GB/T 20267—2006 中 4.1.2 执行。

##### 6.3.2.4 交通规制

按照 GB/T 20267—2006 中 4.1.2.4 执行。

##### 6.3.2.5 道路附属设施

包括电子眼、交通警示牌等。

##### 6.3.2.6 人行道路

包括不可通车的小区、景点内部路等人行路以及人行横道、过街天桥、地下通道、地铁通道、扶梯、直梯、阶梯、空中通道、建筑物穿越通道等人行设施。

##### 6.3.2.7 人行道路结点

包括人行道路的连接信息。

#### 6.3.3 门址数据

门址数据内容应符合 GB/T 35639—2017 中第 5 章、第 6 章要求。

#### 6.3.4 公交数据

##### 6.3.4.1 概述

公交数据包括公交线路、公交站点和公交事件信息，内容构成如图4所示。公交线路几何形状为线；公交站点几何形状为点。

<div style="text-align: center;"><img src="imgs/img_in_image_box_340_976_865_1452.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 4 公交数据构成</div>


##### 6.3.4.2 公交线路

包括线路名称、始发站名称、终点站名称、线路轨迹、运营状态、运营时间、票价、线路类型等：

a）线路名称：由线路关键字、始发站名称、终点站名称组成，用于完整且唯一标识某一条公交线路。示例：26路（二里庄—西便门），其中线路关键字26、始发站名称二里庄、终点站名称西便门。

b）运营状态：表示线路的运营状态，应包含4类：正常运营、停运、建设中、规划中。

c) 运营时间: 公交线路运营时间正常情况下每天都在一个或多个固定时间段内, 也有按冬、夏季变换运营时间。

d）票价：包括高低票价、起价总价。

高低票价：同一线路，由于车型、位置不同而引起的不同票价，其中价格最低的为低票价，价格最高的为高票价。

起价总价：从某一条线路的任意站点上车，到该线路的任意站点下车而产生的最低票价为起价，线路的全程标价为总价。

e）线路类型：分为短途公交线路和长途公交线路。其中短途公交线路包含普通公交、快速公交、

微循环公交、旅游观光线路、机场大巴、有轨电车、无轨电车、地铁线路、轮渡、索道；长途公交线路包含长途大巴、火车等。

f）线路轨迹：公交线路的行车轨迹。

##### 6.3.4.3 公交站点

包括站点名称、站点顺序、站点运营状态、站点首末班发车时间、站点类型、关联线路等：

a）站点名称：官方命名，一般应为该站点在所属车次的站牌中的名称。

b）站点顺序：线路从始发站至终点站运行过程中，停靠站点的顺序。

c) 站点运营状态：表示站点的运营状态，应包括 4 类：正常运营、停运、建设中、规划中。

d）站点首末班发车时间：首班车到达本站点的时间、末班车到达本站点的时间。

e）站点类型：包括普通公交站点、地铁站点、快速公交站点、长途公交站点。

f） 关联线路：公交站点关联的公交线路标识。

##### 6.3.4.4 公交事件

用以表达现实中突然发生的公共交通事件，包括事件展示时间、事件详情以及关联关系：

a）事件展示时间：明确事件的开始时间和预计结束时间。

b）事件详情：具体描述事件的内容。

c）关联关系：明确事件所关联的公交线路标识。

#### 6.3.5 背景数据

背景数据包括手机地图显示用的行政区划、岛屿、兴趣面（AOI）、水系、绿地、居民地、铁路等信息，根据不同比例尺，几何形状为点、线或面。

#### 6.3.6 实时交通数据

##### 6.3.6.1 概述

实时交通数据主要包括交通状态和交通事件信息。交通状态描述某段道路上的交通流拥堵状态；交通事件描述某段路上发生的临时或一段时间内的交通事件。

##### 6.3.6.2 交通状态

包括批次时间、位置参考、交通流状态、速度、旅行时间、可信度：

a）批次时间：实时交通数据的批次处理时间。

b）位置参考：交通状态的位置描述，通常用道路唯一编码来表示某段道路。

c) 交通流状态：道路的交通拥堵状态，通常有未知、畅通、缓行、拥堵、严重拥堵、禁止通行等。

d）速度：道路通行的平均速度，通常以公里/小时为单位表达。

e）旅行时间：通过某段道路预计所花费的时间。

f）可信度：交通状态的可信程度。

示例：

发布字段

批次时间：2016-11-28 09:30

位置参考: 北京北四环东路

交通流状态:缓行

速度:30 km/h

发布含义

2016-11-28 09:30，北京北四环东路交通流状态为缓行，当前时速30 km/h。

##### 6.3.6.3 交通事件

包括事件的开始时间、结束时间、位置参考、事件类型代码、事件描述、事件影响长度、可信度：

a） 开始时间：交通事件的开始时间。

b）结束时间：交通事件的结束时间。

c）位置参考：交通事件发生的位置描述。

d）事件类型：交通事件类型。示例：交通事故、道路施工。

e）事件描述：交通事件的文字描述。

f） 事件影响长度：交通事件实际影响的道路长度。

g）可信度：交通事件的可靠程度。

示例：

发布字段

开始时间:2016-11-01 08:30

结束时间：2016-11-30 17:30

位置参考:北京北四环东路辅路

事件类型:道路施工

发布含义

从2016-11-01 08:30至2016-11-30 17:30，北京北四环东路辅路将进行道路施工。

#### 6.3.7 空间定位数据

##### 6.3.7.1 概述

空间定位数据用于手机地图室内外定位，包括卫星定位数据、网络定位数据，几何形状为点。卫星定位数据包括GPS在内的GNSS发布的定位信息；网络定位数据包括移动通信基站、无线路由器（WiFi）等网络设备信息，用于辅助卫星定位系统加快定位速度，提高定位精度，弥补卫星定位系统无法覆盖的定位场景（如室内）的定位需要。

##### 6.3.7.2 卫星定位数据

卫星定位数据应包括日期、定位时间、经度、纬度、定位状态、对地速度、方位角等信息，内容及结构可参考 GNSS 相关协议标准，本标准不作定义和要求。

##### 6.3.7.3 网络定位数据

###### 6.3.7.3.1 移动通信基站

移动通信基站应包括移动国家码（MCC）、移动网络码（MNC）、地区区域码（LAC）、基站小区代码（CellID）、经纬度、信号覆盖范围（半径）：

a） 国家码(MCC): 由国际电联统一分配和管理, 唯一识别移动用户所属的国家, 共 3 位, 中国为 460。

b) 移动网络码(MNC): 共 2 位, 中国移动 TD 系统使用 00, 中国联通 GSM 系统使用 01, 中国移动 GSM 系统使用 02, 中国电信 CDMA 系统使用 03。

c） 地区区域码(LAC): 区域划分代码。

d）基站小区代码(CellID):代表某个移动通信基站。

e） 经纬度：移动通信基站的空间位置。

###### 6.3.7.3.2 无线路由器

无线路由器(WiFi)应包括介质访问控制(MAC)地址、经纬度、信号覆盖范围(半径):

a）介质访问控制(MAC)地址：也称物理地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。每一个无线路由器有一个全球唯一的MAC地址。

b）经纬度：无线路由器的空间位置。

#### 6.3.8 室内地图数据

##### 6.3.8.1 概述

室内地图数据包括建筑物轮廓、楼层轮廓、商铺、通行设施、公共设施和室内路网等信息，内容构成如图5所示。建筑物轮廓、楼层轮廓几何形状为面；商铺几何形状为点、面；通行设施、公共设施几何形状为点；室内路网几何形状为点、线。

<div style="text-align: center;"><img src="imgs/img_in_image_box_231_961_941_1476.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 5 室内地图数据构成</div>


##### 6.3.8.2 建筑物轮廓

建筑物外轮廓范围。

##### 6.3.8.3 楼层轮廓

建筑物内每个楼层的外轮廓范围，用于显示具体楼层的范围。

##### 6.3.8.4 商铺

商铺包括商铺区块和商铺门。

商铺区块：所有被墙体或无形分界线隔开的区域块范围，包含区块名称、类型等属性。

商铺门：商铺出入口，包含底商外部门及普通商铺门，用于路径规划时指引到对应的商铺。

##### 6.3.8.5 通行设施

包括楼梯、扶梯、直梯、货梯、建筑物大门等，建筑物大门用于连接室内与室外，楼梯、扶梯、直梯、货梯等用于连接不同楼层间的空间关系。

##### 6.3.8.6 公共设施

包括卫生间、公用电话、取款机、服务台、收银台等用于服务大众的设施，用于展示公共服务设施的位置及信息检索。

##### 6.3.8.7 室内路网

包括室内通道及结点，为用户提供室内路径规划。

### 6.4 数据分层

#### 6.4.1 数据层划分

手机地图数据 8 大类要素按照数据层来组织，共划分为 31 个数据层。

#### 6.4.2 数据层命名

数据层名称采用 4 位数字代码，前 2 位数字表示要素类代码，后 2 位数字表示该要素类下的数据层代码，空位以 0 补齐。数据层名称结构如图 6 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_371_1176_827_1277.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">图 6 数据层名称结构</div>


示例：车行道路数据层用0201表示，其中02表示路网要素类代码，01表示车行道路数据层代码。

#### 6.4.3 数据层表

数据层表内容应符合附录 A 要求。

#### 6.4.4 数据层扩充原则

数据层可根据需要进行扩展。扩展数据层不应与已有数据层存在重复或冲突。

### 6.5 属性结构

#### 6.5.1 属性字段命名

属性字段名应由半角大写英文字母、阿拉伯数字和下划线组成，以字母开头，小于或等于10个字符。

示例：属性项“第一中文名称”的字段名用“NAME_CN_1”表示。

#### 6.5.2 属性项与属性表

各数据层属性项及属性表结构应符合附录 B 要求。

#### 6.5.3 属性项扩展原则

属性项可根据需要进行扩展。扩展属性项不应与已有属性项存在重复或冲突。

## 7 质量要求

### 7.1 POI 数据

POI 数据应满足如下要求：

a）数据完整性：

1）重要、次重要 POI 主体遗漏或多余率应低于 5%；

2）重要、次重要 POI 深度信息遗漏率应低于 20%。

注1：重要 POI 指构成一个城市或地区的中心或支撑点的，手机地图用户最关注的 POI。

注2：次重要POI指具有地理位置参照点意义的，经常被手机地图用户使用的POI。

注3：遗漏（多余）率= $ \left[\text{样本区内比照现实遗漏（多余）POI个数/样本区内POI总个数}\right]\times100\% $ 。

b) 逻辑一致性：

1）重要、次重要 POI 与道路、背景的相对空间位置错误率应低于 5%;

2）一般 POI 与道路的相对空间位置错误率应低于 10%。

c) 位置精度：

1）坐标系应符合本标准6.1要求；

2）重要、次重要 POI 与实际位置偏差应在 30 m 以内。

d) 属性精度：

1）重要、次重要 POI 的分类、名称、地址应与真实特征相符，错误率应低于 5%；

2）一般 POI 的分类、名称、地址应与真实特征相符，错误率应低于 10%；

3）重要、次重要 POI 简介应有格式标签，营业时间应符合 GDF 时间域表达规范，图片大小应控制在  $ 80 \, kb \sim 100 \, kb $  以内，评分或价格与真实情况应相符。

### 7.2 路网数据

路网数据应满足如下要求：

a） 数据完整性：

1）高级别道路遗漏或多余率应低于3%；

2）中级别道路遗漏或多余率应低于5%；

3）重要交通规制信息遗漏或多余率应低于10%。

注 $ ^{1} $ ：高级别道路指高速公路、国道、城市快速路。

注2：中级别道路指省道、县道、城市主干道、城市次干道。

注3：重要交通规制信息指高、中级别道路上的交通禁止、限制信息。

## b) 逻辑一致性：

1）高级别道路的空间位置关系（平面或交叉）和空间连接错误率应低于3%；

2）高、中级别道路的交通流方向或路口交通规制错误率应低于10%；

3）人行道路的空间位置关系(平面或交叉)和空间连接错误率应低于15%。

## c) 位置精度：

1）坐标系应符合本标准6.1要求。

2）高级别道路与实际位置偏差应小于15 m；

3）中、低级别道路与实际位置偏差应小于25 m；

4）人行道路与实际位置偏差应小于25 m。

## d) 属性精度：

1）高级别道路的功能等级、道路编号、名称、交通流方向等影响路径规划与引导的属性错误率应低于3%;

2）中、低级别道路的功能等级、道路编号、名称、交通流方向等影响路径规划与引导的属性错误率应低于5%;

3）人行道路的交通流方向、设施类型、指示信息错误率应低于10%。

### 7.3 门址数据

门址数据应满足如下要求：

a）数据完整性：

门址数据类型应符合 GB/T 35639—2017 中 6.2 要求。

b) 逻辑一致性：

门址与道路、背景的相对位置错误率应低于3%。

c) 位置精度：

1）坐标系应符合本标准6.1要求；

2）门址与实际位置偏差应小于30 m。

d) 属性精度：

门址数据结构应符合 GB/T 35639—2017 中 6.3、6.4 要求。

### 7.4 公交数据

公交数据应满足如下要求：

a）数据完整性：

1）地铁线路遗漏或多余率应低于3%；

2）公交线路遗漏或多余率应低于5%；

3）换乘站点遗漏或多余率应低于10%。

## b) 逻辑一致性：

1）公交站点与线路不匹配率应低于3%；

2）公交站序错误率应低于5%；

3）公交线路轨迹错误率应低于10%。

## c) 位置精度：

1）坐标系应符合本标准6.1要求；

2）公交站点与实际位置偏差应小于30 m。

d) 属性精度：

1）地铁线路的名称、站点名称、运营状态、运营时间等重要属性信息错误率应低于3%；

2）公交线路的名称、站点名称、运营状态、运营时间等重要属性错误率应低于10%。

### 7.5 背景数据

背景数据应满足如下要求：

a）数据完整性：

1）县级（含）以上行政区划遗漏或多余率应低于0.5%；

2）全国一级水系遗漏或多余率应低于2%；

3）重要城市中重要 AOI 遗漏或多余率应低于 10%；

4）居民地的遗漏或多余率应低于20%。

注 $ ^{1} $ ：重要城市指按手机地图用户分布排名前20城市。

注2：重要AOI对应重要POI类型。

b) 逻辑一致性：

<div style="text-align: center;"><img src="imgs/img_in_image_box_717_549_766_590.jpg" alt="Image" width="4%" /></div>


1）水系、铁路、绿地等相对空间位置错误率应低于5%；

2）背景与道路、POI相对空间位置错误率应低于10%；

3）行政区划形状应闭合；

4）全国一级水系之间应接边、连通。

c) 位置精度：

1）坐标系应符合本标准6.1要求；

2）国界、未定国界应与国家公布的基础地理数据一致；

3）区县级（含）以上行政区划边界应与国家公布的基础地理数据一致；

4）全国一级水系的空间位置或形状应与国家出版物一致。

d) 属性精度：

1）国界、未定国界处地名应保证主权归属正确；

2）县级（含）以上行政区划属性（名称、行政区划代码）应与国家公布的基础地理数据相符；

3）全国一级水系的名称、类别等重要属性错误率应低于2%；

4）铁路、绿地等属性错误率应低于10%。

### 7.6 实时交通数据

实时交通数据应满足如下要求：

a）数据完整性：

1）交通状态的批次时间、交通流状态、速度、位置参考等重要属性不应遗漏或多余；

2）交通事件的开始时间、结束时间、事件代码、位置参考等重要属性不应遗漏或多余。

b) 逻辑一致性：

1）交通状态的参考位置与路网、背景等其他数据的相对空间位置错误率应低于10%;

2）交通事件的参考位置与路网、背景等其他数据的相对空间位置错误率应低于3%。

c) 位置精度：

1）坐标系应符合本标准6.1要求；

2）交通状态或事件描述的位置和实际位置偏差应小于15 m。

d) 属性精度：

1）交通状态错误率应低于15%；

2）重大/紧急交通事件错误率应低于2%。

e) 时间精度：

交通状态或交通事件延时应低于 10 min。

### 7.7 空间定位数据

卫星定位数据质量要求可遵循 GNSS 相关协议标准，本标准仅对网络定位数据作出如下要求：

a） 数据完整性：

1）提供全球网络定位服务，网络定位数据覆盖有移动通信基站或 WiFi 的国家和地区应高于 90%;

2）提供中国（含港澳台地图）网络定位服务，网络定位数据覆盖有移动通信基站或 WiFi 的人口聚居区域应高于 90%。

b) 位置精度：

1）坐标系应符合本标准6.1要求；

2）移动通信基站位置，城市密集区域与实际偏差应小于200 m，郊区和农村与实际偏差应小于2000 m，偏远地区与实际偏差应小于10000 m；

3）WiFi位置，城市密集区域与实际偏差应小于50 m，郊区和农村与实际偏差应小于200 m，偏远地区与实际偏差应小于1 000 m。

c) 时间精度: 移动通信基站和 WiFi 数据, 城市密集区域更新周期应小于 3 天, 郊区和农村更新周期应小于 7 天, 偏远地区更新周期应小于 30 天。

### 7.8 室内地图数据

室内地图数据应满足如下要求：

a） 数据完整性：

1）建筑物轮廓、楼层轮廓不应遗漏或多余；

2）商铺、商铺门、通行设施等遗漏或多余率应低于5%。

b) 逻辑一致性：

1）建筑物轮廓应与实际建筑物轮廓形状、比例保持一致；

2）楼层轮廓应在建筑物外轮廓内；

3）商铺、公共设施、通行设施数据应在楼层轮廓内；

4） 室内商铺相对位置错误率应低于3%；

5）公共设施、通行设施、商铺三者相对空间位置错误率应低于5%。

c) 位置精度：

1）坐标系应符合本标准6.1要求；

2）建筑物轮廓与背景、路网的相对位置偏差应小于5 m；

3）不同层直梯的垂直相对位置偏差应小于3 m。

d) 属性精度：

1）室内楼层名称错误率应低于0.5%;

2）通行设施名称及类型错误率应低于3%；

3）直梯、扶梯等通行设施的连通关系错误率应低于3%；

4）室内商铺名称、分类错误率应低于5%；

5）公共设施、通行设施名称、分类错误率应低于5%。

## 8 元数据

元数据主要包括手机地图数据的基本信息和质量评价信息,具体内容应符合附录 C 要求。

# 附录 A

(规范性附录)

数据层表

手机地图数据分层内容见表 A.1。

### 表 A.1


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>要素类代码</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>数据层代码</td><td style='text-align: center;'>几何特征</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="2">POI</td><td rowspan="2">01</td><td style='text-align: center;'>POI基础信息</td><td style='text-align: center;'>0101</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>POI深度信息</td><td style='text-align: center;'>0102</td><td style='text-align: center;'>—</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="6">路网</td><td rowspan="6">02</td><td style='text-align: center;'>车行道路</td><td style='text-align: center;'>0201</td><td style='text-align: center;'>线</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>车行道路结点</td><td style='text-align: center;'>0202</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>交通规制</td><td style='text-align: center;'>0203</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>人行道路</td><td style='text-align: center;'>0204</td><td style='text-align: center;'>线</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>人行道路结点</td><td style='text-align: center;'>0205</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路附属设施</td><td style='text-align: center;'>0206</td><td style='text-align: center;'>点</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="2">门址</td><td rowspan="2">03</td><td style='text-align: center;'>通用地址</td><td style='text-align: center;'>0301</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>专用信箱</td><td style='text-align: center;'>0302</td><td style='text-align: center;'>点</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="3">公交</td><td rowspan="3">04</td><td style='text-align: center;'>公交线路</td><td style='text-align: center;'>0401</td><td style='text-align: center;'>线</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>公交站点</td><td style='text-align: center;'>0402</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>公交事件</td><td style='text-align: center;'>0403</td><td style='text-align: center;'>—</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="7">背景</td><td rowspan="7">05</td><td style='text-align: center;'>水系</td><td style='text-align: center;'>0501</td><td style='text-align: center;'>线、面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>绿地</td><td style='text-align: center;'>0502</td><td style='text-align: center;'>线、面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>岛屿</td><td style='text-align: center;'>0503</td><td style='text-align: center;'>面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>铁路</td><td style='text-align: center;'>0504</td><td style='text-align: center;'>线</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划</td><td style='text-align: center;'>0505</td><td style='text-align: center;'>线、面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>兴趣面</td><td style='text-align: center;'>0506</td><td style='text-align: center;'>面</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>居民地</td><td style='text-align: center;'>0507</td><td style='text-align: center;'>点、面</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="2">实时交通</td><td rowspan="2">06</td><td style='text-align: center;'>交通状态</td><td style='text-align: center;'>0601</td><td style='text-align: center;'>—</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>交通事件</td><td style='text-align: center;'>0602</td><td style='text-align: center;'>—</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="2">空间定位</td><td rowspan="2">07</td><td style='text-align: center;'>移动通信基站</td><td style='text-align: center;'>0701</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>无线路由器</td><td style='text-align: center;'>0702</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 A.1(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>要素类代码</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>数据层代码</td><td style='text-align: center;'>几何特征</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="7">室内地图</td><td rowspan="7">08</td><td style='text-align: center;'>建筑物轮廓</td><td style='text-align: center;'>0801</td><td style='text-align: center;'>面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>楼层轮廓</td><td style='text-align: center;'>0802</td><td style='text-align: center;'>面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>商铺</td><td style='text-align: center;'>0803</td><td style='text-align: center;'>点、面</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>通行设施</td><td style='text-align: center;'>0804</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>公共设施</td><td style='text-align: center;'>0805</td><td style='text-align: center;'>点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>室内通道</td><td style='text-align: center;'>0806</td><td style='text-align: center;'>线</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>室内通道结点</td><td style='text-align: center;'>0807</td><td style='text-align: center;'>点</td><td style='text-align: center;'>O</td></tr><tr><td colspan="6">注: 约束条件取值 M(必选)、O(可选)。</td></tr></table>

## 附录 B

(规范性附录)

基础属性表

手机地图数据分层的基础属性项及属性结构见表 B.1。

<div style="text-align: center;">表 B.1</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="14">POI</td><td rowspan="7">POI基础信息</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>电话</td><td style='text-align: center;'>TEL</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>允许多个电话，多个电话用半角“|”分隔</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>地址</td><td style='text-align: center;'>ADDR</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>允许多个分类，多个分类用半角“|”分隔</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>ADCODE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>重要度</td><td style='text-align: center;'>IMP</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>POI的重要程度或等级</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="7">POI深度信息</td><td style='text-align: center;'>关联POI标识</td><td style='text-align: center;'>POIID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>图片</td><td style='text-align: center;'>PIC</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>图片URL链接</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>价格</td><td style='text-align: center;'>PRI</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>单位为元，保留两位小数</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>简介</td><td style='text-align: center;'>INT</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>时间</td><td style='text-align: center;'>TIME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>规范的营业时间，采用GDF时间域格式</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>评论</td><td style='text-align: center;'>REVIEW</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>评分</td><td style='text-align: center;'>SCORE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0.0～5.0</td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td rowspan="10">路网</td><td rowspan="10">车行道路</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>起始结点</td><td style='text-align: center;'>FNODE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>终止结点</td><td style='text-align: center;'>TNODE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路等级</td><td style='text-align: center;'>RC</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>功能等级</td><td style='text-align: center;'>FC</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路形态</td><td style='text-align: center;'>FW</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路方向</td><td style='text-align: center;'>DIRECTION</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路编号</td><td style='text-align: center;'>ROADNO</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="17">路网</td><td rowspan="4">车行道路结点</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>结点类型</td><td style='text-align: center;'>NODETYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1:普通路口2:复合路口3:出入口</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>结点标志</td><td style='text-align: center;'>NODEMARK</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1:普通结点2:主点3:子点</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>连接路信息</td><td style='text-align: center;'>LRID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>多条连接路用“|”分隔</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="5">交通规制</td><td style='text-align: center;'>通过结点标识</td><td style='text-align: center;'>NODEID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>进入道路标识</td><td style='text-align: center;'>FRID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>退出道路标识</td><td style='text-align: center;'>TRID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>规制信息</td><td style='text-align: center;'>MANOEUVRE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>时间限制</td><td style='text-align: center;'>TIMERES</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="3">道路附属设施</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>关联道路标识</td><td style='text-align: center;'>ROADID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>设施类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1:电子眼2:交通警示</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="5">人行道路</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>进入结点</td><td style='text-align: center;'>FWNODE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>退出结点</td><td style='text-align: center;'>TWNODE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>道路方向</td><td style='text-align: center;'>DIRECTION</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>人行道路类型</td><td style='text-align: center;'>WFTYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1:人行横道3:地下通道4:过街天桥5:地铁通道8:扶梯9:直梯10:索道11:空中通道12:建筑物穿越通道13:行人道路14:游船路线15:观光车路线16:阶梯17:斜坡18:桥19:隧道</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="3">路网</td><td style='text-align: center;'>人行道路</td><td style='text-align: center;'>禁止信息</td><td style='text-align: center;'>TIME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>禁止通行时间</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="2">人行道路结点</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>连接人行道路信息</td><td style='text-align: center;'>LWID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>多条连接路用“|”分隔</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="13">门址</td><td rowspan="7">通用地址</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>ADCODE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划中文地址</td><td style='text-align: center;'>AADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>街路巷/片区中文地址</td><td style='text-align: center;'>SADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>院门/楼址中文地址</td><td style='text-align: center;'>HADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>单元户室号中文地址</td><td style='text-align: center;'>UADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>地块号中文地址</td><td style='text-align: center;'>BADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td rowspan="6">专用信箱</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>ADCODE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划中文地址</td><td style='text-align: center;'>AADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>街路巷/片区中文地址</td><td style='text-align: center;'>SADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>信箱编号中文地址</td><td style='text-align: center;'>MADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>分信箱编号中文地址</td><td style='text-align: center;'>SMADDR_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td rowspan="6">公交</td><td rowspan="6">公交线路</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>线路名称</td><td style='text-align: center;'>NAME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>包含线路编号和起止点站名称</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>公交线路的类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>用以区分普通公交、地铁、机场大巴等不同类型</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>首班车发车时间</td><td style='text-align: center;'>STIME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0000～2359</td><td style='text-align: center;'>格式为“HHMM”，时间为24小时制</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>末班车发车时间</td><td style='text-align: center;'>ETIME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0000～2359</td><td style='text-align: center;'>格式为“HHMM”，时间为24小时制</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>不规则发车时间描述</td><td style='text-align: center;'>TIMEDES</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>当线路的运营时间不是全年每天都相同时，在此详细记录</td><td style='text-align: center;'>O</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="15">公交</td><td rowspan="4">公交线路</td><td style='text-align: center;'>基本价格</td><td style='text-align: center;'>BPRICE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>普通车型的起价</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>总价格</td><td style='text-align: center;'>TPRICE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>普通车型的总价。当为单一票价的时候，总价格=基本价格</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>线路状态</td><td style='text-align: center;'>STATUS</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0:停运1:正常2:规划3:建设</td><td style='text-align: center;'>表示线路的运营状态</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>预计开通时间</td><td style='text-align: center;'>EXPDATE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>在建中的地铁线路，计划开通时间</td><td style='text-align: center;'>O</td></tr><tr><td rowspan="6">公交站点</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>站点唯一编号</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>公交车站名称</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>站序</td><td style='text-align: center;'>STANUM</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>在公交车线里面的车站顺序，表示这个车站在公交车线里面是第几站</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>站点运营状态</td><td style='text-align: center;'>STATUS</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0:停运1:正常2:规划中3:在建</td><td style='text-align: center;'>描述站点的运营状态</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>站点类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>用以区分普通公交、地铁、BTR等站点类型</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>关联线路</td><td style='text-align: center;'>LID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>站点所属公交线路的ID号</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="5">公交事件</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>突发事件索引ID</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>开始展示时间</td><td style='text-align: center;'>STIME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>描述开始展示突发事件的时间点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>结束展示时间</td><td style='text-align: center;'>ETIME</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>描述结束展示突发事件的时间点</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>事件详情</td><td style='text-align: center;'>DES</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>描述具体的事件内容</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>线路ID</td><td style='text-align: center;'>LID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>关联的公交线路的ID号</td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="26">背景</td><td rowspan="5">水系</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>水系全长</td><td style='text-align: center;'>LENGTH</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>水系级别</td><td style='text-align: center;'>WATERLEVEL</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>水系类别</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="4">绿地</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>绿地类别</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>面积</td><td style='text-align: center;'>AREA</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td rowspan="3">居民地</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>居民地分级</td><td style='text-align: center;'>CLASSTYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td rowspan="5">铁路</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>铁路全长</td><td style='text-align: center;'>LENGTH</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>铁路类别</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>铁路级别</td><td style='text-align: center;'>RAILLEVL</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="3">岛屿</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>面积</td><td style='text-align: center;'>AREA</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td rowspan="3">行政区划</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>行政区划代码</td><td style='text-align: center;'>ADCODE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="3">兴趣面</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>SETT_ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>兴趣面类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="2">实时交通</td><td rowspan="2">交通状态</td><td style='text-align: center;'>批次时间</td><td style='text-align: center;'>TIME</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>处理某一批次交通数据源的时刻</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>位置参考</td><td style='text-align: center;'>LOCREF</td><td style='text-align: center;'>复合类型</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>交通状态的位置描述,可用一个或多个属性表示某段道路的某一方向</td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="11">实时交通</td><td rowspan="4">交通状态</td><td style='text-align: center;'>交通流状态</td><td style='text-align: center;'>STATUS</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0:未知1:畅通2:缓行3:拥堵4:严重拥堵5:无交通流</td><td style='text-align: center;'>道路的交通拥堵状态</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>速度</td><td style='text-align: center;'>SPEED</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>特定时段通过特定道路的平均速度,通常以公里/小时为单位表达</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>旅行时间</td><td style='text-align: center;'>TRTIME</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>在特定时段通过特定路段所花费的平均时间,单位为秒</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>可信度</td><td style='text-align: center;'>REL</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~100:0表示完全不可信,100为100%完全可信的理想状态</td><td style='text-align: center;'>交通状态的可信程度</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="7">交通事件</td><td style='text-align: center;'>开始时间</td><td style='text-align: center;'>STIME</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>交通事件的开始时间</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>结束时间</td><td style='text-align: center;'>ETIME</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>交通事件的结束时间</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>位置参考</td><td style='text-align: center;'>LOCREF</td><td style='text-align: center;'>复合类型</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>交通事件发生的地区、路段或点位置描述</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>事件类型</td><td style='text-align: center;'>EVENTTY</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>交通事件类型</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>事件描述</td><td style='text-align: center;'>DES</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>交通事件的详细文字描述</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>事件影响长度</td><td style='text-align: center;'>AFFLEN</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>交通事件实际影响的道路长度,单位为米</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>可信度</td><td style='text-align: center;'>REL</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~100:0表示完全不可信,100为100%完全可信的理想状态</td><td style='text-align: center;'>交通事件的可靠程度</td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="7">空间定位</td><td rowspan="5">移动通信基站</td><td style='text-align: center;'>移动国家码</td><td style='text-align: center;'>MCC</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>基站所在国家</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>移动网络码</td><td style='text-align: center;'>MNC</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>运营商</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>地区区域码</td><td style='text-align: center;'>LAC</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>区域代码</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>基站代码</td><td style='text-align: center;'>CELLID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>基站代码</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>半径</td><td style='text-align: center;'>RADIUS</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>覆盖半径</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="2">无线路由器</td><td style='text-align: center;'>介质访问控制地址</td><td style='text-align: center;'>MAC</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>唯一地址</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>半径</td><td style='text-align: center;'>RADIUS</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>覆盖半径</td><td style='text-align: center;'>M</td></tr><tr><td rowspan="24">室内地图</td><td rowspan="6">建筑物外围轮廓</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>建筑物地址</td><td style='text-align: center;'>ADDR</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>地上楼层数</td><td style='text-align: center;'>UPNUM</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>地下楼层数</td><td style='text-align: center;'>DWNUM</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>建筑物类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="3">建筑物楼层轮廓</td><td style='text-align: center;'>该楼层的顺序号</td><td style='text-align: center;'>FLNO</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>-9～999</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>楼层实际标注名</td><td style='text-align: center;'>FL_NONA</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>所属建筑物标识</td><td style='text-align: center;'>LID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="6">商铺</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>商铺类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>商铺门类型</td><td style='text-align: center;'>DOOR</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>商铺编号</td><td style='text-align: center;'>FTNUM</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>所属楼层</td><td style='text-align: center;'>FLNO</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="5">通行设施</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>通行设施类型</td><td style='text-align: center;'>TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>所属楼层</td><td style='text-align: center;'>FLNO</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>连通关系</td><td style='text-align: center;'>TO_CON</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="4">公共设施</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>中文名称</td><td style='text-align: center;'>NAME_CN</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>所属楼层</td><td style='text-align: center;'>FLNO</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>公共设施类型</td><td style='text-align: center;'>FT_TYPE</td><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr></table>

<div style="text-align: center;">表 B.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>要素类</td><td style='text-align: center;'>数据层</td><td style='text-align: center;'>属性项</td><td style='text-align: center;'>字段名</td><td style='text-align: center;'>类型</td><td style='text-align: center;'>最大出现次数</td><td style='text-align: center;'>值域</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>约束条件</td></tr><tr><td rowspan="7">室内地图</td><td rowspan="5">室内通道</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>所属楼层</td><td style='text-align: center;'>FLNO</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>通行方向</td><td style='text-align: center;'>DIRECTION</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0:双向1:正向2:逆向</td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>进入结点</td><td style='text-align: center;'>FINODE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>退出结点</td><td style='text-align: center;'>TINODE</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td rowspan="2">室内通道结点</td><td style='text-align: center;'>唯一标识</td><td style='text-align: center;'>ID</td><td style='text-align: center;'>N</td><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>连接室内通道标识</td><td style='text-align: center;'>LIID</td><td style='text-align: center;'>C</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>多条连接路用“|”分隔</td><td style='text-align: center;'>M</td></tr><tr><td colspan="9">注:约束条件取值M(必选)、O(可选)。</td></tr></table>

附录 C

(规范性附录)

元数据结构表

手机地图数据元数据内容见表C.1。

### 表 C.1


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>数据项名称</td><td style='text-align: center;'>数据类型</td><td style='text-align: center;'>格式</td><td style='text-align: center;'>填写示例</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>约束条件</td></tr><tr><td colspan="7">数据基本信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>数据名称</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>30C</td><td style='text-align: center;'>2017版手机地图数据</td><td style='text-align: center;'>填写数据名称</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>生产单位名称</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>40C</td><td style='text-align: center;'>某某单位</td><td style='text-align: center;'>填写生产单位名称</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>所有权单位名称</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>40C</td><td style='text-align: center;'>某某单位</td><td style='text-align: center;'>填写版权所有单位名称</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>生产时间</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>6C</td><td style='text-align: center;'>201612</td><td style='text-align: center;'>格式为YYYYMM</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>空间坐标系</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>20C</td><td style='text-align: center;'>WGS84</td><td style='text-align: center;'>填写数据坐标系统</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>地图投影名称</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>30C</td><td style='text-align: center;'>Web墨卡托</td><td style='text-align: center;'>填写地图投影方式</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>坐标单位</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>10C</td><td style='text-align: center;'>度</td><td style='text-align: center;'>根据实际情况填写坐标单位</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>总层数</td><td style='text-align: center;'>整型</td><td style='text-align: center;'>2D</td><td style='text-align: center;'>25</td><td style='text-align: center;'>根据实际情况填写总层数</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>层名</td><td style='text-align: center;'>变长文本</td><td style='text-align: center;'>VCHAR</td><td style='text-align: center;'>0101,0201,0202,0301</td><td style='text-align: center;'>根据实际情况填写层名</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>数据规格版本</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>40C</td><td style='text-align: center;'>V1.3</td><td style='text-align: center;'>填写数据符合的规格版本号</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>数据量</td><td style='text-align: center;'>单精度</td><td style='text-align: center;'>5.1F</td><td style='text-align: center;'>1024.1</td><td style='text-align: center;'>单位为兆(M),注至小数点后一位</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>数据覆盖范围</td><td style='text-align: center;'>变长文本</td><td style='text-align: center;'>VCHAR</td><td style='text-align: center;'>365个城市</td><td style='text-align: center;'>数据覆盖城市</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>数据现势性</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>6C</td><td style='text-align: center;'>201610</td><td style='text-align: center;'>格式为YYYYMM</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>数据现势性描述</td><td style='text-align: center;'>变长文本</td><td style='text-align: center;'>VCHAR</td><td style='text-align: center;'>北京、上海、广州、深圳2016年10月更新</td><td style='text-align: center;'>根据数据现势性情况如实填写</td><td style='text-align: center;'>O</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>数据内容完整性描述</td><td style='text-align: center;'>变长文本</td><td style='text-align: center;'>VCHAR</td><td style='text-align: center;'>缺失室内地图要素</td><td style='text-align: center;'>描述数据内容的完整性,对本标准规定应当表示,但数据中缺失的图层、要素、属性进行说明</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>元数据创建日期</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>8C</td><td style='text-align: center;'>20170115</td><td style='text-align: center;'>格式为YYYYMMDD</td><td style='text-align: center;'>M</td></tr><tr><td colspan="7">质量评价信息</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>数据质量总评价</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>10C</td><td style='text-align: center;'>合格</td><td style='text-align: center;'>填写评价分值或者等级(优/良/合格/不合格)</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>数据质量总评价时间</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>8C</td><td style='text-align: center;'>20161225</td><td style='text-align: center;'>格式为YYYYMMDD</td><td style='text-align: center;'>M</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>数据质量总评价单位</td><td style='text-align: center;'>字符型</td><td style='text-align: center;'>30C</td><td style='text-align: center;'>某某单位</td><td style='text-align: center;'>填写质检单位名称</td><td style='text-align: center;'>M</td></tr><tr><td colspan="7">注:约束条件取值M(必选)、O(可选)。</td></tr></table>

## 参考文献

[1] GB/T 16820—1997 地图学术语

[2] GB/T 19710—2005 地理信息 元数据

[3] GB/T 19711—2005 导航地理数据模型与交换格式

[4] GB/T 20268—2006 车载导航地理数据采集处理技术规程

[5] GB/T 24356—2009 测绘成果质量检查与验收

[6] GB/T 25528—2010 地理信息 数据产品规范

[7] GB/T 28441—2012 车载导航电子地图数据质量规范

[8] GB/T 28445—2012 个人位置导航电子地图数据质量规范

[9] GB/T 29101—2012 道路交通信息服务 数据服务质量规范

[10] GB/T 33183—2016 基础地理信息 1:50 000 地形要素数据规范

[11] CH/T 1019—2010 导航电子地图检测规范

[12] CH/T 9008.2—2010 基础地理信息数字成果 1:500、1:1000、1:2000 数字高程模型