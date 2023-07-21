num=[8, 5, 9, 11, 3, 7]
sub_list=[9,11]
new=[]
final=[]
for index in range(len(num)):
        if num[index] not in sub_list:
                    
        # if sub_list[0]!= num[index] and sub_list[1]!=num[index]:
            new.append(num[index])
            final.append(new)
        else:
            final.append(num[index])
print(final)