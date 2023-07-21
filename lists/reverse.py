num=[15,47,12,23,45]
rev=[]
for index in range(len(num)):
    if index<len(num):
        rev.append(num[len(num)-index-1])
print(rev)