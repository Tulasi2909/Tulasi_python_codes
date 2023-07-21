enter= input("enter: ")
count=0
for i in enter:
    count=enter.count(i)
    if count%2!=0:
        print(f"{i}:{count}")
