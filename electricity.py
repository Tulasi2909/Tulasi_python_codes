units = int(input("number of units: "))
if units<=100:
    print("no charge")
elif units>100 and units<200:
    charge = units*5
    print(f"{charge}")
elif units > 200:
    charge1 = units*10
    print(f"{charge1}")
