# Notion 通俗讲解与第一性原理推导（任务 02 + 任务 04 交付物）

本目录同步了在 Notion 上为项目所有者制作的《视觉图网络免训练转脉冲网络》全部通俗讲解页（任务 02）与第一性原理数学推导主线、配套可运行 Notebook（任务 04，分六批更新，当前已上线**第 1 批**）。所有事实均严格来自仓库 `literature/` 下已核实的条目，来自论文的公式均与原文逐字符核对，自推导补全步骤均标明“推导（非论文原文）”并经 Notebook 数值验证。

## Notion 在线访问方式

- **总页面标题**：🐱 视觉图网络免训练转脉冲网络：通俗讲解
- **总页面链接**：https://www.notion.so/41b0e3342e6f818f86b9d9a6cbc71968 （或工作区直达链接：https://app.notion.com/p/41b0e3342e6f818f86b9d9a6cbc71968 ）
- **所在工作区**：`维 杜的 Notion`
- **权限与版权说明（C0）**：总页面及全部论文子页面均为**不公开分享的私有页面（Private）**，仅供项目所有者个人学习阅读；原文 PDF（共 86 篇 `≤ 5 MiB` 已直接上传嵌入对应论文页顶部）与逐段中文全文仅保存在 Notion 私有页面与本机 `.gitignore` 忽略的 `papers/` 目录中，**绝不提交进 GitHub 仓库**。
- **离线审阅方式**：审阅方（如 Claude）可直接阅读 [`export/`](export/) 与 [`export/derivations/`](export/derivations/) 下从 Notion 实时导出的全部 Markdown（含第 11 页数据库的全部 **118 条**记录快照），查看 [`notebooks/`](notebooks/) 下保留了完整运行输出与图表的 Jupyter Notebooks，并用浏览器打开 [`figures/`](figures/) 下的 `.svg` / `.html` 图文件。

## 页面清单（与 Notion 顺序一一对应）

### 一、通俗讲解组（任务 02，全页论文引用已按 C1 升级为 `短名（年份）[原文] [中文] [代码]`）

| 顺序 | Notion 页面标题 | Notion 链接 | 仓库导出文件 | 包含的自制图 |
| --- | --- | --- | --- | --- |
| 总页 | 🐱 视觉图网络免训练转脉冲网络：通俗讲解 | https://www.notion.so/41b0e3342e6f818f86b9d9a6cbc71968 | [`export/index.md`](export/index.md) | — |
| 0 | 0 一页读懂 | https://www.notion.so/41b0e3342e6f8100a67cd692f7be6d08 | [`export/00-一页读懂.md`](export/00-一页读懂.md) | — |
| 1 | 1 基础概念 | https://www.notion.so/41b0e3342e6f81d89aa3fad02e1a9faa | [`export/01-基础概念.md`](export/01-基础概念.md) | F1、F2、F3（交互+静态）、F4 |
| 2 | 时间线：转换技术 | https://www.notion.so/41b0e3342e6f81d9ad63c20ebe0b51b5 | [`export/02-时间线-转换技术.md`](export/02-时间线-转换技术.md) | F8、F5（交互+静态） |
| 3 | 时间线：脉冲图网络 | https://www.notion.so/41b0e3342e6f812caa0ec9ae9c741522 | [`export/03-时间线-脉冲图网络.md`](export/03-时间线-脉冲图网络.md) | — |
| 4 | 时间线：视觉图模型 | https://www.notion.so/41b0e3342e6f81d3b941f53e1b53937f | [`export/04-时间线-视觉图模型.md`](export/04-时间线-视觉图模型.md) | — |
| 5 | 时间线：只算变化的部分 | https://www.notion.so/41b0e3342e6f81dcb2a2c3c138cfe0f7 | [`export/05-时间线-只算变化的部分.md`](export/05-时间线-只算变化的部分.md) | F7（交互+静态） |
| 6 | 省电到底怎么算 | https://www.notion.so/41b0e3342e6f81fd8f2af94f380e93da | [`export/06-省电到底怎么算.md`](export/06-省电到底怎么算.md) | — |
| 7 | 难点地图 | https://www.notion.so/41b0e3342e6f81c68e0ac192040b01d3 | [`export/07-难点地图.md`](export/07-难点地图.md) | F9、F6（交互+静态） |
| 8 | 可以做的论文 | https://www.notion.so/41b0e3342e6f815cb595c1c6c712b79c | [`export/08-可以做的论文.md`](export/08-可以做的论文.md) | — |
| 9 | Claude 的判断哪里对、哪里错 | https://www.notion.so/41b0e3342e6f81cba505e4f774ccf728 | [`export/09-Claude的判断哪里对哪里错.md`](export/09-Claude的判断哪里对哪里错.md) | — |
| 10 | 术语表 | https://www.notion.so/41b0e3342e6f811e8e69f0040d257997 | [`export/10-术语表.md`](export/10-术语表.md) | — |
| 11 | 文献库（118 篇数据库，含内嵌 PDF 与中文全文子页面） | https://www.notion.so/41b0e3342e6f814a98b5c85f2ded4083 （数据库：https://www.notion.so/41b0e3342e6f815fbac2e645330b5177 ） | [`export/11-文献库.md`](export/11-文献库.md) | — |

### 二、从零推导：第一性原理数学主线与辅助页（任务 04，第 1 批已上线）

| 章节 / 页面 | Notion 链接 | 仓库导出文件 | 配套可运行 Notebook |
| --- | --- | --- | --- |
| 📐 符号表（全课程统一记号） | https://www.notion.so/41c0e3342e6f81b58fb2e4fd6fdbc8c7 | [`export/符号表.md`](export/符号表.md) | — |
| 1️⃣ 第 1 章 线性代数最小集 | https://www.notion.so/41c0e3342e6f8102aeb4d13255acb166 | [`export/derivations/ch01-线性代数最小集.md`](export/derivations/ch01-线性代数最小集.md) | [`notebooks/ch01_linear_algebra.ipynb`](notebooks/ch01_linear_algebra.ipynb) |
| 2️⃣ 第 2 章 神经网络的前向计算 | https://www.notion.so/41c0e3342e6f8156afa8d6260fe476ce | [`export/derivations/ch02-神经网络的前向计算.md`](export/derivations/ch02-神经网络的前向计算.md) | [`notebooks/ch02_nn_forward_and_bn_folding.ipynb`](notebooks/ch02_nn_forward_and_bn_folding.ipynb) |
| 3️⃣ 第 3 章 训练：反向传播与脉冲困境 | https://www.notion.so/41c0e3342e6f816db904cb868ade3e5c | [`export/derivations/ch03-训练-反向传播与脉冲困境.md`](export/derivations/ch03-训练-反向传播与脉冲困境.md) | [`notebooks/ch03_backprop_and_step_derivative.ipynb`](notebooks/ch03_backprop_and_step_derivative.ipynb) |
| 4️⃣ 第 4 章 图与图神经网络 | https://www.notion.so/41c0e3342e6f8167aff7f5ea10295347 | [`export/derivations/ch04-图与图神经网络.md`](export/derivations/ch04-图与图神经网络.md) | [`notebooks/ch04_graphs_and_gnn.ipynb`](notebooks/ch04_graphs_and_gnn.ipynb) |

## 目录文件说明

- [`README.md`](README.md)：本说明文件。
- [`export/`](export/)：从 Notion 实时抓取导出的总页面、`0`～`11` 通俗页、`符号表.md` 及 [`export/derivations/`](export/derivations/) 下的第 1～4 章推导 Markdown（共 18 个文件）。
- [`notebooks/`](notebooks/)：仅用 Python 3.10+、NumPy、Matplotlib 编写并完整运行保留输出的第 1～4 章配套 Notebook 及环境说明 [`notebooks/README.md`](notebooks/README.md)。
- [`figures/`](figures/)：9 张自制图表的全部源码（4 个 `.mmd` Mermaid 文件、5 个 `.svg` 静态矢量图、4 个带暂停与滑块的 `.html` 交互页，共 13 个文件）。
- [`figure-sources.md`](figure-sources.md)：每张图的来源、所在页、制作方式与示意图数据说明。
- [`gaps.md`](gaps.md)：制作讲解时发现 `literature/` 中缺少独立条目或尚待实验测量的内容记录。
- [`self-check.md`](self-check.md)：任务 02 九项自查清单核对记录。
