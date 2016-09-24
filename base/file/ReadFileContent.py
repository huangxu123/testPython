#data mode
#filename:test.txt
#  data:
#    iPhone, ios, 10
#    Nokia, WP, 10
#    HTC, android, 7
#

f=open("test.txt","r")

#read all bytes 
content=f.read()

#read one line
#content=f.readline()

#read all lines to list
#['iPhone, ios, 10'\n,'Nokia, WP, 10\n','HTC, android, 7\n']
#content=f.readlines()

print(content)
f.close()