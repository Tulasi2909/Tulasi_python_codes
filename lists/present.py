list=[1,5,6,7,3,'a']
number=int(input("enter number: "))
for i in range(len(list)):
    if number==list[i]:
        print("entered number is present in the list")
        break
else:
    print("not present")


    

