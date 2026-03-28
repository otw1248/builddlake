

# 中华人民共和国国家标准

GB/T 38378—2019

# 新闻出版 知识服务 知识关联通用规则

# Press and publication—Knowledge services—General rules of knowledge association

2019-12-31 发布

2020-07-01 实施

国家市场监督管理总局发布

国家标准化管理委员会

## 目次

前言 …… I  
  
1 范围 …… 1  
  
2 规范性引用文件 …… 1  
  
3 术语和定义 …… 1  
  
4 缩略语 …… 1  
  
5 知识关联的原则 …… 2  
  
5.1 目的性原则 …… 2  
  
5.2 多样性原则 …… 2  
  
5.3 规范性原则 …… 2  
  
5.4 适应性原则 …… 2  
  
5.5 可管理性原则 …… 2  
  
6 知识关联的类型 …… 2  
  
6.1 知识关联类型的划分维度 …… 2  
  
6.2 按相关度划分 …… 2  
  
6.3 按关联方法划分 …… 2  
  
6.4 按领域范围划分 …… 3  
  
7 知识关联的构建 …… 3  
  
7.1 知识获取 …… 3  
  
7.2 知识描述 …… 3  
  
7.3 关联建立 …… 3  
  
7.4 知识存储和应用 …… 3  
  
8 知识关联的表达 …… 3  
  
8.1 知识关联的表达原则 …… 3  
  
8.2 知识关联的表达规则 …… 3  
  
8.3 词汇表的定义 …… 4  
  
8.4 知识关联对象的 URI …… 4  
  
8.5 语义化属性词汇的选择和定义 …… 4  
  
8.6 跨域知识关联的表达 …… 5  
  
8.7 跨域的知识关联方式 …… 6  
  
9 关联数据的发布 …… 6  
  
参考文献 …… 7

## 前言

本标准按照 GB/T 1.1—2009 给出的规则起草。

本标准由国家新闻出版署提出。

本标准由全国新闻出版标准化技术委员会(SAC/TC 527)归口。

本标准起草单位：中国大地出版社有限公司、知识产权出版社有限责任公司、中国新闻出版研究院、中国水利水电出版社有限公司、中地数媒（北京）科技文化有限责任公司、北京中知智慧科技有限公司、海洋出版社、中华书局有限公司、中国林业出版社有限公司、中国法制出版社有限公司、成都音像出版社有限公司、英大传媒投资集团有限公司、中国科技出版传媒股份有限公司、九州出版社有限公司、武汉大学、河北领先文化传播有限公司、苏州梦想人软件科技有限公司。

本标准主要起草人：刘化冰、张新新、谢冰、唐学贵、孙涛涛、倪薇钧、朱欣昱、于晓华、李烨、江波、孙巍、张保生、彭天赦、干生洪、樊慧、雍志娟、任彦、张锴、戚雪、王玥、王帅。

# 新闻出版 知识服务 知识关联通用规则

## 1 范围

本标准规定了知识关联的原则、知识关联的类型、知识关联的构建、知识关联的表达和关联数据的发布。

本标准适用于新闻出版及相关领域知识服务产品的开发与应用。

## 2 规范性引用文件

下列文件对于本文件的应用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 38377—2019 新闻出版 知识服务 知识资源建设与服务基础术语

## 3 术语和定义

GB/T 38377—2019 界定的以及下列术语和定义适用于本文件。

### 3.1 

统一资源标识符 uniform resource identifier; URI

包含名字或地址的短数据串，指向 web 上的某个对象。

[GB/T 25069—2010, 定义 2.1.39]

### 3.2 

关联属性词汇 attribution vocabulary of association

用于描述知识的各种属性和知识关联中各种关系的规范化词汇。

### 3.3 

资源描述框架 resource description framework: RDF

由万维网联盟制定的一种用来表示 web 资源的特性以及资源之间关系的表示规范。

### 3.4 

资源描述框架模式 RDF schema: RDFS

由万维网联盟制定的基于资源描述框架的数据建模词汇集。

### 3.5 

跨域知识关联 cross domain knowledge association

来源于不同领域的知识和知识之间通过一定规则所建立的关系。

### 3.6 

词汇表 terminology list

在一个特定的领域表示系统性概念的词汇集合。

## 4 缩略语

下列缩略语适用于本文件。

ISLI: 国际标准关联标识符(International Standard Link Identifier)

OWL: OWL 网络本体语言 (OWL Web Ontology Language)

SKOS: 简单知识组织系统 (Simple Knowledge Organization System)

XML: 可扩展标记语言 (Extensible Markup Language)

FOAF: FOAF 词汇表 (Friend Of A Friend)

DOAP:DOAP 词汇表 (Description of A Project)

KLSV: 自定义的知识关联词汇(Knowledge Linking Service Vocabulary)

## 5 知识关联的原则

### 5.1 目的性原则

构建知识关联应与知识获取的特定需求目的相结合。

### 5.2 多样性原则

建立各种知识之间的多种关联关系，包括知识组织体系中各知识概念之间的关联关系、知识元之间的关联关系和跨域知识之间的关联关系等。

### 5.3 规范性原则

所构建的知识关联信息应能够进行访问和整合，以支持跨机构、跨行业的知识共享。

### 5.4 适应性原则

满足知识及构建环境的动态变化，具备一定的灵活性、扩展性和适应性。

### 5.5 可管理性原则

所构建的知识关联信息应对其知识产权等建立必要的管理机制。

## 6 知识关联的类型

### 6.1 知识关联类型的划分维度

可按照相关度、关联方法和领域范围对知识关联的类型进行划分。

### 6.2 按相关度划分

按相关度可划分为：

a）同一性关联，对知识之间所具有的某种程度的相同（或相似）之处所形成的关联关系；

b）隶属性关联，构成某知识或知识集合，隶属于某一概念、范畴和类别的逻辑关系，是由知识本身的性质决定的，常见的隶属关系包括属分、包含等关系；

c) 相关性关联，在同一性、隶属性关联关系之外，知识之间所具有的相互依存、相互渗透、相互制约、相互作用的关系，一般是指相反、相对、因果、引用、应用、影响等各种关系，其关联关系可以是不严格固定的，其数量关系也可以是不完全确定的。

### 6.3 按关联方法划分

按关联方法可划分为：

a）直接关联关系，通过知识的表达可以直接识别和发现的关联关系，可以从知识表达的对象中直接识别和发现，也可以通过引用规范的词汇表识别和发现。常见的直接知识关联包括：学科关联、主题关联、文献外部特征关联（如分类、作者、引文、标题、机构、期刊等）；

b）间接关联关系，通过知识的表达无法直接识别和发现，通过词汇表也无法建立识别，需要通过数据挖掘或语义网络才能够发现的知识关联关系。常见的间接知识关联包括：共引关联、共词关联、组配关联、同概念关联等。

### 6.4 按领域范围划分

按领域范围可划分为：

a）本领域知识关联关系，本领域范围的知识之间所建立的关联关系；

b）跨领域知识关联关系，不同领域范围的知识之间所建立的关联关系。

## 7 知识关联的构建

### 7.1 知识获取

<div style="text-align: center;"><img src="imgs/img_in_image_box_677_599_718_638.jpg" alt="Image" width="3%" /></div>


利用知识发现和数据挖掘等技术，对数字内容资源进行加工处理，经提炼、整合、完善和分解，形成知识。

### 7.2 知识描述

宜采用 RDF、OWL、主题词表等方法对获取的知识进行描述。

### 7.3 关联建立

对知识之间的关联关系进行描述，所建立的知识关联关系包括关联属性和/或其链接。

### 7.4 知识存储和应用

对知识及其关联关系进行存储，形成知识库，在此基础上建立相关的应用，实现知识关联信息的发布。

## 8 知识关联的表达

### 8.1 知识关联的表达原则

通过计算机可理解的语言规范和技术将知识关联信息进行结构化标识。宜遵循以下原则：

a）采用资源描述框架(RDF)来表达知识关联；

b）采用统一资源标识符(URI)和实体名词作为知识关联中的三要素进行标识；

c） 利用 HTTP URI 以方便资源对象的可定位查找。

### 8.2 知识关联的表达规则

#### 8.2.1 资源描述框架

在揭示资源之间的语义关系时，宜采用 RDFS 定义资源的类型、属性。

#### 8.2.2 知识关联的表达

知识关联宜采用 RDF 表达，通过 URI 或 ISLI 等进行标识。

#### 8.2.3 知识关联的语法规范

知识关联的表达形式可采用 XML 语法规范。

### 8.3 词汇表的定义

应符合下列要求：

a）通过 RDF 可采用元数据词汇作为描述特定资源的规范化属性，也可根据不同的知识关联类型和领域，自定义元数据词汇规范；

b) 具体定义方法可通过规范元数据词汇表和指定 URI 实现，在具体的 RDF 描述中使用命名空间来表示该词汇表，并在属性的定义中采用该词汇表中的词汇。

### 8.4 知识关联对象的 URI

在知识关联对象的描述中，可使用 URI 作为实体的标识名称。该 URI 应满足如下要求：

a）在指定的命名空间内定义知识对象的 URI；

b) 选择知识对象合适的主键，确保每个知识对象 URI 的唯一性；

c）保证 URI 的长期存在和可解释；

d）尽量保证 URI 短小、易记。

### 8.5 语义化属性词汇的选择和定义

#### 8.5.1 关联属性词汇

主体资源及其属性值宜采用 URI 标识的知识对象，需通过标识属性的谓语 URI 描述两者之间的关联关系。该谓语来自公认词汇，也可来自自定义词汇。

#### 8.5.2 公认词汇

描述知识关联可使用以下公认的词汇：

a）使用 FOAF 词汇表描述科研人员兴趣、专业、单位以及之间的关系；

b）使用复审词汇描述知识产品和服务的评价；

c) 使用简单知识组织系统(SKOS)描述分类表；

d）使用网络本体语言(OWL)描述知识本体；

e） 使用项目描述(DOAP)词汇表描述知识项目。

#### 8.5.3 属性自定义

在描述知识关联时，宜采用自定义的知识关联词汇（KLSV）对主体资源和属性值之间关联关系以及跨域知识之间关联关系进行描述。KLSV 对主体资源和属性值之间关联关系见表 1。

<div style="text-align: center;">表 1 KLSV 对主体资源和属性值之间关联关系</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Is equivalent to</td><td style='text-align: center;'>主体资源和属性值描述相同知识</td></tr><tr><td style='text-align: center;'>Standard</td><td style='text-align: center;'>属性值是经过规范的知识</td></tr><tr><td style='text-align: center;'>Generic</td><td style='text-align: center;'>属性值是上位知识信息</td></tr><tr><td style='text-align: center;'>Specific</td><td style='text-align: center;'>属性值是下位知识信息</td></tr></table>

## 表 1 (续)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>定义</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>Related</td><td style='text-align: center;'>属性值是主体资源的相关知识信息</td></tr><tr><td style='text-align: center;'>Field</td><td style='text-align: center;'>属性值是主体资源所属领域信息</td></tr><tr><td style='text-align: center;'>Classification</td><td style='text-align: center;'>属性值是主体资源所属分类类目信息</td></tr><tr><td style='text-align: center;'>Citation</td><td style='text-align: center;'>属性值是主体资源的引用知识或文献信息</td></tr><tr><td style='text-align: center;'>Logic</td><td style='text-align: center;'>属性值是主体资源的逻辑关联关系信息</td></tr><tr><td style='text-align: center;'>Sequence</td><td style='text-align: center;'>属性值是主体资源的时间、地点和数列等顺序信息</td></tr><tr><td style='text-align: center;'>Multimedia</td><td style='text-align: center;'>属性值是主体资源的多媒体信息关联</td></tr><tr><td style='text-align: center;'>Website</td><td style='text-align: center;'>属性值是主体资源的相关网址链接</td></tr><tr><td style='text-align: center;'>Source</td><td style='text-align: center;'>属性值是主体资源的知识所属来源</td></tr><tr><td style='text-align: center;'>Similar</td><td style='text-align: center;'>属性值是主体资源的同类别或相似知识信息</td></tr><tr><td style='text-align: center;'>Identification</td><td style='text-align: center;'>属性值是主体资源的关联标识符</td></tr><tr><td style='text-align: center;'>Same as</td><td style='text-align: center;'>属性值与主体资源相同或相等</td></tr><tr><td style='text-align: center;'>Contain</td><td style='text-align: center;'>主体资源包含属性值</td></tr><tr><td style='text-align: center;'>Belong to</td><td style='text-align: center;'>主体资源隶属于属性值</td></tr><tr><td style='text-align: center;'>Opposite</td><td style='text-align: center;'>属性值与主体资源是相对或相反关系</td></tr><tr><td style='text-align: center;'>Reason is</td><td style='text-align: center;'>主体资源是属性值的原因</td></tr><tr><td style='text-align: center;'>Result is</td><td style='text-align: center;'>主体资源是属性值的结果</td></tr><tr><td style='text-align: center;'>Cite</td><td style='text-align: center;'>主体资源引用属性值</td></tr><tr><td style='text-align: center;'>Cite by</td><td style='text-align: center;'>主体资源被属性值引用</td></tr><tr><td style='text-align: center;'>Used by</td><td style='text-align: center;'>属性值应用于主体资源</td></tr><tr><td style='text-align: center;'>Effect</td><td style='text-align: center;'>主体资源对属性值产生影响</td></tr><tr><td style='text-align: center;'>Coexist with</td><td style='text-align: center;'>主体资源和属性值同时出现</td></tr><tr><td style='text-align: center;'>Match</td><td style='text-align: center;'>主体资源和属性值是相互匹配关系</td></tr><tr><td style='text-align: center;'>Near</td><td style='text-align: center;'>主体资源和属性值相邻或相近</td></tr><tr><td style='text-align: center;'>Similar to</td><td style='text-align: center;'>主体资源和属性值相似</td></tr><tr><td style='text-align: center;'>Is concept of</td><td style='text-align: center;'>属性值是主体资源的概念描述</td></tr><tr><td style='text-align: center;'>cluster of</td><td style='text-align: center;'>属性值是主体资源的聚类表述</td></tr><tr><td style='text-align: center;'>sequence up</td><td style='text-align: center;'>主体资源和属性值依顺序升序关联</td></tr><tr><td style='text-align: center;'>sequence down</td><td style='text-align: center;'>主体资源和属性值依顺序降序关联</td></tr></table>

### 8.6 跨域知识关联的表达

应符合下列要求：

a）在表达跨域知识关联的 RDF 表达中，当主语和宾语来自不同的知识，宜通过谓语来构建主语和宾语之间的关联关系；

b）具有重要影响的跨域知识关联谓词，宜采用基于不同行业领域知识自定义的谓语词汇表来表达跨域知识关联，宜采用 RDFS 等其他词汇表表达跨域知识关联关系。

### 8.7 跨域的知识关联方式

#### 8.7.1 等同关联

通过某一关联数据集中知识对象指向其他数据集中相同知识对象的链接来建立等同关联关系。示例：当同一知识对象在多个关联数据集中被赋予不同的 URI 时，可在 URI 标识之间建立等同链接。

#### 8.7.2 词汇关联

应符合下列要求：

a）对于基于关联数据的知识关联，可通过异构词汇表之间的词汇关联来实现聚合；

b）通过知识关联词汇表中某一概念术语指向其他与之存在知识关联的名词术语的链接来建立词汇关联关系；

c) 可采用常用的词汇性链接，如 RDFS 或 OWL 本体语言所提供的属性关联，也可自定义关联关系属性。

#### 8.7.3 相关性关联

应符合下列要求：

a）通过某一关联数据集中知识对象指向其他数据集中与之存在相关性的其他知识对象的链接来建立相关性关联关系；

b）相关性关联的谓语可采用跨域关联关系的自定义属性，也可采用包含相关性链接谓语词汇的权威词汇表。

## 9 关联数据的发布

根据数据量的大小、数据的更新频率、数据的存储方式和访问方式的不同，宜采用以下方式发布关联数据：

a) 静态发布，发布静态的关联关系文件，例如 RDF 文件或 XML 文件，适用于数据量很小的情况；

b）批量存储，将关联关系文件存储在数据库中，可采用服务器作为关联数据服务的前端，适用于数据量大的情况；

c）调用时生成，在请求数据时根据原始数据在线生成数据，适用于更新频率大的情况；

d）事后转换，采用从关系数据库到RDF数据转换，适用于将关系数据库存储的数据内容发布成关联数据。

## 参考文献

[1] GB/T 5271.5—2008 信息技术 词汇 第 5 部分: 数据表示

[2] GB/T 20001.1—2001 标准编写规则 第1部分：术语

[3] GB/T 25069—2010 信息安全技术 术语

[4] GB/T 25100—2010 信息与文献 都柏林核心元数据元素集

[5] GB/T 32867—2016 中国标准关联标识符(ISLI)

[6] DL/T 890.501—2007 能量管理系统应用程序接口(EMS-API) 第 501 部分: 公共信息模型的资源描述框架(CIM RDF) 模式

[7] ISO 26324:2012 Information and documentation—Digital object identifier system

[8] W3C XML Schema http://www.w3.org/standards/techs/xmlschema#completed

[9] W3C RDF (Resource Description Framework, 资源描述框架) http://www.w3.org/standards/semanticweb/data

[10] FOAF http://www.foaf-project.org/

[11] SKOS https://www.w3.org/2001/sw/wiki/SKOS

[12] OWL https://www.w3.org/2001/sw/wiki/OWL

[13] DOAP http://www.chuci.info/view/schema/97ac7e9e37694a238d7e3ca5b84efa38