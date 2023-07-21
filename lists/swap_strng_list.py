words = ['GGg', 'is', 'best', 'for', 'Geeks']
new=[]
for index in range(len(words)):
        words[index]=words[index].replace("G","#")
        words[index]=words[index].replace("e","$")
        words[index]=words[index].replace("#","e")
        words[index]=words[index].replace("$","G")
        new.append(words[index])
print(new)
