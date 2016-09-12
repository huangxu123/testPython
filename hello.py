print('Hello World!')

s1 = (1,2,3,'hello',4,'world',True,5)
s2 = [5,4,3,'hello',2,'world',False,1]
print(s1,type(s1))
print(s2,type(s2))

s3 = (1,s1,s2)
print(s3,type(s3))

s2[1]=11
print(s2[1])

#s1[1]=12
#print(s1[1])

s4='abcdefg'
print(s4[2:6:2])

i=1

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

if x==1:
	print('x=',x)
	if y==2:
		print('hello')
elif x==3:
	print('y=',y)
else:
	print('else')
	
	
for i in [1,2,3,4]:
	print(i)
	
j = range(210)
print(j)

for i in range(10):
	print(i)
	
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

print(change_integer(a))
print(a)


b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print(change_list(b))

print(b)