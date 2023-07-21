words=['g fg', '   ', ' ', 'is', '            ', 'best']
new=""
final=[]
for word in range(len(words)):
    new=words[word]
    for index in range(len(new)):
        if new[index].isalpha():
            final.append(new)
            break
print(final)













# words=['gfg', '   ', ' ', 'is', '            ', 'best']
# new=""
# final=[]
# for word in range(len(words)):
#     new=words[word]
#     if new.isalpha()==True:
#         final.append(new)
# print(final)