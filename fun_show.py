
def user_input_list():
    record=[]
    name=input("enter your name :"),
    age=input("enter your age :"),
    password=input("enter your password")
    data={"name":name,
        "age":age,
        "password":password
    }
    record.append(data)
    while True:
        user = input("aap kya dekhna chahte ho : (name ,age ,password)")
        if user in data:
            print(f"aapka {user} hai : {data[user]}")
        else:
            print("aap ne koi option chose nahi kiya ")

        exit=input("kya aapko kuch or dekhna hai kya (yes,no)")
        if exit.lower() == "no":
            print("aapka bahot shukriya :")
            break



