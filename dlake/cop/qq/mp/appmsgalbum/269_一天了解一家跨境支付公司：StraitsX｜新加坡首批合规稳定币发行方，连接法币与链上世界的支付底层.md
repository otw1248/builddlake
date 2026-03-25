# 一天了解一家跨境支付公司：StraitsX｜新加坡首批合规稳定币发行方，连接法币与链上世界的支付底层

**Author:** 汇付通途
**Position:** 269
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488463&idx=1&sn=3c9d0b3e1b026e51522ec2c39cb79139&chksm=c46e4be7f319c2f1f0f6c87d349252094ccebd26dbb096f207aed9db222c83bc6091ca5afad7#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **🏢****一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****发展历程**

前身 Xfers 于 2014 年在新加坡创立，2015 年加入 Y Combinator（S15 批次），以法币支付网关起步。2020 年推出 StraitsX 品牌并上线首个新加坡元稳定币 XSGD。2025 年完成品牌焕新，正式定位为独立的稳定币基础设施品牌。

StraitsX 通过多个新加坡注册实体分别运营稳定币发行、数字支付代币服务和法币支付网关业务，隶属于 Fazz Financial Group，承担集团数字资产基础设施板块。

**🌍****全球布局**

总部位于新加坡，在印尼设有运营实体。

**🛡️****合规资质**

  * 加密货币牌照：新加坡 MAS MPI（Major Payment Institution，主要支付机构）牌照 4 张，覆盖电子货币发行、境内与跨境汇款、商户收单、DPT（Digital Payment Token，数字支付代币）服务

  * 稳定币发行批准：2023 年获 MAS 稳定币发行 IPA（In-Principle Approval，原则性批准），XSGD 和 XUSD 被认定为符合即将实施的 SCS（Single-Currency Stablecoin，单一货币稳定币）框架

  * 印尼牌照：电子货币运营牌照

  * 卡组织资质：VISA Principal Member




## **二、费用体系**

**📋****服务项目清单**

链上交易费用：包含 Gas 费（链上交易手续费）由谁承担的规则，以及网络费用上限。平台按区块链网络类型分别设定费用上限，L2（Layer 2，扩展层）和低 Gas 费网络的上限显著低于 Ethereum 主网。小额链上转入可享受手续费减免。

法币出入金费用：SGD 和 USD 入金通道（FAST、PayNow、银行转账、SWIFT）费用规则各异；SGD 出金和 USD 出金采用不同的收费机制。

稳定币铸造与赎回费用：铸造（将法币按 1:1 转换为稳定币）和赎回（将稳定币按面值转回法币）的费用因币种和通道而异，部分铸造和赎回操作不收取平台手续费。

稳定币兑换费用：稳定币之间的即时兑换（Swap）声称不收取额外手续费，但根据服务条款，兑换汇率中可能包含买卖价差（spread）和加价（mark-up），具体比例由平台决定。

OTC 费用：大额交易通过 OTC（场外交易）柜台进行，报价中包含买卖价差。

API 集成费用：面向企业客户的 API 集成包含设置费、账户维护费和交易费三层费用结构，具体金额需联系销售团队。

**📊****计费规则**

按交易类型、币种、区块链网络、交易金额等因素分级定价。链上 Gas 费根据网络拥堵情况动态调整，平台设有费用上限。个人账户不收取月度管理费。

**📌****小结：** 本章聚焦收费项目与适用规则，不含数值，最终以《商户协议》为准。

## **三、支付网络与稳定币体系**

###  （一）区块链网络支持

平台整体覆盖 12 条区块链网络（含用于第三方稳定币收发的 Tron 等通道），覆盖范围如下：

  * L1（Layer 1，主链）：Ethereum（以太坊）、Solana、BNB Chain、Avalanche、Zilliqa、XRPL（XRP Ledger）、Hedera、PlatON

  * L2（Layer 2，扩展层）：Polygon、Arbitrum、Base

  * 其他：Tron（波场，用于第三方稳定币收发）




跨链方式：通过平台内部完成——用户将稳定币存入 StraitsX 账户后，余额统一显示，可选择任一支持网络转出，无需使用外部跨链桥。

### （二）自有稳定币体系

XSGD（新加坡元稳定币）：锚定 SGD，2020 年发行，支持 Ethereum、Polygon、Avalanche、Arbitrum、Zilliqa、Hedera、XRPL、Solana 等多条区块链网络，市值约 1300 万美元（截至 2025 年底）。

XUSD（美元稳定币）：锚定 USD，2024 年在 Ethereum 部署，支持 Ethereum、BNB Chain、Solana。

XIDR（印尼盾稳定币）：锚定 IDR，支持 Ethereum、Polygon、Zilliqa，仅面向印尼居民。

第三方稳定币：支持 USDC（Circle 发行的美元稳定币）和 USDT（Tether 发行的美元稳定币）的收发与兑换。

**⚠️********注意：** StraitsX 聚焦稳定币基础设施，平台支持稳定币的收发和兑换，BTC、ETH 等加密货币的交易需通过交易所等渠道完成。

### （三）Swap 兑换与法币铸造、赎回

**🔄****Swap 兑换功能**

支持稳定币之间的即时兑换，包含 XSGD 与 USDC、XSGD 与 XUSD、XUSD 与 USDC 等交易对。

**💱****法币与稳定币兑换**

  * 铸造：银行转入法币后，平台自动铸造对应稳定币

  * 赎回：持有人可按面值赎回法币，通过银行转出




**💡********应用场景：** 如果您从事东南亚跨境贸易，需要在 SGD、USD 之间频繁转换，可利用 XSGD 和 XUSD 之间的 Swap 功能，配合法币铸造和赎回通道，减少传统银行换汇的中间环节和时间成本。

### （四）法币通道与区域覆盖

**💵****法币出入金**

  * SGD（新加坡元）：FAST（新加坡即时转账）、PayNow（新加坡即时支付系统）、银行转账

  * USD（美元）：SWIFT 电汇

  * IDR（印尼盾）：银行转账、QRIS（印尼国家 QR 支付标准）、便利店零售支付（Alfamart、Indomaret 等）


**📍****区域覆盖**

  * 新加坡：完整的 SGD 和 USD 出入金通道

  * 印尼：IDR 出入金（通过本地运营实体）




## **四、安全与托管**

###  （一）储备金证明机制

XSGD 和 XUSD 的储备资产由 DBS Bank、Standard Chartered 等银行以信托形式托管，独立于公司运营资产，保障代币持有人权益。

审计频率：每月两次，由 ISCA（Institute of Singapore Chartered Accountants，新加坡特许会计师协会）注册公共会计师执行独立审计证明，报告在官网公开发布。

XIDR 储备由印尼受监管金融机构持有，月度储备报告由独立第三方会计师事务所按 SSAE 3000 标准出具。

### （二）智能合约审计

XSGD 和 XUSD 智能合约由 Quantstamp（区块链安全审计公司）进行审计。Ethereum 合约源码已在 Etherscan 验证，Zilliqa 合约在 GitHub 开源。智能合约采用可升级的合约架构，包含冻结功能——仅在执法机构要求下使用。

### （三）托管架构与安全体系

钱包类型：托管钱包（Custodial Wallet）——平台控制私钥，用户通过 Dashboard 管理资产。

访问控制：支持 2FA（双因素认证）验证、区块链地址白名单、四级角色权限管理（Owner/Admin/Operation/Developer）。

链上安全监控：对接 Elliptic 和 Merkle Science 两家区块链分析公司，覆盖交易监控和合规筛查。

云服务：使用 AWS，持有 PCI DSS Level 1、ISO 27001 等多项安全认证。

## **五、合作生态与开发者工具**

###  （一）交易所与金融机构合作

与 Binance、Bybit、OKX、Coinbase、Gemini、Bitstamp 等交易所建立合作。DVA（Dedicated Virtual Accounts，专属虚拟账户）为交易所和机构客户提供合规的以法币计价的虚拟账户，法币存入后自动转换为稳定币，接入 SWIFT 和 FAST 银行轨道。

### （二）开发者工具

API 体系：提供 6 大类 RESTful API——Customer Profiles（客户档案管理）、Payment（收款）、Payout（付款）、Swap（兑换）、Blockchain（链上转账）、Transaction Limit（限额管理），覆盖完整的法币与稳定币交易流程。支持三种集成模式：First Party Transfer（交易所/金融科技平台）、Third Party Transfer（支付服务商/市场平台）、Regular Transfer（企业财务/内部流转）。

Webhook 系统：覆盖收款、付款、链上转账、Swap、客户档案等事件，支持签名验证、来源 IP 白名单和自动重试机制。

测试环境：提供独立 Sandbox 端点和密钥，支持模拟银行转账和 PayNow 支付测试。

辅助工具：Postman Collection、cURL 示例、错误码文档、请求去重（幂等性）机制。

## **六、合规与监管状态**

###  （一）KYC/AML 实施

KYC（Know Your Customer，了解你的客户）：新加坡用户支持 Singpass MyInfo 一键验证；国际用户通过 Jumio 进行身份验证。企业客户由 Sales Team 直接管理验证流程。

AML（Anti-Money Laundering，反洗钱）：作为 MAS 持牌机构，须建立 AML 程序、进行客户筛查和交易监控、向有关部门报告可疑交易。XSGD 声称为全球首个 Travel Rule（资金旅行规则）合规稳定币。

### （二）监管风险提示

**⚠️********风险提示：** 加密货币监管政策在全球范围内仍处于快速演变阶段，各国政策可能发生变化，使用前请确认当地法规要求。StraitsX 目前在新加坡和印尼持有监管牌照，在扩展至更多市场前，建议用户确认目标市场的法规要求并咨询专业法律和税务顾问。MAS SCS 框架尚在实施过程中，政策细节可能调整。

## **七、拓展业务与产品路线图**

###  （一）VISA 卡发行服务

作为 VISA BIN Sponsor 提供卡发行基础设施，支持虚拟卡和实体卡发行，以稳定币结算。已与 Pionex、RedotPay 等合作发行稳定币消费卡，适用于金融科技公司、Web3 项目等场景。

### （二）OTC 柜台服务

为大额交易提供 OTC 服务，支持稳定币与稳定币、法币与稳定币之间的兑换，当日结算，适用于机构客户和高净值用户。

### （三）跨境 QR 支付网络

代表性案例：Alipay+ × GrabPay × StraitsX 跨境支付方案已于 2024 年正式上线——游客使用 Alipay+ 扫描 GrabPay 商户 QR 码，StraitsX 处理实时外汇转换和稳定币结算，覆盖新加坡超过 10 万家商户。运行于 Avalanche 区块链，基于 MAS Project Orchid 框架下的 PBM（Purpose Bound Money，有目的约束的数字货币）标准。

计划中项目：Project BLOOM——与泰国 KBank 合作的新加坡至泰国跨境 QR 支付方案。

### （四）其他服务与路线图

  * StraitsX Earn：允许特定用户借出代币获取收益，由独立实体运营

  * StraitsX ON（开放网络）：2025 年推出的统一稳定币解决方案网络，由 XUSD 驱动

  * x402 标准支持：XSGD 和 XUSD 原生支持 x402 互操作标准，适用于 AI 代理间的自动支付场景

  * 产品路线图：2026 年初已在 Solana 上线 XSGD 和 XUSD；Grab Web3 钱包集成（MOU 已签署）；跨境支付通道拓展至日本、台湾（规划中）；2026 年 3 月宣布加速韩国市场扩展，探索与 Visa 合作的全球汇款方案




## **八、适用场景与选择建议**

###  适合使用 StraitsX 的场景

  * **加密交易所与金融科技平台**  
如果您运营加密交易所或金融科技平台，需要合规的法币出入金通道，StraitsX 的 DVA 服务可提供对应方案。

  * **跨境稳定币结算需求**  
如果您从事东南亚跨境贸易，希望利用稳定币降低传统电汇的时间和手续费成本，StraitsX 提供多币种稳定币和多链转账能力。

  * **稳定币卡发行需求**  
如果您需要发行可用稳定币余额消费的 VISA 卡，StraitsX 提供 BIN Sponsor 卡发行服务。

  * **新加坡与印尼市场运营**  
如果您的核心业务集中在新加坡和印尼，StraitsX 在这两个市场持有完整的监管牌照和本地化法币通道。

  * **大额交易需求**  
如果您需要进行大额稳定币交易，StraitsX 提供 OTC 柜台服务，支持当日结算。




### 决策建议

在选择稳定币支付基础设施时，建议从以下维度进行综合评估：

  * **业务场景匹配度：** 根据核心需求对比多家服务商。如果需要全球范围的法币出入金通道和美元稳定币服务，可同时了解 Circle、Paxos 等方案；如果聚焦东南亚加密支付网关，可对比 Triple-A、dtcpay 等本地化方案。

  * **技术实施能力：** 评估团队是否具备 API 对接能力；如技术资源有限，可优先考虑提供插件等低门槛接入方式的服务商。

  * **安全与托管偏好：** 如果偏好自主控制资产，可选择支持自托管或 MPC（Multi-Party Computation，多方安全计算）钱包的方案。

  * **费用与合同条款：** 在签约前，务必明确计费规则和服务边界等关键条款。




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

