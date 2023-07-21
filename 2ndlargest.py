x= int(input("x: "))
y= int(input("y: "))
z= int(input("z: "))
if x<y<z:
    print(f"{y} is second largest number")
elif x<y>z: 
    print(f"{x} is second largest number")
elif x>y<z: 
    print(f"{z} is second largest number")

