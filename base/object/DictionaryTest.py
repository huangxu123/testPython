dic={'iphone':'ios','sony':'android','htc':'ios'}
print('======type(dic)======')
print(type(dic))

print('======dic[''iphonne'']======')
print(dic['iphone'])

print('======before update dic[''htc'']======')
print(dic['htc'])

print('======after update dic[''htc'']======')
dic['htc']='android'
print(dic['htc'])

print('======new dic and add element======')
#dic={}

print('======add huawei=======')
dic['huawei']='android'
print(dic['huawei'])

print('======for key===============')
print(dic.keys())
print(dic.values())
for key in dic:
    print(key)
    print(dic[key])



#print('======dic.keys()===============')
#print(dic.keys())
#print('======dic.values()===============')
#print(dic.values())
print('======dic.items()===============')

print('======dic.clear()===============')
#dic.clear()

print('======del huawei=================')
del dic['huawei']
print(dic.items())

print('======len========================')
print(len(dic))
