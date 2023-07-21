count=0
sum=0
average=0
while True:
    n=input("n= ")
    if n=="zero":
        break
    count+=1
    sum+=int(n)
    average=sum/count
    
print(sum)
print(average)