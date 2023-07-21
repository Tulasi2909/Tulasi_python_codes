words=['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
sub='Geek'
new_word=''
final=[]
for index in range(len(words)):
    new_word=words[index]
    for i in range(len(new_word)-len(sub)):
        if new_word[i:len(sub)]==sub:
            final.append(new_word)
            break
print(final)