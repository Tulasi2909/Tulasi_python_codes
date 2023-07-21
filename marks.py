maths = int(input("maths marks: "))
english = int(input("english marks: "))
science = int(input("science marks: "))
social_studies = int(input("social studies marks: "))
if maths>80 and english>80 and science>80 and social_studies>80:
    print("science stream")
elif english>80 and science>50:
    print("commerce stream")
elif english>80 and social_studies>80:
    print("humanities")
