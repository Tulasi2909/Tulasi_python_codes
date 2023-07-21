num=[1,25,48,5,64]
new=[]

add=0
temp=0
for i in num:
    sum=0
    if i<=9:
        new.append(i)
    else:
        while i!=0:
            temp=i%10
            sum+=temp
            i=i//10
        new.append(sum)

       
print(new)