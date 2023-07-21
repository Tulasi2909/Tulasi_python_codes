str1=input("str1: ")
new1=str1.split()
str2=input("str2: ")
new2=str2.split()
uncommon=[]
for i in new1:
    if i not in str2:
        uncommon.append(i)
        continue
for i in new2:
    if i not in str1:
        uncommon.append(i)
        continue
print(uncommon)


