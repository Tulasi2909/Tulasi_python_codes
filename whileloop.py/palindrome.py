n=int(input("num: "))
rem=0
b=0
temp=n
while n>0:
    rem=n%10
    b=b*10+rem
    n=n//10
    if temp==b:
        print(" num is palindrome number")
        break
else :
    print("num is not a palindrome number")




