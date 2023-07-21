msg= input("enter: ")
new= msg.split()
print(new)
length= int(input("enter length: "))
list=[]
# for index in range(len(new)):
#     if index>length:
#         print(new[index])
for i in new:
    if len(i)>length:
        list.append(i)
print(list)