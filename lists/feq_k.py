num=[1,5,2,1,4,2,1,6,4]
count=0
for i in range(len(num)):
    if num[i] in num[i+1:] :  
        count+=1
        