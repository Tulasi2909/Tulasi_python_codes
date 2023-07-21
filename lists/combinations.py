num=[1,2,3]
index=0

while index<3:
    third=index+2
    if third>=3:
        third=third-3
    second = third-1
    print(str(num[index])+" "+str(num[second])+" "+str(num[third]))
    print(str(num[index])+" "+str(num[third])+" "+str(num[second]))
    index+=1
    
# index =1

# 1 1+1  1+2
# 1  2   0
# 2 2+1 2+2
# 2 0   1