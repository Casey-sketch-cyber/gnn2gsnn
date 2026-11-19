# 配套可运行代码（Notebooks）

本目录存放任务 04“从零推导”数学主线各章配套的 Jupyter Notebook。设计原则：**只使用 Python 标准库、NumPy 与 Matplotlib，不依赖 GPU 或 PyTorch/TensorFlow 等深度学习框架**，把每一个矩阵乘法、形状变换与手算中间数摊开在明处。所有 Notebook 在提交前均已完整执行并保留输出结果，不运行也可直接在 GitHub 中查看数值与图表。

## 环境要求与本地运行方法

- **Python 版本**：Python 3.10 及以上
- **依赖包**：`numpy`、`matplotlib`、`jupyter`（或 `nbclient`）

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\pip install numpy matplotlib jupyter
.\.venv\Scripts\jupyter notebook notion/notebooks/
```

也可以直接点击每个 Notebook 顶部的 **Open in Colab** 徽章在浏览器中零配置运行。

## 章节对应清单（当前进度：第 3 批，第 1～10 章）

| 章节 | Notebook 文件 | 核心验证内容 | Colab 直达 |
| --- | --- | --- | --- |
| 第 1 章 线性代数最小集 | [`ch01_linear_algebra.ipynb`](ch01_linear_algebra.ipynb) | 逐元素矩阵乘 $C_{ij}=\sum_k A_{ik}B_{kj}$ 手算核对；线性/仿射/ReLU 对比；脉冲序列时间平均与权重乘法可交换性验证及 `max` 反例 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch01_linear_algebra.ipynb) |
| 第 2 章 神经网络的前向计算 | [`ch02_nn_forward_and_bn_folding.ipynb`](ch02_nn_forward_and_bn_folding.ipynb) | 两层纯线性退化为单层；批量行向量矩阵形式 $XW^\top+\mathbf{b}$；1D 卷积转共享权重稀疏矩阵；批归一化（BatchNorm）推理期无损折叠进 $\tilde{W},\tilde{\mathbf{b}}$ | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch02_nn_forward_and_bn_folding.ipynb) |
| 第 3 章 训练（反向传播与脉冲困境） | [`ch03_backprop_and_step_derivative.ipynb`](ch03_backprop_and_step_derivative.ipynb) | 两层 ReLU 网络前向+反向链式法则手算核对与中心差分检验；Heaviside 阶跃导数处处为 0 阻断梯度演示与替代梯度（Surrogate Derivative）曲线对比 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch03_backprop_and_step_derivative.ipynb) |
| 第 4 章 图与图神经网络 | [`ch04_graphs_and_gnn.ipynb`](ch04_graphs_and_gnn.ipynb) | 3 节点 2 维特征 $2\times 2$ 权重 GCN 完整手算复现（验收标准第 1 条）；4 节点图 GCN 对称归一化与 MPNN 求和/平均/最大值聚合对比；特征值谱稳定实验 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch04_graphs_and_gnn.ipynb) |
| 第 5 章 视觉图网络 | [`ch05_vision_gnn.ipynb`](ch05_vision_gnn.ipynb) | 图像切块矩阵乘与步幅卷积恒等性；两两平方距离矩阵公式 $D=\mathbf{q}\mathbf{1}^\top+\mathbf{1}\mathbf{q}^\top-2XX^\top$；ViG `max-relative` 有符号差值手算复现与 DGCNN / MobileViG / ST-GCN 对照 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch05_vision_gnn.ipynb) |
| 第 6 章 脉冲神经元 | [`ch06_spiking_neurons.ipynb`](ch06_spiking_neurons.ipynb) | 置零复位 vs 减法复位两张 10 步对照表；$z=0.3,\theta=1,T=10$ 核心手算表（验收标准第 2 条）及 Python `float64` 第 10 步 `0.9999999999999998` 漏脉冲现象与 `1e-9` 容差修正；IF vs LIF 死区演示 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch06_spiking_neurons.ipynb) |
| 第 7 章 核心：为什么发放率约等于 ReLU | [`ch07_ann2snn_rate_and_errors.ipynb`](ch07_ann2snn_rate_and_errors.ipynb) | 裂项求和恒等式验证；$v[0]=\theta/2$ 半阈值修正与 QCFS 定理 1–2 验证；线性复制权重原理与 `max`/乘法反例（验收标准第 4 条）；截断/量化/到达不均匀三种误差手算核对（验收标准第 3 条）；99.9% 分位数阈值与权重缩放等价性；两层网络 $T=4,8,16,32$ 端到端并排对照 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch07_ann2snn_rate_and_errors.ipynb) |
| 第 8 章 带符号、多阈值和差分编码 | [`ch08_signed_multithreshold_diff.ipynb`](ch08_signed_multithreshold_diff.ipynb) | 带符号 IF 撤回误发脉冲与编码负激活；DCGS $2n$ 级多阈值（Eq. 1–6 / Appendix P 位运算）与差分编码全套方程（Definition 4.1 & Theorems 4.2–4.5，含核出原文式 19 笔误）手算复现；复现 DCGS 图 2 及 $T=1\sim 32$ 误差/脉冲数基准（验收标准第 7 条 DCGS 部分） | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch08_signed_multithreshold_diff.ipynb) |
| 第 9 章 非线性运算为什么难转换 | [`ch09_nonlinear_operators.ipynb`](ch09_nonlinear_operators.ipynb) | 逐步 `max` 反例（`1010` vs `0101`）与均匀噪声最大化正偏置 $\frac{k-1}{k+1}\epsilon$ 仿真；Bu 等 Theorem 2 交换律验证、SNN 时域条件反例及 ViG 失效算例；双脉冲流乘法错相/同相反例与增量乘积恒等式；GELU / Softmax / LayerNorm 非交换性反例 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch09_nonlinear_operators.ipynb) |
| 第 10 章 近似误差会不会让选邻居出错 | [`ch10_knn_stability.ipynb`](ch10_knn_stability.ipynb) | 三角不等式 $2\varepsilon$ 距离扰动界与取等验证；$4\varepsilon$ 邻居不变定理手算与翻转演示（验收标准第 5 条，附紧界构造）；$\varepsilon(T)$ 换算到向量范数并在 $N=49, C=32, k=9$ 模拟视觉图上实测 IF / 半阈值 IF / DCGS 的 $k$-NN 边翻转率曲线 | [Open in Colab](https://colab.research.google.com/github/Casey-sketch-cyber/gnn2gsnn/blob/main/notion/notebooks/ch10_knn_stability.ipynb) |
