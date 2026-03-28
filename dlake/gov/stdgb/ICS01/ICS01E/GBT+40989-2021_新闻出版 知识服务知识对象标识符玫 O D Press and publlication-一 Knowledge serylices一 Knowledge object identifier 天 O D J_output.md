

# 中华人民共和国国家标准

GB/T 40989—2021

# 新闻出版 知识服务 知识对象标识符(KOI)

# Press and publication—Knowledge services—Knowledge object identifier (KOI)

2021-11-26 发布

2022-06-01 实施

国家市场监督管理总局发布

国家标准化管理委员会

## 目次

前言 …… III    
引言 …… IV    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和定义 …… 1    
4 KOI 的标识范围 …… 2    
5 KOI 的标识对象 …… 2    
5.1 知识元 …… 2    
5.2 知识集 …… 2    
5.3 知识链 …… 2    
6 KOI 的结构和显示 …… 2    
6.1 KOI 的结构 …… 2    
6.2 KOI 的显示 …… 2    
7 元数据 …… 3    
7.1 知识元 KOI 的元数据 …… 3    
7.2 知识集 KOI 的元数据 …… 5    
7.3 知识链 KOI 的元数据 …… 7    
8 KOI 的分配原则 …… 9    
9 KOI 的注册解析 …… 10    
9.1 KOI 的注册 …… 10    
9.2 KOI 的解析 …… 11    
附录 A（规范性） KOI 的管理 …… 12    
参考文献 …… 13

## 前言

本文件按照 GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国新闻出版标准化技术委员会(SAC/TC 527)归口。

本文件起草单位：中新金桥数字科技（北京）有限公司、中国新闻出版研究院、中国大百科全书出版社、电子工业出版社有限公司、中国建筑出版传媒有限公司。

本文件主要起草人：赵海涛、蒋隽、张巍巍、薛建川、赵军科、刘颖丽、香江波、刘杭、张新智、郭继艳、梁燕、郭丽琴、王德胜、魏枫、汪智、李雅婧。

## 引言

知识作为人类社会发展的重要生产力要素，其作用日益突出，特别是在新闻出版领域数字化转型升级的大背景下，知识服务应运而生。

在新闻出版领域知识服务构建过程中，知识之间常常存在交叉或重复，例如，某个领域的核心知识往往成为另外一个领域的基础支撑，但是由于标识体系不同，所以难以实现知识的跨系统或跨领域应用，造成知识发现和识别存在障碍，也导致了知识构建工作的重复浪费。

知识对象是相对抽象和稳定的，并不依赖于每种特定的内容资源而存在，截至目前从全球范围来看都没有一套技术机制能够对知识对象进行有效的管理。随着互联网的发展，太多的伪知识和错误知识误导并影响着越来越多的人，甚至严重干扰社会的发展和人类进步，而权威可信的知识存在一定程度的唯一性，因此，统一的知识对象管理为正确知识的应用和传播提供了重要的技术支撑，具有非常高的必要性和紧迫性。

知识对象标识符(KOI)是新闻出版领域专门用于标识知识对象的永久标识符，KOI可以避免知识重复，甄别知识真伪，便于系统之间的交互操作和知识跨领域引用、推荐或发掘。在此基础上，可以实现跨系统、跨学科、跨行业的知识整合，形成开放的新闻出版领域知识库，为构建高品质的知识服务产品提供支撑。

# 新闻出版 知识服务 知识对象标识符(KOI)

## 1 范围

本文件规定了知识对象标识符的标识范围、编码结构、显示方法、元数据、分配原则和注册解析等。

本文件适用于信息与文献领域各种知识对象的标识，知识对象包括最小粒度知识及其不同粒度的组合。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 4880.2—2000 语种名称代码 第2部分：3字母代码

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

## 知识 knowledge

通过学习、实践或探索所获得的认知、判断或技能。

注 $ ^{1} $ ：知识可以是显性的，也可以是隐性的；可以是组织的，也可以是个人的。

注 $ ^{2} $ ：知识可包括事实知识、原理知识、技能知识和人际知识。

注3：知识是经过“编辑”的信息，在具有意义的背景环境与分析处理后，能为组织带来真正的价值，它是隐含在专利技术、成功产品与有效策略之后的知识力量。而组织知识的集合（累积的经验、员工、管理技能、作业方式、科技应用、策略伙伴与供货商的关系、顾客及市场情报）就是它智慧资本（intellectual capital）。

[来源:GB/T 23703.2—2010, 2.1]

### 3.2 

知识对象 knowledge object

具有完备知识表达的内容。

### 3.3 

知识对象标识符 knowledge object identifier; KOI

一组用以表示知识对象的编码。

### 3.4 

知识元 knowledge element

在应用需求下，表达一个完整事物或概念的不必再分的独立的知识单位。

[来源:GB/T 38377—2019,2.3]

### 3.5 

知识集 knowledge set

由两个及以上无显著相关性但描述同一知识类型的知识对象所构成的整体。

3.6

知识链 knowledge link

由多个顺序知识元所构成的知识结合体。

## 4 KOI 的标识范围

KOI 是专门用于标识知识对象的永久的标识符，可用于标识一切知识对象，如，从知识领域划分，包括专业知识和大众知识；从知识的功能划分，包括事实知识、原理知识、技能知识和人物知识等。

## 5 KOI 的标识对象

### 5.1 知识元

KOI可用于标识知识元，包括概念、理论、方法、流程、工艺、技术等，如三极管、混凝土、量词等。

### 5.2 知识集

KOI 可用于标识知识集，如建筑材料、中国四大发明等。

表示知识集时，应说明其包含的成员。

### 5.3 知识链

KOI 可用于标识知识链，如混凝土浇筑工艺流程、社会发展阶段等。

表示知识链时，应说明其包含的成员和成员顺序信息。

## 6 KOI 的结构和显示

### 6.1 KOI 的结构

KOI 编码由不定长度的十进制数字组成，如图 1 所示，KOI 编码分为知识对象类型和顺序编号两部分。

## a）知识对象类型

知识对象类型部分由3位数字组成，从000开始编码，由KOI管理机构负责定义，其中已分配编码000表示知识元，001为知识集，002表示知识链。

## b）顺序编号

顺序编号部分采用不定长度的编码方式，从数字0开始编码，按照申请顺序分配并自动增位。

<div style="text-align: center;"><img src="imgs/img_in_image_box_355_1243_808_1364.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">图 1 KOI 编码结构</div>


### 6.2 KOI 的显示

当以屏幕或打印的方式显示知识对象标识符时，应在编码两个组成部分之间加连接符“-”，并在编码

前加 “KOI”，“KOI” 和编码之间加半个空格符号，连接符“-”及“KOI”不构成编码的组成部分，示例如下：

KOI 000-9501

## 7 元数据

### 7.1 知识元 KOI 的元数据

表 1 中所述的描述性元数据元素、表 2 中的管理性元数据元素应按照知识元各自的 KOI 编码进行注册。

<div style="text-align: center;">表 1 知识元 KOI 的描述性元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>KOI编码</td><td style='text-align: center;'>〈KOI〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>知识对象标识符编码，由KOI管理机构统一分配</td><td style='text-align: center;'>0009876</td></tr><tr><td style='text-align: center;'>知识元名称</td><td style='text-align: center;'>〈KnowledgeName〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>代表知识元的规范化的自然语言词语</td><td style='text-align: center;'>爬山虎</td></tr><tr><td style='text-align: center;'>并列名称</td><td style='text-align: center;'>〈AlternativeName〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>可表达知识元的并列的规范化自然语言词语</td><td style='text-align: center;'>Parthenocissus tricuspidata</td></tr><tr><td style='text-align: center;'>并列名称语言</td><td style='text-align: center;'>〈AlternativeLanguage〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>并列名称语种和并列名称成对出现，取值按照GB/T 4880.2—2000三位小写字母目录代码</td><td style='text-align: center;'>lat</td></tr><tr><td style='text-align: center;'>别名</td><td style='text-align: center;'>〈Alias〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识元名称及并列名称以外的名称</td><td style='text-align: center;'>爬墙虎</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>〈Description〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>对知识元的解释和说明</td><td style='text-align: center;'>爬山虎属多年生大型落叶木质藤本植物，其形态与野葡萄藤相似。夏季开花，花小，黄绿色，浆果紫黑色。常攀缘在墙壁或岩石上，广见于我国各地</td></tr><tr><td style='text-align: center;'>描述语种</td><td style='text-align: center;'>〈DescriptionLanguage〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>描述语种和描述成对出现，取值按照GB/T 4880.2—2000表1中的汉语名称</td><td style='text-align: center;'>汉语</td></tr><tr><td style='text-align: center;'>领域分类</td><td style='text-align: center;'>〈DomainClass〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>取值从由KOI管理机构维护的领域类型列表中选出</td><td style='text-align: center;'>建筑材料-〉绿化植物</td></tr><tr><td style='text-align: center;'>参考资料</td><td style='text-align: center;'>〈Resources〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识元的来源/出处文献资料，多个参考资料使用英文分号“；”隔开</td><td style='text-align: center;'>《植物大辞典》</td></tr></table>

<div style="text-align: center;">表 1 知识元 KOI 的描述性元数据（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>版本语言</td><td style='text-align: center;'>（VersionLanguage）</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>编辑当前版本所使用的主要语言，取值按照GB/T 4880.2—2000三位小写字母目录代码</td><td style='text-align: center;'>chi</td></tr><tr><td style='text-align: center;'>版本编号</td><td style='text-align: center;'>（VersionNum）</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>按照申请顺序生成的流水编号，作为版本的唯一标识</td><td style='text-align: center;'>1</td></tr></table>

<div style="text-align: center;">表 2 知识元 KOI 的管理性元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>注册版本</td><td style='text-align: center;'>〈RegistrationNum〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>注册版本编号，由系统生成</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>注册者</td><td style='text-align: center;'>〈Registrant〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>注册者身份标识，知识对象编辑者在KOI管理结构维护系统中注册后可以获得相应的标识。当KOI有多个语言版本时，允许多个注册者</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>注册时间</td><td style='text-align: center;'>〈RegistrationTime〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>提交KOI编码注册申请的时间，由系统自动获取和记录</td><td style='text-align: center;'>2017-10-23 09:55:03</td></tr><tr><td style='text-align: center;'>修订时间</td><td style='text-align: center;'>〈RevisionTime〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>提交知识元元数据修改的时间，由系统自动获取和记录</td><td style='text-align: center;'>2017-11-23 10:55:03</td></tr><tr><td style='text-align: center;'>修订者</td><td style='text-align: center;'>〈Reviser〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>修订者身份标识，知识对象编辑者在KOI管理结构维护系统中注册后可以获得相应的标识</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>修订描述</td><td style='text-align: center;'>〈RevisionDescription〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>对修订原因或修订细节的描述</td><td style='text-align: center;'>知识元描述不准确，修改和完善其描述</td></tr><tr><td style='text-align: center;'>审核时间</td><td style='text-align: center;'>〈ReviewTime〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>提交审核结果的时间，由系统自动获取并记录</td><td style='text-align: center;'>2017-10-23 16:55:03</td></tr><tr><td style='text-align: center;'>审核者</td><td style='text-align: center;'>〈Reviewer〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>审核者身份标识，知识对象审核者在KOI管理结构维护系统中注册后可以获得相应标识</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>审核结果</td><td style='text-align: center;'>〈ReviewResult〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>审核结论及其描述</td><td style='text-align: center;'>再次编辑。知识元名称用词不规范</td></tr></table>

<div style="text-align: center;">表 2 知识元 KOI 的管理性元数据（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>是否停用</td><td style='text-align: center;'>〈Deactivating〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>注册者因特殊需求可申请停用。一般情况该字段默认取值为“否”，即非停用状态，停用之后注册者可申请恢复</td><td style='text-align: center;'>否</td></tr><tr><td style='text-align: center;'>停用原因</td><td style='text-align: center;'>〈Deactivated Description〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>停用原因叙述</td><td style='text-align: center;'>内容失效，停止使用。</td></tr><tr><td style='text-align: center;'>停用时间</td><td style='text-align: center;'>〈DeactivatedTime〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>停用时间以注册者填写时间为准</td><td style='text-align: center;'>2022-11-23 00:00:00</td></tr></table>

### 7.2 知识集 KOI 的元数据

表 3 中所述的描述性元数据元素、表 4 中的管理性元数据元素应按照知识集各自的 KOI 编码进行注册。

<div style="text-align: center;">表 3 知识集 KOI 的描述元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>KOI编码</td><td style='text-align: center;'>〈KOI〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>知识对象标识符编码，由KOI管理机构统一分配</td><td style='text-align: center;'>0019879</td></tr><tr><td style='text-align: center;'>知识集名称</td><td style='text-align: center;'>〈KnowledgeName〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>代表知识集的规范化的自然语言词语</td><td style='text-align: center;'>混凝土材料</td></tr><tr><td style='text-align: center;'>并列名称</td><td style='text-align: center;'>〈AlternativeName〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>可表达知识集的并列的规范化自然语言词语</td><td style='text-align: center;'>Material of Concrete</td></tr><tr><td style='text-align: center;'>并列名称语言</td><td style='text-align: center;'>〈AlternativeLanguage〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>并列名称语种和并列名称成对出现，取值按照GB/T 4880.2—2000三位小写字母目录代码</td><td style='text-align: center;'>eng</td></tr><tr><td style='text-align: center;'>别名</td><td style='text-align: center;'>〈Alias〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识集名称及并列名称以外的名称</td><td style='text-align: center;'>混凝土构成材料</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>〈Description〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>对知识集的解释和说明</td><td style='text-align: center;'>混凝土的基本材料包括胶凝材料、骨料和水。为改善混凝土的某些性质，混凝土中可加入外加剂</td></tr><tr><td style='text-align: center;'>描述语种</td><td style='text-align: center;'>〈DescriptionLanguage〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>描述语种和描述成对出现，取值按照GB/T 4880.2—2000表1中的汉语名称</td><td style='text-align: center;'>汉语</td></tr><tr><td style='text-align: center;'>领域分类</td><td style='text-align: center;'>〈DomainClass〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>取值从由KOI管理机构维护的领域类型列表中选出</td><td style='text-align: center;'>建筑工程-〉建筑材料</td></tr></table>

<div style="text-align: center;">表 3 知识集 KOI 的描述元数据（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>成员</td><td style='text-align: center;'>〈Element〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识集包含的知识对象，取值为知识对象 KOI 编码，多个 KOI 编码之间通过英文分号“；”隔开</td><td style='text-align: center;'>0009871；0009872；0009873；0009874；</td></tr><tr><td style='text-align: center;'>成员数量</td><td style='text-align: center;'>〈ElementTotal〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>知识集包含的知识对象数量，通过十进制数字记录</td><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>成员重要度</td><td style='text-align: center;'>〈ElementLevel〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>每个成员与知识集的紧密的程度，分为三级，1 表示必不可少、2 表示重要、3 表示一般</td><td style='text-align: center;'>0019871|1；0019872|1；0019873|1；0019874|3；</td></tr><tr><td style='text-align: center;'>参考资料</td><td style='text-align: center;'>〈Resources〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识集的来源/出处文献资料，多个参考资料使用英文分号“；”隔开</td><td style='text-align: center;'>《建筑施工手册3》</td></tr><tr><td style='text-align: center;'>版本语言</td><td style='text-align: center;'>〈VersionLanguage〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>编辑当前版本所使用的主要语言，取值按照 GB/T 4880.2—2000 三位小写字母目录代码</td><td style='text-align: center;'>chi</td></tr><tr><td style='text-align: center;'>版本编号</td><td style='text-align: center;'>〈VersionNum〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>按照申请顺序生成的流水编号，作为版本的唯一标识</td><td style='text-align: center;'>1</td></tr></table>

<div style="text-align: center;">表 4 知识集 KOI 的管理元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>注册版本</td><td style='text-align: center;'>（RegisterNum）</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>注册版本编号，由系统生成</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>注册者</td><td style='text-align: center;'>（Registrant）</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>注册者身份标识，知识对象编辑者在KOI管理结构维护系统中注册后可以获得相应的标识。当KOI有多个语言版本时，允许多个注册者</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>注册时间</td><td style='text-align: center;'>（RegistrationTime）</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>提交KOI编码注册申请的时间，由系统自动获取和记录</td><td style='text-align: center;'>2017-10-23 15:55:03</td></tr><tr><td style='text-align: center;'>修订时间</td><td style='text-align: center;'>（RevisionTime）</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>提交知识集元数据修改的时间，由系统自动获取和记录</td><td style='text-align: center;'>2017-11-23 10:55:03</td></tr></table>

<div style="text-align: center;">表 4 知识集 KOI 的管理元数据（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>修订者</td><td style='text-align: center;'>〈Reviser〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>修订者身份标识，知识对象编辑者在KOI管理结构维护系统注册后可以获得相应的标识</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>修订描述</td><td style='text-align: center;'>〈RevisionDescription〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>对修订原因或修订细节的描述</td><td style='text-align: center;'>知识集描述不准确，修改和完善其叙述</td></tr><tr><td style='text-align: center;'>审核时间</td><td style='text-align: center;'>〈ReviewTime〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>提交审核结果的时间，由系统自动获取并记录</td><td style='text-align: center;'>2017-10-23 16:55:03</td></tr><tr><td style='text-align: center;'>审核者</td><td style='text-align: center;'>〈Reviewer〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>审核者身份标识，知识对象审核者在KOI管理结构维护系统注册后即可获得相应标识</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>审核结果</td><td style='text-align: center;'>〈ReviewResult〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>审核结论及其描述</td><td style='text-align: center;'>再次编辑。知识集名称用词不规范</td></tr><tr><td style='text-align: center;'>是否停用</td><td style='text-align: center;'>〈Deactivating〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>注册者因特殊需求可申请停用。一般情况该字段默认取值为“否”，即非停用状态，停用之后注册者可申请恢复</td><td style='text-align: center;'>否</td></tr><tr><td style='text-align: center;'>停用原因</td><td style='text-align: center;'>〈DeactivatedDescription〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>停用原因叙述</td><td style='text-align: center;'>内容失效，停止使用</td></tr><tr><td style='text-align: center;'>停用时间</td><td style='text-align: center;'>〈DeactivatedTime〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>停用时间以注册者填写时间为准</td><td style='text-align: center;'>2022-11-23 00:00:00</td></tr></table>

### 7.3 知识链 KOI 的元数据

表 5 中所述的描述性元数据元素、表 6 中的管理性元数据元素应按照知识链各自的 KOI 编码进行注册。

<div style="text-align: center;">表 5 知识链 KOI 的描述元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>KOI编码</td><td style='text-align: center;'>〈KOI〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>知识对象标识符编码，由KOI管理机构统一分配</td><td style='text-align: center;'>0029869</td></tr><tr><td style='text-align: center;'>知识链名称</td><td style='text-align: center;'>〈KnowledgeName〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>代表知识链的规范化的自然语言词语</td><td style='text-align: center;'>混凝土浇筑</td></tr><tr><td style='text-align: center;'>并列名称</td><td style='text-align: center;'>〈AlternativeName〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>可表达知识链的并列的规范化自然语言词语</td><td style='text-align: center;'>Concrete Casting Process</td></tr><tr><td style='text-align: center;'>并列名称语言</td><td style='text-align: center;'>〈AlternativeLanguage〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>并列名称语种和并列名称成对出现，取值按照GB/T 4880.2—2000三位小写字母目录代码</td><td style='text-align: center;'>eng</td></tr></table>

<div style="text-align: center;">表 5 知识链 KOI 的描述元数据（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>别名</td><td style='text-align: center;'>〈Alias〉</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识链名称及并列名称以外的名称</td><td style='text-align: center;'>混凝土浇筑工艺</td></tr><tr><td style='text-align: center;'>描述</td><td style='text-align: center;'>〈Description〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>对知识链的解释和说明</td><td style='text-align: center;'>混凝土浇筑指的是将混凝土浇筑入模直至塑化的过程</td></tr><tr><td style='text-align: center;'>描述语种</td><td style='text-align: center;'>〈DescriptionLanguage〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>描述语种和描述成对出现，取值按照GB/T 4880.2—2000表1中的汉语名称</td><td style='text-align: center;'>汉语</td></tr><tr><td style='text-align: center;'>领域分类</td><td style='text-align: center;'>〈DomainClass〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>从由KOI管理机构维护的领域类型列表中选出</td><td style='text-align: center;'>建筑工程→主体工程→混凝土工程</td></tr><tr><td style='text-align: center;'>成员</td><td style='text-align: center;'>〈Element〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>知识链包含的知识对象，取值为知识对象KOI编码，多个KOI编码之间通过英文分号“；”隔开</td><td style='text-align: center;'>0019861；0009862；0009863；0009864；</td></tr><tr><td style='text-align: center;'>起点成员</td><td style='text-align: center;'>〈FirstElement〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识链起点，取值为知识对象KOI编码，一条知识链可以包含多个起点，多个KOI编码之间通过英文分号“；”隔开</td><td style='text-align: center;'>0019861；0009862；</td></tr><tr><td style='text-align: center;'>成员数量</td><td style='text-align: center;'>〈ElementTotal〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>知识链包含的知识对象数量，通过十进制数字记录</td><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>链路信息</td><td style='text-align: center;'>〈LinkInformation〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>构成知识链中的知识对象的顺序信息，通过关系对的方式进行描述，例如（A，B）表示从A到B的关系</td><td style='text-align: center;'>（A，C）；（B，C）；（C，D）；（E，D）对应的知识链图如下所示：</td></tr><tr><td style='text-align: center;'>参考资料</td><td style='text-align: center;'>〈Resources〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>知识链的来源/出处文献资料，多个参考资料使用英文分号“；”隔开</td><td style='text-align: center;'>《建筑施工手册3》</td></tr><tr><td style='text-align: center;'>版本语言</td><td style='text-align: center;'>〈VersionLanguage〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>编辑当前版本所使用的主要语言，取值按照GB/T 4880.2—2000三位小写字母目录代码</td><td style='text-align: center;'>chi</td></tr><tr><td style='text-align: center;'>版本编号</td><td style='text-align: center;'>〈VersionNum〉</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>按照申请顺序生成的流水编号，作为版本的唯一标识</td><td style='text-align: center;'>1</td></tr></table>

<div style="text-align: center;">表 6 知识链 KOI 的管理元数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>标签</td><td style='text-align: center;'>必备性</td><td style='text-align: center;'>重复性</td><td style='text-align: center;'>描述</td><td style='text-align: center;'>示例</td></tr><tr><td style='text-align: center;'>注册版本</td><td style='text-align: center;'>(RegisterNum)</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>注册版本编号，由系统生成</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>注册者</td><td style='text-align: center;'>(Registrant)</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>注册者身份标识，知识对象编辑者在KOI管理结构维护系统中注册后即可获得相应的标识。当KOI有多个语言版本时，允许多个注册者</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>注册时间</td><td style='text-align: center;'>(RegistrationTime)</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>提交KOI编码注册申请的时间，由系统自动获取和记录</td><td style='text-align: center;'>2017-10-23 15:55:03</td></tr><tr><td style='text-align: center;'>修订时间</td><td style='text-align: center;'>(RevisionTime)</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>提交知识链修改的时间，由系统自动获取和记录</td><td style='text-align: center;'>2017/11/23 10:55:03</td></tr><tr><td style='text-align: center;'>修订者</td><td style='text-align: center;'>(Reviser)</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>修订者身份标识，知识对象编辑者在KOI管理结构维护系统注册后可即可以获得相应的标识</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>修订描述</td><td style='text-align: center;'>(RevisionDescription)</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>对修订原因或修订细节的描述</td><td style='text-align: center;'>知识链描述不准确，修改和完善其叙述</td></tr><tr><td style='text-align: center;'>审核时间</td><td style='text-align: center;'>(ReviewTime)</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>提交审核结果的时间，由系统自动获取并记录</td><td style='text-align: center;'>2017-10-23 16:55:03</td></tr><tr><td style='text-align: center;'>审核者</td><td style='text-align: center;'>(Reviewer)</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>审核者身份标识，知识对象审核者在KOI管理结构维护系统注册后即可获得相应标识</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>审核结果</td><td style='text-align: center;'>(ReviewResult)</td><td style='text-align: center;'>必备</td><td style='text-align: center;'>可重复</td><td style='text-align: center;'>审核结论及其描述</td><td style='text-align: center;'>再次编辑。知识链名称用词不规范</td></tr><tr><td style='text-align: center;'>是否停用</td><td style='text-align: center;'>(Deactivating)</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>注册者因特殊需求可申请停用。一般情况该字段默认取值为“否”，即非停用状态，停用之后注册者可申请恢复</td><td style='text-align: center;'>否</td></tr><tr><td style='text-align: center;'>停用原因</td><td style='text-align: center;'>(DeactivatedDescription)</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>停用原因叙述</td><td style='text-align: center;'>内容失效，停止使用</td></tr><tr><td style='text-align: center;'>停用时间</td><td style='text-align: center;'>(DeactivatedTime)</td><td style='text-align: center;'>有则必备</td><td style='text-align: center;'>不可重复</td><td style='text-align: center;'>停用时间以注册者填写时间为准</td><td style='text-align: center;'>2022-11-23 00:00:00</td></tr></table>

## 8 KOI 的分配原则

KOI 编码的分配应符合以下原则。

## a）唯一性

一个 KOI 只能分配给一个标识对象。当不同的词语表示同一个知识时，作为同一个知识对象进行标识，仅为其分配一个 KOI，其中当编辑语言不同时，可作为同一个 KOI 不同语言版本进行标识；当同一词语既表示知识元，又表示知识集或知识链，作为不同知识对象进行标识，为其分配不同 KOI。

## b）永久性

KOI 的分配与使用不受时间限制。当标识对象的责任者或管理责任发生变化时，KOI 及其标识对象不受影响。

## c) 顺序性

KOI 按照注册者提交编码申请的时间顺序进行分配，如果不同知识对象 KOI 申请时间完全相同，则按照知识对象名称首字母顺序进行排序分配编码。

## d）可停用

注册者可根据需求对 KOI 发起停用申请。停用后，KOI 及其标识对象依然存在，其状态由公开转为非公开，并且仅注册者本人可以查询和使用。

## e）不可修改

KOI 编码一旦通过审核分配后，就不能再进行任何形式的变更。分配的 KOI 编码可以被注销，注销的 KOI 编码不能再次分配。

## 9 KOI 的注册解析

### 9.1 KOI 的注册

KOI 通过 KOI 管理机构维护的注册系统进行注册，注册流程如图 2 所示，首先注册者填写知识对象元数据申请 KOI 编码，然后 KOI 管理机构则对接收到的编码及其元数据申请进行审核，最后 KOI 管理机构根据审核结果返回 KOI 编码，KOI 的管理遵循附录 A 的规定。

审核结果分为三种, 分别是通过、再次编辑和不通过:

a）如果审核结果为“通过”，KOI管理机构为注册者申请的知识对象分配KOI编码，录入所有元数据，并将KOI编码下发给注册者；

b) 如果审核结果为“再次编辑”，注册者需按照修改意见进行完善，再次提交知识对象标识符的申请；

c）如果审核结果为“不通过”，KOI管理机构将审核结果及其原因返回给注册者。

<div style="text-align: center;"><img src="imgs/img_in_image_box_318_206_887_811.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">图 2 KOI 注册流程</div>


### 9.2 KOI 的解析

KOI 通过 KOI 管理机构维护的解析系统进行解析，KOI 的解析流程如图 3 所示。

a）相关应用向 KOI 解析系统提交 KOI 编码，申请解析 KOI；

b) KOI 解析系统对 KOI 编码进行判断；

c) 如果 KOI 编码是有效的，则返回 KOI 标识对象的元数据；如果 KOI 无效，则返回应用错误消息及原因。

<div style="text-align: center;"><img src="imgs/img_in_image_box_375_1117_820_1467.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">图 3 KOI 解析流程</div>


## 附录 A

(规范性)

## KOI 的管理

KOI 管理机构是 KOI 编码及其元数据注册、解析、运营和推广机构，其职责包括：

a）建立 KOI 的运营系统，管理 KOI 注册、解析及相关元数据等；

b）制定 KOI 编码的审核细则，并对注册者提交的 KOI 申请进行审核；

c）为通过审核的注册者分配 KOI 编码；

d）解析 KOI 编码，并返回相应元数据；

e）管理 KOI 元数据结构，录入、维护和更新 KOI 元数据，并保证 KOI 元数据的可靠性和准确性；

f）维护领域分类，并根据用户反馈及时更新领域分类表；

g）管理 KOI 的注册者、修订者和审核者标识，并维护其元数据信息；

h）提供 KOI 编码的查询，让用户能够查找与某个元数据相关的 KOI 编码或者 KOI 编码对应的元数据；

i) 提供 KOI 的查重、咨询和培训服务；

i) 推广、协调、监督 KOI 的应用。

## 参考文献

[1] GB/T 23703.2—2010 知识管理 第 2 部分: 术语

[2] GB/T 38377—2019 新闻出版 知识服务 知识资源建设与服务基础术语