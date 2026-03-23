

# 中华人民共和国国家标准

GB/T 44795—2024

# 系统级封装(SiP) 一体化基板通用要求

# General requirements for integral substrate of System in Package(SiP)

2024-10-26 发布

2024-10-26 实施



## 目次

前言：……Ⅲ  
  
1 范围……1  
  
2 规范性引用文件……1  
  
3 术语和定义……1  
  
4 总体要求……1  
  
4.1 通则……1  
  
4.2 文件优先顺序……1  
  
4.3 一体化基板类型……2  
  
5 特性定义要求……2  
  
5.1 总则……2  
  
5.2 电气特性……2  
  
5.3 热特性……2  
  
5.4 结构特性……2  
  
6 设计要求……3  
  
6.1 总则……3  
  
6.2 一体化厚膜基板设计要求……3  
  
6.3 一体化薄膜基板设计要求……4  
  
6.4 一体化厚薄膜混合基板设计要求……5  
  
6.5 一体化有机印制基板设计要求……6  
  
7 验证要求……7  
  
7.1 总则……7  
  
7.2 验证方案……7  
  
7.3 仿真模型……7  
  
7.4 试制验证……7  
  
7.5 建模提参……7  
  
8 制造要求……8  
  
8.1 总则……8  
  
8.2 验证与制造一致性……8  
  
8.3 关键工序与特殊过程……8  
  
8.4 质量控制……8  
  
8.5 工艺模型库……8  
  
8.6 环境要求……8  
  
9 检验要求……8

9.1 总则……8    
9.2 静态指标检验……9    
9.3 环境性能试验……9    
10 交付要求……9    
10.1 标识……9    
10.2 文件……10    
11 产品转运、贮存要求……10    
11.1 转运……10    
11.2 贮存……10    
附录 A（资料性） 基板设计典型参考值……11    
A.1 一体化厚膜基板……11    
A.2 一体化薄膜基板……13    
A.3 一体化厚薄膜混合基板……15    
A.4 一体化有机印制基板……15    
参考文献……17

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由中华人民共和国工业和信息化部提出。

本文件由全国集成电路标准化技术委员会(SAC/TC 599)归口。

本文件起草单位：中国电子科技集团公司第二十九研究所、中国科学院微电子研究所、清华大学、电子科技大学、厦门云天半导体科技有限公司、成都迈科科技股份有限公司。

本文件主要起草人：李彦睿、王春富、徐洋、边方胜、贾松良、于慧慧、季兴桥、陆吟泉、吕拴军、秦跃利、徐榕青、向伟玮、王文博、张健、徐诺心、万里兮、于大全、张继华、李勇、龚小林、高明起、王娜、张刚、张湉、徐飞。



# 系统级封装(SiP)

# 一体化基板通用要求

## 1 范围

本文件规定了系统级封装（SiP）一体化基板通用要求，包括一体化基板总体要求、特性定义、设计、验证、制造、检验、交付、产品转运、贮存等方面要求。

本文件适用于系统级封装(SiP)中成为成品外壳整体一部分的底部基板。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 9178—1988 集成电路术语

GB/T 12842—1991 膜集成电路和混合膜集成电路术语

GB/T 44801—2024 系统级封装(SiP)术语

## 3 术语和定义

GB/T 9178—1988、GB/T 12842—1991 和 GB/T 44801—2024 界定的术语和定义适用于本文件。

## 4 总体要求

### 4.1 通则

系统级封装(SiP)一体化基板(以下简称“一体化基板”)要求包括。

a）技术要求，按产品流程一般可分为：

1）特性定义要求；

2）设计要求；

3）验证要求；

4）制造要求。

b）其他要求，包括但不限于：

1）检验要求；

2）交付要求；

3）产品转运、贮存要求。

除本文件规定的要求外，一体化基板其他要求应符合或超过其他相关规范性文件的特定应用等级的所有要求。

### 4.2 文件优先顺序

采用本文件或其他相关规范性文件时，优先顺序如下：

a）图纸、合同等产品采购文件；

b) 本文件；

c）其他相关规范或法律文件。

### 4.3 一体化基板类型

本文件适合的基板类型如下。

a）一体化无机电路基板，按工艺可分为：

1）一体化厚膜基板，如陶瓷厚膜基板、低温共烧陶瓷基板、高温烧陶瓷基板等；

2）一体化薄膜基板，如玻璃薄膜基板（典型如 TGV 转接板）、陶瓷薄膜基板（典型如 TCV 转接板、DPC 基板）等；

3）一体化混合膜集成电路基板，如淀积/低温共烧陶瓷混合集成电路基板、淀积/高温共烧陶瓷混合集成电路基板等。

b) 一体化有机电路基板，包括各类印制基板，如聚四氟乙烯基多层印制基板、聚苯醚基多层印制基板等。

## 5 特性定义要求

### 5.1 总则

定义或规定一体化基板的基本功能和性能参数等信息,通常可包括:

a) 电气特性；

b) 热特性；

c）结构特性。

### 5.2 电气特性

一体化基板电气特性指集成电路芯片等元器件的信号传输和电源分配有效输入/输出途径，一般包括：

a）功能单元：一体化基板的功能区划，包括但不限于射频、数字、电源、模拟、存储等；

b) 互连：电路包含的元器件及其互连方式；

c）端口：基板直接输入/输出信号时的级联关系和类型；

d）隔离：产品整体或信道间信号传输抑制对围框、孔等一体化封装结构的要求。

### 5.3 热特性

一体化基板热特性指电路工作时产生的热量影响和有效耗散途径,一般包括:

a）基板散热：基板自身材料热导率参数或导热孔、流道等一体化基板内嵌散热结构布局；

b) 导热结构：一体化基板面向的外部环境或下级封装的热耗散要求；

c）热匹配性：一体化基板与元器件间，与下级封装间的热膨胀系数匹配性。

### 5.4 结构特性

结构特性主要指元器件保护结构，在面对外界机械应力和化学环境腐蚀时，确保电路不受损害和退化，一般包括：

a）封焊区域：焊接框、盖板等壳体的焊接区域设置和可焊性；

b）结构强度：一体化基板作为封装承载结构的应力、抗弯强度和平整度等参数要求；

c）保护性：基板隔绝外部环境影响能力，包括气密性、耐腐蚀性等。

## 6 设计要求

### 6.1 总则

宜按照 4.3 中分类执行不同类型一体化基板设计要求，设计要求按要素类别可分为：

a）材料，包含强度、热特性、电学性能等要素，应满足抗弯强度、热导率、介电特性等参数要求；

b）结构，包含孔、腔体、外形、散热等要素，应满足应力、平整度、热匹配、抗弯强度、散热途径等参数要求；

c）布线，包含布线、焊盘、封焊区域等要素，应满足可焊性、堆叠互连尺寸、气密性等要求；

d）端口，包含输入、输出等要素，应满足布线、屏蔽、基板级联等互连要求。

### 6.2 一体化厚膜基板设计要求

一体化厚膜基板设计要求见表1。

<div style="text-align: center;">表 1 一体化厚膜基板设计要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>要素</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>典型参考值</td></tr><tr><td rowspan="3">材料</td><td style='text-align: center;'>强度</td><td style='text-align: center;'>基板材料机械强度应符合封装工艺和产品使用要求，典型包括抗弯强度、密度、硬度等参数</td><td rowspan="3">A.1.1</td></tr><tr><td style='text-align: center;'>热特性</td><td style='text-align: center;'>a）基板材料热导率应满足SiP系统功率耗散要求；b）基板材料热膨胀系数应同时与电路元器件和下级封装匹配</td></tr><tr><td style='text-align: center;'>电学性能</td><td style='text-align: center;'>基板材料电学参数应满足一体化集成性能指标要求，典型包括介电常数、介质损耗、电阻率等</td></tr><tr><td rowspan="3">结构</td><td style='text-align: center;'>孔</td><td style='text-align: center;'>a）孔分布设计应符合产品机械强度及平整度要求，宜根据互连、隔离、散热等指标最低要求设置孔密度和位置；b）孔边缘到产品或腔体边缘距离应满足材料结构强度要求；c）隔离孔和气密封装孔宜避免垂直堆栈布局；d）金属化孔宜采用浆料充分填充，无影响元件可焊性的任何杂质</td><td rowspan="3">A.1.2</td></tr><tr><td style='text-align: center;'>腔体</td><td style='text-align: center;'>a）基板开腔率（每层腔体面积与基板面积的比值）应符合产品结构强度要求；b）方/矩形腔体顶角点宜根据要求设置足额半径的圆角；c）腔体内部、边缘宜避免出现孤岛或半岛结构</td></tr><tr><td style='text-align: center;'>外形</td><td style='text-align: center;'>a）外形尺寸与偏差应符合热膨胀系数及抗弯强度要求；b）外形加工宜选取符合产品形状要求条件下应力最小的加工工艺；c）基板平整度应满足下级封装平整度要求；d）基板厚度不满足抗弯强度要求时，宜设置仅有孔互连功能的补充层增加至足额厚度</td></tr></table>

<div style="text-align: center;">表 1 一体化厚膜基板设计要求 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>要素</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>典型参考值</td></tr><tr><td style='text-align: center;'>结构</td><td style='text-align: center;'>散热</td><td style='text-align: center;'>a）可增加热孔层提升基板局部散热率，导热孔阵列宜采用垂直堆栈方式；b）必要时，可设计流道进行液冷散热，流道应符合产品机械强度及平整度要求</td><td style='text-align: center;'>A.1.2</td></tr><tr><td rowspan="3">布线</td><td style='text-align: center;'>导带</td><td style='text-align: center;'>a）基板电路图形布局时，X、Y、Z轴上导带密度应满足基板翘曲度指标要求；b）在不同层间主要导带图形投影间隔距离宜不小于线宽；c）导带厚度应满足产品电性能和基板翘曲度指标要求；d）接地图形设置应符合产品应力要求，外层接地一般采用实心地结构，内层接地一般采用边缘开口的网格地结构</td><td rowspan="3">A.1.3</td></tr><tr><td style='text-align: center;'>焊盘</td><td style='text-align: center;'>a）同类互连工艺或同样封装类型的焊盘尺寸宜保持一致；b）含孔的焊盘不宜直接采用键合或焊接工艺，一般采用扩展面积的方式延伸装配区域</td></tr><tr><td style='text-align: center;'>封焊区域</td><td style='text-align: center;'>封焊区域应满足围框/壳体材料可焊性要求</td></tr><tr><td style='text-align: center;'>端口</td><td style='text-align: center;'>输入/输出</td><td style='text-align: center;'>封装引出端节距、形式应符合电路互连设计要求，输出端口应满足布线、屏蔽、级联等要求，一般采用球栅阵列、柱栅阵列、表贴引线键合、插接等形式</td><td style='text-align: center;'>A.1.4</td></tr></table>

### 6.3 一体化薄膜基板设计要求

一体化薄膜基板设计要求见表2。

<div style="text-align: center;">表 2 一体化薄膜基板设计要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>要素</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>典型参考值</td></tr><tr><td rowspan="3">材料</td><td style='text-align: center;'>机械强度</td><td style='text-align: center;'>基板材料机械强度应符合封装工艺和产品使用要求，典型包括抗弯强度、密度、硬度等参数</td><td rowspan="3">A.2.1</td></tr><tr><td style='text-align: center;'>热特性</td><td style='text-align: center;'>a）基板材料热导率应满足SiP系统功率耗散要求，宜优先采用高散热率基板，如氮化铝、碳化硅等，并在保证机械强度基础上尽可能减少基板厚度；b）基板材料热膨胀系数应同时与电路元器件和下级封装匹配</td></tr><tr><td style='text-align: center;'>电学性能</td><td style='text-align: center;'>基板材料电学参数应满足一体化集成或内埋元器件性能指标要求，典型包括介电常数、介质损耗、电阻率等</td></tr></table>

<div style="text-align: center;">表 2 一体化薄膜基板设计要求(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>要素</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>典型参考值</td></tr><tr><td rowspan="4">结构</td><td style='text-align: center;'>孔</td><td style='text-align: center;'>a）孔分布设计应符合产品机械强度，宜根据互连、隔离、散热等指标最低要求设置孔密度和位置；b）孔边缘到产品或开腔边缘距离应满足材料结构强度要求；c）宜选取符合产品设计要求条件下应力最小的加工工艺；d）穿孔互连结构宜根据互连密度、传输损耗、散热率等指标最低要求确定是否实心填充；有气密封装要求时，宜采用实心孔，并避免孔壁和孔表焊盘存在开放界面</td><td rowspan="2">A.2.2</td></tr><tr><td style='text-align: center;'>腔体</td><td style='text-align: center;'>a）基板开腔层最小宽度尺寸应符合结构强度要求；b）方/矩形腔体顶角点宜根据要求设置足额半径的圆角；c）多层开腔层堆叠时，开腔形状宜保持一致</td></tr><tr><td style='text-align: center;'>外形</td><td style='text-align: center;'>a）外形尺寸与偏差应符合材料热膨胀系数及抗弯强度要求；b）外形加工宜选取符合产品形状要求条件下应力最小的加工工艺；c）基板翘曲度应满足下级封装平整度要求，必要时宜适当增加基板厚度</td><td rowspan="2">A.2.2</td></tr><tr><td style='text-align: center;'>散热</td><td style='text-align: center;'>a）必要时，可采用实心金属化孔阵列提升基板局部散热率；b）必要时，可设计流道进行液冷散热，流道应符合产品机械强度要求</td></tr><tr><td rowspan="3">布线</td><td style='text-align: center;'>导带</td><td style='text-align: center;'>a）多层布线介质层厚度和层数应满足产品结构空间尺寸和焊接强度要求；b）多层布线电路宜避免在介质层电路上布置焊盘等封装结构；c）单层基板布线介质层数大于2层时，宜转化为等效的2层介质布线多层基板堆叠结构</td><td rowspan="3">A.2.3</td></tr><tr><td style='text-align: center;'>焊盘</td><td style='text-align: center;'>a）同类互连工艺或同样封装类型的焊盘尺寸宜保持一致；b）含孔的焊盘不宜直接采用键合或焊接工艺，一般采用扩展面积的方式延伸装配区域</td></tr><tr><td style='text-align: center;'>封焊区域</td><td style='text-align: center;'>封焊区域应满足围框/壳体材料可焊性要求</td></tr><tr><td style='text-align: center;'>端口</td><td style='text-align: center;'>输入/输出</td><td style='text-align: center;'>端口应满足布线、屏蔽、级联等要求，一般采用球栅阵列、柱栅阵列、表贴引线键合、表贴无引线等形式</td><td style='text-align: center;'>A.2.4</td></tr></table>

### 6.4 一体化厚薄膜混合基板设计要求

除本节内容外，一体化厚薄膜混合基板表层布线要求与6.3性能要求一致，其他要求与6.2性能要求一致。

一体化厚薄膜混合基板设计要求见表3。

<div style="text-align: center;">表 3 一体化厚薄膜混合基板设计要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>要素</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>典型参考值</td></tr><tr><td rowspan="2">结构</td><td style='text-align: center;'>孔</td><td style='text-align: center;'>a) 互连孔宜为厚膜工艺；b) 焊接区域孔表焊盘宜设置放气孔</td><td rowspan="2">A.3.1</td></tr><tr><td style='text-align: center;'>外形</td><td style='text-align: center;'>a) 基板表面任意两点间的距离应满足淀积膜层图形对准要求，通常以功能图形对应距离作为参照；b) 基板表面最大高度差和平整度间的较大值应满足装配最大深度容差要求</td></tr><tr><td rowspan="2">布线</td><td style='text-align: center;'>导带</td><td style='text-align: center;'>a) 表层导带布线图形宜为薄膜工艺；b) 与表层淀积膜层电路存在互连关系的底层导带材料宜选择多层共烧陶瓷金体系</td><td rowspan="2">A.3.2</td></tr><tr><td style='text-align: center;'>焊盘</td><td style='text-align: center;'>表层焊盘宜为薄膜工艺，淀积膜系应满足焊接工艺要求</td></tr></table>

### 6.5 一体化有机印制基板设计要求

一体化有机印制基板设计要求见表4。

<div style="text-align: center;">表 4 一体化有机印制板基板设计要求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>类别</td><td style='text-align: center;'>要素</td><td style='text-align: center;'>要求</td><td style='text-align: center;'>典型参考值</td></tr><tr><td rowspan="3">材料</td><td style='text-align: center;'>强度</td><td style='text-align: center;'>基板材料机械强度应符合封装工艺和产品使用要求，典型包括抗弯强度等参数</td><td rowspan="3">A.4.1</td></tr><tr><td style='text-align: center;'>热特性</td><td style='text-align: center;'>a）基板材料热导率应满足SiP系统功率耗散要求；b）基板材料热膨胀系数应同时与电路元器件和下级封装匹配；c）基板材料温度相关参数应满足一体化装配工艺要求，典型如转化温度等</td></tr><tr><td style='text-align: center;'>电学性能</td><td style='text-align: center;'>基板材料电学参数应满足一体化集成性能指标要求，典型包括介电常数、介质损耗、电阻率等</td></tr><tr><td rowspan="2">结构</td><td style='text-align: center;'>孔</td><td style='text-align: center;'>a）孔分布设计应符合产品机械强度及平整度要求，宜根据互连、隔离、散热等指标最低要求设置孔密度和位置；b）孔边缘到产品或腔体边缘距离应满足材料结构强度要求；c）孔径应满足互连电气性能、可靠性及结构强度要求</td><td rowspan="2">A.4.2</td></tr><tr><td style='text-align: center;'>外形</td><td style='text-align: center;'>a）外形尺寸与偏差应符合材料热膨胀系数及抗弯强度要求；b）基板平整度应满足下级封装平整度要求；c）基板厚度不满足抗弯强度要求时，宜设置仅有孔互连功能的补充层增加至足额厚度</td></tr><tr><td rowspan="2">布线</td><td style='text-align: center;'>导带</td><td style='text-align: center;'>双导带图形占比差异应满足产品翘曲度设计要求</td><td rowspan="2">A.4.3</td></tr><tr><td style='text-align: center;'>封焊区域</td><td style='text-align: center;'>封装焊盘应满足围框/壳体材料可焊性要求</td></tr><tr><td style='text-align: center;'>端口</td><td style='text-align: center;'>输入/输出</td><td style='text-align: center;'>输出端口应满足布线、屏蔽、级联等要求，一般采用球栅阵列、插接等形式</td><td style='text-align: center;'>A.4.4</td></tr></table>

## 7 验证要求

### 7.1 总则

必要时，可在设计完成后对设计方案进行验证，验证要求一般包括：

a）验证方案；

b) 仿真模型；

c) 试制验证；

d）建模提参。

### 7.2 验证方案

宜根据设计文件确定验证方案，一般包括：

a）验证指标，一体化基板设计中影响性能的关键特征指标，典型如孔、腔体、收缩率等；

b）验证内容，包括可制造性、可靠性等；

c）验证方法，一般包括仿真、试制等；

d）验证环境，构建测试平台的内容和功能，列出测试平台清单、验证工具名称和版本/型号。

### 7.3 仿真模型

一般可采用的仿真模型包括：

a）根据原理公式推导的等效数学模型；

b）有限元仿真模型。

建立仿真模型包括但不限于：

a）一体化基板设计的所有物理参数及单位；

b）一体化基板结构、信号、热模型等效公式；

c）一体化基板的外围边界信息及面积信息；

d）一体化基板的内容结构要素，如孔、腔体、导线等，包括类型、数量及坐标位置；

e）一体化基板原点坐标及参考性坐标；

f) 一体化基板输出端口属性，包括端口名称、类型、方向、输入输出信号类型、形状、金属层、级联要求等。

### 7.4 试制验证

完成仿真后，可采用样件试制的方式开展试制验证，试制工艺应与实际制造工艺信息、数据和方法一致。

试制完成后，可按照9.2中检验方法检验并反馈测试结果。

必要时，可生成试制验证报告，包括：

a） 宜对测试设备进行描述；

b）宜对测试条件进行描述；

c）宜对测试完成情况进行描述，没有完成的测试项应说明原因；

d）对测试中所发现的设计问题和生产缺陷宜详细记录。

### 7.5 建模提参

应根据每个验证项的仿真模型或试制结果提取适宜的参数，并对原设计做必要的修改。必要时，

可反复迭代7.2~7.4过程，直至设计、仿真和试制验证结果一致。

## 8 制造要求

### 8.1 总则

制造要求一般包括：

a）验证与制造一致性；

b）关键工序与特殊过程；

c）质量控制；

d）工艺模型库；

e） 环境要求。

### 8.2 验证与制造一致性

制造过程宜尽可能与已验证的试制工艺一致，当制造过程较验证工艺出现不可抗拒的偏差时，应分析差异对实际制造效果的影响，必要时重新进行验证。

基板材料一致性应满足仿真容差要求，对于基片等关键材料，必要时可在每批产品或每批工艺中抽取质量监控件进行分析、测试或检验。

### 8.3 关键工序与特殊过程

对一体化基板机械强度有较大影响或导致后续工艺中应力分布恶化的工序可确定为关键工序，典型如激光加工、烧结等。

对制造过程中不能通过其后的检验或试验而直接表征基板应力变化情况的工序可确定为特殊过程，典型如高温焊接、焊盘电镀等。

### 8.4 质量控制

定期总结一体化基板制造过程中故障模式，完成影响分析。

工艺设备稳定性应满足制造过程一致性要求，必要时可严格实行岗位责任制，实行定人定机、凭证操作。

应根据一体化基板产量要求和质量控制情况逐步提升产能，必要时，可在前期执行多次小批量制造以验证制造过程符合性。

### 8.5 工艺模型库

必要时，可针对制造过程情况或重大工艺问题，修正一体化基板工艺参数边界，反馈工艺模型库，完善一体化基板设计准则和可制造性准则。

### 8.6 环境要求

制造过程环境参数应满足一体化基板自身要求，对于温度、湿度等关键指标，宜持续监控并保持一致。

## 9 检验要求

### 9.1 总则

宜在一体化基板不同产品阶段分别执行相关检验，一般可分为：

a）完成一体化基板制造程序后，应进行静态指标检验，除外观、尺寸、结构、电通断等指标外，可执行包括但不限于9.2中内容，检验要求和抽样条件参考产品技术文件或不同类型基板有关规范；

b）完成静态指标测试后，可以进行基板热应力和机械应力的环境性能检验，包括但不限于9.3中要求；

c） 完成系统级封装（SiP）电路装配后，应根据产品试验大纲开展环境试验，典型如 GB/T 4937（所有部分）。

### 9.2 静态指标检验

#### 9.2.1 翘曲度

宜按照 GB/T 6620—2009 中翘曲度测量方法要求进行全版面翘曲度检验，一般采用影像测量仪、激光测量仪等非接触式测试方法。

#### 9.2.2 抗弯强度

宜按照 GB/T 4741—1999 中抗弯强度测量方法要求进行抗弯强度检验，每种一体化基板产品的抗弯强度测试频度宜不少于 1 次，一般采用三点负荷法。

#### 9.2.3 残余应力

基板自身材料特性允许时，宜按照 GB/T 32073—2015 中超声临界纵波检测测量方法要求，进行非破坏性残余应力检验。

#### 9.2.4 气密性

必要时，可按照 GB/T 4937（所有部分）中密封试验要求在封装前进行气密性测试，一般采用质谱仪示踪气体法。

### 9.3 环境性能试验

#### 9.3.1 热应力试验

宜按照 GB/T 4937（所有部分）中快速温度变化（空气—空气）试验要求检验一体化基板热应力。产品应满足技术文件电试验要求，并进行外观检查以便发现裂缝、破裂。

#### 9.3.2 机械应力试验

宜按照 GB/T 4937（所有部分）中变频振动试验要求检验一体化基板机械应力。产品应满足技术文件电试验要求，并进行外观检查以便发现裂缝、破裂。

## 10 交付要求

### 10.1 标识

产品交付应具备明确标识，一般包括：

a）承制方名称或商标；

b） 批识别代码或日期代码；

c） 产品认证标识(如果通过认证)。

标识可以采用永久性油墨印刷、金属图形、激光打标等方式制作。

除非采购、设计文件另有规定，一体化基板应在基板、包装或其他合适位置清晰地进行标识。

因基板尺寸和空间限制，无法在基板或包装上完整提供上述标识时，可以通过和产品接收方协商采用其他形式。

### 10.2 文件

必要时，可随产品同步交付设计、仿真和使用说明等文件，其中：

a）文档文件宜使用适用于常规文本阅读器的文本文件格式；

b） 数据文件宜使用符合主流设计程序的文件格式。

## 11 产品转运、贮存要求

### 11.1 转运

一体化基板转运过程中应整齐码放在基板盒内。基板盒应为一体化基板提供机械支撑和保护，防止外力挤压和划伤，并避免一体化基板从片盒内滑落。必要时，转运过程中应采用真空包装。

### 11.2 贮存

一体化基板宜避免直接暴露在空气中，一般采用充氮柜进行贮存，并保持湿度不大于10%，温度在22℃~26℃区间。

# 附录 A

(资料性)

## 基板设计典型参考值

### A.1 一体化厚膜基板

#### A.1.1 材料

基板及导带材料选取要求与常规厚膜混合集成电路、多层共烧陶瓷电路一致。厚膜混合集成电路基板一般选用96%氧化铝体系，共烧陶瓷电路基板一般选取低温共烧陶瓷体系或高温共烧陶瓷体系。

基板材料选取宜与结构件材料性能匹配，典型的对比参数见表A.1。

<div style="text-align: center;">表 A.1 无机厚膜电路基板性能参数对比</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>材料</td><td style='text-align: center;'>密度/(g/cm³)</td><td style='text-align: center;'>热导率/[W/(m·K)]</td><td style='text-align: center;'>热膨胀系数10⁻⁶/K</td></tr><tr><td style='text-align: center;'>Al₂O₃(96%)</td><td style='text-align: center;'>3.75～4.0</td><td style='text-align: center;'>22～40</td><td style='text-align: center;'>6.5～7.2</td></tr><tr><td style='text-align: center;'>LTCC</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>2～5</td><td style='text-align: center;'>5～7</td></tr><tr><td style='text-align: center;'>HTCC (&gt;92%Al₂O₃)</td><td style='text-align: center;'>3.6</td><td style='text-align: center;'>17</td><td style='text-align: center;'>6.8</td></tr><tr><td style='text-align: center;'>AlN</td><td style='text-align: center;'>3.2</td><td style='text-align: center;'>100～260</td><td style='text-align: center;'>2.7～4.6</td></tr></table>

焊盘表面镀层材料宜考虑各种工艺要求，如金丝、铝丝、金带及铝带键合和金锡、锡铅焊接等，典型焊盘表面镀层材料包括镍钯金合金等。必要时，也可根据产品技术要求针对不同用途焊盘分配不同材料，典型如镍、钯银合金、铂钯金合金等。

#### A.1.2 结构

##### A.1.2.1 孔

厚膜混合集成电路孔宜采用激光工艺打孔。共烧陶瓷基板孔一般宜采用冲孔工艺，当孔尺寸小于 $ 50\mu m $ 时，宜采用激光打孔。

孔设计宜符合产品封装机械强度及平整度要求，宜根据产品互连、隔离、散热等电路指标最低要求设置孔数量。

孔一般在平面内最大化均匀布置，沿垂直方向最大化对称布置。孔边缘到产品或腔体边缘距离宜不小于0.4 mm。

共烧陶瓷基板交错孔示意图见图 A.1, 各类型孔设置如下:

a）互连孔宜根据产品封装焊接要求设置扩展焊盘，焊盘直径不小于0.2 mm，孔中心距宜大于3倍孔径；

b) 隔离孔宜采用交错布孔方式，孔中心距宜大于2倍孔径，层间交错距离宜不小于 $ 50\mu m $ ，可采用图A.1a)或图A.1b)两种排列方式；

c) 导热孔阵列宜采用图 A.1c) 方式，孔中心距宜大于 1.5 倍孔径，最大布孔面积宜不大于  $ 10 \, mm \times 10 \, mm $ ;

d）进行气密封装时，宜至少交错一层孔，交错距离不小于2倍孔径；

e）含孔的焊盘区域不宜采用打线、键合或焊接工艺，一般采用扩展焊盘面积的方式延伸键合区

域，扩展面积单边长度通常不小于1倍孔径。

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_245_411_439.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">a）互连孔布局</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_448_245_707_441.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">b）隔离孔布局</div>


<div style="text-align: center;">图 A.1 交错孔示意图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_766_246_967_438.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">c）导热孔布局</div>


##### A.1.2.2 腔体

基板开腔率(每层腔体面积与基板面积的比值)宜符合产品结构强度要求,一般开腔率不宜大于60%。

产品腔体尺寸宜保持统一，腔体内部、边缘宜避免出现孤岛或半岛结构，方/矩形腔体顶角点宜倒圆角且圆角半径不小于0.1 mm。

共烧陶瓷基板盲腔深度宜不大于单层基板厚度，最大深度宽度比为1:3，底部厚度不低于0.6 mm。

##### A.1.2.3 外形

共烧陶瓷基板设计厚度小于  $ 0.6 \, mm $  时，宜设置仅有孔互连功能的补充层补足厚度至  $ 0.6 \, mm $  以上。

基板平面尺寸宜符合材料热膨胀系数及抗弯强度要求，典型单边长度为20 mm～50 mm。基板单边尺寸不小于20 mm时，厚度宜不小于1 mm；基板单边尺寸不小于40 mm时，厚度宜不小于1.2 mm。

厚膜电路基板外形见图A.2，基板外形加工宜满足下列规定：

a）图 A.2a) 宜采用砂轮切割分片；

b) 图 A.2b) 宜采用砂轮切割正交边和激光切割异形边的混合切割工艺，基板外形内角顶角点宜成圆角且圆角半径不小于 0.1 mm；

c）图 A.2c) 宜采用激光切割分片，激光单位功率宜选取工艺范围内最低值，宜采用固体激光器光源皮秒激光。

<div style="text-align: center;"><img src="imgs/img_in_image_box_224_1136_412_1273.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">a）矩形基板</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_487_1134_680_1275.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">b) 含异性部位矩形基板</div>


<div style="text-align: center;">图 A.2 厚膜电路基板外形示意图</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_786_1135_961_1280.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">c) 非矩形基板</div>


#### A.1.3 布线

##### A.1.3.1 导带

共烧陶瓷基板电路图形布局时，X、Y、Z轴上导带密度宜满足基板翘曲度指标要求，其中：

a）在同一层中主要导带图形的布线方向宜一致且与产品边缘平行或垂直；

b）相邻层的主要布线方向宜互相垂直，相邻层布线方向一致的导带不宜在垂直方向上重叠，其投影间隔距离宜不小于线宽。

基板的图形特征尺寸规定包括：

a）线宽/线缝尺寸宜符合设计和工艺能力要求，一般线宽/线缝宜不小于 $ 100\mu m $ ，尺寸误差宜不大于 $ 10\mu m $ ；

b）导带到板边距宜不小于0.4 mm。

共烧陶瓷基板内层导带规定包括：

a）导带厚度宜基板翘曲度指标要求，一般为 $ 6\mu m\sim8\mu m $ ;

b）采用不损耗金层的组装工艺时，表面导带厚度一般为 $ 8\ \mu m\sim15\ \mu m $ ，典型如导电胶粘接、金丝/带键合、锡铅焊等；

c）采用损耗金层的组装工艺时，表面导带厚度宜满足焊接工艺要求，典型如金-锡、金-锗共晶焊等。

接地图形设计规定包括：

a）接地图形设置宜符合产品应力要求，厚膜基板或共烧陶瓷基板外层接地一般采用实心地结构，内层接地一般采用边缘开口的网格地结构；

b）必要时，共烧陶瓷基板内层接地亦可采用实心接地结构，其面积宜不大于基板有效面积的50%，且在有效区域内对称布置；

c) 网格地宜采用开放式结构，网格间距宜不低于  $ 500 \mu m $ ，基板边缘到网格地距离宜不低于  $ 250 \mu m $ ，孔接触焊盘到网格地距离宜不低于  $ 300 \mu m $ ；

d）网格地分布区域宜不小于基片面积的75%，金属总填充率宜为40%~60%；

e）采用多层网格地时，相邻两层宜使用不同的网格图形（网格线宽/间距不同）或交错布置，交错距离宜与网格线宽相当。

##### A.1.3.2 焊盘

焊盘图形设计规则如下：

a）同类互连工艺或同样封装类型的焊盘尺寸宜保持一致；

b）基板间互连焊盘直径宜为  $ 180 \mu m \sim 300 \mu m $ ;

c）芯片与基板间互连焊盘直径宜为  $ 150 \mu m \sim 200 \mu m $ ;

d）焊盘与导带距离宜大于孔径，孔接触焊盘扩展半径宜不小于 $ 50\ \mu m $ ，焊盘宽度宜不小于 $ 100\ \mu m $ ，与相邻焊盘距离宜不小于 $ 200\ \mu m $ ，与芯片安装区域距离宜不小于 $ 200\ \mu m $ ；

e）采用堆叠封装设计时，对于与其他叠层焊盘、金丝焊盘和其他有导带互连的叠层焊盘，宜在叠层焊盘与导带接口处布置阻焊层，一般采用液态光致阻焊剂。

#### A.1.4 端口

宜根据基板类型、基板尺寸等指标选择适宜的端口类型，典型端口形式包括：

a）厚膜电路基板可采用插接、表贴引线键合等封装形式；

b）共烧陶瓷基板可采用球栅阵列、柱栅阵列、表贴引线键合等封装形式。

### A.2 一体化薄膜基板

#### A.2.1 材料

基板材料选用宜满足抗弯强度、热膨胀系数等要求，通常选用无机基板，常用材料包括陶瓷或玻璃，典型陶瓷基板如99%氧化铝、氮化铝、压电陶瓷、铁氧体等，典型玻璃基板如石英、硼硅玻璃等，见表A.2。

<div style="text-align: center;">表 A.2 常用无机薄膜电路基板性能参数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>材料</td><td style='text-align: center;'>介电常数@1Hz</td><td style='text-align: center;'>介电损耗</td><td style='text-align: center;'>电阻率Ω·cm</td><td style='text-align: center;'>热膨胀系数10-6/℃</td><td style='text-align: center;'>热导率W/m·K</td><td style='text-align: center;'>抗弯强度MPa</td><td style='text-align: center;'>密度g/cm3</td></tr><tr><td style='text-align: center;'>Al3O2</td><td style='text-align: center;'>4.5～10</td><td style='text-align: center;'>0.000 4～0.001</td><td style='text-align: center;'>&gt;1014</td><td style='text-align: center;'>6.5～7.2</td><td style='text-align: center;'>22～40</td><td style='text-align: center;'>300～385</td><td style='text-align: center;'>3.75～4.0</td></tr><tr><td style='text-align: center;'>AlN</td><td style='text-align: center;'>8.5～10</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>&gt;1014</td><td style='text-align: center;'>2.7～4.6</td><td style='text-align: center;'>100～260</td><td style='text-align: center;'>280～320</td><td style='text-align: center;'>3.2</td></tr><tr><td style='text-align: center;'>BeO</td><td style='text-align: center;'>6.5～8.9</td><td style='text-align: center;'>&lt;0.001</td><td style='text-align: center;'>&gt;1015</td><td style='text-align: center;'>6.3～9.0</td><td style='text-align: center;'>260～300</td><td style='text-align: center;'>170～240</td><td style='text-align: center;'>2.95</td></tr><tr><td style='text-align: center;'>BN</td><td style='text-align: center;'>4.1～5.4</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>&gt;1014</td><td style='text-align: center;'>2.6～8.6</td><td style='text-align: center;'>55～600</td><td style='text-align: center;'>110</td><td style='text-align: center;'>2.2～3.1</td></tr><tr><td style='text-align: center;'>SiC</td><td style='text-align: center;'>20～45</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>&gt;1014</td><td style='text-align: center;'>2.8～4.6</td><td style='text-align: center;'>70～270</td><td style='text-align: center;'>450</td><td style='text-align: center;'>3.0～3.2</td></tr><tr><td style='text-align: center;'>玻璃等</td><td style='text-align: center;'>4.5～8.5</td><td style='text-align: center;'>&gt;0.002</td><td style='text-align: center;'>&gt;1013</td><td style='text-align: center;'>2.5～6.5</td><td style='text-align: center;'>0.8～2.3</td><td style='text-align: center;'>150～240</td><td style='text-align: center;'>2.9</td></tr></table>

#### A.2.2 结构

##### A.2.2.1 孔

陶瓷基板宜采用激光熔融切割制孔，玻璃基板可采用激光熔融切割、刻蚀、光刻、激光诱导等技术制孔。

设计穿孔互连结构时，宜根据互连密度、传输损耗、散热率等指标选取孔工艺，互连焊盘面积小于3倍孔径（含孔）时，宜采用实心孔互连工艺。

孔壁金属膜系宜与基板表面保持一致，实心孔填充宜采用电镀铜工艺。

孔尺寸宜满足互连电气性能、可靠性及结构强度的规定，包括如下内容。

a）陶瓷基板孔径宜不小于  $ 50 \mu m $ ，玻璃基板孔径宜不小于  $ 10 \mu m $ ，并在满足电性能要求基础上选取可选的最小值。

b）采用通孔时，孔径误差宜低于20%；采用实心孔时，孔径误差宜低于10%。

c）通孔深径比宜符合互连工艺导通性要求，一般不宜大于2。

孔距宜不小于相邻孔孔径的较大值。当该值大于0.5 mm时，孔距宜不小于0.5 mm。

进行气密封装时，宜采用电镀铜填充实心孔，并保留实心孔表面铜层。

孔密度宜符合封装结构强度和工艺技术要求，一般陶瓷基板孔密度不大于每平方厘米50个，玻璃基板孔密度不大于每平方厘米10 000个。

##### A.2.2.2 外形

基板平面尺寸宜符合材料热膨胀系数及抗弯强度的规定，典型基板尺寸的规定包括：

a） 单片电路典型单边长度不大于 40 mm；

b）多层堆叠电路典型单边长度不大于15 mm；

c）基片厚度宜符合产品设计的电性能和结构强度要求，典型厚度为0.2 mm~0.5 mm。

基片分片工艺同 A.1.2.3 中基板外形加工要求。

#### A.2.3 布线

##### A.2.3.1 导带

一体化薄膜基板导带图形线宽/线缝尺寸宜符合设计和工艺能力要求，一般陶瓷电路线宽/线缝宜不小于 $ 10\ \mu m $ ，尺寸误差宜不大于 $ 3\ \mu m $ ，玻璃电路线宽/线缝宜不小于 $ 5\ \mu m $ ，尺寸误差宜不大于 $ 1\ \mu m $ 。

采用单片电路多层布线时，宜根据产品要求设计介质层数和介质厚度。一般采用 PI 或 BCB 工

艺，介质宜为1层～2层，单层厚度 $ 5\mu m\sim10\mu m $ 。介质层上导带图形线宽/线缝宜不小于 $ 20\mu m $ 。

背面图形距板边宜不小于0.1 mm。采用激光切割工艺时，缝边距宜不小于0.2 mm。

##### A.2.3.2 焊盘

一体化薄膜基板焊盘图形宜大于孔径，孔接触焊盘扩展半径宜不小于 $ 20\ \mu m $ ，焊盘宽度宜不小于 $ 50\ \mu m $ 。采用扇出设计时，扇出焊盘与孔图形距离宜不小于0.2 mm。

#### A.2.4 端口

包含互连孔时，可采用球栅阵列、柱栅阵列、表贴无引线、表贴引线键合等封装形式；无互连孔时，宜采用表贴引线键合封装形式。

### A.3 一体化厚薄膜混合基板

#### A.3.1 结构

##### A.3.1.1 孔

孔表层覆盖膜层宜为淀积薄膜，宜适用于键合、打线、焊接等工艺。孔表面焊盘宜采用放气孔工艺，一般在孔边缘设置放气孔，如图A.3。

<div style="text-align: center;"><img src="imgs/img_in_image_box_315_734_892_785.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">图 A.3 放气孔设置示意图</div>


##### A.3.1.2 外形

内层基板表面任意两点间的距离较设计理论值的误差宜不大于0.2%，通常以导带图形对宜距离作为参照。

基板表面最大高度差和翘曲度间的较大值宜小于  $ 50 \mu m $ 。

采用基板堆叠工艺时，基板平面尺寸宜符合厚膜电路基板结构强度匹配性要求，典型单边长度宜为  $ 10 \, mm \sim 30 \, mm $ 。

#### A.3.2 布线

导带材料类型宜在垂直方向上保持对称分布，如图 A.4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_322_1167_562_1286.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">a） 推荐金银导带交叉分布形式</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_639_1167_880_1287.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">b) 宜避免的金银导带交叉分布形式</div>


<div style="text-align: center;">图 A.4 材料类型 Z 向分布示意图</div>


### A.4 一体化有机印制基板

#### A.4.1 材料

基板材料选用高频芯板和粘接片，常用材料包括聚四氟乙烯体系和聚苯醚体系等，典型参数见表A.3。

<div style="text-align: center;">表 A.3 常用有机印制基板性能参数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>材料名称</td><td style='text-align: center;'>转化温度℃</td><td style='text-align: center;'>平面膨胀系数10-6/℃</td><td style='text-align: center;'>热导率W/m·K</td><td style='text-align: center;'>介电常数@1MHz</td><td style='text-align: center;'>电阻率Ω·cm</td><td style='text-align: center;'>表面电阻Ω</td><td style='text-align: center;'>吸水率%</td></tr><tr><td style='text-align: center;'>环氧玻璃纤维材料</td><td style='text-align: center;'>125</td><td style='text-align: center;'>13～18</td><td style='text-align: center;'>0.16</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>1012</td><td style='text-align: center;'>1013</td><td style='text-align: center;'>0.1</td></tr><tr><td style='text-align: center;'>聚酰亚胺玻璃纤维材料</td><td style='text-align: center;'>250</td><td style='text-align: center;'>12～16</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>1014</td><td style='text-align: center;'>1013</td><td style='text-align: center;'>0.35</td></tr><tr><td style='text-align: center;'>环氧芳香族聚酰胺纤维</td><td style='text-align: center;'>125</td><td style='text-align: center;'>6～8</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>1016</td><td style='text-align: center;'>1016</td><td style='text-align: center;'>0.85</td></tr><tr><td style='text-align: center;'>聚酰亚胺芳香族聚酰胺纤维材料</td><td style='text-align: center;'>250</td><td style='text-align: center;'>3～7</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>3.6</td><td style='text-align: center;'>1012</td><td style='text-align: center;'>1012</td><td style='text-align: center;'>1.5</td></tr><tr><td style='text-align: center;'>聚酰亚胺石英材料</td><td style='text-align: center;'>250</td><td style='text-align: center;'>6～8</td><td style='text-align: center;'>0.3</td><td style='text-align: center;'>4</td><td style='text-align: center;'>109</td><td style='text-align: center;'>108</td><td style='text-align: center;'>0.5</td></tr><tr><td style='text-align: center;'>聚四氟乙烯玻璃纤维材料</td><td style='text-align: center;'>75</td><td style='text-align: center;'>20</td><td style='text-align: center;'>0.26</td><td style='text-align: center;'>2.3</td><td style='text-align: center;'>1010</td><td style='text-align: center;'>1011</td><td style='text-align: center;'>1.1</td></tr></table>

#### A.4.2 结构

##### A.4.2.1 孔

孔布局宜最大化随机分布，任意两个孔边缘距离宜大于0.2 mm。

穿过电路片任意直线上的孔，不宜损伤（去除）介质超过50%。

##### A.4.2.2 外形

基板厚度宜符合产品设计的电性能和结构强度要求，基板厚度宜不小于0.6 mm，基板厚度尺寸公差宜控制在10%范围以内。

基板外形被包容尺寸宜为负公差，包容尺寸宜为正公差。

#### A.4.3 布线

##### A.4.3.1 导带

导带的设计宜满足以下规定：

a）导带图形离金属化过孔边缘最小宜为  $ 127 \mu m $ ;

b）需要作为器件引线安装的非金属化孔，孔环宽度宜不小于 $ 380\mu m $ ;

c） 导带设计宜符合基板翘曲度要求，亦即产品结构宜力设计要求。铜厚、图形分布类型（线路层、地层）宜尽量满足对称性要求，即相对于基板的垂直中心对称。

##### A.4.3.2 焊盘

焊盘表面镀层材料宜兼容金丝、金带键合和金锡、锡铅等焊接工艺要求，典型焊盘表面镀层材料包括镍钯金等。必要时，也可根据产品技术要求针对不同用途焊盘分配不同镀层材料。

#### A.4.4 端口

与下级封装间宜采用球栅阵列、插接等封装形式。

## 参考文献

[1] GB/T 4741—1999 陶瓷材料抗弯强度试验方法

[2] GB/T 4937(所有部分) 半导体器件 机械和气候试验方法

[3] GB/T 6620—2009 硅片翘曲度非接触式测试方法

[4] GB/T 32073—2015 无损检测 残余应力超声临界折射纵波检测方法