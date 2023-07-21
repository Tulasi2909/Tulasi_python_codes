words=['geekforgeeks', 'best','is', 'for', 'geeks']
k=int(input("enter kth value: "))
new=0
new_word=""
for index in range(len(words)):
    if new+len(words[index])>=k:
        new_word=words[index]
        print(new_word[k-new-1],k-new-1)
        break
    new+=len(words[index])
print(new_word)