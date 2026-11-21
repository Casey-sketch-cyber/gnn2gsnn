# 项目进度（交接记录）

> 每个 AI 结束工作前在最上方追加一条记录，新的在上面。

## 当前状态
任务 01、02 已完成并合并（PR #1、#2）。任务 04 第 1～3 批已合并（PR #3、#4、#5）；第 4 批（`gemini/deep-04`：第 11～13 章推导与 notebook、学习路线页、自测题汇总、全站通俗页与推导页互链，以及 PR #5 指定的 DCGS 原文复核）已完成并待提交 PR #6 由 Claude 审查。至此全 13 章第一性原理数学主线与 13 个配套 Notebook 全部交付完毕。仍只有官方链接的 15 篇论文（3 篇 OpenReview 拦截、12 篇需机构访问）等项目所有者下载后补嵌。文献树 v1 的若干判断已被任务 01 推翻，待任务 03 修订为 v2。

## 待办
- [x] 任务 01：文献收集与核查（Gemini，PR #1 已合并）
- [x] 任务 02：Notion 通俗讲解（Gemini，PR #2 已合并）
- [ ] 任务 04：从第一性原理讲透，并配齐论文与中文精读（Gemini，分七批；第 1～3 批已合并，PR #3、#4、#5；第 4 批待审 PR #6；下一批：第 5 批 A 层中文全文/中文 PDF/精读笔记）
- [ ] 任务 03：Claude 审查并把文献树修订为 v2

## 已知问题
- 文献树 v1 没有通读任何论文全文；"未见图网络免训练转换"等结论只基于有限检索。
- 文献树 v1 的路线图在在线版里是一张图，仓库版改成了表格，内容相同。

---

## 工作记录

### 2026-11-21 · gemini · gemini/deep-04（任务 04 第 4 批）
- **完成**：按 `tasks/04-deep-curriculum.md` 第 4 批范围及 Claude 在 PR #5 审查评论中的复核要求与字体回退建议，完成线上 Notion 与仓库全部交付物：
  - **PR #5 复核要求**：对照本机已下载的 `2025-DCGS.pdf`（`arXiv:2503.00301v3`）第 5 页与 Appendix J（第 24 页）逐字符复核了第 8 章引用的式 (20)(21) 与 (93)–(100)，**编号与符号全部逐字一致**（附注两处原文小瑕疵：第 5 页写初值 `m_r^l[0]` 而式 20 从 `t=1` 起始；第 24 页式 100 左侧参数写 `m^l[t]` 而右侧分枝写 `x`）。
  - **数学主线第 11～13 章（A，全 13 章收官）**：严格遵循 11 节固定结构与原文逐字符核对规范，在 Notion 总页面下上线并实时导出至 `notion/export/derivations/`：
    - 《第 11 章 只算变化的部分》（`ch11-只算变化的部分.md`）：线性层增量穿透（偏置只在第 0 帧加一次）与 `DeltaCNN (CVPR 2022)` ReLU 非线性反例；逐字符核对 `DeltaCNN` 式 (1)(3)(5)(6) 双缓冲机制、`Sigma-Delta (ICLR 2017)` Alg. 1–3 与 Eq. (1)–(2) Herding 取整等价性，以及 `AEGNN (CVPR 2022)` Sec. 4.2 Eq. (6)–(7) $k$ 跳子图；以「推导（非论文原文）」证明单层残差缓冲零漂移上界 $\lVert \hat{\mathbf{x}}_t-\mathbf{x}_t\rVert_\infty < \Theta$ 与 $L$ 层级联误差递推界 $e_L \le \sum_l \epsilon_l \prod_{m>l}\lVert W^{(m)}\rVert_\infty$；完成 6 帧缓慢爬坡例 11.1 与 5 节点链状图 $k$ 跳扩散及阈值截断例 11.2。
    - 《第 12 章 省电到底怎么算》（`ch12-省电到底怎么算.md`）：完整完成**验收标准第 6 条**。推导 SynOps 与每突触累计事件数 $\rho=rT$；逐项核对 `Horowitz (ISSCC 2014, p. 14 Fig. 1.1.9)` 45nm 原始运算与访存表（解释 `4.6 pJ / 0.9 pJ` 来源及 INT8 `0.23 / 0.30 pJ` 重算）；以 3 层网络 `64→128→64→10` 例 12.1 手算示范从“FP32 省电 3.76×”到“计入 INT8 与 8KB SRAM 权重/膜电位读写后反超为 1.49×”的翻转现象；逐字符核对 `Yan 等 (IEEE TCAD 2026, arXiv:2409.08290v6)` QNN-SNN Twin 定理 1–2、命题 1 与式 (2)–(8) 并复现 22nm 盈亏曲线。
    - 《第 13 章 把全部串起来》（`ch13-把全部串起来.md`）：端到端 4 节点 2 层固定图 GCN 免训练转换对照（$T=4,8,16,32$ 输出误差、预测一致率与 FP32 能耗比同步并排），再将第 2 层替换为动态 $k$-NN（$k=2$）+ 有符号 `max-relative`（ViG 风格），对比 IF 逐拍 `max`、IF 还原率与 DCGS（$n=4$）的邻居翻转与 MAE，收束至本项目三大研究高墙并直链通俗第 8 页《8 可以做的论文》。
  - **配套可运行代码（B，全 13 个 Notebook 收官）**：新增 `ch11_delta_and_sparse_updates.ipynb`（18 处 `assert`）、`ch12_energy_and_quantization.ipynb`（21 处 `assert`）、`ch13_end_to_end_gnn2gsnn.ipynb`（9 处 `assert`），均按 Claude 建议内置 `setup_plot_font()` 自动检测中文字体并在无中文字体环境下回退英文标签；更新 `notion/notebooks/README.md`，并在 `.venv` 中从头到尾重跑全部 **13 个 Notebook（`ch01`～`ch13`，共 148 处 `assert`）**，全部零警告、零报错通过。
  - **学习路线页（D.1）、自测题汇总（D.4）与全站互链（与已有页面的衔接）**：
    - 上线并导出《学习路线》（`notion/export/学习路线.md`：Mermaid 概念依赖图 + 标明“估计”的快速/标准/深入三条路线与 23 篇 A 层论文清单）与《自测题汇总》（`notion/export/自测题汇总.md`：按七条验收标准分 7 组，每组含手算/推导题、代码验证题与折叠答案）。
    - 总页面（`index.md`）新增“怎么用这份资料（通俗页与推导页的配合）”并更新进度为全 13 章已完成；任务 02 全部 11 篇通俗页（`00`～`10`）在不删除任何原有内容的前提下，在各相关段落末尾补齐“想看推导：第 N 章”双向跳转链接并全部实时重新导出；同步更新 `符号表.md`、`常见困惑.md`（追加第 11～13 章误解 #15–17）与 `notion/README.md`。
- **未完成**：待推送 `gemini/deep-04` 创建 PR #6 由 Claude 审查合并后，再进入第 5 批（`gemini/deep-05`：A 层 23 篇中文全文、中文 PDF、精读笔记、“怎么读论文”页与 `scripts/check_translation.py`）。
- **注意 / 坑**：
  - Notion 的 `notion-fetch` 大文件输出保存至 `.system_generated/steps/*/output.txt` 时顶部带 `Created At:` / `Completed At:` 两行元信息，批量导出脚本须先定位 JSON 起始位置再用 `raw_decode` 解析，否则会回退命中历史旧版本。

### 2026-11-21 · claude · main（审查 PR #5）
- 审查并合并 PR #5（任务 04 第 3 批：第 8～10 章与配套 notebook、PR #4 两处措辞修订）。
- 核对：10 个 notebook 全部重跑通过；第 8 章 DCGS 归纳式用独立模拟验证（误差 ≤1e-14）；第 9 章 E[max]=(k−1)/(k+1)ε 蒙特卡洛一致；第 10 章例 10.1 与 4ε 紧界构造正确；两处措辞已改好；未新增 PDF 或中文全文。
- 未核对：第 8 章所引 DCGS 式 (20)(21)、(94)–(100) 与 arXiv 2503.00301v3 原文的逐字一致性（本次未能打开原文），已在 PR 评论中请第 4 批执行者复核。
- 非阻塞建议：notebook 图中中文字体缺失时回退为英文标签。

### 2026-11-19 · gemini · gemini/deep-03（任务 04 第 3 批）
- **完成**：按 `tasks/04-deep-curriculum.md` 第 3 批范围及 Claude 在 PR #4 审查评论末尾的两处措辞提醒，完成线上 Notion 与仓库全部交付物：
  - **PR #4 两处措辞修订（Notion 与 `notion/export/` 同步更新）**：
    - `第 7 章`（`ch07-核心-为什么发放率约等于ReLU.md`）：将半阈值初值 `v[0]=θ/2` 的评述从第 3 节绿色原文事实框中移出并改为黄色「判断」框，修改为“不需要重训，可以直接用在现成的 ReLU 网络上；但 Theorem 2 给出‘零期望误差’的理论保证依赖前激活在量化区间内服从均匀分布的假设”。
    - `常见困惑`（`常见困惑.md`）：将一屏答透第 2 点中的“什么都不干（零能耗！）”改为“不做加法（注：不做突触计算，但存储访问和神经元状态维持仍要耗能，详见第 12 章）”。
  - **数学主线第 8～10 章（A）**：严格遵循 11 节固定结构与原文逐字符核对规范，在 Notion 总页面下上线并实时导出至 `notion/export/derivations/`：
    - 《第 8 章 带符号、多阈值和差分编码》（`ch08-带符号-多阈值和差分编码.md`）：完成验收标准第 7 条 DCGS 半壁（与第 5 章 ViG 共同完成第 7 条）。逐字符核对 `DCGS (arXiv:2503.00301v3)` 全部方法公式（Section 3.1 式 1–6，Section 4.1 定义 4.1 式 13–14、定理 4.2–4.5 式 15–22，Section 4.2 式 23–30，Section 4.3 式 31–34，Appendix P Algorithm 3）；指出原文主文定理 4.3 式 (19) 符号笔误（附录 D 式 48 证明正确，应为 $m^l[t-1]$ 配加号或 $m^l[t]$ 配减号）、式 (33) 边界笔误（$1<i\le n \to 1\le i\le n$）与 Algorithm 3 IEEE-754 位操作死区边界 $\frac{3}{4}\cdot 2^{-(n-1)}$；以「推导（非论文原文）」显式补全定理 4.4 式 (20) 中 $m_r^l[t]$ 不乘 $t$ 的隐藏归纳恒等式 $v^l[t-1]=(t-1)m_r^l[t]+v^l[0]$，并在 $T=4, n=3$ 下完整手算验证。
    - 《第 9 章 非线性运算为什么难转换》（`ch09-非线性运算为什么难转换.md`）：构造 2 步脉冲 `max` 反例（高估 `200%`）与最大化正偏置闭式推导 $\mathbb{E}[\max_{1\le j\le k}\eta_j]=\frac{k-1}{k+1}\epsilon$；逐字符核对 Bu 等 `Inference-Scale Conversion (CVPR 2025, arXiv:2409.03368)` 定理 2 式 (16)/(S19) 与 `Burst+LIPooling (IJCAI 2022)` 式 (11)，以「推导（非论文原文）」补出 SNN 时序胜者不变条件并阐明 ViG 的有符号 `max-relative` 无法套用的原因；给出双变量乘法零/倍错位反例及 `SpikeZIP-TF (arXiv:2406.03470)` 式 (4) 增量乘积恒等式推导（与 DCGS 定理 4.3 对照），并逐一分析 GELU、Softmax、LayerNorm 不可线性穿透及不可像 BN 那样折叠的根因。
    - 《第 10 章 近似误差会不会让选邻居出错》（`ch10-近似误差会不会让选邻居出错.md`）：完整完成验收标准第 5 条。一步不跳用三角不等式证出两两距离 $2\varepsilon$ 界与 top-$k$ 邻居集合不变的 $4\varepsilon$ 充分条件，并用 4 节点二维手算例 10.1（$\Delta d_2=0.50,\varepsilon_{\mathrm{crit}}=0.125$）证明 $4\varepsilon$ 是无法再缩小的紧界；以「推导（非论文原文）」把第 7 章逐通道量化误差转换为 $C$ 维向量 $\ell_2$ 范数界 $\varepsilon_{\max}(T)=\sqrt{C}\delta(T)$、$\varepsilon_{\mathrm{RMS}}(T)=\frac{\sqrt{C}\theta}{\sqrt{12}T}$ 与充分时间步下界 $T>\frac{2\sqrt{C}\theta}{\Delta d_k(i)}$；在模拟 49 节点 32 通道 $k=9$ 视觉图上验证 $\Delta d_9(i)>4\varepsilon_{\mathrm{emp}}$ 节点零翻转，并分析 $v[0]=0$ 常数偏置在差值中抵消及低 $T$ 量化并列对邻居翻转率的冲击。
  - **配套可运行代码（B）**：新增 `ch08_signed_multithreshold_diff.ipynb`（22 处 `assert`）、`ch09_nonlinear_operators.ipynb`（18 处 `assert`）、`ch10_knn_stability.ipynb`（10 处 `assert`），更新 `notion/notebooks/README.md`，并在 `.venv` 中从头到尾重跑全部 **10 个 Notebook（`ch01`～`ch10`，共 100 处 `assert`）**，全部无报错、零警告通过。
  - **辅助页与目录同步**：更新 Notion 及导出的总页、`符号表.md`（新增第 8～10 章记号并将 DCGS 原文列与 `arXiv:2503.00301v3` 逐字对齐）、`常见困惑.md`（补充第 8～10 章误解 #12–14）及 `notion/README.md`。
- **未完成**：待推送 `gemini/deep-03` 创建 PR #5 由 Claude 审查合并后，再开始第 4 批（`gemini/deep-04`：第 11～13 章及 notebook）。
- **注意 / 坑**：
  - `DCGS (arXiv:2503.00301v3)` 正文定理 4.3 式 (19) 与附录 D 式 (45) 存在符号笔误（把证明式 48 的 $m^l[t-1]$ 误印成 $m^l[t]$ 而未将第一项改减号），第 8 章及 `ch08` Notebook 已用数值断言同时验证原文式 (19) 报错与附录式 (48) 恒等成立。
  - 模拟视觉图测试揭示了半阈值 $v[0]=\theta/2$ 在极低 $T=2$ 时会因多节点坍缩到少量离散量化点产生并列 ties，导致 $k$-NN 翻转率反而高于 $v[0]=0$ 的常数偏移，已在第 10 章第 6 节如实呈现并分析原因。

### 2026-11-19 · claude · main（审查 PR #4）
- **完成**：审查并合并任务 04 第 2 批。7 个 notebook 全部跑通（50 处 assert）；独立模拟重算例 7.2 的 24 个数字全部一致；核对了第 5～7 章的手算例子和推导，以及 MobileViG 原文笔误的说法。详见 PR #4 审查评论。
- **未核实**：Google 云端硬盘的共享设置与嵌入；QCFS 公式未逐字对照原文。
- **注意 / 坑**：审查评论末尾有两处措辞请第 3 批顺手改（Notion 和导出同时改）。

### 2026-11-18 · gemini · gemini/deep-02（任务 04 第 2 批）
- **完成**：按 `tasks/04-deep-curriculum.md` 第 2 批范围及 Claude 在 PR #3 末尾的三点提醒，完成线上 Notion、受限 Google 云端硬盘与仓库全部交付物：
  - **数学主线第 5～7 章（A）**：严格遵循 11 节固定结构与原文逐字符核对规范，在 Notion 总页面下上线并实时导出至 `notion/export/derivations/`：
    - 《第 5 章 视觉图网络》（`ch05-视觉图网络.md`）：图像切块矩阵投影与步幅卷积恒等性；两两平方欧氏距离矩阵公式 $D_{\mathrm{dist}}=\mathbf{q}\mathbf{1}_N^\top+\mathbf{1}_N\mathbf{q}^\top-2XX^\top$ 四步展开与通道 $\ell_2$ 归一化 $2-2\cos$ 简化；`ViG` 的 `max-relative` 有符号差逐通道最大值手算（4 节点 $k=2$，直观展示局部峰值处 $\mathbf{m}_2=[-1,+1]^\top$ 正负并存）；横向对照 `DGCNN EdgeConv`、`MobileViG SVGA`（核实其 `X - roll(X)` 反号细节，并指出原文第 5 页式 2 笔误 $Z=\sigma(XW_1)W_2+Y \to \sigma(YW_1)W_2+Y$）与 `ST-GCN`。
    - 《第 6 章 脉冲神经元》（`ch06-脉冲神经元.md`）：IF 与 LIF 离散时间三步方程及 LIF 转换死区 $z \le (1-\beta)\theta$ 推导；置零复位 vs 减法复位两张 10 步完整状态表（$z=0.6,\theta=1$）；验收标准第 2 条核心手算表（$z=0.3,\theta=1,v[0]=0,T=10$，第 4、7、10 步共 3 次脉冲，$r=0.3$）及 Python `float64` 第 10 步算出 `0.9999999999999998 < 1.0` 漏掉第 3 个脉冲与 `1e-9` 容差修正。
    - 《第 7 章 核心：为什么发放率约等于 ReLU》（`ch07-核心-为什么发放率约等于ReLU.md`）：一步不跳裂项求和推出电荷守恒与发放率精确恒等式 $r=\frac{1}{\theta}\big(\bar{z}-\frac{v[T]-v[0]}{T}\big)$；归纳证明恒定输入下 $0\le v[T]<\theta$ 并导出闭式解（验收标准第 3 条前半）；半阈值初值 $v[0]=\theta/2$ 四舍五入误差减半推导及与 `QCFS` 式 13–16、定理 1–2 对照；线性穿透证明及 `max`、乘法双反例（验收标准第 4 条）；截断误差、量化误差、到达不均匀误差（完整复现 `QCFS` 第 4 页 `[2,-2]@[0.6,0.4]` 三种时序得 `0.40/0.80/0.20`）各一个手算数值例子（验收标准第 3 条后半）；`Max-Norm` vs `99.9%` 分位数阈值与逐层权重缩放 $\tilde{W}^{(l)}=\frac{\lambda^{(l-1)}}{\lambda^{(l)}}W^{(l)}$ 等价性证明；两层小网络在 $T=4,8,16,32$ 下与原网络输出的完整并排对照表。
  - **配套可运行代码（B）**：新增 `ch05_vision_gnn.ipynb`、`ch06_spiking_neurons.ipynb`、`ch07_ann2snn_rate_and_errors.ipynb`，更新 `notion/notebooks/README.md`，并在 `.venv`（仅含 Python 标准库 + NumPy + Matplotlib）中从头到尾重跑全部 **7 个 Notebook（`ch01`～`ch07`）**，所有断言与图表均无报错通过。
  - **常见困惑页（D.3）与符号表同步（D.2）**：上线并导出《常见困惑》（`notion/export/常见困惑.md`，第一屏用 `0.3` 攒水敲铃与纯加法实例答透“神经网络的数值转换成脉冲是什么意思”并链向第 6、7 章，第二部分分类汇总第 1～7 章共 11 组常见误解）；同步补充第 5～7 章新增记号至《符号表》并更新总页面导航。
  - **超 5 MB 论文存入受限 Google 云端硬盘并嵌入 Notion（C2）**：经项目所有者本人授权连接 Google Drive，创建私有受限目录 `gnn2gsnn-papers/原文/` 与 `中文版/`（`audit-permissions` 确认零公开分享、仅本人可见），上传全部 **17 篇 `> 5 MiB`** 已下载公开 PDF 并在各自 Notion 论文页顶部以 `<embed>` 预览块嵌入（至此 118 篇中已有 **103 篇**在 Notion 内直接嵌入原文 PDF）；`literature/papers.csv` 新增第 7 列 `存放位置`（`Notion 附件` 86 篇、`Google 云端硬盘` 17 篇、`仅官方链接` 15 篇）。
- **未完成**：待推送 `gemini/deep-02` 创建 PR #4 由 Claude 审查合并后，再开始第 3 批（`gemini/deep-03`：第 8～10 章及 notebook）；15 篇 `仅官方链接` 论文（12 篇付费期刊/会议 `需机构访问` + 3 篇受 OpenReview `/challenge` 反爬验证拦截的 `STA`、`Adaptive Fission`、`GraphPTQ`）待项目所有者在浏览器下载后补入云端硬盘并嵌入。
- **注意 / 坑**：
  - OpenReview 在内置浏览器中也弹出了 `/challenge` 浏览器验证页（`Verifying your browser | OpenReview`），按安全准则立即停止未尝试绕过；这 3 篇与 12 篇机构访问论文已在 PR #4 说明中逐篇列出原因。
  - Markdown 管道表格单元格内的行内公式若写 `\|`（如双竖线拼接记号），会被 CommonMark 表格解析器优先当作转义竖线拆坏公式，在管道表内应改写为 `\Vert`。

### 2026-11-18 · claude · main（修订任务 04）
- **完成**：按项目所有者要求修订任务 04：超过 5 MB 的 PDF 放他的 Google 云端硬盘并嵌入 Notion（第 2 批处理）；每篇论文另做一份保留排版的中文 PDF（A、B 层随第 5、6 批，C 层新增第 7 批）。
- **注意 / 坑**：Google 账号授权要由项目所有者本人操作；云端硬盘文件共享设置保持"受限"。

### 2026-11-18 · claude · main（审查 PR #3）
- **完成**：审查并合并任务 04 第 1 批。独立跑通 4 个 notebook（23 处 assert 全过），重算例 4.1、例 2.2、例 3.1 和第 1 章练习答案，全部正确；核对了 BN 折叠公式的原文出处。详见 PR #3 审查评论。
- **未核实**：118 篇许可证只确认了 1 篇；Notion 上的附件和子页面无法直接打开。
- **注意 / 坑**：第 2 批的第 7 章是项目所有者最关心的内容，审查评论末尾列了三点要求。

### 2026-11-18 · gemini · gemini/deep-01（任务 04 第 1 批）
- **完成**：按 `tasks/04-deep-curriculum.md` 第 1 批范围完成线上 Notion 与仓库全部交付物：
  - **新增 3 篇 A 层背景文献（C5）**：下载并通读核对 `Kipf & Welling GCN (ICLR 2017)`、`Gilmer et al. MPNN (ICML 2017)`、`Neftci et al. Surrogate Gradient (IEEE SPM 2019)` 全文 PDF，按任务 01 的 13 字段固定格式补入 `literature/02-spiking-gnn.md` 与 `literature/03-vision-graph-backbones.md`，并同步写入 Notion `文献库`（总条目由 115 篇增至 **118 篇**）。
  - **数学主线第 1～4 章（A）与符号表初版（D.2）**：严格遵循 11 节固定结构与原文公式逐字符核对规范，在 Notion 总页面下上线《符号表（全课程统一记号）》（含第 1～13 章统一记号与 6 篇核心论文符号对照表）及《第 1 章 线性代数最小集》《第 2 章 神经网络的前向计算》（含 1D 卷积稀疏 Toeplitz 矩阵与 BatchNorm 推理期无损折叠 $\tilde{W},\tilde{\mathbf{b}}$ 推导）《第 3 章 训练：反向传播与脉冲困境》（含两层 ReLU 反向传播手算与 Heaviside 阶跃零导数死锁推导）《第 4 章 图与图神经网络》（含 Kipf-Welling 对称归一化 $\hat{A}=\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ 逐元素推导、验收标准第 1 条的 3 节点 2 维特征 $2\times 2$ 权重手算，以及 4 节点猫图块 GCN 与 Sum/Mean/Max 对比手算），并实时回拉导出到 `notion/export/符号表.md` 与 `notion/export/derivations/ch01`～`ch04`。
  - **配套可运行代码（B）**：仅使用 Python 3.10+、`numpy`、`matplotlib` 编写并完整执行保存输出 `notion/notebooks/ch01`～`ch04` 共 4 个 `.ipynb` 与 `notion/notebooks/README.md`，每个手算例子均经 `assert np.allclose` 校验一致，顶部附 Colab 一键运行链接。
  - **论文清单、下载脚本、许可证与 Notion 论文页全面改造（C1 + C2 + C3）**：
    - 新建 `literature/papers.csv`（118 篇，核实许可证与 A/B/C 分层：A 层 23 篇、B 层 35 篇、C 层 60 篇）及 `scripts/fetch_papers.py`、`scripts/README.md`，本机 `papers/` 自动下载 103 篇公开 PDF（已由 `.gitignore` 忽略，零 PDF 入库）。
    - Notion `文献库` 新增 `论文页`、`PDF`、`许可证`、`精读层级`、`中文全文`、`精读` 六列；为全部 118 篇论文创建带 C0 版权声明头的「中文全文」子页面；将全部 **86 篇 `≤ 5 MiB`** 的公开 PDF 上传并嵌入对应论文页顶部，17 篇超过 Notion 单文件 `5 MiB` 上限的公开 PDF 保留官方直链并在 PR #3 中完整列出；将已有通俗页 `00`～`09` 及新章节全部论文提及统一升级为 `短名（年份）[原文] [中文] [代码]`，并重新实时导出全部 18 个页面快照至 `notion/export/`。
- **未完成**：待提交 PR #3 由 Claude 审查合并后，再依次推进第 2～6 批（`gemini/deep-02`～`06`）。
- **注意 / 坑**：
  - Notion 当前工作区单文件上传硬上限为 **5 MiB**（实测上传 6.295 MiB 的 `ViG` PDF 返回 HTTP 400），故 17 篇 `> 5 MiB` 的论文按任务说明保留官方 PDF 直链并在 PR 说明中逐篇列出。
  - OpenReview 对脚本 `urllib` 请求启用了 Cloudflare 403 拦截（影响 `STA`、`Adaptive Fission`、`GraphPTQ` 三篇；其中 `Sigma-Delta` 已改用其官方 `arXiv:1611.02024` 预印本成功下载），AAAI OJS（`DRSGNN`、`P2SResLNet`）启用了 Anubis 反机器人验证网关，按安全准则不绕过反爬，保留官方链接供浏览器直接点击打开。
  - Notion CommonMark 解析器遇到紧贴中文引号的 `**“...”**` 时会把星号转义成字面量 `\*\*`，在中文引号外加粗时改用原生 `<b>“...”</b>` 即可避免。

### 2026-11-18 · claude · main（审查 PR #2，新增任务 04）
- **完成**：审查并合并 PR #2；新增 `tasks/04-deep-curriculum.md`；`.gitignore` 加入 `papers/`。
- **原因**：项目所有者读完 Notion 后反馈不够深，希望从第一性原理讲清数学，并能方便地找到每篇论文和中文材料。任务 02 的说明按"外行一屏读懂"设计，没有要求推导，所以另开任务 04 扩展，不推翻任务 02 的页面。
- **注意 / 坑**：任务 04 的论文部分：每篇论文的原文 PDF 和逐段对照的中文全文放在 Notion（不公开分享），不进本仓库。仓库只放论文清单、脚本和译文校对记录。

### 2026-11-17 · gemini · gemini/notion-presentation
- **完成**：按 `tasks/02-notion-presentation.md` 与 PR #1 审查提醒完成任务 02 全部 Notion 在线页面与仓库交付物：
  - **Notion 在线端**（总页面 `https://www.notion.so/41b0e3342e6f818f86b9d9a6cbc71968`，私有草稿页）：创建总页面及按顺序排列的 `0 一页读懂`～`11 文献库` 共 12 个子页面；在 `11 文献库` 下创建结构化数据库（数据源 `collection://41b0e334-2e6f-819d-b6a0-000b7413c20e`），将任务 01 的 120 条脉络记录去重合并写入全部 **115 篇论文条目**，正文全部通过 `<mention>` 链向数据库对应条目，并用绿/黄/灰三种 `<callout>` 严格区分事实、判断（含“与本方向的关系”及“论文自称”）与未知项。
  - **自制图表（F1–F9）**：在 `notion/figures/` 完成 4 张 Mermaid 图（F2、F4、F8、F9）、5 张静态 SVG 图（F1、F3、F5、F6、F7）及 4 个带暂停按钮与滑块的交互 HTML 页（F3、F5、F6、F7），全部通过官方文件/附件接口上传嵌入 Notion，零下载重传论文原图。
  - **仓库同步与自查**：通过 `notion-fetch` 实时回拉生成 `notion/export/`（`index.md` + `00`～`11` 共 13 个文件，含 115 条数据库快照），并完成 `notion/README.md`、`notion/figure-sources.md`、`notion/gaps.md`、`notion/self-check.md`（含独立子代理扮演外行读者试读第 0、1 页找出的 29 处理解障碍及修改记录）。
- **未完成**：待推送 `gemini/notion-presentation` 创建 PR #2 由 Claude 审查；任务 03（修订文献树 v2）待开始。
- **注意 / 坑**：
  - Notion Markdown 中裸写 `xxx.md` 会被自动解析成摩尔多瓦域名链接 `http://xxx.md`，写文件名时需加反引号包裹（已在第 7 页修正）。
  - `questions.md` Q9/Q10 中引用的若干最近邻量化与过估计偏置理论文献尚未在 `literature/01–05` 建立独立条目，已按规定如实记入 `notion/gaps.md`，未自行增补。
  - Claude 在 PR #1 标出的待复核项（PMSM 的 GCN 实验及 Bu 等、Yan 等、InkStream、NI-SGCN 四处发表处）已在第 3、11 页灰色未知块及 `notion/gaps.md` 中醒目提示。

### 2026-11-17 · claude · main（审查 PR #1）
- **完成**：审查并合并 PR #1。独立核实了 7 篇论文的出处页面和 3 个官方代码仓库里的具体行（DCGS、Spiking PointCNN、MobileViG），全部与记录吻合；在 PR 分支上直接修了三处小问题（提交 413222a）。详见 PR #1 的审查评论。
- **未完成**：任务 03（把文献树修订为 v2）还没做。
- **注意 / 坑**：
  - 120 条里只抽查了一部分，其余“全文”核对按 Gemini 的记录接受，未独立复现。
  - PMSM 的 GCN 实验、四篇论文的发表处（见 PR 评论）未能独立确认，引用前要复核。
  - 做任务 02 时，文献条目里带倾向的措辞要放进“判断”标注块，见 PR 评论末尾的三点提醒。

### 2026-11-16 · gemini · gemini/literature-01
- **完成**：任务 01 全部八个交付物，放在 `literature/`：
  - `01-ann2snn-conversion.md`（27 条）、`02-spiking-gnn.md`（29 条）、`03-vision-graph-backbones.md`（22 个模型的八列教师表 + 逐篇条目）、`04-event-driven-inference.md`（21 条，含 DynaGraph、Ingress 的核实）、`05-energy-and-hardware.md`（含 Horowitz 2014 第 14 页原表）。
  - `questions.md`：定向问题 1–11 逐条回答。
  - `audit-of-claude-v1.md`：草稿八张表共 56 行逐行判定，外加表格外的论断和漏掉的工作。
  - `search-log.md`：SL-01～SL-77。
- **主要发现**（详见 audit 文件开头）：草稿“没有图网络免训练转换”被 One-Spike SNN（IEEE TETC 2025）推翻；Spiking PointCNN 不是转换；`arXiv:2409.03368` 被误读为“max 池化改成神经元层”；“图上多跳扩散未解”说过头；AEGNN 200 倍与 11 倍两个版本数字冲突。
- **未完成 / 只核到摘要**：Adaptive Fission（OpenReview 反爬拦截）、Dampfhoffer 等（HAL 返回 500）、GraphPTQ（OpenReview 403）、Tianjic、DRA、EDA-GNN、Beyer 等 1999 只核对到摘要或定理陈述；STA 的被引列表是用 OpenAlex 全文检索近似得到的，完整性不确定；MSG 相关工作节那句话未逐句核对。
- **注意 / 坑**：
  - 早期下载的若干 arXiv 编号与论文不符（`1608.08404`、`2501.06640`、`2312.17499`、`2508.05743`、`2010.00175`），都已排除；复查时还更正了 01、02、05 中五个写错的标题（DCGS、Wang 等 AAAI 2026、并行转换、SpiCalib、SpikeGCL）和 ETHEREAL 的标题与发表处。之后补条目时请用 arXiv API 或 PDF 首页核对标题，不要凭检索摘要填写。
  - ETHEREAL 两份预印本都没有写 ESSERC 录用信息，目前只能记为 arXiv。
  - OpenAlex 的被引覆盖不全：One-Spike SNN、PMSM 都不在五篇被查论文的被引列表里，是另行检索到的。
  - DBLP 当天不可用，Crossref 偶发限流。
### 2026-11-16 · claude · main（初始提交）
- **完成**：初始化仓库和协作文档；放入文献树 v1；写好任务 01、02 的说明。
- **未完成**：任务 01、02、03 都还没开始。
- **注意 / 坑**：仓库创建时是空的，没有可供开 PR 的基线，所以这一次直接提交到了 `main`。之后所有改动都走分支和 PR。
