num= int(input("enter number: "))
rem=1
a=1
while num>0:
    rem=num%10
    a*=rem
    num=num//10
print(a)