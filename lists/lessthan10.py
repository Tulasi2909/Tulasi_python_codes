numbers=[1,5,3,12,10,6]
new=[]
for i in range(len(numbers)):
    if numbers[i]>=10:
        new.append(numbers[i])
print(new)
