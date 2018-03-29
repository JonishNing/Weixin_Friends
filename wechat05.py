import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import jieba
import re

from wordcloud import WordCloud,ImageColorGenerator
from matplotlib.font_manager import *
from snownlp import SnowNLP

"""
个性签名分词，出词云的图
"""

df = pd.read_csv('./friends0.csv',sep='|', na_values='null')
#填空值
df = df.fillna(999999) 
#正则去表情
rep = re.compile('<.*>')
#存储的签名的列表
slist = []
#存储情绪值的列表
sentimentlist = []
for i in range(0,len(df)):
	signature = df.loc[i,'Signature']
	if type(signature) == int or len(signature) == 0:
		continue
	signature = signature.strip().replace('span','').replace('class','').replace('emoji','')
	signature = rep.sub('',signature)
	slist.append(signature)
	#得到情绪值，加入列表，越大，情绪越正向
	if(len(signature)>0):
		sentimentlist.append(SnowNLP(signature).sentiments)

#不同情绪的人数
good = len(list(filter(lambda x:x>0.66,sentimentlist)))
normal = len(list(filter(lambda x:x>=0.33 and x<=0.66,sentimentlist)))
bad = len(list(filter(lambda x:x<0.33,sentimentlist)))
labels = [u'负面',u'正常',u'正面']
values = (bad,normal,good)
#中文乱码解决
myfont = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')  
#plt.rcParams['font.sans-serif'] = ['simHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel(u'情感分析',fontproperties=myfont)
plt.ylabel(u'频数',fontproperties=myfont)
plt.xticks(range(3),labels,fontproperties=myfont)
plt.legend(loc='upper right',)
plt.bar(range(3),values,color ='rgb')
plt.title(u'微信好友签名情感分析',fontproperties=myfont)
plt.show()
#画签名的词云
text = ''.join(slist)
wordlist_jieba = jieba.cut(text,cut_all=True)
wl_space_split = ' '.join(wordlist_jieba)
#print(wl_space_split[:500])
my_wordcloud = WordCloud(background_color='white',max_words=2000,max_font_size=40,
						random_state=42,font_path='/Library/Fonts/Arial Unicode.ttf')\
						.generate(wl_space_split)
#image_colors = ImageColorGenerator(back_image)
my_wordcloud.to_file('./signature.png')
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()



	
	
	