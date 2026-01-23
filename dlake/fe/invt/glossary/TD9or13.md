# 汤姆·迪马克（Tom DeMark）TD序列（TD Sequential）技术指标分析

## 核心概念
汤姆·迪马克的TD序列是技术分析体系中的核心指标，旨在识别市场趋势的潜在转折点（抄底逃顶）。其核心思想基于左侧交易理念：“在市场恐惧中买入，在市场贪婪中卖出”。

---

## 一、核心构成与基本原理
TD序列是一个包含多个阶段的系统，主要分为两部分：

### 1. 准备期（Set up）—— “神奇九转”
- **定义**：要求连续9个交易日的收盘价，都低于（买入结构）或高于（卖出结构）其对应的4个交易日前的收盘价。
- **触发与显示逻辑**：
    - 计数从连续第6天满足条件时开始显示数字1-6。
    - 如果第7天依然满足条件，则显示7，否则前6天的序号消失。
    - 第8、9天逻辑相同，只有连续第9天满足条件时，完整的“九转结构”才成立。
- **结构类型**：
    - **买入结构（低九）**：在下跌趋势中形成，预示可能见底反弹。
    - **卖出结构（高九）**：在上涨趋势中形成，预示可能见顶回落。

### 2. 倒数期（Count down）—— 更精确的信号确认
- **定义**：在准备期完成后开始。
    - **买入结构**：从第9天起，每当某日的收盘价低于其2个交易日前的最低价时，计数增加1（计数日无需连续），累积达到13时发出强烈买入信号。
    - **卖出结构**：逻辑相反。
- **作用**：对准备期信号进行强化和确认，提高可靠性。

---

## 二、实战应用与优化
单纯依赖九转结构成功率有限，需结合以下条件优化：

### 1. 结合“完美”结构条件
- **买入结构**：第8或第9日的最低价应高于第6和第7日的最低价。
- **卖出结构**：第8或第9日的最高价应高于第6和第7日的最高价。

### 2. 与其他技术指标共振
- 与MACD背离、RSI等超买超卖震荡指标结合，过滤假信号。
- 只有当九转信号出现在超买或超卖区域时，才视为确认信号。

### 3. 多周期配合
- 例如：日线图出现“低9”买入结构时，若同时在120分钟图上出现“高9”卖出结构，则信号更可靠。

### 4. 适用场景与局限
- **适用市场**：震荡市、弱牛市及弱熊市中效果较好。
- **主要局限**：
    - 在单边大牛市或大熊市（极端行情）中容易失效。
    - 属于左侧预测指标，可能面临信号发出后市场仍延续原趋势的风险。

---

## 三、信号失效与取消机制

### 1. 准备期被取消
- 在计数完成前，出现以下情况之一则原计数作废：
    - 收盘价超过整个准备期内的最高价（对于买入结构）。
    - 出现一个相反方向的准备结构。

### 2. 倒数期被取消
- 在倒数完成前，出现以下情况之一则原倒数计数失效：
    - 出现反向的准备结构。
    - 出现一个新的、更强的同向准备结构（称为“再循环”），以新结构为准重新开始。

---

## 总结
TD序列是一个系统性的趋势拐点探测工具：
- “神奇九转”仅是其中的准备阶段。
- 完整应用需结合倒数计数、“完美”结构条件、其他技术工具及多周期验证。
- 需清醒认识其在大趋势行情中的局限性。
- 任何技术指标都非万能，严谨的规则和风险控制是关键。



----


Tom DeMark (TD) Sequential is a counter-trend indicator designed to identify the exact point of **trend exhaustion**.

Unlike moving averages or MACD, which follow the trend, TD Sequential is predictive. It attempts to mathematically determine when a trend has become overextended and is due for a reversal or a significant correction. It is famous for its "9" and "13" signals.

### The Core Concept: 9 and 13

The indicator operates in two distinct phases. You must complete the first phase (Setup) before the second phase (Countdown) can begin.

#### Phase 1: TD Setup (The "9")

This phase looks for a temporary correction or the start of a trend. It requires **9 consecutive candles**.

* **Buy Setup (Green 9):**
* Looks for a bottom.
* **Rule:** 9 *consecutive* closes that are **lower** than the close 4 bars earlier.
* **Trading Implication:** When the "9" prints, the market is often oversold. Traders expect a price bounce for 1–4 candles.


* **Sell Setup (Red 9):**
* Looks for a top.
* **Rule:** 9 *consecutive* closes that are **higher** than the close 4 bars earlier.
* **Trading Implication:** When the "9" prints, the market is often overbought. Traders expect a pullback.



> **Crucial Rule:** If the sequence is interrupted (e.g., bar 5 closes higher than 4 bars ago during a Buy Setup), the count resets to zero. It *must* be consecutive.

#### Phase 2: TD Countdown (The "13")

This phase looks for major trend exhaustion (the absolute top or bottom). It starts *after* a Setup (9) is completed.

* **Buy Countdown (13):**
* **Rule:** The close is **lower (or equal to)** the **low** 2 bars earlier.
* **Count:** You need 13 of these bars.
* **Non-Consecutive:** Unlike the Setup, these *do not* have to be consecutive. If the market goes sideways, the count pauses and resumes when the condition is met again.


* **Sell Countdown (13):**
* **Rule:** The close is **higher (or equal to)** the **high** 2 bars earlier.
* **Count:** You need 13 of these bars.



---

### How to Trade It

The signals are objective, but timing matters.

#### 1. Trading the "9" (Aggressive)

Traders often use the completion of a **Setup (9)** to scalp a quick reversal.

* **The Signal:** A Green 9 (Buy) or Red 9 (Sell) prints.
* **The "Perfection" Filter:** To increase accuracy, many traders wait for "Perfection."
* *Buy Perfection:* The low of bar 8 or 9 is lower than the low of bar 6 and 7.
* *Sell Perfection:* The high of bar 8 or 9 is higher than the high of bar 6 and 7.
* *Why?* This ensures the momentum was still pushing at the very end of the count before you fade it.



#### 2. Trading the "13" (Conservative)

The **Countdown (13)** is a stronger signal indicating the trend is "done."

* **The Signal:** The number 13 appears on the chart.
* **Risk:** Sometimes a strong trend will print a 13 and keep going (known as a "Gorilla" trend).
* **Confirmation:** Never trade a 13 blindly. Wait for a "Price Flip" (a candle that closes in the opposite direction) or a divergence in RSI to confirm the reversal.

#### 3. Stop Loss Management (TDST)

Tom DeMark suggests using the **TDST Level** for invalidation.

* **TDST Support/Resistance:** The true high or low of the *first* candle in the Setup (Bar 1).
* If you are buying a Green 9, but the price crashes through the TDST Support level established at the start of the count, the setup is failed/invalidated.

### Summary of Rules

| Feature | TD Setup | TD Countdown |
| --- | --- | --- |
| **Target Number** | **9** | **13** |
| **Goal** | Identify a pause/correction. | Identify major trend exhaustion. |
| **Comparison** | Close vs. Close (4 bars back). | Close vs. High/Low (2 bars back). |
| **Sequence** | Must be **Consecutive**. | Can be **Non-Consecutive**. |

### Psychology: Why it Works

TD Sequential works because it mathematically quantifies the "herd mentality."

* **The Setup (9)** catches the point where early traders are taking profit.
* **The Countdown (13)** catches the point where the last buyer has bought (or last seller has sold), leaving no one left to push the trend further.

**Would you like me to explain the "TD Combo," which is a faster version of this indicator, or help you find a script for this on TradingView?**