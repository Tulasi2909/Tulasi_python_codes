name=input("enter: ")
vowels="aeiouAEIOU"
count=0
for i in name:
    if i in vowels:
        count+=1
print(count)
