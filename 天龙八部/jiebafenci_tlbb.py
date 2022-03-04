################################
# 把天龙八部用jieba分词，并写入文件#
################################
import jieba
import gensim

# 定义阻止词库
STOPWORDS = []

with open("HIT.txt", "r") as fp:
    STOPWORDS.extend(i.strip() for i in fp.readlines())
with open("stop.txt", "r") as fp:
    STOPWORDS.extend(i.strip() for i in fp.readlines())
with open("name.txt", "r") as f_name:
    special_names = [name.strip() for name in f_name.readlines()]
    for i in special_names:
        jieba.add_word(i)
with open("tlbb.txt", "rb") as fp:
    fsort = open("words_list.txt", "w", encoding='utf-8')
    # 按照行来统计
    sentence = []
    for line in fp.readlines():
        clean_line = line.strip()
        # 每行都做一个jieba的分词，这里用默认模式，也就是精准分词
        word_list = jieba.cut(clean_line)
        # 对于分的词，如果不在STOPWORDS里，就写入文件
        unique_list = []
        for word in word_list:
            if word not in STOPWORDS:
                fsort.writelines(str(word) + '\n')
                unique_list.append(word)
        sentence.append(unique_list)
    print('开始训练模型。。。这个时间很长，去喝杯咖啡吧')
    model = gensim.models.Word2Vec(
        sentence, size=300, min_count=20, workers=8)
    print('训练完毕。正在将模型保存到本地')
    model.save('天龙八部.model')
    print('Okey ')
fsort.close()

print("jieba cut is finished\n")
