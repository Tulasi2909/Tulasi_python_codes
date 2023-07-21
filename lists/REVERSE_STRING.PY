words=['geeks', 'for', 'geeks', 'is', 'best']
new_words=[]
for word in words:
    rev=""
    for index in range(len(word)):
        rev+=word[len(word)-index-1]
    new_words.append(rev)
print(new_words)



    




