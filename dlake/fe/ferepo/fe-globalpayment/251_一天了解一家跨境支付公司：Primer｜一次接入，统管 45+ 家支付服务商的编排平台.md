# 一天了解一家跨境支付公司：Primer｜一次接入，统管 45+ 家支付服务商的编排平台

**Author:** 汇付通途
**Position:** 251
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488268&idx=1&sn=7f1d3da9bc86bfc86bdf02a5ccd2baba&chksm=c46e4b24f319c232ac8c3ec38ef7deb7a9bafa8ae2c2da9fc2685940910afaf07eef55cd7a94#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体**

2019 年注册成立，法定名称 PRIMER API LIMITED。

**🌍****全球布局**

总部位于英国伦敦，采用远程优先（Remote-first）的办公模式；团队分布在 **30+** 个国家和市场。2025 年在新加坡正式注册设立法律实体，进一步布局亚太市场。

⚠️说明：Primer 定位为支付编排平台（Payment Orchestration Platform），提供技术基础设施连接商户与多个支付服务提供商（PSP），商户资金由持牌 PSP 直接结算，Primer 专注于技术编排层。

**🛡️****合规资质**

通过 PCI-DSS Level 1、SOC 2 Type II 认证，遵循 GDPR 与 UK GDPR 数据合规要求。

**📊****基本服务能力概览**

通过单一 API 集成，支持商户自主选择和组合多个 PSP、风控工具与增值服务，主要服务于跨境电商、在线旅游、数字娱乐与票务、金融科技、出行平台等行业。

核心产品：Universal Checkout（统一收银台）、Payments API、Workflows（无代码编排引擎）、Centralized Vault（Token 管理）、Observability（数据分析看板）

支付覆盖：**100+** 支付方式、**150+** 币种、**30+** 语言

PSP 集成：支持 **45+** 个全球主流 PSP

智能路由：支持多维度智能路由与 Fallbacks 自动切换

电商平台：提供主流电商平台官方插件

主要客户行业：跨境电商（Conforama、Printify）、在线旅游（GetYourGuide、Pelago）、数字娱乐（ONE Championship）、金融科技（Zip、Banxa）、出行（Voi、Lime）

## **二、计费模式与费用说明**

**📋****定价模式**

采用商务咨询定价模式（Contact Sales），定价面向中大型客户，为非公开的定制化模式，具体费率与订阅价格以商务沟通为准。

**🧾****计费项目清单**

  * 交易处理费（基于计费事件）

  * 平台订阅费（月度/年度分级）


**⚖️****计费规则**

根据交易规模、币种、服务层级等因素定制收费规则，设有最低消费承诺机制——若实际产生的费用未达到约定的最低金额，则按最低金额计费。

**📝****费用项目补充说明**

Primer 的平台费用独立于 PSP 费用，商户需同时承担两部分费用，适合交易量较大、对接多个 PSP 的场景。

## **三、全球化能力与合规体系**

###  （一）支付网络与覆盖

**💳****国际卡收单**

通过集成 PSP 支持 Visa、Mastercard、American Express、JCB、UnionPay（银联）、Cartes Bancaires（法国本地卡组织）等卡组织，覆盖信用卡、借记卡与预付卡。

**🔗****本地支付聚合**

覆盖多种支付类型：

  * 欧洲：SEPA 即时转账、iDEAL、SOFORT

  * 亚太：Alipay、WeChat Pay、GrabPay、GCash、Touch 'n Go、KakaoPay 等

  * 北美：ACH 转账、Venmo

  * 数字钱包：Apple Pay、Google Pay、PayPal


**🔄****先买后付（BNPL）**

整合 Klarna、Affirm、Afterpay/Clearpay、Zip、Atome、Alma（法国）等 **6+** 家 BNPL 服务商。

**💱****多货币能力**

支持 **150+** 币种，提供多货币支付接受、货币转换、跨币种结算、动态货币定价（DCC）等功能。Global Accounts 产品支持多币种账户余额管理、本地支付通道和 SWIFT 转账。

⚠️说明：因场景与合作 PSP 的定义、统计范围存在差异，具体支付方式和币种覆盖以签约时点及合同清单为准。

### （二）合规与安全体系

**🛡️****安全认证**

  * PCI-DSS Level 1：通过年度现场审核（QSA）

  * SOC 2 Type II：通过独立第三方审计，覆盖安全性、可用性等核心维度


**🔒****数据保护**

  * 传输层：TLS 加密、强制 HTTPS 传输、3DS 2.0 支持

  * 静态数据：敏感支付数据加密存储

  * 访问控制：API 密钥安全存储与定期更换、强制启用多因素认证（MFA）

  * 数据处理：遵循 GDPR 与 UK GDPR，提供标准数据处理协议，支持 EU 标准合同条款（SCCs）进行跨境数据传输


**⚖️****反欺诈与合规义务**

服务条款明确商户反洗钱与反恐融资义务，Primer 保留因欺诈、信用或重大风险暂停或终止服务的权限。

## **四、技术架构与开发者工具**

**⚙️****API 架构**

采用 RESTful API 设计，通过 HTTP Header（X-Api-Version）进行版本控制。

**🧪****沙盒环境**

提供独立测试 API 端点（api.sandbox.primer.io）与 Primer Sandbox Processor，支持 3D Secure、Fallbacks、欺诈检测、网络令牌化等场景测试，无交易费用。

**🔑****API 认证**

采用 API Key 认证（X-Api-Key header），提供 9 类权限范围。

**🔧****SDK 支持**

提供 4 个主要平台客户端 SDK：Web（JavaScript/TypeScript）、iOS（Swift）、Android（Kotlin）、React Native，以及 Stripe、Klarna、3D Secure 等专用集成 SDK。服务器端通过 REST API 直接对接。

**🔔****Webhook 事件系统**

支持支付、退款、争议等事件的实时通知，提供签名验证机制（signing secret），确保通知来源可信，失败后自动重试，最多 5 次，每次间隔逐步延长，可通过 Dashboard 测试。

**📚****开发者文档**

文档结构完整，涵盖 Get Started、API Reference、SDK Reference、Connections、Changelogs、Testing 等模块，无需注册即可公开访问，提供 cURL、JavaScript、TypeScript 代码示例。

## **五、集成能力与支付管理**

###  （一）PSP 集成

已上线 **45+** 个 PSP 对接方案，包含 Stripe、Adyen、Braintree、Checkout.com、Worldpay、PayPal、J.P. Morgan Payments、Airwallex、Xendit、Mollie、Worldline 等。

PSP 连接方式：Dashboard 配置 → 授权 Primer 访问 PSP 账户 → 选择支付方式 → 无需编码即可启用新 PSP。

### （二）智能路由与 Fallbacks

**🔄****Workflows 工作流引擎**

可视化拖拽式规则编辑器，支持无代码配置"if-then-else"条件逻辑，非技术团队可独立管理支付路由策略、风控规则、A/B 测试等。

**📍****智能路由策略**

支持地理位置路由、成本优化路由、成功率路由、货币路由、BIN 路由（基于银行识别码）、交易金额路由、负载均衡等多维度路由策略。

**🔄****Fallbacks 功能**

主 PSP 交易失败时自动切换备用 PSP，软拒绝（Soft Decline，即可重试的临时性拒绝）自动重试，将各 PSP 不同格式的拒绝原因代码统一映射为标准分类，Fallback 重试时可复用原有 3DS 认证结果，无需客户重新验证。

### （三）电商平台与收银台

**🛒****电商平台插件**

提供 Shopify、WooCommerce、Magento、BigCommerce、Wix、Squarespace 官方插件，支持保存支付方式、一键支付、分期与订阅等能力开关。

**💳****Universal Checkout（统一收银台）**

支持 Drop-in 托管式、Headless 嵌入式、组件化模块、Payment Links 四种集成形式，具备动态展示可用支付方式、自适应屏幕设计（响应式）、品牌定制等能力，支持多语言与多货币。商户可通过 A/B 测试持续优化结账流程。

### （四）业务系统联动

**🔄****Workflow Apps 生态**

支持 Primer 原生应用与第三方应用集成，覆盖：

  * 会计系统：Xero、QuickBooks、FreshBooks

  * 通讯工具：Slack、Twilio、SendGrid、Zendesk

  * 风控服务商、物流与队列服务（Shippo、Amazon SQS）等




### （五）统一对账与结算报告

提供跨 PSP 统一结算报告产品，将不同 PSP 的结算数据（支付、退款、拒付、费用拆分等）归集为统一格式输出，目前支持 Adyen、Stripe、PayPal、Klarna、Monext 等处理器的结算报告接入，覆盖范围持续扩展。

报告能力：按 PSP、商户账户、结算币种分别自动生成对账批次；支持 Dashboard 在线查看与 CSV/SFTP 导出；对交换费、处理费等各项费用逐笔明细拆分，便于核对 PSP 实际扣费是否与协议一致。

💡应用场景：如果您同时对接 3 个以上 PSP，每家的结算报告格式、时间周期和费用拆分方式各不相同，统一结算报告可将多源数据归集到同一格式中，减少财务团队手工整理和跨系统比对的工作量。

## **六、风控、数据分析与智能工具**

###  （一）风控能力

**🛡️****内置风控引擎**

覆盖机器学习模型、规则引擎、实时风险评分、设备指纹、行为分析等多维度风险识别能力，并支持 AVS 地址验证与 CVV 校验。检查节点包括授权前、授权后与人工审核三个时机，商户可自定义风险阈值、触发条件等风控策略。

**🔗****第三方风控集成**

预集成 Forter、Riskified、Syft、Signifyd 等风控服务商，商户可在 Workflows 中灵活配置风控策略组合。

**🔐****3D Secure 认证**

支持 3DS 1.0 与 3DS 2.0，提供 Adaptive 3DS（ML 优化触发策略）、免打扰验证（基于风险等级自动判断是否需要额外验证）、生物识别（指纹/FaceID），遵循 PSD2 强客户认证（SCA）要求。

### （二）数据分析与监控

**📊****分析看板**

提供 **100+** 可视化图表、**25+** 筛选维度、实时数据更新，覆盖 Snapshot、Payments、Sales、Refunds、3D Secure、Declines、Network Tokenization、Sales Recovery 等主题看板，支持完整的交易流程追踪与失败原因分析。

**⚠️****告警与监控**

支持自定义阈值告警、ML 异常检测，通过 Slack、PagerDuty、Email、Webhook 等多渠道通知。

**📤****数据导出**

提供数据导出接口（External Payment Insight API）与 ETL 数据同步功能，支持第三方 BI 工具集成与报表导出。

### （三）AI 能力

**🤖****Primer Companion**

面向支付场景的 AI 助手，可调用每笔交易 400 多个数据点进行分析并给出优化建议。

**📈****UpliftAI**

基于机器学习优化授权率，自动分析交易失败原因并选择最佳重试时间，支持 A/B 测试验证策略效果。

### （四）Token 管理与网络令牌化

提供跨 PSP 通用的 Token 化服务，支持网络 Token（Network Tokenization）自动配置、CVV 重新捕获、自动卡过期更新、跨 PSP 重试无需重新认证。网络 Token 化在典型场景下可降低欺诈风险、提升授权率。

## **七、适用场景与选型建议**

###  （一）适合使用 Primer 的场景

**🔄****多 PSP 管理需求**

如果您的业务已对接或计划对接多个 PSP（如 Stripe + Adyen + 本地 PSP），需要统一管理交易路由与数据分析，Primer 提供单一 API 集成与 Workflows 工具，可降低多 PSP 管理的技术复杂度和开发成本。

**🌏****跨境电商与多区域拓展**

如果您的业务覆盖欧洲、亚太、北美等多个区域，需要接入各区域本地支付方式（如 SEPA、Alipay、GrabPay、ACH 等），通过智能路由实现本地收单优化。

**📈****支付成功率优化**

如果您面临较高的支付失败率，Primer 提供 Fallbacks、Adaptive 3DS 与 UpliftAI 等工具，支持自动重试与智能路由优化支付成功率。

**👨‍💼****无代码支付运营**

如果运营团队希望在无需开发资源的情况下独立调整路由规则、风控阈值、A/B 测试等支付策略，Workflows 提供了可视化操作界面。

**🔄****SaaS 与订阅业务**

如果您运营订阅制或周期性收费业务，需要定期自动扣款（MITs）、失败重试与催缴策略，Primer 支持订阅场景下的 Fallback 与智能重试优化。

### （二）决策建议

在选择支付编排平台时，建议从以下维度进行综合评估：

**📊****业务规模与经济性**

编排平台适合年交易量较大、已对接或计划对接多个 PSP 的中大型商户。如果您处于业务起步阶段或仅使用单一 PSP，可先评估直接对接 PSP 的方案（如 Stripe、Adyen、PayPal 等），待业务规模与复杂度增长后再考虑编排层。Primer 推出 Primer for Growth 计划，面向初创与成长期企业提供限时免费试用计划，符合条件的企业可获得一年免费使用 Observability 与 Monitors 工具的权限（名额有限，需申请审核），感兴趣的企业可关注该计划的适用条件与申请流程。

**🌍****区域覆盖匹配度**

根据公司公开信息，Primer 在欧洲和亚太市场的本地支付覆盖较为深入，如果您的业务主要集中在拉美、中东或非洲，可同时了解 dLocal、CellPoint Digital 等在这些区域覆盖更广的方案。

**🔧****技术实施能力**

Primer 提供无代码 Workflows 与电商平台插件，旨在降低技术门槛。如果技术团队有能力直接管理多 PSP 集成，也可评估自建编排层的可行性与长期成本。

**💰****费用与合同条款**

在签约前，建议明确计费事件定义、最低承诺额、费率变更条款、服务边界等关键内容，与多家方案进行对比评估。

### 📌 重要提示与数据说明

**⚠ 跨境支付涉及外汇管制、区域合规及技术风险** ，企业决策前请以官方信息为准并咨询专业机构；

**⏰时效** ：本文信息截至2026年2月，含行业分析及公开数据整理，可能存在时效差异；

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

