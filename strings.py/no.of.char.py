name=input("enter: ")
a=[]
b=[]
temp=""
for i in name:
    temp=name.count(i)
    if i not in a:
        a.append(i)
        b.append(temp)
print(f"{a}:{b}")
    
    
