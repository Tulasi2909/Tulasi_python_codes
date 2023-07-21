name= input("enter: ")
new=""
new1=""
if len(name)<3:
    print(name)
elif name[-3:]=="ing":
    new1=name+"ly"
    print(new1)
else:
    new=name+"ing"
    print(new)

    