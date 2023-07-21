x= int(input("x: "))
y= int(input("y: "))
even=0
odd=0
while x<=y:
    x+=1
    print(x)
    if x%2==0:
        even+=x
    if x%2!=0:
        odd+=x
print(f"sum of even numbers is {even}")
print(f"sum of odd numbers is {odd}")




    
