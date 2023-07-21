name= input("enter: ")
flag1=False
flag2=False
for i in name:
    if i.isalpha():
        flag1=True
    elif i.isnumeric():
        flag2=True
if flag1==True and flag2==True:
    print(True)
else:
    print(False)