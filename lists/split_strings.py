words=[['Gfg', 'is', 'best'], ['for', 'Geeks'], ['Preparing']]
new_words=""
new=[]
for word in range(len(words)):
    new_words=(words[word])
    for index in range(len(new_words)):
        new.append(new_words[index])
print(new)

    



# words=['Gfg is best', 'for Geeks', 'Preparing']
# new_words=""
# new=""
# for word in range(len(words)):
#     new_words+=words[word]+" "
#     new=new_words.split()   
# print(new)
    