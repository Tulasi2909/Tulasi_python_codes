list=[25,64]
# if list[0]>list[1]:
#     print(f"{list[0]} is highest")
# else:
#     print(f"{list[1]} is highest")


min=float('-inf')
for index in range(len(list)):
    if list[index]>min:
        min=list[index]
print(f"highest: {min}")