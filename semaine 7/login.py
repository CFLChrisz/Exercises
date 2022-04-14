
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

while loggin == False:
    user = input('Hello! please enter your username: ')
    psswrd=input("enter your account's password: ")
    
    if user==user1 and pass1==psswrd or user==user2 and pass2==psswrd or user==user3 and pass3==psswrd:
        print('Welcome', user,'!')
        loggin=True
    elif user==admin and adminpass==psswrd:
        print('welcome Administrator',user,'!')
        adminacc = True
        break
    else:
        error = input('the password or username you provided is incorrect. Would you like to try again? y/n?: ')
        if error == 'y'.lower():
            loggin=False
        else:
            print('Thank you, goodbye!')
            quit()

while loggin==True:
    print('How can we help you today?\n','type[1] for your checking account\n','type[2] for your saving account\n','type[3]')
    input('')
    
    if input==1:
        print('Checking Account')
