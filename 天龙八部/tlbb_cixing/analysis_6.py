import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

words_dict = {}
fp = open("words_list_3.txt", "r")
for k in fp.readlines():
    i = k.strip()
    # 匹配空格以前的内容
    word = re.match(".+( )", i)
    # 把空格及空格以前的内容删除，留下后面的词性标识
    flag = re.sub(".+( )", "", i)
    if flag == "p":
        if word.group(0) in words_dict:
            words_dict[word.group(0)] += 1
        else:
            words_dict[word.group(0)] = 1
fp.close()

print("the dict is finished\n")

sort_list = []
for key, value in words_dict.items():
    if value > 20 and len(key) > 1:
        sort_list.append((value, key))
sort_list.sort(reverse=True)
fp = open("sort_by_介词.txt", "w")
for value, key in sort_list:
    fp.writelines(str(key)+"---"+str(value)+"\n")
fp.close()



# 利用关键词制作图云：
font = r'C:\Windows\Fonts\simfang.ttf'
txt = ''.join([v + ',' for v, x in words_dict.items()])
wordcloud = WordCloud(background_color='white', width=1000, height=700, font_path=font, max_font_size=100).generate(txt)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('介词.jpg')
fp.close()
