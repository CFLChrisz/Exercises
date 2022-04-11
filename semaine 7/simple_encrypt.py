message = input('enter the message: ')  # each character in your message will be checked inside the var.
                                        # alphabet for its position inside alphabet and then it will add
                                        # the key value to that position and then this value will be store
                                        # in new variable as message.
alphabet ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789$%.!? '

key=5
encrypt=''
decrypt=''
for i in message:
    position=alphabet.find(i)
    newposition=(position+key)%68 #26%26=0(number of alphabet modulo)
    encrypt+=alphabet[newposition]  #slicing of alphabet
print(encrypt)

for i in encrypt:
    pos=alphabet.find(i)
    newpos=(pos-key)%68
    decrypt+=alphabet[newpos]
print(decrypt)
