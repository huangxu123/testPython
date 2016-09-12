#打印 Hello World
print('Hello World!')

#tuple和list的主要区别在于,一旦建立,tuple的各个元素不可再变更,而list的各个元素可以再变更
#s1是tuple定值表，元组
s1 = (1,2,3,'hello',4,'world',True,5)
#s2是list表
s2 = [5,4,3,'hello',2,'world',False,1]

#内置函数type(),查询变量的类型
print(s1,type(s1))
print(s2,type(s2))

#集合可以作为另一个集合的元素
s3 = (1,s1,s2)
print(s3,type(s3))

#序列的引用通过s[<int>]实现， int为下标
s2[1]=11
print(s2[1])

#s1[1]=12
#print(s1[1])

#范围引用： 基本样式[下限:上限:步长]
#在范围引用的时候，如果写明上限，那么这个上限本身不包括在内
s4='abcdefg'
print(s4[2:6:2])
