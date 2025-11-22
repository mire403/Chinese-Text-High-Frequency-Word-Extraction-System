# Chinese Text High-Frequency Word Extraction System （中文高频词提取系统）

本项目用于对中文文本进行分词、词频统计与可视化展示。  
系统基于 `jieba` 中文分词库，能够自动检测中文字体、批量读取文本文件、清洗内容、统计高频词，并生成词云图与 Excel 词频表。

---

## 🚀 项目简介

本系统实现了以下功能：
- 批量读取文本文件，自动检测编码格式；
- 使用 **jieba** 进行中文分词；
- 过滤 HTML 符号、停用词等无效信息；
- 统计词频并输出 Excel 表格；
- 自动生成样本文本与全部文本的词云图；
- 兼容 Windows / macOS / Linux 系统中文字体自动识别。

---

## 🧩 环境要求

| 环境 | 版本要求 |
|------|-----------|
| Python | 3.8 及以上 |
| 依赖库 | jieba, wordcloud, matplotlib, pandas, chardet |

安装依赖：
```bash
pip install jieba wordcloud matplotlib pandas chardet
```

## 🛠️ 运行方法
将所有待分析的文本文件放入 data/ 文件夹中。

可选：在 data/ 文件夹中放置 stop_words.utf8 作为停用词表。

修改脚本中的以下路径：

```bash
data_dir = r"你的数据目录"
output_dir = r"输出目录"
```

运行主程序：

```bash
python word_analysis.py
```

程序会输出：

高频词 Excel 文件（Top10 词频表）

样本文本与合并语料的词云图

控制台打印词频结果与输出路径

## 📊 效果展示
示例输出：

✅ 高频词表：

| 词语 | 词频 |
|------|-----------|
| 学习 | 52 |
| 数据 | 47 |

✅ 词云图


## 📁 输出文件说明

| 文件名 | 内容 |
|------|-----------|
| top10_sample.xlsx | 单个样本文本的高频词统计 |
| top10_all.xlsx | 所有文本合并后的高频词统计 |
| wordcloud_sample.png | 样本文本词云图 |
| wordcloud_all.png | 合并文本词云图 |

## ⭐ Star Support

如果你觉得这个项目对你有帮助，请给仓库点一个 ⭐ Star！
你的鼓励是我继续优化此项目的最大动力 😊
