import gensim

# 读入训练好的模型
model = gensim.models.Word2Vec.load('天龙八部.model')

# 检索名字
name_list = []
with open("name_list.txt", "r") as fp:
    for i in fp.readlines():
        word = i.strip()
        name_list.append(word)
with open("人物关系.txt", "w") as f:
    for name in name_list:
        f.writelines('===============和{}关系近的人物================='.format(name)+'\n')
        try:
            for k, s in model.wv.most_similar(positive=name, topn=100):
                if k in name_list:
                    f.writelines(k+'\n')
        except:
            pass
