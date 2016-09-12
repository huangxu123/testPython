##判断是否是闰年
def isLeapYear(year):
	if year%400!=0 and year%4!=0:
		return False
	else:
		return True
		
def printYear(year):
	if isLeapYear:
		print(year,'年是闰年！')
	else:
		print(year,'年不是闰年！')

	
year=2016
printYear(year)