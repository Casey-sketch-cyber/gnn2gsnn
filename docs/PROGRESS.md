# 项目进度（交接记录）

> 每个 AI 结束工作前在最上方追加一条记录，新的在上面。

## 当前状态
任务 01、02 已完成并合并（PR #1、#2）。任务 04 第 1 批已合并（PR #3），可以开始第 2 批（第 5～7 章及 notebook、常见困惑页）。文献树 v1 的若干判断已被任务 01 推翻，待任务 03 修订为 v2。

## 待办
- [x] 任务 01：文献收集与核查（Gemini，PR #1 已合并）
- [x] 任务 02：Notion 通俗讲解（Gemini，PR #2 已合并）
- [ ] 任务 04：从第一性原理讲透，并配齐论文与中文精读（Gemini，分六批；第 1 批已合并，PR #3；下一批：第 2 批）
- [ ] 任务 03：Claude 审查并把文献树修订为 v2

## 已知问题
- 文献树 v1 没有通读任何论文全文；"未见图网络免训练转换"等结论只基于有限检索。
- 文献树 v1 的路线图在在线版里是一张图，仓库版改成了表格，内容相同。

---

## 工作记录

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
