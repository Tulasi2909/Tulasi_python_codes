units = int(input("enter units: "))
if units<=100:
    print("free charge")
elif units>100 and units<=300:
    bill = (units-100)*2
    print(f"total bill= {bill}")
elif units>300:
    bill = 400 + (units-200)*5
    print(f"total bill= {bill}")