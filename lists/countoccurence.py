B= [34,21,3,12,34,56,76,5,4,21,12,34]
num=int(input("enter number: "))
count=0
for i in range(len(B)):
    if num==B[i]:
        count+=1
print(count)

    