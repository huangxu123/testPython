#test function loop

#range()
def f_1(para):
	for i in range(0,len(para),3):
		print(para[i])

def Test_f():
	S = 'abcdefghijk'
	f_1(S)

Test_f()