#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import itchat
import PIL.Image as Image

#TencentYoutuyun是自己下载的，不是用pip安装的
from TencentYoutuyun import *
from wordcloud import WordCloud,ImageColorGenerator

#搞头像

#itchat.login()
#friends = itchat.get_friends(update=True)[1:]

#df = pd.read_csv('./friends0.csv',sep='|', na_values='null')

def downloadHeadImage(friends):
	"""
	下载微信好友头像到文件夹
	"""
	basePath = os.path.abspath('.')
	baseFolder = os.path.join(basePath,'HeadImage')
	if os.path.exists(baseFolder) == False:
		os.makedirs(baseFolder)
	for i in range(0,len(friends)):
		friend = friends[i]
		imgFile = os.path.join(baseFolder,('Image%s.jpg' %(str(i) + '_' + friend['PYQuanPin'])))
		imgData = itchat.get_head_img(userName = friend['userName'])
		if os.path.exists(imgFile) == False:
			with open(imgFile,'wb') as f:
				f.write(imgData)



def analysisHeadImage(baseFolder):
	"""
	分析头像信息
	"""
	if os.path.exists(baseFolder) == False:
		return 'Error Path!!!'
	faceApi = YouTu(appid='10124339',secret_id='AKIDPefUBnjxZz9LNCx7C4hAVhDcmhUCu180',secret_key='mIYYKq67sNcbKn02sUqzua3HI5e2HKAo')
	use_face = not_use_face = 0
	image_tags = ''
	index = 0
	for imageFile in os.listdir(baseFolder):
		index += 1
		AbsPath = os.path.join(baseFolder,imageFile)
		if os.path.isdir(AbsPath):
			continue
		#返回一个json,有人脸信息
		ret = faceApi.DetectFace(AbsPath)
		#判断是否包含人脸
		if len(ret['face']) == 0 or len(ret['face'][0]) == 0:
			not_use_face += 1
		else:
			use_face += 1

		#返回一个json,有标签信息
		ret1 = faceApi.imagetag(AbsPath)
		if 'tags' not in ret1:
			continue
		#标签组成一个str
		for tag in ret1['tags']:
			image_tags += tag['tag_name'].encode('iso8859-1').decode('utf-8') + ','		
		if(index % 20 == 0):
			print(u'已处理%d个人,还剩%d个人' %(index,len(os.listdir(baseFolder))))	
	back_coloring = np.array(Image.open('./timg.jpg'))
	wordcloud = WordCloud(
		font_path='/Library/Fonts/Arial Unicode.ttf',
		background_color="white",
		max_words=1200,
		mask=back_coloring, 
		max_font_size=75,
		random_state=45,
		width=800, 
		height=480, 
		margin=15
	)
	wordcloud.generate(image_tags)
	wordcloud.to_file('./HeadImage.png')
	plt.imshow(wordcloud)
	plt.axis("off")
	#plt.show()
	print(u'头像关键字出图成功')
	labels = [u'使用人脸头像',u'不使用人脸头像']
	counts = [use_face,not_use_face]
	colors = ['red','yellowgreen','lightskyblue']
	plt.figure(figsize=(8,5), dpi=80)
	plt.axes(aspect=1) 
	plt.pie(counts, 
			labels=labels, 
			colors=colors, 
			labeldistance = 1.1, 
			autopct = '%3.1f%%', 
			shadow = False, 
			startangle = 90, 
			pctdistance = 0.6 
	)
	plt.legend(loc='upper right',)
	plt.title(u'微信好友使用人脸头像情况')
	plt.show()
	



baseFolder = r'/Users/Ning/Desktop/Code/Python_Learning/wechat/HeadImage'
analysisHeadImage(baseFolder)




#itchat.log_out()