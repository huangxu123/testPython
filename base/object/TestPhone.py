class Phone(object):
	name=''
	size=''
	price=''
	model=''
	
class iPhone(Phone):
	appId=''
	def getAppId(self):
		print('this is iPhone!')
		return self.appId

def TestPhone():
	iPhone7 =iPhone()
	iPhone7.name='iPhone7_my'
	iPhone7.size='4.7'
	iPhone7.price='5388'
	iPhone7.appId='123123456'
	iPhone7.getAppId()
	return "hello"

print(TestPhone())