

# 中华人民共和国国家标准

GB/T 35631—2017

# 地图符号 XML 描述规范

# Specification for XML description of map symbol

2017-12-29 发布

2018-07-01 实施

## 目次

前言 …… III    
引言 …… IV    
1 范围 …… 1    
2 术语和定义 …… 1    
3 符号和缩略语 …… 2    
3.1 缩略语 …… 2    
3.2 符号 …… 2    
4 基本原则 …… 3    
5 地图符号的表达 …… 4    
5.1 地图符号的分类与结构 …… 4    
5.1.1 地图符号的分类 …… 4    
5.1.2 地图符号的结构 …… 4    
5.2 点符号表达模型 …… 5    
5.2.1 点符号的分类 …… 5    
5.2.2 矢量点符号的表达 …… 5    
5.2.3 栅格点符号的表达 …… 5    
5.2.4 TrueType 点符号的表达 …… 5    
5.3 线符号表达模型 …… 5    
5.3.1 线符号的分类 …… 5    
5.3.2 简单线符号的表达 …… 6    
5.3.3 组合线符号的表达 …… 6    
5.3.4 填充线符号的表达 …… 6    
5.4 面符号表达模型 …… 6    
5.4.1 面符号的分类 …… 6    
5.4.2 颜色填充面符号的表达 …… 7    
5.4.3 点填充面符号的表达 …… 7    
5.4.4 复杂填充面符号的表达 …… 7    
5.4.5 线填充面符号的表达 …… 7    
6 基于 XML 的地图符号描述 …… 7    
6.1 基本要求 …… 7    
6.2 点符号的 XML 描述 …… 7    
6.2.1 矢量点符号的 XML 描述 …… 7    
6.2.2 栅格点符号的 XML 描述 …… 10    
6.2.3 TrueType 点符号的 XML 描述 …… 10    
6.3 线符号的 XML 描述 …… 11    
6.3.1 简单线符号的 XML 描述 …… 11

6.3.2 组合线符号的 XML 描述 …… 12    
6.3.3 填充线符号的 XML 描述 …… 15    
6.4 面符号的 XML 描述 …… 17    
6.4.1 颜色填充面符号的 XML 描述 …… 17    
6.4.2 点填充面符号的 XML 描述 …… 18    
6.4.3 复杂填充面符号的 XML 描述 …… 19    
6.4.4 线填充面符号的 XML 描述 …… 20    
7 地图符号库共享元数据 …… 22    
7.1 地图符号库元数据 …… 22    
7.2 映射比例 …… 22    
7.3 局部坐标系 …… 22    
7.4 地图符号库的 XML 描述 …… 23    
7.5 地图符号库的共享与扩展 …… 23    
附录 A（资料性附录） 地图符号基本图元 …… 25    
附录 B（资料性附录） 点符号 XML 模式 …… 28    
附录 C（资料性附录） 线符号 XML 模式 …… 38    
附录 D（资料性附录） 面符号 XML 模式 …… 50    
附录 E（资料性附录） 符号库 XML 模式 …… 61    
参考文献 …… 63

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由国家测绘地理信息局提出。

本标准由全国地理信息标准化技术委员会(SAC/TC 230)归口。

本标准起草单位:武汉大学、武汉理工大学、国家测绘地理信息局测绘标准化研究所、国家基础地理信息中心。

本标准主要起草人：李霖、尹章才、朱海红、于忠海、胡玮、张坤、王东华、张航、应申、蔡忠亮。

## 引言

地图符号共享是地理信息共享的重要组成部分，采用通用的描述方法来描述地图符号是实现符号共享的有效途径。本标准依据地图符号表达的共性技术特征，给出了用 XML 描述符号的方案，为地图符号共享提供了核心技术基础。本标准描述的符号不包含注记。

# 地图符号 XML 描述规范

## 1 范围

本标准规定了地图符号的基本表达模型、地图符号的基本描述原则与基于 XML 的描述方案，在具体实现时可结合各软件系统平台进行扩展和修改。

本标准适用于面向跨平台及网络环境中的地形图符号设计、制作和更新，也可为各类专题地图符号的共享提供参照。

## 2 术语和定义

下列术语和定义适用于本文件。

### 2.1 

## 地图符号 map symbol

地图上各种图形和记号的总称，由形状、尺寸、位置、方向、文字、色彩等图形变量构成。

注：改写 GB/T 16820—2009，定义 4.35。本标准仅讨论图形符号部分，不讨论注记部分。

### 2.2 

## 地图符号库 map symbol library

按照预定结构组织成的供地图编制选用的各种地图符号的数据信息的集合。

[GB/T 16820—2009, 定义 5.8]

### 2.3 

## 点符号 point symbol

用来表示抽象为点的地物或现象的符号。

注：改写 GB/T 16820—2009，定义 4.36。点符号的大小与地图比例尺无关但具有定位特征。

### 2.4 

## 线符号 linear symbol

用来表示抽象为线的地物或现象的符号。

注：改写 GB/T 16820—2009，定义 4.37。线符号沿着某个方向延伸的长度与地图比例尺有关。

### 2.5 

## 面符号 areal symbol

用来表示抽象为面状的地物或现象的符号。

注：改写 GB/T 16820—2009，定义 4.38。面符号的范围同地图比例尺有关。

### 2.6 

## 基本图元 primary graphic element

组成地图符号的最基本的点、线、面等图形元素，是可以编辑的最小图形单位。

[CH/T 4017—2012, 定义 2.4]

### 2.7 

## 复合图元 composite symbol cell

一系列基本图元的有序集合。

[CH/T 4017—2012, 定义 2.12]

### 2.8 

## 符号成员 symbol component

对复合图元施加一定配置规则而形成的符号单元。

[CH/T 4017—2012, 定义 2.13]

### 2.9 

## 径向渐变 radial-gradient

从内到外(从中间向外拉伸)进行一种或多种颜色渐变填充。

### 2.10 

## 线性渐变 linear-gradient

从起点到终点沿符号的轴线、水平线或垂直线方向进行一种或多种颜色渐变填充。

### 2.11 

## 晕线 hatched line

由一组平行的简单直线共同构成的符号样式，这些简单线具有相同的宽度、间距、角度、颜色和背景色等属性。

注：晕线适用于复杂线符号和复杂填充符号。

### 2.12 

## X ML 元素 XML element

具有自我描述性，用于传输数据，从（且包括）开始标签直到（且包括）结束标签的部分。

注：XML 元素的命名可以含字母、数字以及其他字符，不能包含空格，并且不能以数字、标点符号、字符“xml”（或者 XML、Xml）开始。

## 3 符号和缩略语

下列缩略语和符号适用于本文件。

### 3.1 缩略语

UML 统一建模语言(Unified Modeling Language)

XML 可扩展标记语言(Extensible Markup Language)

### 3.2 符号

本标准采用 UML 静态结构图来描述符号库及符号表达模型，本标准中用到的 UML 表示法见图 1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_167_220_1038_715.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 1 UML 符号</div>


出现在本标准中描述符号的 XML 模式的视图表示法见图 2。

<div style="text-align: center;"><img src="imgs/img_in_image_box_297_856_906_1106.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">图 2 XML 模式视图表示法</div>


## 4 基本原则

基于 XML 对地图符号进行描述，应遵循以下基本原则：

——地图符号的 XML 描述的实质，是采用 XML 对地图符号的形状、尺寸、方向、颜色、网纹等视觉变量所进行的系统描述。

——地图符号的 XML 描述的目的，是方便地图符号的交流与共享，它应具备开放性、中立性和灵活性。

——地图符号的 XML 描述的规则，应与地图图式规范保持一致。

——地图符号的 XML 描述的扩展，应与本标准中地图符号表达模型保持一致。

## 5 地图符号的表达

### 5.1 地图符号的分类与结构

#### 5.1.1 地图符号的分类

根据几何特征，地图符号通常可分为点符号、线符号和面符号。点符号、线符号、面符号与自定义符号共同构成了地图符号库（见图3）。其中自定义符号是一种用户根据实际需要而定义的地图符号类型，这类符号在地图符号库中往往没有预定义。

<div style="text-align: center;"><img src="imgs/img_in_image_box_289_475_886_677.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 3 地图符号的分类</div>


#### 5.1.2 地图符号的结构

##### 5.1.2.1 地图符号结构模型

地图符号的结构模型分为地图符号、符号成员、复合图元和基本图元4个层级。

图 4 为本标准推荐的地图符号、符号成员、复合图元、基本图元的组合关系。

<div style="text-align: center;"><img src="imgs/img_in_image_box_206_920_967_986.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 4 地图符号的结构模型</div>


##### 5.1.2.2 基本图元

基本图元是构成符号不可再分的基本单元，它由图形参数和绘制参数定义：

——图形参数用来描述基本图元的几何形状及定位信息等图形特征，它包括定位点、形状参数、旋转角度等。

——绘制参数用来描述基本图元的轮廓样式和填充样式等渲染信息。其中轮廓样式是指图元轮廓线的线宽、线型、颜色等样式；填充样式是指图元内部填充的颜色、晕线、图案等样式。

——点状基本图元：仅用一个定位点及图形参数即可表达的基本图元。

——线状基本图元：用连接多个定位点的线及图形参数即可表达的基本图元。

——面状基本图元：用连接多个定位点的封闭线及图形参数即可表达的基本图元。

地图符号基本图元参见附录 A。

##### 5.1.2.3 复合图元

复合图元是一系列基本图元的有序集合，其有序性是通过配置规则来确保的。复合图元的配置规则用于描述基本图元之间的空间关系及绘制顺序，以满足制图需要（如乡村路的明显拐弯点应为实部）。

复合图元配置规则有：

——基本图元的渐变方式，如地面河流单线符号中首尾宽度的渐变方式，时令河符号中实部与虚部在长度上的渐变方式。

——基本图元的拉伸方式，如陡坎符号中依比例尺长线与水平投影宽度的关系。

——基本图元的排列方式，如各类植被符号中填充符号的排列间距及排列模式。

——基本图元间的依附关系，如地下河段及出入口符号中圆弧符号半径与河宽的关系。

——基本图元间的压盖关系，如沙砾滩、沙泥滩等干出滩符号内不同层级符号单元的避让压盖关系。

##### 5.1.2.4 符号成员

符号成员是一系列复合图元的有序集合，其有序性是通过配置规则来确保的。符号成员的配置规则用于描述复合图元之间的空间关系及绘制顺序，以满足制图需要（如通过调整不同复合图元的绘制顺序来实现跨符号间的显示效果，不同等级道路之间的连通性表达就属于此类）。

### 5.2 点符号表达模型

#### 5.2.1 点符号的分类

根据图形类型，点符号可分为矢量点符号、栅格点符号和 TrueType 点符号，其结构模型见图 5。

<div style="text-align: center;"><img src="imgs/img_in_image_box_332_739_870_976.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图 5 点符号的分类</div>


#### 5.2.2 矢量点符号的表达

矢量点符号是基于矢量基本图元和配置规则来实现对点符号的一种表达。基本比例尺地形图中的点状符号均可用矢量点符号表达。

#### 5.2.3 栅格点符号的表达

栅格点符号是基于图片等图像格式来实现对点符号的一种表达。

#### 5.2.4 TrueType 点符号的表达

TrueType 点符号是基于 TrueType 字符来实现对点符号的一种表达，其中 TrueType 字符具有字体名称、字符值、字体颜色、大小等属性。

### 5.3 线符号表达模型

#### 5.3.1 线符号的分类

根据符号的结构，线符号通常可分为简单线符号、组合线符号和填充线符号，其结构模型见图6。其中，填充线符号又包括图片填充线符号、渐变填充线符号和晕线填充线符号。

<div style="text-align: center;"><img src="imgs/img_in_image_box_238_203_933_476.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">图 6 线符号的分类</div>


#### 5.3.2 简单线符号的表达

简单线符号通过定义图元样式(如虚实样式、线帽样式、线宽等)来完成线符号(如道路、单线河流等)的表达。

#### 5.3.3 组合线符号的表达

组合线符号是点符号与简单线符号的组合，它通过定义特定点状符号（包括其个数、偏移量、旋转角度、旋转类型等参数）和简单线符号来完成线符号（如水闸、船闸、电力线、车行桥、人行桥等）的表达。

#### 5.3.4 填充线符号的表达

##### 5.3.4.1 图片填充线符号的表达

基于图片纹理，对指定范围内的区域（以线要素为中心，以指定距离为半径的缓冲区区域）进行填充，实现线符号的表达。

##### 5.3.4.2 渐变填充线符号的表达

基于线性渐变或径向渐变颜色，对指定范围内的区域（以线要素为中心的缓冲区）进行填充，实现线符号的表达。

##### 5.3.4.3 晕线填充线符号的表达

基于晕线样式（包括晕线的线宽、角度、间隔、颜色等）与背景色，对指定范围内的区域（以线要素为中心的缓冲区）进行填充，实现线符号的表达。

### 5.4 面符号表达模型

#### 5.4.1 面符号的分类

根据填充内容，面符号通常可分为颜色填充面符号、点填充面符号、复杂填充面符号、线填充面符号四种类型，其结构模型见图7。其中，复杂填充面符号又可分为图片填充面符号、晕线填充面符号和渐变填充面符号三类。

<div style="text-align: center;"><img src="imgs/img_in_image_box_243_202_958_476.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">图 7 面符号的分类</div>


#### 5.4.2 颜色填充面符号的表达

颜色填充面符号通过内部颜色填充实现湖泊、池塘等单色填充符号的表达。

#### 5.4.3 点填充面符号的表达

点填充面符号通过面状要素区域内基于特定点状符号及其配置规则（如缩放比例、旋转角度、填充间距、填充角度、随机类型等）的填充来实现面状要素的表达。

#### 5.4.4 复杂填充面符号的表达

##### 5.4.4.1 图片填充面符号的表达

图片填充面符号通过面状要素区域内基于图片纹理的填充来实现面状要素的表达。

##### 5.4.4.2 晕线填充面符号的表达

晕线填充面符号通过面状要素区域内基于晕线样式（包括晕线的线宽、角度、间隔、颜色等）与背景色的填充来实现面状要素的表达。

##### 5.4.4.3 渐变填充面符号的表达

渐变填充面符号通过面状要素区域内基于线性渐变或径向渐变颜色的填充来实现面状要素的表达。

#### 5.4.5 线填充面符号的表达

线填充面符号通过面状要素区域内基于线符号（包括旋转角度、填充间距等参数）的填充来实现面状要素的表达。

## 6 基于 XML 的地图符号描述

### 6.1 基本要求

地图符号基于 XML 语言的描述，应满足 XML 语言规范和地图图式规范的基本要求。

### 6.2 点符号的 XML 描述

#### 6.2.1 矢量点符号的 XML 描述

基于 XML 对矢量点符号进行描述，应包含符号名称、符号代码、旋转角度、符号成员、复合图元、基

本图元等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 B.2。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_549_265_623_330.jpg" alt="Image" width="6%" /></div>


<div style="text-align: center;">图 8 1:250 000 地形图三角点符号</div>


GB/T 20257.4—2007 国家基本比例尺地图图式 1：250 000 中的三角点符号(图 8)可由以下 XML 定义：

〈SymbolCode〉10001〈/SymbolCode〉

〈! ---符号代码---〉

<! ———三角形基本图元——>

<PGraphUnit>

<GraphUnitType>PGT_TRIANGLE_REGULAR</GraphUnitType>

<GraphUnitCode>1000</GraphUnitCode>

角形基本图元定位点

(！___三角形基本图元定位点___)

(MapSymbolGeometryProp)

(CentralPointX)

(Value)0(/Value)

(Type)TRUE(/Type)

(/CentralPointX)

(CentralPointY)

(Value)0(/Value)

(Type)TRUE(/Type)

角形基本图元轮廓样式

(！___三角形基本图元轮廓样式___

(MapSymbolPen)

(PenWidth)10（/PenWidth）

(StyleCount)2（/StyleCount）

(Color)RGB(31,26,23)（/Color）

(Hatch)HS_HORIZONTAL（/Hatch）

(Style)BS_SOLID（/Style）

(Style0)100（/Style0）

(Style1)0（/Style1）

(MapSymbolPen)

<!——三角形基本图元内部填充样式——>

<MapSymbolBrush>

    <Style>BS_NULL</Style>

    <Color>RGB(255,255,255)</Color>

    <Hatch>HS_VERTICAL</Hatch>

    <FillColor>RGB(255,255,255)</FillColor>

</MapSymbolBrush>

<RotateAngle>0</RotateAngle>

<BeTensile>FALSE</BeTensile>

</PGraphUnit>

<!——椭圆基本图元——>

    <PGraphUnit>

        <GraphUnitType>PGT_ELLIPSE</GraphUnitType>

        <GraphUnitCode>1001</GraphUnitCode>

    </PGraphUnit>

    <MapSymbolGeometryProp>

        <CentralPointX>

            <Value>0</Value>

            <Type>TRUE</Type>

        </CentralPointX>

        <CentralPointY>

            <Value>0</Value>

            <Type>TRUE</Type>

        </CentralPointY>

    </MapSymbol>

    <MapSymbol>

        <LongRadius>7</LongRadius>

    </LongRadius>

    <ShortRadius>7</ShortRadius>

    <SideNum>5</SideNum>

    <StartAngle>0</StartAngle>

    <EndAngle>0</EndAngle>

    <MapSymbolGeometryProp>

        <!——椭圆基本图元轮廓样式——>

            <MapSymbolPen>

                <PenStyle>PS_NULL</PenStyle>

                <PenWidth>10</PenWidth>

                <StyleCount>0</StyleCount>

                <Color>RGB(31,26,23)</Color>

                <Hatch>HS_HORIZONTAL</Hatch>

                <Style>BS_SOLID</Style>

            </MapSymbolPen>

        </!——椭圆基本图元内部填充样式——>

    </MapSymbolBrush>

    <MapSymbol>

        <Style>BS_SOLID</Style>

        <Color>RGB(31,26,23)</Color>

        <Hatch>HS_VERTICAL</Hatch>

        <FillColor>RGB(31,26,23)</FillColor>

    </MapSymbol>

</MapSymbolBrush>

</MapSymbolBrush>

<RotateAngle>0</RotateAngle>

<BeTensile>FALSE</BeTensile>

</PGraphUnit>

</SymbolComponent>

</PointSymbol>

#### 6.2.2 栅格点符号的 XML 描述

基于 XML 对栅格点符号进行描述，应包含符号名称、符号代码、旋转角度、符号宽度、符号高度、栅格图片 Base64 编码等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 B.3。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_541_535_631_620.jpg" alt="Image" width="7%" /></div>


<div style="text-align: center;">图 9 1:250 000 地形图飞机场符号</div>


GB/T20257.4—2007 国家基本比例尺地图图式1：250 000中的飞机场符号(图9)可由以下XML定义：

<?xml version="1.0" encoding="UTF-8"?>
<SymbolName>飞机场</SymbolName>
<SymbolCode>10008</SymbolCode>
<RotateAngle>0</RotateAngle>
<Width>250</Width>
<Height>250</Height>
<!-- 栅格图片 Base64 编码 -->
<!-- 符号名称 -->
<!-- 符号代码 -->
<!-- 旋转角度 -->
<!-- 符号宽度 -->
<!-- 符号高度 -->

注：由于图片 Base64 编码内容较长，为简洁表达飞机场符号的〈Content〉仅截取部分内容示意表达。

#### 6.2.3 TrueType 点符号的 XML 描述

基于 XML 对 TrueType 点符号进行描述，应包含对符号名称、符号代码、旋转角度、TrueType 字符等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 B.4。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_538_1226_634_1295.jpg" alt="Image" width="8%" /></div>


<div style="text-align: center;">图 10 1:250 000 地形图不依比例尺单层桥符号</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_74_1374_110_1413.jpg" alt="Image" width="3%" /></div>


GB/T 20257.4—2007 国家基本比例尺地图图式 1：250 000 中的不依比例尺单层桥符号（图 10）可由以下 XML 定义：

<?xml version="1.0" encoding="UTF-8"?>
<PointSymbol>
    <SymbolName>单层桥</SymbolName>
    <SymbolCode>372</SymbolCode>
</PointSymbol>

〈！---符号名称---〉

〈！---符号代码---〉

<! ———— TrueType 字符的描述集合————>
<SymbolUnit>
    <Unicode>60533</Unicode>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</OffsetY>
    <Angle>0</Angle>
    <SymbolUnit>
        <! ———— TrueType 字符的描述集合————>
    </SymbolUnit>
    <FontName>Public</FontName>
    <Visible>True</Visible>
    <Size>5</Size>
    <Color>255,52,52.52</Color>
    <OffsetX>0</OffsetX>
    <OffsetY>0</

<Content>
RO1GODlh1wBOAPcAAAAAAP///7a4u+jq7bGlucrNON7g4tLU1u3u7+Tl5uHi49na26quscLGybe9wc7R0-7rBxfHz90/x8ubo6d3f4Nrc3dXY2evs7Ojp6cnKyv/++f7788G5rc+tgdKzi72zpf3376eAUK6FVLGlV597Tr-SLWrWNXbOLXMWkfOTN
</Content>
<Content>
ointSymbol>

注：由于 TrueType 字体的 Base64 编码内容较长，为简洁表达，不依比例尺单层桥点符号的  $ \langle $ Content $ \rangle $  仅截取部分内容示意表达。

### 6.3 线符号的 XML 描述

#### 6.3.1 简单线符号的 XML 描述

基于 XML 对简单线符号进行描述，应包含符号名称、符号代码、简单线符号的图元集合等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 C.2。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_456_1028_749_1053.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">图 11 1:250 000 地形图国道符号</div>


GB/T20257.4—2007国家基本比例尺地图图式1：250000中的国道符号(图11)可由以下XML定义：

<?xml version="1.0" encoding="UTF-8"?>
<LineSymbol>
    <SymbolName>国道</SymbolName>
    <SymbolCode>20003</SymbolCode>
    <! 符号代码---
        符号成员
    </!>
</SymbolComponent>
<SymbolRect>
    <Left>0</Left>
    <Top>20</Top>
    <Right>180</Right>
    <Bottom>-20</Bottom>
</SymbolRect>

<!-- 折线基本图元 -->

<LGraphUnit>
    <GraphUnitType>LGT_LINE</GraphUnitType>
    <GraphUnitCode>2000</GraphUnitCode>
    <PointList>
        <Point>
            <List.x>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.x>
            <List.y>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.y>
        </Point>
        <Point>
            <List.x>
                <Value>180</Value>
                <Type>TRUE</Type>
            </List.x>
            <List.y>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.y>
        </Point>
    </PointList>
</LGraphUnit>

折线基本图元轮廓样式

<MapSymbolPen>
    <PenWidth>40</PenWidth>
    <StyleCount>2</StyleCount>
    <Color>RGB(218,37,29)</Color>
    <Hatch>HS_HORIZONTAL</Hatch>
    <Style>BS_SOLID</Style>
    <Style0>10</Style0>
    <Style1>0</Style1>
    <MapSymbolPen>
        <BeTensile>TRUE</BeTensile>
    </LGraphUnit>
</MapSymbolPen>

#### 6.3.2 组合线符号的 XML 描述

基于 XML 对组合线符号进行描述，应包含符号名称、符号代码、组合线符号中点符号和线符号等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 C.3。

<div style="text-align: center;"><img src="imgs/img_in_image_box_483_185_728_277.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">图 12 1:50 000 地形图高速公路符号</div>


GB/T 20257.3—2006 国家基本比例尺地图图式 1:50 000 中的高速公路符号(图 12)可由以下 XML 定义：

〈！---符号名称---〉

<！---符号代码--->

<?xml version="1.0" encoding="UTF-8"?>
<LineSymbol>
    <SymbolName>高速公路</SymbolName>
    <SymbolCode>20002</SymbolCode>
    <SymbolComponent>
        <SymbolRect>
            <Left>0</Left>
            <Top>55</Top>
            <Right>300</Right>
            <Bottom>-55</Bottom>
        </SymbolRect>
        <LGraphUnit>
            <GraphUnitType>LGT_LINE</GraphUnitType>
            <GraphUnitCode>2000</GraphUnitCode>
            <PointList>
                <Point>
                    <List.x>
                        <Value>0</Value>
                        <Type>TRUE</Type>
                    </List.x>
                    <List.y>
                        <Value>0</Value>
                        <Type>TRUE</Type>
                    </List.y>
                </Point>
                <Point>
                    <List.x>
                        <Value>300</Value>
                        <Type>TRUE</Type>
                    </List.x>
                </List.y>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.y>
        </Point>
    </SymbolUnit>
    <MapSymbolPen>
        <PenStyle>PS_USERSTYLE|PS_ENDCAP_FLAT|PS_JOIN_ROUND|PS_GEOMETRIC</PenStyle>
        <PenWidth>110</PenWidth>
        <StyleCount>2</StyleCount>
        <Color>RGB(31,26,23)</Color>
    </MapSymbolPen>
</LineSymbol>

<lbHatch>HS_HORIZONTAL</lbHatch>
<Style>BS_SOLID</Style>
<Style0>300</Style0>
<Style1>0</Style1>
</MapSymbolPen>
<BeTesile>TRUE</BeTesile>
</LGraphUnit>
<LGraphUnit>
<GraphUnitType>LGT_LINE</GraphUnitType>
<GraphUnitCode>2001</GraphUnitCode>
<PointList>
<Point>
<List.x>
<Value>0</Value>
<Type>TRUE</Type>
</List.x>
<List.y>
<Value>0</Value>
<Type>TRUE</Type>
</List.y>
</Point>
<Point>
<List.x>
<Value>300</Value>
<Type>TRUE</Type>
</List.x>
<List.y>
<Value>0</Value>
<Type>TRUE</Type>
</List.y>
</Point>
</PointList>
<MapSymbolPen>
<PenStyle>PS_USERSTYLE|PS_ENDCAP_FLAT|PS_JOIN_ROUND|PS_GEOMETRIC</PenStyle>
<PenWidth>70</PenWidth>
<StyleCount>2</StyleCount>
<Color>RGB(255,205,175)</Color>
<lbHatch>HS_HORIZONTAL</lbHatch>
<Style>BS_SOLID</Style>
<Style0>300</Style0>
<Style1>0</Style1>
</MapSymbolPen>
<BeTesile>TRUE</BeTesile>
</LGraphUnit>
<LGraphUnit>
<GraphUnitType>LGT_LINE</GraphUnitType>
<GraphUnitCode>2002</GraphUnitCode>
</LGraphUnit>
</LGraphUnit>

<PointList>
    <Point>
        <List.x>
            <Value>0</Value>
            <Type>TRUE</Type>
        </List.x>
        <List.y>
            <Value>0</Value>
            <Type>TRUE</Type>
        </List.y>
    </Point>
    <Point>
        <List.x>
            <Value>300</Value>
            <Type>TRUE</Type>
        </List.x>
        <List.y>
            <Value>0</Value>
            <Type>TRUE</Type>
        </List.y>
    </Point>
</PointList>

<MapSymbolPen>
    <PenStyle>PS_USERSTYLE|PS_ENDCAP_FLAT|PS_JOIN_ROUND|PS_GEOMETRIC</PenStyle>
    <PenWidth>10</PenWidth>
    <StyleCount>2</StyleCount>
    <Color>RGB(31,26,23)</Color>
    <lbHatch>HS_HORIZONTAL</lbHatch>
    <Style>BS_SOLID</Style>
    <Style0>300</Style0>
    <Style1>0</Style1>
</MapSymbolPen>

<BeTesile>TRUE</BeTesile>
</LGraphUnit>
</SymbolComponent>
</LineSymbol>

#### 6.3.3 填充线符号的 XML 描述

##### 6.3.3.1 图片填充线符号的 XML 描述

基于 XML 对图片填充线符号进行描述，应包含符号名称、符号代码、填充图片 Base64 编码及其填充样式[宽度、高度、填充类型(平铺或拉伸)、填充半径]等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 C.4。

示例：

假设沿线要素两侧各  $ 5 \, mm $  宽度、以重复方式填充图片，可由以下 XML 定义：

〈? xml version="1.0" encoding="UTF-8"?〉
〈SymbolName〉图片填充线符号〈/SymbolName〉

〈! ——符号名称——〉

(SymbolCode)10001(/SymbolCode)
(Width)0(/Width)
(Height)1000(/Height)
(Type)REPEAT(/Type)
(Radius)1000(Radius)

（!———填充图片的Base64编码——）

注：由于图片 Base64 编码内容较长，为简洁表达，图片填充线符号的〈Content〉仅截取部分内容示意表达。

##### 6.3.3.2 渐变填充线符号的 XML 描述

基于 XML 对渐变填充线符号进行描述，应包含符号名称、符号代码、填充样式[渐变类型（线性渐变或径向渐变）、起始颜色、终止颜色、起始宽度、终止宽度]等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 C.5。

示例：

假设沿线要素从红色渐变到黑色，宽度从 0.1 mm 渐变到 0.4 mm，可由以下 XML 定义：

<?xml version="1.0" encoding="UTF-8"?>
<SymbolName>渐变填充线符号</SymbolName>
<SymbolCode>10002</SymbolCode>
<Type>LINEAR</Type>
<StartColor>RGB(255,0,0,0)</StartColor>
<EndColor>RGB(0,0,0,0)</EndColor>
<StartWidth>10</StartWidth>
<EndWidth>40</EndWidth>

<!-- 符号名称 -->
<!-- 符号代码 -->
<!-- 填充类型 -->
<!-- 起始颜色 -->
<!-- 终止颜色 -->
<!-- 起始宽度 -->
<!-- 终止宽度 -->

##### 6.3.3.3 晕线填充线符号的 XML 描述

基于 XML 对晕线填充线符号进行描述，应包含符号名称、符号代码、晕线样式（包括晕线的宽度、间距、角度、颜色、背景色、填充半径等）等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 C.6。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_512_1175_661_1242.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;">图 13 晕线填充线符号示例</div>


图 13 中的晕线填充线符号可由以下 XML 定义：

<?xml version="1.0" encoding="UTF-8"?>
<SymbolName>晕线填充线符号</SymbolName>
<SymbolCode>10001</SymbolCode>
<Width>15</Width>
<Space>200</Space>
<Angle>45</Angle>
<Color>RGB(0,0,0,0)</Color>

<!--符号名称-->
<!--符号代码-->
<!--晕线宽度-->
<!--晕线间距-->
<!--晕线角度-->
<!--晕线颜色-->

<BackColor>RGB(255,255,255,0)(BackColor)
<Radius>1000<Radius>

〈！----背景色----〉

〈！---填充半径---〉

### 6.4 面符号的 XML 描述

#### 6.4.1 颜色填充面符号的 XML 描述

基于 XML 对颜色填充面符号进行描述，应包含符号名称、符号代码、面符号填充样式（填充颜色）、面符号轮廓线样式等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 D.2。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_532_465_675_526.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;">图 14 1:50 000 地形图湖泊符号</div>


GB/T 20257.3—2006 国家基本比例尺地图图式 1:50 000 中的湖泊符号(图 14)可由以下 XML 定义：

GB/T 20237.3—2006 国家基本比例尺地图图式 1·50 000 中的湖沿村马（图 14）可由以下 XML 定义：
<?xml version="1.0" encoding="UTF-8"?>
<SymbolName>湖泊</SymbolName>
<SymbolCode>10001</SymbolCode>
<Color>RGB(179,222,248,0)</Color>
<!-- 面符号边线符号成员 -->
<SymbolComponent>
<! — 面符号边线线基本图元 -->
<LGraphUnit>
<GraphUnitType>LGT_LINE</GraphUnitType>
<GraphUnitCode>2000</GraphUnitCode>
<PointList>
<Point>
<List.x>
<Value>0</Value>
<Type>TRUE</Type>
</List.x>
<List.y>
<Value>0</Value>
<Type>TRUE</Type>
</List.y>
</Point>
<Point>
<List.x>
<Value>10</Value>
<Type>TRUE</Type>
</List.x>
<List.y>
<Value>0</Value>
<Type>TRUE</Type>
</List.y>
</Point>
</PointList>
</LGraphUnit>

(MapSymbolPen)

(PenWidth)10</PenWidth>

(StyleCount)2</StyleCount>

(Color)RGB(0,147,221)</Color>

(Hatch)HS_HORIZONTAL</Hatch>

(Style)BS_SOLID</Style>

(Style0)300</Style0>

(Style1)0</Style1>

(MapSymbolPen)

(BeTensile)TRUE</BeTensile>

(/LGraphUnit)

(/SymbolComponent)

#### 6.4.2 点填充面符号的 XML 描述

基于 XML 对点填充面符号进行描述，应包含符号名称、符号代码、填充的点符号及其填充样式（包括点符号的旋转角度、水平偏移量、垂直偏移量、填充角度是否随机、填充偏移量是否随机）、面符号轮廓线样式等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 D.3。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_495_735_676_807.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">图 15 1:50 000 地形图平沙地符号</div>


GB/T 20257.3—2006 国家基本比例尺地图图式 1:50 000 中的平沙地符号(图 15)可由以下 XML 定义：

<?xml version="1.0" encoding="UTF-8"?>
<AreaSymbol>
    <SymbolName>平沙地</SymbolName>
    <SymbolCode>10001</SymbolCode>
    <Angel>0</Angel>
    <DeltX>100</DeltX>
    <DeltY>100</DeltY>
    <AngleRandom>0</AngleRandom>
    <DeltRandom>0</DeltRandom>
    <!-- 填充点符号 X 轴偏移量 -->
    <!-- 填充点符号 Y 轴偏移量 -->
    <!-- 填充点符号角度是否随机 -->
    <!-- 填充点符号偏移量是否随机 -->
    <!-- 填充点符号 -->
    <PointSymbol>
        <SymbolName>沙(填充面)</SymbolName>
        <SymbolType/>
        <SymbolCode>10132</SymbolCode>
        <RotateAngle>0</RotateAngle>
        <PGraphUnit>
            <GraphUnitType>PGT_ELLIPSE</GraphUnitType>
            <GraphUnitCode>1000</GraphUnitCode>
            <MapSymbolGeometryProp>
                <CentralPointX>
                    <Value>0</Value>
                    <Type>TRUE</Type>
                </MapSymbolGeometryProp>
            </GraphUnitType>
        </MapSymbolGeometryProp>
    </PGraphUnit>
</AreaSymbol>

</CentralPointX>

<CentralPointY>
    <Value>0</Value>
    <Type>TRUE</Type>
</CentralPointY>

<LongRadius>8</LongRadius>
<ShortRadius>8</ShortRadius>
<SideNum>5</SideNum>
<StartAngle>0</StartAngle>
<EndAngle>0</EndAngle>
</MapSymbolGeometryProp>

<MapSymbolPen>
    <PenStyle>PS_NULL</PenStyle>
    <PenWidth>10</PenWidth>
    <StyleCount>0</StyleCount>
    <Color>RGB(165,118,27)</Color>
    <Hatch>HS_HORIZONTAL</Hatch>
    <Style>BS_SOLID</Style>
</MapSymbolPen>

<MapSymbolBrush>
    <Style>BS_SOLID</Style>
    <Color>RGB(165,118,27)</Color>
    <Hatch>HS_VERTICAL</Hatch>
    <FillColor>RGB(96,93,92)</FillColor>
</MapSymbolBrush>

<RotateAngle>0</RotateAngle>
<BeTensile>FALSE</BeTensile>
</PGraphUnit>
</PointSymbol>
</AreaSymbol>

#### 6.4.3 复杂填充面符号的 XML 描述

##### 6.4.3.1 图片填充面符号的 XML 描述

基于 XML 对图片填充面符号进行描述，应包含符号名称、符号代码、填充图片 Base64 编码及其填充样式[填充图片的符号角度、填充类型（平铺或拉伸）]、面符号轮廓线样式等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 D.4。

示例：

假设在面要素内用指定的图片进行平铺填充时，可由以下 XML 定义：

<?xml version="1.0" encoding="UTF-8"?>
<SymbolName>图片填充面符号</SymbolName>
<SymbolCode>10001</SymbolCode>
<Angle>0</Angle>
<Type>REPEAT</Type>
<! 填充图片的 Base64 编码</!>
<Content>
data:image/JPG;base64,/9/44AQSkZJRgABAQEAYABgAAD/2wBDAgGBgcGBQgHBwcJCQgKDBQNDAs-
</Content>

LDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwh</Content>

注：由于图片 Base64 编码内容较长，为简洁表达，图片填充符号的〈Content〉仅截取部分内容示意表达。

##### 6.4.3.2 晕线填充面符号的 XML 描述

基于 XML 对晕线填充面符号进行描述，应包含符号名称、符号代码、面符号填充样式（晕线的宽度、间距、角度、颜色、背景色等）、面符号轮廓线样式等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 D.5。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_522_460_652_516.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;">图 16 晕线填充面符号示例</div>


图 16 的晕线填充面符号示例可由以下 XML 定义：

<?xml version="1.0" encoding="UTF-8"?>
<SymbolName>晕线填充面符号</SymbolName>
<SymbolCode>10001</SymbolCode>
<Width>15</Width>
<Space>200</Space>
<Angle>45</Angle>
<Color>RGB(0,0,0,0)</Color>
<BackColor>RGB(255,255,255,0)</BackColor>

<!--符号名称-->
<!--符号代码-->
<!--晕线宽度-->
<!--晕线距离-->
<!--晕线角度-->
<!--晕线颜色-->
<!--背景色-->

##### 6.4.3.3 渐变填充面符号的 XML 描述

基于 XML 对渐变填充面符号进行描述，应包含符号名称、符号代码、面符号填充样式（填充类型（线性渐变或径向渐变）、起始颜色、终止颜色、起始宽度、终止宽度等）、面符号轮廓线样式等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 D.6。

示例：

假设以面要素重心为中心、由外向内从黄色渐变到红色，可由以下 XML 定义：



（?xml version="1.0" encoding="UTF-8"?>
<SymbolName>渐变填充面符号</SymbolName>
<SymbolCode>10002</SymbolCode>
<Type>RADIAL</Type>
<StartColor>RGB(255,255,0,0)</StartColor>
<EndColor>RGB(255,0,0,0)</EndColor>
<!——符号名称——>
<!——符号代码——>
<!——填充类型——>
<!——起始颜色——>
<!——终止颜色——>
</SymbolCode>
</SymbolName>

#### 6.4.4 线填充面符号的 XML 描述

基于 XML 对线填充面符号进行描述，应包含符号名称、符号代码、填充的线符号及其填充样式（填充间隔、填充角度）、面符号轮廓线样式等内容，每项内容均使用 XML 元素进行描述。其 XML 模式参见 D.7。

示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_512_1384_658_1446.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;">图 17 线填充面符号示例</div>


图 17 的线填充面符号示例可由以下 XML 定义：

<GraphUnit>
    <GraphUnitType>LGT_LINE</GraphUnitType>
    <GraphUnitCode>2000</GraphUnitCode>
    <PointList>
        <Point>
            <List.x>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.x>
            <List.y>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.y>
        </Point>
        <Point>
            <List.x>
                <Value>500</Value>
                <Type>TRUE</Type>
            </List.x>
            <List.y>
                <Value>0</Value>
                <Type>TRUE</Type>
            </List.y>
        </Point>
    </PointList>
    <MapSymbolPen>
        <PenWidth>10</PenWidth>
        <StyleCount>2</StyleCount>
        <Color>RGB(31, 26, 23)</Color>
        <Hatch>HS_HORIZONTAL</Hatch>
        <Style>BS_SOLID</Style>
        <Style0>100</Style0>
        <Style1>10</Style1>
    </MapSymbolPen>
    <BeTensile>FALSE</BeTensile>
</GraphUnit>
</LineSymbol>

## 7 地图符号库共享元数据

### 7.1 地图符号库元数据

地图符号库元数据是地图符号共享的基础，其内容应包括符号库名称，相应地图的比例尺、制作单位、制作人、制作时间、映射比例等基本信息。

### 7.2 映射比例

映射比例是指地图符号库的逻辑单位和绘制设备单位之间的映射关系，绘制设备包括各种显示屏幕和打印机等。为了提高符号表达与绘制时的精度及运算速度，地图符号库采用逻辑单位来存储符号的各种参数。式(1)给出了映射比例与符号库逻辑单位和绘制设备之间的关系。

 $$ f=(\mu\times L)/(\sigma\times S\times D) $$ 

式中：

f —— 映射比例，单位为逻辑单位/设备单位；

 $ \mu $  ——逻辑单位与纸面单位的转换系数；

L ——符号库中的逻辑单位；

σ ——绘制设备单位与纸面单位毫米的转换系数；

S —— 比例尺分母；

D——绘制设备单位。

示例：图 18 为 GB/T 20257.3—2006 国家基本比例尺地图图式 1：50 000 中的三角点符号。该符号由两个基本图形组成：等边三角形和圆。其中等边三角形的高度  $ h = 1.56 \, mm $ ，线宽  $ w = 0.1 \, mm $ ；圆的直径  $ d = 0.15 \, mm $ 。假设符号库中 100 逻辑单位对应于  $ 1 \, mm $ ，即  $ \mu = 100 $ ，则：

 $ h=1.56\ mm=156 $  逻辑单位；

 $ d=0.15\ mm=15 $  逻辑单位；

 $ w=0.1\ mm=10 $  逻辑单位。

<div style="text-align: center;"><img src="imgs/img_in_image_box_508_975_657_1104.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;">图 18 三角点符号</div>


符号库中采用逻辑单位存储三角点符号中各个基本图元的图形参数。假设在打印机（绘制设备）绘制三角点符号时采用单位为米，则  $ \sigma=1/1000 $  。在 1:50000 比例尺中，

 $$ f=(\mu\times L)/(\sigma\times S\times D)=\frac{(100\times L)}{\frac{1}{1\ 000}\times50\ 000\times D}=2\times\frac{L}{D} $$ 

### 7.3 局部坐标系

地图符号借助局部坐标系定义(见图 19):

——X 轴：地图符号配置的定位线方向，前进方向为 X 轴正方向。

——Y轴：X轴的法线方向，沿X轴正方向逆时针旋转 $ 90^{\circ} $ 为Y轴正方向。

——坐标原点：X轴和Y轴的交点，为地图符号局部坐标系的原点。符号定位点和坐标原点的相对位置，也反映了符号化结果与对应要素的空间关系。

<div style="text-align: center;"><img src="imgs/img_in_image_box_418_217_787_482.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">图 19 地图符号局部坐标系</div>


### 7.4 地图符号库的 XML 描述

基于 XML 对地图符号库进行描述，应包含符号库元数据（名称、比例尺、制作单位、制作者、制作时间、映射比例）和地图符号集（点符号集合、线符号集合、面符号集合）等内容，每项均使用 XML 元素进行描述。其 XML 模式参见附录 E。

示例：

下面从实践角度，展示如何使用 XML 来描述符号库的内容，包括符号库元数据和符号集合。一个包含点、线、面符号的地图符号库，可由以下 XML 进行描述：

</! 符号--

### 7.5 地图符号库的共享与扩展

地图符号在基于 XML 描述的基础上，借助地图符号库元数据的 XML 描述，能实现同一系统不同版本之间的符号共享，也能实现不同系统之间的符号共享。

在遵循本标准符号表达模型前提下，不同制图系统或软件可通过额外的动作和变量来扩展符号描

述的编码方案；基本图元类型、描述基本图元的各项参数、图元集合的数量和层次均可按照需要进行扩展。扩展时须遵循以下基本原则：

——扩展的元素名称应遵循 XML 元素的命名规范，扩展元素的名称可以含字母、数字以及其他字符，不能包含空格，并且不能以数字、标点符号、字符“xml”（或者 XML、Xml）开始。推荐扩展的元素命名采用 UCC 命名法，即每个英文单词的首字母均大写。

——扩展基本图元类型时，宜尽量减少对操作系统图形接口的依赖，扩展的符号与操作系统图形接口一般应保持松耦合关系。

——符号表达扩展宜按照本标准的符号结构模型进行扩展，基本图元一级仅描述基本图元的形状和样式，不包含任何配置规则。根据符号特点和符号化要求，将相应的配置规则分别扩展在复合图元、符号成员和地图符号一级。

附录 A

（资料性附录）

地图符号基本图元

### 表 A.1 常用的地图符号基本图元及其图形参数和绘制参数


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>基本图元名称</td><td style='text-align: center;'>基本图元形状</td><td style='text-align: center;'>图形参数</td><td style='text-align: center;'>绘制参数</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>椭圆弧</td><td style='text-align: center;'><img src="imgs/img_in_image_box_371_480_740_702.jpg" ></td><td style='text-align: center;'>R:长轴半径r:短轴半径α:起始角度β:终止角度φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>椭圆</td><td style='text-align: center;'>-</td><td style='text-align: center;'>R:长轴半径r:短轴半径φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>扇形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_395_1015_718_1231.jpg" ></td><td style='text-align: center;'>R:长轴半径r:短轴半径α:起始角度β:终止角度φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>矩形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_375_1270_735_1520.jpg" ></td><td style='text-align: center;'>R:宽度一半r:高度一半φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr></table>

<div style="text-align: center;">表 A.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>基本图元名称</td><td style='text-align: center;'>基本图元形状</td><td style='text-align: center;'>图形参数</td><td style='text-align: center;'>绘制参数</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>菱形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_371_332_709_566.jpg" ></td><td style='text-align: center;'>R:宽度一半r:高度一半φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>等边三角形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_422_644_658_866.jpg" ></td><td style='text-align: center;'>R:外接圆半径φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>等腰三角形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_422_959_658_1165.jpg" ></td><td style='text-align: center;'>R:底边长的一半r:高φ:旋转角度P:定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>五角星</td><td style='text-align: center;'><img src="imgs/img_in_image_box_414_1263_666_1490.jpg" ></td><td style='text-align: center;'>R:外接圆半径r:内定点组成的圆的半径φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr></table>

<div style="text-align: center;">表 A.1 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>基本图元名称</td><td style='text-align: center;'>基本图元形状</td><td style='text-align: center;'>图形参数</td><td style='text-align: center;'>绘制参数</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>正多边形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_434_316_676_545.jpg" ></td><td style='text-align: center;'>R:外接圆半径N:边数φ:旋转角度P:中心定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>折线</td><td style='text-align: center;'><img src="imgs/img_in_image_box_385_585_727_724.jpg" ></td><td style='text-align: center;'>定位点</td><td style='text-align: center;'>轮廓样式</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>箭头</td><td style='text-align: center;'><img src="imgs/img_in_image_box_454_774_659_917.jpg" ></td><td style='text-align: center;'>P:起始点坐标P:终止点坐标L:箭头长度α:箭头夹角</td><td style='text-align: center;'>轮廓样式</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>贝塞尔曲线</td><td style='text-align: center;'><img src="imgs/img_in_image_box_376_965_734_1122.jpg" ></td><td style='text-align: center;'>定位点旋转角度</td><td style='text-align: center;'>轮廓样式</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>多边形</td><td style='text-align: center;'><img src="imgs/img_in_image_box_452_1166_659_1304.jpg" ></td><td style='text-align: center;'>定位点</td><td style='text-align: center;'>轮廓样式内部填充样式</td></tr></table>

# 附录 B

# （资料性附录）

# 点符号 XML 模式

### B.1 概述

该附录包含了矢量点符号、栅格点符号和 TrueType 点符号的标准 XML 模式。

B.2 为矢量点符号 XML 模式。

B.3 为栅格点符号 XML 模式。

B.4 为 TrueType 点符号 XML 模式。

#### B.2 矢量点符号(SimplePointSymbol.xsd)

矢量点符号 XML 模式，如图 B.1 所示。矢量点符号 XML 模式中各元素含义如下：

——PointSymbol: 表示点符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——RotateAngle: 表示符号旋转角度。

——SimpleComponent: 表示组成矢量点符号的符号成员。

——CompositeCells: 表示组成符号成员的复合图元。

——Configurations: 表示符号成员或复合图元的配置规则。

——BasicCell: 表示基本图元，常见的基本图元可参见附录 A。

——CellType: 表示基本图元类型。

——GeometryParas: 表示基本图元图形参数。

——RenderingParas: 表示基本图元绘制参数。

<div style="text-align: center;"><img src="imgs/img_in_image_box_299_236_781_1492.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">图 B.1 矢量点符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="PointSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="RotateAngle" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SimpleComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="CompositeCells" minOccurs="1" maxOccurs="unbounded">
                                <xsd:complexType>
                                    <xsd:sequence>
                                        <xsd:element name="Configurations" type="xsd:string" minOccurs="0"/>
                                    <xsd:element name="BasicCell" minOccurs="1">
                                        <xsd:complexType>
                                            <xsd:sequence>
                                                <xsd:element name="CellType" type="xsd:string" minOccurs="1"/>
                                                <xsd:element name="GeometryParas" minOccurs="1"/>
                                            <xsd:element name="RenderingParas" minOccurs="1"/>
                                        </xsd:sequence>
                                    </xsd:complexType>
                                </xsd:element>
                            </xsd:element>
                        </xsd:sequence>
                    </xsd:complexType>
            </xsd:element>
        </xsd:complexType>
    </xsd:sequence>
</xsd:schema>

#### B.3 栅格点符号(PicturePointSymbol.xsd)

栅格点符号 XML 模式，如图 B.2 所示。栅格点符号 XML 模式中各元素含义如下：

——PointSymbol: 表示点符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——RotateAngle: 表示符号旋转角度。

——PictureComponent: 表示组成栅格点符号的符号成员。

——Configurations: 表示符号成员或复合图元的配置规则。

——CompositeCells: 表示组成符号成员的复合图元。

——BasicCell: 表示基本图元。

——XSize: 表示基本图元中图片的宽度。

——YSize：表示基本图元中图片的高度。

——OffsetX: 表示基本图元中图片在水平方向偏移量。

——OffsetY: 表示基本图元中图片在垂直方向偏移量。

Type: 表示基本图元图片类型。

ContentBase64: 表示基本图元中图片的 Base64 编码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_252_243_756_1488.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图 B.2 栅格点符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="PointSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="RotateAngle" type="xsd:string" minOccurs="1"/>
                <xsd:element name="PictureComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="Configurations" type="xsd:string" minOccurs="0"/>
                            <xsd:element name="CompositeCells" minOccurs="1" maxOccurs="unbounded">
                                <xsd:complexType>
                                    <xsd:sequence>
                                        <xsd:element name="Configurations" type="xsd:string" minOccurs="0"/>
                                    <xsd:element name="BasicCell" minOccurs="1">
                                        <xsd:complexType>
                                            <xsd:sequence>
                                                    <xsd:element name="XSize" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="YSize" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="OffsetX" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="OffsetY" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="Type" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="ContentBase64" type="xsd:string" minOccurs="1"/>
                                                </xsd:sequence>
                            </xsd:complexType>
                        </xsd:element>
                    </xsd:sequence>
            </xsd:complexType>
        </xsd:element>
    </xsd:sequence>
</xsd:complexType>

 $ \langle /xsd:sequence \rangle $ 

</xsd:complexType>

\\xsd:element

</xsd:schema>

#### B.4 TrueType 点符号 (TrueTypePointSymbol.xsd)

TrueType 点符号 XML 模式，如图 B.3 所示。TrueType 点符号 XML 模式中各元素含义如下：

——PointSymbol: 表示点符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——RotateAngle: 表示符号旋转角度。

——ContentBase64:TrueType 点符号中使用的 TrueType 字体的 Base64 编码。

——TrueTypeComponent: 表示组成 TrueType 点符号的符号成员。

——Configuration: 表示符号成员或复合图元的配置规则。

——CompositeCells: 表示复合图元。

——BasicCell: 表示基本图元。

——Unicode: 表示基本图元的 Unicode 码。

——FontName: 表示基本图元字体名称。

——Visible: 表示基本图元是否可见。

——Size: 表示基本图元大小。

——Color: 表示基本图元颜色。

——OffsetX: 表示基本图元在水平方向偏移量。

——OffsetY: 表示基本图元在垂直方向偏移量。

——Angle: 表示基本图元旋转角度。

<div style="text-align: center;"><img src="imgs/img_in_image_box_265_334_787_1449.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图 B.3 TrueType 点符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="PointSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="RotateAngle" type="xsd:string" minOccurs="1"/>
                <xsd:element name="ContentBase64" type="xsd:string" minOccurs="1"/>
                <xsd:element name="TrueTypeComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="Configurations" type="xsd:string" minOccurs="0"/>
                            <xsd:element name="CompositeCells" minOccurs="1" maxOccurs="unbounded">
                                <xsd:complexType>
                                    <xsd:sequence>
                                        <xsd:element name="Configurations" type="xsd:string" minOccurs="0"/>
                                    <xsd:element name="BasicCell" minOccurs="1">
                                        <xsd:complexType>
                                            <xsd:sequence>
                                                    <xsd:element name="Unicode" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="FontName" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="Visible" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="Size" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="Color" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="OffsetX" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="OffsetY" type="xsd:string" minOccurs="1"/>
                                                    <xsd:element name="Angle" type="xsd:string" minOccurs="1"/>
                                                </xsd:sequence>
                            </xsd:complexType>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
</xsd:schema>

</xsd:complexType>

\\xsd:element

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:sequence>

</xsd:complexType>

\\xsd:element

 $ \langle /xsd:schema \rangle $ 

# 附录 C

# （资料性附录）

# 线符号 XML 模式

### C.1 概述

该附录包含了简单线符号、组合线符号、图片填充线符号、渐变填充线符号和晕线填充线符号的标准 XML 模式。

C.2 为简单线符号 XML 模式。

C.3 为组合线符号 XML 模式。

C.4 为图片填充线符号 XML 模式。

C.5 为渐变填充线符号 XML 模式。

C.6 为晕线填充线符号 XML 模式。

#### C.2 简单线符号(SimpleLineSymbol.xsd)

简单线符号 XML 模式，如图 C.1 所示。简单线符号 XML 模式中各元素含义如下：

——LineSymbol: 表示简单线符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示符号成员。

——CompositeSymbolCell: 表示复合图元。

——Configuration: 表示符号成员或复合图元的配置规则。

——BasicCell: 表示基本图元。

——RotateAngle: 表示复合图元配置规则中的旋转角度。

——IsTensile: 表示复合图元是否可拉伸变形。

——SymbolRect: 表示复合图元外接矩形大小，当通过 IsTensile 元素控制复合图元可以拉伸时，可按照给定的矩形范围对复合图元在符号配置线方向或符号配置线的垂直方向进行拉伸变化。

——CellType: 表示基本图元类型, 常用基本图元类型可参见附录 A。

——Left: 表示复合图元外接矩形左侧范围。

——Top: 表示复合图元外接矩形顶部范围。

——Right: 表示复合图元外接矩形右侧范围。

——Bottom: 表示复合图元外接矩形底部范围。

——GeometryParas: 表示基本图元图形参数，常用基本图元图形参数可参见附录 A。

——RenderingParas: 表示基本图元绘制参数，常用基本图元绘制参数可参见附录 A。

<div style="text-align: center;"><img src="imgs/img_in_image_box_271_221_821_1505.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 C.1 简单线符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="LineSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="CompositeSymbolCell" minOccurs="1">
                                <xsd:complexType>
                                    <xsd:sequence>
                                        <xsd:element name="BasicCell" minOccurs="1">
                                            <xsd:complexType>
                                                    <xsd:sequence>
                                                        <xsd:element name="CellType" type="xsd:string" minOccurs="1"/>
                                                        <xsd:element name="GeometryParas" minOccurs="1"/>
                                                        <xsd:element name="RenderingParas" minOccurs="1"/>
                                                    </xsd:sequence>
                                                </xsd:complexType>
                                            </xsd:element>
                                        </xsd:element>
                                    </xsd:sequence>
                                </xsd:complexType>
                            </xsd:element>
                        </xsd:complexType>
                    </xsd:element>
                </xsd:complexType>
            </xsd:sequence>
        </xsd:element>
    </xsd:sequence>
</xsd:schema>

<xsd:element name="Top" type="xsd:string" minOccurs="0"/>

<xsd:element name="Right" type="xsd:string" minOccurs="0"/>

<xsd:element name="Bottom" type="xsd:string" minOccurs="0"/>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:sequence>

</xsd:complexType>

#### C.3 组合线符号(CartoLineSymbol.xsd)

组合线符号 XML 模式，如图 C.2 所示。组合线符号 XML 模式中各元素含义如下：

——LineSymbol: 表示组合线符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示符号成员。

——CompositeSymbolCell: 表示复合图元。

——Configuration: 表示符号成员或复合图元的配置规则。

——BasicCell: 表示基本图元, 组合线符号中的基本图元可以由点符号组成。

——SymbolRect: 表示复合图元外接矩形大小，当通过 IsTensile 元素控制复合图元可以拉伸时，将按照给定的矩形范围对复合图元在符号配置线方向或符号配置线的垂直方向进行拉伸变化。

——Left: 表示复合图元外接矩形左侧范围。

——Top: 表示复合图元外接矩形顶部范围。

——Right: 表示复合图元外接矩形右侧范围。

——Bottom: 表示复合图元外接矩形底部范围。

——CartoUnitCount: 表示组合线符号中点符号个数。

——DeltX: 表示组合线符号中点符号在要素配置方向的偏移量。

——DeltY: 表示组合线符号中点符号在要素配置方向的垂直方向的偏移量。

——RotateAngle: 表示组合线符号中点符号的旋转角度。

——RotateType: 表示组合线符号中点符号的旋转类型(可取值为在要素中点或端点)。

<div style="text-align: center;"><img src="imgs/img_in_image_box_251_224_831_1506.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">图 C.2 组合线符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="LineSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1" />
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1" />
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded" />
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="CompositeSymbolCell" minOccurs="1" maxOccurs="unbounded">
                            <xsd:complexType>
                                <xsd:sequence>
                                    <xsd:element name="BasicCell" minOccurs="1" />
                                    <xsd:complexType>
                                        <xsd:sequence>
                                            <xsd:element name="PointSymbol" type="xsd:string" minOccurs="1"/>
                                        </xsd:sequence>
                                    </xsd:complexType>
                                </xsd:element>
                                <xsd:element name="Configuration" minOccurs="1">
                                    <xsd:complexType>
                                        <xsd:sequence>
                                            <xsd:element name="CartoUnitCount" type="xsd:string" minOccurs="1"/>
                                        <xsd:element name="DeltX" type="xsd:string" minOccurs="1"/>
                                    <xsd:element name="DeltY" type="xsd:string" minOccurs="1"/>
                                    <xsd:element name="RotateAngle" type="xsd:string" minOccurs="1"/>
                                    <xsd:element name="RotateType" type="xsd:string" minOccurs="1"/>
                                </xsd:sequence>
                            </xsd:complexType>
                        </xsd:element>
                    </xsd:sequence>
                </xsd:element>
            </xsd:complexType>
        </xsd:sequence>
    </xsd:complexType>
</xsd:schema>

<xsd:complexType>
    <xsd:sequence>
        <xsd:element name="SymbolRect" minOccurs="0">
            <xsd:complexType>
                <xsd:sequence>
                    <xsd:element name="Left" type="xsd:string" minOccurs="0"/>
                    <xsd:element name="Top" type="xsd:string" minOccurs="0"/>
                    <xsd:element name="Right" type="xsd:string" minOccurs="0"/>
                    <xsd:element name="Bottom" type="xsd:string" minOccurs="0"/>
                </xsd:sequence>
            </xsd:complexType>
        </xsd:element>
    </xsd:sequence>
</xsd:complexType>

#### C.4 图片填充线符号(FillLineSymbol.xsd)

图片填充线符号 XML 模式，如图 C.3 所示。图片填充线符号 XML 模式中各元素含义如下：

——LineSymbol: 表示图片填充线符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示符号成员。

——CompositeSymbolCell: 表示复合图元。

——Configuration: 表示符号成员的配置规则, 可以扩展表达填充半径等参数。

——FillType: 表示图片填充线符号中填充图片的填充类型(平铺或拉伸)。

——Width: 表示图片填充线符号中填充图片的宽度。

——Height: 表示图片填充线符号中填充图片的高度。

——ContentBase64: 表示图片填充线符号中填充图片的 Base64 编码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_144_202_1060_489.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 C.3 图片填充线符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="LineSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="CompositeSymbolCell" minOccurs="1" maxOccurs="unbounded">
                                    <xsd:complexType>
                                        <xsd:sequence>
                                            <xsd:element name="FillType" type="xsd:string" minOccurs="1"/>
                                            <xsd:element name="Width" type="xsd:string" minOccurs="1"/>
                                            <xsd:element name="Height" type="xsd:string" minOccurs="1"/>
                                            <xsd:element name="ContentBase64" type="xsd:string" minOccurs="1"/>
                                        </xsd:sequence>
                                    </xsd:complexType>
                                </xsd:element>
                            <xsd:element name="Configuration" minOccurs="0"/>
                        </xsd:sequence>
                    </xsd:complexType>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
</xsd:schema>

</xsd:complexType>

</xsd:element>

</xsd:schema>

#### C.5 渐变填充线符号(GradientLineSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_392_1043_730.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 C.4 渐变填充线符号 XML 模式</div>


渐变填充线符号 XML 模式，如图 C.4 所示。渐变填充线符号 XML 模式中各元素含义如下：

——LineSymbol: 表示渐变填充线符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示符号成员。

——CompositeSymbolCell: 表示复合图元。

——Configuration: 表示符号成员或复合图元的配置规则。

——FillType: 表示渐变类型(线性渐变或径向渐变)。

——StartColor: 表示渐变起始颜色。

——EndColor: 表示渐变终止颜色。

——StartWidth: 表示渐变起始宽度。

——EndWidth: 表示渐变终止宽度。

<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
<xsd:element name="LineSymbol">
    <xsd:complexType>
        <xsd:sequence>
            <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
            <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
            <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                <xsd:complexType>
                    <xsd:sequence>

<xsd:element name="CompositeSymbolCell" minOccurs="1" maxOccurs="unbounded">
    <xsd:complexType>
        <xsd:sequence>
            <xsd:element name="FillType" type="xsd:string" minOccurs="1"/>
            <xsd:element name="StartColor" type="xsd:string" minOccurs="1"/>
            <xsd:element name="EndColor" type="xsd:string" minOccurs="1"/>
            <xsd:element name="StartWidth" type="xsd:string" minOccurs="1"/>
            <xsd:element name="EndWidth" type="xsd:string" minOccurs="1"/>
        </xsd:sequence>
    </xsd:complexType>
</xsd:element>
<xsd:element name="Configuration" minOccurs="0"/>
</xsd:sequence>
</xsd:complexType>
</xsd:element>
</xsd:schema>

#### C.6 晕线填充线符号(HatchedLineSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_1083_1058_1465.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 C.5 晕线填充线符号 XML 模式</div>


晕线填充线符号 XML 模式，如图 C.5 所示。晕线填充线符号 XML 模式中各元素含义如下：

—— LineSymbol：表示晕线填充线符号。

—— SymbolName：表示符号名称。

—— SymbolCode：表示符号代码。

—— SymbolComponent：表示符号成员。

—— CompositeSymbolCell：表示复合图元。

—— Configuration：表示符号成员或复合图元的配置规则。

—— Width：表示晕线宽度。

—— Distance：表示晕线间距。

—— Angle：表示晕线角度。

—— Color：表示晕线颜色。

—— BackColor：表示背景色。

—— Radius：表示晕线的填充半径。

（? xml version="1.0" encoding="utf-8"?）

（xsd:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">

（xsd:element name="LineSymbol">

    （xsd:complexType）

    （xsd:sequence）

    （xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
    （xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
    （xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">

    （xsd:complexType）

    （xsd:sequence）

    （xsd:element name="CompositeSymbolCell" minOccurs="1"
                     maxOccurs="unbounded">

    （xsd:complexType）

    （xsd:sequence）

    （xsd:element name="Width" type="xsd:string"
                     minOccurs="1"/>

    （xsd:element name="Distance" type="xsd:string"
                     minOccurs="1"/>

    （xsd:element name="Angle" type="xsd:string"
                     minOccurs="1"/>

    （xsd:element name="Color" type="xsd:string"
                     minOccurs="1"/>

    （xsd:element name="BackColor" type="xsd:string"
                     minOccurs="1"/>

    （xsd:element name="Radius" type="xsd:string"
                     minOccurs="1"/>

    （/xsd:sequence）

    （/xsd:complexType）

</xsd:element>

<xsd:element name="Configuration" minOccurs="0">
    <xsd:complexType>
        <xsd:sequence>
            <xsd:element name="SymbolRect" minOccurs="0">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="Left" type="xsd:string" minOccurs="0"/>
                        <xsd:element name="Top" type="xsd:string" minOccurs="0"/>
                        <xsd:element name="Right" type="xsd:string" minOccurs="0"/>
                        <xsd:element name="Bottom" type="xsd:string" minOccurs="0"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
</xsd:element>

附录 D

(资料性附录)

面符号 XML 模式

### D.1 介绍

该附录包含了颜色填充面符号、点填充面符号、图片填充面符号、晕线填充面符号、渐变填充面符号和线填充面符号的标准 XML 模式。

D.2 为颜色填充面符号 XML 模式。

D.3 为点填充面符号 XML 模式。

D.4 为图片填充面符号 XML 模式。

D.5 为晕线填充面符号 XML 模式。

D.6 为渐变填充面符号 XML 模式。

D.7 为线填充面符号 XML 模式。

#### D.2 颜色填充面符号(ColorFillSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_256_802_923_968.jpg" alt="Image" width="56%" /></div>


<div style="text-align: center;">图 D.1 颜色填充面符号 XML 模式</div>


颜色填充面符号 XML 模式，如图 D.1 所示。颜色填充面符号 XML 模式中各元素含义如下：

——AreaSymbol: 表示颜色填充面符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——Configuration: 表示颜色填充面符号的配置规则，可根据需要扩展填充颜色是否渐变以及渐变类型等配置方式。

——FillColor: 表示填充颜色。

<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="AreaSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
            </xsd:complexType>
        </xsd:sequence>
    </xsd:complexType>
</xsd:schema>

<xsd:element name="Configuration" minOccurs="1" maxOccurs="unbounded">
    <xsd:complexType>
        <xsd:sequence>
            <xsd:element name="FillColor" type="xsd:string" minOccurs="1"/>
        </xsd:sequence>
    </xsd:complexType>
</xsd:element>
</xsd:sequence>
</xsd:complexType>
</xsd:element>
</xsd:schema>

#### D.3 点填充面符号(PointFillSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_592_1059_1001.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 D.2 点填充面符号 XML 模式</div>


点填充面符号 XML 模式如图 D.2 所示。点填充面符号 XML 模式中各元素含义如下：

——AreaSymbol: 表示点填充面符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示点填充面符号的符号成员。

——CompositeSymbolCell: 表示点填充面符号的复合图元，其由点符号组成。

——Configuration: 表示点填充面符号中符号成员或复合图元的配置规则。

——Angle: 表示填充点符号的旋转角度。

——DeltX：表示填充点符号在水平方向的偏移量。

——DeltY: 表示填充点符号在垂直方向的偏移量。

——AngleRandom: 表示填充的点符号角度是否随机。

——DeltRandom: 表示填充的点符号间距是否随机。

〈? xml version="1.0" encoding="utf-8"?〉
〈xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"

xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">

<xsd:element name="AreaSymbol">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>

<xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>

<xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="CompositeSymbolCell" minOccurs="1" maxOccurs="unbounded">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="PointSymbol" type="xsd:string" minOccurs="1"/>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

<xsd:element name="Configuration" minOccurs="1">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="Angle" type="xsd:string" minOccurs="1"/>

<xsd:element name="DeltX" type="xsd:string" minOccurs="1"/>

<xsd:element name="DeltY" type="xsd:string" minOccurs="1"/>

<xsd:element name="AngleRandom" type="xsd:string" minOccurs="1"/>

<xsd:element name="DeltRandom" type="xsd:string" minOccurs="1"/>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:complexType>

</xsd:sequence>

</xsd:complexType>

#### D.4 图片填充面符号(PictureFillSymbol.xsd)

图片填充面符号 XML 模式如图 D.3 所示。图片填充面符号 XML 模式中各元素含义如下：

——AreaSymbol: 表示图片填充面符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示图片填充面符号的符号成员。

——CompositeSymbolCell: 表示图片填充面符号的复合图元。

——Configuration: 表示图片填充面符号中符号成员或复合图元的配置规则。

——BasicCell：表示图片填充符号基本图元。

——FillType: 表示图片填充类型，可为拉伸或平铺。

——Type: 表示图片填充面符号中填充图片的类型。

——ContentBase64: 图片填充面符号中填充图片的 Base64 编码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_378_227_738_1501.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">图 D.3 图片填充面符号 XML 模式</div>


<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="AreaSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="CompositeSymbolCell" minOccurs="1" maxOccurs="unbounded">
                                <xsd:complexType>
                                    <xsd:sequence>
                                        <xsd:element name="Configuration" type="xsd:string" minOccurs="0"/>
                                        <xsd:element name="BasicCell" minOccurs="1">
                                            <xsd:complexType>
                                                <xsd:sequence>
                                                    <xsd:element name="Type" type="xsd:string" minOccurs="1"/>
                                                <xsd:element name="ContentBase64" type="xsd:string" minOccurs="1"/>
                                            </xsd:sequence>
                                        </xsd:complexType>
                                    </xsd:element>
                                </xsd:sequence>
                                <xsd:element name="Configuration" minOccurs="0" maxOccurs="unbounded">
                                    <xsd:complexType>
                                        <xsd:sequence>
                                            <xsd:element name="Angle" type="xsd:string" minOccurs="0"/>
                                        </xsd:sequence>
                                    </xsd:complexType>
                                </xsd:element>
                            </xsd:sequence>
                        </xsd:complexType>
                    </xsd:sequence>
            </xsd:complexType>
        </xsd:element>
    </xsd:complexType>
</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:schema>

#### D.5 晕线填充面符号(HatchedFillSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_128_391_1040_709.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 D.4 晕线填充面符号 XML 模式</div>


晕线填充面符号 XML 模式如图 D.4 所示。晕线填充面符号 XML 模式中各元素含义如下：

——AreaSymbol: 表示晕线填充面符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示晕线填充面符号的符号成员。

——Configuration: 表示晕线填充面符号中符号成员的配置规则。

——Width: 表示晕线宽度。

——Space: 表示晕线填充间距。

——Angle: 表示晕线角度。

——Color: 表示晕线颜色。

——BackColor: 表示背景色。

<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="AreaSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="Configuration" minOccurs="1" />
                        </xsd:sequence>
                    </xsd:complexType>
                </xsd:sequence>
            </xsd:element>
        </xsd:complexType>
    </xsd:schema>
</xsd:schema>

<xsd:element>

#### D.6 渐变填充面符号(GradientFillSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_144_1012_1058_1233.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 D.5 渐变填充面符号 XML 模式</div>


渐变填充面符号 XML 模式如图 D.5 所示。渐变填充面符号 XML 模式中各元素含义如下：

——AreaSymbol: 表示渐变填充面符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示渐变填充面符号的符号成员。

——Configuration: 表示渐变填充面符号中符号成员配置规则。

——Type: 表示颜色渐变类型(线性渐变或径向渐变)。

——StartColor: 表示渐变起始颜色。

——EndColor: 表示渐变终止颜色。

<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="AreaSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="Configuration" minOccurs="1" maxOccurs="unbounded">
                                    <xsd:complexType>
                                        <xsd:sequence>
                                            <xsd:element name="Type" type="xsd:string" minOccurs="1"/>
                                            <xsd:element name="StartColor" type="xsd:string" minOccurs="1"/>
                                            <xsd:element name="EndColor" type="xsd:string" minOccurs="1"/>
                                        </xsd:sequence>
                                    </xsd:complexType>
                                </xsd:element>
                            </xsd:sequence>
                        </xsd:complexType>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
</xsd:schema>

#### D.7 线填充面符号(LineFillSymbol.xsd)

<div style="text-align: center;"><img src="imgs/img_in_image_box_126_1287_1044_1487.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 D.6 线填充面符号 XML 模式</div>


线填充面符号 XML 模式如图 D.6 所示。线填充面符号 XML 模式中各元素含义如下：

——AreaSymbol: 表示线填充面符号。

——SymbolName: 表示符号名称。

——SymbolCode: 表示符号代码。

——SymbolComponent: 表示线填充面符号的符号成员。

——CompositeSymbolCell: 表示线填充面符号的复合图元，其由要填充的线符号 LineSymbol 组成。

——Configuration: 表示线填充面符号中符号成员或复合图元的配置规则。

——Space: 表示线符号的填充间距。

——Angle: 表示线符号的填充角度。

<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns="xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:element name="LineFillSymbol">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="SymbolName" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolCode" type="xsd:string" minOccurs="1"/>
                <xsd:element name="SymbolComponent" minOccurs="1" maxOccurs="unbounded">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="CompositeSymbolCell" minOccurs="1">
                                <xsd:complexType>
                                    <xsd:sequence>
                                        <xsd:element name="LineSymbol" type="xsd:string" minOccurs="1"/>
                                    </xsd:sequence>
                                </xsd:complexType>
                            </xsd:element>
                        </xsd:complexType>
                    </xsd:element>
                </xsd:element name="Configuration" minOccurs="1">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="Space" type="xsd:string" minOccurs="1"/>
                    </xsd:element>
                </xsd:element>
                <xsd:element name="Angle" type="xsd:string" minOccurs="1"/>
                </xsd:sequence>
            </xsd:complexType>
        </xsd:element>
    </xsd:sequence>
</xsd:complexType>

</xsd:sequence>

</xsd:complexType>

 $ \langle /xsd:element \rangle $ 

 $ \langle /xsd:schema \rangle $ 

附录 E

（资料性附录）

符号库 XML 模式

E.1 该附录包含了符号库的标准 XML 模式，见图 E.1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_257_395_944_936.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">图 E.1 符号库 XML 模式</div>


E.2 符号库 XML 模式中各元素含义如下：

SymbolDB: 表示符号库。

——Name: 表示符号库名称。

——Scale: 表示符号库比例尺。

——Organization: 表示符号库制作单位。

——Producer: 表示符号库制作人。

——DateTime: 表示符号库制作时间。

——Ratio: 表示符号库映射比例。

——PointSymbols: 表示点符号集合。

——LineSymbols: 表示线符号集合。

——AreaSymbols: 表示面符号集合。

——PointSymbol: 表示点符号。

——LineSymbol: 表示线符号。

——AreaSymbol: 表示面符号。

<?xml version="1.0" encoding="utf-8"?>

<xsd:schema xmlns="{{xmlns:xs="http://www.w3.org/2001/XMLSchema}}"

xmlns:msdata="urn:schemas-microsoft-com:xml-msdata"

<xsd:element name="SymbolDB">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="Name" type="xsd:string" minOccurs="1"/>

<xsd:element name="Scale" type="xsd:string" minOccurs="1"/>

<xsd:element name="Organization" type="xsd:string" minOccurs="1"/>

<xsd:element name="Producer" type="xsd:string" minOccurs="1"/>

<xsd:element name="DateTime" type="xsd:string" minOccurs="1"/>

<xsd:element name="Ratio" type="xsd:string" minOccurs="1"/>

<xsd:element name="PointSymbols" minOccurs="0" maxOccurs="1">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="PointSymbol" type="xsd:string" minOccurs="0" maxOccurs="unbounded"/>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

<xsd:element name="LineSymbols" minOccurs="0" maxOccurs="1">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="LineSymbol" type="xsd:string" minOccurs="0" maxOccurs="unbounded"/>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

<xsd:element name="AreaSymbols" minOccurs="0" maxOccurs="1">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="AreaSymbol" type="xsd:string" minOccurs="0" maxOccurs="unbounded"/>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:complexType>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:complexType>

## 參 考 文 献

[1] GB/T 16820—2009 地图学术语

[2] GB/T 20257.1—2006 国家基本比例尺地图图式 第1部分：1:500 1:1000 1:2000 地形图图式

[3] GB/T 20257.2—2006 国家基本比例尺地图图式 第2部分：1:5000 1:10000 地形图图式

[4] GB/T 20257.3—2006 国家基本比例尺地图图式 第3部分：1:250001:500001:100000 地形图图式

[5] GB/T 20257.4—2007 国家基本比例尺地图图式 第4部分：1:2500001:5000001:1000000地形图图式

[6] CH/T 4015—2001 地图符号库建立的基本规定

[7] CH/T 4017—2012 矢量地图符号制作规范

[8] CH/Z 9011—2011 地理信息公共服务平台电子地图数据规范

[9] ISO 19117:2012 Geographic information—Portrayal

[10] FGDC-STD-013-2006 FGDC Digital Cartographic Standard for Geologic Map Symbolization

[11] OGC 02-070 Styled Layer Descriptor Implementation Specification

[12] OGC 05-077r4 Symbology Encoding Implementation Specification