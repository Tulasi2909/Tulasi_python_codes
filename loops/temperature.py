# temp_value=int(input("enter temperature: "))
# temp = input("F or C : ")
# if temp=="F":
#     c=float((temp_value-32)*(5/9))
#     print(c)
# elif temp=="C":
#     f=float((temp_value*(9/5))+32)
#     print(f)
    

while True:
    temp = input("enter temperature: ")

    if "F" in temp:
        temp=int(temp[0:-1])
        c=float((temp-32)*(5/9))
        print(f"{c}C")
        break
    elif "C" in temp:
        temp=int(temp[0:-1])
        f=float((temp*(9/5))+32)
        print(f"{f}F")
        break
    else:
        print("enter correct temp")


