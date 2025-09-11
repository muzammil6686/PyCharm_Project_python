def user_data_info():
    #step 1 user se input lena
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    #sabko ek list me store karna hai
    user_list =[name , age , address , password]


    while True: #loop chalega jab tak user exit nahi karta
        #step 2 choice lena
        choice = input("tumhe kya dekhna hai ? (name ,age ,address ,password )")
        if choice in user_list:
            index = user_list.index(choice)  #choice ka index nikalna
            print(f"tumhara {choice} hai:{user_list[index]}")
        else:
            print("galat choice di hai.")
            #step 3 : exit ka option
            again = input("kya tum kch or dekhna chahta ho ? (yes/no):")
            if again.lower() == "no":
                print("program exit ho gaya :")
                break


