f=open('logs.txt','r')
lines=list(f.readlines())
bd =[]
for l in lines:
    bd.append(l.split())
f.close()
print(bd)
user1=bd[0]
user2=bd[1]
user3=bd[2]
admin=bd[3]
pass1=user1[1]
pass2=user2[1]
pass3=user3[1]
adminpass=admin[1]    
loggin = False
while loggin==False:
    user = input('Hello! please enter your username: ')
    psswrd=input('Enter your password.: ')
    if user==user1[0] and psswrd==pass1 or user==user2[0] and psswrd==pass2 or user==user3[0] and psswrd==pass3:
            print('Welcome',user,)
            loggin=True
    elif user==admin[0] and psswrd==adminpass:
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

while loggin==True:
    checking=user
    print("How can we serve you today!\nType[1] for your checking account\nType[2] for your saving accout\nType[3] for your investment account\ntype[4] to logout\n")
    option =int(input(''))
    if option==1:
        print(checking)