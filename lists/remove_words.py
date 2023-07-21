words=['gfg', 'is', 'best', 'for', 'geeks']
letters=['g','e']
new=""
new_letters=""
final=[]
flag=0
for word in range(len(words)):
    new=words[word]
    for letter in range(len(letters)):
        new_letters=letters[letter]
        if new_letters in new:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        final.append(new)
print(final)
