A=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']

num=[]
char=[]
for i in range(len(A)):
    a=str(A[i])
    if a.isdigit():
        num.append(A[i])
    else:
        char.append(A[i])
print(num,char)