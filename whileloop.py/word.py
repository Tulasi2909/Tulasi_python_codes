n=int(input("num: "))
b=0
rem=0
rev=0
c=0
op=""
while n>0:
    rem=n%10
    b=b*10+rem
    n=n//10
while b>0:
    rev=b%10
    c=c*10+rev
    b=b//10
    if rev==0 :
        op+="zero "
    elif rev==1:
        op+="one "   
    elif rev==2:
        op+="two "
    elif rev==3:
        op+="three "
print(op)
          





    




    
    
