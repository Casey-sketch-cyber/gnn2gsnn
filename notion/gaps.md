# literature/ 缺的内容

做任务 02 时发现的、`literature/` 里没有或不完整的内容。按任务 02 的要求，这里只记录，没有自己补。

| # | 缺什么 | 在讲解哪里需要 | 现状 | 建议 |
| --- | --- | --- | --- | --- |
| 1 | RaBitQ（SIGMOD 2024）、ScaNN（ICML 2020）、Vecchiato & Bruch（2026）、Beyer 等（ICDT 1999）、KNN-Defense（2025）没有独立的文献条目 | 第 7 页“动态选邻居为什么可能出错” | 只在 `questions.md` Q9 里核对过，讲解里只能链接到 Q9，不能链接到文献库 | 补成脉络五或新增“理论工具”脉络的条目 |
| 2 | Thrun & Schwartz（1993）、van Hasselt（2010，Double Q-learning）、Self-correcting Q-Learning（2021）没有独立条目 | 第 7 页“取最大值的误差” | 只在 `questions.md` Q10 里引用，前两篇是通过第三篇交叉核对的 | 同上；前两篇原文未直接打开，补条目时需读原文 |
| 3 | ST-GCN 等骨架模型逐层帧间差分的稀疏度没有任何数据 | 第 5、8 页 | 文献中未找到测量（audit 判据 H2） | 这是实验问题，不是文献问题；可在失效普查中测量 |
| 4 | 真实 ViG / DGCNN 每层“第 k 近与第 k+1 近的距离间隔”分布 | 第 7、8 页 | 文献中未找到 | 同上，属于实验问题 |
| 5 | 彭思达 learning_research 文档里“四种情况”的准确定义 | 第 8 页 | 草稿引用了，但任务 01 没有核对原文档（audit 第六节第 6 行判为“无法核实”） | 打开原文档，把四种情况的定义抄进 `literature/` |
| 6 | Claude 审查时未能独立确认的发表处：Bu 等（2409.03368）CVPR 2025、Yan 等 IEEE TCAD 2026、InkStream IPDPS 2025、NI-SGCN AAAI 2025；以及 PMSM 的 GCN 实验 | 第 2、3、5、6 页及文献库 | 任务 01 记录为已核对，Claude 未复现 | 引用前从会议官网或 DOI 页面复核 |
| 7 | Horowitz 2014 表格的页码与图号 | 第 6 页 | 任务 01 记录为原文第 14 页 Figure 1.1.9；Claude 审查时核对了数值，但没有打开原文核对页码 | 下次核对时顺带确认 |
| 8 | 引用列表里出现但未读全文的增量推理相关工作：*Incrementally-Computable Neural Networks*（2023）、*Pushing the Limits of Asynchronous Graph-based Object Detection with Event Cameras*（2022） | 第 5 页 | 只在检索结果里见过（search-log SL-60、SL-63），未写入脉络四 | 读全文后决定是否补入脉络四 |
