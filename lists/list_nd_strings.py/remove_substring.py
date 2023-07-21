words=['Gfg', 'Gfg is best', 'Geeks', 'Gfg is for Geeks']
new=[]
for index in range(len(words)):
    for index1 in range(len(words)):
        if words[index]==words[index1]:
            continue
        else:
            if words[index] in words[index1]:
                new.append(words[index1])
                break
print(new)