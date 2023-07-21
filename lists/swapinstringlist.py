list=['abc','cae','bce','dat']
new_list=[]
for index in range(len(list)):
    if "a" in list[index]:
        new_list.append(list[index].replace("a","z"))
    else:
        new_list.append(list[index])
print(new_list)
