num= int(input("num: "))
arm=0
rem=0
temp=num
while num>0:
    rem=num%10
    arm+=rem**3
    num=num//10
    if arm==temp:
        print("armstrong number")
        break
else:
        print("not a armstrong number")



