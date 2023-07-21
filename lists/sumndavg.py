num=[1,5,6,8,4,3,9]
sum=0
avg=0
count=0
for i in num:
    sum+=i
    count+=1
    avg=sum/count
    # avg=sum/len(num)
print(sum)
print(avg)