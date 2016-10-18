import pandas as pd

df = pd.read_excel('2016.10.10.xls')
#df = pd.read_excel('log.xls', sheetname=1)

#表头列的数据
#print(df.dtypes)

#某一列的数据
#print(type(df['代码']))

for x in df.index:
	print(df['代码'][x])
	print(type(df['代码'][x]))

#保存为excel
# out = pd.ExcelWriter('output.xls')
# new_df.to_excel(out)
# out.save()