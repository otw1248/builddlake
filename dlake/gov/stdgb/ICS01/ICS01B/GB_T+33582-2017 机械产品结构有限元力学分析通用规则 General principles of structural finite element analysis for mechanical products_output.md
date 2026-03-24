

# 中华人民共和国国家标准

GB/T 33582—2017

# 机械产品结构有限元力学分析通用规则

# General principles of structural finite element analysis for mechanical products

2017-05-12 发布

2017-09-01 实施

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国技术产品文件标准化技术委员会(SAC/TC 146)提出并归口。

本标准主要起草单位：中国电子科技集团公司第三十八研究所、上海湃睿信息科技有限公司、合肥京联信息科技有限公司、北京科新纪元信息技术有限公司、中机生产力促进中心。

本标准主要起草人：王梅、张红旗、林劲松、潘康华、刘静、杨静、毛亮、王学勤、胡祥涛、马春雷、高宏伟。

# 机械产品结构有限元力学分析通用规则

## 1 范围

本标准规定了机械产品结构有限元力学分析的类型、流程、一般要求、模型建立规则、有限元分析（简称“分析”）、结果评估、结果输出、报告编写。

本标准适用于机械产品结构的有限元力学分析。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2298—2010 机械振动、冲击与状态监测 词汇

GB 3100—1993 国际单位制及其应用

GB 3101—1993 有关量、单位和符号的一般原则

GB/T 10853—2008 机构与机器科学词汇

GB/T 26099.1—2010 机械产品三维建模通用规则 第1部分：通用要求

GB/T 31054—2014 机械产品计算机辅助工程 有限元数值计算 术语

## 3 术语和定义

GB/T 2298—2010、GB 3100—1993、GB 3101—1993、GB/T 10853—2008、GB/T 26099.1—2010 和 GB/T 31054—2014 界定的以及下列术语和定义适用于本文件。

3.1

## 有限元建模 finite element modeling

构建有限元模型的过程，包括几何模型构建和（或）处理、材料属性定义、网格划分、边界条件施加等步骤。

### 3.2 

## 材料属性 material property

描述机械产品结构所用材料物理特性的数据集合。

### 3.3 

## 边界条件 boundary condition

描述机械产品结构在给定工况下，求解域边界上几何以及物理条件，如力、温度、速度、位移等载荷的数据信息。

3.4

## 应力集中 stress concentration

结构局部过渡区域刚度急剧变化引起的应力数值明显增高的现象。

### 3.5 

## 节点 node

单元之间的铰接点。

注：每个单元仅在节点处和相邻单元及外部发生联系。

[GB/T 31054—2014, 定义 3.1.5]

### 3.6 

## 单元 element

具有几何、物理属性的最小求解域。

[GB/T 31054—2014, 定义 3.1.4]

### 3.7 

## 零 维单元 zero dimensional element

表现形式为点的单元,如质量单元等。

### 3.8 

## 一 维单元 one dimensional element

表现形式为线段的单元，如刚性单元、杆单元、梁单元等。

[GB/T 31054—2014, 定义 3.3.6]

### 3.9 

## 二 维单元 two dimensional element

表现形式为平面片的单元，如矩形单元、三角形单元等。

[GB/T 31054—2014, 定义 3.3.7]

### 3.10 

## 三 维单元 three dimensional element

表现形式为实体的单元,如四面体单元、六面体单元等。

[GB/T 31054—2014, 定义 3.3.8]

### 3.11 

## 质量单元 mass element

表征只具备质量属性的单元。

### 3.12 

## 弹簧单元 spring element

表征结构之间具有弹簧约束作用的单元。

### 3.13 

## 杆 bar

一类长度远大于其他方向尺寸的构件。

[GB/T 31054—2014, 定义 4.1.4]

### 3.14 

## 梁 beam

一类承受横向载荷，以弯曲变形为主的杆结构。

[GB/T 31054—2014, 定义 4.1.3]

### 3.15 

## 板/壳 plane/shell

一类厚度方向尺寸远小于长度和宽度方向尺寸的结构。

注：表面为平面的称为板，表面为曲面的称为壳。

[GB/T 31054—2014, 定义 4.1.4]

### 3.16 

## 实体 solid body

由面或棱边构成封闭体积的三维几何体。

[GB/T 26099.1—2010, 定义 3.2]

### 3.17 

## 高阶单元 high order element

使用二次或更高次函数描述边界的单元。

### 3.18 

## 低阶单元 low order element

使用一次函数描述边界的单元。

### 3.19 

## 约束 constraint

减少系统自由度的各种限制条件。

[GB/T 10853—2008, 定义 3.3.13]

### 3.20 

## 位移 displacement

表征物体上一点相对于某参考系的位置变化的时间变量。

[GB/T 2298—2010, 定义 2.1]

### 3.21 

## 载荷 loads

施加在物体上或系统上作用力系。

[GB/T 10853—2008 中, 定义 5.2.58]

### 3.22 

## 强度 strength

描述结构抵抗破坏的能力。

[GB/T 31054—2014, 定义 4.1.5]

### 3.23 

## 刚度 stiffness

描述结构抵抗变形的能力。

[GB/T 31054—2014, 定义 4.1.6]

### 3.24 

## 结构静力学分析 structural statics analysis

在静态或可近似静态载荷作用下，时间参数对分析无影响的结构响应分析。

[GB/T 31054—2014, 定义 3.1.10]

### 3.25 

## 结构动力学分析 structural dynamics analysis

在时变载荷以及惯性和阻尼效应作用下，对结构动力学特性和响应的分析。

[GB/T 31054—2014, 定义 3.1.11]

### 3.26 

## 长宽比 aspect ratio

描述二维或三维单元最长边与最短边之比的量。

### 3.27 

## 长细比 slenderness

杆件的计算长度与杆件截面的回转半径之比。

### 3.28 

翘曲度 warpage

单元偏离平面的程度，用于检查单元的翘曲。

### 3.29 

偏斜度 skew

描述单元的扭曲程度的数学量。

### 3.30 

## 内角 interior angle

指三角形单元或四边形单元的夹角的值，常用于描述单元的最大内角或者最小内角的数学量。

## 4 类型

### 4.1 结构静力学分析

当惯量和阻尼对结构力学性能不产生影响或影响很小时，采用静力学分析。

### 4.2 结构动力学分析

主要包括模态分析、谐响应分析、谱分析和瞬态动力学分析。当惯量和阻尼对结构力学性能的影响不可忽略时，需采用动力学分析。

## 5 流程

机械产品结构有限元力学分析流程主要包括有限元建模、有限元分析、有限元分析结果评估、有限元结果输出及分析报告编写等5部分，具体参见附录A。

## 6 一般要求

6.1 有限元模型建立前，应根据机械产品的结构特点、载荷和约束（或者边界条件）特点、仿真目的、仿真周期和计算资源制定有限元分析方案。

6.2 几何模型简化时，在确保关注部位有限元分析精度的前提下尽可能的简化结构的棱角、小凸台、小凹槽等几何模型细节特征。

6.3 单元选择时，应根据机械产品几何模型、载荷及约束特点和有限元分析的类型及目的，合理选择单元的类型，以保证计算精度。

6.4 网格划分时，应粗化应力缓慢变化区域，细化应力急剧变化区域；粗化不关注区域（仅为力传递而建入模型的区域）、细化关注区域。

6.5 计算方法选择时，应根据机械产品结构有限元力学分析类型、分析结果要求、算法的适用范围与优缺点、有限元模型的规模和计算机资源来确定。

6.6 分析模型和计算结果评估应根据分析类型和试验结果进行。

6.7 分析结果(列表、等值线图、曲线图等)应根据有限元分析的目的和要求输出。

## 7 模型建立规则

### 7.1 坐标系

坐标系由右手定则来确定，宜选用笛卡尔直角坐标系，必要时可选用柱坐标系或球坐标系。

有限元分析建模时应定义全局坐标系，当模型载荷、约束或结果显示需求与全局坐标系不一致时，可增加局部坐标系。

### 7.2 单位制

单位制的选择应按照 GB 3100—1993 和 GB 3101—1993 执行。根据机械产品特点选择 SI 单位制或其他单位制。例如，对质量较敏感的机械产品推荐采用 SI 单位制，质量单位为千克，具体参见附录 B 中表 B.1；对质量不敏感的大型机械产品推荐采用 SI 单位制倍数单位，质量单位为吨，具体参见表 B.2。

### 7.3 几何模型构建

#### 7.3.1 构建原则

7.3.1.1 几何模型应简洁准确地表达机械产品结构设计信息。

7.3.1.2 在满足要求的情况下，尽量使模型简化。

#### 7.3.2 构建要求

几何模型应按 GB/T 26099.1—2010 中第 6 章的规定进行构建。

几何模型的构建应符合以下要求：

a）几何模型的命名应采用软件可识别的字符，并要保持唯一性；

b）几何模型宜按1:1的比例关系建立；

c）长细比大于8的结构，宜选取中间轴线构建；

d）典型结构尺寸与壁厚比值大于10的结构，宜选取中面构建；

e）不适合采用线、面构建的结构以及结构的关键部位，应采用实体构建。

### 7.4 有限元网格划分

#### 7.4.1 单元类型选择

机械产品单元类型的选择应能反映不同部件的结构形式，有限元单元类型包括零维单元（如质量单元）、一维单元（如刚性单元、杆单元、梁单元）、二维单元（如壳单元）、三维单元（如体单元）。建模时应根据结构的几何特点及需求，合理选择单元类型。

#### 7.4.2 单元阶次选择

7.4.2.1 结构形状不规则、变形和应力分布复杂时宜选用高阶单元。

7.4.2.2 计算精度要求高的区域宜选用高阶单元，精度要求低的可选用低阶单元。

7.4.2.3 不同阶次单元的连接位置应使用过渡单元或多点约束等。

#### 7.4.3 网格疏密控制

7.4.3.1 应对结构变化大、曲面曲率变化大、载荷变化大或不同材料连接的部位进行细化。

7.4.3.2 单元尺寸过渡平滑，粗细网格之间应有足够的单元进行过渡，避免相邻单元的质量和刚度差别太大。

7.4.3.3 应力响应关注区域的网格密度应大于位移响应关注区域的网格密度。

7.4.3.4 主承力方向的单元尺寸应较小，垂直于该方向的单元在满足质量要求时可以将尺寸稍作放大。

#### 7.4.4 网格划分

7.4.4.1 应保留主要的几何轮廓线，网格应与几何轮廓保持基本一致。

7.4.4.2 对于实体单元网格，在结构厚度方向上应确保三层以上。

7.4.4.3 对称结构宜采用对称网格。

### 7.5 材料属性设置

7.5.1 材料属性单位应与几何模型单位一致。

7.5.2 材料属性输入信息应准确完整，能准确表达结构的刚度、质量和阻尼特性。

7.5.3 经过试验验证的材料属性信息宜作为数据积累，为材料属性设置作参考。

### 7.6 边界条件施加

#### 7.6.1 约束

7.6.1.1 机械产品有限元模型约束施加应符合实际安装条件。

7.6.1.2 根据约束类型选择施加方式。

注：固支应选择全部自由度约束；铰支应选择平动自由度约束；对称结构应选择对称或反对称约束。

7.6.1.3 约束区域应能准确反映实际约束情况。应避免单点约束，以防止应力集中；若实际约束区域小于一个单元时，应约束四个以上节点或细化网格。

#### 7.6.2 载荷

7.6.2.1 按实际载荷选择载荷类型。结构静力学分析常用的载荷包括重力载荷、加速度载荷、冰雪载荷、风载荷、温度载荷、位移载荷等；结构动力学分析常用的载荷包括冲击载荷、振动载荷、谱载荷等。

7.6.2.2 载荷大小、方向和作用区域应符合实际载荷情况。

7.6.2.3 经过试验验证的载荷信息宜作为数据积累，为载荷施加作参考。

### 7.7 有限元模型检查

#### 7.7.1 网格检查

划分网格时，应对网格单元进行检查，具体检查内容及要求如下：

a）模型中不应存在畸变网格，网格检查的主要参数包括单元方向、长宽比、翘曲度、偏斜度、内角等方面。网格划分时，上述参数推荐的量化数值要求参见表B.3。

b）保证结构重点关注区域的单元高质量，非重点关注区域的单元质量可适当降低。

#### 7.7.2 质量特性检查

在有限元建模中，应对影响计算准确性的模型质量分布、总质量、质心分布等因素进行检查，检查配重后模型各部分质量分布、质心是否与实际状态一致。

#### 7.7.3 工程特性检查

划分网格结束后，应对有限元模型进行工程特性检查，具体检查内容及要求如下：

a）材料参数检查。依据机械产品结构设计时的材料特性，对材料参数进行复核，检查材料参数是否与设计一致。

b）单元类型检查。依据机械产品几何特点、分析需求和装配方式，对单元类型进行检查，检查单元类型的选择是否与结构形式和连接方式一致。

c）约束检查。依据机械产品结构安装接口，对约束进行检查，检查约束是否与安装条件一致。

d）载荷检查。依据机械产品结构工作载荷条件，对载荷进行检查，检查载荷类型、载荷作用对象等是否与工作载荷条件一致。

<div style="text-align: center;"><img src="imgs/img_in_image_box_71_472_107_507.jpg" alt="Image" width="3%" /></div>


8 分析  
  
8.1 静力学分析  
  
8.1.1 计算时多采用默认求解设置。  
  
8.1.2 在满足收敛性、计算精度和计算机资源的条件下，设置合理的计算时间步长。  
  
8.2 动力学分析  
  
8.2.1 模态分析  
  
8.2.1.1 计算时通常采用分块 Lanczos 法。  
  
8.2.1.2 根据模态个数及模态计算方法设置合理的模态阶数或模态上限。  
  
8.2.2 谐响应分析  
  
8.2.2.1 计算时通常采用直接积分法，当计算效率低时，可采用模态叠加法。  
  
8.2.2.2 施加非零位移时不应采用模态叠加法。  
  
8.2.2.3 采用模态叠加法提取模态时应提取对振动响应有贡献的所有模态。  
  
8.2.3 谱分析  
  
8.2.3.1 计算时宜采用分块 Lanczos 法，先提取模态。  
  
8.2.3.2 提取的模态数应提取关注频段内对振动响应有贡献的所有模态。  
  
8.2.3.3 应定义激励谱与激励方向。  
  
8.2.4 瞬态动力学分析  
  
8.2.4.1 计算时宜采用直接积分法，当计算效率低时，可采用模态叠加法。  
  
8.2.4.2 施加非零位移时不应选择模态叠加法。  
  
8.2.4.3 采用模态叠加法时应采用恒定时间步长。  
  
9 结果评估  
  
9.1 评估方法  
  
9.1.1 表象评估法  
  
通过结果表象进行定性评估，具体原则如下：  
  
a) 检查模型的收敛性；  
  
b) 分析应力集中位置的合理性；  
  
c) 根据结构振动响应曲线和模态计算结果，分析产生的波峰波谷的合理性。  
  
9.1.2 数值评估法  
  
多次试算调整有限元模型的位移边界和模型参数，数值评估分析结果的可靠性。  
  
9.1.3 物理样机法

进行物理样机试验，对比有限元分析结果和试验结果，如偏差较大，以试验结果为依据修正有限元

分析模型重新计算后评估。

### 9.2 评估方法选择

应采用表象和数值两种评估方法对分析结果进行评价，必要时，采用物理样机法进行评估。评估后，如分析结果与结构实际状态存在偏差，需根据情况，对有限元模型的单元类型、阶次、网格尺寸、材料属性及边界条件进行修正，并重新计算和评估，直到结果满足评估要求。

## 10 结果输出

### 10.1 静力学分析结果输出

静力学分析结果的提取和输出至少应包含以下信息：

a）显示或输出结果前应读入关注部位的结果数据；

b）输出结果应包含关注部位的应力、应变和变形等值线图的全部或部分内容。

### 10.2 模态分析结果输出

模态分析结果的提取和输出至少应包含以下信息：

a）显示或输出结果前应读入关注的所有模态阶数的结果数据；

b）输出结果应包含关注频段内的固有频率、模态振型、相对应力和相对应变等值线图的全部或部分内容。

### 10.3 谐响应分析结果输出

谐响应分析结果的提取和输出至少应包含以下信息：

a）显示或输出结果前应先读取关注频率点的计算结果；

b）根据结构关注区域典型位置节点的振动响应（位移、应力、应变、力等）频谱曲线的极值，确定需要重点关注的振动响应分布的频率值；

c）计算放大系数时，应按照激励的类型（加速度或速度）将振动位移响应转换为同类型的量纲；

d) 谐响应分析输出的结果应包含结构在关注频段内关注测点的振动位移、速度、加速度、应力等变量的幅值、相位、实部或虚部与频率关系曲线，典型频率激励下的结构变形、应力、应变等值线、矢量图或列表，关注频段内关注测点的放大系数与频率关系曲线的全部或部分内容。

### 10.4 谱分析结果输出

谱分析结果的提取和输出至少应包含以下信息：

a）显示或输出结果前应先读取关注频率点的计算结果；

b）谱分析结果的输出应包含结构 $ 1\sigma $ 位移、速度、加速度、应力、应变、力的等值图和关注点的功率谱密度曲线。

### 10.5 瞬态动力学分析结果输出

瞬态动力学分析结果的提取和输出至少应包含以下信息：

a）显示或输出结果前应先读取关注时间点的计算结果；

b）根据结构关注区域典型位置节点的振动响应（位移、应力、应变、力等）时间历程曲线的极值确定应重点关注的振动响应的临界时间点；

c) 瞬态动力学分析输出的结果应包含结构关注测点的位移、速度、加速度、应力等变量的时间历程曲线，典型时间点的结构变形、应力、应变等值线、矢量图或列表。

## 11 报告编写

### 11.1 报告编写内容

针对具体分析对象、分析目的、分析问题编写有限元分析报告，报告编写内容至少应包括以下方面：

a）报告名称；

b） 分析对象；

c） 分析问题。

### 11.2 任务概述

应对分析问题进行一定的背景介绍，并说明本报告所采取的分析类型和拟关注的分析结果。

### 11.3 引用文件

包含其他文件的数据或结论时，应在报告中相应部分明确指出，并给出引用文件的作者、名称和时间。

### 11.4 符号说明

对初次出现的符号应做必要的解释说明，下文继续引用时可直接引用。

### 11.5 分析过程

分析过程包括了模型简化、网格划分、材料模型、边界条件、载荷和求解方式，应对上述逐个进行必要的说明。

### 11.6 结果分析和结论

应给出典型的图表结果，如应力/应变云图、模态振型等。图表应简明、易懂，图表中不应有无关的信息。

根据给出的图表结果，总结分析结论，如刚强度特性、振动特性等。

### 11.7 参考文件

相关的参考文献、报告等应在报告最后进行标明，包括参考文件的作者、全名和发表时间等相关信息。

附录 A

（资料性附录）

机械产品结构有限元力学分析流程图

机械产品结构有限元力学分析常用流程如图 A.1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_415_387_754_1094.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 A.1 机械产品结构有限元力学分析常用流程图</div>


# 附录 B

(资料性附录)

# 单位制系统及单元质量检查指标

### B.1 SI 单位制系统

表 B.1 给出了对质量较敏感的机械产品分析建模时推荐采用的 SI 单位制。

<div style="text-align: center;">表 B.1 SI 单位制系统</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">物理量名称</td><td colspan="2">SI基本单位制系统</td></tr><tr><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>单位符号</td></tr><tr><td style='text-align: center;'>长度</td><td style='text-align: center;'>米</td><td style='text-align: center;'>m</td></tr><tr><td style='text-align: center;'>质量</td><td style='text-align: center;'>千克</td><td style='text-align: center;'>kg</td></tr><tr><td style='text-align: center;'>时间</td><td style='text-align: center;'>秒</td><td style='text-align: center;'>s</td></tr><tr><td style='text-align: center;'>温度</td><td style='text-align: center;'>开[尔文]</td><td style='text-align: center;'>K</td></tr><tr><td style='text-align: center;'>—</td><td colspan="2">SI导出单位制系统</td></tr><tr><td style='text-align: center;'>力</td><td style='text-align: center;'>牛顿</td><td style='text-align: center;'>N</td></tr><tr><td style='text-align: center;'>应力</td><td style='text-align: center;'>帕</td><td style='text-align: center;'>Pa(N/m²)</td></tr><tr><td style='text-align: center;'>力矩</td><td style='text-align: center;'>牛顿米</td><td style='text-align: center;'>N·m</td></tr><tr><td style='text-align: center;'>密度</td><td style='text-align: center;'>千克每立方米</td><td style='text-align: center;'>kg/m³</td></tr><tr><td style='text-align: center;'>位移</td><td style='text-align: center;'>米</td><td style='text-align: center;'>m</td></tr><tr><td style='text-align: center;'>速度</td><td style='text-align: center;'>米每秒</td><td style='text-align: center;'>m/s</td></tr><tr><td style='text-align: center;'>加速度</td><td style='text-align: center;'>米每二次方秒</td><td style='text-align: center;'>m/s²</td></tr><tr><td style='text-align: center;'>频率</td><td style='text-align: center;'>赫兹</td><td style='text-align: center;'>Hz</td></tr></table>

### B.2 单位制系统 2

表 B.2 给出了对质量不敏感的大型机械产品有限元分析建模要求时推荐采用的单位制系统。

<div style="text-align: center;">表 B.2 单位制系统 2</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">物理量名称</td><td colspan="2">单位制系统2</td></tr><tr><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>单位符号</td></tr><tr><td style='text-align: center;'>长度</td><td style='text-align: center;'>毫米</td><td style='text-align: center;'>mm</td></tr><tr><td style='text-align: center;'>质量</td><td style='text-align: center;'>吨</td><td style='text-align: center;'>t</td></tr><tr><td style='text-align: center;'>时间</td><td style='text-align: center;'>秒</td><td style='text-align: center;'>s</td></tr><tr><td style='text-align: center;'>温度</td><td style='text-align: center;'>开[尔文]、摄氏度</td><td style='text-align: center;'>K、℃</td></tr></table>

<div style="text-align: center;">表 B.2 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">物理量名称</td><td colspan="2">单位制系统2</td></tr><tr><td style='text-align: center;'>单位名称</td><td style='text-align: center;'>单位符号</td></tr><tr><td style='text-align: center;'>力</td><td style='text-align: center;'>牛顿</td><td style='text-align: center;'>N</td></tr><tr><td style='text-align: center;'>应力</td><td style='text-align: center;'>兆帕</td><td style='text-align: center;'>MPa(N/mm²)</td></tr><tr><td style='text-align: center;'>力矩</td><td style='text-align: center;'>牛顿毫米</td><td style='text-align: center;'>N·mm</td></tr><tr><td style='text-align: center;'>密度</td><td style='text-align: center;'>吨每立方毫米</td><td style='text-align: center;'>t/mm³</td></tr><tr><td style='text-align: center;'>位移</td><td style='text-align: center;'>毫米</td><td style='text-align: center;'>mm</td></tr><tr><td style='text-align: center;'>速度</td><td style='text-align: center;'>毫米每秒</td><td style='text-align: center;'>mm/s</td></tr><tr><td style='text-align: center;'>加速度</td><td style='text-align: center;'>毫米每二次方秒</td><td style='text-align: center;'>mm/s²</td></tr><tr><td style='text-align: center;'>频率</td><td style='text-align: center;'>赫兹</td><td style='text-align: center;'>Hz</td></tr></table>

### B.3 单元质量检查

表 B.3 给出了有限元分析建模要求中单元质量检查控制参数。

<div style="text-align: center;">表 B.3 单元质量检查控制参数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>四边形单元</td><td style='text-align: center;'>三角形单元</td><td style='text-align: center;'>六面体单元</td><td style='text-align: center;'>楔形单元</td><td style='text-align: center;'>四面体单元</td></tr><tr><td style='text-align: center;'>长宽比</td><td style='text-align: center;'>≤5.0</td><td style='text-align: center;'>≤5.0</td><td style='text-align: center;'>≤5.0</td><td style='text-align: center;'>≤5.0</td><td style='text-align: center;'>≤5.0</td></tr><tr><td style='text-align: center;'>翘曲度</td><td style='text-align: center;'>≤16°</td><td style='text-align: center;'>—</td><td style='text-align: center;'>≤18°</td><td style='text-align: center;'>≤18°</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>偏斜度</td><td style='text-align: center;'>≤60°</td><td style='text-align: center;'>≤60°</td><td style='text-align: center;'>≤60°</td><td style='text-align: center;'>≤60°</td><td style='text-align: center;'>≤60°</td></tr><tr><td style='text-align: center;'>内角</td><td style='text-align: center;'>40°~135°</td><td style='text-align: center;'>20°~120°</td><td style='text-align: center;'>40°~135°</td><td style='text-align: center;'>20°~120°</td><td style='text-align: center;'>20°~120°</td></tr></table>