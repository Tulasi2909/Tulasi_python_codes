name= input("enter: ")
new=""
for index in range(len(name)):
    if index==0:
        new+=name[index]
if new in name:
    print(name.replace(new,"&"))
      
