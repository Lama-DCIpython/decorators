# functions can take fixed number of  positional arguments (list of arguments) they are ordered e.g

def greeting(first_name, Last_name):
    print(f"Hallo {first_name} , {Last_name}")


# they can have also fixed number of named arguments (dictionary of arguments) they are not ordered e.g:

def greeting2(first_name="Lama", last_name="Osman"):
    print(f"Hallo {first_name} , {last_name}")

# they can take flexible number of positional arguments using *args

# and they can have a flexible number of named arguments (using **kwargs)


def greeting3(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    if "Country" in kwargs.keys():
        print(kwargs["Country"])


if __name__ == '__main__':
    country= input("Enter your country: ")
    greeting3("Lama", "Osman", 18, "some-street", "Berlin", Country=country)
