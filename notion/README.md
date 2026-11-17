# Notion 通俗讲解（任务 02 交付物）

本目录同步了在 Notion 上为项目所有者制作的《视觉图网络免训练转脉冲网络：通俗讲解》全部内容、图源文件、来源说明、文献缺口记录与自查清单。讲解中的所有事实均严格来自仓库 `literature/` 下已核实并合并入 `main` 的条目（PR #1）。

## Notion 在线访问方式

- **总页面标题**：🐱 视觉图网络免训练转脉冲网络：通俗讲解
- **总页面链接**：https://www.notion.so/41b0e3342e6f818f86b9d9a6cbc71968 （或工作区直达链接：https://app.notion.com/p/41b0e3342e6f818f86b9d9a6cbc71968 ）
- **所在工作区**：`维 杜的 Notion`
- **权限说明**：按 Notion 官方集成规范，总页面以**私有草稿页（Private Draft）**方式直接创建在项目所有者本人的工作区根部，项目所有者登录后在左侧栏“私人页面（Private）”即可直接打开阅读和拖动交互图表；如需分享给其他人或移入指定团队空间，由项目所有者本人在 Notion 右上角“分享（Share）/ 移动到（Move to）”中自行设置。
- **离线审阅方式**：若审阅方（如 Claude）无法登录该 Notion 工作区，可直接阅读 [`export/`](export/) 下从 Notion 实时导出的全部页面 Markdown（含第 11 页数据库的全部 115 条记录快照），并用浏览器打开 [`figures/`](figures/) 下的 `.svg` / `.html` 图文件。

## 页面清单（与 Notion 顺序一一对应）

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
| 11 | 文献库（含 Notion 数据库） | https://www.notion.so/41b0e3342e6f814a98b5c85f2ded4083 （数据库：https://www.notion.so/41b0e3342e6f815fbac2e645330b5177 ） | [`export/11-文献库.md`](export/11-文献库.md) | — |

## 目录文件说明

- [`README.md`](README.md)：本说明文件。
- [`export/`](export/)：从 Notion 实时抓取导出的总页面与 0–11 子页面 Markdown（共 13 个文件）。
- [`figures/`](figures/)：9 张自制图表的全部源码（4 个 `.mmd` Mermaid 文件、5 个 `.svg` 静态矢量图、4 个带暂停与滑块的 `.html` 交互页，共 13 个文件）。
- [`figure-sources.md`](figure-sources.md)：每张图的来源、所在页、制作方式与示意图数据说明。
- [`gaps.md`](gaps.md)：制作讲解时发现 `literature/` 中缺少独立条目或尚待实验测量的内容记录。
- [`self-check.md`](self-check.md)：对照 `tasks/02-notion-presentation.md` 九项自查清单逐项核对的记录（含外行读者试读与修改记录）。
