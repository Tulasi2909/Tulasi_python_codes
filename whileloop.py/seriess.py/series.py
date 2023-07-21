n= int(input("n: "))
i=1
j=1
while n>1:
    i+=i*j
    j+=1
    n-=1
print(i)