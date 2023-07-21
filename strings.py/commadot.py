msg= input("enter: ")
new=""
for i in msg:
    if i==",":
        new+="."
    elif i==".":
        new+=","
    else:
        new+=i
    
print(new)
        
