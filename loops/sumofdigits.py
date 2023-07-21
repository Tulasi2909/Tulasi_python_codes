num= int(input("num: "))
rem=0
sum=0
while num>0:
    rem=num%10
    sum+=rem
    num=num//10
print(sum)
