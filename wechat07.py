import PIL.Image as Image
import math
import os

"""
头像拼图
"""

def pastePic(baseFolder):
	if os.path.exists(baseFolder) == False:
		return 'Error Path!!!'

	pics = os.listdir(baseFolder)
	numPic = len(pics)
	#拼后每个图片的边长	
	eachsize = int(math.sqrt(float(640*640) /numPic))
	#每列、每行几张图
	numline = int(640/eachsize)
	toImage = Image.new('RGBA',(640,640))
	x = y = 0
	for imageFile in pics:
		AbsPath = os.path.join(baseFolder,imageFile)
		#过滤不是图片的
		if not AbsPath.endswith('jpg') or os.path.isdir(AbsPath):
			continue
		img = Image.open(AbsPath)
		img = img.resize((eachsize,eachsize), Image.ANTIALIAS)
		#把小图堆上去
		toImage.paste(img,(x*eachsize,y*eachsize))
		x += 1
		if x == numline:
			x = 0
			y += 1
	#此处不能用jpg和bmp，因为RGBA有四个通道
	toImage.save('./touxiang.png')

baseFolder = r'/Users/Ning/Desktop/Code/Python_Learning/wechat/HeadImage'
pastePic(baseFolder)
