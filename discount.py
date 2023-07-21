marked_price = int(input("enter marked price: "))
if marked_price>10000:
    discount=20
elif marked_price>7000 and marked_price<=10000:
    discount=15
elif marked_price<=7000:
    discount=10
net_amount = marked_price-(discount/100*marked_price)
print(net_amount)


