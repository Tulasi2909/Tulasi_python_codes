num=[1,5,4,2,1,6,4]
new=[]
pro=1
for i in num:
    if i not in new:
        new.append(i)
for i in new:
    pro*=i
print(pro)