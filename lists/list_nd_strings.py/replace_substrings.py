list1= ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
list2=[['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
new_list2=""
new2=""
new=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list2[j][0] in list1[i]:
            # list1[i]=list1[i][i:len(list2[j][0])].replace(list1[i][i:len(list2[j][0])],list2[j][1])+list1[i][(len(list2[j][0])+1):(len(list1[i]))+1]
            # list1[i]=list1[i].replace(list1[i],list2[j][1])
            list1[i]=list1[i].replace(list2[j][0],list2[j][1])
            
    new.append(list1[i])
            
print(new)

            


    
            

