f=open('logs.txt','r')
lines=list(f.readlines())
bd =[]
for l in lines:
    bd.append(l.split())
    f.close()
input('hello how are you today: ')
for i in range(len(bd)):
    i=1
    checking=bd[i][2]
    saving=bd[i][3]
    investment=bd[i][4]
    rate=bd[i][5]
ammout=(investment)
time=int(input('type how many years of interests: '))
real_rate=float(rate)*0.01
i= 0
print()
print('initial year:', "%.2f" %(round(ammout,2)),'$')

while i < time:
    ammout=(float(ammout) * (1+real_rate))
    i = i+1
    print('year',i,':', "%.2f" %float(round(ammout,2)),'$')