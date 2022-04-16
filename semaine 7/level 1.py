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
    