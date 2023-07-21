num= int(input("number: "))
rem=0
b=1
while num>0:
    rem = num%10
    b*=rem
    num=num//10
print(f"produ t: {b}")