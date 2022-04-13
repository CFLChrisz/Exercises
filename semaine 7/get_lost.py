f=open('logs.txt','r')
data=[]
db=f.readlines()
for line in db:
    data.append(line.split(''))
bd=[line.split('')for line in f.readlines()]
print(bd) 