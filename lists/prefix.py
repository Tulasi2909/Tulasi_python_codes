words=['gfgisbest', 'gegfgeks', 'gfgfreak', 'gfgCS', 'Gcourses']
k=input("enter prefix: ")
prefix=[]
for index in range(len(words)):
    if k in words[index][0:len(k)]:
        prefix.append(words[index])
print(prefix)
        
