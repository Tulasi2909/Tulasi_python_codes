list1=['Gfg', 'is', 'not', 'best', 'and', 'not', 'for', 'CS']
list2=['Its ok', 'all ok', 'wrong', 'looks ok', 'ok', 'wrong', 'ok', 'thats ok']
k='ok'
num=0
final=[]
for index in range(len(list2)):
    if k in list2[index]:
        final.append(list1[index])
print(final)
