s= input("enter: ")
flag=True
for i in s:
    if ord(i)>33 and ord(i)<47:
        flag=False

        print(ord(i))
        break
    elif ord(i)>58 and ord(i)<64:
        flag=False

        print(ord(i))
        break
    elif ord(i)>91 and ord(i)<96:
        flag=False

        print(ord(i))
        break
    elif ord(i)>123 and ord(i)<126:
        flag=False

        print(ord(i))
        break
    
if flag == True:
    print("Acepted")
else:
    print("NOO")