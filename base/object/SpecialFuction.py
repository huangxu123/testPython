class Man(object):
    sex='man'

wo=Man()
#dir() function
#print(dir(wo))

#help() function
#print(help(list))

ni=[8,1,2,4,3,5,9,6,7]
print('=========count=======')
print(ni.count(2))
print('=========index=======')
print(ni.index(4))
print('=========len=======')
print(len(ni))

ni.append(8)
print('=========list=======')
print(ni)
print(len(ni))

ni.sort()
print('=========pop=======')
print(ni.pop)
print(len(ni))

print('=========remove=======')
ni.remove(1)
print(ni)
print(len(ni))

print('=========insert=======')
ni.insert(0,1)
print(ni)
print(len(ni))
