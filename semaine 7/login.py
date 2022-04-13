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
correct = True
while correct:
    user = input('Hello! please enter your username: ')
    if user == user1 or user2 or user3 or admin and not[]:
        psswrd = input('please enter the password: ')
        if psswrd == pass1:
            print('supreme victory!!!')
        elif psswrd == adminpass:
            print('welcome Administaror')
            break
        if psswrd !=pass1 or pass2 or pass3 or adminpass:
            pssn = input('the password or username you provided is incorrect. Would you like to try again? y/n?')
            if pssn == 'y'.lower():
                correct=True
            else:
                print('Thank you, goodbye!')
                quit()

    if user != user1 or user2 or user3 or admin:
        fail =input('invalid Username; would you like to try again? y/n?')
        if fail == 'y'.lower():
            correct=True
        else:
            print('Thank you, goodbye!')
            quit()