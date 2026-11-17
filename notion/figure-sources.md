# 图的来源

任务 02 要求的九张图全部是自己画的，没有下载或重新上传任何论文图片。示意图里的数字都是为说明而编的，已在图上和图注里标“示意，非真实数据”；凡是引用论文结论的地方，都在图注里写明出处。

| 编号 | 图 | 放在哪一页 | 源文件 | 形式 | 来源与说明 |
| --- | --- | --- | --- | --- | --- |
| F1 | 一张图片怎么变成一张“图” | 1 基础概念 | [f1-image-to-graph.svg](figures/f1-image-to-graph.svg) | 静态 SVG | 自己画。切块数、连线是示意，不是任何模型的真实建图结果。 |
| F2 | 图网络的一次信息传递 | 1 基础概念 | [f2-message-passing.mmd](figures/f2-message-passing.mmd) | Mermaid | 自己画。特征数值是示意。 |
| F3 | 普通神经元和脉冲神经元的区别 | 1 基础概念 | [f3-neuron-vs-spiking.html](figures/f3-neuron-vs-spiking.html)（交互，可暂停）+ [f3-neuron-vs-spiking.svg](figures/f3-neuron-vs-spiking.svg)（静态） | 动画 + 静态图 | 自己画。阈值 1、减法复位的积分—发放神经元，输入 0.3 时 10 步发 3 次，是按规则算出的示意。 |
| F4 | “转换”是什么 | 1 基础概念 | [f4-conversion.mmd](figures/f4-conversion.mmd) | Mermaid | 自己画。数值是示意。 |
| F5 | 时间步多少的影响 | 2 时间线：转换技术 | [f5-timesteps.html](figures/f5-timesteps.html)（交互，可暂停）+ [f5-timesteps.svg](figures/f5-timesteps.svg)（静态） | 交互 + 静态图 | 自己画。目标值 0.37，按减法复位规则算出各 T 下的发放次数与误差，是示意。 |
| F6 | 动态选邻居为什么可能出错 | 7 难点地图 | [f6-knn-flip.html](figures/f6-knn-flip.html)（交互，可暂停）+ [f6-knn-flip.svg](figures/f6-knn-flip.svg)（静态） | 交互 + 静态图 | 自己画。距离数值是示意；“间隔大于 4ε 时邻居不变”的条件来自 `literature/questions.md` Q9。 |
| F7 | 视频里只算变化的部分 | 5 时间线：只算变化的部分 | [f7-video-delta.html](figures/f7-video-delta.html)（动画，可暂停）+ [f7-video-delta.svg](figures/f7-video-delta.svg)（静态） | 动画 + 静态图 | 自己画。画面是示意；“一个像素经三层 3×3 卷积扩散到 49 个像素”来自 DeltaCNN（CVPR 2022）第 3.3 节，见 `literature/04-event-driven-inference.md`。 |
| F8 | 三条时间线 | 2 时间线：转换技术 | [f8-timelines.mmd](figures/f8-timelines.mmd) | Mermaid | 自己画。里程碑与结论来自 `literature/01`、`02`、`04` 的条目与演化小结。 |
| F9 | 难点地图 | 7 难点地图 | [f9-difficulty-map.mmd](figures/f9-difficulty-map.mmd) | Mermaid | 自己画。分组依据 `literature/audit-of-claude-v1.md` 难点树的核查结果。 |

## 上传方式

- SVG 静态图通过 Notion 官方集成的文件上传接口（`notion-create-file-upload`）上传，HTML 交互页通过附件接口（`notion-create-attachment`）上传到本页面所在的工作区，Notion 里分别以图片块（`<image>`）和嵌入块（`<embed>`）显示。
- Mermaid 图在 Notion 里用 `mermaid` 代码块，由 Notion 渲染。
- 交互页在 Notion 中以沙盒嵌入显示；如果嵌入不显示，可以在仓库里直接用浏览器打开对应的 `.html` 文件，静态 SVG 的内容与交互页一致。
