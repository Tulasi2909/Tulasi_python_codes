num=[21,2,1,2,4,5,1,21]
new=[]
for index in range(len(num)):
    if num[index] in num[index+1:]:
        new.append(num[index])
print(new)

