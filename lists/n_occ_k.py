num=[[4, 5, 5, 4], [5, 4, 2]]
k=int(input("enter k: "))
N= int(input("enter occ of k: "))
new=[]
final=[]
count=0
for index in range(len(num)):
    if k in num[index]:
        new.append(num[index])
for index in range(len(new)):
    if k in new[index]:
        count+=1
        if count==N:
            final.append(new[index])
        

print(new)
print(final)
