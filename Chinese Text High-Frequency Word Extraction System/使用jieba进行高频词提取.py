import os
import glob
import random
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re
import chardet

def find_chinese_font():
    candidates = []
    if sys.platform.startswith("win"):
        candidates = [
            r"C:\Windows\Fonts\msyh.ttc",
            r"C:\Windows\Fonts\simhei.ttf",
            r"C:\Windows\Fonts\simsun.ttc"
        ]
    elif sys.platform == "darwin":
        candidates = [
            "/System/Library/Fonts/STHeiti Medium.ttc",
            "/System/Library/Fonts/PingFang.ttc"
        ]
    else:
        candidates = [
            "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
            "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"
        ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None
font_path = find_chinese_font()
if not font_path:
    print("未检测到中文字体，请手动修改 font_path 参数。")
else:
print(f"检测到中文字体：{font_path}")

def get_content(path):
    with open(path, 'rb') as f:
        raw = f.read()
        enc = chardet.detect(raw)['encoding'] or 'utf-8'
        if enc.lower() in ['gb2312','gb18030']:
            enc = 'gbk'
    return raw.decode(enc, errors='ignore')

def clean_html(text):
    text = re.sub(r"&nbsp;|&gt;|&lt;|&amp;", "", text)
    text = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fa5]", " ", text)
    return text

def stop_words(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return [l.strip() for l in f if l.strip()]

def tokenize(text, stop_list=[]):
    return [w for w in jieba.lcut(text) if w.strip() and w not in stop_list]

def export_top_words(freq_dict, title, topK=10, save_path=None):
    top_list = freq_dict.most_common(topK)
    df = pd.DataFrame(top_list, columns=['词语','词频'])
    print(f"\n {title} Top{topK} 高频词表：")
    print(df.to_string(index=False))
    if save_path:
        df.to_excel(save_path, index=False)
        print(f"已保存 Excel 表格：{save_path}")
    return df

def generate_wordcloud(freq_dict, save_path, title, font_path):
    if not freq_dict:
        print(f"词频为空：{title}")
        return
    wc = WordCloud(
        font_path=font_path,
        background_color="white",
        width=800,
        height=600,
        max_words=200,
 collocations=False,
        colormap="rainbow" 
 ).generate_from_frequencies(freq_dict)
    wc.to_file(save_path)
    print(f"已保存词云：{save_path}")

    plt.figure(figsize=(10,8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.show()

data_dir = r"C:\Users\zheng\Desktop\作业1（词法分析实践）\作业1（词法分析实践）\题目1--使用jieba进行高频词提取\data"
output_dir = r"C:\Users\zheng\Desktop\作业1（词法分析实践）\output"
os.makedirs(output_dir, exist_ok=True)

stop_list = stop_words(os.path.join(data_dir,"stop_words.utf8"))
files = glob.glob(os.path.join(data_dir,"*.txt"))

if not files:
    print("没有找到任何 .txt 文件，请检查路径或文件")
else:
    sample_file = random.choice(files)
    sample_text = clean_html(get_content(sample_file))
    sample_words = tokenize(sample_text, stop_list)
    sample_freq = Counter(sample_words)

    all_text = "\n".join([clean_html(get_content(f)) for f in files])
    all_words = tokenize(all_text, stop_list)
    all_freq = Counter(all_words)

    export_top_words(sample_freq, f"样本《{os.path.basename(sample_file)}》", save_path=os.path.join(output_dir,"top10_sample.xlsx"))
    export_top_words(all_freq, "全部语料（合并）", save_path=os.path.join(output_dir,"top10_all.xlsx"))

    generate_wordcloud(sample_freq, os.path.join(output_dir,"wordcloud_sample.png"),
                       f"样本词云：{os.path.basename(sample_file)}", font_path=font_path)
    generate_wordcloud(all_freq, os.path.join(output_dir,"wordcloud_all.png"),
                       "全部语料词云（合并）", font_path=font_path)

    print(f"\n 输出目录：{os.path.abspath(output_dir)}")