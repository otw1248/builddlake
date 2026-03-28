

# 中华人民共和国国家标准

GB/T 32918.1—2016

# 信息安全技术  SM2 椭圆曲线公钥密码算法 第 1 部分: 总则

# Information security technology—

# Public key cryptographic algorithm SM2 based on elliptic curves—Part 1: General

2016-08-29 发布

2017-03-01 实施

## 目次

前言 …… I  
引言 …… II  
1 范围 …… 1  
2 符号和缩略语 …… 1  
3 域和椭圆曲线 …… 2  
3.1 有限域 …… 2  
3.2 有限域上的椭圆曲线 …… 3  
4 数据类型及其转换 …… 5  
4.1 数据类型 …… 5  
4.2 数据类型转换 …… 5  
5 椭圆曲线系统参数及其验证 …… 8  
5.1 一般要求 …… 8  
5.2  $ F_{p} $  上椭圆曲线系统参数及其验证 …… 8  
5.3  $ F_{2^{m}} $  上椭圆曲线系统参数及其验证 …… 9  
6 密钥对的生成与公钥的验证 …… 9  
6.1 密钥对的生成 …… 9  
6.2 公钥的验证 …… 10  
附录 A（资料性附录）关于椭圆曲线的背景知识 …… 11  
A.1 素域  $ F_{p} $  …… 11  
A.2 二元扩域  $ F_{2^{m}} $  …… 13  
A.3 椭圆曲线多倍点运算 …… 23  
A.4 求解椭圆曲线离散对数问题的方法 …… 26  
A.5 椭圆曲线上点的压缩 …… 27  
附录 B（资料性附录）数论算法 …… 29  
B.1 有限域和模运算 …… 29  
B.2 有限域上的多项式 …… 33  
B.3 椭圆曲线算法 …… 35  
附录 C（资料性附录）曲线示例 …… 37  
C.1 一般要求 …… 37  
C.2  $ F_{p} $  上椭圆曲线 …… 37  
C.3  $ F_{2^{m}} $  上椭圆曲线 …… 37  
附录 D（资料性附录）椭圆曲线方程参数的拟随机生成及验证 …… 39  
D.1 椭圆曲线方程参数的拟随机生成 …… 39  
D.2 椭圆曲线方程参数的验证 …… 40  
参考文献 …… 41

## 前言

GB/T 32918《信息安全技术 SM2 椭圆曲线公钥密码算法》分为以下 5 个部分：

——第1部分:总则;

——第2部分:数字签名算法;

——第3部分：密钥交换协议；

——第4部分：公钥加密算法；

——第5部分:参数定义。

本部分为 GB/T 32918 的第 1 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

本部分由国家密码管理局提出。

本部分由全国信息安全标准化技术委员会(SAC/TC 260)归口。

本部分起草单位:北京华大信安科技有限公司、中国人民解放军信息工程大学、中国科学院数据与通信保护研究教育中心。

本部分主要起草人：陈建华、祝跃飞、叶顶峰、胡磊、裴定一、彭国华、张亚娟、张振峰。

## 引言

N.Koblitz 和 V.Miller 在 1985 年各自独立地提出将椭圆曲线应用于公钥密码系统。椭圆曲线公钥密码所基于的曲线性质如下：

——有限域上椭圆曲线在点加运算下构成有限交换群，且其阶与基域规模相近；

——类似于有限域乘法群中的乘幂运算，椭圆曲线多倍点运算构成一个单向函数。

在多倍点运算中，已知多倍点与基点，求解倍数的问题称为椭圆曲线离散对数问题。对于一般椭圆曲线的离散对数问题，目前只存在指数级计算复杂度的求解方法。与大数分解问题及有限域上离散对数问题相比，椭圆曲线离散对数问题的求解难度要大得多。因此，在相同安全程度要求下，椭圆曲线密码较其他公钥密码所需的密钥规模要小得多。

SM2 是国家密码管理局组织制定并提出的椭圆曲线密码算法标准。GB/T 32918 的主要目标如下：

——GB/T 32918.1 定义和描述了 SM2 椭圆曲线密码算法的相关概念及数学基础知识，并概述了

该部分同其他部分的关系。

——GB/T 32918.2 描述了一种基于椭圆曲线的签名算法，即 SM2 签名算法。

——GB/T 32918.3 描述了一种基于椭圆曲线的密钥交换协议，即 SM2 密钥交换协议。

——GB/T 32918.4 描述了一种基于椭圆曲线的公钥加密算法，即 SM2 加密算法，该算法需使用 GB/T 32905—2016 定义的 SM3 密码杂凑算法。

——GB/T 32918.5 给出了 SM2 算法使用的椭圆曲线参数，以及使用椭圆曲线参数进行 SM2 运算的示例结果。

本部分为 GB/T 32918 的第 1 部分，描述了必要的数学基础知识与一般技术，以帮助实现其他各部分所规定的密码机制。

# 信息安全技术  SM2 椭圆曲线公钥密码算法 第 1 部分: 总则

## 1 范围

GB/T 32918 的本部分规定了 SM2 椭圆曲线公钥密码算法涉及的必要数学基础知识与相关密码技术，以帮助实现其他各部分所规定的密码机制。

本部分适用于基域为素域和二元扩域的椭圆曲线公钥密码算法的设计、开发、使用。

## 2 符号和缩略语


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">下列符号和缩略语适用于本文件。</td></tr><tr><td style='text-align: center;'>B</td><td style='text-align: center;'>MOV 阈。正数 B，使得求取  $ F_{q^{B}} $  上的离散对数至少与求取  $ F_{q} $  上的椭圆曲线离散对数一样困难。</td></tr><tr><td style='text-align: center;'>deg(f)</td><td style='text-align: center;'>多项式  $ f(x) $  的次数。</td></tr><tr><td style='text-align: center;'>E</td><td style='text-align: center;'>有限域上由 a 和 b 定义的一条椭圆曲线。</td></tr><tr><td style='text-align: center;'>E(F_{q})</td><td style='text-align: center;'>$ F_{q} $  上椭圆曲线 E 的所有有理点（包括无穷远点 O）组成的集合。</td></tr><tr><td style='text-align: center;'>ECDLP</td><td style='text-align: center;'>椭圆曲线离散对数问题。</td></tr><tr><td style='text-align: center;'>$ F_{p} $</td><td style='text-align: center;'>包含 p 个元素的素域。</td></tr><tr><td style='text-align: center;'>$ F_{q} $</td><td style='text-align: center;'>包含 q 个元素的有限域。</td></tr><tr><td style='text-align: center;'>$ F_{q}^{*} $</td><td style='text-align: center;'>由  $ F_{q} $  中所有非零元构成的乘法群。</td></tr><tr><td style='text-align: center;'>$ F_{2^{m}} $</td><td style='text-align: center;'>包含  $ 2^{m} $  个元素的二元扩域。</td></tr><tr><td style='text-align: center;'>G</td><td style='text-align: center;'>椭圆曲线的一个基点，其阶为素数。</td></tr><tr><td style='text-align: center;'>gcd(x,y)</td><td style='text-align: center;'>x 和 y 的最大公因子。</td></tr><tr><td style='text-align: center;'>h</td><td style='text-align: center;'>余因子， $ h=\#E(F_{q})/n $ ，其中 n 是基点 G 的阶。</td></tr><tr><td style='text-align: center;'>LeftRotate()</td><td style='text-align: center;'>循环左移运算。</td></tr><tr><td style='text-align: center;'>$ l_{\text{max}} $</td><td style='text-align: center;'>余因子 h 的最大素因子的上界。</td></tr><tr><td style='text-align: center;'>m</td><td style='text-align: center;'>二元扩域  $ F_{2^{m}} $  关于  $ F_{2} $  的扩张次数。</td></tr><tr><td style='text-align: center;'>modf(x)</td><td style='text-align: center;'>模多项式  $ f(x) $  的运算。若  $ f(x) $  是二元域上的多项式，则所有系数执行模 2 运算。</td></tr><tr><td style='text-align: center;'>mod n</td><td style='text-align: center;'>模 n 运算。例如，23 mod 7=2。</td></tr><tr><td style='text-align: center;'>n</td><td style='text-align: center;'>基点 G 的阶 [n 是  $ \#E(F_{q}) $  的素因子]。</td></tr><tr><td style='text-align: center;'>O</td><td style='text-align: center;'>椭圆曲线上的一个特殊点，称为无穷远点或零点，是椭圆曲线加法群的单位元。</td></tr><tr><td style='text-align: center;'>P</td><td style='text-align: center;'>$ P=(x_{P},y_{P}) $  是椭圆曲线上除 O 之外的一个点，其坐标  $ x_{P},y_{P} $  满足椭圆曲线方程。</td></tr><tr><td style='text-align: center;'>$ P_{1}+P_{2} $</td><td style='text-align: center;'>椭圆曲线 E 上两个点  $ P_{1} $  与  $ P_{2} $  的和。</td></tr><tr><td style='text-align: center;'>p</td><td style='text-align: center;'>大于 3 的素数。</td></tr><tr><td style='text-align: center;'>q</td><td style='text-align: center;'>有限域  $ F_{q} $  中元素的数目。</td></tr></table>

a, b

 $ F_{q} $  中的元素，它们定义  $ F_{q} $  上的一条椭圆曲线 E。

 $ r_{\min} $  基点 G 的阶 n 的下界。

 $ \operatorname{Tr}() $  迹函数。

 $ x_{P} $  点 P 的 x 坐标。

 $ x^{-1} \mod n $  使得  $ x \cdot y \equiv 1 \pmod{n} $  成立的唯一整数  $ y, 1 \leqslant y \leqslant n-1, \gcd(x, n)=1 $ 。

 $ x \parallel y $  x 与 y 的拼接，其中 x 和 y 是比特串或字节串。

 $ x \equiv y \pmod{n} $  x 与 y 模 n 同余。亦即， $ x \mod n = y \mod n $ 。

 $ y_{P} $  点 P 的 y 坐标。

 $ \widetilde{y}_{P} $   $ y_{P} $  的点压缩表示。

 $ Z_{p} $  整数模 p 的剩余类环。

 $ \langle G \rangle $  基点 G 生成的循环群。

[k] P 椭圆曲线上点 P 的 k 倍点，即： $ [k] P = P + P + \cdots + P $ ，其中 k 是正整数。

[x, y] 大于或等于 x 且小于或等于 y 的整数的集合。

 $ \left\lfloor x \right\rfloor $  顶函数，大于或等于 x 的最小整数。例如， $ \left\lfloor 7 \right\rfloor = 7, \left\lfloor 8.3 \right\rfloor = 9 $ 。

 $ \left\lfloor x \right\rfloor $  底函数，小于或等于 x 的最大整数。例如， $ \left\lfloor 7 \right\rfloor = 7, \left\lfloor 8.3 \right\rfloor = 8 $ 。

 $ \# E(F_{q}) $   $ E(F_{q}) $  上点的数目，称为椭圆曲线  $ E(F_{q}) $  的阶。

 $ \oplus $  长度相等的两个比特串按比特的异或运算。

## 3 域和椭圆曲线

### 3.1 有限域

#### 3.1.1 概述

本条给出有限域  $ F_{q} $  的描述及其元素的表示，q 是一个奇素数或者是 2 的方幂。当 q 是奇素数 p 时，要求  $ p > 2^{191} $ ；当 q 是 2 的方幂  $ 2^{m} $  时，要求 m > 192 且为素数。

#### 3.1.2 素域  $ F_{p} $ 

当 q 是奇素数 p 时，素域  $ F_{p} $  中的元素用整数 0, 1, 2, …, p-1 表示。素域特性如下：

a） 加法单位元是整数 0；

b）乘法单位元是整数1；

c) 域元素的加法是整数的模 p 加法，即若  $ a, b \in F_{p} $ ，则  $ a + b = (a + b) \mod p $ ；

d）域元素的乘法是整数的模 p 乘法，即若  $ a, b \in F_{p} $ ，则  $ a \cdot b = (a \cdot b) \bmod p $ 。

#### 3.1.3 二元扩域  $ F_{2^{m}} $ 

当 q 是 2 的方幂  $ 2^{m} $  时，二元扩域  $ F_{2^{m}} $  可以看成  $ F_{2} $  上的 m 维向量空间，其元素可用长度为 m 的比特串表示。

 $ F_{2^{m}} $  中的元素有多种表示方法，其中最常用的两种方法是多项式基(PB)表示(参见 A.2.1.1)和正规基(NB)表示(参见 A.2.1.3)。基的选择原则是使得  $ F_{2^{m}} $  中的运算效率尽可能高。本部分并不规定基的选择。下面以多项式基表示为例说明二元扩域  $ F_{2^{m}} $ 。

设  $ F_{2} $  上 m 次不可约多项式  $ f(x)=x^{m}+f_{m-1}x^{m-1}+\cdots+f_{2}x^{2}+f_{1}x+f_{0} $  （其中  $ f_{i}\in F_{2}, i=0,1,\cdots,m-1 $ ）是二元扩域  $ F_{2^{m}} $  的约化多项式。 $ F_{2^{m}} $  由  $ F_{2} $  上所有次数低于 m 的多项式构成。多项式集合  $ \left\{x^{m-1}, x^{m-2}, \cdots, x, 1\right\} $  是  $ F_{2^{m}} $  在  $ F_{2} $  上的一组基，称为多项式基。 $ F_{2^{m}} $  中的任意一个元素  $ a(x)= $ 

 $ a_{m-1}x^{m-1}+a_{m-2}x^{m-2}+\cdots+a_{1}x+a_{0} $  在  $ F_{2} $  上的系数恰好构成了长度为 m 的比特串，用  $ a=(a_{m-1}, a_{m-2}, \cdots, a_{1}, a_{0}) $  表示。多项式域特性如下：

a）零元 0 用全 0 比特串表示；

b）乘法单位元 1 用比特串 00…001 表示；

c) 两个域元素的加法为比特串的按比特异或运算；

d）域元素 a 和 b 的乘法定义如下：设 a 和 b 对应的  $ F_{2} $  上多项式为  $ a(x) $  和  $ b(x) $ ，则  $ a \cdot b $  定义为多项式  $ (a(x)b(x)) \bmod f(x) $  对应的比特串。

### 3.2 有限域上的椭圆曲线

有限域  $ F_{q} $  上的椭圆曲线是由点组成的集合。在仿射坐标系下，椭圆曲线上点 P（非无穷远点）的坐标表示为  $ P=(x_{P},y_{P}) $ ，其中  $ x_{P},y_{P} $  为满足一定方程的域元素，分别称为点 P 的 x 坐标和 y 坐标。在本部分中，称  $ F_{q} $  为基域。

关于椭圆曲线更多的背景知识,参见附录 A 中 A.1 和 A.2。

在本部分中，如果不做特别说明，椭圆曲线上的点均采用仿射坐标表示。

#### 3.2.1 $ F_{p} $  上的椭圆曲线

定义在  $ F_{p}(p $  是大于 3 的素数) 上的椭圆曲线方程为：

 $$ y^{2}=x^{3}+ax+b,a,b\in F_{p}, 且 (4a^{3}+27b^{2})\bmod p\ne0。\cdots\cdots\cdots\cdots\cdots\cdots\cdots(1) $$ 

椭圆曲线  $ E(F_{p}) $  定义为，参见 C.2：

 $ E(F_{p})=\left\{(x,y)\mid x,y\in F_{p}\right\} $ ，且满足方程(1) $ \bigcup\{O\} $ ，其中O是无穷远点。

椭圆曲线  $ E(F_{p}) $  上的点的数目用  $ \#E(F_{p}) $  表示，称为椭圆曲线  $ E(F_{p}) $  的阶。

#### 3.2.2 $ F_{2^{m}} $  上的椭圆曲线

定义在  $ F_{2^{m}} $  上的椭圆曲线方程为：

 $$ y^{2}+xy=x^{3}+ax^{2}+b,a,b\in F_{2^{m}}, 且 b\ne0。 $$ 

椭圆曲线  $ E(F_{2^{m}}) $  定义为，参见 C.3：

 $ E(F_{2^{m}})=\left\{(x,y)\mid x,y\in F_{2^{m}}\right\} $  ,且满足方程(2) $ \bigcup\{O\} $  ,其中O是无穷远点。

椭圆曲线  $ E(F_{2^{m}}) $  上的点的数目用  $ \#E(F_{2^{m}}) $  表示，称为椭圆曲线  $ E(F_{2^{m}}) $  的阶。

#### 3.2.3 椭圆曲线群

##### 3.2.3.1 $ F_{p} $  上的椭圆曲线群

椭圆曲线  $ E(F_{p}) $  上的点按照下面的加法运算规则，构成一个交换群：

a） $ O+O=O; $ 

b)  $ \forall P=(x,y)\in E(F_{p})\backslash\{O\},P+O=O+P=P; $ 

c)  $ \forall P=(x,y)\in E(F_{p})\backslash\{O\} $ ，P 的逆元素  $ -P=(x,-y) $ ， $ P+(-P)=O $ ；

d）两个非互逆的不同点相加的规则：

设  $ P_{1}=(x_{1},y_{1})\in E(F_{p})\backslash\{O\},P_{2}=(x_{2},y_{2})\in E(F_{p})\backslash\{O\} $ ，且  $ x_{1}\neq x_{2} $ 

设  $ P_{3}=(x_{3},y_{3})=P_{1}+P_{2} $ ，则

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}-x_{1}-x_{2},\\ y_{3}=&\lambda\left(x_{1}-x_{3}\right)-y_{1},\end{aligned}\right. $$ 

式中：

 $$ \lambda=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}； $$ 

e) 倍点规则：

设  $ P_{1}=(x_{1},y_{1})\in E(F_{p})\backslash\{O\} $ ，且  $ y_{1}\neq0,P_{3}=(x_{3},y_{3})=P_{1}+P_{1} $ ，则

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}-2x_{1},\\ y_{3}=&\lambda\left(x_{1}-x_{3}\right)-y_{1},\end{aligned}\right. $$ 

式中：

 $$ \lambda=\frac{3x_{1}^{2}+a}{2y_{1}}。 $$ 

##### 3.2.3.2 $ F_{2^{m}} $  上的椭圆曲线群

椭圆曲线  $ E(F_{2^{m}}) $  上的点按照下面的加法运算规则，构成一个交换群：

a)  $ O+O=O; $ 

b)  $ \forall P=(x,y)\in E(F_{2^{m}})\setminus\{O\},P+O=O+P=P; $ 

c)  $ \forall P=(x,y)\in E(F_{2^{m}})\backslash\{O\} $ ，P 的逆元素  $ -P=(x,x+y) $ ， $ P+(-P)=O $ ；

d）两个非互逆的不同点相加的规则：

设  $ P_{1}=(x_{1},y_{1})\in E(F_{2^{m}})\backslash\{O\},P_{2}=(x_{2},y_{2})\in E(F_{2^{m}})\backslash\{O\} $ ，且  $ x_{1}\neq x_{2} $ 

设  $ P_{3}=(x_{3},y_{3})=P_{1}+P_{2} $ ，则

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}+\lambda+x_{1}+x_{2}+a,\\ y_{3}=&\lambda\left(x_{1}+x_{3}\right)+x_{3}+y_{1},\end{aligned}\right. $$ 

式中：

 $$ \lambda=\frac{y_{1}+y_{2}}{x_{1}+x_{2}}； $$ 

e) 倍点规则：

设  $ P_{1}=(x_{1},y_{1})\in E(F_{2^{m}})\backslash\{O\} $ ，且  $ x_{1}\neq0,P_{3}=(x_{3},y_{3})=P_{1}+P_{1} $ ，则

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}+\lambda+a,\\ y_{3}=&x_{1}^{2}+(\lambda+1)x_{3},\end{aligned}\right. $$ 

式中：

 $$ \lambda=x_{1}+\frac{y_{1}}{x_{1}}。 $$ 

#### 3.2.4 椭圆曲线多倍点运算

椭圆曲线上同一个点的多次加称为该点的多倍点运算。设 k 是一个正整数，P 是椭圆曲线上的点，称点 P 的 k 次加为点 P 的 k 倍点运算，记为  $ Q = [k] P = \underbrace{P + P + \cdots + P}_{k} $ 。因为  $ [k] P = [k - 1] P + P $ ，所以 k 倍点可以递归求得。

多倍点运算的输出有可能是无穷远点 O。

多倍点运算也可以通过一些技巧更有效地实现，参见附录 A 中 A.3。

#### 3.2.5 椭圆曲线离散对数问题(ECDLP)

已知椭圆曲线  $ E(F_{q}) $  、阶为 n 的点  $ G \in E(F_{q}) $  及  $ Q \in \langle G \rangle $  ，椭圆曲线离散对数问题是指确定整数  $ l \in [0, n-1] $ ，使得 Q = [l] G 成立。

椭圆曲线离散对数问题关系到椭圆曲线密码系统的安全，因此应选择安全的椭圆曲线。关于如何选择安全椭圆曲线，参见附录 A 中 A.4。

#### 3.2.6 弱椭圆曲线

若某椭圆曲线存在优于 $ n^{1/2} $ 级(n是基点的阶)计算复杂度的攻击方法，则称此曲线为弱椭圆曲线。在本部分中禁止使用弱椭圆曲线。

 $ F_{q} $ 上的超奇异曲线[有限域 $ F_{q} $ 的特征整除 $ q+1-\#E(F_{q}) $ ]和 $ F_{p} $ 上的异常(Anomalous)曲线 $ \left[\#E(F_{p})=p\right] $ 都是弱椭圆曲线。

## 4 数据类型及其转换

### 4.1 数据类型

在本部分中，数据类型包括比特串、字节串、域元素、椭圆曲线上的点和整数。

比特串：有序的 0 和 1 的序列。

字节串：有序的字节序列，其中8比特为1个字节。

域元素：有限域  $ F_{q} $  中的元素。

椭圆曲线上的点：椭圆曲线上的点  $ P \in E(F_{q}) $ ，或者是一对域元素  $ (x_{P}, y_{P}) $ ，其中域元素  $ x_{P} $  和  $ y_{P} $  满足椭圆曲线方程，或者是无穷远点 O。

点的字节串表示有多种形式，用一个字节 PC 加以标识。无穷远点 O 的字节串表示是单一的零字节 PC=00。非无穷远点  $ P=(x_{P},y_{P}) $  有如下三种字节串表示形式：

a）压缩表示形式，PC=02 或 03；

b）未压缩表示形式，PC=04；

c）混合表示形式，PC=06 或 07。

注：混合表示形式既包含压缩表示形式又包含未压缩表示形式。在实现中，它允许转换到压缩表示形式或者未压缩表示形式。

对于椭圆曲线上点的压缩表示形式和混合表示形式，本部分中定为可选形式。椭圆曲线上点的压缩表示形式参见附录 A 中 A.5。

### 4.2 数据类型转换

#### 4.2.1 数据类型转换关系

图 1 提供了各种数据类型之间的转换关系, 线上的标志是相应数据转换方法所在的条。

<div style="text-align: center;"><img src="imgs/img_in_image_box_280_1160_908_1454.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 1 数据类型和转换约定</div>


#### 4.2.2 整数到字节串的转换

输入:非负整数 x，以及字节串的目标长度 k（其中 k 满足  $ 2^{8k} > x $ ）。

输出: 长度为 k 的字节串 M。

a）设  $ M_{k-1}, M_{k-2}, \cdots, M_{0} $  是 M 的从最左边到最右边的字节；

b）M 的字节满足：

 $$ x=\sum_{i=0}^{k-1}2^{8i}M_{i}。 $$ 

#### 4.2.3 字节串到整数的转换

输入: 长度为 k 的字节串 M。

输出: 整数 x。

a）设  $ M_{k-1}, M_{k-2}, \cdots, M_{0} $  是 M 的从最左边到最右边的字节；

b）将 M 转换为整数 x :

 $$ x=\sum_{i=0}^{k-1}2^{8i}M_{i}。 $$ 

#### 4.2.4 比特串到字节串的转换

输入: 长度为 m 的比特串 s。

输出: 长度为 k 的字节串 M, 其中  $ k = \left\lceil m / 8 \right\rceil $ 。

a）设  $ s_{m-1}, s_{m-2}, \cdots, s_{0} $  是 s 从最左边到最右边的比特；

b) 设  $ M_{k-1}, M_{k-2}, \cdots, M_{0} $  是 M 从最左边到最右边的字节，则

 $ M_{i}=s_{8i+7}s_{8i+6}\cdots s_{8i+1}s_{8i} $ ，其中 $ 0\leqslant i<k $ ，当 $ 8i+j\geqslant m,0<j\leqslant7 $ 时， $ s_{8i+j}=0 $ 。

#### 4.2.5 字节串到比特串的转换

输入: 长度为 k 的字节串 M。

输出: 长度为 m 的比特串 s，其中 m = 8k。

a）设  $ M_{k-1}, M_{k-2}, \cdots, M_{0} $  是 M 从最左边到最右边的字节；

b）设  $ s_{m-1}, s_{m-2}, \cdots, s_{0} $  是 s 从最左边到最右边的比特，则  $ s_{i} $  是  $ M_{j} $  右起第  $ i - 8j + 1 $  比特，其中  $ j = \left\lfloor i / 8 \right\rfloor $ 。

#### 4.2.6 域元素到字节串的转换

输入： $ F_{q} $  中的元素  $ \alpha $ 。

输出：长度  $ l=\left\lceil t/8 \right\rceil $  的字节串 S，其中  $ t=\left\lceil \log_{2} q \right\rceil $ 。

a）若 q 为奇素数，则  $ \alpha $  必为区间  $ [0, q-1] $  中的整数，按 4.2.2 的方法把  $ \alpha $  转换成长度为 l 的字节串 S；

b）若  $ q=2^{m} $ ，则  $ \alpha $  必为长度为 m 的比特串，按 4.2.4 的方法把  $ \alpha $  转换成长度为 l 的字节串 S。

#### 4.2.7 字节串到域元素的转换

输入: 基域  $ F_{q} $  的类型, 长度为  $ l=\left\lceil t/8 \right\rceil $  的字节串 S, 其中  $ t=\left\lceil \log_{2} q \right\rceil $ 。

输出： $ F_{q} $  中的元素  $ \alpha $ 。

a）若 q 是奇素数，则按 4.2.3 的方法将 S 转换为整数  $ \alpha $ ，若  $ \alpha \notin [0, q-1] $ ，则报错；

b）若  $ q=2^{m} $ ，则按 4.2.5 的方法将 S 转换为长度为 m 的比特串  $ \alpha $ 。

#### 4.2.8 域元素到整数的转换

输入: 域  $ F_{q} $  中的元素  $ \alpha $ 。

输出: 整数 x。

a）若 q 为奇素数，则  $ x=\alpha $ （不需要转换）；

b）若  $ q=2^{m} $ ，则  $ \alpha $  必为长度为 m 的比特串，设  $ s_{m-1}, s_{m-2}, \cdots, s_{0} $  是  $ \alpha $  的从最左边到最右边的比特，将  $ \alpha $  转化为整数 x：

 $$ x=\sum_{i=0}^{m-1}2^{i}s_{i}。 $$ 

#### 4.2.9 点到字节串的转换

输入:椭圆曲线上的点  $ P=(x_{P},y_{P}) $  ，且  $ P\neq O $  。

输出：字节串 S。若选用未压缩表示形式或混合表示形式，则输出字节串长度为  $ 2l+1 $ ；若选用压缩表示形式，则输出字节串长度为  $ l+1(l=\left[\left(\log_{2}q\right)/8\right] $ 。

a）按 4.2.6 中的方法把域元素  $ x_{p} $  转换成长度为 l 的字节串  $ X_{1} $ ;

b) 若选用压缩表示形式，则：

1）计算比特  $ \widetilde{y}_{P} $  (参见附录 A 中 A.5);

2）若  $ \widetilde{y}_{P}=0 $ ，则令 PC=02；若  $ \widetilde{y}_{P}=1 $ ，则令 PC=03；

3） 字节串  $ S=PC \parallel X_{1} $  ；

c) 若选用未压缩表示形式，则：

1）按 4.2.6 的方法把域元素  $ y_{p} $  转换成长度为 l 的字节串  $ Y_{1} $ ;

2）令 PC=04；

3） 字节串  $ S=PC \parallel X_{1} \parallel Y_{1} $  ；

d）若选用混合表示形式，则：

1）按 4.2.6 的方法把域元素  $ y_{p} $  转换成长度为 l 的字节串  $ Y_{1} $ ;

2）计算比特 $ \widetilde{y}_{P} $ （参见附录A中A.5）；

3）若  $ \widetilde{y}_{P}=0 $ ，则令 PC=06；若  $ \widetilde{y}_{P}=1 $ ，则令 PC=07；

4） 字节串  $ S=PC \parallel X_{1} \parallel Y_{1} $  。

#### 4.2.10 字节串到点的转换

输入: 定义  $ F_{q} $  上椭圆曲线的域元素 a, b, 字节串 S。若选用未压缩表示形式或混合表示形式, 则字节串 S 长度为  $ 2l + 1 $ ; 若选用压缩表示形式, 则字节串 PO 长度为  $ l + 1 (l = \left[\frac{\log_{2}q}{8}\right] $ 。

输出:椭圆曲线上的点  $ P=(x_{P},y_{P}) $  ，且  $ P\neq O $  。

a）若选用压缩表示形式，则  $ S = PC \parallel X_{1} $ ；若选用未压缩表示形式或混合表示形式，则  $ S = PC \parallel X_{1} \parallel Y_{1} $ ，其中 PC 是单一字节， $ X_{1} $  和  $ Y_{1} $  都是长度为 l 的字节串；

b）按4.2.7的方法把字节串 $ X_{1} $ 转换成域元素 $ x_{p} $ ;

c）若选用压缩表示形式，则：

1）检验 PC=02 或者是 PC=03，若不是这种情形，则报错；

2）若 PC=02，则令  $ \widetilde{y}_{P}=0 $ ；若 PC=03，则令  $ \widetilde{y}_{P}=1 $ ；

3）将 $ (x_{P},\widetilde{y}_{P}) $ 转换为椭圆曲线上的一个点 $ (x_{P},y_{P}) $ （参见附录A中A.5）；

d）若选用未压缩表示形式，则：

1）检验 PC=04，若不是这种情形，则报错；

2）按 4.2.7 的方法把字节串  $ Y_{1} $  转换成域元素  $ y_{p} $ ;

e）若选用混合表示形式，则：

1）检验 PC=06 或者 PC=07，若不是这种情形，则报错；

2）执行步骤如下：

——按 4.2.7 的细节把字节串  $ Y_{1} $  转换成域元素  $ y_{p} $ ;

——若 PC=06，则令  $ \widetilde{y}_{P}=0 $ ，否则令  $ \widetilde{y}_{P}=1 $ ；

3) 将 $ (x_{P},\widetilde{y}_{P}) $ 转换为椭圆曲线上的一个点 $ (x_{P},y_{P}) $ （参见附录A中A.5）；

f）若 q 为奇素数，则验证  $ y_{P}^{2} \equiv y_{P}^{3} + ax_{P} + b \pmod{q} $ ，若不是这种情形，则报错；

若  $ q=2^{m} $ ，则在  $ F_{2^{m}} $  中验证  $ y_{P}^{2}+x_{P}y_{P}=x_{P}^{3}+ax_{P}^{2}+b $ ，若不是这种情形，则报错；

g)  $  P = (x_{P}, y_{P})  $ 

## 5 椭圆曲线系统参数及其验证

### 5.1 一般要求

椭圆曲线系统参数是可以公开的，系统的安全性不依赖于对这些参数的保密。本部分不规定椭圆曲线系统参数的生成方法，但规定了系统参数的验证方法。椭圆曲线阶的计算和基点的选取方法可参见附录 B 中 B.3，曲线参数的生成方法可参见附录 D。

椭圆曲线系统参数按照基域的不同可以分为两种情形：

——当基域是  $ F_{p}(p $  为大于 3 的素数) 时， $ F_{p} $  上的椭圆曲线系统参数；

——当基域是 $ F_{2^{m}} $ 时， $ F_{2^{m}} $ 上的椭圆曲线系统参数。

### 5.2 $ F_{p} $  上椭圆曲线系统参数及其验证

#### 5.2.1 $ F_{p} $  上椭圆曲线系统参数

 $ F_{p} $  上椭圆曲线系统参数包括：

a）域的规模 q=p, p 是大于 3 的素数；

b）（选项）一个长度至少为192的比特串SEED（若按照附录D描述的方法产生椭圆曲线）；

c)  $ F_{p} $  中的两个元素 a 和 b，它们定义椭圆曲线 E 的方程： $ y^{2}=x^{3}+ax+b $ ；

d) 基点  $ G=(x_{G},y_{G})\in E(F_{p}),G\neq O; $ 

e) 基点 G 的阶 n(要求:  $ n > 2^{191} $  且  $ n > 4p^{1/2} $ );

f）（选项）余因子  $ h=\#E(F_{p})/n $  。

#### 5.2.2 $ F_{p} $  上椭圆曲线系统参数的验证

椭圆曲线系统参数的生成者应验证下面的条件。椭圆曲线系统参数的用户可选择验证这些条件。

输入： $ F_{p} $  上椭圆曲线系统参数的集合。

输出：若椭圆曲线系统参数是有效的，则输出“有效”；否则输出“无效”。

a）验证 q=p 是奇素数（参见附录 B 中 B.1.10）；

b) 验证 a, b,  $ x_{G} $  和  $ y_{G} $  是区间 [0, p-1] 中的整数；

c) 若按照附录 D 描述的方法拟随机产生椭圆曲线，验证 SEED 是长度至少为 192 的比特串，且 a, b 由 SEED 派生得到；

d）验证 $ (4a^{3}+27b^{2})\bmod p\neq0 $ ;

e）验证  $ y_{G}^{2} \equiv x_{G}^{3} + ax_{G} + b \pmod{p} $ ;

f）验证 n 是素数， $ n>2^{191} $  且  $ n>4p^{1/2} $  （参见附录 B 中 B.1.10）；

g）验证 $$ n $$ G=O（参见附录 A 中 A.3）；

h）（选项）计算  $ h'=\left[\left(p^{1/2}+1\right)^{2}/n\right] $ ，并验证  $ h=h' $ ;

i) 验证抗 MOV 攻击条件和抗异常曲线攻击条件成立(参见附录 A 中 A.4.2.1 和 A.4.2.2);

i) 若以上任何一个验证失败，则输出“无效”；否则，输出“有效”。

### 5.3 $ F_{2^{m}} $  上椭圆曲线系统参数及其验证

#### 5.3.1 $ F_{2^{m}} $  上椭圆曲线系统参数

 $ F_{2^{m}} $ 上的椭圆曲线系统参数包括：

a）域的规模  $ q=2^{m} $ ，对  $ F_{2^{m}} $  中元素表示法（三项式基 TPB、五项式基 PPB 或高斯正规基 GNB）的标识，一个  $ F_{2} $  上的 m 次约化多项式（若所用的基是 TPB 或 PPB）；

b）（选项）一个长度至少为 192 的比特串 SEED（若按照附录 D 描述的方法拟随机产生椭圆曲线）；

c)  $ F_{2^{m}} $  中的两个元素 a 和 b，它们定义椭圆曲线 E 的方程： $ y^{2} + xy = x^{3} + ax^{2} + b $ ;

d) 基点  $ G=(x_{G},y_{G})\in E(F_{2^{m}}),G\neq O; $ 

e）基点 G 的阶 n（要求： $ n \geq 2^{191} $  且  $ n \geq 2^{2+m/2} $ ）；

f）（选项）余因子  $ h=\#E(F_{2^{m}})/n $ 。

#### 5.3.2 $ F_{2^{m}} $  上椭圆曲线系统参数的验证

下面的条件椭圆曲线系统参数的生成者应加以验证。这些条件椭圆曲线系统参数的用户可选择验证。

输入： $ F_{2^{m}} $  上椭圆曲线系统参数的集合。

输出：若椭圆曲线系统参数是有效的，则输出“有效”；否则输出“无效”。

a）对某个 m，验证  $ q=2^{m} $ ；若所用的是 TPB，则验证约化多项式是  $ F_{2} $  上的不可约三项式（参见表 A.3）；若所用的是 PPB，则验证不存在 m 次不可约三项式，且约化多项式是  $ F_{2} $  上的不可约五项式（参见表 A.4）；若所用的是 GNB，则验证 m 不能被 8 整除；

b) 验证 a, b,  $ x_{G} $  和  $ y_{G} $  是长度为 m 的比特串；

c) 若按照附录 D 描述的方法拟随机产生椭圆曲线，验证 SEED 是长度至少为 192 的比特串，且 a, b 由 SEED 派生得到；

d）验证  $ b \neq 0 $ ;

e) 在  $ F_{2^{m}} $  中验证  $ y_{G}^{2} + x_{G}y_{G} = x_{G}^{3} + a x_{G}^{2} + b $ ;

f) 验证 n 是一个素数， $ n > 2^{191} $  且  $ n > 2^{2+m/2} $  （参见附录 B 中 B.1.10）；

g）验证 $$ n $$ G=O(参见附录A.3.2)；

h）（选项）计算  $ h'=\left[(2^{m/2}+1)^{2}/n\right] $ ，验证  $ h=h' $ ;

i) 验证抗 MOV 攻击条件成立(参见附录 A 中 A.4.2.1);

i) 若以上任何一个验证失败，则输出“无效”；否则输出“有效”。

## 6 密钥对的生成与公钥的验证

### 6.1 密钥对的生成

输入:一个有效的  $ F_{q}(q=p $  且 p 为大于 3 的素数,或  $ q=2^{m} $  )上椭圆曲线系统参数的集合。

输出：与椭圆曲线系统参数相关的一个密钥对 $ (d,P) $ 。

a）用随机数发生器产生整数  $ d \in [1, n-2] $ ;

b) G 为基点，计算点  $ P=(x_{P},y_{P})=[d]G $  (参见附录 A 中 A.3.2)；

c）密钥对是 $ (d,P) $ ，其中d为私钥，P为公钥。

### 6.2 公钥的验证

#### 6.2.1 $ F_{p} $  上椭圆曲线公钥的验证

输入:一个有效的  $ F_{p}(p>3 $  且 p 为素数)上椭圆曲线系统参数集合及一个相关的公钥 P。

输出：对于给定的椭圆曲线系统参数，若公钥 P 是有效的，则输出“有效”；否则输出“无效”。

a）验证 P 不是无穷远点 O；

b）验证公钥 P 的坐标  $ x_{P} $  和  $ y_{P} $  是域  $ F_{p} $  中的元素（即验证  $ x_{P} $  和  $ y_{P} $  是区间  $ [0, p-1] $  中的整数）；

c) 验证  $ y_{P}^{2} \equiv x_{P}^{3} + ax_{P} + b \pmod{p} $ ;

d）验证 $$ n]P=O $$ 

e） 若通过了所有验证，则输出“有效”；否则输出“无效”。

#### 6.2.2 $ F_{2^{m}} $  上椭圆曲线公钥的验证

输入:一个有效的  $ F_{2^{m}} $  上椭圆曲线系统参数集合及一个相关的公钥 P。

输出：对于给定的椭圆曲线系统参数，若公钥 P 是有效的，则输出“有效”；否则输出“无效”。

a）验证 P 不是无穷远点 O；

b）验证公钥 P 的坐标  $ x_{P} $  和  $ y_{P} $  是域  $ F_{2^{m}} $  中的元素（即验证  $ x_{P} $  和  $ y_{P} $  是长度为 m 的比特串）；

c) 在  $ F_{2^{m}} $  中验证  $ y_{P}^{2} + x_{P}y_{P} = x_{P}^{3} + ax_{P}^{2} + b $ ;

d）验证 $$ n]P=O; $$ 

e） 若通过了所有验证，则输出“有效”；否则输出“无效”。

注：公钥的验证是可选项。

# 附录 A

# （资料性附录） 关于椭圆曲线的背景知识

### A.1 素域  $ F_{p} $ 

#### A.1.1 素域  $ F_{p} $  的定义

设 p 是一个素数， $ F_{p} $  由  $ \{0,1,2,\cdots,p-1\} $  中 p 个元素构成，称  $ F_{p} $  为素域。加法单位元是整数 0，乘法单位元是整数 1， $ F_{p} $  的元素满足如下运算法则：

——加法：设  $ a, b \in F_{p} $ ，则  $ a + b = r $ ，其中  $ r = (a + b) \mod p, r \in [0, p - 1] $ 。

——乘法：设  $ a, b \in F_{p} $ ，则  $ a \cdot b = s $ ，其中  $ s = (a \cdot b) \bmod p, s \in [0, p-1] $ 。

记  $ F_{p}^{*} $  是由  $ F_{p} $  中所有非零元构成的乘法群，由于  $ F_{p}^{*} $  是循环群，所以在  $ F_{p} $  中至少存在一个元素 g，使得  $ F_{p} $  中任一非零元都可以由 g 的一个方幂表示，称 g 为  $ F_{p}^{*} $  的生成元（或本原元），即  $ F_{p}^{*}=\{g^{i} \mid 0 \leqslant i \leqslant p-2\} $ 。设  $ a=g^{i} \in F_{p}^{*} $ ，其中  $ 0 \leqslant i \leqslant p-2 $ ，则 a 的乘法逆元为： $ a^{-1}=g^{p-1-i} $ 。

示例 1: 素域  $ F_{2}, F_{2} = \{0, 1\} $ 

 $ F_{2} $  的加法表如表 A.1，乘法表如表 A.2：

<div style="text-align: center;">表 A.1</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>+</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_178_1018_214_1052.jpg" alt="Image" width="3%" /></div>


<div style="text-align: center;">表 A.2</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>•</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td></tr></table>

示例 2: 素域  $ F_{19}, F_{19} = \{0, 1, 2, \cdots, 18\} $ 

 $ F_{19} $ 中加法的示例： $ 10,14\in F_{19},10+14=24,24\mod19=5 $ ，则 $ 10+14=5 $ 。

 $$ F_{19} 中乘法的示例:7,8\in F_{19},7\times8=56,56\mod19=18,则 7\cdot8=18。 $$ 

13 是  $ F_{19} $  的一个生成元，则  $ F_{19} $  中元素可由 13 的方幂表示出来：

 $$ 13^{0}=1,13^{1}=13,13^{2}=17,13^{3}=12,13^{4}=4,13^{5}=14,13^{6}=11,13^{7}=10,13^{8}=16,13^{9}=18, $$ 

 $$ 13^{10}=6,13^{11}=2,13^{12}=7,13^{13}=15,13^{14}=5,13^{15}=8,13^{16}=9,13^{17}=3,13^{18}=1。 $$ 

#### A.1.2  $ F_{p} $  上椭圆曲线的定义

##### A.1.2.1 概述

 $ F_{p} $  上椭圆曲线常用的表示形式有两种：仿射坐标表示和射影坐标表示。

##### A.1.2.2 仿射坐标表示

当 p 是大于 3 的素数时， $ F_{p} $  上椭圆曲线方程在仿射坐标系下可以简化为  $ y^{2}=x^{3}+ax+b $ ，其中  $ a, b \in F_{p} $ ，且使得  $ (4a^{3}+27b^{2})\bmod p \neq 0 $ 。椭圆曲线上的点集记为  $ E(F_{p}) = \left\{(x, y) \mid x, y \in F_{p} \text{ 且满足曲线方程 } y^{2} = x^{3} + ax + b \right\} \cup \{O\} $ ，其中 O 是椭圆曲线的无穷远点。

 $ E(F_{p}) $ 上的点按照下面的加法运算规则,构成一个阿贝尔群:

a)  $ O+O=O; $ 

b)  $ \forall P=(x,y)\in E(F_{p})\backslash\{O\},P+O=O+P=P; $ 

c)  $ \forall P=(x,y)\in E(F_{p})\backslash\{O\},P $  的逆元素  $ -P=(x,-y),P+(-P)=O; $ 

d) 点  $ P_{1}=(x_{1},y_{1})\in E(F_{p})\backslash\{O\} $ ， $ P_{2}=(x_{2},y_{2})\in E(F_{p})\backslash\{O\} $ ， $ P_{3}=(x_{3},y_{3})=P_{1}+P_{2}\neq O $ ，则

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}-x_{1}-x_{2},\\ y_{3}=&\lambda\left(x_{1}-x_{3}\right)-y_{1},\end{aligned}\right. $$ 

其中

 $$ \lambda=\left\{\begin{aligned}&\frac{y_{2}-y_{1}}{x_{2}-x_{1}},& 若 x_{1}\neq x_{2},\\&\frac{3{x_{1}}^{2}+a}{2y_{1}},& 若 x_{1}=x_{2} 且 P_{2}\neq-P_{1}。\end{aligned}\right. $$ 

示例 3: 有限域  $ F_{19} $  上一条椭圆曲线

 $ F_{19} $  上方程： $ y^{2}=x^{3}+x+1 $ ，其中 a=1, b=1。则  $ F_{19} $  上曲线的点为：

(0,1),(0,18),(2,7),(2,12),(5,6),(5,13),(7,3),(7,16),(9,6),(9,13),(10,2),(10,17),(13,8),(13,11),(14,2),(14,17),(15,3),(15,16),(16,3),(16,16),

则  $ E(F_{19}) $  有 21 个点（包括无穷远点 O）。

a）取  $ P_{1}=(10,2) $ ， $ P_{2}=(9,6) $ ，计算  $ P_{3}=P_{1}+P_{2} $ ：

 $$ \lambda=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}=\frac{6-2}{9-10}=\frac{4}{-1}=-4\equiv15(\bmod19), $$ 

 $$ x_{3}=15^{2}-10-9=225-10-9\equiv16-10-9=-3\equiv16\pmod{19}, $$ 

 $$ y_{3}=15\times(10-16)-2=15\times(-6)-2\equiv3(\bmod19), $$ 

所以  $ P_{3}=(16,3) $ 。

b) 取  $ P_{1}=(10,2) $ ，计算  $ [2]P_{1} $ ：

 $$ \lambda=\frac{3{x_{1}}^{2}+a}{2{y_{1}}}=\frac{3\times10^{2}+1}{2\times2}=\frac{3\times5+1}{4}=\frac{16}{4}=4(\bmod19), $$ 

 $$ x_{3}=4^{2}-10-10=-4\equiv15(\bmod19), $$ 

 $$ y_{3}=4\times(10-15)-2=-22\equiv16(\bmod19), $$ 

所以 $ [2]P_{1}=(15,16) $ 。

##### A.1.2.3 射影坐标表示

###### A.1.2.3.1 标准射影坐标系

当 p 是大于 3 的素数时， $ F_{p} $  上椭圆曲线方程在标准射影坐标系下可以简化为  $ y^{2}z = x^{3} + axz^{2} + bz^{3} $ ，其中  $ a, b \in F_{p} $ ，且  $ 4a^{3} + 27b^{2} \neq 0 \mod p $ 。椭圆曲线上的点集记为  $ E(F_{p}) = \{(x, y, z) \mid x, y, z \in F_{p}\} $  且满足曲线方程  $ y^{2}z = x^{3} + axz^{2} + bz^{3} $ 。对于  $ (x_{1}, y_{1}, z_{1}) $  和  $ (x_{2}, y_{2}, z_{2}) $ ，若存在某个  $ u \in F_{p} $  且  $ u \neq 0 $ ，使得： $ x_{1} = ux_{2} $ ， $ y_{1} = uy_{2} $ ， $ z_{1} = uz_{2} $ ，则称这两个三元组等价，表示同一个点。

若  $ z \neq 0 $ ，记 X = x/z，Y = y/z，则可从标准射影坐标表示转化为仿射坐标表示： $ Y^{2} = X^{3} + aX + b $ ；若 z = 0，(0, 1, 0) 对应的仿射坐标系下的点即无穷远点 O。

标准射影坐标系下， $ E(F_{p}) $  上点的加法运算定义如下：

a） $ O+O=O; $ 

b)  $ \forall P=(x,y,z)\in E(F_{p})\backslash\{O\},P+O=O+P=P; $ 

c)  $ \forall P=(x,y,z)\in E(F_{p})\backslash\{O\},P $  的逆元素  $ -P=(ux,-uy,uz),u\in F_{p} $  且  $ u\neq0,P+(-P)=O; $ 

d）设点  $ P_{1}=(x_{1},y_{1},z_{1})\in E(F_{p})\backslash\{O\} $ ， $ P_{2}=(x_{2},y_{2},z_{2})\in E(F_{p})\backslash\{O\} $ ， $ P_{3}=P_{1}+P_{2}=(x_{3},y_{3},z_{3})\neq O $ ，

若  $ P_{1} \neq P_{2} $ ，则：

 $$ \lambda_{1}=x_{1}z_{2},\lambda_{2}=x_{2}z_{1},\lambda_{3}=\lambda_{1}-\lambda_{2},\lambda_{4}=y_{1}z_{2},\lambda_{5}=y_{2}z_{1},\lambda_{6}=\lambda_{4}-\lambda_{5},\lambda_{7}=\lambda_{1}+\lambda_{2},\lambda_{8}=z_{1}z_{2}, $$ 

 $$ \lambda_{9}=\lambda_{3}^{2},\lambda_{10}=\lambda_{3}\lambda_{9},\lambda_{11}=\lambda_{8}\lambda_{6}^{2}-\lambda_{7}\lambda_{9},x_{3}=\lambda_{3}\lambda_{11},y_{3}=\lambda_{6}(\lambda_{9}\lambda_{1}-\lambda_{11})-\lambda_{4}\lambda_{10},z_{3}=\lambda_{10}\lambda_{8}; $$ 

若  $ P_{1}=P_{2} $ ，则：

 $$ \lambda_{1}=3{x_{1}}^{2}+{a{z_{1}}^{2}},\lambda_{2}=2{y_{1}}{z_{1}},\lambda_{3}={y_{1}}^{2},\lambda_{4}=\lambda_{3}{x_{1}}{z_{1}},\lambda_{5}=\lambda_{2}^{2},\lambda_{6}=\lambda_{1}^{2}-8\lambda_{4}, $$ 

 $$ x_{3}=\lambda_{2}\lambda_{6},y_{3}=\lambda_{1}(4\lambda_{4}-\lambda_{6})-2\lambda_{5}\lambda_{3},z_{3}=\lambda_{2}\lambda_{5}。 $$ 

###### A.1.2.3.2 Jacobian 加重射影坐标系

 $ F_{p} $  上椭圆曲线方程在 Jacobian 加重射影坐标系下可以简化为  $ y^{2}=x^{3}+axz^{4}+bz^{6} $ 。其中  $ a,b \in F_{p} $ ，且  $ 4a^{3}+27b^{2} \neq 0 \mod p $ 。椭圆曲线上的点集记为  $ E(F_{p}) = \{(x,y,z) \mid x,y,z \in F_{p} $  且满足曲线方程  $ y^{2}=x^{3}+axz^{4}+bz^{6}\} $ 。对于  $ (x_{1},y_{1},z_{1}) $  和  $ (x_{2},y_{2},z_{2}) $ ，若存在某个  $ u \in F_{p} $  且  $ u \neq 0 $ ，使得： $ x_{1}=u^{2}x_{2} $ ， $ y_{1}=u^{3}y_{2} $ ， $ z_{1}=uz_{2} $ ，则称这两个三元组等价，表示同一个点。

若  $ z \neq 0 $ ，记  $ X = x / z^{2} $ ， $ Y = y / z^{3} $ ，则可从 Jacobian 加重射影坐标表示转化为仿射坐标表示： $ Y^{2} = X^{3} + aX + b $ ；

若  $ z=0,(1,1,0) $  对应的仿射坐标系下的点即无穷远点 O。

Jacobian 加重射影坐标系下， $ E(F_{p}) $  上点的加法运算定义如下：

a)  $ O+O=O; $ 

b)  $ \forall P=(x,y,z)\in E(F_{p})\backslash\{O\},P+O=O+P=P; $ 

c)  $ \forall P=(x,y,z)\in E(F_{p})\backslash\{O\},P $  的逆元素  $ -P=(u^{2}x,-u^{3}y,uz),u\in F_{p} $  且  $ u\neq0,P+(-P)=O; $ 

d）设点  $ P_{1}=(x_{1},y_{1},z_{1})\in E(F_{p})\backslash\{O\} $ ， $ P_{2}=(x_{2},y_{2},z_{2})\in E(F_{p})\backslash\{O\} $ ， $ P_{3}=P_{1}+P_{2}=(x_{3},y_{3},z_{3})\neq O $ ，

若  $ P_{1} \neq P_{2} $ ，则：

 $$ \lambda_{1}=x_{1}z_{2}^{2},\lambda_{2}=x_{2}z_{1}^{2},\lambda_{3}=\lambda_{1}-\lambda_{2},\lambda_{4}=y_{1}z_{2}^{3},\lambda_{5}=y_{2}z_{1}^{3},\lambda_{6}=\lambda_{4}-\lambda_{5},\lambda_{7}=\lambda_{1}+\lambda_{2}, $$ 

 $$ \lambda_{8}=\lambda_{4}+\lambda_{5},x_{3}=\lambda_{6}^{2}-\lambda_{7}\lambda_{3}^{2},y_{3}=\lambda_{6}(\lambda_{1}\lambda_{3}^{2}-x_{3})-\lambda_{4}\lambda_{3}^{3},z_{3}=z_{1}z_{2}\lambda_{3}; $$ 

若  $ P_{1}=P_{2} $ ，则：

 $$ \lambda_{1}=3x_{1}^{2}+a z_{1}^{4},\lambda_{2}=4x_{1}y_{1}^{2},\lambda_{3}=8y_{1}^{4},x_{3}=\lambda_{1}^{2}-2\lambda_{2},y_{3}=\lambda_{1}(\lambda_{2}-x_{3})-\lambda_{3},z_{3}=2y_{1}z_{1}。 $$ 

#### A.1.3  $ F_{p} $  上椭圆曲线的阶

 $ F_{p}(p $  为大于 3 的素数) 上一条椭圆曲线的阶是指点集  $ E(F_{p}) $  中元素的个数，记为  $ \#E(F_{p}) $  。由 Hasse 定理知： $ p+1-2p^{1/2}\leqslant\#E(F_{p})\leqslant p+1+2p^{1/2} $  。

若一条曲线的阶 $ \#E(F_{p})=p+1 $ ，则称此曲线为超奇异的，否则为非超奇异的。

### A.2 二元扩域  $ F_{2^{m}} $ 

#### A.2.1 二元扩域  $ F_{2^{m}} $  的定义

由  $ 2^{m} $  个元素构成的有限域  $ F_{2^{m}} $  是  $ F_{2} $  的 m 次扩张，称为 m 次二元扩域。 $ F_{2^{m}} $  可以看成  $ F_{2} $  上维数为

m 的向量空间，也就是说，在  $ F_{2^{m}} $  中存在 m 个元素  $ \alpha_{0}, \alpha_{1}, \cdots, \alpha_{m-1} $ ，使得  $ \forall \alpha \in F_{2^{m}}, \alpha $  可以唯一表示为： $ \alpha = a_{0}\alpha_{0} + a_{1}\alpha_{1} + \cdots + a_{m-1}\alpha_{m-1} $ ，其中  $ a_{i} \in F_{2} $ ，称  $ \{\alpha_{0}, \alpha_{1}, \cdots, \alpha_{m-1}\} $  为  $ F_{2^{m}} $  在  $ F_{2} $  上的一组基。给定这样一组基，就可以由向量  $ (a_{0}, a_{1}, \cdots, a_{m-1}) $  来表示域元素  $ \alpha $ 。 $ F_{2^{m}} $  在  $ F_{2} $  上的基有多种选择，域元素的加法在不同的基下的运算规则是一致的，都可以通过向量按分量异或运算得到；域元素的乘法在不同的基下有不同的运算规则（如用多项式基表示和用正规基表示时其运算规则就不一致）。

##### A.2.1.1 多项式基

设  $ F_{2} $  上 m 次不可约多项式  $ f(x)=x^{m}+f_{m-1}x^{m-1}+\cdots+f_{2}x^{2}+f_{1}x+f_{0} $  （其中  $ f_{i}\in F_{2}, i=0,1,\cdots,m-1 $ ）是二元扩域  $ F_{2^{m}} $  的约化多项式。 $ F_{2^{m}} $  由  $ F_{2} $  上所有次数低于 m 的多项式构成，即：

 $$ F_{_{2^{m}}}=\left\{a_{_{m-1}}x^{_{m-1}}+a_{_{m-2}}x^{_{m-2}}+\cdots+a_{_{1}}x+a_{_{0}}\mid a_{_{i}}\in F_{_{2}},i=0,1,\cdots,m-1\right\}。 $$ 

多项式集合 $ \left\{x^{m-1},x^{m-2},\cdots,x,1\right\} $ 是 $ F_{2^{m}} $ 作为向量空间在 $ F_{2} $ 上的一组基，称为多项式基。

域元素  $ a_{m-1}x^{m-1}+a_{m-2}x^{m-2}+\cdots+a_{1}x+a_{0} $  相对多项式基可以由长度为 m 的比特串  $ (a_{m-1}a_{m-2}\cdots a_{1}a_{0}) $  来表示，所以

 $$ F_{2^{m}}=\left\{\left(a_{m-1}a_{m-2}\cdots a_{1}a_{0}\right)\mid a_{i}\in F_{2},i=0,1,\cdots,m-1\right\}。 $$ 

乘法单位元 1 由  $ (00\cdots01) $  表示，零元由  $ (00\cdots00) $  表示。域元素的加法和乘法定义如下：

——加法运算

 $ \forall(a_{m-1}a_{m-2}\cdots a_{1}a_{0}),(b_{m-1}b_{m-2}\cdots b_{1}b_{0})\in F_{2^{m}} $ ，则 $ (a_{m-1}a_{m-2}\cdots a_{1}a_{0})+(b_{m-1}b_{m-2}\cdots b_{1}b_{0})=(c_{m-1}c_{m-2}\cdots c_{1}c_{0}) $ ，其中 $ c_{i}=a_{i}\oplus b_{i},i=0,1,\cdots,m-1 $ ，亦即，加法运算按分位异或运算执行。

——乘法运算

 $ \forall(a_{m-1}a_{m-2}\cdots a_{1}a_{0}),(b_{m-1}b_{m-2}\cdots b_{1}b_{0})\in F_{2^{m}} $ ，则 $ (a_{m-1}a_{m-2}\cdots a_{1}a_{0})\cdot(b_{m-1}b_{m-2}\cdots b_{1}b_{0})=(r_{m-1}r_{m-2}\cdots r_{1}r_{0}) $ ，其中多项式 $ (r_{m-1}x^{m-1}+r_{m-2}x^{m-2}+\cdots+r_{1}x+r_{0}) $ 是 $ (a_{m-1}x^{m-1}+a_{m-2}x^{m-2}+\cdots+a_{1}x+a_{0})\cdot(b_{m-1}x^{m-1}+b_{m-2}x^{m-2}+\cdots+b_{1}x+b_{0}) $ 在 $ F_{2} $ 上 $ \bmod f(x) $ 的余式。

注意, $ F_{2^{m}} $ 恰包含 $ 2^{m} $ 个元素。记 $ F_{2^{m}} $ 是由 $ F_{2^{m}} $ 中所有非零元构成的乘法群, $ F_{2^{m}} $ 是循环群,在 $ F_{2^{m}} $ 中至少存在一个元素g,使得 $ F_{2^{m}} $ 中任一非零元都可以由g的一个方幂表示,称g为 $ F_{2^{m}} $ 的生成元(或本原元),即: $ F_{2^{m}}}^{*}=\left\{g^{i}\mid0\leqslant i\leqslant2^{m}-2\right\} $ 。设 $ a=g^{i}\in F_{2^{m}}^{*} $ ,其中 $ 0\leqslant i\leqslant2^{m}-2 $ ,则a的乘法逆元为: $ a^{-1}=g^{2m-1-i} $ 。

示例 4: 二元扩域  $ F_{25} $  的多项式基表示

取  $ F_{2} $  上的一个不可约多项式  $ f(x)=x^{5}+x^{2}+1 $ ，则  $ F_{25} $  中的元素是：

(00000), (00001), (00010), (00011), (00100), (00101), (00110),

(00111), (01000), (01001), (01010), (01011), (01100), (01101),

(01110), (01111), (10000), (10001), (10010), (10011), (10100),

(10101), (10110), (10111), (11000), (11001), (11010), (11011),

(11100), (11101), (11110), (11111).

加法： $  (11011) + (10011) = (01000)  $ 

乘法： $  (11011) \cdot (10011) = (00100)  $ 

 $$ \begin{aligned}(x^{4}+x^{3}+x+1)\bullet(x^{4}+x+1)&=x^{8}+x^{7}+x^{4}+x^{3}+x^{2}+1\\&=(x^{5}+x^{2}+1)\bullet(x^{3}+x^{2}+1)+x^{2}\\&\equiv x^{2}(\bmod f(x))\end{aligned} $$ 

即  $ x^{2} $  是  $ (x^{4}+x^{3}+x+1)\cdot(x^{4}+x+1) $  除以  $ f(x) $  的余式。

乘法单位元是 $ (00001) $ ， $ \alpha=x $  是 $ F_{25} $  的一个生成元，则 $ \alpha $  的方幂为：

 $$ \alpha^{0}=(00001),\alpha^{1}=(00010),\alpha^{2}=(00100),\alpha^{3}=(01000),\alpha^{4}=(10000),\alpha^{5}=(00101), $$ 

 $$ \alpha^{6}=\left(01010\right),\alpha^{7}=\left(10100\right),\alpha^{8}=\left(01101\right),\alpha^{9}=\left(11010\right),\alpha^{10}=\left(10001\right),\alpha^{11}=\left(00111\right), $$ 

 $$ \alpha^{12}=(01110),\alpha^{13}=(11100),\alpha^{14}=(11101),\alpha^{15}=(11111),\alpha^{16}=(11011),\alpha^{17}=(10011), $$ 

 $$ \alpha^{18}=\left(00011\right),\alpha^{19}=\left(00110\right),\alpha^{20}=\left(01100\right),\alpha^{21}=\left(11000\right),\alpha^{22}=\left(10101\right),\alpha^{23}=\left(01111\right), $$ 

 $$ \begin{aligned}&\alpha^{24}=(11110),\alpha^{25}=(11001),\alpha^{26}=(10111),\alpha^{27}=(01011),\alpha^{28}=(10110),\alpha^{29}=(01001),\\ &\alpha^{30}=(10010),\alpha^{31}=(00001)。\\ \end{aligned} $$ 

##### A.2.1.2 三项式和五项式基

###### A.2.1.2.1 概述

三项式基(TPB)和五项式基(PPB)是特殊的多项式基。

###### A.2.1.2.2 三项式基

 $ F_{2} $ 上的三项式是形如 $ x^{m}+x^{k}+1 $ 的多项式，其中 $ 1\leqslant k\leqslant m-1 $ 。

 $ F_{2^{m}} $  的一个三项式基表示是由  $ F_{2} $  上一个 m 次不可约三项式决定的，只有某些特定的 m 值存在这样的三项式。上述示例 4 即为  $ F_{2^{5}} $  的三项式基表示。

对  $ 192 \leqslant m \leqslant 512 $ ，表 A.3 给出了存在 m 次不可约三项式的每一个 m 值；并对每个这样的 m，给出了最小的 k，使得三项式  $ x^{m} + x^{k} + 1 $  在  $ F_{2} $  上是不可约的。

<div style="text-align: center;">表 A.3</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td></tr><tr><td style='text-align: center;'>193,15</td><td style='text-align: center;'>194,87</td><td style='text-align: center;'>196,3</td><td style='text-align: center;'>198,9</td><td style='text-align: center;'>199,34</td><td style='text-align: center;'>201,14</td></tr><tr><td style='text-align: center;'>202,55</td><td style='text-align: center;'>204,27</td><td style='text-align: center;'>207,43</td><td style='text-align: center;'>209,6</td><td style='text-align: center;'>210,7</td><td style='text-align: center;'>212,105</td></tr><tr><td style='text-align: center;'>214,73</td><td style='text-align: center;'>215,23</td><td style='text-align: center;'>217,45</td><td style='text-align: center;'>218,11</td><td style='text-align: center;'>220,7</td><td style='text-align: center;'>223,33</td></tr><tr><td style='text-align: center;'>225,32</td><td style='text-align: center;'>228,113</td><td style='text-align: center;'>231,26</td><td style='text-align: center;'>233,74</td><td style='text-align: center;'>234,31</td><td style='text-align: center;'>236,5</td></tr><tr><td style='text-align: center;'>238,73</td><td style='text-align: center;'>239,36</td><td style='text-align: center;'>241,70</td><td style='text-align: center;'>242,95</td><td style='text-align: center;'>244,111</td><td style='text-align: center;'>247,82</td></tr><tr><td style='text-align: center;'>249,35</td><td style='text-align: center;'>250,103</td><td style='text-align: center;'>252,15</td><td style='text-align: center;'>253,46</td><td style='text-align: center;'>255,52</td><td style='text-align: center;'>257,12</td></tr><tr><td style='text-align: center;'>258,71</td><td style='text-align: center;'>260,15</td><td style='text-align: center;'>263,93</td><td style='text-align: center;'>265,42</td><td style='text-align: center;'>266,47</td><td style='text-align: center;'>268,25</td></tr><tr><td style='text-align: center;'>270,53</td><td style='text-align: center;'>271,58</td><td style='text-align: center;'>273,23</td><td style='text-align: center;'>274,67</td><td style='text-align: center;'>276,63</td><td style='text-align: center;'>278,5</td></tr><tr><td style='text-align: center;'>279,5</td><td style='text-align: center;'>281,93</td><td style='text-align: center;'>282,35</td><td style='text-align: center;'>284,53</td><td style='text-align: center;'>286,69</td><td style='text-align: center;'>287,71</td></tr><tr><td style='text-align: center;'>289,21</td><td style='text-align: center;'>292,37</td><td style='text-align: center;'>294,33</td><td style='text-align: center;'>295,48</td><td style='text-align: center;'>297,5</td><td style='text-align: center;'>300,5</td></tr><tr><td style='text-align: center;'>302,41</td><td style='text-align: center;'>303,1</td><td style='text-align: center;'>305,102</td><td style='text-align: center;'>308,15</td><td style='text-align: center;'>310,93</td><td style='text-align: center;'>313,79</td></tr><tr><td style='text-align: center;'>314,15</td><td style='text-align: center;'>316,63</td><td style='text-align: center;'>318,45</td><td style='text-align: center;'>319,36</td><td style='text-align: center;'>321,31</td><td style='text-align: center;'>322,67</td></tr><tr><td style='text-align: center;'>324,51</td><td style='text-align: center;'>327,34</td><td style='text-align: center;'>329,50</td><td style='text-align: center;'>330,99</td><td style='text-align: center;'>332,89</td><td style='text-align: center;'>333,2</td></tr><tr><td style='text-align: center;'>337,55</td><td style='text-align: center;'>340,45</td><td style='text-align: center;'>342,125</td><td style='text-align: center;'>343,75</td><td style='text-align: center;'>345,22</td><td style='text-align: center;'>346,63</td></tr><tr><td style='text-align: center;'>348,103</td><td style='text-align: center;'>350,53</td><td style='text-align: center;'>351,34</td><td style='text-align: center;'>353,69</td><td style='text-align: center;'>354,99</td><td style='text-align: center;'>358,57</td></tr><tr><td style='text-align: center;'>359,68</td><td style='text-align: center;'>362,63</td><td style='text-align: center;'>364,9</td><td style='text-align: center;'>366,29</td><td style='text-align: center;'>367,21</td><td style='text-align: center;'>369,91</td></tr><tr><td style='text-align: center;'>370,139</td><td style='text-align: center;'>372,111</td><td style='text-align: center;'>375,16</td><td style='text-align: center;'>377,41</td><td style='text-align: center;'>378,43</td><td style='text-align: center;'>380,47</td></tr><tr><td style='text-align: center;'>382,81</td><td style='text-align: center;'>383,90</td><td style='text-align: center;'>385,6</td><td style='text-align: center;'>386,83</td><td style='text-align: center;'>388,159</td><td style='text-align: center;'>390,9</td></tr><tr><td style='text-align: center;'>391,28</td><td style='text-align: center;'>393,7</td><td style='text-align: center;'>394,135</td><td style='text-align: center;'>396,25</td><td style='text-align: center;'>399,26</td><td style='text-align: center;'>401,152</td></tr><tr><td style='text-align: center;'>402,171</td><td style='text-align: center;'>404,65</td><td style='text-align: center;'>406,141</td><td style='text-align: center;'>407,71</td><td style='text-align: center;'>409,87</td><td style='text-align: center;'>412,147</td></tr><tr><td style='text-align: center;'>414,13</td><td style='text-align: center;'>415,102</td><td style='text-align: center;'>417,107</td><td style='text-align: center;'>418,199</td><td style='text-align: center;'>420,7</td><td style='text-align: center;'>422,149</td></tr><tr><td style='text-align: center;'>423,25</td><td style='text-align: center;'>425,12</td><td style='text-align: center;'>426,63</td><td style='text-align: center;'>428,105</td><td style='text-align: center;'>431,120</td><td style='text-align: center;'>433,33</td></tr></table>

<div style="text-align: center;">表 A.3 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td><td style='text-align: center;'>m,k</td></tr><tr><td style='text-align: center;'>436,165</td><td style='text-align: center;'>438,65</td><td style='text-align: center;'>439,49</td><td style='text-align: center;'>441,7</td><td style='text-align: center;'>444,81</td><td style='text-align: center;'>446,105</td></tr><tr><td style='text-align: center;'>447,73</td><td style='text-align: center;'>449,134</td><td style='text-align: center;'>450,47</td><td style='text-align: center;'>455,38</td><td style='text-align: center;'>457,16</td><td style='text-align: center;'>458,203</td></tr><tr><td style='text-align: center;'>460,19</td><td style='text-align: center;'>462,73</td><td style='text-align: center;'>463,93</td><td style='text-align: center;'>465,31</td><td style='text-align: center;'>468,27</td><td style='text-align: center;'>470,9</td></tr><tr><td style='text-align: center;'>471,1</td><td style='text-align: center;'>473,200</td><td style='text-align: center;'>474,191</td><td style='text-align: center;'>476,9</td><td style='text-align: center;'>478,121</td><td style='text-align: center;'>479,104</td></tr><tr><td style='text-align: center;'>481,138</td><td style='text-align: center;'>484,105</td><td style='text-align: center;'>486,81</td><td style='text-align: center;'>487,94</td><td style='text-align: center;'>489,83</td><td style='text-align: center;'>490,219</td></tr><tr><td style='text-align: center;'>492,7</td><td style='text-align: center;'>494,17</td><td style='text-align: center;'>495,76</td><td style='text-align: center;'>497,78</td><td style='text-align: center;'>498,155</td><td style='text-align: center;'>500,27</td></tr><tr><td style='text-align: center;'>503,3</td><td style='text-align: center;'>505,156</td><td style='text-align: center;'>506,23</td><td style='text-align: center;'>508,9</td><td style='text-align: center;'>510,69</td><td style='text-align: center;'>511,10</td></tr></table>

###### A.2.1.2.3 五项式基

 $ F_{2} $ 上的五项式是形如 $ x^{m}+x^{k_{3}}+x^{k_{2}}+x^{k_{1}}+1 $ 的多项式，其中 $ 1\leqslant k_{1}<k_{2}<k_{3}\leqslant m-1 $ 。 $ F_{2^{m}} $ 的五项式基表示是由 $ F_{2} $ 上一个m次不可约五项式决定的。对 $ 4\leqslant m\leqslant512 $ ，均存在这样的五项式。

对  $ 192 \leqslant m \leqslant 512 $  且不存在不可约三项式的 m，表 A.4 列出了其不可约五项式的 m 值；并对每一个这样的 m，列出三元组  $ (k_{1}, k_{2}, k_{3}) $ ，满足：

a） $ x^{m}+x^{k_{3}}+x^{k_{2}}+x^{k_{1}}+1 $  在  $ F_{2} $  上不可约；

b)  $ k_{1} $  尽可能地小；

c）对这个选定的 $ k_{1},k_{2} $ 尽可能地小；

d）对选定的 $ k_{1} $ 和 $ k_{2} $ ， $ k_{3} $ 尽可能地小。

<div style="text-align: center;">表 A.4</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>m(k1,k2,k3)</td><td style='text-align: center;'>m(k1,k2,k3)</td><td style='text-align: center;'>m(k1,k2,k3)</td><td style='text-align: center;'>m(k1,k2,k3)</td></tr><tr><td style='text-align: center;'>192 (1,2,7)</td><td style='text-align: center;'>195 (1,2,37)</td><td style='text-align: center;'>197 (1,2,21)</td><td style='text-align: center;'>200 (1,2,81)</td></tr><tr><td style='text-align: center;'>203 (1,2,45)</td><td style='text-align: center;'>205 (1,2,21)</td><td style='text-align: center;'>206 (1,2,63)</td><td style='text-align: center;'>208 (1,2,83)</td></tr><tr><td style='text-align: center;'>211 (1,2,165)</td><td style='text-align: center;'>213 (1,2,62)</td><td style='text-align: center;'>216 (1,2,107)</td><td style='text-align: center;'>219 (1,2,65)</td></tr><tr><td style='text-align: center;'>221 (1,2,18)</td><td style='text-align: center;'>222 (1,2,73)</td><td style='text-align: center;'>224 (1,2,159)</td><td style='text-align: center;'>226 (1,2,30)</td></tr><tr><td style='text-align: center;'>227 (1,2,21)</td><td style='text-align: center;'>229 (1,2,21)</td><td style='text-align: center;'>230 (1,2,13)</td><td style='text-align: center;'>232 (1,2,23)</td></tr><tr><td style='text-align: center;'>235 (1,2,45)</td><td style='text-align: center;'>237 (1,2,104)</td><td style='text-align: center;'>240 (1,3,49)</td><td style='text-align: center;'>243 (1,2,17)</td></tr><tr><td style='text-align: center;'>245 (1,2,37)</td><td style='text-align: center;'>246 (1,2,11)</td><td style='text-align: center;'>248 (1,2,243)</td><td style='text-align: center;'>251 (1,2,45)</td></tr><tr><td style='text-align: center;'>254 (1,2,7)</td><td style='text-align: center;'>256 (1,2,155)</td><td style='text-align: center;'>259 (1,2,254)</td><td style='text-align: center;'>261 (1,2,74)</td></tr><tr><td style='text-align: center;'>262 (1,2,207)</td><td style='text-align: center;'>264 (1,2,169)</td><td style='text-align: center;'>267 (1,2,29)</td><td style='text-align: center;'>269 (1,2,117)</td></tr><tr><td style='text-align: center;'>272 (1,3,56)</td><td style='text-align: center;'>275 (1,2,28)</td><td style='text-align: center;'>277 (1,2,33)</td><td style='text-align: center;'>280 (1,2,113)</td></tr><tr><td style='text-align: center;'>283 (1,2,200)</td><td style='text-align: center;'>285 (1,2,77)</td><td style='text-align: center;'>288 (1,2,191)</td><td style='text-align: center;'>290 (1,2,70)</td></tr><tr><td style='text-align: center;'>291 (1,2,76)</td><td style='text-align: center;'>293 (1,3,154)</td><td style='text-align: center;'>296 (1,2,123)</td><td style='text-align: center;'>298 (1,2,78)</td></tr><tr><td style='text-align: center;'>299 (1,2,21)</td><td style='text-align: center;'>301 (1,2,26)</td><td style='text-align: center;'>304 (1,2,11)</td><td style='text-align: center;'>306 (1,2,106)</td></tr><tr><td style='text-align: center;'>307 (1,2,93)</td><td style='text-align: center;'>309 (1,2,26)</td><td style='text-align: center;'>311 (1,3,155)</td><td style='text-align: center;'>312 (1,2,83)</td></tr><tr><td style='text-align: center;'>315 (1,2,142)</td><td style='text-align: center;'>317 (1,3,68)</td><td style='text-align: center;'>320 (1,2,7)</td><td style='text-align: center;'>323 (1,2,21)</td></tr></table>

<div style="text-align: center;">表 A.4 (续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>m(k1,k2,k3)</td><td style='text-align: center;'>m(k1,k2,k3)</td><td style='text-align: center;'>m(k1,k2,k3)</td><td style='text-align: center;'>m(k1,k2,k3)</td></tr><tr><td style='text-align: center;'>325(1,2,53)</td><td style='text-align: center;'>326(1,2,67)</td><td style='text-align: center;'>328(1,2,51)</td><td style='text-align: center;'>331(1,2,134)</td></tr><tr><td style='text-align: center;'>334(1,2,5)</td><td style='text-align: center;'>335(1,2,250)</td><td style='text-align: center;'>336(1,2,77)</td><td style='text-align: center;'>338(1,2,112)</td></tr><tr><td style='text-align: center;'>339(1,2,26)</td><td style='text-align: center;'>341(1,2,57)</td><td style='text-align: center;'>344(1,2,7)</td><td style='text-align: center;'>347(1,2,96)</td></tr><tr><td style='text-align: center;'>349(1,2,186)</td><td style='text-align: center;'>352(1,2,263)</td><td style='text-align: center;'>355(1,2,138)</td><td style='text-align: center;'>356(1,2,69)</td></tr><tr><td style='text-align: center;'>357(1,2,28)</td><td style='text-align: center;'>360(1,2,49)</td><td style='text-align: center;'>361(1,2,44)</td><td style='text-align: center;'>363(1,2,38)</td></tr><tr><td style='text-align: center;'>365(1,2,109)</td><td style='text-align: center;'>368(1,2,85)</td><td style='text-align: center;'>371(1,2,156)</td><td style='text-align: center;'>373(1,3,172)</td></tr><tr><td style='text-align: center;'>374(1,2,109)</td><td style='text-align: center;'>376(1,2,77)</td><td style='text-align: center;'>379(1,2,222)</td><td style='text-align: center;'>381(1,2,5)</td></tr><tr><td style='text-align: center;'>384(1,2,299)</td><td style='text-align: center;'>387(1,2,146)</td><td style='text-align: center;'>389(1,2,159)</td><td style='text-align: center;'>392(1,2,145)</td></tr><tr><td style='text-align: center;'>395(1,2,333)</td><td style='text-align: center;'>397(1,2,125)</td><td style='text-align: center;'>398(1,3,23)</td><td style='text-align: center;'>400(1,2,245)</td></tr><tr><td style='text-align: center;'>403(1,2,80)</td><td style='text-align: center;'>405(1,2,38)</td><td style='text-align: center;'>408(1,2,323)</td><td style='text-align: center;'>410(1,2,16)</td></tr><tr><td style='text-align: center;'>411(1,2,50)</td><td style='text-align: center;'>413(1,2,33)</td><td style='text-align: center;'>416(1,3,76)</td><td style='text-align: center;'>419(1,2,129)</td></tr><tr><td style='text-align: center;'>421(1,2,81)</td><td style='text-align: center;'>424(1,2,177)</td><td style='text-align: center;'>427(1,2,245)</td><td style='text-align: center;'>429(1,2,14)</td></tr><tr><td style='text-align: center;'>430(1,2,263)</td><td style='text-align: center;'>432(1,2,103)</td><td style='text-align: center;'>434(1,2,64)</td><td style='text-align: center;'>435(1,2,166)</td></tr><tr><td style='text-align: center;'>437(1,2,6)</td><td style='text-align: center;'>440(1,2,37)</td><td style='text-align: center;'>442(1,2,32)</td><td style='text-align: center;'>443(1,2,57)</td></tr><tr><td style='text-align: center;'>445(1,2,225)</td><td style='text-align: center;'>448(1,3,83)</td><td style='text-align: center;'>451(1,2,33)</td><td style='text-align: center;'>452(1,2,10)</td></tr><tr><td style='text-align: center;'>453(1,2,88)</td><td style='text-align: center;'>454(1,2,195)</td><td style='text-align: center;'>456(1,2,275)</td><td style='text-align: center;'>459(1,2,332)</td></tr><tr><td style='text-align: center;'>461(1,2,247)</td><td style='text-align: center;'>464(1,2,310)</td><td style='text-align: center;'>466(1,2,78)</td><td style='text-align: center;'>467(1,2,210)</td></tr><tr><td style='text-align: center;'>469(1,2,149)</td><td style='text-align: center;'>472(1,2,33)</td><td style='text-align: center;'>475(1,2,68)</td><td style='text-align: center;'>477(1,2,121)</td></tr><tr><td style='text-align: center;'>480(1,2,149)</td><td style='text-align: center;'>482(1,2,13)</td><td style='text-align: center;'>483(1,2,352)</td><td style='text-align: center;'>485(1,2,70)</td></tr><tr><td style='text-align: center;'>488(1,2,123)</td><td style='text-align: center;'>491(1,2,270)</td><td style='text-align: center;'>493(1,2,171)</td><td style='text-align: center;'>496(1,3,52)</td></tr><tr><td style='text-align: center;'>499(1,2,174)</td><td style='text-align: center;'>501(1,2,332)</td><td style='text-align: center;'>502(1,2,99)</td><td style='text-align: center;'>504(1,3,148)</td></tr><tr><td style='text-align: center;'>507(1,2,26)</td><td style='text-align: center;'>509(1,2,94)</td><td style='text-align: center;'>512(1,2,51)</td><td style='text-align: center;'></td></tr></table>

###### A.2.1.2.4 选择多项式基的规则

 $ F_{2^{m}} $  的不同多项式基表示取决于约化多项式的选择：

a）若存在  $ F_{2} $  上的 m 次不可约三项式，则约化多项式  $ f(x) $  选用不可约三项式  $ x^{m} + x^{k} + 1 $ ，为了使实现的效果更好，k 的取值应尽可能小（这样的多项式在表 A.3 给出）；

b）若不存在  $ F_{2} $  上的 m 次不可约三项式，则约化多项式  $ f(x) $  选用不可约五项式  $ x^{m} + x^{k_{3}} + x^{k_{2}} + x^{k_{1}} + 1 $ ，为了使实现的效果更好：

1） $ k_{1} $  应尽可能小；

2）对这个选定的 $ k_{1},k_{2} $ 应尽可能小；

3）对选定的 $ k_{1} $ 和 $ k_{2} $ ， $ k_{3} $ 应尽可能小（这样的多项式在表A.4给出）。

##### A.2.1.3 正规基

形如 $ \{\beta,\beta^{2},\beta^{2^{2}},\cdots,\beta^{2^{m-1}}\} $ 的基是 $ F_{2^{m}} $ 在 $ F_{2} $ 上的一组正规基，其中 $ \beta\in F_{2^{m}} $ 。这样的基总是存在的。

 $ \forall\alpha\in F_{2^{m}} $ ，则  $ \alpha=a_{0}\beta^{20}+a_{1}\beta^{21}+\cdots+a_{m-1}\beta^{2m-1} $ ，其中  $ a_{i}\in F_{2} $ ， $ (i=0,1,\cdots,m-1) $ ，并记为  $ \alpha=(a_{0}a_{1}a_{2}\cdots a_{m-2}a_{m-1}) $ ，域元素  $ \alpha $  由长度为 m 的比特串表示。所以  $ F_{2^{m}}=\left\{(a_{0}a_{1}a_{2}\cdots a_{m-2}a_{m-1})\mid a_{i}\in F_{2},0\leqslant i\leqslant m-1\right\} $ ，乘法单位元 1 由 m 个 1 的比特串  $ (11\cdots1) $  表示，零元由 m 个 0 的比特串  $ (00\cdots0) $  表示。

注：通过约定，正规基表示的比特排序同多项式基表示的比特排序是不一样的（参见 A.2.1.1）。

在正规基表示下， $ F_{2^{m}} $  中求平方运算是循环右移位运算：

 $$ \forall\alpha\in F_{2^{m}},\alpha=a_{0}\beta^{2^{0}}+a_{1}\beta^{2^{1}}+\cdots+a_{m-1}\beta^{2^{m-1}}=(a_{0}a_{1}a_{2}\cdots a_{m-2}a_{m-1}), $$ 

 $$ \alpha^{2}=\big(\sum_{i=0}^{m-1}a_{i}\beta^{2i}\big)^{2}=\sum_{i=0}^{m-1}a_{i}^{2}\beta^{2i+1}=\sum_{i=0}^{m-1}a_{i-1}\beta^{2i}=\left(a_{m-1}a_{0}\cdots a_{m-2}\right)。 $$ 

在这种情况下，求平方运算只是长度为 m 的比特串的循环移位，便于在硬件上实现。

##### A.2.1.4 高斯正规基

由 A.2.1.3 可知， $ F_{2^{m}} $  在  $ F_{2} $  上的正规基是形式为  $ N=\{\beta,\beta^{2},\beta^{2^{2}},\cdots,\beta^{2^{m}-1}\} $  的一组基，其中  $ \beta\in F_{2^{m}} $ 。正规基表示在求取元素的平方时有计算优势，但对于一般意义下的不同元素的乘法运算不太方便。因此，通常专用一种称为高斯正规基的基，对这样的基，乘法既简单又有效。

当 m 不能被 8 整除时  $ F_{2^{m}} $  存在高斯正规基。高斯正规基的类型 T 是指在此基下度量乘法运算复杂度的一个正整数。一般情况下，类型 T 愈小，乘法效率愈高。对于给定的 m 和 T，域  $ F_{2^{m}} $  至多有一个类型 T 的高斯正规基。在所有正规基中，类型 1 和类型 2 的高斯正规基有最有效的乘法运算，因而也称它们为最优正规基。类型 1 的高斯正规基称为 I 型最优正规基，类型 2 的高斯正规基称为 II 型最优正规基。

有限域  $ F_{2^{m}} $  中的元素 a 在高斯正规基下可以由长度为 m 的比特串  $ (a_{m-1}a_{m-2}\cdots a_{1}a_{0}) $  来表示。

a）乘法单位元 1 由 m 个 1 的比特串表示；

b）零元 0 由 m 个 0 的比特串表示；

c）两个域元素的加法由比特串对位异或运算完成；

d）域元素的乘法在 A.2.1.4.3 中描述。

###### A.2.1.4.1 选择正规基的规则

选择  $ F_{2^{m}} $  存在的最小类型的高斯正规基。

表 A.5 列出 [192,512] 中素数 m 的  $ F_{2^{m}} $  上高斯正规基的类型。

<div style="text-align: center;">表 A.5</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>m类型</td><td style='text-align: center;'>m类型</td><td style='text-align: center;'>m类型</td><td style='text-align: center;'>m类型</td><td style='text-align: center;'>m类型</td><td style='text-align: center;'>m类型</td></tr><tr><td style='text-align: center;'>193 4</td><td style='text-align: center;'>197 18</td><td style='text-align: center;'>199 4</td><td style='text-align: center;'>211 10</td><td style='text-align: center;'>223 12</td><td style='text-align: center;'>227 24</td></tr><tr><td style='text-align: center;'>229 12</td><td style='text-align: center;'>233 2</td><td style='text-align: center;'>239 2</td><td style='text-align: center;'>241 6</td><td style='text-align: center;'>251 2</td><td style='text-align: center;'>257 6</td></tr><tr><td style='text-align: center;'>263 6</td><td style='text-align: center;'>269 8</td><td style='text-align: center;'>271 6</td><td style='text-align: center;'>277 4</td><td style='text-align: center;'>281 2</td><td style='text-align: center;'>283 6</td></tr><tr><td style='text-align: center;'>293 2</td><td style='text-align: center;'>307 4</td><td style='text-align: center;'>311 6</td><td style='text-align: center;'>313 6</td><td style='text-align: center;'>317 26</td><td style='text-align: center;'>331 6</td></tr><tr><td style='text-align: center;'>337 10</td><td style='text-align: center;'>347 6</td><td style='text-align: center;'>349 10</td><td style='text-align: center;'>353 14</td><td style='text-align: center;'>359 2</td><td style='text-align: center;'>367 6</td></tr><tr><td style='text-align: center;'>373 4</td><td style='text-align: center;'>379 12</td><td style='text-align: center;'>383 12</td><td style='text-align: center;'>389 24</td><td style='text-align: center;'>397 6</td><td style='text-align: center;'>401 8</td></tr><tr><td style='text-align: center;'>409 4</td><td style='text-align: center;'>419 2</td><td style='text-align: center;'>421 10</td><td style='text-align: center;'>431 2</td><td style='text-align: center;'>433 4</td><td style='text-align: center;'>439 10</td></tr><tr><td style='text-align: center;'>443 2</td><td style='text-align: center;'>449 8</td><td style='text-align: center;'>457 30</td><td style='text-align: center;'>461 6</td><td style='text-align: center;'>463 12</td><td style='text-align: center;'>467 6</td></tr><tr><td style='text-align: center;'>479 8</td><td style='text-align: center;'>487 4</td><td style='text-align: center;'>491 2</td><td style='text-align: center;'>499 4</td><td style='text-align: center;'>503 6</td><td style='text-align: center;'>509 2</td></tr></table>

###### A.2.1.4.2 高斯正规基的检验

给定类型 T，利用下述算法可以检验  $ F_{2^{m}} $  （m 大于 1 且不能被 8 整除）中类型 T 的高斯正规基的存在性。

输入:大于1且不被8整除的整数m,正整数T。

输出：若  $ F_{2^{m}} $  存在一个类型 T 的高斯正规基，输出“正确”；否则输出“错误”。

a）计算  $ p=T \cdot m+1 $ ;

b）若 p 不是素数，则输出“错误”并停止；

c） 计算 2 模 p 的阶 k (参见 B.1.8);

d）计算  $ u = T \cdot m / k $  ;

e) 计算  $ d=\gcd(u,m) $ ;

f）若 d=1，则输出“正确”；否则输出“错误”。

###### A.2.1.4.3 高斯正规基下的乘法算法

对于任意给定的高斯正规基，其乘法运算包含三部分：乘法预运算；给定两个元素后，其乘积的第一项 $ c_{0} $ 的公式；利用两个元素乘积的第一项 $ c_{0} $ 的公式，计算两个元素的乘积。下面对这三部分进行详细描述：

——乘法预运算：

输入: 大于 1 的整数 m，正整数 T，其中在  $ F_{2^{m}} $  上存在类型 T 的高斯正规基 B。

输出:相对于 B 的序列  $ f(1), f(2), \cdots, f(p-1) $ 。

a）计算  $ p = T \cdot m + 1 $ ;

b）产生模 p 阶为 T 的整数 u（参见 B.1.9）；

c） 计算序列  $ f(1) $ ,  $ f(2) $ ,  $ \cdots $ ,  $ f(p-1) $ :

1）置 w=1;

2）从j=0到T-1执行：

——置 n=w;

——从 i=0 到 m-1 执行：

● 置  $ f(n)=i $ ;

● 置  $ n=2n \mod p $ ;

• 置  $ w = u \cdot w \mod p $ ;

d）输出序列  $ f(1), f(2), \cdots, f(p-1) $ 。

——给定在高斯正规基 B 表示下的两个域元素 a 和 b，其乘积的第一项  $ c_{0} $  的公式：

记  $ c_{0}=F(a,b) $ 。

输入:大于1的整数m,正整数T(其中在 $ F_{2^{m}} $ 上存在类型T的高斯正规基B)及在高斯正规基B表示下的两个域元素a,b。

输出: 在高斯正规基 B 表示下的两个域元素 a、b 乘积的第一项  $ c_{0} $  的公式。

a）利用乘法预运算得到输出序列  $ f(1), f(2), \cdots, f(p-1) $ ;

b）T 为偶数，则 J=0，否则

 $$ J=\sum_{k=1}^{m}\left(a_{k-1}b_{m/2+k-1}+a_{m/2+k-1}b_{k-1}\right)； $$ 

c） 输出公式

 $$ c_{0}=J+\sum_{k=1}^{p-2}a_{f(k+1)}b_{f(p-k)}。 $$ 

——利用域元素 a 和 b 乘积的第一项  $ c_{0} $  的公式，计算域元素 a 和 b 的乘积：

对  $ u=(u_{0}u_{1}\cdots u_{m-1}),v=(v_{0}v_{1}\cdots v_{m-1}) $  ，设  $ F(u,v) $  是以  $ c_{0}=F(a,b) $  导出的表达式。

输入:大于1的整数m,正整数T(其中在 $ F_{2^{m}} $ 上存在类型T的高斯正规基B)及在高斯正规基B表示下的两个域元素a,b。

输出：积 $ (c_{0}c_{1}\cdots c_{m-1})=(a_{0}a_{1}\cdots a_{m-1})\times(b_{0}b_{1}\cdots b_{m-1}) $ 。

a）置 $ (u_{0}u_{1}\cdots u_{m-1})=(a_{0}a_{1}\cdots a_{m-1}) $ ；

b) 置 $ (v_{0}v_{1}\cdots v_{m-1})=(b_{0}b_{1}\cdots b_{m-1}) $ ;

c）对 k 从 0 到 m-1 执行：

1）计算  $ c_{k}=F(u,v) $ ;

2）置  $ u=\mathrm{LeftRotate}(u) $ ，并置  $ v=\mathrm{LeftRotate}(v) $ ，其中 LeftRotate() 表示循环左移 1 位运算，即 LeftRotate $ (u)=\mathrm{LeftRotate}(u_{0}u_{1}\cdots u_{m-2}u_{m-1})=(u_{1}u_{2}\cdots u_{m-1}u_{0}) $ ；

d）输出  $ c=(c_{0}c_{1}\cdots c_{m-1}) $ 。

在示例 4 中，用多项式乘法和带余除法描述了  $ F_{25} $ ，下面的示例 5 用高斯正规基表示  $ F_{25} $ 。

示例 5: 二元扩域  $ F_{25} $  的高斯正规基表示

 $ F_{25} $  域元素为比特五位组：

(00000), (00001), (00010), (00011), (00100), (00101), (00110), (00111),

(01000), (01001), (01010), (01011), (01100), (01101), (01110), (01111),

(10000),(10001),(10010),(10011),(10100),(10101),(10110),(10111),

(11000), (11001), (11010), (11011), (11100), (11101), (11110), (11111).

域加法： $ (a_{0}a_{1}a_{2}a_{3}a_{4})+(b_{0}b_{1}b_{2}b_{3}b_{4})=(c_{0}c_{1}c_{2}c_{3}c_{4}) $ ，其中 $ c_{i}=a_{i}\oplus b_{i},0\leqslant i<5 $ ，也就是域加法通过向量表示按分量异或运算来实现。

域乘法：

因为  $ 2 \times 5 + 1 = 11, 11 $  是一素数，则 T = 2, 2 模 11 的阶为 10，且  $ \gcd(5, (11 - 1) / 10) = 1 $ ，所以  $ F_{25} $  有第 2 类高斯正规基。10 模 11 的阶为 2，取 u = 10，则可计算出 f 的值如下：

 $$ f(1)=0,\qquad f(2)=1,\qquad f(4)=2,\qquad f(8)=3,\qquad f(5)=4, $$ 

 $$ f(10)=0,\quad f(9)=1,\quad f(7)=2,\quad f(3)=3,\quad f(6)=4。 $$ 

 $ a=(10000) $ ,  $ b=(11001) $ ，由 T=2 为偶数，则有 J=0。

则有  $ F(a,b)=\sum_{k=1}^{11-2}a_{f(k+1)}b_{f(11-k)} $ 

 $$ =a_{0}b_{1}+a_{1}(b_{0}+b_{3})+a_{2}(b_{3}+b_{4})+a_{3}(b_{1}+b_{2})+a_{4}(b_{2}+b_{4})。 $$ 

 $$ c_{0}=a_{0}b_{1}+a_{1}(b_{0}+b_{3})+a_{2}(b_{3}+b_{4})+a_{3}(b_{1}+b_{2})+a_{4}(b_{2}+b_{4}), $$ 

 $$ c_{1}=a_{1}b_{2}+a_{2}(b_{1}+b_{4})+a_{3}(b_{4}+b_{0})+a_{4}(b_{2}+b_{3})+a_{0}(b_{3}+b_{0}), $$ 

 $$ c_{2}=a_{2}b_{3}+a_{3}(b_{2}+b_{0})+a_{4}(b_{0}+b_{1})+a_{0}(b_{3}+b_{4})+a_{1}(b_{4}+b_{1}) $$ 

 $$ c_{3}=a_{3}b_{4}+a_{4}(b_{3}+b_{1})+a_{0}(b_{1}+b_{2})+a_{1}(b_{4}+b_{0})+a_{2}(b_{0}+b_{2}), $$ 

 $$ c_{4}=a_{4}b_{0}+a_{0}\left(b_{4}+b_{2}\right)+a_{1}\left(b_{2}+b_{3}\right)+a_{2}\left(b_{0}+b_{1}\right)+a_{3}\left(b_{1}+b_{3}\right)。 $$ 

可以得出：

 $$ c_{0}=F\left(\left(10000\right),\left(11001\right)\right)=1, $$ 

 $$ c_{1}=F\left(\left(00001\right),\left(10011\right)\right)=1, $$ 

 $$ c_{2}=F\left(\left(00010\right),\left(00111\right)\right)=1, $$ 

 $$ c_{3}=F\left(\left(00100\right),\left(01110\right)\right)=1, $$ 

 $$ c_{4}=F\left(\left(01000\right),\left(11100\right)\right)=1, $$ 

记 $ c=(c_{0}c_{1}c_{2}c_{3}c_{4}) $ ，所以 $ c=a\cdot b=(11111) $ 。

#### A.2.2  $ F_{2^{m}} $  上椭圆曲线的定义

##### A.2.2.1 概述

 $ F_{2^{m}} $  上椭圆曲线常用的表示形式有两种：仿射坐标表示和射影坐标表示。

##### A.2.2.2 仿射坐标表示

 $ F_{2^{m}} $  上非超奇异椭圆曲线方程在仿射坐标系下可以简化为  $ y^{2} + xy = x^{3} + ax^{2} + b $ ，其中  $ a, b \in F_{2^{m}} $ ，且  $ b \neq 0 $ 。椭圆曲线上的点集记为  $ E(F_{2^{m}}) = \{(x, y) \mid x, y \in F_{2^{m}} $  且满足曲线方程  $ y^{2} + xy = x^{3} + ax^{2} + b\} \cup \{O\} $ ，其中 O 是椭圆曲线的无穷远点，又称为零点。

 $ E(F_{2^{m}}) $ 上的点按照下面的加法运算规则,构成一个阿贝尔群:

a)  $ O+O=O; $ 

b)  $ \forall P=(x,y)\in E(F_{2^{m}})\backslash\{O\},P+O=O+P=P; $ 

c)  $ \forall P=(x,y)\in E(F_{2^{m}})\backslash\{O\} $ ，P 的逆元素  $ -P=(x,x+y) $ ， $ P+(-P)=O $ ；

d）两个非互逆的不同点相加的规则：

设  $ P_{1}=(x_{1},y_{1})\in E(F_{2^{m}})\backslash\{O\},P_{2}=(x_{2},y_{2})\in E(F_{2^{m}})\backslash\{O\} $ ，且  $ x_{1}\neq x_{2} $ 

设  $ P_{3}=(x_{3},y_{3})=P_{1}+P_{2} $ ，则：

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}+\lambda+x_{1}+x_{2}+a,\\ y_{3}=&\lambda\left(x_{1}+x_{3}\right)+x_{3}+y_{1},\end{aligned}\right. $$ 

其中  $ \lambda=\frac{y_{1}+y_{2}}{x_{1}+x_{2}} $ ;

e）倍点规则：

设  $ P_{1}=(x_{1},y_{1})\in E(F_{2^{m}})\setminus\{O\} $  且  $ x_{1}\neq0,P_{3}=(x_{3},y_{3})=P_{1}+P_{1} $ ，则：

 $$ \left\{\begin{aligned}x_{3}=&\lambda^{2}+\lambda+a,\\ y_{3}=&x_{1}^{2}+(\lambda+1)x_{3},\end{aligned}\right. $$ 

其中  $ \lambda = x_{1} + \frac{y_{1}}{x_{1}} $ 。

下面给出  $ F_{2^{5}} $  上椭圆曲线的两个示例。示例 6 用三项式基表示  $ F_{2^{5}} $ ，示例 7 用一种最优正规基表示  $ F_{2^{5}} $ 。

示例 6: 用三项式基表示  $ F_{25} $  的椭圆曲线

取不可约三项式  $ f(x)=x^{5}+x^{2}+1 $ ，取其一个根  $ \alpha=x $ ，则  $ F_{25}^{*} $  可由  $ \alpha $  生成：

 $ \alpha^{0}=(00001),\quad\alpha^{1}=(00010),\quad\alpha^{2}=(00100),\quad\alpha^{3}=(01000),\quad\alpha^{4}=(0000),\quad\alpha^{5}=(00101),\quad\alpha^{6}=(01010), $ 

 $ \alpha^{7}=(10100),\quad\alpha^{8}=(01101),\quad\alpha^{9}=(11010),\quad\alpha^{10}=(10001),\quad\alpha^{11}=(00111),\quad\alpha^{12}=(01110),\quad\alpha^{13}=(11100), $ 

 $ \alpha^{14}=(11101),\quad\alpha^{15}=(11111),\quad\alpha^{16}=(11011),\quad\alpha^{17}=(10011),\quad\alpha^{18}=(00011),\quad\alpha^{19}=(00110),\quad\alpha^{20}=(01100), $ 

 $ \alpha^{21}=(11000),\quad\alpha^{22}=(10101),\quad\alpha^{23}=(01111),\quad\alpha^{24}=(11110),\quad\alpha^{25}=(11001),\quad\alpha^{26}=(10111),\quad\alpha^{27}=(01011), $ 

 $ \alpha^{28}=(10110),\quad\alpha^{29}=(01001),\quad\alpha^{30}=(10010),\quad\alpha^{31}=\alpha^{0}=(00001) $ 。



取一条非超奇异曲线，方程为： $ y^{2}+xy=x^{3}+x^{2}+1 $ ，其中a=1,b=1。此方程可以表示如下：

 $$ (00001)y^{2}+(00001)xy=(00001)x^{3}+(00001)x^{2}+(00001) $$ 

这是因为乘法单位元为00001。

 $ F_{25} $  上此曲线的点为：

 $$ \left(0,1\right),\quad\left(\alpha^{3},\alpha^{15}\right),\quad\left(\alpha^{3},\alpha^{26}\right),\quad\left(\alpha^{6},\alpha^{21}\right),\quad\left(\alpha^{6},\alpha^{30}\right),\quad\left(\alpha^{7},\alpha^{8}\right),\quad\left(\alpha^{7},\alpha^{25}\right), $$ 

 $$ \left(\alpha^{12},\alpha^{11}\right),\quad\left(\alpha^{12},\alpha^{29}\right),\quad\left(\alpha^{14},\alpha^{16}\right),\quad\left(\alpha^{14},\alpha^{19}\right),\quad\left(\alpha^{17},\alpha^{13}\right),\quad\left(\alpha^{17},\alpha^{23}\right),\quad\left(\alpha^{19},\alpha^{4}\right). $$ 

 $$ \left(\alpha^{19},\alpha^{28}\right),\quad\left(\alpha^{24},\alpha^{22}\right),\quad\left(\alpha^{24},\alpha^{27}\right),\quad\left(\alpha^{25},\alpha^{2}\right),\quad\left(\alpha^{25},\alpha^{14}\right),\quad\left(\alpha^{28},\alpha\right),\quad\left(\alpha^{28},\alpha^{7}\right) $$ 

则  $ E(F_{25}) $  有 22 个点（包括无穷远点 O）。

a）取  $ P_{1}=(x_{1},y_{1})=(\alpha^{6},\alpha^{21}) $ ,  $ P_{2}=(x_{2},y_{2})=(\alpha^{3},\alpha^{15}) $ ，计算  $ P_{3}=(x_{3},y_{3})=P_{1}+P_{2} $ ;

 $ \lambda=\frac{y_{2}+y_{1}}{x_{2}+x_{1}}=\frac{\alpha^{15}+\alpha^{21}}{\alpha^{3}+\alpha^{6}}=\frac{\alpha^{11}}{\alpha}=\alpha^{10} $ ,

 $ x_{3}=\lambda^{2}+\lambda+x_{1}+x_{2}+a=\alpha^{20}+\alpha^{10}+\alpha^{6}+\alpha^{3}+1=\alpha^{24} $ ,

 $ y_{3}=\lambda(x_{1}+x_{3})+x_{3}+y_{1}=\alpha^{10}(\alpha^{6}+\alpha^{24})+\alpha^{24}+\alpha^{21}=\alpha^{22} $ ,

 $ P_{3}=(\alpha^{24},\alpha^{22}) $ 。

 $$ \begin{aligned}b)\quad P_{1}=&(\alpha^{6},\alpha^{21}), 计算 [2]P_{1}=(x_{3},y_{3})：\\&\lambda=x_{1}+\frac{y_{1}}{x_{1}}=\alpha^{6}+\frac{\alpha^{21}}{\alpha^{6}}=\alpha^{22},\\&x_{3}=\lambda^{2}+\lambda+a=\alpha^{44}+\alpha^{22}+1=\alpha^{3},\\&y_{3}=x_{1}^{2}+(\lambda+1)x_{3}=\alpha^{12}+(\alpha^{22}+1)\alpha^{3}=\alpha^{15},\\&[2]P_{1}=(\alpha^{3},\alpha^{15})。\end{aligned} $$ 

示例 7: 用Ⅱ型最优正规基表示  $ F_{25} $  的椭圆曲线

取生成元  $ \alpha=(11000) $ ，(11111) 是其乘法单位元，则  $ F_{25}^{*} $  可由  $ \alpha $  生成：

 $$ \alpha^{1}=(11000),\quad\alpha^{2}=(01100),\quad\alpha^{3}=(11100),\quad\alpha^{5}=(10111),\quad\alpha^{6}=(01110), $$ 

 $$ \alpha^{7}=\left(00001\right),\quad\alpha^{9}=\left(11110\right),\quad\alpha^{10}=\left(11011\right),\quad\alpha^{11}=\left(10010\right),\quad\alpha^{13}=\left(10100\right), $$ 

 $$ \alpha^{14}=(10000),\ \alpha^{15}=(11010),\ \alpha^{17}=(11001),\ \alpha^{18}=(01111),\ \alpha^{19}=(00010), $$ 

 $$ \alpha^{21}=\left(00101\right),\ \alpha^{22}=\left(01001\right),\ \alpha^{23}=\left(10101\right),\ \alpha^{25}=\left(00100\right),\ \alpha^{26}=\left(01010\right), $$ 

 $$ \alpha^{27}=\left(01011\right),\ \alpha^{28}=\left(01000\right),\ \alpha^{29}=\left(10110\right),\ \alpha^{30}=\left(01101\right),\ \alpha^{31}=\alpha^{0}=\left(11111\right)。 $$ 

取一非超奇异曲线，方程为： $ y^{2}+xy=x^{3}+1 $ ，其中a=0,b=1。此方程可以表示如下：

 $$ (11111)y^{2}+(11111)xy=(11111)x^{3}+(11111) $$ 

这是因为乘法单位元为 $ 11111 $ 。

 $ F_{25} $  上此曲线的点为：

 $$ \left(0,\alpha^{0}\right),\qquad\left(\alpha^{0},\alpha^{0}\right),\qquad\left(\alpha^{0},0\right),\qquad\left(\alpha^{3},\alpha^{17}\right),\quad\left(\alpha^{3},\alpha^{21}\right),\quad\left(\alpha^{5},\alpha^{8}\right),\quad\left(\alpha^{5},\alpha^{13}\right),\quad\left(\alpha^{6},\alpha^{3}\right), $$ 

 $$ \left(\alpha^{6},\alpha^{11}\right),\quad\left(\alpha^{7},\alpha^{21}\right),\quad\left(\alpha^{7},\alpha^{25}\right),\quad\left(\alpha^{9},\alpha^{2}\right),\quad\left(\alpha^{9},\alpha^{11}\right),\quad\left(\alpha^{10},\alpha^{16}\right),\left(\alpha^{10},\alpha^{26}\right),\quad\left(\alpha^{11},\alpha^{8}\right), $$ 

 $$ \left(\alpha^{11},\alpha^{16}\right),\quad\left(\alpha^{12},\alpha^{6}\right),\quad\left(\alpha^{12},\alpha^{22}\right),\quad\left(\alpha^{13},\alpha^{1}\right),\quad\left(\alpha^{13},\alpha^{2}\right),\quad\left(\alpha^{14},\alpha^{11}\right),\left(\alpha^{14},\alpha^{19}\right),\quad\left(\alpha^{17},\alpha^{24}\right), $$ 

 $$ \left(\alpha^{17},\alpha^{26}\right),\quad\left(\alpha^{18},\alpha^{4}\right),\quad\left(\alpha^{18},\alpha^{22}\right),\quad\left(\alpha^{19},\alpha^{26}\right),\quad\left(\alpha^{19},\alpha^{28}\right),\quad\left(\alpha^{20},\alpha^{1}\right),\quad\left(\alpha^{20},\alpha^{21}\right),\quad\left(\alpha^{21},\alpha^{4}\right), $$ 

 $$ \left(\alpha^{21},\alpha^{8}\right),\quad\left(\alpha^{22},\alpha^{1}\right),\quad\left(\alpha^{22},\alpha^{16}\right),\quad\left(\alpha^{24},\alpha^{12}\right),\quad\left(\alpha^{24},\alpha^{13}\right),\quad\left(\alpha^{25},\alpha^{13}\right),\left(\alpha^{25},\alpha^{14}\right),\quad\left(\alpha^{26},\alpha^{2}\right), $$ 

 $$ \left(\alpha^{26},\alpha^{4}\right),\quad\left(\alpha^{28},\alpha^{7}\right),\quad\left(\alpha^{28},\alpha^{22}\right)。 $$ 

则  $ E(F_{25}) $  有 44 个点（包括无穷远点 O），且  $ E(F_{25}) $  是循环群。

取  $ P=(\alpha^{3},\alpha^{17}) $ ，按加法运算规则，有：

 $$ \left[1\right]P=\left(\alpha^{3},\alpha^{17}\right),\qquad\left[2\right]P=\left(\alpha^{26},\alpha^{2}\right),\qquad\left[3\right]P=\left(\alpha^{14},\alpha^{19}\right),\qquad\left[4\right]P=\left(\alpha^{9},\alpha^{2}\right), $$ 

 $$ \left[5\right]P=\left(\alpha^{12},\alpha^{6}\right),\qquad\left[6\right]P=\left(\alpha^{13},\alpha^{1}\right),\qquad\left[7\right]P=\left(\alpha^{6},\alpha^{11}\right),\qquad\left[8\right]P=\left(\alpha^{10},\alpha^{26}\right), $$ 

 $$ \left[9\right]P=\left(\alpha^{24},\alpha^{12}\right),\qquad\left[10\right]P=\left(\alpha^{11},\alpha^{8}\right),\qquad\left[11\right]P=\left(\alpha^{0},\alpha^{0}\right),\qquad\left[12\right]P=\left(\alpha^{20},\alpha^{1}\right), $$ 

 $$ \left[13\right]P=\left(\alpha^{7},\alpha^{21}\right),\quad\left[14\right]P=\left(\alpha^{21},\alpha^{8}\right),\quad\left[15\right]P=\left(\alpha^{25},\alpha^{14}\right),\quad\left[16\right]P=\left(\alpha^{18},\alpha^{4}\right), $$ 

 $$ \left[17\right]P=\left(\alpha^{19},\alpha^{26}\right),\quad\left[18\right]P=\left(\alpha^{22},\alpha^{16}\right),\quad\left[19\right]P=\left(\alpha^{17},\alpha^{26}\right),\quad\left[20\right]P=\left(\alpha^{5},\alpha^{8}\right), $$ 

 $$ \left[21\right]P=\left(\alpha^{28},\alpha^{22}\right),\quad\left[22\right]P=\left(0,\alpha^{0}\right),\quad\left[23\right]P=\left(\alpha^{28},\alpha^{7}\right),\quad\left[24\right]P=\left(\alpha^{5},\alpha^{13}\right), $$ 

 $$ \left[25\right]P=\left(\alpha^{17},\alpha^{24}\right),\quad\left[26\right]P=\left(\alpha^{22},\alpha^{1}\right),\quad\left[27\right]P=\left(\alpha^{19},\alpha^{28}\right),\quad\left[28\right]P=\left(\alpha^{18},\alpha^{22}\right), $$ 

 $$ \left[29\right]P=\left(\alpha^{25},\alpha^{13}\right),\quad\left[30\right]P=\left(\alpha^{21},\alpha^{4}\right),\quad\left[31\right]P=\left(\alpha^{7},\alpha^{25}\right),\quad\left[32\right]P=\left(\alpha^{20},\alpha^{21}\right), $$ 

 $$ \left[33\right]P=\left(\alpha^{0},0\right),\qquad\left[34\right]P=\left(\alpha^{11},\alpha^{16}\right),\qquad\left[35\right]P=\left(\alpha^{24},\alpha^{13}\right),\qquad\left[36\right]P=\left(\alpha^{10},\alpha^{16}\right), $$ 

 $$ \left[37\right]P=\left(\alpha^{6},\alpha^{3}\right),\qquad\left[38\right]P=\left(\alpha^{13},\alpha^{2}\right),\qquad\left[39\right]P=\left(\alpha^{12},\alpha^{22}\right),\qquad\left[40\right]P=\left(\alpha^{9},\alpha^{11}\right), $$ 

 $$ \left[41\right]P=\left(\alpha^{14},\alpha^{11}\right),\quad\left[42\right]P=\left(\alpha^{26},\alpha^{4}\right),\quad\left[43\right]P=\left(\alpha^{3},\alpha^{21}\right),\quad\left[44\right]P=O。 $$ 

##### A.2.2.3 射影坐标表示

###### A.2.2.3.1 标准射影坐标系

 $ F_{2^{m}} $  上非超奇异椭圆曲线方程在标准射影坐标系下可以简化为  $ y^{2}z + xyz = x^{3} + ax^{2}z + bz^{3} $ ，其中  $ a, b \in F_{2^{m}} $ ，且  $ b \neq 0 $ 。 $ \left(E\left(F_{2^{m}}\right) = \left\{(x, y, z) \mid x, y, z \in F_{2^{m}} \text{ 且满足曲线方程 } y^{2}z + xyz = x^{3} + ax^{2}z + bz^{3}\right\}\right. $ 。对于  $ (x_{1}, y_{1}, z_{1}) $  和  $ (x_{2}, y_{2}, z_{2}) $ ，若存在某个  $ u \in F_{2^{m}} $  且  $ u \neq 0 $ ，使得： $ x_{1} = ux_{2} $ ， $ y_{1} = uy_{2} $ ， $ z_{1} = uz_{2} $ ，则称这两个三元组等价，表示同一个点。

若  $ z \neq 0 $ ，记 X = x/z，Y = y/z，则可从标准射影坐标表示转化为仿射坐标表示： $ Y^{2} + XY = X^{3} + aX^{2} + b $ ；

若 z=0，则  $ (0,1,0) $  对应的仿射坐标系下的点即无穷远点 O。

标准射影坐标系下， $ E(F_{2^{m}}) $  上点的加法运算定义如下：

椭圆曲线  $ E(F_{2^{m}}) $  上的点按照下面的加法运算规则, 构成一个交换群:

a） $ O+O=O; $ 

b)  $ \forall P=(x,y,z)\in E(F_{2^{m}})\backslash\{O\} $ ，则  $ P+O=O+P=P $ ;

c)  $ \forall P=(x,y,z)\in E\left(F_{2^{m}}\right)\backslash\{O\} $ ，P 的逆元素  $ -P=(ux,u(x+y),uz) $ ， $ u\in F_{2^{m}} $  且  $ u\neq0 $ ， $ P+(-P)=O $ ;

d）设点  $ P_{1}=(x_{1},y_{1},z_{1})\in E\left(F_{2^{m}}\right)\backslash\left\{O\right\} $ ， $ P_{2}=(x_{2},y_{2},z_{2})\in E\left(F_{2^{m}}\right)\backslash\left\{O\right\} $ ， $ P_{3}=P_{1}+P_{2}=(x_{3},y_{3},z_{3})\neq O $ ，

若  $ P_{1} \neq P_{2} $ ，则：

 $$ \lambda_{1}=x_{1}z_{2},\lambda_{2}=x_{2}z_{1},\lambda_{3}=\lambda_{1}+\lambda_{2},\lambda_{4}=y_{1}z_{2},\lambda_{5}=y_{2}z_{1},\lambda_{6}=\lambda_{4}+\lambda_{5},\lambda_{7}=z_{1}z_{2},\lambda_{8}=\lambda_{3}^{2}, $$ 

 $ \lambda_{9}=\lambda_{8}\lambda_{7},\lambda_{10}=\lambda_{3}\lambda_{8},\lambda_{11}=\lambda_{6}\lambda_{7}(\lambda_{6}+\lambda_{3})+\lambda_{10}+a\lambda_{9},x_{3}=\lambda_{3}\lambda_{11},y_{3}=\lambda_{6}(\lambda_{1}\lambda_{8}+\lambda_{11})+x_{3}+\lambda_{10}\lambda_{4},z_{3}=\lambda_{3}\lambda_{9}; $ 

若  $ P_{1}=P_{2} $ ，则：

 $$ \lambda_{1}=x_{1}z_{1},\lambda_{2}=x_{1}{}^{2},\lambda_{3}=\lambda_{2}+y_{1}z_{1},\lambda_{4}=\lambda_{1}{}^{2},\lambda_{5}=\lambda_{3}(\lambda_{1}+\lambda_{3})+a\lambda_{4},x_{3}=\lambda_{1}\lambda_{5}, $$ 

 $$ y_{3}=\lambda_{2}^{2}\lambda_{1}+\lambda_{3}\lambda_{5}+x_{3},z_{3}=\lambda_{1}\lambda_{4}。 $$ 

###### A.2.2.3.2 Jacobian 加重射影坐标系

 $ F_{2^{m}} $  上非超奇异椭圆曲线方程在 Jacobian 加重射影坐标系下可以简化为  $ y^{2} + xyz = x^{3} + ax^{2}z^{2} + bz^{6} $ ，其中  $ a, b \in F_{2^{m}} $ ，且  $ b \neq 0 $ 。 $ \left(E\left(F_{2^{m}}\right) = \left\{(x, y, z) \mid x, y, z \in F_{2^{m}}\right.\right. $  且满足曲线方程  $ y^{2} + xyz = x^{3} + ax^{2}z^{2} + bz^{6} $ 。对于  $ (x_{1}, y_{1}, z_{1}) $  和  $ (x_{2}, y_{2}, z_{2}) $ ，若存在某个  $ u \in F_{2^{m}} $  且  $ u \neq 0 $ ，使得： $ x_{1} = u^{2}x_{2}, y_{1} = u^{3}y_{2}, z_{1} = uz_{2} $ ，则称这两个三元组等价，表示同一个点。

若  $ z \neq 0 $ ，记  $ X = x / z^{2} $ ， $ Y = y / z^{3} $ ，则可从 Jacobian 加重射影坐标表示转化为仿射坐标表示： $ Y^{2} + XY = X^{3} + aX^{2} + b $ ；

若 z=0，则  $ (1,1,0) $  对应的仿射坐标系下的点即无穷远点 O。

Jacobian 加重射影坐标系下， $ E(F_{2^{m}}) $  上点的加法运算定义如下：

椭圆曲线  $ E(F_{2^{m}}) $  上的点按照下面的加法运算规则, 构成一个交换群:

a)  $ O+O=O; $ 

b)  $ \forall P=(x,y,z)\in E(F_{2^{m}})\setminus\{O\} $ ，则  $ P+O=O+P=P $ ;

c)  $ \forall P=(x,y,z)\in E(F_{2^{m}})\setminus\{O\} $ ，P 的逆元素  $ -P=(u^{2}x,u^{2}x+u^{3}y,uz) $ ， $ u\in F_{2^{m}} $  且  $ u\neq0 $ ， $ P+(-P)=O $ ；

d）设点  $ P_{1}=(x_{1},y_{1},z_{1})\in E(F_{2^{m}})\setminus\{O\} $ ， $ P_{2}=(x_{2},y_{2},z_{2})\in E(F_{2^{m}})\setminus\{O\} $ ， $ P_{3}=P_{1}+P_{2}=(x_{3},y_{3},z_{3})\neq O $ ，

若  $ P_{1} \neq P_{2} $ ，则：

 $$ \lambda_{1}=x_{1}z_{2}^{2},\lambda_{2}=x_{2}z_{1}^{2},\lambda_{3}=\lambda_{1}+\lambda_{2},\lambda_{4}=y_{1}z_{2}^{3},\lambda_{5}=y_{2}z_{1}^{3},\lambda_{6}=\lambda_{4}+\lambda_{5},\lambda_{7}=z_{1}\lambda_{3}, $$ 

 $$ \lambda_{8}=\lambda_{6}x_{2}+\lambda_{7}y_{2},z_{3}=\lambda_{7}z_{2},\lambda_{9}=\lambda_{6}+z_{3},x_{3}=a z_{3}^{2}+\lambda_{6}\lambda_{9}+\lambda_{3}^{3},y_{3}=\lambda_{9}x_{3}+\lambda_{8}\lambda_{7}^{2}； $$ 

若  $ P_{1}=P_{2} $ ，则：

 $$ z_{3}=x_{1}z_{1}^{2},x_{3}=x_{1}^{4}+b z_{1}^{8},\lambda=z_{3}+x_{1}^{2}+y_{1}z_{1},y_{3}=x_{1}^{4}z_{3}+\lambda x_{3}。 $$ 

#### A.2.3  $ F_{2^{m}} $  上椭圆曲线的阶

 $ F_{2^{m}} $  上的一条椭圆曲线 E 的阶是指点集  $ E(F_{2^{m}}) $  中元素的个数，记为  $ \#E(F_{2^{m}}) $ 。

由 Hasse 定理知： $ 2^{m}+1-2^{1+m/2}\leqslant\#E(F_{2^{m}})\leqslant2^{m}+1+2^{1+m/2} $ 

### A.3 椭圆曲线多倍点运算

#### A.3.1 概述

设 P 是椭圆曲线 E 上阶为 N 的点, k 为正整数, P 的 k 倍点为 Q, 即

 $$ Q=[k]P=\underbrace{P+P+\cdots+P}_{k}。 $$ 

#### A.3.2 椭圆曲线多倍点运算的实现

椭圆曲线多倍点运算的实现有多种方法，这里给出三种方法，以下都假设  $ 1 \leqslant k < N $ 。

## 算法一: 二进制展开法

输入: 点 P, l 比特的整数  $ k = \sum_{j=0}^{l-1} k_j 2^j $ ,  $ k_j \in \{0, 1\} $ .

输出:Q=[k]P。

a）置 Q=O；

b) j 从 l-1 下降到 0 执行：

1） $ Q=[2]Q; $ 

2）若  $ k_{i}=1 $ ，则  $ Q=Q+P $ ；

c） 输出 Q。

## 算法二：加减法

输入: 点 P, l 比特的整数  $ k = \sum_{j=0}^{l-1} k_j 2^j $ ,  $ k_j \in \{0, 1\} $ .

输出： $ Q=[k]P $ 。

a）设 3k 的二进制表示是  $ h_{r}h_{r-1}\cdots h_{1}h_{0} $ ，其中最高位  $ h_{r} $  为 1；

b）设 k 的二进制表示是  $ k_{r}k_{r-1}\cdots k_{1}k_{0} $ ，显然 r=l 或  $ l+1 $ ；

c）置 Q = P；

d）对 i 从 r-1 下降到 1 执行：

1） $ Q=[2]Q; $ 

2）若 $ h_{i}=1 $ ，且 $ k_{i}=0 $ ，则 $ Q=Q+P $ ；

3）若 $ h_{i}=0 $ ，且 $ k_{i}=1 $ ，则Q=Q-P；

e） 输出 Q。

注：减去点 $ (x,y) $ ，只要加上 $ (x,-y) $ （对域 $ F_{p} $ ），或者 $ (x,x+y) $ （对域 $ F_{2^{m}} $ ）。有多种不同的变种可以加速这一运算。

## 算法三：滑动窗法

输入: 点 P, l 比特的整数  $ k = \sum_{j=0}^{l-1} k_j 2^j, k_j \in \{0, 1\} $ 。

输出： $ Q=\left[k\right]P $ 。

设窗口长度 r > 1。

预计算

a)  $ P_{1}=P, P_{2}=[2]P; $ 

b) i 从 1 到  $ 2^{r-1}-1 $  计算  $ P_{2i+1}=P_{2i-1}+P_{2} $ ;

c) 置 j=l-1,Q=O;

主循环

d) 当  $ j \geqslant 0 $  执行：

1）若  $ k_{i}=0 $ ，则  $ Q=[2]Q,j=j-1; $ 

2）否则

——令 t 是使  $ j - t + 1 \leqslant r $  且  $ k_{t} = 1 $  的最小整数；

 $$ \frac{ 冏 }{ 冏 }h_{j}=\sum_{i=0}^{j-t}k_{t+i}2^{i}； $$ 

 $$ \begin{aligned}&——Q=[2^{j-t+1}]Q+P_{_{hj}}；\\&—— 置 j=t-1；\end{aligned} $$ 

e） 输出 Q。

#### A.3.3 椭圆曲线多倍点运算复杂度估计

不同坐标系下椭圆曲线点加运算和倍点运算的复杂度如表 A.6 和表 A.7。

<div style="text-align: center;">表 A.6 素域上椭圆曲线加法运算复杂度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">运算</td><td colspan="3">坐标系</td></tr><tr><td style='text-align: center;'>仿射坐标</td><td style='text-align: center;'>标准射影坐标</td><td style='text-align: center;'>Jacobian 加重射影坐标</td></tr><tr><td style='text-align: center;'>一般加法</td><td style='text-align: center;'>1I+2M+1S</td><td style='text-align: center;'>13M+2S</td><td style='text-align: center;'>12M+4S</td></tr><tr><td style='text-align: center;'>倍点</td><td style='text-align: center;'>1I+2M+2S</td><td style='text-align: center;'>8M+5S</td><td style='text-align: center;'>4M+6S</td></tr></table>

<div style="text-align: center;">表 A.7 二元扩域上椭圆曲线加法运算复杂度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">运算</td><td colspan="3">坐标系</td></tr><tr><td style='text-align: center;'>仿射坐标</td><td style='text-align: center;'>标准射影坐标</td><td style='text-align: center;'>Jacobian 加重射影坐标</td></tr><tr><td style='text-align: center;'>一般加法( $ a \neq 0 $ )</td><td style='text-align: center;'>1I + 2M + 1S</td><td style='text-align: center;'>15M + 1S</td><td style='text-align: center;'>15M + 5S</td></tr><tr><td style='text-align: center;'>倍点</td><td style='text-align: center;'>1I + 2M + 2S</td><td style='text-align: center;'>8M + 3S</td><td style='text-align: center;'>5M + 5S</td></tr></table>

注：表中 I、M 和 S 分别表示有限域中的求逆运算、乘法运算和平方运算。

计算多倍点 Q=[k]P，设 k 的比特数为 l，k 的 Hamming 重量为 W，则算法一需要 l-1 次椭圆曲线 2 倍点和 W-1 次点加运算；算法二需要 l 次椭圆曲线 2 倍点和 l/3 次点加运算；算法三分两部分：预计算时需要一次 2 倍点运算和  $ 2^{-1}-1 $  次点加运算，主循环部分需要 l-1 次 2 倍点运算和  $ l/(r+1)-1 $  次点加运算，共需要 l 次 2 倍点运算和  $ 2^{-1}+l/(r+1)-2 $  次点加运算。一般有  $ W\approx l/2 $ ，则多倍点运算的复杂度如下（基域为二元扩域时，假设  $ a\neq0 $ ，当 a=0 时，少一次乘法运算）：

算法一：

基域为素域：

仿射坐标下的复杂度： $ 1.5lI+3lM+2.5lS $ 

标准射影坐标下的复杂度： $ 14.5lM+6lS $ 

Jacobian 加重射影坐标下的复杂度： $ 10lM+8lS $ 

基域为二元扩域：

仿射坐标下的复杂度： $ 1.5lI+3lM+2.5lS $ 

标准射影坐标下的复杂度： $ 15.5lM+3.5lS $ 

Jacobian 加重射影坐标下的复杂度： $ 12.5lM+7.5lS $ 

算法二：

基域为素域：

仿射坐标下的复杂度： $ 1.33lI+2.67lM+2.33lS $ 

标准射影坐标下的复杂度： $ 12.33lM+5.67lS $ 

Jacobian 加重射影坐标下的复杂度： $ 8lM+7.33lS $ 

基域为二元扩域：

仿射坐标下的复杂度： $ 1.33lI+2.67lM+2.33lS $ 

标准射影坐标下的复杂度：13lM+3.33lS

Jacobian 加重射影坐标下的复杂度：10lM+6.67lS

算法三：

基域为素域：

仿射坐标下的复杂度： $ (l+l/(r+1)+2^{r-1}-2)(2M+I+S)+lS) $ 

标准射影坐标下的复杂度： $ (l/(r+1)+2^{r-1}-2)(13M+2S)+l(8M+5S)) $ 

Jacobian 加重射影坐标下的复杂度： $ (l/(r+1)+2^{r-1}-2)(12M+4S)+l(4M+6S)) $ 

基域为二元扩域：

仿射坐标下的复杂度： $ (l+l/(r+1)+2^{r-1}-2)(2M+I+S)+lS) $ 

标准射影坐标下的复杂度： $ (l/(r+1)+2^{r-1}-2)(15M+1S)+l(8M+3S)) $ 

Jacobian 加重射影坐标下的复杂度： $ (l/(r+1)+2^{r-1}-2)(15M+5S)+l(5M+5S)) $ 

### A.4 求解椭圆曲线离散对数问题的方法

#### A.4.1 椭圆曲线离散对数求解方法

已知椭圆曲线  $ E(F_{q}) $ ，阶为 n 的点  $ P \in E(F_{q}) $  及  $ Q \in \langle P \rangle $ ，椭圆曲线离散对数问题是指确定整数  $ k \in [0, n-1] $ ，使得  $ Q = [k] P $  成立。

ECDLP 现有攻击方法有：

• Pohlig-Hellman 方法: 设 l 是 n 的最大素因子, 则算法复杂度为  $ O(l^{1/2}) $ ;

• BSGS 方法: 时间复杂度与空间复杂度均为  $ (\pi n/2)^{1/2} $ ;

• Pollard 方法: 算法复杂度为  $ (\pi n / 2)^{1 / 2} $ ;

• 并行 Pollard 方法: 设 r 为并行处理器个数, 算法复杂度降至  $ (\pi n / 2)^{1 / 2} / r $ ;

MOV-方法: 把超奇异椭圆曲线及具有相似性质的曲线的 ECDLP 降到  $ F_{q} $  的小扩域上的离散对数问题(亚指数级计算复杂度算法);

- 异常曲线离散对数求解方法：对异常曲线 $$  \#E(F_{p}) = p  $$ 的曲线 $$ 的有效攻击方法（多项式级计算复杂度算法）；

- GHS-方法: 利用 Weil 下降技术求解扩张次数为合数的二元扩域上椭圆曲线离散对数问题, 将 ECDLP 转化为超椭圆曲线离散对数问题, 而求解高亏格的超椭圆曲线离散对数存在亚指数级计算复杂度算法。

对于一般曲线的离散对数问题，目前的求解方法都为指数级计算复杂度，未发现有效的亚指数级计算复杂度的一般攻击方法；而对于某些特殊曲线的离散对数问题，存在多项式级计算复杂度或者亚指数级计算复杂度算法。

选择曲线时，应避免使用易受上述方法攻击的密码学意义上的弱椭圆曲线。

#### A.4.2 安全椭圆曲线满足的条件

##### A.4.2.1 抗 MOV 攻击条件

A. Menezes、T. Okamoto、S. Vanstone、G. Frey 和 H. Rück 的约化攻击将有限域  $ F_{q} $  上的椭圆曲线离散对数问题约化为  $ F_{qB}(B>1) $  上的离散对数问题。这个攻击方法只有在 B 较小时是实用的，大多数椭圆曲线不符合这种情况。抗 MOV 攻击条件确保一条椭圆曲线不易受此约化方法攻击。多数  $ F_{q} $  上的椭圆曲线确实满足抗 MOV 攻击条件。

在验证抗 MOV 攻击条件之前，应选择一个 MOV 阈，它是使得求取  $ F_{qB} $  上的离散对数问题至少与求取  $ F_{q} $  上的椭圆曲线离散对数问题同样难的一个正整数 B。对于  $ q > 2^{191} $  的标准，要求  $ B \geqslant 27 $ 。选择

 $ B \geqslant 27 $  也限制了对非超奇异椭圆曲线的选取。

下述算法用于验证椭圆曲线系统参数是否满足抗 MOV 攻击条件。

输入：MOV 阈 B，素数幂 q 和素数 n [n 是  $ \#E(F_{q}) $  的素因子，其中  $ E(F_{q}) $  是  $ F_{q} $  上的椭圆曲线]。输出：若  $ F_{q} $  上包含 n 阶基点的椭圆曲线满足抗 MOV 攻击条件，则输出“正确”；否则输出“错误”。

a）置 t=1;

b）对 i 从 1 到 B 执行：

1）置  $ t=(t \cdot q) \mod n $  ；

2）若 t=1，则输出“错误”并结束；

c） 输出“正确”。

##### A.4.2.2 抗异常曲线攻击条件

设  $ E(F_{p}) $  为定义在素域  $ F_{p} $  上的椭圆曲线，若  $ \#E(F_{p})=p $ ，则称椭圆曲线  $ E(F_{p}) $  为异常曲线。N.Smart、T.Satoh 和 K.Araki 证明可在多项式时间内求解异常曲线的离散对数。抗异常曲线攻击条件为  $ \#E(F_{p})\neq p $ ，满足此条件确保椭圆曲线不受异常曲线攻击。 $ F_{p} $  上的绝大多数椭圆曲线确实满足抗异常曲线攻击条件。

下述算法用于验证椭圆曲线系统参数是否满足抗异常曲线攻击条件。

输入： $ F_{p} $ 上的椭圆曲线 $ E(F_{p}) $ ，阶 $ N=\#E(F_{p}) $ 。

输出：若  $ E(F_{p}) $  满足抗异常曲线攻击条件，则输出消息“正确”；否则输出消息“错误”。

a）若 N=p，则输出“错误”；否则输出“正确”。

##### A.4.2.3 其他条件

为避免 Pohlig-Hellman 方法和 Pollard 方法的攻击，基点的阶 n 应是一个足够大的素数；为避免 GHS 方法的攻击， $ F_{2^{m}} $  中的 m 应该选择素数。

### A.5 椭圆曲线上点的压缩

#### A.5.1 概述

对于椭圆曲线  $ E(F_{q}) $  上的任意非无穷远点  $ P=(x_{P},y_{P}) $ ，该点能由仅存储 x- 坐标  $ x_{P}\in F_{q} $  以及由  $ x_{P} $  和  $ y_{P} $  导出的一个特定比特简洁地表示，称为点的压缩表示。

#### A.5.2  $ F_{p} $  上椭圆曲线点的压缩与解压缩方法

设  $ P=(x_{P},y_{P}) $  是定义在  $ F_{P} $  上椭圆曲线  $ E:y^{2}=x^{3}+ax+b $  上的一个点， $ \widetilde{y}_{P} $  为  $ y_{P} $  的最右边的一个比特，则点 P 可由  $ x_{P} $  和比特  $ \widetilde{y}_{P} $  表示。

由  $ x_{P} $  和  $ \tilde{y}_{P} $  恢复  $ y_{P} $  的方法如下：

a）计算域元素  $ \alpha=(x_{p}^{3}+ax_{p}+b)\bmod p $  ；

b）计算  $ \alpha \mod p $  的平方根  $ \beta $  (参见 B.1.4)，若输出是“不存在平方根”，则报错；

c) 若  $ \beta $  的最右边比特等于  $ \widetilde{y}_{P} $ ，则置  $ y_{P}=\beta $ ；否则置  $ y_{P}=p-\beta $ 。

#### A.5.3  $ F_{2^{m}} $  上椭圆曲线点的压缩与解压缩方法

设  $ P=(x_{P},y_{P}) $  是定义在  $ F_{2^{m}} $  上的椭圆曲线  $ E:y^{2}+xy=x^{3}+ax^{2}+b $  上的一个点。若  $ x_{P}=0 $ ，则令  $ \widetilde{y}_{P} $  为 0；若  $ x_{P}\neq0 $ ，则令  $ \widetilde{y}_{P} $  为域元素  $ y_{P}\cdot x_{P}^{-1} $  的最右边一个比特。

由  $ x_{P} $  和  $ \widetilde{y}_{P} $  恢复  $ y_{P} $  的方法如下：

a）若  $ x_{P}=0 $ ，则  $ y_{P}=b^{2^{m-1}}\left(y_{P}\right) $  是 b 在  $ F_{2^{m}} $  中的平方根）；

b）若  $ x_{p} \neq 0 $ ，则执行：

1）在  $ F_{2^{m}} $  中计算域元素  $ \beta = x_{P} + a + bx_{P}^{-2} $ ;

2）寻找一个域元素 z，使得  $ z^{2} + z = \beta $ （参见 B.1.6），若输出是“解不存在”，则报错；

3）设 $ \tilde{z} $ 为z的最后一个比特；

4）若  $ y_{P} \neq \tilde{z} $ ，则置  $ z = z + 1 $ ，其中 1 是乘法单位元；

计算  $ y_{P}=x_{P}\cdot z_{0} $ 

# 附录 B

# (资料性附录)

# 数论算法

### B.1 有限域和模运算

#### B.1.1 有限域中的指数运算

设 a 是正整数, g 是域  $ F_{q} $  上的元素, 指数运算是计算  $ g^{a} $  的运算过程。通过以下概述的二进制方法可以有效地执行指数运算。

输入:正整数 a, 域  $ F_{q} $ , 域元素 g。

输出： $ g^{a} $ 

a）置  $ e=a \bmod(q-1) $ ，若 e=0，则输出 1；

b）设 e 的二进制表示是  $ e=e_{r}e_{r-1}\cdots e_{1}e_{0} $ ，其最高位  $ e_{r} $  为 1；

c）置x=g；

d）对 i 从 r-1 下降到 0 执行：

1）置 $ x=x^{2} $ ;

2）若 $ e_{i}=1 $ ，则置 $ x=g\cdot x $ ；

e） 输出 x。

其他加速算法参见 Brickell et al. 1993、Knuth 1981。

#### B.1.2 有限域中的逆运算

设 g 是域  $ F_{q} $  上的非零元素，则逆元素  $ g^{-1} $  是使得  $ g \cdot c = 1 $  成立的域元素 c。由于  $ c = g^{q-2} $ ，因此求逆可通过指数运算实现。注意到，若 q 是素数，g 是满足  $ 1 \leqslant g \leqslant q-1 $  的整数，则  $ g^{-1} $  是整数  $ c, 1 \leqslant c \leqslant q-1 $ ，且  $ g \cdot c \equiv 1 \pmod{q} $ 。

输入: 域  $ F_{q}, F_{q} $  中的非零元素 g。

输出:逆元素  $ g^{-1} $ 

a）计算  $ c=g^{q-2} $  (参见 B.1.1);

b） 输出 c。

更为有效的方法是扩展的欧几里德算法，参见 Knuth 1981。

#### B.1.3 Lucas 序列的生成

令 X 和 Y 是非零整数，X 和 Y 的 Lucas 序列  $ U_{k} $ 、 $ V_{k} $  的定义如下：

 $ U_{0}=0,U_{1}=1 $ ,当 $ k\geqslant2 $ 时, $ U_{k}=X\cdot U_{k-1}-Y\cdot U_{k-2} $ ;

 $ V_{0}=2,V_{1}=X $ ，当 $ k\geqslant2 $ 时， $ V_{k}=X\cdot V_{k-1}-Y\cdot V_{k-2} $ 。

上述递归式适于计算 k 值较小的  $ U_{k} $  和  $ V_{k} $  。对大整数 k，下面的算法可有效地计算  $ U_{k} \bmod p $  和  $ V_{k} \bmod p $  。

输入: 奇素数 p, 整数 X 和 Y, 正整数 k。

输出： $ U_{k} \mod p $  和  $ V_{k} \mod p $ 。

a）置 $ \Delta=X^{2}-4Y $ ；

b）设 k 的二进制表示是  $ k=k_{r}k_{r-1}\cdots k_{1}k_{0} $ ，其中最高位  $ k_{r} $  为 1；

c）置 U=1, V=X；

d）对 i 从 r-1 下降到 0 执行：

1）置 $ (U,V)=((U\cdot V)\bmod p,((V^{2}+\Delta\cdot U^{2})/2)\bmod p) $ ;

2）若  $ k_{i}=1 $ ，则置  $ (U,V)=((X\cdot U+V)/2)\bmod p,\left((X\cdot V+\Delta\cdot U)/2\right)\bmod p $ ；

e）输出 U 和 V。

#### B.1.4 模素数平方根的求解

设 p 是奇素数，g 是满足  $ 0 \leqslant g < p $  的整数，g 的平方根  $ (\bmod p) $  是整数  $ y, 0 \leqslant y < p $ ，且  $ y^{2} \equiv g \pmod{p} $ 。

若 g=0，则只有一个平方根，即 y=0；若  $ g \neq 0 $ ，则 g 有 0 个或 2 个平方根（modp），若 y 是其中一个平方根，则另一个平方根就是 p-y。

下面的算法可以确定 g 是否有平方根  $ (mod p) $ ，若有，就计算其中一个根。

输入: 奇素数 p, 整数 g, 0 < g < p.

输出：若存在 g 的平方根，则输出一个平方根 mod p，否则输出“不存在平方根”。

算法 1: 对  $ p \equiv 3 \pmod{4} $ ，即存在正整数 u，使得  $ p = 4u + 3 $ 。

a）计算  $ y=g^{u+1} \mod p $  (参见 B.1.1);

b）计算  $ z=y^{2} \mod p $  ；

c) 若 z=g，则输出 y；否则输出“不存在平方根”。

算法 2: 对  $ p \equiv 5 \pmod{8} $ ，即存在正整数 u，使得  $ p = 8u + 5 $ 。

a）计算  $ z=g^{2u+1} \mod p $  (参见 B.1.1);

b) 若  $ z \equiv 1 \pmod{p} $ ，计算  $ y = g^{u+1} \mod p $ ，输出 y，终止算法；

c) 若  $ z \equiv -1 \pmod{p} $ ，计算  $ y = (2g \cdot (4g)^{u}) \mod p $ ，输出 y，终止算法；

d）输出“不存在平方根”。

算法 3: 对  $ p \equiv 1 \pmod{8} $ ，即存在正整数 u，使得  $ p = 8u + 1 $ 。

a）置Y=g；

b）生成随机数 X,0<X<p；

c) 计算 Lucas 序列元素(参见 B.1.3):  $ U=U_{4u+1} \mod p $ ,  $ V=V_{4u+1} \mod p $ ;

d）若  $ V^{2} \equiv 4Y(\bmod p) $ ，则输出  $ y = (V/2) \bmod p $ ，并终止；

e）若  $ U \mod p \neq 1 $  且  $ U \mod p \neq p - 1 $ ，则输出“不存在平方根”，并终止；

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_1099_190_1132.jpg" alt="Image" width="3%" /></div>


f) 返回步骤 b)。

#### B.1.5 迹函数和半迹函数

设  $ \alpha $  是  $ F_{2^{m}} $  中的元素,  $ \alpha $  的迹是:  $ \mathrm{Tr}(\alpha)=\alpha+\alpha^{2}+\alpha^{2^{2}}+\cdots+\alpha^{2^{m}-1} $ 

 $ F_{2^{m}} $  中有一半元素的迹是 0，一半元素的迹是 1。迹的计算方法如下：

若  $ F_{2^{m}} $  中的元素用正规基表示：

设  $ \alpha=(\alpha_{0}\alpha_{1}\cdots\alpha_{m-1}) $ ，则  $ \mathrm{Tr}(\alpha)=\alpha_{0}\bigoplus\alpha_{1}\bigoplus\cdots\bigoplus\alpha_{m-1} $ 。

若  $ F_{2^{m}} $  中元素用多项式基表示：

a）置 $ T=\alpha; $ 

b）对 i 从 1 到 m-1 执行：

1） $ T=T^{2}+\alpha $ 

c） 输出  $ \mathrm{Tr}(\alpha)=T $  。

若 m 是奇数，则  $ \alpha $  的半迹是： $ \alpha + \alpha^{22} + \alpha^{24} \cdots + \alpha^{2^{m-1}} $ 

若  $ F_{2^{m}} $  中元素用多项式基表示，则半迹可通过下面的方法计算：

a）置  $ T=\alpha $ ;

b）对 i 从 1 到  $ (m-1)/2 $  执行：

1） $ T=T^{2} $ ;

2） $ T=T^{2}+\alpha $ 

c） 输出半迹 T。

#### B.1.6  $ F_{2^{m}} $  上二次方程的求解

设  $ \beta $  是  $ F_{2^{m}} $  中元素，则方程  $ z^{2} + z = \beta $  在  $ F_{2^{m}} $  上有  $ 2 - 2\mathrm{Tr}(\beta) $  个解，因此方程有 0 个或 2 个解。若  $ \beta = 0 $ ，则解是 0 和 1；若  $ \beta \neq 0 $ ，z 是方程的解，则  $ z + 1 $  也是方程的解。

给定  $ \beta $ ，利用下面的算法可确定解 z 是否存在，若存在，则算出一个解。

输入： $ F_{2^{m}} $  及表示其元素的一组基，以及元素  $ \beta \neq 0 $ 。

输出：若存在解，则输出元素z，使 $ z^{2}+z=\beta $ ；否则输出“无解”。

算法1：对正规基表示

a）设 $ (\beta_{0}\beta_{1}\cdots\beta_{m-1}) $ 是 $ \beta $ 的表示；

b) 置  $ z_{0}=0 $ ;

c) 对 i 从 1 到 m-1 执行：

1） $ z_{i}=z_{i-1}\oplus\beta_{i} $ 

d) 置  $ z=(z_{0}z_{1}\cdots z_{m-1}) $ ;

e） 计算  $ \gamma=z^{2}+z; $ 

f) 若  $ \gamma=\beta $ ，则输出 z；否则输出“无解”。

算法 2: 对多项式基  $ (m $  是奇数 $ ) $  表示

a）计算  $ z=\beta $  的半迹(参见 B.1.5);

b）计算  $ \gamma=z^{2}+z; $ 

c）若  $ \gamma=\beta $ ，则输出 z；否则输出“无解”。

算法 3: 对任意基

a）选择  $ \tau\in F_{2^{m}} $  ，使得  $ \tau+\tau^{2}+\cdots+\tau^{2^{m}-1}=1 $  ；

b）置z=0, $ w=\beta; $ 

c）对 i 从 1 到 m-1 执行：

1） $ z=z^{2}+w^{2}\cdot\tau; $ 

2)  $ w=w^{2}+\beta; $ 

d）若  $ w \neq 0 $ ，则输出“无解”，并终止；

e） 输出 z。

#### B.1.7 整数模素数阶的检查

设 p 是一个素数，整数 g 满足  $ 1 \leq g \leq p $ ， $ g \mod p $  的阶是指最小正整数 k，使得  $ g^{k} \equiv 1 \pmod{p} $ 。以下算法测试  $ g \mod p $  的阶是否为 k。

输入: 素数 p, 整除 p-1 的正整数 k, 整数 g 满足 1 < g < p.

输出: 若 k 是 g mod p 的阶, 则输出为“正确”, 否则输出“错误”。

a）确定 k 的素因子；

b）若  $ g^{k} \mod p \neq 1 $ ，则输出“错误”，终止；

c）对 k 的每一个素因子 l，执行：

1）若  $ g^{k/l} \bmod p = 1 $ ，则输出“错误”，终止；

d）输出“正确”。

#### B.1.8 整数模素数阶的计算

设 p 是素数，整数 g 满足 1 < g < p 。下面的算法确定 g mod p 的阶，此算法只在 p 较小时有效。

输入: 素数 p 和满足 1 < g < p 的整数 g。

输出:  $ g \mod p $  的阶 k 。

a）置b=g,j=1;

b)  $  b = (g \cdot b) \bmod p, j = j + 1;  $ 

c) 若  $ b \geq 1 $ ，则返回步骤 b);

d）输出 k=j。

#### B.1.9 模素数的阶为给定值的整数的构造

设 p 是素数且 T 整除 p-1，下面的算法可求出  $ F_{p} $  中阶为 T 的元素。此算法只在 p 值较小时有效。

输入: 素数 p 和整除 p-1 的整数 T。

输出: 模 p 的阶为 T 的整数 u。

a）随机生成整数 g,1<g<p；

b）计算 g mod p 的阶 k（参见 B.1.8）；

c）若 T 不整除 k，则返回步骤 a）；

d）输出  $ u=g^{k/T} \mod p $  。

#### B.1.10 概率素性检测

u 是一个大的正整数，下面的概率算法（Miller-Rabin 检测）将确定 u 是素数还是合数。

输入:一个大的奇数 u 和一个大的正整数 T。

输出：“概率素数”或“合数”。

a）计算 v 和奇数 w，使得  $ u-1=2^{v}\cdot w $ ；

b）对 j 从 1 到 T 执行：

1）在区间 $$ 2, u-1 $$ 中选取随机数a；

2）置 $ b=a^{w}\bmod u $ ；

3）若 b=1 或 u-1，转到步骤6）；

4）对 i 从 1 到 v-1 执行：

——置  $ b=b^{2} $  modu ;

——若 b=u-1 ，转到步骤6）；

——若 b=1 ，输出“合数”并终止；

——下一个i；

5）输出“合数”，并终止；

6）下一个j；

c） 输出“概率素数”。

若算法输出“合数”，则 u 是一个合数。若算法输出“概率素数”，则 u 是合数的概率小于  $ 2^{-2T} $  。这样，通过选取足够大的 T，误差可以忽略。

#### B.1.11 近似素性检测

给定一个试除的界  $ l_{\max} $ ，若正整数 h 的每个素因子都不超过  $ l_{\max} $ ，则称 h 为  $ l_{\max} $ -光滑的。给定一个正整数  $ r_{\min} $ ，若存在某个素数  $ v \geqslant r_{\min} $ ，使得正整数  $ u = h \cdot v $ ，且整数 h 是  $ l_{\max} $ -光滑的，则称 u 为近似素

数。下面的算法检查 u 的近似素性。

输入: 正整数 u,  $ l_{max} $  和  $ r_{min} $ 

输出: 若 u 是近似素数则输出 h 和 v, 否则输出“不是近似素数”。

a）置 v=u,h=1;

b) 对 l 从 2 到  $ l_{max} $  执行：

1）若 l 是合数，则转到步骤 3）；

2）当 l 整除 v 时，循环执行：

——置 v=v/l 和  $ h=h\cdot l $ ;

——若  $ v<r_{\min} $ ，则输出“不是近似素数”并终止；

3）下一个l；

c）若 v 是概率素数，则输出 h 和 v 且终止；

d） 输出“不是近似素数”。

### B.2 有限域上的多项式

#### B.2.1 最大公因式

若  $ f(t) \neq 0 $  和  $ g(t) \neq 0 $  是系数在域  $ F_{q} $  中的两个多项式，则唯一地存在系数也在域  $ F_{q} $  中的次数最高的首一多项式  $ d(t) $ ，它同时整除  $ f(t) $  和  $ g(t) $ 。多项式  $ d(t) $  称为  $ f(t) $  和  $ g(t) $  的最大公因子，记为  $ \gcd(f(t), g(t)) $ 。下面的算法（欧几里德算法）计算两个多项式的最大公因子。

输入:有限域  $ F_{q}, F_{q} $  上的两个非零多项式  $ f(t) \neq 0, g(t) \neq 0 $ 。

输出: $ d(t)=\gcd(f(t),g(t)) $ 。

a）置 $ a(t)=f(t) $ ， $ b(t)=g(t) $ ；

b) 当  $ b(t) \neq 0 $  时，循环执行：

1）置  $ c(t)=a(t)\bmod b(t) $ ;

2）置 $ a(t)=b(t) $ ;

3）置 $ b(t)=c(t) $ ;

c) 设  $ \alpha $  是  $ a(t) $  的首项系数并输出  $ \alpha^{-1}a(t) $ 。

#### B.2.2  $ F_{2} $  上不可约多项式在  $ F_{2^{m}} $  中根的求解

设  $ f(t) $  是  $ F_{2} $  上 m 次不可约多项式，则  $ f(t) $  在域  $ F_{2^{m}} $  中有 m 个不同的根。利用以下的算法可有效地求解一个根。

输入： $ F_{2} $  上 m 次不可约多项式  $ f(t) $ ，域  $ F_{2^{m}} $ 。

输出： $ f(t) $  在  $ F_{2^{m}} $  中的一个根。

a）置 $ g(t)=f(t) $ ;

b) 当  $ \deg(g)>1 $  时，循环执行：

1）随机选择 $ u\in F_{2^{m}} $ ;

2）置 $ c(t)=ut $ ；

3）对 i 从 1 到 m-1 执行：

 $$ \text{——}c\left(t\right)=\left(c\left(t\right)^{2}+u t\right)\bmod g\left(t\right); $$ 

4）置 $ h(t)=\gcd(c(t),g(t)) $ ;

5）若  $ h(t) $  是常数，或者  $ \deg(g)=\deg(h) $ ，则返回步骤1）；

6）若  $ 2\deg(h) > \deg(g) $ ，则置  $ g(t) = g(t)/h(t) $ ；否则，置  $ g(t) = h(t) $ ；

c） 输出  $ g(0) $ 。

注：上述多项式运算皆在  $ F_{2^{m}} $  中进行。

#### B.2.3 基的转换

给定域  $ F_{2^{m}} $  ，以及在  $ F_{2} $  上两组基（多项式基或正规基） $ B_{1} $  和  $ B_{2} $  ，下面的算法可在基  $ B_{1} $  和  $ B_{2} $  之间进行转换。

a）令  $ f(t) $  是  $ B_{2} $  的域多项式，即：

1）若  $ B_{2} $  是多项式基，设  $ f(t) $  是  $ F_{2} $  上 m 次约化多项式；

2）若  $ B_{2} $  是Ⅰ型最优正规基，设  $ f(t)=t^{m}+t^{m-1}+\cdots+t+1 $ ;

3）若  $ B_{2} $  是Ⅱ型最优正规基，设  $ f(t)=\sum_{0\leq i\leq m}t^{i} $ 

其中 a, b 的二进制表示为： $ a = \sum u_{i} 2^{i}, b = \sum w_{i} 2^{i} $ ，则  $ a \prec b $  表示对所有的 i，都有  $ u_{i} \leqslant w_{i} $ ；

4）若  $ B_{2} $  是类型  $ T \geqslant 3 $  的高斯正规基，则：

——置  $ p = T \cdot m + 1 $ ;

——生成模 p 的阶为 T 的整数 u（参见 B.1.9）；

——对 k 从 1 到 m 执行：

 $$ e_{k}=\sum_{j=0}^{T-1}\exp\left(\frac{2^{k}u^{j}\pi i}{p}\right), 其中 i 为虚数单位； $$ 

——计算多项式

 $$ g\left(t\right)=\prod_{k=1}^{m}\left(t-e_{k}\right);[ 多项式 \;g\left(t\right)\; 的系数为整数 ] $$ 

——输出  $ f(t)=g(t)\bmod2 $ 。

复数  $ e_{k} $  的计算必须足够精确才能与  $ g(t) $  的每一个系数保持一致。由于每一个系数都是整数，这就意味着计算系数过程中的偏差必须小于 1/2。

b）设  $ \gamma $  是相对于  $ B_{1} $  的  $ f(t) $  的根 ( $ \gamma $  可通过 B.2.2 中的方法计算)。

c）令  $ \Gamma $  是如下矩阵：

 $$ \Gamma=\left\{\begin{aligned}\gamma_{0,0}\quad&\gamma_{0,1}\quad\cdots\quad\gamma_{0,m-1}\\ \gamma_{1,0}\quad&\gamma_{1,1}\quad\cdots\quad\gamma_{1,m-1}\\ \vdots\quad&\vdots\quad\ddots\quad\vdots\\ \gamma_{m-1,0}\quad&\gamma_{m-1,1}\quad\cdots\quad\gamma_{m-1,m-1}\end{aligned}\right\}, $$ 

其中的项  $ \gamma_{i,j} $  定义如下：

1）若  $ B_{2} $  是多项式基，则相对于  $ B_{1} $  有：

\[\begin{aligned}&1=(\gamma_{0,0}\gamma_{0,1}\cdots\gamma_{0,m-1}),\\&\gamma=(\gamma_{1,0}\gamma_{1,1}\cdots\gamma_{1,m-1}),\\&\gamma^{2}=(\gamma_{2,0}\gamma_{2,1}\cdots\gamma_{2,m-1}),\\&\cdots\cdots\\&\gamma^{m-1}=(\gamma_{m-1,0}\gamma_{m-1,1}\cdots\gamma_{m-1,m-1})。\\& 亘

(通过不断地乘以  $ \gamma $  得到项  $ \gamma_{i,j} $ )

2）若  $ B_{2} $  是高斯正规基（类型  $ T \geqslant 1 $ ），则相对于  $ B_{1} $  有：

 $$ \begin{aligned}&\gamma=(\gamma_{0,0}\gamma_{0,1}\cdots\gamma_{0,m-1}),\\&\gamma^{2}=(\gamma_{1,0}\gamma_{1,1}\cdots\gamma_{1,m-1}),\\&\gamma^{4}=(\gamma_{2,0}\gamma_{2,1}\cdots\gamma_{2,m-1}),\\&\cdots\cdots\\ \end{aligned} $$ 

 $$ \gamma^{2^{m-1}}=(\gamma_{m-1,0}\gamma_{m-1,1}\cdots\gamma_{m-1,m-1})。 $$ 

(通过不断求  $ \gamma $  的平方得到项  $ \gamma_{i,i} $ )

d）若一个元素相对于 $ B_{2} $ 的表示是 $ (\beta_{0}\beta_{1}\cdots\beta_{m-1}) $ ，则它相对于 $ B_{1} $ 的表示为：

 $$ (\alpha_{0}\alpha_{1}\cdots\alpha_{m-1})=(\beta_{0}\beta_{1}\cdots\beta_{m-1})\Gamma; $$ 

若一个元素相对于  $ B_{1} $  的表示是  $ (\alpha_{0}\alpha_{1}\cdots\alpha_{m-1}) $ ，则它相对于  $ B_{2} $  的表示为：

 $$ (\beta_{0}\beta_{1}\cdots\beta_{m-1})=(\alpha_{0}\alpha_{1}\cdots\alpha_{m-1})\Gamma^{-1}, $$ 

其中  $ \Gamma^{-1} $  表示  $ \Gamma $  的模 2 逆。

示例：

假定  $ B_{1} $  是  $ F_{25} $  的多项式基，其域多项式为  $ t^{5} + t^{2} + 1 $ ， $ B_{2} $  是  $ F_{25} $  的Ⅱ型最优正规基，则域多项式为  $ f(t) = t^{5} + t^{4} + t^{2} + t + 1 $ ， $ f(t) $  相对于  $ B_{1} $  的一个根为  $ \gamma = (01100) $ ，则：

 $$ \begin{aligned}&\gamma=(01100),\\&\gamma^{2}=(11010),\\&\gamma^{4}=(00011),\\&\gamma^{8}=(00101),\\&\gamma^{16}=(10001)。\\ \end{aligned} $$ 

 $$ \begin{aligned} 因此 \Gamma=\begin{pmatrix}{{{0}}}&{{{1}}}&{{{1}}}&{{{0}}}&{{{0}}} \\{{{1}}}&{{{1}}}&{{{0}}}&{{{1}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0}}}&{{{1}}}&{{{1}}} \\{{{0}}}&{{{0}}}&{{{1}}}&{{{0}}}&{{{1}}} \\{{{1}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{1}}}\end{pmatrix},\Gamma^{-1}=\begin{cases}{{{1}}}&{{{1}}}&{{{1}}}&{{{1}}}&{{{0}}} \\{{{0}}}&{{{1}}}&{{{1}}}&{{{0}}}&{{{1}}} \\{{{1}}}&{{{1}}}&{{{1}}}&{{{0}}}&{{{1}}} \\{{{1}}}&{{{1}}}&{{{0}}}&{{{1}}}&{{{1}}} \\{{{1}}}&{{{1}}}&{{{1}}}&{{{1}}}&{{{1}}}\end{cases}\end{aligned}。 $$ 

若  $ \lambda $  相对于  $ B_{2} $  的表示为  $ \lambda=(11001) $ ，则  $ \lambda $  相对于  $ B_{1} $  的表示是： $ (00011)=(11001)\Gamma $ ；

若  $ \lambda $  相对于  $ B_{1} $  的表示为  $ \lambda=(10110) $ ，则  $ \lambda $  相对于  $ B_{2} $  的表示是： $ (11000)=(10110)\Gamma^{-1} $ 。

#### B.2.4  $ F_{2} $  上多项式不可约性的检测

设  $ f(x) $  是  $ F_{2} $  上的多项式，利用下面的算法可以有效地检测  $ f(x) $  的不可约性。

输入: $ F_{2} $ 上的多项式 $ f(x) $ 。

输出: 若  $ f(x) $  在  $ F_{2} $  上不可约, 则输出“正确”; 否则, 输出“错误”。

a）置  $ d=\deg(f(x)) $ ；

b）置 $ u(x)=x $ ；

c) 对 i 从 1 到  $ \lfloor d/2 \rfloor $  执行：

1）置  $ u(x)=u(x)^{2}\bmod f(x) $ ;

2）置 $ g(x)=\gcd(u(x)+x,f(x)) $ ;

3）若  $ g(x) \neq 1 $ ，则输出“错误”并终止；

d）输出“正确”。

### B.3 椭圆曲线算法

#### B.3.1 椭圆曲线阶的计算

对于有限域上随机的椭圆曲线，其阶的计算是一个相当复杂的问题。目前有效的计算方法有 SEA 算法和 Satoh 算法。关于计算椭圆曲线阶的详细描述参见 Lehmann et al. 1994、Müller 1995、Satoh 2000、Satoh 2002、Satoh et al. 2003、Schoof 1985 和 Schoof 1995。

#### B.3.2 椭圆曲线上点的寻找

给定有限域上的椭圆曲线，利用下面的算法可有效地找出曲线上任意一个非无穷远点。

##### B.3.2.1  $ F_{p} $  上的椭圆曲线

输入: 素数 p,  $ F_{p} $  上一条椭圆曲线 E 的参数 a, b。

输出:E 上一个非无穷远点。

a）选取随机整数 $ x,0\leqslant x<p; $ 

b）置 $ a=(x^{3}+ax+b)\bmod p $ ；

c) 若  $ \alpha=0 $ ，则输出  $ (x,0) $  并终止；

d）求  $ \alpha \mod p $  的平方根(参见 B.1.4);

e) 若步骤 d) 的输出是“不存在平方根”，则返回步骤 a);

否则，步骤 d) 的输出是整数 y, 0 < y < p，且  $ y^{2} \equiv \alpha \pmod{p} $ ;

f） 输出 $ (x,y) $ 。

##### B.3.2.2  $ F_{2^{m}} $  上的椭圆曲线

输入:二元扩域  $ F_{2^{m}} $ ,  $ F_{2^{m}} $  上的椭圆曲线 E 的参数 a, b。

输出:E 上一个非无穷远点。

a）在  $ F_{2^{m}} $  中选取随机元素 x；

b) 若 x=0，则输出  $ (0, b^{2m-1}) $  并终止；

c) 置  $ \alpha=x^{3}+ax^{2}+b $ ;

d）若  $ \alpha=0 $ ，则输出  $ (x,0) $  并终止；

e) 置  $ \beta=x^{-2}\alpha; $ 

f) 求 z，使得  $ z^{2} + z = \beta $ （参见 B.1.6）；

g) 若步骤 f) 的输出是“无解”，则返回步骤 a)；否则，步骤 f) 的输出是解 z；

h）置  $ y = x \cdot z; $ 

i) 输出 $ (x,y) $ 。

## 附录 C

## (资料性附录)

## 曲线示例

### C.1 一般要求

在此附录中所有值均以16进制表示，左边为高位，右边为低位。

### C.2  $ F_{p} $  上椭圆曲线

椭圆曲线方程为： $ y^{2}=x^{3}+ax+b $ 

示例 1:  $ F_{p}-192 $  曲线

 $$ p:BDB6F4FE3E8B1D9E0DA8C0D46F4C318CEFE4AFE3B6B8551F $$ 

系数 a:BB8E5E8F BC115E13 9FE6A814 FE48AAA6 F0ADA1AA 5DF91985

系数 b:1854BEBD C31B21B7 AEFC80AB 0ECD10D5 B1B3308E 6DBF11C1

基点  $ G=(x,y) $ ，其阶记为 n。

 $$ x:4AD5F7048DE709AD51236DE65E4D4B482C836DC6E4106640 $$ 

 $$ y:02BB3A02D4AAADACAE24817A4CA3A1B014B5270432DB27D2 $$ 

阶 n：BDB6F4FE 3E8B1D9E 0DA8C0D4 0FC96219 5DFAE76F 56564677

示例 2:  $ F_{p}-256 $  曲线

素数 p:8542D69E 4C044F18 E8B92435 BF6FF7DE 45728391 5C45517D 722EDB8B 08F1DFC3

系数 a:787968B4 FA32C3FD 2417842E 73BBFEFF 2F3C848B 6831D7E0 EC65228B 3937E498

基点  $ G=(x,y) $ ，其阶记为 n。

坐标 x:421DEBD6 1B62EAB6 746434EB C3CC315E 32220B3B ADD50BDC 4C4E6C14 7FEDD43D

 $$ y:0680512B CBB42C07 D47349D2153B70C4 E5D7FDFC BFA36EA1 A85841B9 E46E09A2 $$ 

阶 n: 8542D69E 4C044F18 E8B92435 BF6FF7DD 29772063 0485628D 5AE74EE7 C32E79B7

### C.3  $ F_{2^{m}} $  上椭圆曲线

椭圆曲线方程为： $ y^{2}+xy=x^{3}+ax^{2}+b $ 

示例 3. $ F_{2m}-193 $  曲线

基域生成多项式: $ x^{193}+x^{15}+1 $ 

系数a:0

 $$ b:002FE22037B624DBEB C4C618E13FD998B1A18E1EE0D05C46FB $$ 

 $$ G=(x,y) $$ 

 $$ ?2 $$ 

坐标 x:00 D78D47E8 5C936440 71BC1C21 2CF994E4 D21293AA D8060A84

坐标 y:00 615B9E98 A31B7B2F DDEEECB7 6B5D8755 86293725 F9D2FC0C

阶 n: 80000000 00000000 00000000 43E9885C 46BF45D8 C5EBF3A1

示例 4: $ F_{2m}-257 $  曲线

 $$ x^{257}+x^{12}+1 $$ 

系数a:0

 $$ b:00E78BCD09746C202378A7E72B12BCE00266B9627ECB0B5A25367AD1AD4CC6242B $$ 

基点  $ G=(x,y) $ ，其阶记为 n。

坐标 x:00 CDB9CA7F 1E6B0441 F658343F 4B10297C 0EF9B649 1082400A 62E7A748 5735FADD  

坐标 y:01 3DE74DA6 5951C4D7 6DC89220 D5F7777A 611B1C38 BAE260B1 75951DC8 060C2B3E  

阶 n: 7FFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF BC972CF7 E6B6F900 945B3C6A 0CF6161D

# 附录 D

# （资料性附录）  椭圆曲线方程参数的拟随机生成及验证

### D.1 椭圆曲线方程参数的拟随机生成

#### D.1.1  $ F_{p} $  上椭圆曲线方程参数的拟随机生成

方式 1:

输入: 素域的规模 p。

输出: 比特串 SEED 及  $ F_{p} $  中的元素 a, b。

a）任意选择长度至少为 192 的比特串 SEED；

b) 计算  $ H=H_{256} $  (SEED)，并记  $ H=(h_{255}, h_{254}, \cdots, h_{0}) $ ;

c) 置  $ R = \sum_{i=0}^{255} h_{i} 2^{i} $ ;

d) 置  $ r = R \mod p $ ;

e) 任意选择  $ F_{p} $  中的元素 a 和 b，使  $ r \cdot b^{2} \equiv a^{3} \pmod{p} $ ;

f) 若 $ (4a^{3}+27b^{2})\bmod p=0 $ ，则转步骤 a);

g）所选择的 $ F_{p} $ 上的椭圆曲线为 $ E:y^{2}=x^{3}+ax+b $ ；

h）输出(SEED,a,b)。

方式 2:

输入: 素域的规模 p。

输出: 比特串 SEED 及  $ F_{p} $  中的元素 a, b。

a）任意选择长度至少为 192 的比特串 SEED；

b) 计算  $ H=H_{256} $  (SEED)，并记  $ H=(h_{255},h_{254},\cdots,h_{0}) $ ;

c) 置  $ R = \sum_{i=0}^{255} h_{i} 2^{i} $ ;

d) 置  $ r = R \mod p $ ;

e）置b=r；

f) 取  $ F_{p} $  中的元素 a 为某固定值；

g）若 $ (4a^{3}+27b^{2})\bmod p=0 $ ，则转步骤a）；

h）所选择的 $ F_{p} $ 上的椭圆曲线为 $ E:y^{2}=x^{3}+ax+b $ ;

i) 输出 $ (SEED, a, b) $ 。

#### D.1.2  $ F_{2^{m}} $  上椭圆曲线方程参数的拟随机生成

输入: 域的规模  $ q=2^{m} $ ， $ F_{2^{m}} $  的约化多项式  $ f(x)=x^{m}+f_{m-1}x^{m-1}+\cdots+f_{2}x^{2}+f_{1}x+f_{0} $  （其中  $ f_{i}\in F_{2}, i=0,1,\cdots,m-1 $ ）。

输出: 比特串 SEED 及  $ F_{2^{m}} $  中的元素 a, b。

a）任意选择至少 192 比特长的比特串 SEED；

b) 计算  $ H=H_{256} $  (SEED)，并记  $ H=(h_{255}, h_{254}, \cdots, h_{0}) $ ;

c) 若  $ i \geqslant 256 $ ，令  $ h_{i} = 1 $ ，置比特串  $ HH = (h_{m-1}, h_{m-2}, \cdots, h_{0}) $ ，b 为与 HH 对应的  $ F_{2^{m}} $  中的元素；

d）若 b=0，则转步骤 a）；

e）取 a 为  $ F_{2^{m}} $  中的任意元素；

f) 所选择的  $ F_{2^{m}} $  上的椭圆曲线为  $ E: y^{2} + xy = x^{3} + ax^{2} + b $ ;

g）输出 $ (SEED,a,b) $ 。

### D.2 椭圆曲线方程参数的验证

#### D.2.1  $ F_{p} $  上椭圆曲线方程参数的验证

方式 1

输入:比特串 SEED 及  $ F_{p} $  中的元素 a, b。

输出: 输入参数“有效”或“无效”。

a）计算  $ H' = H_{256}(SEED) $ ，并记  $ H' = (h_{255}, h_{254}, \cdots, h_{0}) $ ；

b) 置  $ R' = \sum_{i=0}^{255} h_{i} 2^{i} $ ;

c) 置  $ r' = R' $  mod p;

d）若  $ r^{\prime} \cdot b^{2} \equiv a^{3} \pmod{p} $ ，则输出“有效”；否则输出“无效”。

方式 2

输入:比特串 SEED 及  $ F_{p} $  中的元素 b。

输出: 输入参数“有效”或“无效”。

a）计算  $ H' = H_{256}(SEED) $ ，并记  $ H' = (h_{255}, h_{254}, \cdots, h_{0}) $ ；

b) 置  $ R' = \sum_{i=0}^{255} h_{i} 2^{i} $ ;

c) 置  $ r' = R' \mod p $ ;

d）若  $ r' = b $ ，则输出“有效”；否则输出“无效”。

#### D.2.2  $ F_{2^{m}} $  上椭圆曲线方程参数的验证

输入:比特串 SEED 及  $ F_{2^{m}} $  中的元素 b。

输出: 输入参数“有效”或“无效”。

a）计算  $ H' = H_{256} $  (SEED)，并记  $ H' = (h_{255}, h_{254}, \cdots, h_{0}) $ ；

b）若  $ i \geqslant 256 $ ，令  $ h_{i} = 1 $ ，置比特串  $ HH' = (h_{m-1}, h_{m-2}, \cdots, h_{0}) $ ， $ b' $  为与  $ HH' $  对应的  $ F_{2^{m}} $  中的元素；

c) 若  $ b' = b $ ，则输出“有效”；否则输出“无效”。

注：本附录中的函数  $ H_{256} $  () 是输出长度为 256 比特的密码杂凑算法。

## 参考文献

[1] GB/T 15843.1—1999 信息技术 安全技术 实体鉴别 第1部分：概述

[2] GB/T 25069—2010 信息安全技术 术语

[3] Agnew G, Beth T, Mullin R, et al. 1993. Arithmetic operations in GF $ _{2}^{m} $ . Journal of Cryptology, (6): 3~13

[4] Agnew G, Mullin R, Onyszchuk I, et al. 1991. An implementation for a fast public-key cryptosystem. Journal of Cryptology, (3): 63~79

[5] ANSI X9.62—1999 Public Key Cryptography For The Financial Services Industry: The Elliptic Curve Digital Signature Algorithm(ECDSA). American National Standards Institute

[6] ANSI X9.63—2001 Public Key Cryptography for the Financial Services Industry: Key Agreement and key Transport Using Elliptic Curve Cryptography. American Nation Standard Institute

[7] Brickell E, Gordon D, Mccurley K, et al. 1993. Fast Exponentiation with precomputation. Advances in Cryptology-EUROCRYPT'92. LNCS 658. Berlin: Springer-Verlag. 200~207

[8] Blake I, Seroussi G, Smart N. 1999. Elliptic Curves in Cryptography. Cambridge: Cambridge University Press

[9] ISO/IEC 15946-1:2002 Information technology—Security techniques—Cryptographic techniques based on elliptic curves—Part 1: General

[10] ISO/IEC 15946-2:2002 Information technology—Security techniques—Cryptographic techniques based on elliptic curves—Part 2: Digital signatures

[11] ISO/IEC 15946-3:2002 Information technology—Security techniques—Cryptographic techniques based on elliptic curves—Part 3: Key establishment

[12] ISO/IEC 15946-4:2003 Information technology—Security techniques—Cryptographic techniques based on elliptic curves—Part 4: Digital signatures giving message recovery

[13] ITU-T Recommendation X.680 Information Technology—Abstract Syntax Notation One (ASN.1): Specification of Basic Notation (eqv ISO/IEC 8824-1)

[14] ITU-T Recommendation X.681 Information Technology—Abstract Syntax Notation One (ASN.1): Information Object Specification(eqv ISO/IEC 8824-2)

[15] ITU-T Recommendation X.682 Information Technology—Abstract Syntax Notation One (ASN.1):Constraint Specification(eqv ISO/IEC 8824-3)

[16] ITU-T Recommendation X.683 Information Technology—Abstract Syntax Notation One (ASN.1): Parametrization of ASN.1 Specifications (eqv ISO/IEC 8824-4)

[17] ITU-T Recommendation X.690 Information Technology—ASN.1 Encoding Rules: Specification of Basic Encoding Rules (BER), Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER) (eqv ISO/IEC 8825-1)

[18] ITU-T Recommendation X.691 Information Technology—ASN.1 Encoding Rules: Specification of Packed Encoding Rules (PER) (eqv ISO/IEC 8825-2)

[19] Knuth D. 1981. The Art of Computer Programming. v. 2. 2nd ed, Reading (MA): Addison-Wesley

[20] Koblitz N. 1987. Elliptic curve cryptosystems. Mathematics of Computation, (48) 203~209

[21] Lehmann F, Maurer M, Müller V, et al. 1994. Counting the number of points on elliptic curves over finite field of characteristic greater than three. In: Adleman L, Huang M D, ed. Algorithmic

Number Theory.LNCS 877.Berlin:Springer-Verlag.60~70

[22] Lidl R, Niederreiter H. 1987. Finite Fields. Cambridge: Cambridge University Press

[23] Mceliece R. 1987. Finite Fields for Computer Scientists and Engineers. Boston: Kluwer Academic Publishers

[24] Menezes A. 1993. Elliptic Curve Public Key Cryptosystems. Boston: Kluwer Academic Publishers

[25] Menezes A, Okamoto T, Vanstone S. 1993. Reducing elliptic curve logarithms to logarithms in a finite field. IEEE Transactions on Information Theory, 39: 1639–1646

[26] Müller V. 1995. Counting the number of points on elliptic curves over finite fields of characteristic greater than three: [Doctorate Dissertation]. Saarlandes: University of Saarlandes

[27] Pollard J. 1978. Monte Carlo methods for index computation mod p. Mathematics of Computation, 32: 918-924

[28] Satoh T, Araki K. 1998. Fermat quotients and the polynomial time discrete log algorithm for anomalous elliptic curves. Comment. Math. Univ. St. Paul., 47(1): 81~92

[29] Satoh T. 2000. The canonical lift of an ordinary elliptic curve over a finite field and its point counting. J. Ramanujan Math. Soc., 15: 247~270

[30] Satoh T. 2002. On p-adic point counting algorithms for elliptic curves over finite fields. In: Fieker C, Kohel D R, eds. Algorithmic Number Theory, LNCS 2369, Berlin: Springer-Verlag, 43~66

[31] Satoh T, Skjernaa B, Taguchi Y. 2003. Fast computation of canonical lifts of elliptic curves and its application to point counting. Finite Fields Appl., 9: 89–101

[32] Schoof R. 1985. Elliptic curves over finite fields and the computation of square roots mod p. Mathematics of Computation, 44(170):483~494

[33] Schoof R. 1995. Counting Points on Elliptic Curves over Finite Fields. Jl. de Theorie des Nombres de Bordeaux, 7:219~254

[34] Silverman J. 1986. The Arithmetic of Elliptic Curves. Berlin: Springer-Verlag, GTM 106

[35] Smart N. 1999. The discrete logarithm problem on elliptic curves of trace one. Journal of Cryptology, 12(3): 193~196

[36] ГОСТ Р 34.10—2001 ИНФОРМАЦИОННАЯ ТЕХНОЛОГИЯ—КРИПТОГРАФИЧЕСКАЯ ЗАЩИТА ИНФОРМАЦИИ—Процессы формирования и проверки электронной цифровой подписи. ГОСУДАРСТВЕННЫЙ СТАНДАРТ РОССТИЙСКОЙ ФЕДЕРАЦИИ