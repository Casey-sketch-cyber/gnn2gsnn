# 7️⃣ 第 7 章 核心：为什么发放率约等于 ReLU

> Notion 页面：https://www.notion.so/41c0e3342e6f819b94c7f590cf469e44 （导出自 Notion 实时内容，最后编辑时间 `2026-11-18T14:59:13.131Z`）

<callout icon="📌" color="blue_bg">
<b>这一章要回答的问题</b>：为什么把普通神经网络的权重原封不动搬进脉冲神经元后，脉冲发放率会自动约等于 $\mathrm{ReLU}$ 激活值，转换误差到底从哪三个地方冒出来，以及时间步从 $T=4$ 增加到 $32$ 时两层脉冲网络是怎样一步步逼近原网络的？
</callout>

## 前置知识

<mention url="https://app.notion.com/p/41c0e3342e6f8102aeb4d13255acb166">第 1 章 线性代数最小集</mention>、<mention url="https://app.notion.com/p/41c0e3342e6f8156afa8d6260fe476ce">第 2 章 神经网络的前向计算</mention>、<mention url="https://app.notion.com/p/41c0e3342e6f817094a3d6783a3721a1">第 6 章 脉冲神经元</mention>。

## 直觉

<b>打个比方</b>：想象你开了一家糖果店，原本按克称重卖散装糖（普通网络里的小数激活值，比如 <code>0.45</code> 千克；顾客欠账小于 <code>0</code> 就记作不发货 <code>0</code>，这就是 $\mathrm{ReLU}$）。现在店里换了规矩，取消电子秤，只准在 $T=4$ 分钟里每分钟最多递出 $1$ 小包（每包 $\frac{1}{4}=0.25$ 千克，对应发脉冲 <code>1</code> 或不发 <code>0</code>）。只要你在后台拿个本子诚实记账（减法复位膜电位），把顾客要的重量分摊到 $4$ 分钟里攒满一包就递出去，最后顾客手里收到的总包数乘以包重，自然就等于他原本要买的散装重量——但有三个地方会差一点点：（1）最多每分钟发 1 包，4 分钟封顶只能发 1 千克，要买 1.5 千克的那部分发不出去（<b>截断误差</b>）；（2）只能整包发，0.45 千克只能发 1 包即 0.25 千克，零头 0.20 千克卡在后台本子上没凑够第 2 包（<b>量化误差</b>；如果在开张前先往本子上预垫半包底数，就能把“抹零头”变成公平的“四舍五入”！）；（3）如果上游进货不是均匀送来，而是前两分钟猛送、后两分钟退货，就可能先把包发出去了后面收不回来（<b>到达不均匀误差</b>）。

<b>准确地说</b>：把第 6 章减法复位 IF 神经元的差分方程 $v[t]-v[t-1] = z[t] - \theta s[t]$ 从 $t=1$ 到 $T$ 做裂项求和，中间所有膜电位两两抵消，直接推出时间平均脉冲输出 $\varphi(T) = \theta r = \bar{z} - \frac{v[T]-v[0]}{T}$；再结合第 1 章矩阵乘法的线性性质 $\frac{1}{T}\sum_t W\mathbf{s}[t] = W\mathbf{r}$，就严格证明了“原样复制权重 $W$ 的脉冲层在时间平均意义下逼近截断并量化的 $\mathrm{ReLU}$”。<b>比方不成立的地方</b>：糖果店的货物不会变成负数，而深层脉冲神经元接收的是上游正权重与负权重混合打进来的脉冲流 $z[t]$，当负脉冲先到或后到时，末态膜电位 $v[T]$ 可能跌破 $0$ 或冲过 $\theta$，产生静态单层公式看不见的动态时序误差。

---

## 符号

| 符号 | 形状 / 取值域 | 含义 |
| --- | --- | --- |
| $\mathbf{a}^{(l)}$ | $\mathbb{R}_{\ge 0}^{d_l}$ | 原普通网络（ANN）第 $l$ 层的 $\mathrm{ReLU}$ 激活输出向量，$\mathbf{a}^{(l)} = \mathrm{ReLU}(W^{(l)}\mathbf{a}^{(l-1)}+\mathbf{b}^{(l)})$ |
| $z[t],\; \bar{z}$ | $\mathbb{R},\; \mathbb{R}$ | 单神经元第 $t$ 步输入电流与 $T$ 步平均输入电流 $\bar{z} = \frac{1}{T}\sum_{t=1}^T z[t]$ |
| $\theta$（或逐层 $\theta^{(l)}$） | $\mathbb{R}_+$ | 第 $l$ 层 IF 脉冲神经元的发放阈值 |
| $r$（向量 $\mathbf{r}^{(l)}$） | $[0, 1]$（或 $[0, 1]^{d_l}$） | $T$ 步平均发放率，$r = \frac{1}{T}\sum_{t=1}^T s[t]$ |
| $\varphi(T)$（向量 $\boldsymbol{\varphi}^{(l)}(T)$） | $[0, \theta^{(l)}]$（或 $[0, \theta^{(l)}]^{d_l}$） | 平均突触后电位（将二值脉冲乘回本层阈值还原物理量纲），$\boldsymbol{\varphi}^{(l)}(T) = \theta^{(l)} \mathbf{r}^{(l)} = \frac{1}{T}\sum_{t=1}^T \theta^{(l)}\mathbf{s}^{(l)}[t]$ |
| $\lfloor u \rfloor,\; \mathrm{clip}(u, a, b)$ | $\mathbb{Z},\; [a, b]$ | 向下取整函数（不超过 $u$ 的最大整数）与上下界截断函数 $\min(\max(u, a), b)$ |
| $\lambda^{(l)}$ | $\mathbb{R}_+$ | 第 $l$ 层激活归一化尺度（数据最大激活、高分位数，或 QCFS 可训练阈值） |
| $\tilde{W}^{(l)},\; \tilde{\mathbf{b}}^{(l)}$ | 与 $W^{(l)}, \mathbf{b}^{(l)}$ 同形状 | 统一单位阈值 $\theta=1$ 写法下的缩放后等效权重与等效偏置 |
| $L_{\mathrm{quant}},\; \phi$ | 正整数，$\mathbb{R}$ | QCFS 源网络激活函数的训练量化阶数（原文记为 $L$）与平移偏置项（最优取 $\phi = \frac{1}{2}$） |

---

## 推导（本课程最核心推导，一步不跳）

### 1. 裂项求和（Telescoping Sum）：从逐步充放电推出全局电荷守恒方程

回顾第 6 章减法复位 IF 神经元在每个时间步 $t \in \{1, 2, \dots, T\}$ 的充电方程与复位方程：

$$
v^-[t] = v[t-1] + z[t], \qquad v[t] = v^-[t] - \theta\,s[t]
$$

<b>第 1 步（消去中间变量 </b><b>$v^-[t]$</b><b>）</b>：将第一式 $v^-[t] = v[t-1] + z[t]$ 直接代入第二式：

$$
v[t] = v[t-1] + z[t] - \theta\,s[t]
$$

<b>第 2 步（移项写成相邻两步膜电位之差，依据：等式两边同减 </b><b>$v[t-1]$</b><b>）</b>：

$$
v[t] - v[t-1] = z[t] - \theta\,s[t]
$$

<b>第 3 步（对 </b><b>$t = 1, 2, \dots, T$</b><b> 逐式相加，展开左端裂项相消！）</b>：<br />把 $t=1$ 到 $t=T$ 的全部 $T$ 个等式竖着排出来相加：

- $t=1$: $v[1] - v[0] = z[1] - \theta s[1]$
- $t=2$: $v[2] - v[1] = z[2] - \theta s[2]$
- $\dots$
- $t=T$: $v[T] - v[T-1] = z[T] - \theta s[T]$

看等号左边相加（依据：加法交换律与结合律）：$+v[1]$ 与 $-v[1]$ 抵消，$+v[2]$ 与 $-v[2]$ 抵消，……，$+v[T-1]$ 与 $-v[T-1]$ 抵消，整串和式只剩下首尾两项 $v[T] - v[0]$！右端则是输入电流之和减去 $\theta$ 乘以脉冲总数（依据：常数 $\theta$ 对求和的乘法分配律）：

$$
\sum_{t=1}^{T} \big(v[t] - v[t-1]\big) = v[T] - v[0] = \sum_{t=1}^{T} z[t] - \theta \sum_{t=1}^{T} s[t]
$$

把 $-v[0]$ 移到右边，这就是脉冲神经网络的<b>电荷守恒总账本</b>：

$$
v[T] = v[0] + \sum_{t=1}^{T} z[t] - \theta \sum_{t=1}^{T} s[t]
$$

（物理意义直白得像小学算术：<b>期末余电 = 期初底电 + 总充入电量 - 总发走脉冲带走的电量</b>！）

<b>第 4 步（解出平均发放率 </b><b>$r$</b><b> 与平均脉冲输出 </b><b>$\varphi(T) = \theta r$</b><b>）</b>：

1. 把 $\theta \sum_{t=1}^T s[t]$ 移到左边、$v[T]$ 移到右边：

$$
\theta \sum_{t=1}^{T} s[t] = \sum_{t=1}^{T} z[t] - \big(v[T] - v[0]\big)
$$

2. 等式两边同时除以总时间步 $T > 0$，并记平均输入电流 $\bar{z} = \frac{1}{T}\sum_{t=1}^T z[t]$、平均发放率 $r = \frac{1}{T}\sum_{t=1}^T s[t]$：

$$
\theta\,r = \bar{z} - \frac{v[T] - v[0]}{T}
$$

3. 等式两边再同时除以阈值 $\theta > 0$，即得全课程最核心的<b>发放率精确恒等式</b>（完全对应 <mention url="https://app.notion.com/p/41b0e3342e6f81a3b2f0dca38f8f241d">SNN Toolbox（2017）</mention> \[[原文](https://arxiv.org/abs/1612.04052)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8178a7dcc29d4be95557)\] \[[代码](https://github.com/NeuromorphicProcessorProject/snn_toolbox)\] Section 2 Eq. 6 第 3 页，及 <mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention> \[[原文](https://arxiv.org/abs/2303.04347)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)\] \[[代码](https://github.com/putshua/SNN_conversion_QCFS)\] Section 2 Eq. 7–8 第 3 页）：

$$
r = \frac{1}{T}\sum_{t=1}^{T} s[t] = \frac{1}{\theta}\left(\bar{z} - \frac{v[T] - v[0]}{T}\right)
$$

注意：到这一步为止，我们<b>没有做任何近似</b>，也没有假设 $z[t]$ 恒定——上式对任意随时间跳变的输入序列 $z[1..T]$ 都 $100\%$ 严格成立！

---

### 2. 从精确恒等式一步步推出“截断并量化的 ReLU”

现在看恒定输入情形 $z[t] \equiv z$（于是 $\bar{z} = z$），并设初始膜电位落在正常范围 $0 \le v[0] < \theta$（如 $v[0]=0$ 或 $v[0]=\theta/2$）。我们来严格推出发放率 $r$（以及还原物理尺度后的 $\varphi(T) = \theta r$）的三条核心性质（补全 <mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention> \[[原文](https://arxiv.org/abs/2106.06984)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)\] Eq. 8–10 与 <mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention> \[[原文](https://arxiv.org/abs/2303.04347)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)\] \[[代码](https://github.com/putshua/SNN_conversion_QCFS)\] Eq. 11 省略的归纳法细节，标为推导）：

<callout icon="💡" color="gray_bg">
<b>推导（补全论文省略的数学步骤）：恒定输入下的三条性质与精确阶梯闭式解</b><br /><br /><br /><b>性质一（负数归零，对应 ReLU 左半轴）</b>：若输入电流 $z \le 0$，因为初值 $v[0] < \theta$，由数学归纳法：第 1 步 $v^-[1] = v[0] + z \le v[0] < \theta \implies s[1]=0,\; v[1]=v^-[1] \le v[0] < \theta$；依此类推对所有 $t=1,\dots,T$ 都有 $v^-[t] < \theta \implies s[t] = 0$。故 $z \le 0$ 时<b>一个脉冲都不发</b>，$r = 0$，与 $\mathrm{ReLU}(z) = \max(0, z) = 0$ 完全一致！<br /><br /><br /><b>性质二（上界截断，对应上限 </b><b>$\theta$</b><b>）</b>：由于每一步 $s[t] \in \{0, 1\}$ 最多只能发 $1$ 个脉冲，$T$ 步总脉冲数 $N_{\mathrm{sp}}(T) = \sum_{t=1}^T s[t] \le T$，故发放率恒满足 $r \le 1$（物理尺度输出 $\varphi(T) = \theta r \le \theta$）。当输入过大使得每一步都触发脉冲时，输出被硬截断在上限 $\theta$。<br /><br /><br /><b>性质三（离散量化为 </b><b>$1/T$</b><b> 的整数倍，并严格求出脉冲整数 </b><b>$N_{\mathrm{sp}}(T)$</b><b>）</b>：因为 $N_{\mathrm{sp}}(T) \in \{0, 1, \dots, T\}$ 是整数，发放率 $r = N_{\mathrm{sp}}(T)/T$ 只能取 $\{0, \frac{1}{T}, \frac{2}{T}, \dots, 1\}$ 这 $T+1$ 个离散台阶！当输入落在未饱和区间 $0 \le z \le \theta$（且若 $z=\theta$、$v[0]=0$）或一般地只要没有发生过饱和堆积使得末态膜电位满足 $0 \le v[T] < \theta$ 时（对任意 $0 \le z < \theta$ 且 $0 \le v[0] < \theta$，归纳检验：若 $0 \le v[t-1] < \theta$，则 $0 \le v^-[t] = v[t-1]+z < 2\theta$；若 $v^-[t] < \theta$ 则 $s[t]=0, v[t]=v^-[t] \in [0,\theta)$；若 $\theta \le v^-[t] < 2\theta$ 则 $s[t]=1, v[t]=v^-[t]-\theta \in [0,\theta)$，故<b>末态余电必被严格夹在 </b><b>$0 \le v[T] < \theta$</b><b> 之间</b>！），将 $0 \le v[T] < \theta$ 代入电荷守恒式 $\theta N_{\mathrm{sp}}(T) = T z + v[0] - v[T]$：

$$
T z + v[0] - \theta < \theta N_{\mathrm{sp}}(T) \le T z + v[0] \quad \overset{\div \theta}{\Longrightarrow} \quad \frac{z T + v[0]}{\theta} - 1 < N_{\mathrm{sp}}(T) \le \frac{z T + v[0]}{\theta}
$$

在长度为 $1$ 的左开右闭区间 $(u-1, u]$ 里有且仅有一个整数，这个整数按定义就是<b>向下取整函数 </b><b>$\lfloor u \rfloor$</b>！再把负数自动归零与上界不超过 $T$ 合并进来，就得到恒定输入下脉冲层输出的精确闭式公式：

$$
r(z) = \mathrm{clip}\!\left(\frac{1}{T}\left\lfloor \frac{z T + v[0]}{\theta} \right\rfloor,\; 0,\; 1\right), \qquad \varphi(T) = \theta\,r(z) = \theta\,\mathrm{clip}\!\left(\frac{1}{T}\left\lfloor \frac{z T + v[0]}{\theta} \right\rfloor,\; 0,\; 1\right)
$$
</callout>

一句话读懂这个公式：当 $T \to \infty$ 且 $\theta$ 覆盖正激活范围时，$\frac{v[T]-v[0]}{T} \to 0$，阶梯台阶宽度 $\frac{\theta}{T} \to 0$，脉冲输出 $\varphi(T)$ 就光滑地收敛到普通网络的 $\mathrm{ReLU}(z) = \max(0, z)$；而在有限步 $T$ 下，<b>IF 脉冲神经元的平均输出完完全全就是一个“在 </b><b>$\theta$</b><b> 处封顶截断、按步长 </b><b>$\theta/T$</b><b> 离散量化的 ReLU”</b>！

---

### 3. 初始电压 $v[0] = \theta/2$ 的四舍五入魔力与 QCFS 激活函数及定理对照

仔细对比 $v[0] = 0$ 和 $v[0] = \frac{\theta}{2}$ 代入上式时的几何图像（对应本章 Notebook 第 1 节阶梯对比图）：

1. <b>传统设法 </b><b>$v[0] = 0$</b><b>（向下取整 Flooring）</b>：
   - 公式为 $\varphi(T) = \frac{\theta}{T} \lfloor \frac{zT}{\theta} \rfloor$（在 $z \in [0, \theta)$ 上）。
   - 整个区间 $[0, \frac{\theta}{T})$ 里的所有正输入统统被抹成 $0$，$[\frac{\theta}{T}, \frac{2\theta}{T})$ 统统被抹成 $\frac{\theta}{T}$——<b>永远单向往小了偏</b>！误差 $\varphi(T) - z \in (-\frac{\theta}{T},\; 0]$，最大绝对误差为 <b>$\frac{\theta}{T}$</b>，平均系统性偏低 <b>$-\frac{\theta}{2T}$</b>。层数一深，每层都往小抹一截，到了第 10 层脉冲就快死光了！
2. <b>半阈值初始化 </b><b>$v[0] = \frac{\theta}{2}$</b><b>（四舍五入 Rounding）</b>：
   - 把 $v[0] = \frac{\theta}{2}$ 代入取整号内部：

$$
\left\lfloor \frac{z T + \theta/2}{\theta} \right\rfloor = \left\lfloor \frac{z T}{\theta} + \frac{1}{2} \right\rfloor = \mathrm{round}\!\left(\frac{z T}{\theta}\right)
$$

- 任何实数加上 $0.5$ 再向下取整，正是标准的<b>四舍五入</b>！现在台阶跳变点挪到了区间正中间 $\frac{\theta}{2T}, \frac{3\theta}{2T}, \dots$：前半段略微低估、后半段略微高估，单层误差对称落在 $\left[-\frac{\theta}{2T},\; +\frac{\theta}{2T}\right]$ 之间——<b>最大量化误差直接砍半为 </b><b>$\frac{\theta}{2T}$</b><b>，且正负误差在区间上的平均值恰好抵消为 </b><b>$0$</b>！

这一洞察正是 <mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention> \[[原文](https://arxiv.org/abs/2303.04347)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)\] \[[代码](https://github.com/putshua/SNN_conversion_QCFS)\]（Bu 等，ICLR 2022）能够把转换时间步压到 $T=4$ 的核心数学支柱。我们逐字符核对原文第 4 节的两个激活函数与两条定理：

<callout icon="✅" color="green_bg">
<b>原文公式与定理核对（</b><b><mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention></b><b> \[</b>[<b>原文</b>](https://arxiv.org/abs/2303.04347)<b>\] \[</b>[<b>中文</b>](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)<b>\] \[</b>[<b>代码</b>](https://github.com/putshua/SNN_conversion_QCFS)<b>\] Section 4.1–4.2 Eq. 13–16，第 5–6 页，将层指标统一标为 </b><b>$(l)$</b><b>，量化阶数记为 </b><b>$L$</b><b>，平移项记为 </b><b>$\phi$</b><b>）</b>：<br />

1. <b>无平移量化截断激活（Section 4.1 Eq. 13 & Theorem 1，第 5 页）</b>：若在训练源 ANN 时不用普通 $\mathrm{ReLU}$，而是直接用 $L$ 阶量化截断函数训练：

$$
\mathbf{a}^{(l)} = \bar{h}(\mathbf{z}^{(l)}) = \lambda^{(l)}\,\mathrm{clip}\!\left(\frac{1}{L}\left\lfloor \frac{\mathbf{z}^{(l)} L}{\lambda^{(l)}} \right\rfloor,\; 0,\; 1\right)
$$

<b>Theorem 1</b>：将该 ANN 以相同权重转换为 SNN。若测试时间步满足 $T = L$、阈值 $\theta^{(l)} = \lambda^{(l)}$ 且初始膜电位 $\mathbf{v}^{(l)}[0] = \mathbf{0}$，则估计转换误差恒为零：$\widetilde{\mathbf{Err}}^{(l)} = \boldsymbol{\varphi}^{(l)}(T) - \mathbf{a}^{(l)} = \mathbf{0}$。<br /><br /><i>局限</i>：一旦部署时想换别的时间步 $T \neq L$（例如用 $L=4$ 训出的模型跑 $T=8$），两个不同步长的向下取整阶梯错位，期望误差立刻变为非零（原文图 2b、图 4 绿线精度不升反降）。<br /><br /><br />2. <b>带平移项的 QCFS 激活（Section 4.2 Eq. 15 & Theorem 2，第 5–6 页）</b>：在源 ANN 激活函数里加入平移超参数 $\phi$：

$$
\mathbf{a}^{(l)} = \hat{h}(\mathbf{z}^{(l)}) = \lambda^{(l)}\,\mathrm{clip}\!\left(\frac{1}{L}\left\lfloor \frac{\mathbf{z}^{(l)} L}{\lambda^{(l)}} + \phi \right\rfloor,\; 0,\; 1\right)
$$

<b>Theorem 2</b>：将该 ANN 以相同权重转换为 SNN，取 $\theta^{(l)} = \lambda^{(l)}$、初始电位 $\mathbf{v}^{(l)}[0] = \theta^{(l)}\phi$。假设前激活 $z_i^{(l)}$ 在各量化小区间 $[(t-1)\lambda^{(l)}/T,\; t\lambda^{(l)}/T]$ 与 $[(k-1)\lambda^{(l)}/L,\; k\lambda^{(l)}/L]$ 内服从均匀分布，则当源网络平移项取 $\phi = \frac{1}{2}$（即 $\mathbf{v}^{(l)}[0] = \frac{1}{2}\theta^{(l)}$）时，<b>对任意测试时间步 </b><b>$T$</b><b> 和训练阶数 </b><b>$L$</b><b>（哪怕 </b><b>$T \neq L$</b><b>），转换误差的数学期望恒等于 </b><b>$0$</b>：

$$
\forall T, L,\qquad \mathbb{E}_{\mathbf{z}}\!\left[\widetilde{\mathbf{Err}}^{(l)}\right]\Big|_{\phi = \frac{1}{2}} = \mathbf{0}
$$

（<b>重要边界提醒</b>：QCFS 需要用直通估计器 STE 即原文式 17 重新训练源 ANN，因此严格说属于“训练感知转换”而非对现成预训练权重的零改动免训练转换；但它的“半阈值初始电位 $\mathbf{v}[0] = \frac{1}{2}\theta$”技巧完全不需要重训源网络，直接就能白送给任何现成 ReLU / 视觉图模型的免训练转换！）
</callout>

---

### 4. 为什么直接复制权重 $W^{(l)}$ 和偏置 $\mathbf{b}^{(l)}$ 就能工作？（验收标准第 4 条：线性穿透与非线性反例）

前面第 1～3 节只看了一个孤立神经元。把多层网络串起来时，第 $l$ 层脉冲神经元在每一拍 $t$ 收到的并不是恒定实数 $\mathbf{a}^{(l-1)}$，而是第 $l-1$ 层发来的<b>一串一串跳变的 0/1 脉冲</b> $\mathbf{s}^{(l-1)}[t] \in \{0, 1\}^{d_{l-1}}$！凭什么原网络在连续小数上训出来的权重矩阵 $W^{(l)}$ 和偏置 $\mathbf{b}^{(l)}$，一字不改直接搬过来乘 0/1 脉冲就能算对？

答案完完全全靠我们在<mention url="https://app.notion.com/p/41c0e3342e6f8102aeb4d13255acb166">第 1 章 线性代数最小集</mention>埋下的伏笔——<b>矩阵乘法的线性性质</b>！

在第 $l$ 层的第 $t$ 拍，把上游脉冲乘回其阈值量纲 $\mathbf{x}_{\mathrm{psp}}^{(l-1)}[t] = \theta^{(l-1)}\mathbf{s}^{(l-1)}[t]$，并在<b>每一个时间步 </b><b>$t$</b> 都加上偏置 $\mathbf{b}^{(l)}$：

$$
\mathbf{z}^{(l)}[t] = W^{(l)} \big(\theta^{(l-1)} \mathbf{s}^{(l-1)}[t]\big) + \mathbf{b}^{(l)}
$$

现在把它代入第 1 节裂项求和公式需要的“$T$ 步平均输入电流 $\bar{\mathbf{z}}^{(l)}$”，一步不跳写出展开过程：

1. <b>按时间平均定义写出和式</b>：

$$
\bar{\mathbf{z}}^{(l)} = \frac{1}{T}\sum_{t=1}^{T} \mathbf{z}^{(l)}[t] = \frac{1}{T}\sum_{t=1}^{T} \left( W^{(l)} \big(\theta^{(l-1)} \mathbf{s}^{(l-1)}[t]\big) + \mathbf{b}^{(l)} \right)
$$

2. <b>拆开加法求和（依据：有限和加法交换结合律，以及 </b><b>$T$</b><b> 个相同常向量 </b><b>$\mathbf{b}^{(l)}$</b><b> 求平均仍等于 </b><b>$\mathbf{b}^{(l)}$</b><b>）</b>：

$$
\bar{\mathbf{z}}^{(l)} = \frac{1}{T}\sum_{t=1}^{T} W^{(l)} \big(\theta^{(l-1)} \mathbf{s}^{(l-1)}[t]\big) + \frac{1}{T}\underbrace{\sum_{t=1}^{T} \mathbf{b}^{(l)}}_{T\,\mathbf{b}^{(l)}} = \frac{1}{T}\sum_{t=1}^{T} W^{(l)} \big(\theta^{(l-1)} \mathbf{s}^{(l-1)}[t]\big) + \mathbf{b}^{(l)}
$$

3. <b>把固定矩阵 </b><b>$W^{(l)}$</b><b> 抽到时间求和号外面（核心依据：第 1 章矩阵乘法对向量加法的分配律 </b><b>$W\sum_t \mathbf{u}[t] = \sum_t W\mathbf{u}[t]$</b><b>！）</b>：

$$
\bar{\mathbf{z}}^{(l)} = W^{(l)} \underbrace{\left( \frac{1}{T}\sum_{t=1}^{T} \theta^{(l-1)} \mathbf{s}^{(l-1)}[t] \right)}_{\boldsymbol{\varphi}^{(l-1)}(T)} + \mathbf{b}^{(l)} = W^{(l)} \boldsymbol{\varphi}^{(l-1)}(T) + \mathbf{b}^{(l)}
$$

<b>看懂这一步就看穿了整个转换领域的灵魂</b>：

- 在每一个单拍 $t$ 里，因为 $\mathbf{s}^{(l-1)}[t]$ 的元素只有 $0$ 或 $1$，硬件根本不用做浮点乘法，只需要把 $\mathbf{s}_j^{(l-1)}[t]=1$ 对应的权重列挑出来做<b>纯加法</b>；
- 可是把 $T$ 拍的输入电流合起来看平均效果，线性性保证它<b>一分不差地等于拿原权重 </b><b>$W^{(l)}$</b><b> 去乘上一层的平均脉冲输出 </b><b>$\boldsymbol{\varphi}^{(l-1)}(T)$</b>！只要上一层满足 $\boldsymbol{\varphi}^{(l-1)}(T) \approx \mathbf{a}^{(l-1)}$，本层的平均输入 $\bar{\mathbf{z}}^{(l)}$ 就自动约等于原网络的前激活 $W^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$！全连接层、二维卷积层、第 4 章固定图的 GCN 聚合 $\hat{A}H W$、第 2 章折叠完 BN 后的等效线性层，全都因为是线性/仿射映射而天然享受这条免训练通行证！

<b>反面铁证：为什么取最大值（</b><b><code>max</code></b><b>）和乘法（</b><b><code>×</code></b><b>）绝对不能这样逐步照搬？（验收标准第 4 条后半部分）</b>

一旦算子不是线性的，求和号 $\frac{1}{T}\sum_{t=1}^T$ 就<b>抽不出函数外面</b>（$\frac{1}{T}\sum_{t=1}^T f(\mathbf{s}[t]) \neq f(\frac{1}{T}\sum_{t=1}^T \mathbf{s}[t])$）。用两个最简单的 4 步脉冲例子（$\theta=1, T=4$）当场戳破：

- <b>反例一（逐时间步取最大值 </b><b><code>max</code></b><b> 系统性高估）</b>：<br />设两个神经元的 4 步脉冲序列分别为 $s_1[1..4] = [1, 0, 1, 0]$（发 2 次，真实平均率 $r_1 = 0.50$）和 $s_2[1..4] = [0, 1, 0, 1]$（发 2 次，真实平均率 $r_2 = 0.50$）。
  - 原网络期望的真实最大值是：$\max(r_1, r_2) = \max(0.50, 0.50) = \mathbf{0.50}$。
  - 如果你在每个时间步直接对脉冲取最大 $\max(s_1[t], s_2[t])$：第 1 步 $\max(1,0)=1$，第 2 步 $\max(0,1)=1$，第 3 步 $\max(1,0)=1$，第 4 步 $\max(0,1)=1$，得到 <code>[1, 1, 1, 1]</code>，时间平均变成 <b>$\mathbf{1.00} \neq 0.50$</b><b>（足足高估了一倍！）</b>
- <b>反例二（逐时间步做乘法 </b><b><code>×</code></b><b> 系统性漏算/错位，关系到自注意力 </b><b>$QK^\top$</b><b> 与门控）</b>：<br />仍取上面同一对交替脉冲序列 $s_1 = [1, 0, 1, 0]$（平均 $0.50$）和 $s_2 = [0, 1, 0, 1]$（平均 $0.50$）。
  - 原网络期望的真实乘积是：$r_1 \times r_2 = 0.50 \times 0.50 = \mathbf{0.25}$。
  - 如果你在每个时间步直接把两个脉冲相乘 $s_1[t] \cdot s_2[t]$：因为两路脉冲刚好错峰到达，每一步里总有一个是 $0$（$1\times 0 = 0,\; 0\times 1 = 0$），四步乘积序列变成 <code>[0, 0, 0, 0]</code>，时间平均变成 <b>$\mathbf{0.00} \neq 0.25$</b><b>（信号彻底湮灭归零！）</b> 反过来若两路同步为 <code>[1, 0, 1, 0]</code> 和 <code>[1, 0, 1, 0]</code>，逐步相乘得 <code>[1, 0, 1, 0]</code> 平均为 $\mathbf{0.50} \neq 0.25$（又翻倍高估！）。第 9 章我们将专门展开所有非线性算子的突围方案。

---

### 5. 转换误差的三种来源：定义、成因与逐一具体数值例子（验收标准第 3 条）

即使网络里只有纯线性层加 $\mathrm{ReLU}$，有限时间步 $T$ 下的脉冲输出 $\boldsymbol{\varphi}^{(l)}(T)$ 与原网络激活 $\mathbf{a}^{(l)} = \mathrm{ReLU}(\mathbf{z}^{(l)})$ 之间仍存在误差 $\mathbf{Err}^{(l)} = \boldsymbol{\varphi}^{(l)}(T) - \mathbf{a}^{(l)}$。按照 <mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention> \[[原文](https://arxiv.org/abs/2303.04347)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)\] \[[代码](https://github.com/putshua/SNN_conversion_QCFS)\] Section 3（第 3–4 页）与 <mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention> \[[原文](https://arxiv.org/abs/2106.06984)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)\] Section 4.1（第 3–4 页）的经典拆解，转换误差<b>有且仅有以下三种来源</b>，我们为每一种给出一个可手算核对的具体数值例子：

#### （1）截断误差（Clipping Error）

- <b>成因</b>：脉冲神经元每拍最多发 1 个脉冲（$r \le 1$），因此平均脉冲输出最高封顶在阈值 $\theta$；原网络中任何超过 $\theta$ 的激活值 $z > \theta$ 都会被强行削平到 $\theta$。
- <b>具体数值例子（例 7.1A）</b>：设 $\theta = 1.0,\; T = 4,\; v[0] = 0$，恒定输入电流 $z = 1.5 > \theta$。
  - <b>普通网络输出</b>：$\mathrm{ReLU}(1.5) = \mathbf{1.50}$。
  - <b>脉冲网络逐步过程</b>：
    - $t=1$: $v^-=1.5 \ge 1 \implies s[1]=1,\; v[1]=0.5$
    - $t=2$: $v^-=2.0 \ge 1 \implies s[2]=1,\; v[2]=1.0$
    - $t=3$: $v^-=2.5 \ge 1 \implies s[3]=1,\; v[3]=1.5$
    - $t=4$: $v^-=3.0 \ge 1 \implies s[4]=1,\; v[4]=2.0$
  - <b>结果</b>：4 步连发 4 个脉冲（已经满负荷），SNN 输出 $\varphi(4) = 1.0 \times \frac{4}{4} = \mathbf{1.00}$，比真实值 $1.50$ 少了 <b>$-0.50$</b>（注意末态膜电位 $v[4] = 2.0 \ge \theta$ 积压在肚子里面排不出去，套回第 1 节恒等式：$1.50 - \frac{2.0 - 0}{4} = 1.00$，严丝合缝！）。

#### （2）量化误差 / 取整误差（Quantization / Flooring Error）

- <b>成因</b>：$T$ 步内脉冲个数只能取整数 $0, 1, \dots, T$，分辨率只有 $\frac{\theta}{T}$；夹在两个相邻台阶之间的连续激活值必然留下一小截凑不够整下脉冲的残余膜电位 $v[T] \in [0, \theta)$。
- <b>具体数值例子（例 7.1B）</b>：设 $\theta = 1.0,\; T = 4$，恒定输入电流 $z = 0.45 \in (0, \theta)$。
  - <b>普通网络输出</b>：$\mathrm{ReLU}(0.45) = \mathbf{0.45}$。
  - <b>若初值 </b><b>$v[0] = 0$</b>：4 步累计充入 $4\times 0.45 = 1.80$（$t=1\to 0.45,\; t=2\to 0.90,\; t=3\to 1.35$ 发 1 次剩 $0.35$, $t=4\to 0.80 < 1$ 不发），共发 <b>1 次</b>脉冲，SNN 输出 $\varphi(4) = \frac{1}{4} = \mathbf{0.25}$，产生 <b>$-0.20$</b> 的向下取整误差（恰好等于 $-v[4]/T = -0.80/4$）。
  - <b>若改用半阈值初值 </b><b>$v[0] = 0.5$</b>：总可用电位变为 $0.5 + 1.80 = 2.30$（在 $t=2$ 和 $t=4$ 各发 1 次，末态 $v[4]=0.30$），共发 <b>2 次</b>脉冲，SNN 输出 $\varphi(4) = \frac{2}{4} = \mathbf{0.50}$，误差缩小到 <b>$+0.05$</b>（缩小了整整 4 倍！）。

#### （3）到达不均匀误差（Unevenness Error）

- <b>成因</b>：从第 2 层起，输入电流 $z^{(l)}[t]$ 不再是常数，而是由上一层脉冲乘以正负权重实时合成的波动序列。即使上一层的<b>平均输出 </b><b>$\boldsymbol{\varphi}^{(l-1)}(T)$</b><b> 已经 100% 等于原网络激活 </b><b>$\mathbf{a}^{(l-1)}$</b>，只要正脉冲和负脉冲到达的<b>时间先后顺序不均匀</b>，就可能导致末态膜电位 $v^{(l)}[T]$ 跌破 $0$（前期多发了冤枉脉冲收不回来）或卡在 $\ge \theta$（后期才扎堆来不及发完），使第 2 节闭式公式的前提 $0 \le v[T] < \theta$ 失效！
- <b>具体数值例子（例 7.1C，完整复现 </b><b><mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention></b><b> \[</b>[<b>原文</b>](https://arxiv.org/abs/2303.04347)<b>\] \[</b>[<b>中文</b>](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)<b>\] \[</b>[<b>代码</b>](https://github.com/putshua/SNN_conversion_QCFS)<b>\] Section 3 第 4 页与图 1b–d 原例）</b>：<br />设时间步 $T = 5$，前后两层阈值均为 $\theta^{(l-1)} = \theta^{(l)} = 1.0$，初值 $v^{(l)}[0] = 0$。第 $l-1$ 层有两个神经元连向第 $l$ 层的一个神经元，连接权重为 $W^{(l)} = [2,\; -2]$。设前一层两个神经元在 5 步内始终固定分别发出 <b>3 个脉冲</b>和 <b>2 个脉冲</b>，因此前一层平均输出恒等于原网络激活：$\boldsymbol{\varphi}^{(l-1)}(5) = \mathbf{a}^{(l-1)} = [0.6,\; 0.4]^\top$。
  - <b>普通网络精确输出</b>：$a^{(l)} = \mathrm{ReLU}\!\big([2, -2]\begin{bmatrix} 0.6 \\ 0.4 \end{bmatrix}\big) = \mathrm{ReLU}(1.2 - 0.8) = \mathbf{0.40}$。
  - 现在保持平均发放率 $[0.6, 0.4]$ 和权重 $[2, -2]$ 丝毫不变，只改变两路脉冲到达的时刻：
    1. <b>情形 A（均匀交错到达，零误差）</b>：1 号在 $t=1,3,5$ 发（<code>[1,0,1,0,1]</code>），2 号在 $t=2,4$ 发（<code>[0,1,0,1,0]</code>）$\implies$ 输入电流序列 $z[1..5] = [+2, -2, +2, -2, +2]$。
       - 逐步追踪：$t=1: v^-=2\to \mathbf{s=1}, v=1$；$t=2: v^-=-1\to s=0, v=-1$；$t=3: v^-=1\to \mathbf{s=1}, v=0$；$t=4: v^-=-2\to s=0, v=-2$；$t=5: v^-=0\to s=0, v=0$。
       - 共发 <b>2 个脉冲</b>，末态 $v[5] = 0$，SNN 输出 $\varphi^{(l)}(5) = \frac{2}{5} = \mathbf{0.40}$（误差 $0.00$）。
    2. <b>情形 B（正脉冲先扎堆、负脉冲后到 </b><b>$\implies$</b><b> 误多发翻倍！）</b>：1 号在 $t=1,2,3$ 连发（<code>[1,1,1,0,0]</code>），2 号在 $t=4,5$ 才发（<code>[0,0,0,1,1]</code>）$\implies z[1..5] = [+2, +2, +2, -2, -2]$。
       - 逐步追踪：$t=1: v^-=2\to \mathbf{s=1}, v=1$；$t=2: v^-=3\to \mathbf{s=1}, v=2$；$t=3: v^-=4\to \mathbf{s=1}, v=3$；$t=4: v^-=3+(-2)=1 \ge 1 \to \mathbf{s=1}, v=0$（前 3 步攒了高达 $3$ 的余电，导致第 4 步哪怕收到 $-2$ 还在发第 4 个脉冲！）；$t=5: v^-=-2\to s=0, v=\mathbf{-2}$！
       - 共发 <b>4 个脉冲</b>，SNN 输出暴涨成 $\varphi^{(l)}(5) = \frac{4}{5} = \mathbf{0.80} > 0.40$（多发了一倍！核对第 1 节裂项公式：$0.40 - \frac{-2 - 0}{5} = 0.80$——正是末态负余电 $v[5]=-2 < 0$ 记下了“透支多发”的铁证！）。
    3. <b>情形 C（负脉冲先到、正脉冲后扎堆 </b><b>$\implies$</b><b> 漏发砍半！）</b>：1 号在 $t=3,4,5$ 发（<code>[0,0,1,1,1]</code>），2 号在 $t=1,2$ 先发（<code>[1,1,0,0,0]</code>）$\implies z[1..5] = [-2, -2, +2, +2, +2]$。
       - 逐步追踪：$t=1: v=-2$；$t=2: v=-4$；$t=3: v=-2$；$t=4: v=0$（前两次正脉冲全拿去填负债坑了！）；$t=5: v^-=+2 \ge 1 \to \mathbf{s=1}, v=\mathbf{+1}$！
       - 只在第 5 步发了 <b>1 个脉冲</b>（剩下一格电量 $v[5]=+1$ 来不及在下一拍发出了），SNN 输出跌成 $\varphi^{(l)}(5) = \frac{1}{5} = \mathbf{0.20} < 0.40$（核对裂项公式：$0.40 - \frac{1 - 0}{5} = 0.20$！）。

---

### 6. 阈值怎样选（最大激活 vs 高分位数）及其与“逐层缩放权重”的严格等价证明

看懂上面三种误差，马上就明白选阈值 $\theta^{(l)} = \lambda^{(l)}$ 是一场<b>截断误差与量化误差的拔河</b>：

- $\lambda^{(l)}$ 设得太小 $\implies$ 大量正常激活超过 $\lambda^{(l)}$，<b>截断误差爆炸</b>；
- $\lambda^{(l)}$ 设得太大 $\implies$ 量化台阶宽度 $\frac{\lambda^{(l)}}{T}$ 变得极粗，绝大多数中等激活在低时间步 $T$ 下连第 1 个台阶都够不着（变成 0 脉冲“哑火”），<b>量化误差爆炸</b>！

<callout icon="✅" color="green_bg">
<b>原文方法核对（</b><b><mention url="https://app.notion.com/p/41b0e3342e6f81a3b2f0dca38f8f241d">SNN Toolbox（2017）</mention></b><b> \[</b>[<b>原文</b>](https://arxiv.org/abs/1612.04052)<b>\] \[</b>[<b>中文</b>](https://app.notion.com/p/41c0e3342e6f8178a7dcc29d4be95557)<b>\] \[</b>[<b>代码</b>](https://github.com/NeuromorphicProcessorProject/snn_toolbox)<b>\] Section 3.2.1–3.2.2 与 Fig. 1，第 4–5 页；</b><b><mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention></b><b> \[</b>[<b>原文</b>](https://arxiv.org/abs/2106.06984)<b>\] \[</b>[<b>中文</b>](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)<b>\] Section 4.2 Eq. 11，第 4 页）</b>：<br />

1. <b>Max-Norm（最大激活归一化，</b><b><mention url="https://app.notion.com/p/41b0e3342e6f814d9c5cd7dbcc3e1841">Weight & Threshold Balancing（2015）</mention></b><b> \[</b>[<b>原文</b>](https://doi.org/10.1109/IJCNN.2015.7280696)<b>\] \[</b>[<b>中文</b>](https://app.notion.com/p/41c0e3342e6f81a3b666db35f4856d1c)<b>\] \[</b>[<b>代码</b>](https://github.com/dannyneil/spiking_relu_conversion)<b>\]）</b>：在训练集校准样本上统计第 $l$ 层所有 ReLU 输出的最大值 $\lambda_{\max}^{(l)} = \max \mathbf{a}^{(l)}$。优点是零截断；致命缺点是极易被单个极端离群像素绑架——Rueckauer 等在原文第 5 页图 1 实测 16,666 张 CIFAR-10 图片发现，首层全局最大激活高达 $\lambda_{\max} = \mathbf{23.16}$，而 <b>99.9% 分位数</b>仅为 $\lambda_{99.9\%} = \mathbf{6.83}$（相差 <b>3.4 倍</b>！）。<br />
2. <b>Robust Percentile（高分位数法，</b><b><mention url="https://app.notion.com/p/41b0e3342e6f81a3b2f0dca38f8f241d">SNN Toolbox（2017）</mention></b><b> \[</b>[<b>原文</b>](https://arxiv.org/abs/1612.04052)<b>\] \[</b>[<b>中文</b>](https://app.notion.com/p/41c0e3342e6f8178a7dcc29d4be95557)<b>\] \[</b>[<b>代码</b>](https://github.com/NeuromorphicProcessorProject/snn_toolbox)<b>\] Section 3.2.2）</b>：取激活分布的 $p\%$ 分位数（常用 $99.9\%$ 或 $99.99\%$）作为 $\lambda^{(l)}$，只牺牲千分之一离群点的微小截断，换取全层其余 $99.9\%$ 神经元的脉冲率提高 3 倍以上（本章 Notebook 第 4 节复现显示 $T=16$ 下均方误差直接降低 <b>6.9 倍</b>，哑火率从 $76.6\%$ 降到 $34.1\%$）；更进一步，<mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention> \[[原文](https://arxiv.org/abs/2106.06984)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)\] 直接对给定 $T$ 网格搜索最小化均方误差 $\min_{\theta} \lVert \mathrm{clipfloor}(\mathbf{a}, T, \theta) - \mathbf{a} \rVert_2^2$。
</callout>

在读不同转换论文时，你会看到两种表面截然不同的写法：一种是<b>“原权重不动、把每层阈值设为 </b><b>$\theta^{(l)}=\lambda^{(l)}$</b><b>（脉冲输出乘回 </b><b>$\lambda^{(l)}$</b><b>）”</b>（如 <mention url="https://app.notion.com/p/41b0e3342e6f815d96d5cd4423a54b93">Spike-Norm（2019）</mention> \[[原文](https://arxiv.org/abs/1802.02627)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81329ee8c1e0b80641b3)\]、<mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention> \[[原文](https://arxiv.org/abs/2303.04347)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)\] \[[代码](https://github.com/putshua/SNN_conversion_QCFS)\]）；另一种是<b>“全网所有层统一用单位阈值 </b><b>$\theta=1$</b><b>、二值脉冲 </b><b>$\{0,1\}$</b><b> 不乘系数，但把权重和偏置按 </b><b>$\lambda$</b><b> 重新缩放”</b>（如 <mention url="https://app.notion.com/p/41b0e3342e6f81a3b2f0dca38f8f241d">SNN Toolbox（2017）</mention> \[[原文](https://arxiv.org/abs/1612.04052)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8178a7dcc29d4be95557)\] \[[代码](https://github.com/NeuromorphicProcessorProject/snn_toolbox)\] Section 3.2.1）。下面我们用 4 行代数严格证明：<b>这两种写法在每一个时间步发出的脉冲序列逐位恒等！</b>

<callout icon="💡" color="gray_bg">
<b>推导（补全两种归一化流派完全等价的逐步证明）</b>：<br /><br />设方案甲保持原权重 $W^{(l)}, \mathbf{b}^{(l)}$，第 $l$ 层阈值为 $\lambda^{(l)} > 0$（约定原始输入层尺度 $\lambda^{(0)} = 1$），初始电位设为 $v^{(l)}[0] = c\,\lambda^{(l)}$（如 $c=0$ 或 $c=1/2$）。在第 $t$ 步，方案甲的充电、发放、复位方程为：

$$
{v^{(l)}}^-[t] = v^{(l)}[t-1] + W^{(l)}\big(\lambda^{(l-1)}\mathbf{s}^{(l-1)}[t]\big) + \mathbf{b}^{(l)}, \quad
\mathbf{s}^{(l)}[t] = H\!\big({v^{(l)}}^-[t] - \lambda^{(l)}\big), \quad
v^{(l)}[t] = {v^{(l)}}^-[t] - \lambda^{(l)}\mathbf{s}^{(l)}[t]
$$

现在定义无量纲归一化膜电位 $\tilde{\mathbf{v}}^{(l)}[t] = \frac{1}{\lambda^{(l)}} \mathbf{v}^{(l)}[t]$（初值 $\tilde{\mathbf{v}}^{(l)}[0] = c$），将上面第一式和第三式两边<b>同时除以正常数 </b><b>$\lambda^{(l)} > 0$</b>：

$$
{\tilde{\mathbf{v}}^{(l)}}^-[t] = \tilde{\mathbf{v}}^{(l)}[t-1] + \underbrace{\left(\frac{\lambda^{(l-1)}}{\lambda^{(l)}} W^{(l)}\right)}_{\tilde{W}^{(l)}} \mathbf{s}^{(l-1)}[t] + \underbrace{\left(\frac{1}{\lambda^{(l)}} \mathbf{b}^{(l)}\right)}_{\tilde{\mathbf{b}}^{(l)}}, \qquad
\tilde{\mathbf{v}}^{(l)}[t] = {\tilde{\mathbf{v}}^{(l)}}^-[t] - 1 \cdot \mathbf{s}^{(l)}[t]
$$

同时，因为正常数缩放不改变不等号方向（$u - \lambda^{(l)} \ge 0 \iff \frac{u}{\lambda^{(l)}} - 1 \ge 0$），发放判定式化为：

$$
\mathbf{s}^{(l)}[t] = H\!\left(\lambda^{(l)}\big({\tilde{\mathbf{v}}^{(l)}}^-[t] - 1\big)\right) = H\!\left({\tilde{\mathbf{v}}^{(l)}}^-[t] - 1\right)
$$

证毕！这正是 <mention url="https://app.notion.com/p/41b0e3342e6f81a3b2f0dca38f8f241d">SNN Toolbox（2017）</mention> \[[原文](https://arxiv.org/abs/1612.04052)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8178a7dcc29d4be95557)\] \[[代码](https://github.com/NeuromorphicProcessorProject/snn_toolbox)\] 第 5 页 Section 3.2.1 的参数归一化公式：

$$
\tilde{W}^{(l)} = \frac{\lambda^{(l-1)}}{\lambda^{(l)}} W^{(l)}, \qquad \tilde{\mathbf{b}}^{(l)} = \frac{1}{\lambda^{(l)}} \mathbf{b}^{(l)}
$$

硬件芯片部署最喜欢方案乙（因为全芯片所有神经元阈值都是统一的 $1$，中间传输纯 $1\text{-bit}$ 脉冲 $\{0, 1\}$，只需在最后一层输出乘回一个标量 $\lambda^{(L)}$ 即可；若只看分类 <code>argmax</code> 大小顺序，连最后的 $\lambda^{(L)}$ 都不用乘！）。
</callout>

---

## 手算例子（两层小网络端到端完整对照：$T = 4, 8, 16, 32$）

### 例 7.2：一个两层 ReLU 网络与转换后脉冲网络在 $T = 4, 8, 16, 32$ 下的并排对决

设输入特征 $\mathbf{x} = [0.8,\; 0.6]^\top \in \mathbb{R}^2$，两层普通网络（第 1 层 3 个神经元，第 2 层 2 个神经元，均带 $\mathrm{ReLU}$）的权重与偏置为：

$$
W^{(1)} = \begin{bmatrix}
1.0 & 0.5 \\
-0.5 & 1.5 \\
0.5 & -1.0
\end{bmatrix} \in \mathbb{R}^{3\times 2}, \quad \mathbf{b}^{(1)} = \begin{bmatrix} 0.1 \\ 0.0 \\ 0.1 \end{bmatrix}, \qquad
W^{(2)} = \begin{bmatrix}
1.0 & 0.5 & -1.0 \\
-0.5 & 1.5 & 0.5
\end{bmatrix} \in \mathbb{R}^{2\times 3}, \quad \mathbf{b}^{(2)} = \begin{bmatrix} 0.05 \\ 0.10 \end{bmatrix}
$$

<b>第 1 步：手算原普通网络（ANN）的精确输出</b>

1. <b>第 1 层</b>：
   - $z_1^{(1)} = 1.0(0.8) + 0.5(0.6) + 0.1 = 0.8 + 0.3 + 0.1 = \mathbf{1.20}$
   - $z_2^{(1)} = -0.5(0.8) + 1.5(0.6) + 0.0 = -0.4 + 0.9 = \mathbf{0.50}$
   - $z_3^{(1)} = 0.5(0.8) - 1.0(0.6) + 0.1 = 0.4 - 0.6 + 0.1 = \mathbf{-0.10}$
   - 过 $\mathrm{ReLU}$ 得 $\mathbf{a}^{(1)} = \mathbf{[1.20,\; 0.50,\; 0.00]^\top}$（3 号神经元处于负半轴静默）。
2. <b>第 2 层</b>：
   - $z_1^{(2)} = 1.0(1.20) + 0.5(0.50) - 1.0(0.00) + 0.05 = 1.20 + 0.25 + 0.05 = \mathbf{1.50}$
   - $z_2^{(2)} = -0.5(1.20) + 1.5(0.50) + 0.5(0.00) + 0.10 = -0.60 + 0.75 + 0.10 = \mathbf{0.25}$
   - 过 $\mathrm{ReLU}$ 得最终精确输出：$\mathbf{a}^{(2)} = \mathbf{[1.5000,\; 0.2500]^\top}$。

<b>第 2 步：原样复制权重转换为两层 IF 脉冲网络，先手算 </b><b>$T=4$</b><b>（半阈值初始化 </b><b>$v[0]=\theta/2$</b><b>）的每一拍</b>

取各层最大激活作为阈值：$\theta^{(1)} = 1.20$（初值 $\mathbf{v}^{(1)}[0] = [0.60, 0.60, 0.60]^\top$），$\theta^{(2)} = 1.50$（初值 $\mathbf{v}^{(2)}[0] = [0.75, 0.75]^\top$）：

1. <b>第 1 层 4 拍过程</b>（每拍恒定流入 $\mathbf{z}^{(1)} = [1.20, 0.50, -0.10]^\top$）：
   - 神经元 1（$z=1.20=\theta^{(1)}$）：每拍都满额发放，$s_1^{(1)}[1..4] = [1, 1, 1, 1]$；
   - 神经元 2（$z=0.50, v[0]=0.60$）：$t=1: 1.10\to 0$；$t=2: 1.60\ge 1.20 \to \mathbf{1}$（余 $0.40$）；$t=3: 0.90\to 0$；$t=4: 1.40\ge 1.20 \to \mathbf{1}$（余 $0.20$），故 $s_2^{(1)}[1..4] = [0, 1, 0, 1]$；
   - 神经元 3（$z=-0.10 < 0$）：电位从 $0.60$ 一路降到 $0.20$，全程静默 $s_3^{(1)}[1..4] = [0, 0, 0, 0]$。
   - 乘回 $\theta^{(1)}=1.20$，第 1 层传给第 2 层的突触后电位在奇数拍 $t=1,3$ 为 $[1.20, 0, 0]^\top$，在偶数拍 $t=2,4$ 为 $[1.20, 1.20, 0]^\top$（4 拍平均为 $[1.20, 0.60, 0]^\top$）。
2. <b>第 2 层 4 拍过程</b>（奇数拍收到 $W^{(2)}[1.2,0,0]^\top+\mathbf{b}^{(2)} = [1.25, -0.50]^\top$；偶数拍收到 $W^{(2)}[1.2,1.2,0]^\top+\mathbf{b}^{(2)} = [1.85, +1.30]^\top$）：
   - $t=1$: $\mathbf{v}^- = [0.75+1.25,\; 0.75-0.50]^\top = [2.00,\; 0.25]^\top \implies \mathbf{s}^{(2)}[1]=[1, 0]^\top$，$\mathbf{v}^{(2)}[1]=[0.50, 0.25]^\top$；
   - $t=2$: $\mathbf{v}^- = [0.50+1.85,\; 0.25+1.30]^\top = [2.35,\; 1.55]^\top \implies \mathbf{s}^{(2)}[2]=[1, 1]^\top$，$\mathbf{v}^{(2)}[2]=[0.85, 0.05]^\top$；
   - $t=3$: $\mathbf{v}^- = [0.85+1.25,\; 0.05-0.50]^\top = [2.10,\; -0.45]^\top \implies \mathbf{s}^{(2)}[3]=[1, 0]^\top$，$\mathbf{v}^{(2)}[3]=[0.60, -0.45]^\top$；
   - $t=4$: $\mathbf{v}^- = [0.60+1.85,\; -0.45+1.30]^\top = [2.45,\; 0.85]^\top \implies \mathbf{s}^{(2)}[4]=[1, 0]^\top$，$\mathbf{v}^{(2)}[4]=[0.95, 0.85]^\top$。
   - 汇总 4 拍脉冲总数 $[4, 1]^\top$，还原物理输出 $\boldsymbol{\varphi}^{(2)}(4) = 1.50 \times [\frac{4}{4}, \frac{1}{4}]^\top = \mathbf{[1.5000,\; 0.3750]^\top}$！短短 4 拍之内，两个输出通道的大小主次关系（$1.50 > 0.375$）已经与原网络（$1.50 > 0.25$）完全一致！

<b>第 3 步：普通网络输出 vs </b><b>$T = 4, 8, 16, 32$</b><b> 脉冲网络输出完整并排对照表</b>

下表并排展示三种配置在 $T = 4, 8, 16, 32$ 下的真实运行结果（包含分类头常用的“末层不发脉冲、直接对膜电位输入求平均 $\frac{1}{T}\sum_{t=1}^T \mathbf{z}^{(2)}[t]$”读出方式，见 <mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention> \[[原文](https://arxiv.org/abs/2106.06984)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)\] 第 3 页）：

| 模型 / 时间步 $T$ | 两层脉冲输出（$v[0]=0$ 向下取整） | 与 ANN 的 $\ell_2$ 误差 | 两层脉冲输出（$v[0]=\theta/2$ 四舍五入） | 与 ANN 的 $\ell_2$ 误差 | 第 1 层脉冲 + 末层直接积分读出（$v[0]=\theta/2$） | 与 ANN 的 $\ell_2$ 误差 |
| --- | --- | --- | --- | --- | --- | --- |
| <b>原普通网络（ANN 基准）</b> | <b><code>[1.5000, 0.2500]</code></b> | <code>0.0000</code> | <b><code>[1.5000, 0.2500]</code></b> | <code>0.0000</code> | <b><code>[1.5000, 0.2500]</code></b> | <code>0.0000</code> |
| <b>$T = 4$</b> | <code>[1.1250, 0.0000]</code> | <code>0.4507</code> | <code>[1.5000, 0.3750]</code> | <code>0.1250</code> | <code>[1.5500, 0.4000]</code> | <code>0.1581</code> |
| <b>$T = 8$</b> | <code>[1.3125, 0.0000]</code> | <code>0.3125</code> | <code>[1.5000, 0.3750]</code> | <code>0.1250</code> | <code>[1.4750, 0.1750]</code> | <code>0.0791</code> |
| <b>$T = 16$</b> | <code>[1.4062, 0.1875]</code> | <code>0.1127</code> | <code>[1.5000, 0.2812]</code> | <code>0.0313</code> | <code>[1.5125, 0.2875]</code> | <code>0.0395</code> |
| <b>$T = 32$</b> | <code>[1.4531, 0.1875]</code> | <code>0.0781</code> | <b><code>[1.5000, 0.2812]</code></b> | <b><code>0.0313</code></b> | <b><code>[1.4938, 0.2312]</code></b> | <b><code>0.0198</code></b> |

从这张并排对照表一眼能读出两条核心规律：

1. <b>$v[0]=0$</b><b> 在极低时间步有多伤</b>：在 $T=4$ 和 $T=8$ 时，$v[0]=0$ 的第 2 个输出神经元因为层层向下取整，直接变成 <code>0.0000</code>（哑火了）；仅把初始膜电位改成 $v[0]=\theta/2$，不改一个权重，$T=4$ 的误差就从 <code>0.4507</code> 骤降到 <code>0.1250</code>（缩小了 <b>3.6 倍</b>）！
2. <b>随时间步翻倍，误差按 </b><b>$O(1/T)$</b><b> 稳步收敛</b>：在末层直接积分读出列，$T=4 \to 8 \to 16 \to 32$ 每翻一倍，误差 <code>0.1581 -> 0.0791 -> 0.0395 -> 0.0198</code> <b>精确减半</b>！

---

## 代码验证

- 仓库路径：[<code>notion/notebooks/ch07_ann2snn_rate_and_errors.ipynb</code>](https://github.com/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch07_ann2snn_rate_and_errors.ipynb)
- 浏览器一键运行：[Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch07_ann2snn_rate_and_errors.ipynb)
- 验证结果摘录：901 个测试点上裂项恒等式最大误差 <code>< 1e-12</code>；QCFS Theorem 1（$T=L=4$）误差严格为 <code>0.0</code>，Theorem 2（$L=4 \to T=8, \phi=0.5$）均匀分布平均误差为 <code>+0.000000</code>；三种误差手算例（截断 <code>1.00 vs 1.50</code>、量化 <code>0.25/0.50 vs 0.45</code>、到达不均匀 <code>0.40 / 0.80 / 0.20</code>）、阈值/权重缩放逐步脉冲等价性与两层网络 $T=4,8,16,32$ 对照表全部与正文逐位一致。

---

## 常见误解

1. <b>误解一：“既然 </b><b>$v[0] = \theta/2$</b><b> 能让期望量化误差等于 </b><b>$0$</b><b>（QCFS 定理 2），那单张图片在 </b><b>$T=4$</b><b> 时的转换误差也等于 </b><b>$0$</b><b> 了！”</b>
   - <b>纠正</b>：<b>期望为 </b><b>$0$</b><b> 不等于逐个神经元误差为 </b><b>$0$</b><b>！</b> “期望为 $0$”是指在大量神经元上，有的高估 $+0.05$、有的低估 $-0.05$，正负平均抵消了系统性偏移；但具体到每一个单独的特征通道，它仍然带着最大可达 $\pm\frac{\theta}{2T}$ 的量化噪声。在普通卷积网络里，下一层做几百个通道加权求和时正负误差确实会互相抵消一大部分；但在第 5 章的 ViG / DGCNN 里，对邻居取 <code>max</code> 会专挑被正向高估的那个通道（第 9 章最大化偏置），算 $k$-NN 距离也可能被单个通道误差推翻排序（第 10 章）！
2. <b>误解二：“到达不均匀误差是因为时间步 </b><b>$T$</b><b> 太短，只要上一层的发放率 </b><b>$r^{(l-1)}$</b><b> 准了，下一层肯定也准。”</b>
   - <b>纠正</b>：回看例 7.1C！在例 7.1C 中，上一层的平均发放率 $[0.6, 0.4]$ 已经是 <b>100% 精确无误</b>的了，仅仅因为正脉冲先到、负脉冲后到，本层输出就从 <code>0.40</code> 翻倍跳到了 <code>0.80</code>！这也是为什么第 8 章的带符号脉冲神经元（允许在 $v \le -\theta$ 时发 <code>-1</code> 负脉冲把透支多发的脉冲追回来！）和差分编码（<mention url="https://app.notion.com/p/41b0e3342e6f81d8b1d1ccbe05acdde2">DCGS（2025）</mention> \[[原文](https://arxiv.org/abs/2503.00301)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81aaa37dce2e24d59585)\] \[[代码](https://github.com/h-z-h-cell/ANN-to-SNN-DCGS)\]）对压低超低时间步误差如此关键。
3. <b>误解三：“网络最后一层（分类头 Logits）也必须加 IF 神经元发 0/1 脉冲。”</b>
   - <b>纠正</b>：绝不能给最后一层分类 Logits 套普通单向 IF 神经元！因为分类头的输出可正可负（而且后面没有 ReLU），如果套上只发非负脉冲的 IF 神经元，所有负 Logit 都会被抹成 $0$，大数值还会被阈值截断。标准做法（见 <mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention> \[[原文](https://arxiv.org/abs/2106.06984)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)\] Section 3 第 3 页）是最后一层只把突触电流在膜电位里累加起来求平均（不触发阶跃发放），既不增加任何乘法，又无损保留全部正负分数。

---

## 和论文的关系

- <b>裂项求和推导、复位对比、偏置电流、权重缩放与 99.9% 分位数归一化</b>：完整对应 <mention url="https://app.notion.com/p/41b0e3342e6f81a3b2f0dca38f8f241d">SNN Toolbox（2017）</mention> \[[原文](https://arxiv.org/abs/1612.04052)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8178a7dcc29d4be95557)\] \[[代码](https://github.com/NeuromorphicProcessorProject/snn_toolbox)\] Section 2 Eq. (1)–(8) 与 Section 3.1–3.2（第 2–5 页）；逐层激活阈值缩放参见 <mention url="https://app.notion.com/p/41b0e3342e6f815d96d5cd4423a54b93">Spike-Norm（2019）</mention> \[[原文](https://arxiv.org/abs/1802.02627)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81329ee8c1e0b80641b3)\]。
- <b>三种转换误差（截断、量化、到达不均匀）分类、QCFS 激活函数与定理 1–2</b>：逐字对应 <mention url="https://app.notion.com/p/41b0e3342e6f810591f7f303160e35ff">QCFS（2022）</mention> \[[原文](https://arxiv.org/abs/2303.04347)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81c494d8f8bb510b7924)\] \[[代码](https://github.com/putshua/SNN_conversion_QCFS)\] Section 2–4 Eq. (1)–(17) 及图 1–2（第 2–6 页）。其前驱“半阈值偏置平移”思想源自 <mention url="https://app.notion.com/p/41b0e3342e6f817ba806f0c2e0b5306c">RTS / Optimal Conversion（2021）</mention> \[[原文](https://arxiv.org/abs/2103.00476)\] \[[中文](https://app.notion.com/p/41c0e3342e6f813ba15fee9b1cc7ae68)\] \[[代码](https://github.com/Jackn0/snn_optimal_conversion_pipeline)\]。
- <b>基于少量校准数据的 MMSE 阈值搜索与逐层偏差校准</b>：对应 <mention url="https://app.notion.com/p/41b0e3342e6f81449ff6c194ab8d964a">SNNC-AP / SNN Calibration（2021）</mention> \[[原文](https://arxiv.org/abs/2106.06984)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8147a4e0d2bb781d13cd)\] Section 4 Eq. (7)–(12)（第 3–4 页）。
- <b>固定图 GCN 的直接线性穿透转换</b>：<mention url="https://app.notion.com/p/41b0e3342e6f8142af44e1d41fa091ff">One-Spike SNN（2025）</mention> \[[原文](https://arxiv.org/abs/2403.08786)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81efadabda09415c2abe)\] 第 IV-C 节之所以能把两层 ReLU Text GCN 直接免训练转成脉冲网络，依靠的正是本章第 4 节的线性穿透律（将 $\hat{A}(XW)$ 视为两次连续线性映射）。

---

## 练习

1. <b>（手算裂项公式与半阈值脉冲数）</b> 设恒定输入电流 $z = 0.70$，阈值 $\theta = 1.0$，总时间步 $T = 5$。请分别用闭式公式 $N_{\mathrm{sp}}(T) = \lfloor \frac{zT + v[0]}{\theta} \rfloor$ 和逐步追踪核对：（a）当 $v[0] = 0$ 时发几个脉冲、末态膜电位 $v[5]$ 是多少、脉冲输出 $\varphi(5)$ 与 $\mathrm{ReLU}(0.70)$ 差多少？（b）当 $v[0] = 0.5$ 时发几个脉冲、$v[5]$ 是多少、误差变成多少？
2. <b>（手算构造到达不均匀误差）</b> 设 $T = 4,\; \theta = 1.0,\; v[0] = 0$，连接权重为 $W = [1.5,\; -1.5]$。前一层两个神经元在 4 步内都各发了 <b>2 个脉冲</b>（即平均输入完全相等 $\boldsymbol{\varphi}^{(l-1)}(4) = [0.5, 0.5]^\top$，故原网络输出应为 $\mathrm{ReLU}(1.5\times 0.5 - 1.5\times 0.5) = \mathbf{0.0}$！）。请构造一组两路脉冲的到达时刻（如 1 号在 $t=1,2$ 发、2 号在 $t=3,4$ 发），手算本层神经元居然误发了几个脉冲、末态膜电位 $v[4]$ 是多少！
3. <b>（手算权重缩放归一化）</b> 一个两层 ReLU 网络在训练集上测得第 1 层激活 99.9% 分位数为 $\lambda^{(1)} = 4.0$，第 2 层为 $\lambda^{(2)} = 2.0$（输入已归一化 $\lambda^{(0)} = 1.0$）。若原第 1、2 层标量权重偏置分别为 $(w^{(1)}=2.0, b^{(1)}=-0.8)$ 和 $(w^{(2)}=1.5, b^{(2)}=0.4)$，请算出统一单位阈值 $\theta=1$ 下的缩放参数 $(\tilde{w}^{(1)}, \tilde{b}^{(1)})$ 与 $(\tilde{w}^{(2)}, \tilde{b}^{(2)})$。
4. <b>（改代码看现象）</b> 打开 <code>ch07_ann2snn_rate_and_errors.ipynb</code> 第 5 节，把两层网络的阈值从“恰好等于最大激活 <code>th1_net=1.20, th2_net=1.50</code>”故意改小一半变成 <code>th1_net=0.60, th2_net=0.75</code>（触发严重截断误差），观察当 $T$ 从 <code>4</code> 增加到 <code>32</code> 甚至 <code>1024</code> 时，输出误差还会收敛到 <code>0</code> 吗？为什么？

<toggle>
点击展开练习 1～4 参考答案

1. <b>手算 </b><b>$z=0.70, T=5, \theta=1.0$</b>：
   - （a）$v[0]=0$：公式给 $N_{\mathrm{sp}}(5) = \lfloor 3.5 \rfloor = \mathbf{3}$ 个脉冲；由电荷守恒 $v[5] = 0 + 3.5 - 3 = \mathbf{0.50}$；输出 $\varphi(5) = \frac{3}{5} = \mathbf{0.60}$，误差为 $0.60 - 0.70 = \mathbf{-0.10}$（逐步核对：$0.7\to 1.4(\text{发},0.4)\to 1.1(\text{发},0.1)\to 0.8\to 1.5(\text{发},0.5)$，确为 3 次）。
   - （b）$v[0]=0.5$：公式给 $N_{\mathrm{sp}}(5) = \lfloor 3.5 + 0.5 \rfloor = \lfloor 4.0 \rfloor = \mathbf{4}$ 个脉冲；$v[5] = 0.5 + 3.5 - 4 = \mathbf{0.00}$；输出 $\varphi(5) = \frac{4}{5} = \mathbf{0.80}$，误差为 $+0.10$（因 $3.5$ 恰好卡在整数 $3$ 和 $4$ 正中间）。
2. <b>零均值输入竟误发 2 个脉冲！</b>
   - 设 $s_1 = [1, 1, 0, 0]$，$s_2 = [0, 0, 1, 1]$，则输入电流为 $z[1..4] = [+1.5, +1.5, -1.5, -1.5]$（总和为 $0$）：
   - $t=1$: $v^-=1.5 \implies \mathbf{s=1}, v=0.5$；
   - $t=2$: $v^-=2.0 \implies \mathbf{s=1}, v=1.0$；
   - $t=3$: $v^-=1.0 - 1.5 = -0.5 \implies s=0, v=-0.5$；
   - $t=4$: $v^-=-0.5 - 1.5 = -2.0 \implies s=0, v=\mathbf{-2.0}$！
   - 原网络输出明明是 <b>$0.0$</b>，脉冲网络却凭空误发了 <b>2 个脉冲</b>（输出 $2/4 = \mathbf{0.50}$！若权重放大为 $[2,-2]$ 则误发 3 个脉冲），末态留下负电位 $v[4] = -2.0$——这就是第 8 章为什么要引入“负阈值发 <code>-1</code> 负脉冲”把这 2 个冤枉脉冲退回去的最直观动机！
3. <b>权重偏置缩放</b>：
   - 第 1 层：$\tilde{w}^{(1)} = \frac{\lambda^{(0)}}{\lambda^{(1)}} w^{(1)} = \frac{1.0}{4.0}\times 2.0 = \mathbf{0.5}$，$\tilde{b}^{(1)} = \frac{1}{4.0}(-0.8) = \mathbf{-0.2}$。
   - 第 2 层：$\tilde{w}^{(2)} = \frac{\lambda^{(1)}}{\lambda^{(2)}} w^{(2)} = \frac{4.0}{2.0}\times 1.5 = \mathbf{3.0}$，$\tilde{b}^{(2)} = \frac{1}{2.0}(0.4) = \mathbf{0.2}$。
4. <b>改代码现象</b>：当阈值设成 <code>0.60, 0.75</code> 时，第 1 层真实激活 <code>1.20</code> 被死死截断在 <code>0.60</code>，第 2 层真实激活也被死死截断在 <code>0.75</code>；哪怕把 $T$ 改到 <code>1024</code> 甚至无穷大，误差也死死卡在 <code>> 0.75</code> <b>永远不会归零</b>！因为增加时间步 $T$ 只能消除<b>量化误差</b>（$\propto 1/T$），绝对消不掉阈值过低造成的<b>截断误差</b>！
</toggle>

---

## 三句话小结

1. 对减法复位 IF 神经元在 $1..T$ 上做裂项求和，严格推出发放率恒等式 $r = \frac{1}{\theta}\big(\bar{z} - \frac{v[T]-v[0]}{T}\big)$，结合 $r \in \{0, \frac{1}{T}, \dots, 1\}$ 证明了脉冲神经元在数学上就是“截断并量化的 ReLU”，且半阈值初始化 $v[0]=\theta/2$ 能将向下取整变为四舍五入、使最大量化误差减半且期望误差归零。
2. 全连接、卷积与固定图 GCN 之所以能一字不改直接复制原网络权重 $W$，完全仰仗矩阵乘法与时间平均可交换顺序的线性性质 $\frac{1}{T}\sum_t W\mathbf{s}[t] = W\mathbf{r}$，而取最大值 <code>max</code> 和乘法不满足线性，逐步运算会产生严重偏差。
3. 转换误差由截断误差（超阈值饱和）、量化误差（有限步离散取整）和到达不均匀误差（正负脉冲先后错位导致 $v[T] \notin [0,\theta)$）三部分组成；增加时间步 $T$ 能按 $1/T$ 压低量化误差，而压低超低时间步下的后两类误差正是第 8 章多阈值与差分编码的用武之地。
