# 定义字典类型来存储分词的结果，sort_list存放排序后的结果，STOPWORDS是进一步要忽略的词
words_dict = {}
STOPWORDS = []

# 写入要屏蔽的词库STOPWORDS
sort_list = []
fp = open("hanyu2.txt", "r")
for i in fp.readlines():
    word = i.strip()
    if len(word) > 1:
        STOPWORDS.append(word)
fp.close()

# 在jieba分词的结果里，统计每个词出现的情况，如果不在屏蔽词库里，就写入字典里
fp = open("words_list.txt", "r")
for i in fp.readlines():
    word = i.strip()
    if word in words_dict:
        words_dict[word] += 1
    elif word not in STOPWORDS:
        words_dict[word] = 1
fp.close()

for key, value in words_dict.items():
    if len(key) > 1 and value > 20:
        sort_list.append((value, key))
sort_list.sort(reverse=True)
fp = open("sort.txt", "w")
for value, key in sort_list:
    fp.writelines(str(key) + "---" + str(value) + "\n")
fp.close()
