num=[1,5,2,4,6,7]
new=[]
for index in range(len(num)-1):
    if num[index]<num[index+1]:
        new.append(num[index+1])
    else:
        new.append(num[index])
print(new)
