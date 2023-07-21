sal = int(input("enter salary: "))
service_years = int(input("time period of service: "))
if service_years>=10:
    bonus = sal*0.10
elif service_years>=6 and service_years<=10:
    bonus = sal*0.08
elif service_years<=6:
    bonus = sal*0.05
print(bonus)
    