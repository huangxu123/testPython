i=1

#if语句
if i>0:
	x=1
	y=2
elif i==0:
	x=3
	y=4
else:
	x=5
	y=6
print(x,"=====",y)

#for循环
for i in range(10):
	j=i+1
	
print(j)

#定义函数
#当没有return, 或者return后面没有返回值时，函数将自动返回None
#None多用于关键字参数传递的默认值
def add_1(a,b):
	c=a+b
	print(c)
	print('=====c======')
	return a,b,c
	
print(add_1(3,4))
print(add_1(3,4)[0])


a = 1

def change_integer(a):
    a = a + 1
    return a
	
#整数变量a不发生变化
print(change_integer(a))
print(a)


b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print(change_list(b))
#原来的表b发生变化
print(b)