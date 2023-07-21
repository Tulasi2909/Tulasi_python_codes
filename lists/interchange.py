num=[12,5,36,4,2]
new=[]
new=num[0]
num[0]=num[-1]
num[-1]=new
print(num)