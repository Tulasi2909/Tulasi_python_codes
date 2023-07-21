name= input("enter: ")
new=""   
for index in range(len(name)):
    if len(name)<2:
        print("empty")
        break
    if index==0 or index==1 or index==len(name)-1 or index==len(name)-2:
        new+=name[index]      
print(new)
