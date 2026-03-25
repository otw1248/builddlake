# 一天了解一家跨境支付公司：Coinbase Commerce｜链上加密支付网关与 USDC 稳定币结算平台

**Author:** 汇付通途
**Position:** 267
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488418&idx=1&sn=c0b2d22f2b80f6c9dbaf26fe597b09bb&chksm=c46e4b8af319c29cb79ecfa6f12c11415dd342e273d3e73ca9254a1518d3713d8aa52722ed9a#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体**

Coinbase Commerce 是 Coinbase Global, Inc.（NASDAQ: COIN）旗下的加密货币支付产品线，2018 年 2 月上线；母公司 Coinbase Global, Inc. 于 2012 年在美国特拉华州成立，2021 年在纳斯达克上市，2025 年纳入标普 500 指数。2025 年 12 月完成注册地从特拉华州到德克萨斯州的迁移。

**🌍****全球布局**

Coinbase 自 2020 年起采用 Remote-First（远程优先）工作模式。SEC 文件登记地址位于纽约，在夏洛特设有合规中心。

**🎯****业务定位**

Coinbase Commerce 定位为加密支付网关，帮助商户接受加密货币支付并以 USDC（Circle 发行的美元稳定币）结算。母公司 Coinbase Global 业务覆盖加密货币交易所、机构托管（Coinbase Custody）、开发者平台（CDP）、Layer 2（L2，二层网络）区块链网络 Base 及衍生品交易等。

**🛡️****合规资质**

  * 加密货币牌照：持有美国、欧盟、英国等 12 个以上主要市场的监管牌照

  * 安全认证：SOC 2 Type II（Coinbase Prime 与 Custody）、SOX 合规（上市公司法定要求）

  * 关联代币/协议：USDC、Base（Commerce 核心结算层）


**📋****基本服务能力概览**

产品模式：Self-managed（非托管，商户自持助记词，全球可用，无直接法币出金）与 Coinbase-managed（托管，Coinbase 代管资产，支持法币出金，当前仅美国和新加坡可用）两种模式

支持的区块链：Ethereum（以太坊）、Base、Polygon、Bitcoin、Litecoin、Dogecoin、Bitcoin Cash 共 7 条网络

结算方式：支持加密货币自动兑换为 USDC 结算，商户即时收到确定金额

主要合作：Shopify USDC 直接支付集成、WooCommerce 插件、Stripe 结算基础设施

## **二、费用项目与服务规则**

**⛽****链上交易费用**

Gas 费（链上交易手续费）由付款人（顾客）承担，商户不承担支付环节的网络费用。不同区块链网络的 Gas 费差异较大，Base 网络费用较低。

**💸****平台服务费**

对所有已完成的加密货币收款交易统一收取平台服务费，从结算货币中扣除，适用于所有加密货币和网络。

**🏦****商户提现费用**

商户从 Commerce 钱包提现 ERC-20 代币至外部地址时，需自行承担对应网络的 Gas 费。提现至 Coinbase.com 账户同样需支付网络费。

**📅****账户与订阅费用**

无注册费、无月费、无年费、无设置费。

**📝****费用项目补充说明**

可能包含 Uniswap V3 链上兑换的市场滑点（由流动性池深度决定，非平台收取）、法币转换路径中涉及的 Coinbase 平台费用、跨网络提现的动态 Gas 费等项目。

**📌****小结：** 本章聚焦收费项目与适用规则，不含数值，最终以官方费率页面或《服务协议》为准。

## **三、链上能力与法币通道**

###  （一）区块链网络与资产支持

**⛓️****支持的区块链网络**

Commerce Onchain Payment Protocol 智能合约部署在 Ethereum、Polygon、Base 三条 EVM（以太坊虚拟机）兼容网络上，同时通过传统 UTXO 方式支持 Bitcoin、Litecoin、Dogecoin、Bitcoin Cash 网络，共计 7 条网络。

**⚠️****说明：** Coinbase 交易所平台支持 Solana、Arbitrum、Optimism 等更多网络，但 Commerce 支付产品的智能合约仅部署在上述三条 EVM 链上。

**💵****支持的稳定币与自动兑换**

覆盖 USDC、USDT（Tether 发行的美元稳定币）、DAI 三种美元稳定币，以及 EURC（Circle 发行的欧元稳定币，符合 MiCA 合规要求，支持 Base 和 Ethereum 网络）。Onchain Payment Protocol 通过集成 Uniswap V3（去中心化交易协议）实现链上即时兑换：付款人可使用任意在 Uniswap 上可交易的 ERC-20 代币支付，系统在同一笔链上交易中一步完成代币兑换与 USDC 结算（交易具有原子性，即全部完成或整笔撤回），商户收到的结算金额与请求金额一致。

**🪙****支持的加密货币**

直接支持 BTC、ETH、USDC、BCH 等约 11 种主流加密资产。通过上述 Uniswap V3 自动兑换功能，实际可接受数百种在 Uniswap 上可交易的代币。

**⚡****链上性能**

  * Base 网络：区块时间约 2 秒，Gas 费通常较低，为 Commerce 主推结算网络

  * Ethereum：区块时间约 12 秒，Gas 费波动较大

  * Polygon：区块时间约 2 秒，Gas 费较低

  * Bitcoin：区块时间约 10 分钟，需等待多次区块确认




### （二）法币通道与区域覆盖

**💱****法币出入金覆盖**

  * Self-managed 模式：不提供直接法币出金，商户需先提现至 Coinbase 账户，通过平台完成加密货币到法币的转换后提现至银行账户

  * Coinbase-managed 模式：支持 USD 结算，USDC 余额可通过 Wire 或 ACH 提现至商业银行账户

  * Shopify 集成：商户可选择以当地货币接收（通过 Stripe 处理法币转换）




## **四、安全与托管**

###  （一）资产托管安全

**❄️****冷热钱包分离**

Coinbase 平台绝大多数客户资产采用冷钱包（离线存储）保管，采用分布在不同地理位置的保险箱存储方式。热钱包（在线存储）仅保留少量资产用于日常交易处理。

**🔑****密钥管理**

采用密钥分片技术将私钥分割为多个碎片，需集齐预设数量的碎片方可重组。密钥持有人分布在不同地理位置，密钥操作须经过身份验证和数据完整性校验。配备 HSM（硬件安全模块）保护密钥。

**🔒****数据加密**

静态数据采用 AES-256 加密，传输数据采用 SSL/TLS 加密。

**🛡️****保险覆盖**

持有犯罪保险，覆盖存储系统中因盗窃（含网络安全攻击）导致的数字资产损失。USD 余额通过合作银行享受 FDIC 保险。加密资产不受 FDIC/SIPC 等政府保险保护。

**🔐****Commerce Self-managed 安全模型**

商户自持 12 字助记词，Coinbase 不持有商户私钥，无法恢复丢失的助记词或资金。退款操作需输入助记词确认。

### （二）智能合约安全

**📄****合约开源状态**

Commerce Onchain Payment Protocol 核心合约已在 GitHub 开源，合约采用不可篡改设计，每次版本更新需部署新合约地址。

**🔍****安全审计**

Coinbase 内部安全团队对链上代码执行多轮审计，自研工具用于自动检测和分类智能合约风险。OpenZeppelin 为 Coinbase 长期安全合作伙伴，Commerce 合约安全同时通过 Cantina 平台的漏洞赏金计划接受外部检验。

**💰****漏洞赏金计划**

在 HackerOne 平台运营漏洞赏金计划超过 10 年，累计支付超过 230 万美元赏金；在 Cantina 平台设有覆盖所有主网智能合约的链上漏洞赏金计划，在加密行业属于规模较大的漏洞管理体系之一。

### （三）用户账户安全

强制双因素认证（2FA），支持 Authenticator App、SMS、安全密钥（YubiKey）；支持生物识别登录、Passkey 登录、提款地址白名单、新设备验证、异常活动告警等功能。

**⚠️****风险提示：**

  * 链上交易不可逆，转账前需仔细核对地址

  * 私钥或助记词丢失将导致资产永久无法找回

  * 加密货币价格波动较大，即使是稳定币也存在脱锚风险




## **五、商户工具与平台集成**

###  （一）电商平台集成

**🛍️****Shopify 集成**

通过 Commerce Payments Protocol（与 Shopify 共同开发的开源链上支付协议，部署在 Base 上）实现 USDC 直接支付，覆盖 34 个国家，支持授权-捕获-退款的完整电商支付流程。

**🛒****更多电商插件**

支持 WooCommerce、JumpSeller、Primer 等平台的官方插件集成。

### （二）开发者工具

**🔧****API 与 SDK**

提供 RESTful API，覆盖收款请求创建/查询、结账页面管理、事件查询等核心功能，支持多种主流编程语言的代码示例。新一代前端工具 OnchainKit 提供 React 组件，与主流 Web3 开发库兼容，持续更新。

**🔔****Webhook 事件**

支持已创建、待确认、已确认、失败 4 种事件通知。

**🧩****无代码工具**

提供 Payment Links（可分享支付链接）、Payment Buttons（嵌入式 HTML 按钮）、Dashboard 创建托管收银页面（Hosted Checkout）等无需开发的接入方式。

**🧪****测试环境**

Onchain Payment Protocol 在主要支持网络的测试网上均部署了合约，开发者可使用测试网进行集成测试。

### （三）企业服务功能

**🏢****Coinbase Business 付款功能**

支持发送 USDC 至任何链上地址或邮箱，提供联系人管理、Payouts API（支持批量和定时付款）。

**📊****会计集成**

支持 QuickBooks 和 Xero 对账集成（通过 CoinTracker 实现）。

**📈****Dashboard 功能**

Commerce 商户后台支持创建 Checkout/Invoice、查看支付状态和历史、交易报告、API 密钥管理、Webhook 配置、退款操作和提现管理。

## **六、合规与监管状态**

###  （一）牌照覆盖

Coinbase Global 持有覆盖范围较广的加密货币牌照组合，主要包括：

**🇺🇸****美国**

  * FinCEN MSB 注册

  * 纽约州 NYDFS BitLicense（2017 年获得）及有限目的信托牌照

  * 多州 Money Transmitter License（含华盛顿特区和波多黎各）


**🇪🇺****欧盟**

  * MiCA 授权

  * 爱尔兰央行 EMI 注册

  * 德国 BaFin 加密资产托管和交易许可

  * 塞浦路斯 CySEC MiFID II 投资公司牌照


**🇬🇧****英国及新兴市场**

  * 英国 FCA 加密资产注册（VASP）

  * 百慕大 BMA 加密货币运营许可

  * 阿根廷 CNV 注册、印度 FIU 注册




### （二）KYC/AML 实施

**🆔****KYC（了解你的客户）要求**

  * Coinbase-managed 模式：商户需完成 Coinbase Business 注册和完整 KYC 验证（身份证件、地址、业务信息、UBO 信息等）

  * Self-managed 模式：仅需邮箱注册，无 KYC 要求

  * 付款人：通过 Coinbase 账户支付的用户已完成平台 KYC；自托管钱包支付无直接 KYC 要求


**🚫****AML（反洗钱）措施**

遵循 BSA（银行保密法）和 USA PATRIOT Act（美国爱国者法案）合规要求。Commerce Onchain Payment Protocol 内置 OFAC（美国海外资产控制办公室）制裁地址筛查，采用自研实时拦截工具在交易到达用户账户前自动筛查。使用 Chainalysis 区块链分析工具进行交易监控。

### （三）数据保护

Coinbase Commerce 提供独立隐私政策，遵循 GDPR（通用数据保护条例）和 CCPA（加州消费者隐私法案）数据保护要求，支持跨境数据传输（采用欧盟标准合同条款）。

**⚠️****说明：** 加密货币监管政策在全球范围内仍处于快速演变阶段，各国政策可能发生变化。建议用户在使用前确认当地法规要求。

## **七、适配场景与决策参考**

###  适合使用 Coinbase Commerce 的场景

  * **Shopify 电商商户** 如果您运营 Shopify 独立站且目标市场在已覆盖国家范围内，Commerce Payments Protocol 支持完整的电商支付流程和灵活的结算币种选择。

  * **加密货币原生企业** 如果您的客户群体主要使用加密货币支付，Commerce 支持数百种代币支付并以 USDC 结算，规避商户端的价格波动风险，Self-managed 模式无需 KYC 即可全球使用。

  * **USDC 稳定币收款需求** 如果您需要接受 USDC 稳定币支付（如 SaaS 订阅、数字商品、捐赠等场景），推荐使用 Base 网络，Coinbase Business Payment Links 支持由平台代付 Gas 费。

  * **跨境 B2B 稳定币结算** 如果您有跨境付款需求且希望通过稳定币降低传统电汇的时间和费用成本，Coinbase Business Payouts 支持通过 USDC 向全球地址或邮箱发送付款。




### 决策建议

在选择加密支付服务商时，建议从以下维度进行综合评估：

**📊****业务场景匹配度**

根据您的业务类型（Shopify 电商、加密原生项目、传统企业尝试接受加密支付），对比多家服务商。如果您需要自托管方案，可同时了解 BTCPay Server 等开源方案；如果需要更广泛的区块链网络覆盖（如 Solana、BNB Chain），可对比 BitPay、CoinGate 等方案。

**💱****法币出金需求**

如果您需要将收到的加密货币转换为法币，需注意不同产品模式的法币出金能力差异较大，且 Managed 模式的地区覆盖范围有限。

**⚖️****合规风险评估**

各国加密货币监管政策差异较大，建议在使用前咨询专业法律和税务顾问，确认当地合规要求。

**🔧****技术实施能力**

评估团队是否具备区块链基础知识和 API 对接能力。如技术资源有限，可优先使用 Payment Links、Shopify 插件等无需开发的接入方式。

**🔄****与传统收单方案的差异**

加密支付与信用卡收单、PayPal、银行电汇等传统方案在多个维度存在差异：结算速度方面，链上支付（特别是 Base 网络）可在秒级完成确认，传统跨境电汇通常需要 1～5 个工作日；拒付风险方面，链上支付经区块确认后不可逆，不存在信用卡拒付争议流程，但同时也意味着商户需自行处理退款；买家覆盖面方面，加密支付目前的消费者使用率仍低于信用卡和电子钱包，适合作为补充收款渠道而非完全替代传统收单。建议根据自身业务的客户支付习惯和市场分布，评估加密支付渠道与现有收单方案如何搭配使用。

**🇨🇳****人民币结算路径**

Coinbase Commerce 当前支持 USD 法币出金（Wire/ACH），不提供人民币直接结算通道。如果您的业务最终需要将收入转为人民币，需在 Coinbase 平台完成加密货币到 USD 的转换后，再通过银行或第三方换汇服务完成 USD 到人民币的结算，该环节涉及额外的换汇成本和合规要求，建议提前规划资金结汇方案。

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

