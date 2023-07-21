
numbers=[2,5,36,15,24,6,7]
odd=[]
even=[]

for i in range(len(numbers)):
    
    if numbers[i]%2!=0:
        odd.append(numbers[i])
    else:
        even.append(numbers[i])

print(odd,even)

