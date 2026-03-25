# 一天了解一家跨境支付公司：MoonPay｜连接法币与加密资产的支付基础设施，从出入金到稳定币网络

**Author:** 汇付通途
**Position:** 262
**Source:** http://mp.weixin.qq.com/s?__biz=Mzk2NDcyNzExMQ==&mid=2247488381&idx=1&sn=bdddeb9869c34f4aaf5131e707fc3b01&chksm=c46e4b55f319c24382f3177f10c1173d931dcf43fed157bb99e16af670999dc13813631dd726#rd

---

本文对跨境支付公司的界定：持支付牌照主营跨境收付款 / 换汇，或为该业务提供技术支撑的持牌服务商。

## **一、企业概况**

以下内容基于企业公开材料、监管公示与行业媒体整理，仅供参考。

**📅****成立时间与主体：**

2019 年正式上线运营，项目启动于 2018 年；由 Ivan Soto-Wright（CEO）与 Victor Faramond（首席工程师）联合创立。

美国注册实体：MoonPay USA LLC，注册地为特拉华州 Dover；英国注册实体：MoonPay (UK) Limited；欧洲实体：MoonPay Europe B.V.（荷兰）；另设有澳大利亚、泽西岛等地实体。

**🌍****全球布局：**

历史总部位于美国迈阿密，2025 年 4 月宣布将美国总部迁至纽约 SoHo 区；在伦敦、纽约、迈阿密等地设有运营团队，覆盖 9 个国家。

**🎯****业务定位：**

核心业务为法币出入金（法币与加密货币的双向兑换）基础设施——帮助用户通过信用卡、借记卡、Apple Pay、PayPal、Venmo、银行转账等方式购买和出售加密货币。在此基础上，业务已扩展至商户收款、企业稳定币服务、数字资产托管、NFT、企业稳定币发行及 AI Agent 基础设施等方向。

**🛡️****合规资质：**

  * 加密货币牌照：美国 FinCEN MSB 注册、纽约州 BitLicense 与 Limited Purpose Trust Charter（NYDFS 授权）、美国 47 个州/地区 Money Transmitter License

  * 欧盟：MiCA（欧盟加密资产市场法规）授权，由荷兰 AFM 监管

  * 英国：FCA 加密资产注册

  * 其他：加拿大 FINTRAC 注册、澳大利亚 AUSTRAC 注册、泽西岛 JFSC 注册

  * 安全认证：ISO 27001（信息安全管理）、ISO 27018（云端个人信息保护）、ISO 27701（隐私信息管理）、PCI DSS 4.0 Level 1（支付卡行业安全标准最高等级）、SOC 2 Type 2（服务组织控制报告）




## **二、计费结构与服务规则**

**📋****服务项目清单**

**法币出入金费用**

入金（法币购买加密货币）与出金（加密货币兑换法币）均按支付方式、交易金额、法币币种、地区等因素分别定价；另提供 MoonPay Balance（法币余额账户）模式。

**链上交易费用**

链上 Gas 费（链上交易手续费）由用户承担。Gas 费随网络拥堵程度波动，用户可选择低费用网络（如 Solana、Polygon 等 L2 网络）以降低成本。

**平台服务费与生态费**

平台服务费涵盖支付处理、退款保护、欺诈防护、KYC（了解你的客户）验证、区块链分析、合作伙伴分成等。部分合作伙伴可能设定额外生态费（百分比形式）。

**兑换/交易费用**

加密货币之间的兑换（Swap）与转换（Convert）通过第三方 DeFi（去中心化金融）聚合器执行。资产价格中可能包含点差，用于应对加密资产价格波动和运营成本。

**其他服务费用**

商户收款（MoonPay Commerce）按交易收费，免开户费和月费，商户可选择直接收取加密货币或自动转换为法币。企业级稳定币账户（Virtual Accounts）包含交易处理费、银行通道费及链上 Gas 费，具体费率在开户时告知。数字资产托管和 OTC 交易服务采用定制化报价模式。

**📊****计费规则**

所有费用在交易确认前逐项列明，包含平台服务费、链上 Gas 费和生态费（如适用）三类。非美元交易可能涉及货币转换附加费。

**📝****费用项目补充说明**

可能包含最低交易费用、非美元货币附加费、银行或发卡机构收取的国际交易费等项目。

**📌****小结：** 本章聚焦收费项目与适用规则，不含数值，最终以官方费率页面或《服务协议》为准。

## **三、链上网络与法币通道**

###  （一）链上网络与资产支持

**🔗****支持的区块链网络**

支持 30+ 条区块链网络：

  * L1 主链：Bitcoin、Ethereum（以太坊）、Solana、BNB Chain、Tron（波场）、Avalanche C-Chain、XRP Ledger、Stellar、Cosmos、Cardano、Polkadot、Dogecoin、Litecoin 等 15+ 条

  * L2 扩展层/侧链：Polygon、Arbitrum One、Optimism、Base、Worldchain、Unichain、Noble 等 7+ 条


**💱****稳定币支持**

  * USDC（Circle 发行的美元稳定币）与 EURC（Circle 发行的欧元稳定币）：均支持 Solana、Ethereum、Polygon 等网络

  * USDT（Tether 发行的美元稳定币）：支持 Solana、Ethereum、Tron 等网络

  * EURe（Monerium 发行的欧元稳定币）：支持 Polygon 网络

  * PYUSD（PayPal 发行的美元稳定币）和 USDP（Paxos 发行的美元稳定币）待 MiCA 政策明确后支持




企业级稳定币服务（Virtual Accounts）目前正式支持 Solana、Ethereum、Polygon 三个网络，Base、Arbitrum、Optimism、Tron、Stellar 需单独申请开通。

**🔄****加密资产与兑换能力**

支持 170 种加密资产，提供 2,000+ 个 Swap 交易对。兑换功能（Convert）通过集成第三方 DeFi 聚合器（swaps.xyz、Jupiter、Codex）实现，支持跨链代币兑换（如 BTC 兑换 ETH），用户无需使用第三方跨链转账工具。

### （二）法币通道与区域覆盖

**💵****法币出入金覆盖**

  * 入金：覆盖 180+ 国家/地区，支持 USD、EUR、GBP、CAD、AUD、BRL、MXN 等多种法币

  * 出金：覆盖多个国家/地区，支持银行卡（Visa、Mastercard）、银行转账、PayPal、Venmo 等方式


**📍****区域通道覆盖**

**⚠️****说明：** 各国加密货币监管政策存在差异且可能发生变化，出入金可用性受牌照覆盖和当地法规影响，使用前建议确认当地合规要求。

## **四、安全与托管**

**🏦****（一）托管模式**

采用非托管（Non-custodial）模式，不持有客户购买的加密资产。资产直接转入用户指定的钱包地址。如用户通过 MoonPay 创建钱包，私钥仅用户可访问，MoonPay 员工无法接触。

**💡****提示：** 即使 MoonPay 账户被禁用，用户仍可通过导出恢复短语在其他钱包恢复资产。

**🔐****（二）数据加密与安全措施**

  * 传输加密：TLS 1.2+

  * 静态加密：AES-256 加密（静态数据加密）

  * 支付信息：按 PCI DSS 标准处理和存储

  * 内部控制：公司设备 MDM（移动设备管理）管理、全员强制 SSO（单点登录）与 MFA（多因素认证）、入职前背景调查、定期安全培训

  * 安全开发：代码变更强制 Code Review、SAST（静态应用安全测试）、第三方组件自动更新、安全 SDLC（软件开发生命周期）


**🐞****（三）漏洞管理与审计**

  * 漏洞赏金：通过 HackerOne 平台运营 Bug Bounty 计划

  * 智能合约审计：MoonPay Commerce（原 Helio）链上支付合约已通过 Ackee Blockchain 安全审计

  * 合规工具：使用 Vanta 平台管理 500+ 供应商的日常安全审查

  * 状态监控：覆盖 240 个组件，支持订阅通知




**⚠️****通用风险提示：** 链上交易不可逆，转账前需仔细核对钱包地址；私钥或恢复短语丢失将导致资产永久无法找回。

## **五、生态集成与商户服务**

**🤝****（一）合作伙伴生态**

集成平台约 500 家。采用收入分成（Revenue Sharing）合作模式，合作伙伴从用户通过 MoonPay Widget 完成的交易中获得收入分成，MoonPay 承担所有退款和欺诈成本。

代表性合作伙伴：MetaMask、Phantom、Trust Wallet、Ledger、Exodus、Bitcoin.com（钱包/交易所）；OpenSea、Uniswap（NFT/DEX）；Shopify（电商）；Mastercard（支付网络，2025 年 5 月合作推出稳定币支付卡，覆盖 Mastercard 全球商户网络，持卡人消费时稳定币实时转换为法币；同时支持企业向承包商和零工工作者提供稳定币发放。该合作基于 Iron 稳定币基础设施）。

**🛠️****（二）开发者工具**

  * API：RESTful API，覆盖 On-Ramp、Off-Ramp、Virtual Accounts、Commerce 全产品线，通过 currencyCode 参数统一指定不同币种和网络

  * SDK：Web（JavaScript）、React、Node.js、React Native、iOS、Android 等多平台 SDK

  * Widget 集成：两步脚本嵌入即可完成基础集成，支持浮层（overlay）、内嵌（embedded）、侧边栏（drawer）、标签页（tab）、新窗口（window）五种布局模式，提供品牌主题定制（字体/颜色/边框）

  * Webhook：支持 HMAC-SHA256 签名验证，支持交易创建、状态变更、交易失败等事件通知

  * 沙盒环境：独立测试 API 密钥、Sepolia 测试网、测试信用卡、KYC 模拟

  * Shopify 插件：Solana Pay 官方 Shopify 插件（MoonPay Commerce 开发维护）


**🛒****（三）商户收款（MoonPay Commerce）**

原 Helio，已被 6,000+ 开发者、商户及企业使用。提供支付链接、Checkout Widget、订阅支付、自动出金等能力。支持 Solana、Bitcoin、Ethereum、Base、BNB Chain、Arbitrum、Polygon 等网络。

**🌉****（四）跨境稳定币服务（Iron）**

2025 年收购的稳定币基础设施平台 Iron，目前作为 MoonPay 面向企业客户的稳定币基础设施品牌运营。提供 API 驱动的虚拟账户、法币与稳定币出入金通道、跨境付款、合规处理和自动对账能力，服务对象包括 PSP（支付服务商）、金融科技公司、企业财务和钱包平台。支持 USD、EUR、GBP 法币通道，稳定币覆盖 USDC、USDT、PYUSD 等。

**💡****提示：** 跨境供应商付款或多币种资金调拨场景下，Iron 通常可缩短到账时间、减少中间环节，但具体取决于币种、网络和地区。

## **六、合规实施与数据保护**

**👤****（一）KYC/AML 实施**

  * KYC 分层：基础验证（邮箱 + 手机号）、标准验证（身份证件 + 自拍/活体检测 + 地址）、高级验证（资金来源证明 + 增强验证）

  * AML（反洗钱）措施：交易监控、可疑交易报告、分析公共区块链数据

  * 制裁筛查：对接 UN 制裁名单、US ITA 合并筛查名单、SEC EDGAR、OFAC 合规

  * Travel Rule（资金旅行规则）：超过适用门槛的交易，要求用户确认拥有并控制钱包


**🔏****（二）数据保护**

  * GDPR（欧盟通用数据保护条例）：隐私政策包含完整的数据控制者声明、DPO 联系方式、数据主体权利、跨境传输说明等

  * CCPA（加州消费者隐私法）：隐私政策包含专门的美国居民隐私声明

  * FCA 合规（英国）：实施新客 24 小时冷静期、适当性评估及风险警示


**⚠️****（三）监管风险提示**

**⚠️****说明：** 建议用户在使用前咨询专业法律和税务顾问，确认当地法规要求。加密货币价格波动较大，即使是稳定币也存在脱锚风险，用户应根据自身风险承受能力做出决策。

## **七、增值服务**

**📱****（一）MoonPay Wallet/App**

提供钱包应用（iOS 与 Android），支持 Bitcoin、Solana、Ethereum、Tron、XRP Ledger 等多链网络。功能涵盖法币购买、加密货币出售、跨链兑换（Swap）、质押（Staking）、发送/接收、MoonPay Balance（法币余额账户，目前支持美国、英国、欧盟用户）等。

**🎨****（二）NFT 功能**

  * NFT Checkout：支持通过信用卡、Apple Pay 等法币方式直接购买 NFT，覆盖多条区块链网络

  * HyperMint：无代码 NFT 铸造平台，为品牌提供 Web3 工具，合作品牌包括 Puma、Universal 等


**🏛️****（三）机构服务（MoonPay Trust Company）**

2025 年获得 NYDFS 授权的 Limited Purpose Trust Charter，可提供数字资产托管、OTC 交易和信托服务，面向机构和企业客户。

**🏦****（四）企业稳定币发行**

与 M0 平台集成，支持企业级自定义稳定币发行，覆盖发行、出入金、兑换、支付全价值链，目标市场包括美国、亚洲和拉丁美洲。

**💼****（五）稳定币薪资发放**

2026 年与全球薪资平台 Deel 达成合作，支持企业员工选择以稳定币形式接收全部或部分薪资，资金直接进入员工的非托管钱包。底层由 Iron 稳定币基础设施支持。首批覆盖英国和欧盟市场，美国市场计划后续跟进。

**🤖****（六）AI Agent 交易基础设施**

MoonPay Agents 为开发者提供 AI Agent 非托管钱包生成、法币入金、链上交易、跨链兑换、定期买入、法币出金等能力，兼容 x402 标准（机器间自动支付协议），提供 CLI 命令行工具。

## **八、适配场景分析**

**✅****适合使用 MoonPay 的场景**

  * **钱包/DApp 集成出入金** ：运营加密钱包、DApp（去中心化应用）或交易所的企业，如需为用户提供法币购买加密货币的能力，MoonPay 提供 Widget 嵌入式集成方案，采用收入分成模式。

  * **加密商户收款** ：经营线上商店或内容平台的商户，如需接受加密货币支付，MoonPay Commerce 支持多链收款并可自动兑换为法币入账至银行。

  * **企业跨境结算与稳定币收付** ：有跨境供应商付款、多币种资金调拨或团队薪资发放需求的企业，可通过 Virtual Accounts 和 Iron 获取企业级稳定币结算能力。

  * **法币-加密货币兑换需求** ：有法币与加密货币兑换需求的用户，MoonPay 支持多种支付方式，覆盖广泛的国家、法币与加密资产。MoonPay Balance 模式下平台服务费另有规则，以官方费率页面为准。

  * **机构托管与大额交易** ：机构投资者或企业客户如需合规的数字资产托管和 OTC 交易服务，MoonPay Trust Company 可提供数字资产托管和 OTC 交易服务。


**💡****决策建议**

选择加密支付基础设施服务商时，建议从业务场景匹配度、目标市场牌照覆盖、技术对接能力、托管模式偏好及费用条款等维度综合评估，并在签约前咨询专业法律和税务顾问。主要需要法币出入金通道的，可同时了解 Ramp、Transak 等方案；聚焦商户加密收款的，可对比 Coinbase Commerce、BitPay 等方案。

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

