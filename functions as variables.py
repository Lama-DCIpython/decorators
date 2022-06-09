def greeting():
    print("Hi")


def greeting1(basic_greeting):
    print(f"{basic_greeting}-This is greeting1")


def greeting2(basic_greeting):
    print(f"{basic_greeting}-This is greeting2")


def greeting3(greeting_fun):
    greeting_fun("Hi")


def greeting4(greeting_fun, name):
    greeting_fun(f"Hi {name}")


if __name__ == '__main__':
    # calling the function
    greeting()
    # using the function like a variable (functions are objects)
    nice_greeting = greeting
    # calling the new function
    nice_greeting()
    # pass greeting1 as an argument to greeting3
    greeting3(greeting1)
    # pass greeting1 as an argument to greeting4
    greeting4(greeting1,"Lama")
