n1=input("enter: ")
n2=input("enter: ")

new1=""
new2=""
add1=""
add2=""
final=""

# add=n2[:2]+n1[2:]+" "+n1[:2]+n2[2:]
# print(add)
for index in range(2):
    new1+=n1[index]
    new2+=n2[index]
for index in range(2,len(n1)):
    add1+=n1[index]
for index in range(2,len(n2)):
    add2+=n2[index]
final=new2+add1+" "+new1+add2

print(final)




