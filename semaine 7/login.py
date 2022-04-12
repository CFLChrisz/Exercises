f=open('logs.txt','r+')
lines=f.readlines()
print(lines)
correct = True
while correct:
    user = input('Hello! please enter your username: ')
    if user == 'mobb':
        psswrd = input('please emter the password: ')
        if psswrd == '1234':
            print('supreme victory!!!')
            break

        if psswrd != ('1234'):
            pssn = input('the password or username you provided is incorrect. Would you like to try again? y/n?')
            if pssn == 'y'.lower():
                correct=True
            else:
                print('Thank you, goodbye!')
                quit()

    if user != 'mobb':
        fail =input('invalid Username; would you like to try again? y/n?')
        if fail == 'y'.lower():
            correct=True
        else:
            print('Thank you, goodbye!')
            quit()