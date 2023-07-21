# highest nd least frequency characters by changing < > symbols

enter= input("enter: ")
temp=""
hgst=float('inf')
letter=""
for i in enter:
    temp=enter.count(i)

    if temp<hgst:
        hgst=temp
        letter=i



print(letter)
    


    
    