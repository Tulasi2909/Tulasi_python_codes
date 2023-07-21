
average = 0
count=0
sum=0
product=1
while True:
    a=(input("integer: "))
    if a!="q":
        sum+=int(a)
        count+=1
        average=sum/count
        product*=int(a)
    else:
        break
    print("do you want to quit?")

print(average)
print(product)
    

