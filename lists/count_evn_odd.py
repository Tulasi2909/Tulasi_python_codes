num=[2,5,4,3,6,7]
count_even=0
count_odd=0
for i in num:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(count_even)
print(count_odd)
