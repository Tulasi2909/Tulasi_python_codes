words=['Gfg is Gfg1', 'Gfg is for geeks', 'I love G4G']
k=input("enter k: ")
new=""
new_words=""
final=[]
for word in range(len(words)):
    new=words[word]
    new_words=new.split()
    for index in range(len(new_words)):
        if new_words[index][0]==k:
        # if k in new_words[index]:
            final.append(new_words[index])
print(final,end=" ")




        
            
                
                
        