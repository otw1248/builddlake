

# 中华人民共和国国家标准

GB/T 38368—2019

# 产品几何技术规范(GPS) 基于数字化模型的测量通用要求

# Geometrical product specifications (GPS)—Requirements of digital model-based measurement

2019-12-31 发布

2020-07-01 实施

国家市场监督管理总局发布

国家标准化管理委员会

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由全国产品几何技术规范标准化技术委员会(SAC/TC 240)提出并归口。

本标准起草单位：中国电子科技集团公司第三十八研究所、中国计量科学研究院、机械科学研究总院青岛分院有限公司、上海大学、深圳市计量质量检测研究院、中机生产力促进中心、国家重大技术装备几何量计量站、海克斯康测量技术（青岛）有限公司。

本标准主要起草人：魏一雄、王为农、李明、明翠新、周红桥、于冀平、段玲、张红旗、王慧珍、朱悦。

# 产品几何技术规范(GPS) 基于数字化模型的测量通用要求

## 1 范围

本标准规定了机械结构几何要素基于数字化模型测量的数字化模型要求、测量模型构建、测量过程设计、测量实施等的通用要求。

本标准适用于基于数字化模型机械结构的尺寸、形状、方向、位置等几何要素的数字化测量。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 1958 产品几何技术规范(GPS) 几何公差 检测与验证

GB/T 3177 产品几何技术规范(GPS) 光滑工件尺寸的检验

GB/T 18779.1 产品几何量技术规范(GPS) 工件与测量设备的测量检验 第1部分: 按规范检验合格或不合格的判定规则

GB/T 18779.2—2004 产品几何量技术规范(GPS) 工件与测量设备的测量检验 第2部分:测量设备校准和产品检验中 GPS 测量的不确定度评定指南

GB/T 19022—2003 测量管理体系 测量过程和测量设备的要求

GB/T 24734（所有部分） 技术产品文件 数字化产品定义数据通则

GB/T 26099（所有部分） 机械产品三维建模通用规则

GB/T 26498 工业自动化系统与集成 物理设备控制 尺寸测量接口标准(DMIS)

JJF 1001—2011 通用计量术语及定义

## 3 术语和定义

GB/T 3177、GB/T 18779.1、GB/T 19022—2003、GB/T 24734.1 和 JJF 1001—2011 界定的以及下列术语和定义适用于本文件。为了便于使用，以下重复列出了 GB/T 19022—2003 和 JJF 1001—2011 中的某些术语和定义。

### 3.1 

## 数字化模型 digital model

在计算机辅助设计平台上，由数字化的工程或产品的方案、草图、原图、技术性说明及其他技术图样和技术文件所构成的模型。

注：该模型在计算机平台上可编辑、可复制，为开展制造、测量等后续阶段相关工作进行补充设计，且构成包含该阶段操作规范的新的数字化模型。

### 3.2 

## 测量模型 measurement model

包含了规范化的测量操作信息的数字化模型。

注：测量操作信息包含测量要求、测量前端数据、测量过程数据、测量结果数据的格式以及这些数据生成的相关规范信息等。

### 3.3 

测量过程 measurement process

确定量值的一组操作。

[GB/T 19022—2003, 定义 3.2]

### 3.4 

测量前端数据 front data of measurement

根据测量要求，基于数字化模型及相应标注信息（如尺寸参数、公差参数等）提取的基础信息数据。

### 3.5 

测量过程数据 process data of measurement

根据测量要求和测量前端数据，开展测量操作所生成的需要的信息数据。

### 3.6 

测量结果数据 result data of measurement

测量操作的输出信息数据。

### 3.7 

## 测量不确定度 uncertainty of measurement

根据所用到的信息，表征赋予被测量值分散性的非负参数。

注 $ ^{1} $ ：此参数可以是诸如称为标准测量不确定度的标准差（或其特定倍数），或是说明了包含概率的区间半宽度。

注2：通常，对于一组给定的信息，测量不确定度是相应于所赋予被测量的值。

[JJF 1001—2011, 定义 5.18]

## 4 数字化模型要求

4.1 数字化模型应符合 GB/T 26099、GB/T 24734 的规定。

4.2 数字化模型应满足测量操作所需信息的完整性要求，即：除自身几何特征信息之外，应包含可被识别/提取的前端设计/工艺信息，如被测要素尺寸、公差、基准等。

4.3 测量优先选择原始格式数字化模型，若需要将数字化模型转换为测量软件可识别的格式，应保证转换后模型满足上述两个要求，确保测量信息准确性。

## 5 测量模型的构建

### 5.1 测量要求的确定

5.1.1 明确被测对象，并根据测量要求转换成测量过程设计可操作的输入。

注：转换工作主要包括被测对象的分离、对于“任一”等测量要求的明确、具体测量内容、辅助测量内容以及测量频次和数据处理方法等。

5.1.2 在进行测量操作之前，应充分了解被测要素的属性、特点以及被测对象所处测量环境条件等因素。

### 5.2 输出参数的确定及目标不确定度设定

5.2.1 输出参数应满足测量要求，输出参数的不确定度应满足测量要求对应的准确度要求。

5.2.2 对于事先给定了测量过程的目标不确定度设定，应遵循 GB/T 18779.2—2004 中 6.2 所述规范进行管理。

5.2.3 对于测量过程未确定的不确定度设定，应遵循 GB/T 18779.2—2004 中 6.3 所述规范，即不确定管理程序 (Procedure for Uncertainty Management, PUMA) 进行管理。

### 5.3 测量过程的描述

5.3.1 测量过程的描述应采用与数字化模型相对偶的信息数据表示。

5.3.2 测量过程的描述数据应由测量过程设计得到。

5.3.3 测量过程描述数据应包含由目标不确定度根据 PUMA 方法确立的测量方法、测量程序、测量条件，即理想检验操作集。

5.3.4 测量过程描述数据应与一个或一组可以表达被测要素特征的几何模型特征，或与某一几何模型特征的某一部分关联，例如，形状、位置测量数据定义应关联被测要素形状、位置特征。

### 5.4 测量模型规范

#### 5.4.1 测量模型构成

测量模型包含以下内容：

a）由前端继承的数字化模型；

b）包含特征、被测要素等的前端数据；

c) 包含测量方法、测量路径等的过程设计数据的理想操作集；

d）测量操作数据及结果数据格式。

注：测量模型分阶段输出，在测量过程设计阶段，测量模型的输出仅包括 a)、b) 内容；在测量实施阶段，测量模型的输出需包含上述全部内容。

#### 5.4.2 测量模型要求

5.4.2.1 前端数据一般包含被测要素、特征、评价规则、尺寸/公差/位置/基准、理论值、属性等数据，数据结构应和通用数据格式兼容，如 DMIS。

5.4.2.2 前端数据宜通过如图 1 所示的框格形式在几何模型上进行标注，基本的标注方法和要求（如标注面、指引线、关联性等）符合 GB/T 24734 的规定。

 $$ \begin{array}{l}\mathbf{a}:(x_{1},y_{1},z_{1})\mathbf{c}:(x_{3},y_{3},z_{3})\\ \mathbf{b}:(x_{2},y_{2},z_{2})\mathbf{d}:(x_{4},y_{4},z_{4})\end{array} $$ 

 $$ K\in(K_{1},K_{2}) $$ 

 $$ r\colon(X,Y,Z) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_144_991_1057_1297.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 1 前端数据表达框格形式示意图</div>


5.4.2.3 过程设计数据应包含测量规划数据、测量方法数据、测量设备数据等。

5.4.2.4 过程设计数据应使用标注卡片形式与被测要素关联，信息卡片内容应包含测量名称、方法、设备、规程、属性等，结构形式可参考附录 A 中图 A.1。

## 6 测量过程设计

### 6.1 测量任务

测量任务应取决于测量要求、测量前端数据和目标不确定度。

### 6.2 测量设计

6.2.1 根据测量任务给出测量仪器和环境条件的初始规范。

6.2.2 遵循 GB/T 18779.2—2004 中 PUMA 规范的方法进行不确定度评估，使测量结果的不确定度满足目标不确定度要求。

6.2.3 测量人员应具有可证明的能力，接受相关培训以满足已识别的需要，认识到所承担的职责及其活动对测量有效性和产品质量的影响；并应对测量目标、测量方案详细了解，熟悉测量设备的操作。

6.2.4 应依据目标测量不确定度给出测量仪器选用建议或规范。

6.2.5 选择测量方法时，在保证可以实现目标不确定度的前提下，应考虑成本和效率。

6.2.6 测量操作的设计应符合 GB/T 1958 的规范要求。

6.2.7 测量过程设计应考虑环境对测量不确定度的影响。

6.2.8 测量过程设计应基于测量不确定度的评定，测量不确定度的表述应符合 GB/T 18779.2—2004 的要求。

### 6.3 测量过程设计验证

6.3.1 测量设计方应安排针对测量过程设计的验证，用于证明不确定度评定结果的合理性，验证方法包括：

a）与委托方提供的具有确定值的样品进行比对；

b）与具有溯源性的检测机构的测量结果进行比对。

6.3.2 测量工作的开展，是在送检方和检测方对测量不确定度表述（值）形成共识后才能开展。

### 6.4 测量过程设计的输出

6.4.1 测量过程设计的信息数据应符合 5.3 规定的测量过程描述规范。

6.4.2 测量过程设计的信息数据应与测量模型关联，输出方式应符合 5.4 测量模型规范的表述。

## 7 测量实施

### 7.1 测量管理

7.1.1 测量应保证测量设备、环境条件和工装卡具满足测量模型中的相关规定。

7.1.2 实施测量之前需要确保完成测量的准备工作，如设备的预热和标定、测量模型数据导入等。

7.1.3 测量操作过程需要遵循相应的测量规范，对于测量仪器的使用要按照仪器的使用手册进行。

7.1.4 在测量时，应考虑随时间推移，环境（温度、湿度等）的波动性，采取监视措施保证环境条件始终符合测量设备在允许的工作范围。

7.1.5 给出的测量结果应包含测量不确定度。

### 7.2 测量输出

7.2.1 测量输出的最终结果数据应与测量模型上的被测要素关联。

7.2.2 对于输出到物理设备的数据，格式应符合 GB/T 26498 所规范的内容。

### 7.3 测量流程

基于数字化模型的测量流程参见附录 B。

## 8 其他

与 GPS 矩阵模型的关系参见附录 C。

附录 A

（资料性附录）

测量数据标注示例

测量模型中的过程设计数据标注卡片如图 A.1 所示。


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">检测任务名称：平面度检测</td><td style='text-align: center;'>时间：0000年0月00日</td></tr><tr><td colspan="2">检测方法：三坐标接触式检测（表面结构类）</td><td style='text-align: center;'>检测设备：CMM三坐标检测机</td></tr><tr><td colspan="2">方法示意图：</td><td style='text-align: center;'>设备简图：</td></tr><tr><td style='text-align: center;'>检测规程：</td><td colspan="2">检测工序一：01：确定检测平面起点/边界/终点检测工序一：02：导入检测平面度公差值检测工序一：03：进行检测仿真测试......</td></tr><tr><td style='text-align: center;'>属性信息</td><td colspan="2">操作人员：***环境参数：温度—20℃；湿度—35%；洁净度—100级检测点：135接触探针：碳化钨M5</td></tr><tr><td style='text-align: center;'>备注：</td><td colspan="2">——</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_138_406_983_935.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 A.1 测量模型中的过程设计数据标注卡片</div>


附录 B

(资料性附录)

基于数字化模型的测量流程

基于数字化模型的测量流程见图 B.1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_382_1022_959.jpg" alt="Image" width="70%" /></div>


 $ ^{a} $  MBD: 基于模型的定义 (Model Based Definition)。

<div style="text-align: center;">图 B.1 基于数字化模型的测量流程</div>


# 附录 C   (资料性附录)   与 GPS 矩阵模型的关系

### C. 1 概述

关于 GPS 矩阵模型的完整细则，参见 GB/Z 20308。

GB/Z 20308 中的 GPS 矩阵模型对 GPS 体系进行了综述，本标准是该体系的一部分。除非另有说明，GB/T 4249 给出的 GPS 基本规则适用于本标准，GB/T 18779.1 给出的缺省规则适用于按照本标准制定的规范。

### C.2 关于标准及其使用的信息

本标准规定了机械结构几何要素基于数字化模型测量的数据模型要求、测量模型构建、测量过程设计、测量实施等的通用要求。

### C. 3 在 GPS 矩阵模型中的位置

本标准是一项 GPS 通用标准，本标准中给出的规则和原则适用于 GPS 矩阵中所有标有实心点（●）的部分。如表 C.1 所示。

<div style="text-align: center;">表 C.1 GPS 标准矩阵模型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="3"></td><td colspan="7">链环</td></tr><tr><td style='text-align: center;'>A</td><td style='text-align: center;'>B</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>E</td><td style='text-align: center;'>F</td><td style='text-align: center;'>G</td></tr><tr><td style='text-align: center;'>符号和标注</td><td style='text-align: center;'>要素要求</td><td style='text-align: center;'>要素特征</td><td style='text-align: center;'>符合与不符合</td><td style='text-align: center;'>测量</td><td style='text-align: center;'>测量设备</td><td style='text-align: center;'>校准</td></tr><tr><td style='text-align: center;'>尺寸</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>●</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>距离</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>●</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>形状</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>●</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>方向</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>●</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>位置</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>●</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>跳动</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>轮廓表面结构</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>区域表面结构</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>表面缺陷</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>