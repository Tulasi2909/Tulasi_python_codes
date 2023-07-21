letters=['G','J','O','V','G','X']
letter=input("enter letter: ")
new=[]
for index in range(len(letters)):
    if letters[index]!=letter:
        new.append("*")
    else:
        new.append(letter)
print(new)