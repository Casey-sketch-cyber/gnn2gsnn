# 脚本说明（`scripts/`）

本目录存放文献拉取与校对辅助脚本，仅使用 Python 3.10+ 标准库，无需额外安装第三方依赖。

## 1. 批量下载论文 PDF：`fetch_papers.py`

读取 [`../literature/papers.csv`](../literature/papers.csv)，把所有带有公开官方 PDF 地址（arXiv、CVF Open Access、OpenReview、PMLR、JMLR、VLDB、AAAI、NeurIPS、Frontiers 等）的论文自动下载到仓库根目录下的 `papers/` 文件夹，按 `<年份>-<短名>.pdf` 命名。

> **注意**：`papers/` 与 `*.pdf` 已写入根目录 `.gitignore`，下载的 PDF 仅保存在本机或上传至不公开分享的私人 Notion 页面，**绝不提交进 Git 仓库**。

### 运行方式

在仓库根目录执行：

```bash
# 下载全部层级的公开论文（已下载过的文件会自动跳过）
python scripts/fetch_papers.py

# 只下载 A 层核心精读论文
python scripts/fetch_papers.py --tier A

# 调整并发数或超时时间
python scripts/fetch_papers.py --workers 4 --timeout 120
```

运行结束后，终端会打印四类统计：**新下载成功**、**已存在跳过**、**需机构访问**（付费期刊/会议论文，列出 DOI 供手动补齐）与**下载失败**。
