# 9 Claude 的判断哪里对、哪里错

> Notion 页面：https://www.notion.so/41b0e3342e6f81cba505e4f774ccf728 （导出自 Notion 实时内容，最后编辑时间 `2026-11-21T03:01:18.982Z`）

<callout icon="📌" color="blue_bg">
<b>一句话结论</b>：Claude 草稿的 72 处论断里，43 处正确、18 处不准确、4 处错误、7 处无法核实；错的集中在“图网络从没被转换过”“最大值聚合不再是空白”“Spiking PointCNN 是转换”这几处，方向判断（动态选邻居是空白）站得住。
</callout>

<callout icon="💭" color="yellow_bg">
<b>说明</b>：Claude 的文献树 v1 是在没有通读论文全文的情况下写的，里面的结论都是“判断”，不是事实。下面的核查结果来自 [audit-of-claude-v1.md](https://github.com/Casey-sketch-cyber/gnn2gsnn/blob/main/literature/audit-of-claude-v1.md)，那里有每一行的证据。
</callout>

## 判定统计

| 判定 | 数量 | 含义 |
| --- | --- | --- |
| 正确 | 43 | 与原文一致 |
| 不准确 | 18 | 大体对，但有偏差（数字、发表处、说法过头） |
| 错误 | 4 | 与原文相反 |
| 无法核实 | 7 | 依赖项目内部实验或尚未做的测量 |

<i>表注：草稿八张表共 56 行，加表格外 16 处论断，共 72 处。</i>

## 四处错误

| 草稿说 | 实际情况 |
| --- | --- |
| 检索中没有找到把现成图网络免训练转成脉冲网络的工作 | One-Spike SNN 免训练转换了预训练的文本图网络，5 个数据集平均掉 0.90% <mention url="https://app.notion.com/p/41b0e3342e6f8142af44e1d41fa091ff">One-Spike SNN（2025）</mention> \[[原文](https://arxiv.org/abs/2403.08786)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81efadabda09415c2abe)\] |
| 视觉图任务只有骨架识别有人做 | 点云上有 Spiking PointNet 等多篇 <mention url="https://app.notion.com/p/41b0e3342e6f81da8fd4e977dc2fa215">Spiking PointNet（2023）</mention> \[[原文](https://arxiv.org/abs/2310.06232)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81a5922fc190b551cb6b)\] \[[代码](https://github.com/DayongRen/Spiking-PointNet)\]，SpikingGCN 做了 MNIST 超像素图 <mention url="https://app.notion.com/p/41b0e3342e6f8128a8dec0fa53d7ab03">SpikingGCN（2022）</mention> \[[原文](https://arxiv.org/abs/2205.02767)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81fd97e5c0cdbb609a33)\] \[[代码](https://github.com/ZulunZhu/SpikingGCN)\] |
| Spiking PointCNN 是点云转换的先例 | 它是从头训练的；真正的先例是 Lan 等（ICCV 2023）<mention url="https://app.notion.com/p/41b0e3342e6f81f29a81d3fb0e22e2ed">Spiking PointCNN（2024）</mention> \[[原文](https://www.mdpi.com/2079-9292/13/18/3626)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81e6a40feb926dfac5bc)\] \[[代码](https://github.com/DeadlyAbyss/Spiking-PointCNN)\] <mention url="https://app.notion.com/p/41b0e3342e6f81f6ab43c02a81f1e24c">Lan 等 3D/2D 转换 SNN（2023）</mention> \[[原文](https://openaccess.thecvf.com/content/ICCV2023/html/Lan_Efficient_Converted_Spiking_Neural_Network_for_3D_and_2D_Classification_ICCV_2023_paper.html)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81bdb0d1e3756ae543e5)\] |
| 最大池化已有多种解法（含“改成神经元层”），最大值聚合不再算空白 | Bu 等是把最大池化挪到神经元之前，不是改成神经元层；现有办法都不适用 ViG 的有符号差值 <mention url="https://app.notion.com/p/41b0e3342e6f8189b3dcdf43ac9f4e6e">Inference-Scale Conversion（2025）</mention> \[[原文](https://arxiv.org/abs/2409.03368)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81858a3fc2a999ed12b0)\] \[[代码](https://github.com/putshua/Inference-scale-ANN-SNN)\] |

## 值得注意的不准确

- <b>多跳扩散“未解”</b>：图上已有很多精确增量方法研究并缓解多跳扩散，缺的是视觉图上逐层阈值化的近似方法 <mention url="https://app.notion.com/p/41b0e3342e6f8150b1b1f1356365a7bf">InkStream（2025）</mention> \[[原文](https://arxiv.org/abs/2309.11071)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81e98129eaca94521868)\] \[[代码](https://github.com/WuDan0399/InkStream)\] <mention url="https://app.notion.com/p/41b0e3342e6f81748ed9d8b84b2d24e2">DAGr（2024）</mention> \[[原文](https://doi.org/10.1038/s41586-024-07409-w)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81ffb5c8e00fc33516ae)\] \[[代码](https://github.com/uzh-rpg/dagr)\]。
- <b>AEGNN“最多降 200 倍”</b>：这是 CVPR 原版的说法，arXiv 更新版改成“比最好的异步方法低 11 倍”，引用时要注明版本 <mention url="https://app.notion.com/p/41b0e3342e6f81d58665c55f7cb453c6">AEGNN（2022）</mention> \[[原文](https://arxiv.org/abs/2203.17149)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8191a64dd5931787449f)\] \[[代码](https://github.com/uzh-rpg/aegnn)\]。
- <b>注意力与归一化“Transformer 上已有解法”</b>：Transformer 转换仍靠浮点补偿或很长的时间步 <mention url="https://app.notion.com/p/41b0e3342e6f81e2a77bf2c3063d849f">SpikeZIP-TF（2024）</mention> \[[原文](https://arxiv.org/abs/2406.03470)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8161867ae5e8e17f9ce9)\] \[[代码](https://github.com/Intelligent-Computing-Research-Group/SpikeZIP-TF)\] <mention url="https://app.notion.com/p/41b0e3342e6f814f9595dcc2bb722d1c">STA（2024）</mention> \[[原文](https://openreview.net/forum?id=135eKq323G)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8161998bcb3a2b8280ff)\] \[[代码](https://github.com/ViviaHu/STA)\]。
- <b>ETHEREAL“仅见作者消息”</b>：论文已在 arXiv 公开；草稿写的 ESSERC 2026 在两份 PDF 里都没有出现 <mention url="https://app.notion.com/p/41b0e3342e6f81b78866fd3008d1ab55">ETHEREAL（2026）</mention> \[[原文](https://arxiv.org/abs/2608.17787)\] \[[中文](https://app.notion.com/p/41c0e3342e6f8167aab6d7b4b8b51a3e)\]。
- <b>同位数均匀量化当对照</b>：图网络低位宽下朴素量化会崩，应加入 TopGQ <mention url="https://app.notion.com/p/41b0e3342e6f81d59105ce3ec5d943ac">TopGQ（2026）</mention> \[[原文](https://arxiv.org/abs/2608.30394)\] \[[中文](https://app.notion.com/p/41c0e3342e6f81e0a649ca373b67cb00)\] \[[代码](https://github.com/meowrowan/TopGQ)\]。

## 草稿判断对的地方

<callout icon="✅" color="green_bg">
<b>核查确认</b>：ViG、DGCNN 的转换确实没找到（ViG 的 552 篇被引中也没有）；图网络上的公平能耗对比确实没找到；事件图芯片跑的确实不是脉冲网络；MobileViG 确实是固定图加取最大值（[questions.md Q2、Q3、Q7](https://github.com/Casey-sketch-cyber/gnn2gsnn/blob/main/literature/questions.md)）。
</callout>

## 审查时又发现的问题

<callout icon="✅" color="green_bg">
<b>事实</b>：Claude 审查任务 01 时，独立核对了 7 篇论文和 3 个代码仓库，全部与记录吻合，并修了三处小问题：MobileViG 的差值方向是“自身减邻居”、实现用切片拼接；PMSM 条目对应的是 arXiv 后续版本；One-Spike SNN 的“唯一”改为“本次检索范围内唯一”（见 [docs/PROGRESS.md](https://github.com/Casey-sketch-cyber/gnn2gsnn/blob/main/docs/PROGRESS.md) 2026-11-17 记录）。
</callout>

👉 <b>想看推导</b>：涉及最大值聚合与 Bu 等定理的数学核对见 <mention url="https://app.notion.com/p/41d0e3342e6f815698f9db048cdba5d9">第 9 章 非线性运算为什么难转换</mention>；动态 $k$-NN 翻转理论见 <mention url="https://app.notion.com/p/41d0e3342e6f81139bdec1e4296f2664">第 10 章 近似误差会不会让选邻居出错</mention>；多跳扩散与公平能耗对比见 <mention url="https://app.notion.com/p/41f0e3342e6f8135b55eda085c440a75">第 11 章 只算变化的部分</mention> 与 <mention url="https://app.notion.com/p/41f0e3342e6f81a6ac0bcac80292afa4">第 12 章 省电到底怎么算</mention>。

<b>三句话小结</b>

1. 草稿大部分正确，但四处错误都落在“别人做没做过”这类关键判断上。
2. 草稿最大的问题是没读全文：把 Spiking PointCNN 当转换、把 Bu 等的方法读错。
3. 草稿“动态选邻居是空白”的核心判断经核查成立。

<b>读完应该能回答的两个问题</b>

- 草稿“图网络从没被转换过”错在哪里？
- 为什么草稿说“最大值聚合不再算空白”站不住？
