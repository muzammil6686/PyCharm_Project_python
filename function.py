def mycalc():
    print("1 +")
    print("2 -")
    print("3 *")
    print("4 /")
    n=input("chose one option :")
    a=int(input("chose one number :"))
    b=int(input("chose second number :"))

    if n == 1:
        print(a+b)
    elif n == 2:
        print(a-b)
    elif n == 3:
        print(a*b)
    elif n == 4:
        print(a/b)
    else:
        print("your not chose any option")
mycalc()
