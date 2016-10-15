#查询股票的具体信息，导出excl表格，并保存到mongodb.stock.stock中
import pymongo
import requests as req 
import pandas as pd 
import re
import time
import json
import decimal


#股票类
class Stock(object):

	# #所在市场，1表示沪市，2表示深市
	# market=''

	# #代码
	# code=''

	# #名称
	# name=''

	# #当前价格
	# price_now=''

	# #涨停价格
	# price_rise=''

	# #跌停价格
	# price_fall=''

	# #涨幅
	# gain=''

	# #成交量
	# volume=''

	# #成交额
	# trun_over=''

	# #量比
	# ratio=''

	# #换手率
	# trun_rate=''


	#stock_list是解析为list的股票信息格式为：
	#
	def setAttribute(self,stock_list):
		self.market=stock_list[0]
		self.code=stock_list[1]
		self.name=stock_list[2]
		self.price_now=stock_list[3]
		self.price_rise=stock_list[23]
		self.price_fall=stock_list[24]
		self.gain=stock_list[29]
		self.volume=stock_list[31]
		self.trun_over=stock_list[35]
		self.ratio=stock_list[36]
		self.trun_rate=stock_list[37]
		

#导出excel表格的数据集合
class excel_list(object):
	#所在市场
	MARKETS=[]
	#代码
	CODES=[]
	#名称
	NAMES=[]
	#当前价格
	PRICES_NOW=[]
	#涨停价格
	PRICES_RISE=[]
	#跌停价格
	PRICES_FALL=[]
	#涨幅
	GAINS=[]
	#成交量
	VOLUMES=[]
	#成交额
	TURN_OVER=[]
	#量比
	RATIOS=[]
	#换手率
	TURN_RATE=[]


	"""docstring for excel_list"""
	#设置表格数据集合,stock为股票类
	def appendList(self,stock):
		self.MARKETS.append(stock.market)
		self.CODES.append(stock.code)
		self.NAMES.append(stock.name)
		self.PRICES_NOW.append(stock.price_now)
		self.PRICES_RISE.append(stock.price_rise)
		self.PRICES_FALL.append(stock.price_fall)
		self.GAINS.append(stock.gain)
		self.TURN_RATE.append(stock.trun_rate)
		self.RATIOS.append(stock.ratio)
		self.VOLUMES.append(stock.volume)
		self.TURN_OVER.append(stock.trun_over)

#将类转换为dic形式，用以保存到mongodb中
def toMongoData(stock):
	mongoData={}
	mongoData['market']=stock.market
	mongoData['code']=stock.code
	mongoData['name']=stock.name
	mongoData['price_now']=stock.price_now
	mongoData['price_rise']=stock.price_rise
	mongoData['price_fall']=stock.price_fall
	mongoData['gain']=stock.gain
	mongoData['volume']=stock.volume
	mongoData['trun_over']=stock.trun_over
	mongoData['ratio']=stock.ratio
	mongoData['trun_rate']=stock.trun_rate
	return mongoData

#间歇时间
SleepNum = 3

#股票代码集合
MY_CODES=[]
#发送请求的id集合，在上海股票的代码后拼接1，深圳股票的代码后拼接2
IDS=[]

#df = pd.read_excel('2016.10.10.xls')
#取Sheet2表中的深圳股票
# df_2 = pd.read_excel('2016.10.10.xls', sheetname='Sheet2')

# for x in df_2.index:
# 	MY_CODES.append(df_2['代码'][x])
# 	IDS.append(str(df_2['代码'][x])+'2')

#print(IDS)

#创建数据集合实例
excel_list=excel_list()


mongo_addr = 'localhost'
mongo_port = 27017
db_name = 'stock'

#数据库地址
client = pymongo.MongoClient(mongo_addr, mongo_port)
#数据库名
db = client.stock


IDS=['0007802','0025142']
for y in range(1,len(IDS)+1):
	#id是股票代码（6）+股市代码（1），1表示沪市，2表示深市 
	url='http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id='+IDS[y-1]+'&token=beb0a0047196124721f56b0f0ff5a27c&cb=callback09800053940446487&callback=callback09800053940446487&_=1476150013474'
	#这是请求头，伪装成浏览器访问网站 
	my_headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',} 
	r=req.get(url,headers=my_headers) 

	s=r.text
	#截取符合格式的数据，｛"":[],"":[]｝
	s_1=s[26:len(s)-1]
	#print(s_1)

	#json读取数据,格式为：{'':[],'':[]}
	#decodejson类型为dict()
	decodejson = json.loads(s_1)
	#print(decodejson)
	#print(type(decodejson))

	#stock类型为list
	stock_str=decodejson['Value']
	#print(type(stock))
	print(stock_str)

	
	#
	if stock_str:
		# hsl=''
		# hsl=stock[37]
		# lb=''
		# lb=stock[36]
		#取换手率在1%到10%之间，量比在1到2之间
		#if decimal.Decimal(hsl)>=1 and decimal.Decimal(hsl)<=2 and decimal.Decimal(lb)>=1 and decimal.Decimal(lb)<=2:
		new_stock=Stock()
		new_stock.setAttribute(stock_str)
		excel_list.appendList(new_stock)
		print(new_stock)
		print(excel_list)

		#保存到数据库
		mongo_stock={}
		mongo_stock=toMongoData(new_stock)
		#print(type(mongo_stock))
		db.stock.insert(mongo_stock)

	time.sleep(SleepNum) 

print('--------------end----------------')
#导出excel表
#'涨停价格':excel_list.PRICES_RISE,'跌停价格':excel_list.PRICES_FALL,
df=pd.DataFrame({'代码':excel_list.CODES,'名称':excel_list.NAMES,'价格':excel_list.PRICES_NOW,'涨幅':excel_list.GAINS,'成交量':excel_list.VOLUMES,'成交额':excel_list.TURN_OVER,'换手率':excel_list.TURN_RATE,'量比':excel_list.RATIOS}) 
df.to_excel('D:\\detail.xlsx')
print('--------------文件---------------')