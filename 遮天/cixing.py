import jieba
import jieba.posseg as ps

# 定义阻止词库
STOPWORDS = []

with open("name.txt", "r") as f_name:
    STOPWORDS.extend(i.strip() for i in f_name.readlines())
with open("zt.txt", "rb") as fp:
    fsort = open("words_list_3.txt", "w", encoding='utf-8')
    # 按照行来统计
    for line in fp.readlines():
        clean_line = line.strip()
        # 每行都做一个jieba的分词，这里用默认模式，也就是精准分词
        word_list = ps.cut(clean_line)
            # 对于分的词，如果不在STOPWORDS里，就写入文件
        for word in word_list:
            if word not in STOPWORDS:
                            # 这里写入的方式是在词与词性间添加了一个空格，便于后续读取
                fsort.writelines(f'{str(word.word)} {str(word.flag)}' + '\n')
fsort.close()

print("jieba cut is finished\n")