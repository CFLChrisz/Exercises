f=open('logs.txt','r')
lines=list(f.readlines())
bd =[]
for l in lines:
    bd.append(l.split())
f.close()
print(bd)