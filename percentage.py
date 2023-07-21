working_days = int(input("total number of working days: "))
absent_days = int(input("total number of days absent: "))
percentage = (working_days-absent_days)/working_days*100
if percentage <=75:
    print(format(percentage, ".2f") +  " student will not be able to sit in the exam")
else :
    print(format(percentage, ".2f") +  " student will  be able to sit in the exam")
    
