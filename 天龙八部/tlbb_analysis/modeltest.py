import gensim

# 读入训练好的模型
model = gensim.models.Word2Vec.load('天龙八部.model')

namelist = []

fp = open("sort_by_name.txt", "r")
for i in fp.readlines():
    name = ''
    for s in i:
        if s != '-':
            name += s
        else:
            break
    namelist.append(name)

print(namelist)

for name in namelist:
    try:
        print('===============和{}类似的人物================='.format(name))
        print(model.most_similar(positive=[name]))
        # for s in model.most_similar(positive=[name])[:5]:
        #     # if s in namelist:
        #     print(s)
        print('\n\n')
    except:
        pass