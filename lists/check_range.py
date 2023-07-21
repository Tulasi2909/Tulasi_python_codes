num=[1,5,6,3,4]
start=int(input("start:"))
end=int(input("end:"))
flag=False
for i in num:
    if i>=start and i<=end:
        flag=True
    else:
        break
print(flag)
