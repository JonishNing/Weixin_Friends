import pandas as pd
#from pyecharts import Pie
#from echarts import Echart, Legend, Pie
import matplotlib.pyplot as plt


"""
好友男女比例
"""
df = pd.read_csv('./friends1.csv',sep='|')
#男，女，中性
male = female = mid = 0
for i in range(0,len(df)):
	sex = df.loc[i,'Sex']
	#print(type(sex))
	if sex == 1:
		male += 1
	elif sex == 2:
		female += 1
	else:
		mid += 1

total = len(df)
menp = float(male)/total*100
womenp = float(female)/total*100
midp = float(mid)/total*100


#打印结果
print('men:%d %.2f%%' %(male,menp))
print('women:%d %.2f%%' %(female,womenp))
print('midguy:%d %.2f%%' %(mid,midp))

#用matplotlib画图
labels = 'male','felmale','midguy'
fracs = [menp,womenp,midp]
explode = [0.1,0,0]
plt.axes(aspect = 1)
plt.pie(x=fracs,labels=labels,explode=explode,autopct='%2.2f%%',shadow=True,
		labeldistance=1.2,startangle=90,pctdistance=0.6)
plt.show()
"""
#可以生成一个echart的html
attr = ['male','female','mid']
v1 = [menp,womenp,midp]
pie = Pie('wecaht')
pie.add('',attr,v1,is_label_show=True)
pie.show_config()
pie.render()
pie.plot()
可以生成一个html
"""

"""
#画不了，python3的str的问题
chart = Echart('Percentage of Sex','from wechat')
chart.use(Pie(name = 'WeChat',
              data = [{'value': male, 'name': u'男性 %.2f%%' % (menp)},
               {'value': female, 'name': u'女性 %.2f%%' % (womenp)},
               {'value': mid, 'name': u'其他 %.2f%%' % (midp)}]))
chart.use(Legend(['male','female','mid']))
chart.plot()
"""
