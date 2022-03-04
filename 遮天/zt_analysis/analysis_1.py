# 定义字典类型来存储分词的结果，sort_list存放排序后的结果，STOPWORDS是进一步要忽略的词
STOPWORDS = []
with open("hanyu2.txt", "r") as fp:
    for i in fp.readlines():
        word = i.strip()
        if len(word) > 1:
            STOPWORDS.append(word)
words_dict = {}
with open("words_list.txt", "r") as fp:
    for i in fp.readlines():
        word = i.strip()
        if word in words_dict:
            words_dict[word] += 1
        elif word not in STOPWORDS:
            words_dict[word] = 1
sort_list = [
    (value, key)
    for key, value in words_dict.items()
    if len(key) > 1 and value > 20
]

sort_list.sort(reverse=True)
with open("sort.txt", "w") as fp:
    for value, key in sort_list:
        fp.writelines(f'{str(key)}---{str(value)}' + "\n")
