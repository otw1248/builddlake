# 一天了解一家跨境支付公司：Cashfree Payments｜印度本地支付与跨境收付款服务商

**Author:** 汇付通途
**Position:** 261
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488367&idx=1&sn=0833b226be5c7722621f709f4f98a303&chksm=c46e4b47f319c25170c1ce44c5dfb4bfcec59eb9f40d98197bed2ecca82d2528b59897a23a8d#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体：**

2015 年成立，法定名称为 Cashfree Payments India Private Limited，注册于印度卡纳塔克邦，总部位于班加罗尔（Bengaluru）；公司最初以 Pasfar Technologies Private Limited 注册，后更名为 Cashfree Private Limited，2018 年变更为现名。

**🌍****全球布局：**

班加罗尔为全球总部。2021 年通过股权投资收购 Telr 多数股权，Telr 为 UAE 和沙特阿拉伯的支付服务商，通过 Telr 运营 MENA 业务；美国设有关联实体 Cashfree Inc。

**🛡️****合规资质：**

  * 金融牌照：印度储备银行（RBI）支付聚合器（PA-PG）牌照；RBI 跨境支付聚合器（PA-CB E&I）牌照，为较早获得该牌照的非银行机构之一；RBI 预付费支付工具（PPI）牌照

  * 安全认证：PCI-DSS 合规、ISO 27001:2022 认证、SOC 2 Type II 认证

  * MENA 资质：通过子公司 Telr 运营，Telr 持有 PCI DSS Level 1 认证


**📊****业务覆盖：**

服务场景覆盖跨境电商、在线教育、数字娱乐、保险、金融科技、即时零售等行业。

## **二、收费项目与定价模式**

**📋****服务项目清单：**

国内支付网关收款：覆盖 180+ 种支付模式，具体分类详见第三章。

国际卡收单：支持 140+ 种货币，覆盖主要国际卡组织及 PayPal、Apple Pay。

跨境收款（Global Collections）：支持主要货币本地收款账户与 SWIFT 收款。

付款（Payouts）：支持银行账户 / UPI / 卡 / 钱包等多通道 24×7 付款。

增值服务：身份验证（SecureID）、风控（RiskShield）、分账（Easy Split）、订阅（Subscriptions）、即时结算（Instant Settlements）

**💰****计费规则：**

国内支付网关采用纯百分比费率模式（不含固定每笔费用），按支付方式区分收费标准。无设置费、无月费、无集成费。企业客户可获定制化费率，具体取决于交易量、行业类别、产品组合等因素。

付款（Payouts）、订阅（Subscriptions）、分账（Easy Split）、身份验证（SecureID）、风控（RiskShield）等产品线采用定制化定价模式，需联系销售团队获取报价。

**📝****费用项目补充说明：**

可能包含国际清算附加费（国际卡非 INR 结算时收取外汇转换费）、高级支持年费（可选增值服务）、GST 等项目。

**📌****小结：** 本章聚焦收费项目与适用规则，不含数值，最终以《商户协议》为准。

## **三、支付网络与跨境能力**

###  （一）支付网络与区域布局

**🇮🇳****印度本地支付**

支持 180+ 种支付模式：

  * UPI：Intent / Collect / QR（静态与动态）/ AutoPay / Credit Line on UPI / OTM 等主要类型，自建 UPI Switch（UPI 交换/路由系统）

  * 卡支付：Visa / Mastercard / RuPay / Maestro / American Express，自建卡 Switch（卡交换系统），直连银行和支付网络

  * 网银：覆盖主流银行

  * 钱包：Paytm / Airtel Money / Freecharge / Mobikwik / Ola Money / JioMoney 等

  * 先买后付与 EMI：LazyPay / ePayLater / Flexmoney / 银行 EMI 等

  * 银行转账：NEFT / IMPS / RTGS；eNACH / AutoPay 定期扣款；COD（货到付款）




国际支付网关支持 140+ 种货币的 Visa / Mastercard / American Express 卡支付，同时支持 PayPal Connect 集成和 Apple Pay。

**🌍****跨境收款路径（Global Collections）**

支持四种主要货币（USD / EUR / GBP / CAD）通过本地支付通道收款：ACH（美国）、SEPA（欧洲）、Faster Payments（英国）、EFT（加拿大）；30+ 种货币通过 Global SWIFT Account 收款。出口商路径遵循 OPGSP 规定，单笔限额 USD 10,000。

合规文件出具：Global Collections 通过 AD-1 合作银行在收款到账后 T+1 自动生成 e-FIRA（电子外汇入境汇款通知），用于出口商申请 GST 退税、DGFT 出口激励（如 RoDTEP、EPCG）等合规用途。International PG 路径提供按期汇总的 FIRS（外汇入境汇款报表），而非逐笔 e-FIRA。

**📥****海外商户进入印度市场收款（Import Stack）**

基于 PA-CB E&I 牌照中的进口（Import）授权，Cashfree Payments 提供面向海外注册商户（无印度实体）的印度本地收款方案。海外商户可直接入驻，接入 UPI、信用卡、借记卡、网银、虚拟账户等印度消费者常用支付方式，收取 INR 付款后结算至商户的境外银行账户。

在 RBI PA-CB 进口框架下运行，支持 API 集成与无代码接入两种方式，覆盖电商、数字服务、教育、旅游等跨境进口场景。海外商户入驻需提交公司注册文件、税务识别文件、银行账户信息及董事/授权签字人 KYC 资料。

**💱****汇率与结算机制**

国际支付网关提供动态货币转换（DCC）功能，产品名为 Pay Native：客户以本地货币支付，商户以 INR 结算。按 RBI 规定，跨境支付聚合器收款必须以 INR 结算至印度账户，国际卡交易若以非 INR 货币结算，将收取外汇转换费，具体费率需与服务方确认。

**🕌****MENA 市场（通过 Telr）**

通过子公司 Telr 支持阿联酋和沙特阿拉伯市场，覆盖 Visa / Mastercard / American Express / UnionPay / Apple Pay / PayPal / SADAD / Mada / STCPay 等支付方式。Telr 平台支持 30 种语言，满足中东本地化需求。

### （二）合规与安全体系

**🔒****数据存储与隐私**

数据存储在印度境内，符合 RBI 支付数据本地化要求。隐私政策基于印度法律框架（IT Act 2000 / PMLA 2002），适用《数字个人数据保护法》（DPDPA）2023。

**👤****反洗钱与 KYC**

遵循 PMLA 2002 下的 AML/KYC 要求。商户入驻需提交 KYC 文件（身份证明、地址证明、PAN、GST 号等）。自有 SecureID 身份验证平台提供 KYC、文档验证与欺诈检测能力。

**💰****客户资金管理**

作为 RBI 持牌支付聚合器，须维护客户资金隔离账户（托管账户），遵循最低净资产要求。

## **四、技术能力与结算效率**

###  （一）开发者生态与支付技术

**🔧****API 与开发者生态**

采用 RESTful API 架构，通过 Header 版本控制（x-api-version），覆盖支付网关 / 付款 / 订阅 / 身份验证 / 虚拟账户等完整产品线。

SDK 覆盖：服务端支持 Node.js / Python / Java / PHP / Go / .NET 六种语言；移动端支持 Android / iOS / Flutter / React Native / Cordova；Web 端提供 JavaScript 库与 React / Svelte 组件。

开发者工具：Dev Studio 交互式测试环境、独立沙盒测试环境、支付模拟 API、Webhook 事件系统（HMAC-SHA256 签名验证）、Discord 开发者社区。

在 GitHub 维护数十个公开仓库，API 文档完全公开，支持 AI 辅助搜索。

**🛡️****风控引擎（RiskShield）**

提供 AI/ML 驱动的实时欺诈检测与风险评分，同时覆盖收款（Payment Gateway）和付款（Payouts）双向场景。商户可自定义风控策略（风险阈值 / 黑名单 / 触发条件等）。

**⚡****支付优化**

AI 智能路由：动态重新路由至多银行支付网关，提升支付成功率。FlowWise 支付编排（多通道调度）平台：支持商户自主部署，可对接多个支付聚合器，在编排层集成 RiskShield 实现跨聚合器风控。

### （二）支付与结算效率

**⏱️****到账时效分级**

标准结算：T+2 工作日（含在交易手续费中）。即时结算提供三种模式：按需结算（单击即时）、定时结算（每日固定时段）、实时结算（15 分钟内到账，含银行假日）。

具体对接要求与系统性能指标以官方技术文档为准。

## **五、平台接入与运营支持**

###  （一）电商平台与独立站接入

**🛒****电商插件**

支持 Shopify、WooCommerce、Magento 等 13 个电商平台插件。提供托管收银台（Hosted Checkout）、预置收银组件（Drop-in UI）、Payment Links（无代码支付链接）、Payment Forms（无代码支付表单）等多种接入方式。

**📱****无代码方案**

Payment Links：通过短信、邮件、WhatsApp、社交媒体分享支付链接收款，无需技术开发。Payment Forms：自定义表单收集用户信息并收款。softPOS：手机变 POS 机，支持 UPI QR / NFC Tap&Pay / Payment Links / 现金管理。

### （二）平台分账与对账

**💼****Easy Split 分账服务**

收款后自动分账至多个供应商或合作伙伴账户，支持百分比与固定金额佣金扣除、灵活设置结算周期、供应商对账报告。适用于电商平台、外卖平台、保险经纪平台、共享经济平台等场景。

**🏦****Auto Collect 虚拟账户**

为每个客户或供应商分配唯一虚拟银行账户号或 UPI ID，收款自动匹配对应方，实现 IMPS / NEFT / UPI 收款自动对账。适用于贷款还款、保险保费、教育学费等场景。

**📊****对账与报表**

支持交易报告、结算与调整报告、供应商结算报告，报告导出支持 Dashboard 下载与 SFTP 自动推送（可配置频率）。

### （三）服务交付与支持

支持线上入驻，提供邮件、移动端 App（Pulse）即时聊天、Discord 开发者社区等支持渠道。企业客户可获专属客户经理与 WhatsApp 支持。

## **六、区域合规与避坑指南**

⚠️ 区域支付关键注意事项

**📋****印度市场上线清单**

  * ✅ KYB 资料（营业执照 / 法人身份证 / PAN / GST 号）

  * ✅ 业务说明与合规承诺

  * ✅ 测试环境 API 集成验证

  * ✅ Webhook 配置与回调测试

  * ✅ 风控策略配置




## **七、增值工具与行业方案**

###  （一）风控套件（RiskShield）

**📡****数据信号**

覆盖多维度风险识别：设备维度（设备指纹、越狱检测、Root 检测）；地理维度（IP 地理定位、代理 / VPN 检测、BIN 与发卡国一致性校验）；行为维度（交易频率、金额分布、夜间活动模式）；关系维度（账户关系图谱、邮箱 / 设备 / 卡号关联分析）。

**🧠****策略模型**

规则引擎（Smart Rules）：白黑名单、阈值、组合条件。ML 模型：实时评分，阈值可调。可执行动作：批准 / 拒绝 / 标记人工审核。

### （二）身份验证服务（SecureID）

综合身份验证平台，包含 KYC Link（在线 KYC 表单）、Video KYC（AI 驱动的多语言视频身份验证）、1-Click Onboarding（快速用户注册）。支持 PAN / Aadhaar / GSTIN / 银行账户验证等印度特色验证能力。

### （三）行业方案

**🌐****跨境电商（出口商）**

适配组合：International PG（140+ 货币卡收款）+ Global Collections（本地通道跨境收款）+ Payouts（供应商付款）+ RiskShield（跨境风控）

**🇮🇳****印度电商 / D2C**

适配组合：Payment Gateway（180+ 种支付模式）+ Payment Links + softPOS + Instant Settlements + Easy Split（平台分账）

能力支持：通过电商平台插件快速接入，支持 PayFast 快速结账（记住回头客支付方式）、未完成订单 WhatsApp 自动提醒

**🏥****保险行业**

适配组合：PG 收保费 + Payouts 赔付与佣金 + Cashgram 退款 + Easy Split 经纪分账 + eNACH 定期扣款 + 银行账户验证

**📚****在线教育 / 订阅**

适配组合：Subscriptions（卡 / UPI AutoPay / eNACH 定期扣款）+ Auto Collect（虚拟账户收学费）+ Payment Gateway

**📋****附：快速落地清单**

## **八、适用场景与选型建议**

###  适合使用 Cashfree Payments 的场景

**🌍****印度市场收款为主的跨境电商**

如果您的业务主要面向印度消费者，需要接入 UPI / 网银 / 钱包 / EMI 等印度本地支付方式，Cashfree Payments 在印度本地支付覆盖度较高，且具备自建交换系统的技术能力。

**📦****印度出口商的跨境收款需求**

如果您是印度注册企业，需要从海外客户收取外币货款，可通过 Global Collections 和 International PG 实现本地通道收款和国际卡收款，并提供 e-FIRA 合规文件自动出具能力。

**🏪****印度电商平台或市场模式**

如果您运营需要多方分账结算的平台，可通过 Easy Split、Instant Settlements、Auto Collect 等产品组合实现平台分账与自动对账。

**🕌****MENA 市场收款需求**

如果您的业务涉及阿联酋或沙特阿拉伯市场，可通过 Telr 子公司接入 Mada / SADAD / STCPay 等 MENA 本地支付方式。

**🤝****海外企业进入印度市场**

如果您是海外企业，希望向印度消费者收款但没有印度本地实体，Import Stack 方案基于 PA-CB 进口授权，支持海外商户直接入驻并接入印度本地支付方式，资金结算至境外银行账户。需注意该方案适用于 RBI 允许的商品和服务类别，具体合规要求需与服务方确认。

### 决策建议

**📊****市场覆盖匹配度**

Cashfree Payments 在印度市场具备深度覆盖能力，适合以印度为核心市场或印度出口商的跨境收付款需求。如果您的业务主要面向欧美或东南亚消费者，需要接入 iDEAL / Boleto / GrabPay 等区域本地支付方式，可同时了解 Stripe、Adyen、2C2P 等在相应区域具备本地收单能力的方案。

**💰****业务规模与成本评估**

如果您是印度中小企业，Cashfree Payments 提供无前期固定成本（无设置费 / 月费 / 集成费）、纯百分比费率模式，对小额高频交易（如 UPI 支付）较为友好。如果月交易量较大，可与服务方沟通定制化费率。

**🔧****技术实施能力**

Cashfree Payments 提供丰富的开发者工具（多语言 SDK / Dev Studio / 沙盒环境 / Discord 社区），技术文档和开发者工具较为完善。如技术资源有限，可优先使用无代码方案或电商插件快速接入。

**🔒****合规与数据驻留**

Cashfree Payments 的数据驻留在印度境内。如果您的业务需要满足 GDPR（欧盟）或 CCPA（加州）等国际数据保护要求，需评估合规适配度。

**📝****费用与合同条款**

在签约前，务必与服务方确认跨境交易的外汇转换费、增值服务定价、结算周期与费用等关键条款，建议同时与多家服务商对比，选择最符合业务需求的方案。

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

