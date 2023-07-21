numbers=[1,5,3,4,1,2,5]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)