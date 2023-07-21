# creating list by entering

# num=[]
# n=int(input("enter range: "))
# for i in range(n):
#     a=input("enter:")
#     num.append(a)
# print(num)

num=[15,23,2,48,65]
swap1=int(input("enter: "))
swap2=int(input("enter: "))
new=[]
new=num[swap1]
num[swap1]=num[swap2]
num[swap2]=new
print(num)