name=input("name: ")
i=int(input("enter i to remove character: "))
new=""
for x in range(len(name)):
    if x!=i:
        new+=name[x]
print(new)


