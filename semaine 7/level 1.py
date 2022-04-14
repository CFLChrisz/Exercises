login=False
data=[]
f=open('database.txt', 'r')
reader =list(f.readlines())
for i in reader:
    data.append(i.split())
    f.close()
print(data)

while login == False:
    un=input('choose ur fighter: ')
    ps=input('choose ur destiny: ')
        
        for k in range(0,len(i)):
            if data[k] == un and data[k] == ps:
                print('Fight On!')
                login=True
    else:
                print('we will find you and kill you!')