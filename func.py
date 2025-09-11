def program():
    l=[
        name:=input("enter your name"),
        age:=input("enter your age"),
        password:=input("enter your password"),
    ]

    while True:
        a=input("app kya dekhna chahte hai : (name,age,password)")
        if a in l:
            print(f"aapka {a} hai:{l[a]}")
        else:
            print("galat choice di hai ")

            n=input("do you want to see any thing else ? (yes/no)")
        if n.lower() == "no":
            print("program exit ho gaya :")
            break


