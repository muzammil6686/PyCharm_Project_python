
# 2. take the cost of 3 items as input and print the total bill with GST = 18%.
#
# ان پٹ کے طور پر 3 آئٹمز کی لاگت لیں اور جی ایس ٹی = 18 ٪ کے ساتھ کل بل پرنٹ کریں۔


a=int(input("1 item price "))
b=int(input("2 item price "))
c=int(input("3 item price "))
d=a+b+c
m = d + (d*18/100)
print(m)