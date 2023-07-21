n=int(input("n: "))
x=2
y=0
while n>0:
    y=y*10+x
    n-=1
    print(y,end=",")