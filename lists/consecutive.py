num=[1]
# num=[1,2,2,2,6,4,1,1,1]
flag=False
con=[]
for index in range(len(num)-2):
        if num[index]==num[index+1] and num[index]==num[index+2] :
            con.append(num[index])
            continue
        
print(con)
