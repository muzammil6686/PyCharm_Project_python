# [8:49 PM, 9/6/2025] Arman HR Shaikh: 5. ATM program → Take the amount user wants to withdraw and check:
# 1. Is it divisible by 100?
# 2. Does user have enough balance?
# [8:50 PM, 9/6/2025] Arman HR Shaikh: 5. اے ٹی ایم پروگرام → وہ رقم لیں جو صارف واپس لینا چاہتا ہے اور چیک کریں:
# 1. کیا یہ 100 سے تقسیم ہے؟
# 2. کیا صارف کے پاس کافی توازن ہے؟

while True:
    a=int(input("enter withdraw ammount"))
    b= a % 100
    if b == 0:
            print(" ye raha aapka paisa", a )
    else:
        print("invalid paisa")