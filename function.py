

def greet_with_name(*args):
    print(type(args))
    print(f"assalamu alaikum :{args[0]}")
    print(f" aapki age ye hai :{args[1]}")


def user():
    l=[20,10,300]
    name=input("enter your name")
    age=input("enter your age")
    a=input("enter you address")
    m=name,age,a
    l.append(m)
    print(l)


