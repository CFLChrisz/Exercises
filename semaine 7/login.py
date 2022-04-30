def encrypt():
    f=open('logs.txt','r')
    lines=list(f.readlines())
    bd =[]
    for l in lines:
        bd.append(l.split())
    f.close()
    print(bd[0][1])

    def log():
        user = input('Hello! please enter your username: ')
        psswrd=input("enter your account's password: ")
        checker=[]
        for i in range(len(bd)):
            if user==bd[i][0]:
                checker=bd[i][1]
        if psswrd==checker and psswrd!=bd[3][1]:
            print('\nWelcome', user,'!')
        elif user==bd[3][0] and psswrd==bd[3][1]:
            print('\nwelcome Administrator',user,'!')
        else:
            error = input('the password or username you provided is incorrect. Would you like to try again? y/n?: ')
            if error == 'y'.lower():
                log()
            else:
                print('Thank you, goodbye!')
                quit()
        def logmenu():
            print('How can we help you today?\ntype[1] for your checking account\ntype[2] for your saving account\ntype[3] for your investment account\nType[4] to switch account\nType[5] to logout ')
            for i in range(len(bd)):
                if user==bd[i][0]:
                    checking=bd[i][2]
                    saving=bd[i][3]
                    investment=bd[i][4]
                    rate=bd[i][5]
            option=int(input('Type here: '))
            if option==1:
                Caccount=True
                while Caccount==True:
                    print('\nChecking Account:',("%.2f" % float(checking)),'$')
                    print()
                    print("Type[1] to deposit\nType[2]to withdraw\nType[3] to go back to the main menu\nType[4] to logout")
                    option=int(input('Type here: '))
                    if option==1:
                        depositC=(input("how much do  you want to deposit: "))
                    if option==2:
                        withdrawC=(input("how much do you want to withdraw: "))
                    if option==3:
                        print()
                        Caccount=False
                        logmenu()
                    if option==4:
                        print("Thank you, Goodbye.")
                        Caccount=False
                        quit()

            elif option==2:
                Saccount=True
                while Saccount==True:
                    print("\nsaving account:",("%.2f" % float(saving)),'$')
                    print()
                    print("Type[1] to deposit\nType[2]to withdraw\nType[3] to go back to the main menu\nType[4] to logout")
                    option=int(input('Type here: '))
                    if option==1:
                        depositS=(input("how much do  you want to deposit: "))
                    if option==2:
                        withdrawS=(input("how much do you want to withdraw: "))
                    if option==3:
                        print()
                        Saccount=False
                        logmenu()
                    if option==4:
                        print("Thank you, Goodbye.")
                        Saccount=False
                        quit()
            elif option==3:
                Iaccount=True
                print("\ninvestment account:",("%.2f" % float(investment)),'$')
                print("intrest rate:",rate,'%')
                print("\nType[1] to calculate  the yearly rate of interest\nType[2]to return to the main menu\nType[3] to logout: ")
                option=int(input('Type here: '))
                if option==1:
                    while Iaccount==True:
                        time=int(input('type how many years of interests: '))
                        real_rate=float(rate)*0.01
                        l= 0
                        print()
                        print('Initial year:', "%.2f" %float(investment),'$')
                        while l < time:
                            investment=(float(investment) * (1+real_rate))
                            l = l+1
                            print('year',l,':', "%.2f" %float(round(investment,2)),'$')
                        Iaccount=False
                        print("\nType[1] if you wish to go repeat the opperation\nType[2] to go back to the main menu\nType[3] to logout")
                        option=int(input('Type here: '))
                    if option==1:
                        Iaccount=True
                    elif option==2:
                        logmenu()
                    elif option==3:
                        print('thank you, goodbye!')
                        quit()
                    else:
                        print('Error; please choose a valid option.')
                elif option==2:
                    logmenu()
                elif option==3:
                    print('thank you, goodbye!')
                    quit()
                else:
                    print('Error; please choose a valid option.')
            elif option==4:
                print("login out...")
                log()
            elif option==5:
                print('Thank you, goodbye!')
                quit()
            else:
                ('Error; please choose a valid option.')
        logmenu()
    log()
encrypt()