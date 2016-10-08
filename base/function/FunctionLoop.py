#test function loop

#range(start,end,step),step>=1 
def f_1(para):
	for i in range(0,len(para),2):
		print(para[i])

#x is element
def f_2(para):
	for x in para:
		print(x)

#enumerate()  (index,'value')
def f_3(para):
	for (index,value) in enumerate(para):
		tuble=(index,value)
		print(tuble)

#zip()
def f_4(para):
	ta = [1,2,3]
	tb = [9,8,7]

	# cluster
	zipped = zip(ta,tb)
	print(zipped)

	# decompose
	na, nb = zip(*zipped)
	print(na, nb)

#while
def f_while(para):
	n=len(para)
	i=0
	while i<n:
		print(i)
		i=i+3


def Test_f():
	S = 'abcdefghijk'
	#for
	#f_1(S)
	#f_2(S)
	#f_3(S)
	f_4(S)

	#while
	#f_while(S)

Test_f()