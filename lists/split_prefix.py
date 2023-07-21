words=['geeksforgeeks', 'best', 'geeks', 'and', 'geeks', 'love']
# key_word=input("enter key word: ")
new_word=[]
new=[]
for word in range(len(words)-1):
    new_word=(words[word]+" "+words[word+1])
    new_word.split()
    print(new_word)
    if new_word not in words:
        new.append(new_word)
print(new)


  
  
  
  
  
  
  
  
  
  
    # if key_word in words[word]:
    #     new_word.append(words[word])
    # if key_word not in words[word+1]:
    #     new_word.append(words[word+1])
    #     print(new_word)
    #     break