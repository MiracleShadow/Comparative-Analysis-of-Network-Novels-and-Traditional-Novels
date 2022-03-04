# 定义字典类型来存储分词的结果，sort_list存放排序后的结果，STOPWORDS是进一步要忽略的词
words_dict = {}
with open("words_list.txt", "r") as fp:
    for i in fp.readlines():
        word = i.strip()
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
# 检索名字，对字典里的内容次数排序
name = []
with open("name.txt", "r") as fp:
    for i in fp.readlines():
        word = i.strip()
        name.append(word)
sort_list = [(value, key) for key, value in words_dict.items() if key in name]
sort_list.sort(reverse=True)
with open("sort_by_name.txt", "w") as fp:
    for value, key in sort_list:
        fp.writelines(f'{str(key)}---{str(value)}' + "\n")

# # 检索丹药等内容，对字典里的内容次数排序
# danyao = []
# fp = open("danyao.txt", "r")
# for i in fp.readlines():
#     word = i.strip()
#     danyao.append(word)
# fp.close()
#
# for key, value in words_dict.items():
#     if key in danyao:
#         sort_list.append((value, key))
# sort_list.sort(reverse=True)
# fp = open("sort_by_danyao.txt", "w")
# for value, key in sort_list:
#     fp.writelines(str(key)+"---"+str(value)+"\n")
# fp.close()

# # 检索等级等内容，对字典里的内容次数排序
# dengji = []
# fp = open("dengji.txt", "r")
# for i in fp.readlines():
#     word = i.strip()
#     dengji.append(word)
# fp.close()
#
# for key, value in words_dict.items():
#     if key in dengji:
#         sort_list.append((value, key))
# sort_list.sort(reverse=True)
# fp = open("sort_by_dengji.txt", "w")
# for value, key in sort_list:
#     fp.writelines(str(key)+"---"+str(value)+"\n")
# fp.close()

# 检索帮派等内容，对字典里的内容次数排序
# bangpai = []
# fp = open("bangpai.txt", "r")
# for i in fp.readlines():
#     word = i.strip()
#     bangpai.append(word)
# fp.close()
#
# for key, value in words_dict.items():
#     if key in bangpai:
#         sort_list.append((value, key))
# sort_list.sort(reverse=True)
# fp = open("sort_by_bangpai.txt", "w")
# for value, key in sort_list:
#     fp.writelines(str(key)+"---"+str(value)+"\n")
# fp.close()
