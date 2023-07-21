works=['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']
sub_list=['7','6','11','4']
sorted=[]
for index in range(len(sub_list)):
    for index1 in range(len(works)):
        if sub_list[index] in works[index1]:
            sorted.append(works[index1])
print(sorted)



