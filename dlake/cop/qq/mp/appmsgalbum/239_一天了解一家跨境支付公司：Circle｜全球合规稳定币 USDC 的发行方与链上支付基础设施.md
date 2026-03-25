# 一天了解一家跨境支付公司：Circle｜全球合规稳定币 USDC 的发行方与链上支付基础设施

**Author:** 汇付通途
**Position:** 239
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488095&idx=1&sn=c676db9393b9ab2121eefd52dbb0abe1&chksm=c46e4a77f319c3619f08c8a7edf31b82df9833168e578e67e153fbda1ff0c3fa846258b7571b#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体**

2013 年成立，法定名称 Circle Internet Group, Inc.，注册于美国特拉华州。

**🌍****全球布局**

总部位于纽约 One World Trade Center，在波士顿、都柏林、巴黎、伦敦、新加坡等地设有办公室，支持全球远程办公模式。

**🛡️****合规资质**

持有美国、欧盟、英国、新加坡、百慕大、阿联酋等主要市场的加密货币监管牌照，通过 ISO 27001、SOC 2 Type II 等多项安全认证。

**🎯****业务定位**

稳定币发行方 + 链上支付基础设施服务商。核心产品包括：

  * **USDC** ：美元稳定币，完全准备金，1:1 兑美元

  * **EURC** ：欧元稳定币，完全准备金，按 MiCA 监管为 EMT（电子货币代币）

  * **USYC** ：代币化货币市场基金

  * **Circle Mint** ：机构级稳定币铸造/赎回服务

  * **CCTP（Cross-Chain Transfer Protocol）** ：原生 USDC 多链跨链协议


**📊****基本服务能力概览**

**⚠️****说明：** Circle Mint 仅面向机构客户（交易所、钱包、银行、金融科技公司），个人用户需通过合作交易平台获取 USDC。

## **二、计费结构与收费项目**

服务项目清单**🔗****链上交易费用**

Paymaster 服务：用户可用 USDC 支付 Gas 费（链上交易手续费），Circle 向用户加收 Gas 费的 10%，开发者无需支付费用。支持 Arbitrum、Base 等网络，计划扩展至 Ethereum、Polygon PoS、Solana 等。

Gas Station 服务（Beta）：开发者可为用户代付 Gas 费，按 Gas 费比例收费。

**👛****钱包服务费用**

Wallets 产品采用按月度活跃钱包（MAW）计费模式，提供免费额度，超出部分阶梯定价，具体费率需联系销售。

**🤖****智能合约服务费用**

Contracts 产品按 API 调用次数阶梯计费，不同调用量级别适用不同单价，大规模使用需联系销售定制。

**🏦****法币出入金费用**

Circle Mint 入金：Circle 不收取代币转入费用，发送方需支付网络 Gas 费。银行电汇 Circle 及银行合作伙伴不收费，用户自身银行可能收费。铸造/赎回费用为机构客户定制模式，需联系销售获取报价。

**🔄****跨链服务费用**

Gateway 产品收取链上费用，推广期提供优惠费率。

**📝****费用项目补充说明**

可能包含网络拥堵附加费、跨链转账费、合规审核费、大额交易定制费等项目。

**📌****小结：** 本章聚焦收费项目与适用规则，不含数值，最终以官方费率页面或《服务协议》为准。

## **三、链上能力与网络覆盖**

（一）区块链网络与资产支持**🔗****支持的区块链网络**

USDC 原生发行：约 30 条主流区块链，包括：

  * Layer 1：Ethereum、Solana、Avalanche、Stellar、Sui、Aptos、NEAR、Algorand、Hedera、XRP Ledger、XDC 等

  * Layer 2/Rollup：Arbitrum、OP Mainnet、Base、Polygon PoS、Linea、Starknet、ZKsync、World Chain、Unichain 等

  * 跨链生态：Noble（Cosmos 生态官方 USDC）、Polkadot Asset Hub




Circle Mint / Crypto APIs：约 29 条链具备加密入金/出金能力。

CCTP 跨链：20+ 条链可作为源链/目的链，采用"原生销毁 + 在目标链铸造"模型，保持统一的总供应量与可追溯性。

**💡****说明：** Circle 服务仅直接支持自有资产（USDC/EURC/USYC），不提供 BTC、ETH 等第三方加密货币的托管或交易功能。

（二）法币通道与区域覆盖**🌍****法币出入金覆盖**

Circle Mint 可在 185 个国家为机构客户提供稳定币铸造与赎回，支持：

  * 银行电汇（Wire）

  * SEPA 转账（欧元区）

  * 区域性银行网络转账




通过 FX 模块，可将本地货币（如巴西雷亚尔 BRL）兑换为 USDC，或在 USDC 与 EURC 之间兑换。

**💸****Circle Payments Network（CPN）**

CPN 为受监管金融机构提供稳定币结算网络，已开通支付通道包括：巴西、中国、哥伦比亚、香港、墨西哥、尼日利亚等，并在印度、菲律宾、新加坡、EEA、阿联酋、美国等市场扩展中。典型流程：本地法币转换为 USDC（链上结算），再转换为目标国本地货币，全流程通常在数分钟内完成。

（三）稳定币与储备机制**💰****USDC 储备结构**

  * 储备资产：约 85% 投资于 Circle Reserve Fund（USDXX，注册于 SEC 的 2a-7 政府货币市场基金，由 BlackRock 管理、BNY Mellon 托管），其余为现金存款（主要存放于全球主要银行）

  * 储备金率：100%，与 USDC 流通量完全对应

  * 审计机构：Deloitte & Touche LLP，每月出具审计报告

  * 透明度：每日在官网公布 Circle Reserve Fund 持仓


**💶****EURC 储备**

按 MiCA 监管要求，100% 流动性资产支持，支持随时赎回。

**🔄****链上换币**

CCTP 跨链：在源链销毁 USDC，在目标链根据 Circle 出具的跨链证明铸造等值 USDC，实现多链间统一供应。

Bridge Kit：开发者可收取自定义费用，Circle 按比例保留，剩余归开发者设置的收款地址。

**💱****法币-稳定币兑换**

Circle Mint 支持：

  * 以 USD 铸造/赎回 USDC

  * 以 EUR 铸造/赎回 EURC

  * 通过 FX 模块将本地货币兑换为稳定币




**💡****应用场景：** 如果您是机构客户（交易所、金融科技公司），可通过 Circle Mint 将银行账户中的美元直接铸造为 USDC，或将 USDC 赎回为美元存入银行账户，实现法币与稳定币的合规转换。

## **四、安全与托管**

（一）安全认证与审计**📜****基础认证：**

  * ISO 27001（通过收购 CYBAVO 获得）

  * SOC 2 Type II（独立审计机构执行）

  * NIST 加密模块验证


**🔍****智能合约审计：**

  * CCTP 合约由 ChainSecurity 和 OtterSec 独立审计，报告公开

  * Circle Gateway 智能合约由 ChainSecurity 审计

  * USDC 合约由 EtherAuthority 审计，报告公开


**🐛****漏洞管理：**

  * 提供 Immunefi Bug Bounty 计划

  * 支持安全邮箱和漏洞报告机制


（二）托管方案**🔑****密钥管理：**

通过收购 CYBAVO 获得 MPC（多方计算）技术，采用分布式安全架构、自定义安全加固操作系统、专利加密技术。

**🛡️****保险覆盖：**

CYBAVO 资产由标普 AA 级再保险公司承保，具体保险金额未公开披露。

**🔒****数据加密：**

传输层 TLS 1.2/1.3，存储数据 AES-256 加密。

## **五、生态与集成**

（一）开发者工具**🔌****API 与 SDK**

API 类型：RESTful API，覆盖钱包、合约、Mint、CPN、CCTP 等全流程，接口超过 100 个。

SDK 支持：后端（Node.js、Python、Java）、移动端（iOS、Android）、Web（JavaScript/TypeScript、React Native、Flutter），官方 SDK 共 9+ 个。

**🧪****测试环境**

  * 沙盒环境：独立测试 API 接口和测试密钥

  * 测试网络：Ethereum Sepolia、Polygon Amoy、Solana Devnet、Avalanche Fuji 等

  * 测试币领取工具：Circle Public Faucet（faucet.circle.com）可获取测试 USDC


**🛠️****辅助工具**

  * Postman API Suite：预设模板，支持直接测试

  * SDK Explorer：在线查看 SDK 方法、参数和响应

  * Console Dashboard：钱包、合约、Gas Station 可视化管理


（二）Webhook 与事件系统

支持 Webhook 通知系统，事件类型超过 30 种，包括 CPN 交易事件、Mint 交易事件、Wallets 事件等。安全机制使用 ECDSA_SHA_256 非对称密钥签名，支持自动重试机制。

（三）传统金融对接

支付网络合作伙伴：Visa、Mastercard

银行合作：巴克莱银行

托管机构合作：BNY Mellon、BlackRock（储备资产管理）

## **六、合规与监管状态**

（一）已获牌照与资质**🇪🇺****MiCA 合规状态**

Circle France 获得 ACPR 电子货币机构许可及 MiCA EMT 发行资质。USDC 与 EURC 在欧盟作为 EMT 发行，已发布 MiCA 合规白皮书。

（二）KYC/AML 实施**👤****KYC 要求：**

  * 个人客户：逐级验证（邮箱/手机、身份证件/活体检测、资金来源证明）

  * 企业客户：公司注册文件、受益所有人信息（UBO）、业务描述、财务报表


**🚫****制裁筛查：**

对客户和交易进行制裁筛查，包括 OFAC、UN、EU、UK 制裁名单，筛查制裁地址（如 Tornado Cash）。

**📋****Travel Rule：**

符合 FATF 指南，收集转账方和接收方信息。

## **七、增值服务**

（一）Gateway 统一余额服务

提供跨链 USDC 余额聚合与即时资金调用（跨链转账通常在 500 毫秒内完成），当前支持 11 条链（Arbitrum、Avalanche、Base、Ethereum、HyperEVM、OP Mainnet、Polygon PoS、Sei、Sonic、Unichain、World Chain）。开发者可构建跨链透明化的多链体验，对用户隐藏底层区块链的复杂性。Gateway 采用自托管模式，用户自行管理资金。

（二）USYC 代币化基金

受监管货币市场基金的链上形式，主要面向机构投资与链上收益管理。

（三）Contracts 智能合约平台

提供预审计的智能合约模板库，由 Thirdweb 提供，支持代币化和流程自动化。

**💡****说明：** Circle 当前不提供质押（Staking）、借贷（Lending）、OTC 大宗交易、加密货币卡等增值服务，专注于稳定币发行与链上支付基础设施。

## **八、适配场景分析**

适合使用 Circle 的场景**🏢****机构级稳定币铸造/赎回**

如果您是交易所、钱包、银行或金融科技公司，需要大规模铸造或赎回 USDC/EURC，Circle Mint 提供合规的法币与稳定币转换通道，覆盖全球主要市场。

**🔗****多链应用开发**

如果您正在开发需要多链支持的 Web3 应用，Circle 提供统一的 Wallets API 和 SDK，支持 Ethereum、Solana、Polygon、Arbitrum、Base 等多条链，可简化多链集成难度。

**🔄****跨链流动性管理**

如果您需要在多条区块链之间调配 USDC 流动性，CCTP 提供原生跨链能力（非第三方桥接代币），保持统一的总供应量与可追溯性。

**⛽****链上 Gas 费优化**

如果您希望降低用户链上交互门槛，Paymaster 服务允许用户用 USDC 支付 Gas 费（无需持有原生代币），Gas Station 服务允许开发者代付用户 Gas 费。

**⚖️****合规优先的稳定币集成**

如果您的业务对合规要求较高（如受监管金融机构），Circle 持有美国、欧盟、英国、新加坡等主要市场的监管牌照。

决策建议

在选择稳定币基础设施时，建议从以下维度进行综合评估：

**🎯****业务场景匹配度**

根据您的核心需求（稳定币发行/铸造、多链应用开发、跨链流动性、合规要求），对比多家服务商的适配程度。如果您需要 USDC 相关服务，Circle 是原生发行方；如果您需要 USDT 相关服务，可了解 Tether 方案；如果您需要综合性加密支付网关，可同时了解 BitPay、Coinbase Commerce 等方案。

**👥****客户类型适配**

Circle 主要服务于机构客户和开发者，不直接面向个人用户。如果您是个人用户，需通过 Coinbase、Binance 等合作交易平台获取 USDC。

**🔧****技术实施能力**

评估您的团队是否具备 API 对接、SDK 集成、智能合约交互等技术能力。如技术资源有限，可优先考虑 Circle 提供的测试环境、Postman Suite、SDK Explorer 等开发者工具降低接入门槛。

**⚖️****合规与监管风险**

加密货币监管政策在全球范围内仍不统一，建议在使用前：

  * 确认您所在地区是否允许使用稳定币进行商业活动

  * 确认 Circle 在您所在地区是否持有必要牌照

  * 咨询专业法律和税务顾问




**⚠️****风险提示：**

  * 加密货币价格波动较大，即使是稳定币也存在脱锚风险

  * 各国加密货币监管政策不同，且可能发生变化，使用前请确认当地法规

  * 链上交易不可逆，转账前请仔细核对地址

  * 私钥丢失将导致资产永久无法找回




### 📌 重要提示与数据说明

**⚠ 跨境支付涉及外汇管制、区域合规及技术风险** ，企业决策前请以官方信息为准并咨询专业机构；

**⏰时效** ：本文信息截至2026年1月，含行业分析及公开数据整理，可能存在时效差异；

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

