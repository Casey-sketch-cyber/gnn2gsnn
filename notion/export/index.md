# 🐱 视觉图网络免训练转脉冲网络：通俗讲解

> Notion 页面：https://www.notion.so/41b0e3342e6f818f86b9d9a6cbc71968 （导出自 Notion 实时内容，最后编辑时间 `2026-11-17T16:21:48.297Z`）

<callout icon="📌" color="blue_bg">
这份讲解写给项目所有者：用一张猫的照片贯穿全篇，说明“把训练好的视觉图神经网络，不重新训练就变成省电的脉冲网络”这个方向在做什么、别人做到了哪一步、还空着什么。所有事实都来自仓库 <code>literature/</code> 下已核实的条目（任务 01，PR #1 已合并）。
</callout>

## 怎么读

- 先读“0 一页读懂”和“1 基础概念”，再按需要看后面的页面。
- 每页开头一句话说结论，结尾有“三句话小结”和“读完应该能回答的两个问题”。
- 每条事实后面的链接指向“11 文献库”里的对应论文。

## 三种标注块

<callout icon="✅" color="green_bg">
<b>已核实的事实</b>：来自论文原文或官方代码，并在文献库中有记录。
</callout>

<callout icon="💭" color="yellow_bg">
<b>判断</b>：论文作者、Claude 或文献核查得出的看法，不是定论。
</callout>

<callout icon="❓" color="gray_bg">
<b>未知</b>：还没有人研究，或需要做实验才能回答的问题。
</callout>

## 仓库

- 文献与核查：[https://github.com/Casey-sketch-cyber/gnn2gsnn/tree/main/literature](https://github.com/Casey-sketch-cyber/gnn2gsnn/tree/main/literature)
- 本讲解的导出与图源文件：仓库 <code>notion/</code> 目录（分支 <code>gemini/notion-presentation</code>）

## 页面

<page url="https://app.notion.com/p/41b0e3342e6f8100a67cd692f7be6d08">
0 一页读懂
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81d89aa3fad02e1a9faa">
1 基础概念
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81d9ad63c20ebe0b51b5">
2 时间线：转换技术
</page>

<page url="https://app.notion.com/p/41b0e3342e6f812caa0ec9ae9c741522">
3 时间线：脉冲图网络
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81d3b941f53e1b53937f">
4 时间线：视觉图模型
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81dcb2a2c3c138cfe0f7">
5 时间线：只算变化的部分
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81fd8f2af94f380e93da">
6 省电到底怎么算
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81c68e0ac192040b01d3">
7 难点地图
</page>

<page url="https://app.notion.com/p/41b0e3342e6f815cb595c1c6c712b79c">
8 可以做的论文
</page>

<page url="https://app.notion.com/p/41b0e3342e6f81cba505e4f774ccf728">
9 Claude 的判断哪里对、哪里错
</page>

<page url="https://app.notion.com/p/41b0e3342e6f811e8e69f0040d257997">
10 术语表
</page>

<page url="https://app.notion.com/p/41b0e3342e6f814a98b5c85f2ded4083">
11 文献库
</page>

<b>三句话小结</b>

1. 这组页面把“现成视觉图网络免训练转脉冲网络”拆成基础概念、四条时间线、省电账本、难点地图和候选选题。
2. 绿框是已核实事实，黄框是某一方的判断，灰框是尚待实验或复核的未知项。
3. 建议先读第 0、1 页建立直觉，再按关心的专题查阅第 2–11 页。

<b>读完应该能回答的两个问题</b>

- 页面里的绿、黄、灰三种标注块分别代表什么？
- 如果你想查某条事实的原始论文出处，应该点哪里？
