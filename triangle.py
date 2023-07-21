x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if x==y==z:
    print("all sides of a triangle are equal and it is an equilateral triangle")
elif x!=y!=z and x!=z!=y:
    print("all sides of a triangle are not equal and it is a scalene triangle")
elif x==y!=z or x!=y==z or x==z!=y:
    print("two sides of a triangle are equal and it is an isoceles triangle")



