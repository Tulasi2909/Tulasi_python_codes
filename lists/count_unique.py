num=[1,5,2,1,6,2,4,6]
new=[]
count=0
for i in num:
    if i not in new:
        new.append(i)
        count+=1
print(new)
print(count)
