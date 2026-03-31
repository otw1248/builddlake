

JR/T 0294.1—2024

# 金融市场交易报告数据要素指南 第 1 部分：全球唯一产品识别码

# Guide on data elements of financial market trade reporting—Part 1: Unique product identifier

2024-09-03 发布

2024-09-03 实施

Powered by TCPDF (www.tcpdf.org)

## 目次

前言.....II    
引言.....III    
1 范围.....1    
2 规范性引用文件.....1    
3 术语和定义.....1    
4 UPI 的用途和关键概念.....2    
5 UPI 的基本特征.....3    
6 UPI 参考数据.....5    
7 标的资产识别码.....11    
8 UPI 代码的结构和格式.....12    
附录 A（规范性）UPI 分配过程.....13    
附录 B（资料性）UPI 代理模式.....16    
附录 C（资料性）UPI 用户分类及权限.....18    
附录 D（资料性）参考数据元素取值示例（按资产类别）.....19    
附录 E（规范性）UPI 校验位计算过程.....24    
参考文献.....26

## 前言

本文件按照GB/T 1.1—2020《标准化工作导则 第1部分：标准化文件的结构和起草规则》的规定起草。

本文件是JR/T 0294—2024《金融市场交易报告数据要素指南》的第1部分。JR/T 0294—2024已经发布了以下部分：

——第1部分：全球唯一产品识别码；

第2部分：全球唯一交易识别码；

——第3部分：其他关键数据要素。

请注意本文件的某些内容可能涉及专利。本文件的发布机构不承担识别专利的责任。

本文件由全国金融标准化技术委员会（SAC/TC 180）提出并归口。

本文件起草单位：中国人民银行科技司、中国证券监督管理委员会科技监管司、银行间市场清算所股份有限公司、中证机构间报价系统股份有限公司、中国人民银行福建省分行、北京国家金融标准化研究院有限责任公司、中国银行间市场交易商协会、成方金融科技有限公司、中国期货市场监控中心有限责任公司。

本文件主要起草人：李伟、杨富玉、李兴锋、蒋东兴、戴德毅、何鹏、卢欢、狄休、冯蕾、刘子群、周云晖、王蕾蕾、孙涛、孔方洁、林光丰、张燕、林羽、陈锦铃、周夕崇、谢彦丽、张晋钰、贺宇、丁旸钧天、唐卓、李佳凝、吴冠华、姜才康、茅廷、胡冰冰、林茜漾、杨光、李钟、刘萌、凌肯、秦菁、张小雪。

## 引言

2009年二十国集团（G20）峰会提出，为提高市场透明度和降低系统性风险，所有场外衍生品合约均需向交易报告库（TR）报告，这是场外衍生品市场改革的重要一环。2014年金融稳定理事会（FSB）发布了关于建立全球数据标准机制的可行性研究报告，建议引入全球法人识别编码（LEI）以及创建全球唯一交易识别码（UTI）和全球唯一产品识别码（UPI）。

为了更好地为我国金融市场交易报告制度建设提供标准支持，现根据支付与市场基础设施委员会（CPMI）和国际证监会组织（IOSCO）发布的《UPI协调技术指南》制定本文件，旨在为每一个场外衍生品分配唯一字符串，提出UPI的代码格式和结构，规定UPI的基本特征和分配过程，使UPI能够成为跨系统、跨流程的数据要素。

Powered by TCPDF (www.tcpdf.org)

# 金融市场交易报告数据要素指南   第 1 部分：全球唯一产品识别码

## 1 范围

本文件提供了全球唯一产品识别码（UPI）的用途和关键概念、UPI的基本特征、用于唯一识别场外衍生品的参考数据元素以及包含在UPI参考数据中各种标的资产的识别码、UPI代码的结构和格式等内容。

本文件适用于唯一识别场外衍生品管理部门要求向交易报告库报送的所有场外衍生品。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 2260—2007 中华人民共和国行政区划代码

GB/T 12406—2022 表示货币的代码

GB/T 17710—2008 信息技术 安全技术 校验字符系统

GB/T 27926—2021 金融服务 金融业通用报文方案

ISO 4914:2021 金融服务 唯一产品识别码（Financial services—Unique product identifier (UPI)）

## 3 术语和定义

下列术语和定义适用于本文件。

3.1

全球唯一产品识别码 unique product identifier；UPI

在交易过程中唯一识别每个场外衍生品的代码。

### 3.2 

全球唯一交易识别码 unique transaction identifier; UTI

在交易主体和（或）在该交易发生的管理体系的认可下，分配给一笔金融交易的全球唯一字符串。

[来源：JR/T 0294.2—2024，3.1]

3.3

法定实体 legal entity

法人

根据法律成立的组织。

[来源：GB/T 42495.1—2023，3.1]

## 4 UPI 的用途和关键概念

### 4.1 UPI 的用途

UPI的用途是唯一识别场外衍生品管理部门要求向交易报告库报送的所有场外衍生品。UPI代码、UPI参考数据的组合以及将UPI代码分配给1组特定参考数据的过程构成了UPI系统。UPI参考数据包括1组与任何给定场外衍生工具类型和标的资产相关的参考数据元素。每个参考数据元素都包含1组允许该参考数据元素使用的值（例如数据元素“资产类别”可能包含表示“信用”“利率”“大宗商品”“权益”或“外汇交易”的值）。参考数据元素及其允许值的示例见6.2。

UPI旨在统一全球的交易报告库数据标准，支持全球性数据汇总，并有助于场外衍生品管理部门获得全球性的场外衍生品交易市场情况。此外，UPI支持不同类型的衍生品数据灵活汇总，例如将UPI参考数据元素的值进行分组，支持对具有统一标的资产（例如1个特定的货币对、货币组合、债券）的所有场外衍生品交易的数据汇总。

### 4.2 UPI 和其他报告数据的关系

场外衍生品合约被描述成交易数据并向交易报告库报告，通过组合属于该合约交易的UPI和其他数据元素（除UPI参考数据元素外）进行描述。场外衍生品交易则会被描述成交易报告库中的数据，通过组合数据元素和唯一标识的UTI进行描述。

UPI不宜确定特定场外衍生品是否属于一揽子交易的一部分，因为这可通过在交易层面的其他数据元素更好地获得。

### 4.3 UPI 参考数据元素

场外衍生品可通过UPI参考数据元素进行唯一表示，UPI参考数据元素可分为以下3类。

a）工具类型，例如互换（掉期）。

b）工具特性，例如可摊销。

c）标的资产的相关信息，例如利率指数、3个月欧元银行间拆借利率。

UPI可通过UPI参考数据元素的组合识别每个场外衍生品。UPI代码可标识唯一的场外衍生品，每个单独的UPI代码代表1组UPI参考数据元素及其值。

注：在特定情况下，UPI可能代表不止1种场外衍生品，因为当参考数据元素值被赋值为“其他”，或者标的为一揽

子资产时，标的资产数据将直接报告给交易报告库并不被包含在UPI参考数据中。

场外衍生品、场外衍生合约和场外衍生交易的区别见图1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_377_200_837_716.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">图1 场外衍生品、场外衍生合约和场外衍生交易的区别</div>


### 4.4 UPI 参考数据库

UPI保存在场外衍生品管理部门和市场参与者可访问的参考数据库中，该参考数据库将存储UPI代码及相关的UPI参考数据。场外衍生品管理部门和市场参与者在参考数据库中基于UPI代码检索到参考数据元素及其值，或基于参考数据元素及其值检索到UPI代码。参考数据库的操作和维护及UPI代码的分配由UPI服务提供商完成。

注：UPI服务提供商是由FSB指定的、负责运营和维护UPI参考数据库并为每个场外衍生品产品分配UPI代码的实体。

为了获得给定场外衍生品的新UPI代码，市场参与者（例如交易方、交易所）可组合形成1个与场外衍生工具及其标的资产有关的、具有唯一特征的参考数据元素值集合，并提供给参考数据库。UPI分配过程见附录A，其代理模式见附录B、用户分类及权限见附录C。

UPI参考数据库由UPI服务提供商创建和操作以实现UPI代码的分配，以此生成的UPI代码可被用于场外衍生品管理部门数据汇总。存储在参考数据库中数据的值、质量、维护和配置，将很大程度上决定最终UPI代码用于报告的可用性和可靠性。

## 5 UPI 的基本特征

### 5.1 全球统一

UPI宜仅基于产品详细体现其固有技术特征，以实现全球协调统一，有助于UPI系统在全球范围内适用，从而支持数据汇总。

为了使UPI实现全球协调统一，所有包含在场外衍生品参考数据中的值宜在最大范围内满足各管辖区内的标准。

### 5.2 ——对应

在特定的时间点，每个可报告的场外衍生品可由1组不同的UPI参考数据元素及其值来识别。每个可报告的场外衍生品宜具有不同的UPI代码和其关联的不同的UPI参考数据元素及其值。例如，1组不同的UPI参考数据元素及其值与1个UPI代码相关联，1个UPI代码也与1组不同的UPI参考数据元素及其值相关联。

与UPI参考数据元素相关联的值可精确和详细地描述1个场外衍生品，以便产品具有唯一定义，但不宜涉及合约或交易的描述。

为了适应市场变化（见5.5），包括通用值在内（例如“其他”）的部分UPI参考数据元素可能会随着时间的推移被更具描述性的值替换。因此，一一对应特征仅针对特定时间点的指定UPI，在不同时间点可通过不同的UPI参考数据元素及其值来识别相同的产品，便于在需要改变UPI参考数据元素值的情况下同时满足适应变化特征。

在特定的UPI代码已分配给1个场外衍生品后，不宜将该UPI代码分配给其他场外衍生品。

### 5.3 描述一致

UPI参考数据使用1组一致的UPI参考数据元素来描述每个场外衍生品。不同的资产类别可使用不同的UPI参考数据元素集来表示，从而反映特定资产类别的工具和标的资产的特征。

与特定资产类别相关联的产品可能用到与其他资产类别相关联的产品不同的参考数据元素集，例如用于描述利率类衍生品的UPI参考数据元素集可能与用于描述信用类衍生产品的UPI参考数据元素集不同，与股权类衍生产品或外汇类衍生产品等的UPI参考数据元素集也不同。然而描述1个特定类别衍生品宜与同类别的衍生品采用相同的参考数据元素，例如利率衍生品与其他任何利率类衍生品采用相同的参考数据元素集。

### 5.4 代码不变

当场外衍生品的UPI代码被分配、UPI参考数据元素值被确定时，宜保持UPI代码和UPI参考数据元素值不变。除特殊情况外，不宜为同一产品分配不同的UPI代码和UPI参考数据元素值。

在可行的范围内，场外衍生品的UPI代码和参考数据元素宜在产品的生命周期内持续存在。随着市场的发展，可取的产品描述更加具体或以前定制的产品交易范围变广（见5.2）。在这种情况下，场外衍生品有1个参考数据元素，其值为“其他”，该调整宜具有前瞻性，并适应市场变化（见5.5）。

在UPI代码被初始分配后，UPI参考数据元素值宜保持稳定，以便随着时间的推移能够支持对产品的持久分析。

### 5.5 适应变化

UPI参考数据元素值宜及时适应市场变化和创新，包括引入新的场外衍生品以及响应管理部门不断变化的综合需求。每个UPI参考数据元素的允许值宜包含所需的变化。

版本控制有助于合并不同的变更内容。UPI参考数据元素值的长期管理宜包含可直接跨版本进行比较的方法，例如将新UPI映射到代表类似产品的旧UPI机制。对UPI参考数据元素及其值的修订宜保持历史版本之间的前后兼容性。

为满足5.7和5.11，同时为了使具有新的特征或定制特征的产品更新到更精确的定义，宜将某些UPI参考数据元素的可取值设置为“其他”。

### 5.6 属性清晰

UPI参考数据元素宜清晰明确，并提供全面和免费的技术文档、说明和规范，有利于市场参与者理解和使用UPI，例如提供每个UPI参考数据元素在UPI参考数据库的可取值范围。

### 5.7 易于检索

分配、检索、查询UPI的需求不宜影响交易对手执行交易或及时报告交易数据。

市场参与者可便捷查询特定产品是否已经存在UPI，并在需要时可使用UPI服务提供商分配的新UPI代码或及时检索现有的UPI代码，从而不影响其交易或不影响其在规定的时限内向交易报告库提供报告。

### 5.8 长期有效

UPI宜保持长期有效，并合理地独立于未来可能发生的技术、市场行为、法律环境的变化。

适应变化特征关注UPI参考数据适应场外衍生品创新的能力，而长期有效特征关注可能影响UPI使用方式的其他因素，例如技术、市场行为、法律环境的变化。

### 5.9 范围中立

UPI宜保持范围中立，即在全球的场外衍生品报告制度和范围存在差异的情况下仍然有效。

### 5.10 系统兼容

UPI宜兼容现有金融市场基础设施（例如交易报告库）、市场参与者和管理部门使用的信息系统。

### 5.11 覆盖全面

UPI宜全面考虑任意1种场外衍生品的报告需求，并必须满足多样的管理要求，包括市场监测、风险分析、公开发布市场信息和政策研究。UPI还宜具备支持提高市场透明度、改进风险管理和提高运营效率的功能。

### 5.12 便于扩展

UPI宜兼容或适应更广泛的金融产品（包括在交易所交易的衍生产品）。

### 5.13 精准定位

UPI的设计宜清晰明确，以使管理部门能履行其管理职责，并具有充分的细节和合适的粒度级别。

UPI描述相关参考数据时，宜描述得具体和有辨别性，同时可高效和精确地进行数据汇总，从而满足管理部门的要求，例如具体性和辨别性的水平可通过资产类别确定。

### 5.14 公共传播

UPI宜满足公共传播场外衍生品数据的需求，通过传播UPI代码代替传播与交易产品有关的大量数据元素值，以提高公共传播效率。市场参与者可借助使用UPI参考数据库中产品的参考数据元素及其值，实现透明的场外衍生品交易和有效的价格发现。

### 5.15 易于展示

UPI代码的格式和表示（例如字符集）宜使UPI代码可通过普遍接受的金融交易通信手段来传输，并易于展示。

## 6 UPI 参考数据

### 6.1 UPI 参考数据粒度级别

UPI参考数据粒度级别是本文件的关键方面。场外衍生品合约基于标的资产存在。产品的可识别数据要形成有意义的汇总数据，包括对标的资产的识别。从汇总数据的层面看，场外衍生品的风险随着标的资产的不同而变化。

1个识别标的资产或基准指标的识别码宜被纳入UPI参考数据。具有不同的基准指标的类似产品宜具有不同的UPI。有关标的资产（例如基准指标、一揽子标的和参考实体）的信息可反映在UPI参考数据中。

在某些资产类别（例如大宗商品）中，当缺乏标准化或正式认可的标的资产识别码时，可说明如何验证和维护标的资产识别码。

### 6.2 参考数据元素的规范

#### 6.2.1 UPI 参考数据元素描述（所有资产类别）

场外衍生品市场通常基于不同资产类别构建。围绕资产类别对衍生品进行分类，不同资产类别的参考数据元素取值示例见附录D。表1提供了所有资产类别的每个UPI参考数据元素描述，可按资产类别给出产品的准确画像。

<div style="text-align: center;">表1 所有资产类别的每个UPI参考数据元素描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>数据元素描述</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>衍生品合约挂钩的资产、基准或其他衍生品合约标的，包括信用、利率、大宗商品、权益和外汇交易。</td></tr><tr><td style='text-align: center;'>货币对</td><td style='text-align: center;'>外汇衍生品合约中的货币对。</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>衍生品合约结算时交付实物资产或支付现金。</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）、期权、远期等。</td></tr><tr><td style='text-align: center;'>支付频率</td><td style='text-align: center;'>定额、递增、递减、自定义等。</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>指定何时可行权。欧式期权只能在行权日行权；美式期权可在合约期间任意时间行权；百慕大期权可在合约规定的特定时间段内行权。</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>指定期权是否赋予买方购买标的的权利（即看涨期权）、出售标的的权利（即看跌期权），或在行权时选择买入或卖出标的的权利（即选择期权）。</td></tr><tr><td style='text-align: center;'>收益、定价方法或支付触发方式</td><td style='text-align: center;'>收益指合约的损益是如何确定的；定价方法指合约是如何定价的；支付触发方式指促使合约触发执行的事件。</td></tr><tr><td style='text-align: center;'>优先级</td><td style='text-align: center;'>衍生品合约下债务或一揽子债务的优劣顺序。</td></tr><tr><td style='text-align: center;'>结算渠道</td><td style='text-align: center;'>合约资金结算中使用的支付系统。</td></tr><tr><td style='text-align: center;'>结算货币</td><td style='text-align: center;'>以现金结算的合同，在结算时交付的货币币种。</td></tr><tr><td style='text-align: center;'>单一或多种货币</td><td style='text-align: center;'>衍生品标的是单一货币或多种货币。</td></tr><tr><td style='text-align: center;'>单期限或多期限</td><td style='text-align: center;'>衍生品标的的指数是单一期限或多期限。</td></tr><tr><td style='text-align: center;'>标准合约规范</td><td style='text-align: center;'>提供应用于合约的标准术语和条款的现有文档或引用的名称。该文档或引用说明合约中的标的资产或基准指标如何被UPI中指定的标的资产编号和标的资产编号源所识别。</td></tr></table>

<div style="text-align: center;">表1 所有资产类别的每个UPI参考数据元素描述（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>数据元素名称</td><td style='text-align: center;'>数据元素描述</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>1种识别码，可用于确定合约中约定的资产、指数或比较基准。</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>关联的标的资产编号的来源或发布者。</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td style='text-align: center;'>对衍生品约定的资产、指数或合约特征的大致分类描述。</td></tr><tr><td style='text-align: center;'>标的资产或合约的子类型</td><td style='text-align: center;'>对衍生品标的资产或合约特征的更细节的分类描述。</td></tr><tr><td style='text-align: center;'>标的信用指数系列</td><td style='text-align: center;'>反映指数在一定时期内的组成成分。</td></tr><tr><td style='text-align: center;'>标的信用指数版本</td><td style='text-align: center;'>反映标的信用指数系列在生命周期内索引成分的任何变化的数字。</td></tr><tr><td style='text-align: center;'>标的利率指数周期</td><td style='text-align: center;'>利率指数期限的时间单位（例如日、周、月）。</td></tr><tr><td style='text-align: center;'>标的利率指数期限乘数</td><td style='text-align: center;'>按利率指数周期单位时间计算的数量。</td></tr><tr><td style='text-align: center;'>标的合约期限</td><td style='text-align: center;'>标的合约期限的时间单位。</td></tr><tr><td style='text-align: center;'>标的合约期限乘数</td><td style='text-align: center;'>按标的合约期限单位时间计算的数量。</td></tr><tr><td style='text-align: center;'>标的票据期限</td><td style='text-align: center;'>标的资产期限的时间单位（例如债券）。</td></tr><tr><td style='text-align: center;'>标的票据期限乘数</td><td style='text-align: center;'>按标的资产期限单位时间计算的数量（例如债券）。</td></tr><tr><td colspan="2">注：1. 欧式期权是买入期权的一方在期权到期日当天才能行使的期权。百慕大期权是1种可在到期前所规定的一系列时间行权的期权。2. 对于具有多个标的工具的产品，可在参考数据中采用与这些标的工具相关的多个字段的值表示。</td></tr></table>

#### 6.2.2 UPI 参考数据元素取值（按资产类别）

资产类别为信用的UPI参考数据元素取值宜见表2。

<div style="text-align: center;">表2 资产类别为信用的UPI参考数据元素取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI参考数据元素</td><td colspan="4">UPI参考数据元素值</td></tr><tr><td style='text-align: center;'>资产类别</td><td colspan="4">信用</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td><td style='text-align: center;'>期权</td><td style='text-align: center;'>远期</td><td style='text-align: center;'>其他</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>欧式、美式、百慕大等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>看涨、看跌等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>收益、定价方法或支付触发方式</td><td style='text-align: center;'>信用违约、总收益、第1次违约、第n次违约、潜在、恢复等。</td><td style='text-align: center;'>香草、回溯、其他路径依赖等。</td><td style='text-align: center;'>价差、标的资产的远期价格等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>交割方式</td><td colspan="4">现金、实物等。</td></tr><tr><td style='text-align: center;'>合约子类型</td><td colspan="4">信用风险缓释合约、信用风险缓释凭证、信用违约互换（含单名、多名、指数等）、指数份额（CDS on）。</td></tr><tr><td style='text-align: center;'>标的资产</td><td colspan="4">主权、市政、公司、贷款资产池、资产支持证券等。</td></tr><tr><td style='text-align: center;'>结算渠道</td><td colspan="4">人民币跨境支付系统（CIPS）、中国现代化支付系统（CNAPS）等。</td></tr><tr><td style='text-align: center;'>标准合约规范（如适用）</td><td colspan="4">北美公司标准、欧洲公司标准、欧洲保险公司附属标准、西欧主权标准等。</td></tr><tr><td style='text-align: center;'>标的资产编号源（如适用）</td><td colspan="4">关联的标的资产编号的发布者或来源。</td></tr></table>

<div style="text-align: center;">表2 资产类别为信用的UPI参考数据元素取值（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI 参考数据元素</td><td style='text-align: center;'>UPI 参考数据元素值</td></tr><tr><td style='text-align: center;'>标的资产编号（如适用）</td><td style='text-align: center;'>1 种识别码，可用于确定合约中标的的资产、指数。</td></tr><tr><td style='text-align: center;'>标的信用指数系列（如适用）</td><td style='text-align: center;'>例如 1、2、3、4、…。</td></tr><tr><td style='text-align: center;'>标的信用指数版本（如适用）</td><td style='text-align: center;'>例如 1、2、3、4、…。</td></tr><tr><td colspan="2">注：在本文件中，N/A 表示不适用。</td></tr></table>

资产类别为利率的UPI参考数据元素取值宜见表3。

<div style="text-align: center;">表3 资产类别为利率的UPI参考数据元素取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI参考数据元素</td><td colspan="4">UPI参考数据元素值</td></tr><tr><td style='text-align: center;'>资产类别</td><td colspan="4">利率</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换(掉期)</td><td style='text-align: center;'>期权</td><td style='text-align: center;'>远期</td><td style='text-align: center;'>其他</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>欧式、美式、百慕大等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>看涨、看跌等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>收益、定价方法或支付触发方式</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>香草、亚式、数字(二元)、障碍、二元障碍、回溯、其他的路径依赖等。</td><td style='text-align: center;'>点差交易、标的远期价格、标的名义远期利率、价差合约等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>支付频率</td><td style='text-align: center;'>定额、递增、递减、自定义等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>单一或多种货币</td><td style='text-align: center;'>单一货币、跨币种货币。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>单期限或多期限</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>交割类型</td><td colspan="3">现金、实物等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td style='text-align: center;'>标的互换、固定—浮动、固定—固定、通货膨胀、隔夜指数互换利率(OIS)、零息票息等。</td><td style='text-align: center;'>利率指数、互换(标的)、互换(固定—浮动)、互换(固定—固定)、互换(通胀)、互换(OIS)、期权、远期、期货等。</td><td style='text-align: center;'>利率指数、期权、单一标的、一揽子等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>结算渠道</td><td colspan="4">CIPS、CNAPS等。</td></tr></table>

<div style="text-align: center;">表3 资产类别为利率的UPI参考数据元素取值（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI 参考数据元素</td><td style='text-align: center;'>UPI 参考数据元素值</td></tr><tr><td style='text-align: center;'>标的资产编号源（如适用）</td><td style='text-align: center;'>关联的标的资产编号的发布者或来源。</td></tr><tr><td style='text-align: center;'>标的资产编号（如适用）</td><td style='text-align: center;'>一种识别码，可用于确定合约中标的的资产、指数。</td></tr><tr><td style='text-align: center;'>标的利率指数期限（如适用）</td><td style='text-align: center;'>日、周、月、季度、年等。</td></tr><tr><td style='text-align: center;'>标的利率指数期限乘数（如适用）</td><td style='text-align: center;'>例如 1、2、3、4、…等。</td></tr><tr><td style='text-align: center;'>与标的指数相关的货币（可用于跨货币互换）</td><td style='text-align: center;'>参考 GB/T 12406—2022 表示货币的代码。</td></tr></table>

资产类别为大宗商品的UPI参考数据元素取值宜见表4。

<div style="text-align: center;">表4 资产类别为大宗商品的UPI参考数据元素取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI参考数据元素</td><td colspan="4">UPI参考数据元素值</td></tr><tr><td style='text-align: center;'>资产类别</td><td colspan="4">大宗商品</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换(掉期)</td><td style='text-align: center;'>期权</td><td style='text-align: center;'>远期</td><td style='text-align: center;'>其他</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>欧式、美式、百慕大等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>看涨、看跌等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>收益、定价方法或支付触发方式</td><td style='text-align: center;'>价差合约、总收益、超额收益、贷款或租赁、商品实物、标的资产价值、地点基差、品质基差、日期基差等。</td><td style='text-align: center;'>香草、亚式、数字(二元)、障碍、二元障碍、回溯、其他的路径依赖、上限期权、下限期权等。</td><td style='text-align: center;'>点差交易、标的远期价格、价差合约等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>交割类型</td><td colspan="3">现金、实物、可选交割方式等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td colspan="4">能源、贵金属、非贵金属、农产品、环保、运费、聚丙烯产品、纸品、化肥、指数、多种商品、其他等。</td></tr><tr><td style='text-align: center;'>标的资产或合约的子类型</td><td colspan="4">铝、红豆、波罗的海交易所—干散货航线、波罗的海交易所—湿散货航线、大麦、纯苯、黄油、油菜籽、煤炭、钴、可可、咖啡、纸板、铜、玉米、棉花、原油、重柴油、电力、排放、乙醇和生物燃料、化肥、绒毛、燃料油、轻柴油、汽油、黄金、取暖油、铱、铁矿石、航煤和煤油、铅、牲畜、木材、甲醇、牛奶、钼、石脑油、天然气、液化天然气、报纸、镍、燕麦、橙汁、钯、棕榈油、塑料、铂、普氏轻质油轮、普氏重质游轮、纸浆、回收纸、铑、稻米、橡胶、钌、银、高粱、大豆、钢材、糖、葵花籽、锡、铀、小麦、羊毛、锌、其他。</td></tr></table>

<div style="text-align: center;">表4 资产类别为大宗商品的UPI参考数据元素取值（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI 参考数据元素</td><td style='text-align: center;'>UPI 参考数据元素值</td></tr><tr><td style='text-align: center;'>结算渠道</td><td style='text-align: center;'>CIPS、CNAPS 等。</td></tr><tr><td style='text-align: center;'>标的资产编号源(如适用)</td><td style='text-align: center;'>关联的标的资产编号的发布者或来源。</td></tr><tr><td style='text-align: center;'>标的资产编号(如适用)</td><td style='text-align: center;'>1 种识别码，可用于确定合约中标的的资产、指数。</td></tr></table>

资产类别为权益的UPI参考数据元素取值宜见表5。

<div style="text-align: center;">表5 资产类别为权益的UPI参考数据元素取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI参考数据元素</td><td colspan="4">UPI参考数据元素值</td></tr><tr><td style='text-align: center;'>资产类别</td><td colspan="4">权益</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换(掉期)</td><td style='text-align: center;'>期权</td><td style='text-align: center;'>远期</td><td style='text-align: center;'>其他</td></tr><tr><td style='text-align: center;'>期权执行类别</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>欧式、美式、百慕大等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>看涨、看跌等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>收益、定价方法或支付触发方式</td><td style='text-align: center;'>价格、股息、总收益、方差、波动性、价差合约等。</td><td style='text-align: center;'>香草、亚式、数字(二元)、障碍、二元障碍、回溯、其他的路径等。</td><td style='text-align: center;'>点差交易、标的远期价格等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>交割方式</td><td colspan="4">现金、实物、可选交割方式等。</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td style='text-align: center;'>单一标的、指数、一揽子等。</td><td style='text-align: center;'>单一标的、指数、一揽子、期权、远期合约、期货等。</td><td style='text-align: center;'>单名称、指数、一揽子、期权、期货等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>结算渠道</td><td colspan="4">CIPS、CNAPS等。</td></tr><tr><td style='text-align: center;'>标的资产编号源(如适用)</td><td colspan="4">关联的标的资产编号的发布者或来源。</td></tr><tr><td style='text-align: center;'>标的资产编号(如适用)</td><td colspan="4">1种识别码,可用于确定合约中标的的资产、指数。</td></tr></table>

资产类别为外汇交易的UPI参考数据元素取值宜见表6。

<div style="text-align: center;">表6 资产类别为外汇交易的UPI参考数据元素取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI 参考数据元素</td><td colspan="4">UPI 参考数据元素值</td></tr><tr><td style='text-align: center;'>资产类别</td><td colspan="4">外汇交易</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td><td style='text-align: center;'>期权</td><td style='text-align: center;'>远期</td><td style='text-align: center;'>其他</td></tr><tr><td style='text-align: center;'>期权执行类别</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>欧式、美式、百慕大等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>看涨、看跌等。</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>—</td></tr></table>

<div style="text-align: center;">表 6 资产类别为外汇交易的 UPI 参考数据元素取值（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>UPI参考数据元素</td><td colspan="4">UPI参考数据元素值</td></tr><tr><td style='text-align: center;'>收益、定价方法或支付触发方式</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>香草、亚式、数字（二元）、障碍、二元障碍、回溯、其他的路径等。</td><td style='text-align: center;'>价差合约、点差交易、标的远期价格等。</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>交割方式</td><td colspan="4">现金、实物、可选交割方式等。</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td style='text-align: center;'>即期—远期型、远期—远期型。</td><td style='text-align: center;'>远期、期货、现货、波动性等。</td><td style='text-align: center;'>现货、远期、期权、期货等。</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>结算渠道</td><td colspan="4">CIPS、CNAPS等。</td></tr><tr><td style='text-align: center;'>货币对</td><td colspan="4">例如GB/T 12406—2022表示货币的代码。</td></tr><tr><td style='text-align: center;'>结算货币(如适用)</td><td colspan="4">例如GB/T 12406—2022表示货币的代码。</td></tr></table>

## 7 标的资产识别码

### 7.1 标的资产识别的有关注意事项

根据UPI一一对应特征（见5.2），对使用不同识别码的同一标的的场外衍生品宜分配相同的UPI代码。1个给定UPI的参考数据元素可包含与给定标的资产相关的多个识别码，以满足UPI识别标的资产的管理要求。

对于公开可获得的价格或事件信息的资产和基准指标，当被用于计算与场外衍生品合约相关的价格、估值或支付信息时，其场外衍生品的识别码宜使市场参与者、管理部门和公众通过免费公开可用的资源查看或检索资产的价格、事件信息或者基准指标。

标的资产的识别规范见7.2。若与场外衍生品挂钩的是定制一揽子标的，则UPI参考数据元素列表可不包含定制一揽子标的的识别码。

### 7.2 关于标的资产和基准指标的识别

#### 7.2.1 交易所上市的资产

对于在交易所上市的标的资产（例如股票、期货、期权或现货商品），每一种资产的识别码可由资产所在的交易所指定，并可推断出该资产所在的交易所。对于不同交易所具有相同符号的情况，可通过后缀或其他形式予以区别，以满足该标的资产的唯一性。

#### 7.2.2 债券

如果标的资产为债券，该资产在UPI参考数据库中的识别方式必须满足管理要求，以便可查看或检索债券的发行人、资历和经济效益。

#### 7.2.3 法定实体

如果与场外衍生品挂钩的是1个法定实体（例如公司），该法定实体在UPI参考数据库中的识别方式必须满足管理要求，以便可识别该法定实体相关的场外衍生品合约的价格、估值和支付信息。

#### 7.2.4 公开交易的贷款

如果与场外衍生品挂钩的是公开交易的贷款，该资产在UPI参考数据库中的识别方式必须满足管理要求，以便可查看或检索贷款人、借款人、资历、期限和公开可用的贷款相关经济情况。

#### 7.2.5 私人贷款

如果与场外衍生品挂钩的是私人贷款，则该资产在UPI参考数据库中的识别方式必须满足管理要求。

#### 7.2.6 不在交易所交易的现货商品

如果标的资产是未在交易所交易的现货商品，该商品在UPI参考数据库中的识别方式必须满足管理要求，以便该商品的定价来源和定价来源使用的全名可按照适用于特定管理规则的方式识别。

#### 7.2.7 自然或环境事件

如果与场外衍生品挂钩的是自然事件或环境事件，该事件在 UPI 参考数据库中的识别方式必须满足管理要求，以便可识别该事件、事件的相关度量、相关地理信息或其他与相关场外衍生品合约的价格、估值和支付有关的信息。

#### 7.2.8 货币

如果标的资产是现货货币或货币对，宜符合GB/T 12406—2022的相关内容。如果GB/T 12406—2022规定的货币代码未包含特定货币，该货币的识别方式必须满足管理要求，以便可识别货币以及用于货币的定价来源。

#### 7.2.9 主权

如果场外衍生品以主权国家作为其标的，宜符合GB/T 2260—2007的相关内容。

#### 7.2.10 其他资产

如果与场外衍生品挂钩的是本文件中未涉及的资产，那么该资产在UPI参考数据库中的识别方式必须满足管理要求，以便在可行的范围内，可识别与该资产相关的场外衍生品合约的价格、估值和支付有关的信息。

#### 7.2.11 基准指标

对于作为标的的基准指标，该基准指标在UPI参考数据库中的识别方式必须满足管理要求，以便可识别基准指标的商标名称、发行商、管理员、可适用版本和系列、指定到期日或与其相关的场外衍生品合约的价格、估值和支付有关的信息。

## 8 UPI 代码的结构和格式

按照ISO 4914:2021的相关内容，UPI代码由12个字母或数字组成，具体分解如下。

a）2个字母的前缀“QZ”。

b）9个字母或数字（大写字母A至Z、0至9、不含元音字母A、E、I、O、U和字母Y），不含分隔符或特殊字符。

c）1个字母或数字的校验字符（大写字母A至Z、0至9、不含元音字母A、E、I、O、U和字母Y），可通过附录E中的方法进行计算。

## 附录 A

(规范性)

## UPI 分配过程

任一实体申请某一类场外衍生品的UPI代码时，可向UPI服务提供商提供1组相关的场外衍生品参考数据元素值，这些值形成交易工具和标的资产特征的唯一组合，并代表此类场外衍生品，分配过程如下。

a）如果已存在与该类工具和标的相关的组合特征相对应的 UPI 代码，则 UPI 服务提供商告知提出

请求的该实体已经分配给这组参考数据元素值的 UPI 代码。对标的资产的获取分 2 种情况。

——当标的资产及其标的识别码已经作为参考数据的一部分被包含在衍生品的 UPI 参考数据中，UPI 服务提供商不再补充 UPI 参考数据。

——当 1 个或多个标的资产作为参考数据元素值的一部分，其所采用的替代识别码尚未包含在给定 UPI 代码的参考数据集中，UPI 服务提供商将标的资产的新识别码添加到与此 UPI 代码有关的 UPI 参考数据中。

b）如果对于与该类工具和标的资产相关的特征组合尚不存在相对应的 UPI 代码，则 UPI 服务提供商将所接收的参考数据元素值集合纳入到 UPI 参考数据库中，并为其分配 UPI 代码。

参考数据库将由UPI服务提供商维护。UPI服务提供商确保其质量、完整性和准确性。

通过向 UPI 服务提供商提交参考数据来获取 UPI 代码的过程见图 A.1。

<div style="text-align: center;"><img src="imgs/img_in_image_box_55_219_992_1282.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 A.1 通过向 UPI 服务提供商提交参考数据来获取 UPI 代码的过程</div>


根据现有的 UPI 代码检索 UPI 参考数据的过程见图 A.2。

<div style="text-align: center;"><img src="imgs/img_in_image_box_194_252_1040_1161.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 A.2 根据现有的 UPI 代码检索 UPI 参考数据的过程</div>


## 附录 B

(资料性)

## UPI 代理模式

UPI 服务提供商履行 UPI 参考数据库的维护运营、数据质量管理、代理机构管理责任。其可在各国家及地区发展代理机构，负责受理法人机构的 UPI 代码申请、管理本地 UPI 数据、提供 UPI 代码相关服务等，申请机构可自愿选择全球任意 1 家代理机构申请 UPI 代码。

代理机构与 UPI 服务提供商建立数据交换机制，代理机构收集的相关数据要按要求同步传输至 UPI 参考数据库，发放 UPI 之前要与 UPI 参考数据库进行查重。

发码流程如图 B.1 所示，具体流程说明如下。

a）国内机构用户需要发布衍生产品时，向UPI代理机构提供参考数据元素并发起赋码申请。

b）UPI 代理机构受理申请，并通过对接国际接口查询参考数据组成的 UPI 是否存在，若存在则直接向用户反馈 UPI，若不存在则参照格式规范生成 UPI 代码，审核后反馈用户并完成数据同步。

<div style="text-align: center;"><img src="imgs/img_in_image_box_261_669_941_973.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">图 B.1 发码流程</div>


查询流程如图 B.2 所示，具体流程说明如下。

a）用户可向代理机构提出查询请求，代理机构通过与 UPI 参考数据库连接的方式，为用户提供服务。

b）查询服务主要分为以下3种类型。

——使用特定属性查询特定 UPI。

——使用代码信息查询特定 UPI。

——使用属性集查询所有符合该属性集的 UPI。

c）代理机构根据用户的要求，反馈查询结果。

<div style="text-align: center;"><img src="imgs/img_in_image_box_254_210_966_535.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 B.2 查询流程</div>


## 附录 C

(资料性)

## UPI 用户分类及权限

使用 UPI 服务的用户将按照如下规则划分。

a）专门用户：

——高级用户，拥有完整的编程访问权限，可使用程序连接方式创建、检索和下载数据。

——仅检索接口用户，拥有有限的编程访问权限，可使用程序连接方式检索数据，但被允许的数据总量低于高级用户。

——标准用户，拥有手动访问权限，可使用手动连接方式创建、检索和下载数据。

——低频用户，拥有手动访问权限，可使用手动连接方式创建、检索和下载数据，但被允许的数据总量低于高级用户。

b）非专门用户：注册用户，可使用手动连接方式检索和下载数据。

专门用户和非专门用户均可使用手动连接方式或程序连接方式通过文件下载服务下载数据。

# 附录 D

(资料性)

# 参考数据元素取值示例（按资产类别）

### D. 1 总则

按资产类别列举的参考数据元素值示例中，用于标的资产编号和标的资产编号源的值仅用于说明目的，并不意味着优先考虑用于识别标的资产。标的资产编号和标的资产编号源的允许值可能因国家或地区而不同。

### D.2 资产类别：信用

1 个信用违约互换（掉期）在 1 个具有法人实体识别编码的参考实体中可能具有的参考数据元素值示例见表 D.1。

<div style="text-align: center;">表 D.1 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>信用</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>信用违约</td></tr><tr><td style='text-align: center;'>合约子类型</td><td style='text-align: center;'>单名</td></tr><tr><td style='text-align: center;'>标的资产</td><td style='text-align: center;'>企业</td></tr><tr><td style='text-align: center;'>优先级</td><td style='text-align: center;'>高级</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>拍卖</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>全球法人识别编码（LEI）</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>5493XXXXXXXXXXXXXXX</td></tr></table>

### D.3 资产类别：利率

利率互换（掉期）可能具有的参考数据元素值示例见表D.2。

<div style="text-align: center;">表 D.2 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>利率</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>FR007</td></tr><tr><td style='text-align: center;'>票据周期</td><td style='text-align: center;'>常数</td></tr><tr><td style='text-align: center;'>单一或多种货币</td><td style='text-align: center;'>单一</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>N/A</td></tr></table>

<div style="text-align: center;">表 D.2 参考数据元素值示例（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>N/A</td></tr></table>

3个月美元的伦敦银行间同业拆借利率上限可能具有的参考数据元素值示例见表D.3。

<div style="text-align: center;">表 D.3 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>利率</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>期权</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td style='text-align: center;'>利率指数</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>欧式</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>看涨期权</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>利率上限</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>GB/T 27926—2021</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>LIBO</td></tr><tr><td style='text-align: center;'>标的利率期限乘数</td><td style='text-align: center;'>3</td></tr><tr><td style='text-align: center;'>标的利率期限</td><td style='text-align: center;'>月</td></tr><tr><td style='text-align: center;'>与标的指数相关的货币</td><td style='text-align: center;'>USD</td></tr><tr><td colspan="2">注：USD 指美元。</td></tr></table>

针对插值的 3 个月及 6 个月伦敦银行间同业拆借利率曲线的远期利率协议可能具有的参考数据元素值示例见表 D.4。

<div style="text-align: center;">表 D.4 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>利率</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>远期</td></tr><tr><td style='text-align: center;'>标的资产或合约的类型</td><td style='text-align: center;'>利率指数</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>标的远期利率×名义金额</td></tr><tr><td style='text-align: center;'>交割方</td><td style='text-align: center;'>多个</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>GB/T 27926—2021</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>LIBO</td></tr><tr><td style='text-align: center;'>标的利率1期限乘数</td><td style='text-align: center;'>3</td></tr><tr><td style='text-align: center;'>标的利率1期限</td><td style='text-align: center;'>月</td></tr><tr><td style='text-align: center;'>标的利率2期限乘数</td><td style='text-align: center;'>6</td></tr><tr><td style='text-align: center;'>标的利率2期限</td><td style='text-align: center;'>月</td></tr><tr><td style='text-align: center;'>与标的指数相关的货币</td><td style='text-align: center;'>USD</td></tr></table>

### D.4 资产类别：大宗商品

基于现金结算的黄金期货合约价格的互换（掉期）可能具有的参考数据元素值示例见表D.5。

<div style="text-align: center;">表 D.5 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>大宗商品</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>黄金</td></tr><tr><td style='text-align: center;'>标的资产子类型</td><td style='text-align: center;'>黄金期货</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>标的资产价值</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr></table>

基于现金结算的玉米期货合约的看涨期权可能具有的参考数据元素值示例见表D.6。

<div style="text-align: center;">表 D.6 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>大宗商品</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>期权</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>农产品</td></tr><tr><td style='text-align: center;'>标的资产子类型</td><td style='text-align: center;'>玉米</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>欧式</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>看涨</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>香草</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr></table>

实物交割的 3 个月期黄金远期可能具有的参考数据元素值示例见表 D.7。

<div style="text-align: center;">表 D.7 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>大宗商品</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>远期</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>贵金属</td></tr><tr><td style='text-align: center;'>标的资产子类型</td><td style='text-align: center;'>黄金</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>标的资产的远期价格</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>实物</td></tr><tr><td style='text-align: center;'>标的资产</td><td style='text-align: center;'>黄金</td></tr></table>

### D.5 资产类别：权益

基于某指数的全收益互换（掉期）可能具有的参考数据元素值示例见表D.8。

<div style="text-align: center;">表 D.8 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>权益</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>指数</td></tr><tr><td style='text-align: center;'>收益、定价方法收益触发方式</td><td style='text-align: center;'>全收益</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>某指数</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>某指数</td></tr></table>

基于现金交割的一揽子股票欧式看涨期权可能具有的参考数据元素值示例见表D.9。

<div style="text-align: center;">表 D.9 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>权益</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>期权</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>一揽子</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>欧式</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>看涨</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>香草</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr></table>

基于在某交易所上市交易的某股票的价差合约可能具有的参考数据元素值示例见表D.10。

<div style="text-align: center;">表 D.10 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>权益</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>远期</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>单名</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>价差合约</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>标的资产编号源</td><td style='text-align: center;'>某交易所</td></tr><tr><td style='text-align: center;'>标的资产编号</td><td style='text-align: center;'>某股票</td></tr></table>

### D.6 资产类别：外汇交易

基于现金交割并且实现了即期对远期互换的标准“美元/人民币（USD/CNY）”货币对外汇互换（掉期），各货币的现金交割可能具有的参考数据元素值示例见表D.11。

<div style="text-align: center;">表 D.11 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>外汇交易</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>互换（掉期）</td></tr><tr><td style='text-align: center;'>标的合约类型</td><td style='text-align: center;'>即期-远期型</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>N/A</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>货币对</td><td style='text-align: center;'>USD/CNY</td></tr></table>

基于人民币现金结算并且标的为“美元/人民币”货币对的欧式看涨期权可能具有的参考数据元素值示例见表D.12。

<div style="text-align: center;">表 D.12 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>外汇交易</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>期权</td></tr><tr><td style='text-align: center;'>标的合约类型</td><td style='text-align: center;'>N/A</td></tr><tr><td style='text-align: center;'>期权类型</td><td style='text-align: center;'>欧式</td></tr><tr><td style='text-align: center;'>期权方向</td><td style='text-align: center;'>看涨</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>N/A</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>货币对</td><td style='text-align: center;'>USD/CNY</td></tr><tr><td style='text-align: center;'>结算货币</td><td style='text-align: center;'>CNY</td></tr></table>

基于美元结算并且标的为 “美元/人民币” 货币对的无本金交割远期（NDF）可能具有的参考数据元素值示例见表 D.13。

<div style="text-align: center;">表 D.13 参考数据元素值示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考数据元素</td><td style='text-align: center;'>取值</td></tr><tr><td style='text-align: center;'>资产类别</td><td style='text-align: center;'>外汇交易</td></tr><tr><td style='text-align: center;'>工具类型</td><td style='text-align: center;'>远期</td></tr><tr><td style='text-align: center;'>标的资产类型</td><td style='text-align: center;'>N/A</td></tr><tr><td style='text-align: center;'>收益、定价方法或收益触发方式</td><td style='text-align: center;'>标的资产的远期价格</td></tr><tr><td style='text-align: center;'>交割方式</td><td style='text-align: center;'>现金</td></tr><tr><td style='text-align: center;'>货币对</td><td style='text-align: center;'>USD/CNY</td></tr><tr><td style='text-align: center;'>结算货币</td><td style='text-align: center;'>USD</td></tr></table>

## 附录 E

(规范性)

UPI 校验位计算过程

UPI 校验位计算过程按照 GB/T 17710—2008 相关规定，使用与基本代码相同的字符集（大写字母 A 至 Z、0 至 9、不含元音字母 A、E、I、O、U 和字母 Y）计算校验字符，并为字符指定以下值，UPI 校验位计算映射表见表 E.1。

<div style="text-align: center;">表 E.1 UPI 校验位计算映射表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字符</td><td style='text-align: center;'>系统中用于字母数字字符串的值</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>系统中用于字母数字字符串的值</td><td style='text-align: center;'>字符</td><td style='text-align: center;'>系统中用于字母数字字符串的值</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>B</td><td style='text-align: center;'>10</td><td style='text-align: center;'>N</td><td style='text-align: center;'>20</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>C</td><td style='text-align: center;'>11</td><td style='text-align: center;'>P</td><td style='text-align: center;'>21</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>D</td><td style='text-align: center;'>12</td><td style='text-align: center;'>Q</td><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>F</td><td style='text-align: center;'>13</td><td style='text-align: center;'>R</td><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>G</td><td style='text-align: center;'>14</td><td style='text-align: center;'>S</td><td style='text-align: center;'>24</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>H</td><td style='text-align: center;'>15</td><td style='text-align: center;'>T</td><td style='text-align: center;'>25</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6</td><td style='text-align: center;'>J</td><td style='text-align: center;'>16</td><td style='text-align: center;'>V</td><td style='text-align: center;'>26</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>7</td><td style='text-align: center;'>K</td><td style='text-align: center;'>17</td><td style='text-align: center;'>W</td><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>8</td><td style='text-align: center;'>L</td><td style='text-align: center;'>18</td><td style='text-align: center;'>X</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>9</td><td style='text-align: center;'>M</td><td style='text-align: center;'>19</td><td style='text-align: center;'>Z</td><td style='text-align: center;'>29</td></tr></table>

校验位计算过程的起始值定义为 30，其值等于字符集中的字符数。校验位的计算涉及的运算操作定义如下。

a） $ \left|\right|_{30} $  是除以 30 的余数，如果计算结果为 0，那么将用值 30 进行替换。

b） $ _{31} $  是除以 31 的余数，这个操作后余数不为 0。

示例：

如果基代码（前缀+字母数字字符）是 QZNX2JD91QC，将其转换为表 E.1 中的值如表 E.2 所示。

<div style="text-align: center;">表 E.2 UPI 校验位计算映射表示例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Q</td><td style='text-align: center;'>Z</td><td style='text-align: center;'>N</td><td style='text-align: center;'>X</td><td style='text-align: center;'>2</td><td style='text-align: center;'>J</td><td style='text-align: center;'>D</td><td style='text-align: center;'>9</td><td style='text-align: center;'>1</td><td style='text-align: center;'>Q</td><td style='text-align: center;'>C</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>29</td><td style='text-align: center;'>20</td><td style='text-align: center;'>28</td><td style='text-align: center;'>2</td><td style='text-align: center;'>16</td><td style='text-align: center;'>12</td><td style='text-align: center;'>9</td><td style='text-align: center;'>1</td><td style='text-align: center;'>22</td><td style='text-align: center;'>11</td></tr></table>

对这些值执行运算操作，校验位计算过程示意图如图 E.1 所示。为使校验位对应值与结果 17 相加后除以 30 的余数为 1，则该数值为 14，所对应的校验位字符为 “G”，完整的 UPI 代码为 QZNX2JD91QCG。

上轮运算结果 本轮运算数字


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>30（起始值）</td><td style='text-align: center;'>22（字符Q）</td><td style='text-align: center;'>30+22=52</td><td style='text-align: center;'>$ | $   $ _{30}=22 $</td><td style='text-align: center;'>$ \times $ 2=44</td><td style='text-align: center;'>$ | $   $ _{31}=13 $</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>29（字符Z）</td><td style='text-align: center;'>13+29=42</td><td style='text-align: center;'>$ | $   $ _{30}=12 $</td><td style='text-align: center;'>$ \times $ 2=24</td><td style='text-align: center;'>$ | $   $ _{31}=24 $</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>20（字符N）</td><td style='text-align: center;'>24+20=44</td><td style='text-align: center;'>$ | $   $ _{30}=14 $</td><td style='text-align: center;'>$ \times $ 2=28</td><td style='text-align: center;'>$ | $   $ _{31}=28 $</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>28（字符X）</td><td style='text-align: center;'>28+28=56</td><td style='text-align: center;'>$ | $   $ _{30}=26 $</td><td style='text-align: center;'>$ \times $ 2=52</td><td style='text-align: center;'>$ | $   $ _{31}=21 $</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>2（字符2）</td><td style='text-align: center;'>21+2=23</td><td style='text-align: center;'>$ | $   $ _{30}=23 $</td><td style='text-align: center;'>$ \times $ 2=46</td><td style='text-align: center;'>$ | $   $ _{31}=15 $</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>16（字符J）</td><td style='text-align: center;'>15+16=31</td><td style='text-align: center;'>$ | $   $ _{30}=1 $</td><td style='text-align: center;'>$ \times $ 2=2</td><td style='text-align: center;'>$ | $   $ _{31}=2 $</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>12（字符D）</td><td style='text-align: center;'>2+12=14</td><td style='text-align: center;'>$ | $   $ _{30}=14 $</td><td style='text-align: center;'>$ \times $ 2=28</td><td style='text-align: center;'>$ | $   $ _{31}=28 $</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>9（字符9）</td><td style='text-align: center;'>28+9=37</td><td style='text-align: center;'>$ | $   $ _{30}=7 $</td><td style='text-align: center;'>$ \times $ 2=14</td><td style='text-align: center;'>$ | $   $ _{31}=14 $</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>1（字符1）</td><td style='text-align: center;'>14+1=15</td><td style='text-align: center;'>$ | $   $ _{30}=15 $</td><td style='text-align: center;'>$ \times $ 2=30</td><td style='text-align: center;'>$ | $   $ _{31}=30 $</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>22（字符Q）</td><td style='text-align: center;'>30+22=52</td><td style='text-align: center;'>$ | $   $ _{30}=22 $</td><td style='text-align: center;'>$ \times $ 2=44</td><td style='text-align: center;'>$ | $   $ _{31}=13 $</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>11（字符C）</td><td style='text-align: center;'>13+11=24</td><td style='text-align: center;'>$ | $   $ _{30}=24 $</td><td style='text-align: center;'>$ \times $ 2=48</td><td style='text-align: center;'>$ | $   $ _{31}=17 $</td></tr></table>

<div style="text-align: center;">图 E.1 校验位计算过程示意图</div>


## 參 考 文 献

[1] GB/T 42495.1—2023 金融服务 全球法人识别编码 第1部分：编码说明

[2] JR/T 0249.2—2024 金融市场交易报告数据要素指南 第2部分：全球唯一交易识别码

[3] 《UPI协调技术指南》（Technical Guidance—Harmonisation of the Unique Product Identifier）