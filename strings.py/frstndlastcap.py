name = input("enter: ")
new=""


for index in range(len(name)):
    if index==0:
        new+=name[index].upper()
    elif index==len(name)-1:
        new+=name[index].upper()
    else:
        new+=name[index]
print(new)

    
    

    