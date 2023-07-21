nums=int(input("How many nums? "))
int_count=0
int_limit=nums
average=0
sum = 0
while int_count<int_limit:
    num=int(input("number: "))
    int_count+=1
    sum+=num
    average=sum/nums
    
print(average)
 
