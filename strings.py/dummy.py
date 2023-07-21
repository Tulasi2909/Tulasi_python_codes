# name=input("enter: ")
# count=0
# for index in range(len(name)):
#     if index<len(name):
#         count+=1
# print(f"length of string is {count}")

# name=input("enter: ")
# new=""
# for index in range(len(name)):
#     if index%2==0:
#     # if name[index]!=" ":
#         new+=name[index]
# print(new)

# name=input("enter: ")
# new=""
# for index in range(len(name)):
#     if index<(len(name)/2):
#         new+=name[index].upper()
#     else:
#         new+=name[index]
# print(new)


# name= input("enter: ")
# flag1=0
# flag2=0
# for i in name:
#     if i.isalpha():
#         flag1+=1
#     elif i.isnumeric():
#         flag2+=1
# if flag1>=1 and flag2>=1:
#     print(True)
# else:
#     print(False)


# name=input("enter: ")
# name1= name.lower()
# if "a" in name1 and "e" in name1 and "i" in name1 and "o" in name1 and "u" in name1:
#     print("present all vowels")
# else:
#     print("not present")


# name=input("enter: ")
# first= set(name)
# vowels="aeiouAEIOU"
# second= set(vowels)
# count=0
# for i in first:
#     if i in second:
#         count+=1
# print(count)



# name1= input("enter: ")
# first= set(name1)
# name2= input("enter: ")
# second= set(name2)
# matching=first&second
# print(matching)
# print(len(matching))


# name=input("enter: ")
# new=""
# for i in name:
#     if i not in new:
#         new+=i
# print(new)


# name=input("enter: ")
# temp=""
# letter=""
# hgst=float('inf')
# for i in name:
#     temp=name.count(i)
#     if temp<hgst:
#         hgst=temp
#         letter=i
# print(letter)


name=input("enter: ")
temp=""
for i in name:
    temp=name.count(i)
    if temp%2!=0:
        print(i)
    
