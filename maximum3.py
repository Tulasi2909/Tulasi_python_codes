x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if x>y>z:
    print(f"{x} is maximum")
elif x<y<z:
    print(f"{z} is maximum")
else:
    print(f"{y} is maximum")
