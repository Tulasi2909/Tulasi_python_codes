num = int(input("enter number: "))
b=0
rem=0
while num>0:
    rem=num%10
    b+=rem
    num=num//10

print(f"sum: {b}")





