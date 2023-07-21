course= "python programming"
new1=""
new2=""
for index in range(len(course)):
    if index <= len(course)/2:
        new1+=course[index]
    if index>len(course)/2:
        new2+=course[index]

print(new1.upper()+new2)
