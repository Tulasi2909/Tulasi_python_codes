num=[1,5,2,6]
remove=(input("enter: "))
new=[]
for i in num:
    if i not in remove:
        new.append(i)
print(new)

# remove=int(input("enter: "))
# remove1=int(input("enter: "))
# new=[]
# for i in num:
#     if i!=remove and i!=remove1:
#         new.append(i) 
# print(new)