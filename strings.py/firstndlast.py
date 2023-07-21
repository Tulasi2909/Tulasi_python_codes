course1="python programming"
course2="c programming"
char= input("char: ")
count=0
count1=0
while char in course1:
    count+=1
    

while char in course2:
    count1+=1
    break
# for x in course1:
#     for y in course2:
#         if x==char :
#             continue
#         if y==char:
#             continue
   
print(count+count1)
        