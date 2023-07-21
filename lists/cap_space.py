words=['gfgBest', 'forGeeks', 'andComputerScience']
new=""
new_word=""
final=[]
a=""
for word in words:
    new=word
    for index in new:
        if index.isupper():
            new=new.replace(index," "+index)
    final.append(new)
print(final)
        
       

# # Python3 code to demonstrate working of
# # Add Space between Potential Words

# # initializing list
# test_list = ["gfgBest", "forGeeks", "andComputerScience"]

# # printing original list
# print("The original list : " + str(test_list))

# res = []
# for i in test_list:
# 	for j in i:
# 		if(j.isupper()):
# 			i = i.replace(j, " "+j)
# 	res.append(i)

# # printing result
# print("The space added list of strings : " + str(res))
