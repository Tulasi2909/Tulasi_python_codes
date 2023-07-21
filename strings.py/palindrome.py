name=input("name: ")
flag=0
for i in range(len(name)):
    if name[i]==name[len(name)-i-1]:
        flag+=1
        continue
    else:
        print("not palindrome")
        break
if flag==len(name):
    print("palindrome")


    