count_positive=0
count_negative=0
while True:
    n= input(">>")
    if n=="zero":
        break
    n=int(n)
    if n>=0:
        count_positive+=1
    
    if n<0:
        count_negative+=1
    
print(f"positive numbers= {count_positive}")
print(f"negative numbers= {count_negative}")





