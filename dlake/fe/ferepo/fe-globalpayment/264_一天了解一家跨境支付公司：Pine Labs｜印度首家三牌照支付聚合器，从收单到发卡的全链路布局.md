# 一天了解一家跨境支付公司：Pine Labs｜印度首家三牌照支付聚合器，从收单到发卡的全链路布局

**Author:** 汇付通途
**Position:** 264
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488396&idx=1&sn=1afb8333980bde08f279fe919f8bb2d0&chksm=c46e4ba4f319c2b2ef67bc2991f20c158f4ac676521726f8041c5fb89fdb84f60efd16eeceab#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体**

1998年成立，注册地位于印度哈里亚纳邦古尔冈（Gurugram），总部位于印度北方邦诺伊达（Noida）；2025年在BSE（孟买证券交易所）和NSE（国家证券交易所）上市。

**🌍****全球布局**

在印度设有多个办公室（Noida、Gurugram、Bangalore、Chennai、Mumbai），海外在马来西亚（吉隆坡）、新加坡、阿联酋、澳大利亚、美国、非洲等地设有运营实体，覆盖约20个市场。

**🛡️****合规资质**

\- 支付牌照：持有印度央行（RBI）全部三类支付聚合器牌照——PA-Online（在线支付聚合）、PA-Physical（线下支付聚合）、PA-Cross Border（跨境支付聚合），为印度首家同时持有三类牌照的机构

\- 安全认证：PCI DSS Level 1、PCI-S3F、PCI-PIN、UKPT/TLE（终端线路加密）、ISO 27001

\- 卡组织认证：Visa、Mastercard、American Express三方认证POS终端（截至发稿为印度唯一）

\- PCI SSC（支付卡行业安全标准委员会）参与组织成员

**📊****业务覆盖**

支持Visa、Mastercard、American Express、Diners Club、RuPay五大卡组织，覆盖100+支付模式，支持40+种收单货币。服务对象涵盖商户、银行、品牌和金融机构。

核心产品线包括Plutus Smart POS（Android POS终端）、Plural（在线支付网关）、Qwikcilver/Woohoo（预付卡与礼品卡）、Credit+（信用卡发行与处理）、Setu（金融科技基础设施API）等。

主要合作伙伴：OpenAI、SBI Payments、Visa、Mastercard、Emirates NBD、Wio Bank

## **二、服务项目与计费模式**

###  服务项目清单

**💳****POS支付服务（线下）**

采用SaaS软件服务费模式，包含设备设置费、月租或年度套餐费用。POS渠道的MDR（商户折扣率）由银行与商户协商确定，Pine Labs在此基础上另行收取软件服务费。

**🌐****在线支付网关（Plural）**

覆盖卡收单、UPI、银行转账、钱包、BNPL与分期等在线支付方式，并支持DCC（动态货币转换）。

**📱****分期与消费金融服务**

覆盖信用卡EMI、借记卡EMI、无卡EMI等多种分期形态。

**🎁****预付卡与礼品卡发行及处理**

通过Qwikcilver/Woohoo平台提供预付卡与礼品卡的发行、处理与分销服务。

**✨****增值服务**

包含对外付款（Payouts）、分账结算（Split Settlements）、支付链接（Payment Links）、订阅管理（Subscription）、Setu金融基础设施API。

### 计费规则

采用非公开定价，根据交易量、行业类型、结算速度选择、支付方式等因素分层定制，需联系销售团队获取报价；Pine Labs的收费逻辑与传统统一MDR模式不同，采用向商户、银行和品牌三方分别收取不同类型费用的模式。

**📌****小结：** 本章聚焦收费项目与适用规则，不含数值，最终以《商户协议》为准。

## **三、支付网络与合规体系**

###  （一）支付网络与区域布局

**🇮🇳****印度市场（核心）**

覆盖100+支付模式，涵盖五大卡组织卡收单、UPI全套、银行转账（IMPS/NEFT/Net Banking）、在线钱包、BNPL与分期、预付卡与礼品卡、NFC非接触支付等。

**🌏****东南亚**

通过子公司Pine Payment Solutions Sdn. Bhd.在马来西亚提供本地POS收单；与Visa合作在新加坡、马来西亚、菲律宾推出Visa Instalment Solutions（VIS）分期方案；与IOUPay合作在马来西亚提供myIOU BNPL服务。

**🇦🇪****阿联酋与中东**

与Emirates NBD合作提供商户收单，与Wio Bank合作部署Credit+收单处理平台。

**🇺🇸****北美**

通过Pine Labs US（Qwikcilver Solutions Inc.）运营品牌支付与礼品卡业务。

**🔄****跨境收单**

Plural在线支付网关支持DCC（动态货币转换），接受多种货币的外卡在印度商户支付，收取汇率加点（具体费率在商户入驻时确定）。持有RBI PA-Cross Border牌照，允许处理跨境交易。

**⚠️****说明：** 国际市场（马来西亚、阿联酋、美国等）的运营基于当地银行合作伙伴关系或特定合规安排，具体合规细节以签约时的官方文件为准。

### （二）合规与安全体系

**🔒****数据安全**

采用端到端加密（E2EE），通过HSM（硬件安全模块）生成一次性动态密钥，加密PIN和卡信息，并实施RBI合规的卡号加密替换（Token化）方案。

**🇮🇳****数据本地化**

符合RBI 2018年数据本地化指令，所有支付数据存储在印度境内。

**🛡️****反洗钱与KYC**

遵循印度《反洗钱法》（PMLA 2002）和RBI KYC主指令，每日比对UNSC/UAPA等制裁名单，交易记录保存至少10年，具备AI欺诈预防系统（专利技术）。

**📈****系统可用性**

IPO文件披露支付处理系统和预付发行系统均保持极高的正常运行时间。Setu平台运行在AWS上，在AWS亚太区域建立灾备站点。

## **四、技术架构与开发者工具**

###  （一）开发者工具

**🔧****API架构**

采用RESTful API，支持OAuth 2.0认证机制，数据格式为JSON；API覆盖订单、支付、退款、结算、订阅等支付全流程。

**📦****SDK与插件**

提供Node.js SDK、Android/iOS/React Native移动端SDK、POS集成SDK（Android/Desktop）。后端语言SDK目前覆盖Node.js，Python、Java、PHP、Go等语言可通过RESTful API直接对接。

**📚****开发者文档**

基于ReadMe.io平台构建，提供从入门指南到API接口文档的完整技术文档，包含收银台集成指南、SDK指南、Webhook文档、错误码等，文档公开无需注册。

**🔔****Webhook**

支持HMAC-SHA256签名验证、重试机制、IP白名单配置。

**🧪****测试环境**

提供独立UAT沙盒环境和测试卡号，POS SDK提供模拟器应用（Simulator App）。

**🚀****创新工具**

2025年8月推出MCP Server（面向AI Agent的支付集成标准化工具）和Agent Enablement Toolkit；2026年2月与OpenAI合作构建"Agentic Commerce"，将AI能力集成至支付与对账流程。

### （二）支付与结算效率

**🛒****收银台集成模式**

提供4种模式：标准收银页面（Hosted Checkout，无需PCI）、iFrame嵌入（无需PCI）、Infinity Checkout（高级可定制，部分PCI）、全自定义API（Seamless Checkout，需PCI合规）。

**⏱️****到账时效**

Plural在线支付：标准结算T+1（所有支付方式均支持），即时结算T+0（约15分钟，银行节假日亦可处理，有额外费用）。POS线下：标准结算T+2～T+4。

**💳****核心支付功能**

支持单次支付、预授权与延迟捕获、全额退款与部分退款、Token化支付（免CVV）、Native OTP认证、Apple Pay、订阅与周期性扣款。

**🛡️****风控引擎**

具备AI欺诈预防、FRM引擎（跨境支付风控）、3D Secure支持、IMEI验证（EMI购买设备锁定与解锁）、每笔POS交易的地理定位记录。

## **五、核心产品与行业方案**

###  （一）Affordability Suite（消费分期方案）

Pine Labs在印度分期与消费金融领域具备较完整的产品矩阵：

  * 信用卡EMI、借记卡EMI、首付EMI、无卡EMI（Cardless EMI，手机号验证）

  * Brand EMI（品牌补贴分期）、Pay by Points（积分支付）

  * Visa Instalment Solutions（VIS，覆盖新加坡、马来西亚、菲律宾）

  * IMEI验证（EMI购买的设备验证、锁定与解锁）




**💡****应用场景：** 如果您在印度市场销售高客单价商品（如电子产品、家电），消费者可以在POS终端或在线渠道选择信用卡或借记卡分期付款，或通过手机号验证使用无卡分期。品牌方可以通过Brand EMI补贴分期利息，降低消费者的一次性付款压力。

### （二）预付卡与礼品卡发行（Qwikcilver/Woohoo）

通过IAP平台运营，覆盖16个国家（印度、东南亚、阿联酋、澳大利亚等）。根据Redseer报告，按交易价值计为印度最大的闭环和半闭环礼品卡发行商，Amazon Pay的后台技术提供商。

### （三）信用卡发行与处理（Credit+）

2023年推出Credit+，提供从发卡到处理的完整技术方案，面向银行和金融机构提供信用卡发行与处理后台技术。

### （四）稳定币预付卡

2026年3月宣布将在中东、非洲和东南亚的9个国家推出稳定币支持的预付卡，消费者可通过数字钱包中的稳定币充值，在POS端实时转换为当地货币完成支付。该产品不在印度和中国市场推出。

### （五）Setu金融基础设施平台

Setu by Pine Labs提供印度数字公共基础设施API：

  * BBPS BOU/COU：账单收款与贷款还款API，连接1000+银行，月均处理1000万笔交易

  * Account Aggregator Gateway：经用户授权的金融数据共享API（RBI框架），日均500万请求

  * eKYC/Aadhaar eSign：身份验证与电子文档签名

  * UPISetu：与Axis Bank合作的UPI全功能API平台




### （六）接入方式与服务支持

**🛍️****电商插件**

Shopify、WooCommerce、Magento、OpenCart均提供官方插件，支持保存支付方式、一键支付、分期与订阅等能力。

**🔗****无代码工具**

支付链接支持通过邮件、SMS、WhatsApp分享链接收款，可通过商户后台直接创建，无需技术开发。

**📞****客户支持渠道**

支持电话、邮件、WhatsApp、在线表单、Pine Labs One App内置工单等渠道。

**📝****商户入驻**

POS商户：销售团队联系→门店拜访→设备安装与员工培训→发放入驻资料包后正式上线。Plural在线支付：自助注册（商户后台注册→提交KYC文档→审核→获取API密钥）。

### （七）行业解决方案

Pine Labs针对不同行业提供适配方案：

  * 电商与D2C：Plural在线支付网关 + Affordability Suite（EMI + 返现）

  * 教育（EdTech）：学费收取、流程管理、工作流自动化

  * 石油与燃料：POS终端 + XTRAPOWER忠诚度平台（已签约IOCL/BPCL/HPCL，部署13万台设备）

  * 银行与金融机构：IAP发卡平台 + Credit+ + Setu（AA/BBPS/eKYC）

  * 快餐与零售：POS终端 + EMI分期（McDonald's、Starbucks、Titan、LG等客户）

  * SaaS与订阅：Plural订阅管理，支持自动扣款与订阅生命周期管理




## **六、适配场景分析**

###  适合关注Pine Labs的场景

  * **🇮🇳****印度市场线下零售收单** ：如果您的业务涉及印度线下零售场景（如品牌门店、连锁餐饮、加油站），Pine Labs提供覆盖约100万家商户的POS终端网络和POS Hub集中管理平台。

  * **🌐****印度市场在线收单** ：如果您需要在印度市场接入在线支付，Plural支付网关覆盖100+支付模式，提供多种收银台集成模式。

  * **💳****印度市场分期与消费金融** ：如果您面向印度消费者销售高客单价商品，Affordability Suite提供多种分期方案。

  * **🎁****品牌礼品卡与预付卡发行** ：如果您需要在印度及东南亚、中东等市场发行品牌礼品卡或预付卡，Qwikcilver/Woohoo平台覆盖16个国家。

  * **🏦****银行与金融机构技术合作** ：如果您是银行或金融机构，Setu和Credit+平台提供信用卡发行处理、账户聚合、账单支付、eKYC等基础设施API。




### 决策建议

在评估Pine Labs时，建议从以下维度综合考量：

  * **业务市场匹配度** ：Pine Labs的服务能力集中在印度市场。如果您的业务以印度市场收单为核心需求（线下POS或在线支付），Pine Labs具备较完整的产品覆盖。如果您的核心市场在欧美、拉美或中国出海场景，可同时了解Stripe、Adyen、Razorpay等方案。

  * **线上与线下需求** ：如果您同时需要线下POS和线上支付网关，Pine Labs可通过统一平台覆盖两端。如果仅需在线支付网关，可对比Razorpay、PayU India等印度本地方案。

  * **国际化需求** ：Pine Labs的国际业务覆盖马来西亚、阿联酋、新加坡等市场，但不覆盖欧洲、拉美和中国。如果您需要全球多市场覆盖，建议同时评估其他全球化PSP方案。

  * **定价透明度** ：Pine Labs采用非公开的定制化定价模式，所有费率需联系销售团队获取。在签约前，建议明确SaaS软件服务费、MDR费率分成方案、设备费用、结算附加费、增值服务费等全部计费项目，并与多家服务商对比。

  * **技术集成能力** ：Plural提供多种收银台集成模式、完整的开发者文档和SDK支持。评估您的技术团队能力与集成偏好后再做选择。




### 📌 重要提示与数据说明

**⚠ 跨境支付涉及外汇管制、区域合规及技术风险** ，企业决策前请以官方信息为准并咨询专业机构；

**⏰时效** ：本文信息截至2026年3月，含行业分析及公开数据整理，可能存在时效差异；

**🔍 来源** ：企业官网、监管机构公示平台、行业媒体及行业报告（部分数据经脱敏处理）；

**❌ 声明** ：本文内容仅供参考，不构成任何业务建议，具体信息请以企业官方披露为准。

下期公司征集

您希望解读哪家跨境支付公司？评论区留言，我们将优先呈现！

## 已更新文章合集

  * [一天了解一家跨境支付公司（已更新100+）](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk2NDcyNzExMQ==&action=getalbum&album_id=3948756631097098244#wechat_redirect>)

  * [业务解读与增长逻辑](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk2NDcyNzExMQ==&action=getalbum&album_id=4117151022823161865#wechat_redirect>)

  * [横向对比与场景选择](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk2NDcyNzExMQ==&action=getalbum&album_id=4117624468795473921#wechat_redirect>)

  * [核心功能与技术解读](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk2NDcyNzExMQ==&action=getalbum&album_id=4110118796935741444#wechat_redirect>)

  * [实用工具与避坑指南](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk2NDcyNzExMQ==&action=getalbum&album_id=4120426311749648385#wechat_redirect>)




**微信号 :bj_xtech****👈添加好友**

**欢迎交流、资源对接**

