#抓取东方财富板块信息

import requests as req 
import pandas as pd 
import time 
import re 

url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._BKHY&sty=FPGBKI&st=c&sr=-1&p=1&ps=5000&cb=&js=var%20BKCache=[(x)]&token=7bc05d0d4c3c22ef9fca8c2a912d779c&v=0.811256305515943"

#休息时间
SleepNum = 3 

CODES=[]
NAMES=[]
GAINS=[]
LTGP_CODES=[]
LTGP_NAMES=[]

class BanKuai(object):
	code=''
	name=''
	hsl=''
	gains=''
	lt_code=''
	"""docstring for BanKuai"""
	def __init__(self, arg):
		super(BanKuai, self).__init__()
		self.arg = arg
		
class GuPiao(object):
	market=''
	code=''
	name=''
	price=''
	gains=''
	
	"""docstring for GuPiao"""
	def __init__(self, arg):
		super(GuPiao, self).__init__()
		self.arg = arg


r=req.get(url) 
#print(r.text)
s=r.text
s_1=s[13:len(s)-1:1]
#字符串转json
#d = json.loads(s_1)
#s_1.split(["\",",100])

#把引号全部替换
p=re.compile('[\"]')
pp=re.sub(p,"",s_1)
# print(pp)

#分别取板块信息
result_list=[]
y=0
str_n=''
for x in range(0,len(pp)):
	if pp[x]==',':
		y=y+1
		if y==18:
			result_list.append(str_n)
			str_n=''
			y=0
		else:
			str_n=str_n+pp[x]
	else:
		str_n=str_n+pp[x]

#print(result_list)

#取每个板块的具体信息
str_rs=''
for x in range(1,len(result_list)):
	rs=0
	for y in range(1,len(result_list[x])):
		if result_list[x][y]==',':
			rs=rs+1
			if rs==1:
				str_rs=''
			if rs==2:
				CODES.append(str_rs)
				str_rs=''
			if rs==3:
				NAMES.append(str_rs)
				str_rs=''
			if rs==4:
				GAINS.append(str_rs)
			if rs==7:
				str_rs=''
			if rs==8:
				LTGP_CODES.append(str_rs)
			if rs==9:
				str_rs=''
			if rs==10:
				LTGP_NAMES.append(str_rs)
		else:
			str_rs=str_rs+result_list[x][y]

#print(CODES)

print(NAMES)

#print(GAINS)

#print(LTGP_CODES)

#print(LTGP_NAMES)

df=pd.DataFrame({'板块代码':CODES,'板块名称':NAMES,'龙头股票':LTGP_NAMES,'龙头股票代码':LTGP_CODES,'板块涨幅':GAINS}) 
df.to_excel('D:\\plate.xlsx')


time.sleep(SleepNum) 

print('-------------end--------------')