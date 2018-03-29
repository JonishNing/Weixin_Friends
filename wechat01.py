import itchat,time
import pandas as pd


def lc():
	print('Finish Login!')

def ec():
	print('Exit Login!')

itchat.auto_login(loginCallback = lc ,exitCallback = ec)
time.sleep(2)


"""
生成好友列表的CSV
"""

a = {'MemberList':[],'Uin':[],'UserName':[],'NickName':[],'HeadImgUrl':[],'ContactFlag':[]
,'MemberCount':[],'RemarkName':[],'HideInputBarFlag':[],'Sex':[],'Signature':[],'VerifyFlag':[]
,'OwnerUin':[], 'PYInitial': [], 'PYQuanPin': [], 'RemarkPYInitial': [], 'RemarkPYQuanPin': []
, 'StarFriend': [], 'AppAccountFlag':[], 'Statues':[], 'AttrStatus': [], 'Province': [], 'City':[]
, 'Alias':[], 'SnsFlag':[], 'UniFriend':[], 'DisplayName': [], 'ChatRoomId':[], 'KeyWord': []
, 'EncryChatRoomId': [], 'IsOwner': []}

	
#第一个是自己，所以不要
friends = itchat.get_friends(update=True)[1:]

for friend in friends:
	for key in a.keys():
		a[key].append(friend[key])

df = pd.DataFrame(a,sep='|',index=None)
#不带行索引的CSV
df.to_csv('./friends0.csv',sep='|',index=False)

itchat.logout() #强退




