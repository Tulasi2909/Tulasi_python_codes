x= int(input("x= "))
y= int(input("y= "))
i=2
j=0
while x>=i and y>=i:
    if x==y:
        j=i
    if x%i==0 and y%i==0:
        j=i
    i+=1
print(f"hcf of {x},{y} is {j}")

        
