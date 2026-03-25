# 一天了解一家跨境支付公司：HyperPay｜专注中东北非的本地化支付网关与商户服务平台

**Author:** 汇付通途
**Position:** 259
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488339&idx=1&sn=29a3c4950f2efe26f9952a2c09935654&chksm=c46e4b7bf319c26d82d3fd502069d65fce98a1e34ebc9b48529d50e3565eead0c5f6425ce35b#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体**

2010 年以 Gate2Pay 名义在约旦安曼创立，2014 年以 HyperPay 品牌在沙特阿拉伯正式推出商业运营，总部设于利雅得。

**🌍****全球布局**

曾在约旦安曼、阿联酋迪拜设有办公室，员工分布于亚洲、欧洲、非洲、中东等区域。

**🛡️****合规资质**

  * 金融牌照：沙特央行（SAMA）电子钱包运营牌照

  * 安全认证：PCI DSS Level 1、ISO 27001、ISO 27701


**📊****业务覆盖**

服务市场包括沙特阿拉伯、阿联酋、约旦、阿曼、卡塔尔、伊拉克、黎巴嫩、巴林共 **8 个 MENA（中东北非）市场** 。

**🎯****主要应用场景**

主要面向 MENA 地区的电商零售、酒店旅游、政府与公共部门、航空电信等行业。

**📋****基本服务能力概览**

支付方式：支持 Visa、Mastercard、mada 等 5 个卡组织，以及 Apple Pay、STC Pay、PayPal 等数字钱包，SADAD、SARIE 等本地支付方式，Tabby、Tamara 等 BNPL 服务

产品线：Payments（收款网关）、HyperBill（发票、周期计费）、HyperSplit（出金、分账）、HyperSight（数据分析）、HyperTap（手机 POS）、Hyper Hospitality（酒店行业方案）、Protect（反欺诈引擎）

到账时效：支持 T+1 结算，具体到账时间取决于支付方式、收单行和商户协议

**💰****计费规则**

采用协商制定价，具体取决于商户所在市场、交易量、风险等级、收单行协议等因素，可能包含网关服务费、设置费及各产品线独立服务费用，最终以《商户协议》为准。

## **二、支付网络与合规体系**

###  （一）支付网络与区域布局

**💳****卡支付**

支持 Visa、Mastercard、American Express、mada、银联共 5 个卡组织，覆盖信用卡与借记卡。mada 支持包括预授权、3D Secure、卡号令牌化（Token 化）；已集成银联在线支付（UPOP），为中国消费者在 MENA 地区的跨境支付提供通道。

**📱****数字钱包**

支持 Apple Pay、STC Pay（沙特主要数字钱包）、PayPal。

**🏦****本地支付**

  * 沙特：mada（本地借记卡网络，同时作为卡组织运营）、SADAD（账单支付）、SARIE（即时银行转账）


**🔄****BNPL（先买后付）**

支持 Tabby 和 Tamara，覆盖沙特、阿联酋及 GCC 地区。

**🔗****本地收单网络**

与 MENA 地区多家收单行建立合作，提供智能路由（smart routing）能力，商户可通过多个收单机构处理在线支付；已与 Capital Bank（约旦）、ANB（沙特）等收单行签署合作协议；也为 GOSI（沙特社保机构）等政府机构提供支付服务。

### （二）合规与安全体系

**📜****牌照与认证**

持有 SAMA 电子钱包运营牌照，为 SAMA 授权的第 27 家支付服务提供商。2026 年获得 SAMA 国家支付网关（NPG）认证，符合沙特国家支付法规和技术标准，支持接入国家支付基础设施处理境内及跨境交易。通过 PCI DSS Level 1（支付卡行业最高安全级别）、ISO 27001（信息安全管理）、ISO 27701（隐私信息管理）认证。

**🔒****数据保护**

隐私政策以沙特个人数据保护法（PDPL）为主要适用法律，已任命数据保护官（DPO），数据保护主管机构为沙特数据与人工智能管理局（SDAIA）。SAMA 要求沙特支付数据在境内本地化存储。

**🛡️****反欺诈能力**

Protect 产品提供机器学习驱动的实时欺诈检测、规则引擎、黑名单管理（地区/IP/卡号）、预测分析等能力，支持 3D Secure 验证。2025 年与 Mozn 签署反欺诈合作协议，接入 Focal 平台。

## **三、技术能力与平台集成**

###  （一）接入方式与开发者工具

**⚙️****技术基础**

支付引擎基于 ACI Worldwide 的 OPPWA 平台构建，API 端点使用 oppwa.com 域名。ACI Worldwide 为全球性支付技术提供商，OPPWA 平台具备成熟的支付处理能力和安全标准。

**🔧****API 与集成方式**

提供 RESTful API，支持 5 种集成方式：

  * COPYandPay：JavaScript 支付组件，敏感数据由用户浏览器直接传输至支付平台，商户无需完整 PCI 合规

  * Server-to-Server：服务端直连 API，适用于需要完全自主定制支付流程的商户

  * Mobile SDK：Android（AAR）和 iOS（Framework）原生 SDK，支持主要卡组织和本地支付方式

  * HyperSplit API：出金、分账独立 API

  * HyperBill API：发票系统独立 API


**🧪****测试环境**

提供测试环境，支持测试模式与生产模式切换，使用 Token 密钥认证。

### （二）电商平台插件

提供多个电商平台的支付插件：Magento 2/1、WooCommerce（WordPress）、PrestaShop、OpenCart。

**💡****应用场景：** 如果您在 MENA 市场运营 Magento 或 WooCommerce 独立站，可通过官方插件接入 HyperPay 网关，支持 mada、Apple Pay、STC Pay 等本地支付方式，降低技术集成门槛。

## **四、产品矩阵与行业方案**

###  （一）酒店行业方案（Hyper Hospitality）

面向酒店行业的支付解决方案，通过 Oracle Hospitality OPERA 认证集成（Oracle Validated Integration），支持跨境收款、预订管理、减少客人预订后未入住（no-show）的情况、自动化支付收取等功能。

2024 年 Mastercard 以白标形式采用 Hyper Hospitality 方案，首次国际部署计划于新加坡。2024 年成功集成 250 家酒店。

### （二）出金与分账（HyperSplit）

提供基于 API 的出金与分账服务，支持商户向受益人银行账户转账，支持 24 小时内到账。适用于电商平台、众筹平台、票务平台、外卖、出行服务等需要多方分账的场景。

### （三）电子发票与周期计费（HyperBill）

提供发票生成与周期性自动扣款服务，支持通过 SMS、邮件、WhatsApp 分享支付链接，兼具一次性和周期性计费能力，无需技术开发即可使用。

### （四）手机 POS（HyperTap）

2025 年在阿联酋推出，将 Android NFC 手机转为非接触式 POS 终端，支持 EMV 非接触卡（含 Apple Pay）和 mada 卡，无需额外硬件设备。

### （五）数据分析（HyperSight）

独立的数据分析产品，提供实时交易监控、交易拒绝原因分析、收入报告和自定义数据报告。商户控制面板（BIP）提供 iOS 和 Android 移动端 App，支持随时查看交易详情和分析报告。

### （六）商业卡发行（规划中）

2025 年与 Mastercard 签署合作备忘录（MOU），计划面向沙特、阿联酋、卡塔尔的中小企业发行商业卡，尚处于协议阶段。

## **五、适配场景分析**

###  适合使用 HyperPay 的场景

**🛒****进入沙特市场的电商企业**

如果您计划在沙特阿拉伯开展电商业务，需要接入沙特本地支付方式，HyperPay 作为持有 SAMA 牌照的本地 PSP，提供 mada 本地收单和多家收单行智能路由能力。

**🏨****MENA 地区酒店与旅游企业**

如果您在中东经营酒店或旅游业务，Hyper Hospitality 方案提供与 Oracle OPERA 酒店管理系统的认证集成，支持预订管理和自动化支付收取。

**🏪****MENA 市场平台型商户**

如果您运营需要多方分账的平台（如电商市场、票务、外卖等），HyperSplit 提供基于 API 的出金与分账服务。

**📱****需要无硬件线下收款的小微商户**

如果您在沙特或阿联酋有线下收款需求，HyperTap 支持手机非接触式收款，无需额外硬件。

### 决策建议

在选择 MENA 地区支付服务商时，建议从以下维度进行综合评估：

**🎯****目标市场匹配度**

HyperPay 的支付方式覆盖和牌照资质集中于 MENA 地区，尤其是沙特市场。如果您的业务主要面向中东，可将 HyperPay 纳入评估范围；如果同时覆盖欧美或亚太市场，建议同时了解 Checkout.com、Adyen、Tap Payments 等具备更广泛地理覆盖的方案。

**🏢****商业模式适配度**

HyperPay 采用支付网关（Gateway）模式，商户需通过 HyperPay 推荐至收单行开设商户账户，入驻周期取决于所在市场和收单行审批流程。如果您倾向于聚合模式（即时开户），需对比评估不同模式的入驻流程与业务节奏的匹配度。

**🔧****技术集成能力**

HyperPay 提供电商平台插件（Magento、WooCommerce 等）和移动端 SDK。如果您的团队需要深度 API 集成，需评估直接调用 RESTful API 的技术成本。

**💰****费用与合同条款**

HyperPay 采用协商制定价，建议在签约前与 HyperPay 确认完整费用结构，并与多家 MENA 市场 PSP（如 PayTabs、Moyasar、Tap Payments 等）进行费用对比。

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

