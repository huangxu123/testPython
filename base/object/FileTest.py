#open('file','mode'),mode include r、rb、r+、rb+、w、wb、w+、wb+、a、ab、a+、ab+
f=open('file.txt','w')
#f=open('file.txt','w')
#f=open('file.txt','r')
print('=======read()========')
#content_default=f.read()
#print(content_default)

print('=======readline()====')
#content_one=f.readline()
#print(content_one)

print('========readlines()===')
#content_all=f.readlines()
#print(content_all)

f.write('hello world_2!')
f.close()
