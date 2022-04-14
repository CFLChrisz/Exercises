f=open('logs.txt','r')
lines=list(f.readlines())
bd =[]
for l in lines:
    bd.append(l.split())
f.close()
print(bd)
user1=bd[0][0]
user2=bd[1][0]
user3=bd[2][0]
admin=bd[3][0]
pass1=bd[0][1]
pass2=bd[1][1]
pass3=bd[2][1]
adminpass=bd[3][1]    
loggin = False
while loggin==False:
    user = input('Hello! please enter your username: ')
    psswrd=input('Enter your password.: ')
    if user==user1 and psswrd==pass1 or user==user2 and psswrd==pass2 or user==user3 and psswrd==pass3:
            print('Welcome',user,)
            loggin=True
    elif user==admin and psswrd==adminpass:
        print('welcome Administaror',user,'!!!')
        loggin=True
        adminacc=True
        break
    else:
        pssn = input('the password or username you provided is incorrect. Would you like to try again? y/n?')
        if pssn == 'y'.lower():
            loggin=False
        else:
            print('Thank you, goodbye!')
            quit()

if loggin==True:
    print(user)
elif adminacc==True:
    print(user)