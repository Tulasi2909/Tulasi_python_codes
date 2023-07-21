
x=1
sum=0
n=int(input("n= "))
while n>0:
    if n%2==0:
        x+=n**2
    else:
        x-=n**2
    n-=1
    
print(x)

