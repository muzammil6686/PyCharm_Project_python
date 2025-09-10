
# Write a python code for the following problem
#
# 1. A shopkeeper gives 10% discount on items above ₹1000. Write a program to take price as input and print final price after discount.
#
# Note:You can use algorithm & flow chart for the same



a=int(input("enter price"))
if a > 1000:
    b = a - (a * 10 / 100)
    print("aapka discount 10% ye hai",b)
else:
    print(" no discount")
