import requests as req 
import time
import json

#新股中签号类
class newStock(object):
	#中签号码类数，以位数后几位分类
	count=''
	me=''
	#中签号码
	re=[]
	rc=''
	#查询时间
	update=''

	def setAttribute(self,stock):
		self.count=stock['count']
		self.me=stock['me']
		self.re=stock['re']
		self.rc=stock['rc']
		self.update=stock['update']

	
#间隔休息时间
SleepNum=2

#新股中签号查询
code='002816'
print('查询'+code+'的中签号！')
url='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=MD&sty=MDTOR&code='+code+'&js=var%20zqh={(x)}'

#这是请求头，伪装成浏览器访问网站 
my_headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',} 

r=req.get(url,headers=my_headers) 

s=r.text
#print(s)

#截取符合格式的数据，｛"":[],"":[]｝
s_1=s[8:len(s):1]

#json读取数据,格式为：{'':[],'':[]}
#decodejson类型为dict()
decodejson = json.loads(s_1)
#print(decodejson)

stock_new=newStock()
stock_new.setAttribute(decodejson)
#print(stock_new.re)

sign=[]
sign=stock_new.re
for x in range(1,len(sign)+1):
	#sign[x-]['name']
	print('尾号后'+sign[x-1]['name']+'位中签号：'+sign[x-1]['value'])

time.sleep(SleepNum)