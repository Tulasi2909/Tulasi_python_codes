x= int(input("x: "))
y= int(input("y: "))
for i in range(x,y):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            print(i)
    