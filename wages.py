male = "M"
female = "F"
age = int(input("enter age= "))
sex = input("enter sex= ")
if age>=18 and age<30:
    if sex==male:
        print("wage=700")
    else:
        print("wage=750")
elif age>=30 and age<=40:
    if sex==male:
        print("wage=800")
    else:
        print("wage=850")
else:
    print("enter appropriate age")

