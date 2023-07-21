start=int(input("start: "))
end=int(input("end: "))
for i in range(start,end):
    if i%2==0:
        evens=i
        print(evens,end=",")

