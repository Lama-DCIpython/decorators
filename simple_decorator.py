def simple_decorator(func):
    def wrapper():
        print("Something before calling greeting")
        func()
        print("something after calling greeting")
        print("---------------")
    return wrapper

def simple_decorator1(func):
    def wrapper():
        # print("Something before calling greeting")
        greeting_string = func()
        greeting_string = f"{greeting_string}, welcome to DCI"
        return greeting_string
        # print("something after calling greeting")
    return wrapper


@simple_decorator
def greeting():
    # return "Hi"
    print("Hi")

# alternative to the decorator : greeting = simple_decorator(greeting) the decorator is a function that takes a
# function as an argument but instead of passing the argument function(func) to the decorator after definging it ,
# we can pass it directly while defining it as we have seen above


@simple_decorator
def greeting2():
    print("Hi Lama")


@simple_decorator1
def greeting1():
    return "Hi"


if __name__ == '__main__':
    greeting()
    greeting2()
    value = greeting1()
    print(value)