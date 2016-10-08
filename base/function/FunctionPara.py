#test para

#key word para
def f_1(a,b,c):
	print('This is a:')
	print(a)
	print('This is b:')
	print(b)
	print('This is c:')
	print(c)
	print('This is a+b+c:')
	print(a+b+c)

#default para
def f_2(a,b,c=100):
	print('This is a:')
	print(a)
	print('This is b:')
	print(b)
	print('This is c:')
	print(c)
	print('This is a+b+c:')
	print(a+b+c)

#packing default para
def f_3(*para):
	#print '*para' 
	#1 2 3 4 5
	print(*para)

	#print 'para'
	#(1 2 3 4 5)
	print(para)

	#print type of para
	print(type(para))

#packing keyword para
def f_4(**para):
	#f_4(a=1,b=2)
	#print {'b': 2, 'a': 1}
	print(para)

	#f_4(a=1,b=2)
	#print b a
	print(*para)
	#f_4(a=1,b=2)
	#this type is dict
	print(type(para))
	

def Test_f():
	#one=1
	#two=2
	#three=3
	#print 1 2 3 6 
	#f_1(one,two,three)

	#print 3 1 2 6 
	#f_1(three,one,two)

	#c=3
	#f_2(one,two,three)

	#c=100
	#f_2(one,two)

	#packing para,this para's type is tuple
	#f_3(1,2,3,4,5)

	#packing keyword para
	#f_4(a=1,b=2)

	#unpacking
	#para={1,2,3}
	#f_3(*para)

	#unpacking keyword dict
	para_1={'a':1,'b':2}
	f_4(**para_1)

Test_f()