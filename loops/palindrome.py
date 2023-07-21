num= int(input("num: "))
rem=0
temp=num
b=0
while num>0:
    rem=num%10
    b=b*10+rem
    num=num//10
if temp==b:
    print("num is palindrome")
else:
    print("num is not a palindrome")

   
    