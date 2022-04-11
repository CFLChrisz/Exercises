input('hello how are you today: ')
ammout=int(input('Please enter your initial ammout: '))
rate=float(input('type your yearly interrest rate: '))
time=int(input('type how many years of interests: '))
real_rate= rate*0.01
i= 1

while i < time:
    ammout=(ammout * (1+real_rate))
    i = i+1
    print('year',i,':', "%.2f" %(round(ammout,2)),'$')