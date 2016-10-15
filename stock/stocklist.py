# -*- coding:utf-8 -*-
"""#@author:huangxu"""

import requests as req 
import pandas as pd 
import re
import time
import json

# def getType(paraType):
# 	if paraType=='CODES':
# 		return CODES
# 	elif paraType=='NAMES':
# 		return NAMES
# 	elif paraType=='GAINS':
# 		return GAINS
# 	elif paraType=='PRICES':
# 		return PRICES
# 	else:
# 		return NUM


#参数格式为： "abc...","def...","",""
def getList(rank):
	#将字符串转成list
	result_list=[]
	y=0
	str_n=''
	#x从0到len()-1,不包含len（）本身
	for x in range(len(rank)):
		if rank[x]==',':
			y=y+1
			#有25个字段，第25个逗号隔开
			if y==25:
				result_list.append(str_n)
				str_n=''
				y=0
			else:
				str_n=str_n+rank[x]
		#x从0开始计数，列表下标从0开始，最后一个不能被25整除，单独做处理
		elif x==len(rank)-1:
			str_n=str_n+rank[x]
			result_list.append(str_n)
		else:
			str_n=str_n+rank[x]
	return result_list


#取list中的股票信息
def getInfo(result_list,paraType):
	#取每个股票的具体信息
	str_rs=''
	#x从0开始计数，list下标从0开始
	for x in range(len(result_list)):
		rs=0
		#y从0开始计数，数组下标从0开始
		for y in range(len(result_list[x])):
			if result_list[x][y]==',':
				rs=rs+1
				if rs==1:
					str_rs=''
				if rs==2:
					if paraType=='CODES':
						CODES.append(str_rs)
					str_rs=''
				if rs==3:
					if paraType=='NAMES':
						NAMES.append(str_rs)
					str_rs=''
				if rs==4:
					if paraType=='PRICES':
						PRICES.append(str_rs)
					str_rs=''
				if rs==5:
					str_rs=''
				if rs==6:
					if paraType=='GAINS':
						GAINS.append(str_rs)
					str_rs=''
				if rs==8:
					if paraType=='NUM':
						NUM.append(str_rs)
					str_rs=''
			#最后一个字符要单独处理
			elif y==len(result_list[x])-1:
				rs=rs+1
				if rs==1:
					str_rs=''
				if rs==2:
					if paraType=='CODES':
						CODES.append(str_rs)
					str_rs=''
				if rs==3:
					if paraType=='NAMES':
						NAMES.append(str_rs)
					str_rs=''
				if rs==4:
					if paraType=='PRICES':
						PRICES.append(str_rs)
					str_rs=''
				if rs==5:
					str_rs=''
				if rs==6:
					if paraType=='GAINS':
						GAINS.append(str_rs)
					str_rs=''
				if rs==8:
					if paraType=='NUM':
						NUM.append(str_rs)
					str_rs=''
			else:
				str_rs=str_rs+result_list[x][y]
	if paraType=='CODES':
		return CODES
	elif paraType=='NAMES':
		return NAMES
	elif paraType=='PRICES':
		return PRICES
	elif paraType=='GAINS':
		return GAINS
	elif paraType=='NUM':
		return NUM
	else:
		pass

page='1'
pageSize='20'
#涨幅排序，-1是涨幅高的居前，1是跌幅高的居前
sortRule='-1'

#股票市场，C._SZAME表示深圳股市，C.2表示上海股市
#cmd='C.2'
cmd='C._SZAME'

#间歇时间
SleepNum = 3

#股票代码
CODES=[]
#股票名称
NAMES=[]
#股票价格
PRICES=[]
#股票涨幅
GAINS=[]
#股票成交量
NUM=[]

url='http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd='+cmd+'&sty=FCOIATA&sortType=C&sortRule='+sortRule+'&page='+page+'&pageSize='+pageSize+'&js=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=7bc05d0d4c3c22ef9fca8c2a912d779c&jsName=quote_123&_g=0.9271483678397806'
#这是请求头，伪装成浏览器访问网站 
my_headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',} 
r=req.get(url,headers=my_headers) 

#获取响应文本
s=r.text
#截取主要数据部分
s_1=s[14:len(s):1]

#取页数
pages=s_1[len(s_1)-3:len(s_1)-1]

page=pages
print(page)
#循环取数据
for pageNum in range(1,int(page)+1):
	url='http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd='+cmd+'&sty=FCOIATA&sortType=C&sortRule='+sortRule+'&page='+str(pageNum)+'&pageSize='+pageSize+'&js=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=7bc05d0d4c3c22ef9fca8c2a912d779c&jsName=quote_123&_g=0.9271483678397806'
	#这是请求头，伪装成浏览器访问网站 
	my_headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',} 
	r=req.get(url,headers=my_headers) 

	#获取响应文本
	s=r.text
	#截取主要数据部分
	s_1=s[14:len(s):1]

	#取当前页数据
	#取响应的股票内容
	rank=s_1[7:len(s_1)-11]
	#去除双引号
	p=re.compile('[\"]')
	rank_0=re.sub(p,"",rank)
	#将数据转成list
	result_list=getList(rank_0)
	print(result_list)


	#股票代码
	CODES=getInfo(result_list,'CODES')
	#股票名称
	NAMES=getInfo(result_list,'NAMES')
	#股票涨跌幅
	GAINS=getInfo(result_list,'GAINS')
	#股票价格
	PRICES=getInfo(result_list,'PRICES')
	#成交量
	NUM=getInfo(result_list,'NUM')

	time.sleep(SleepNum) 

print('--------------end-----------------')
df=pd.DataFrame({'代码':CODES,'名称':NAMES,'价格':PRICES,'涨幅':GAINS,'成交量（万）':NUM}) 
df.to_excel('D:\\stocklist.xlsx')