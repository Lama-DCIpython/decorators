" click on an object and open its documentation in a new window "
"""These lines are trying to implement some explanations from the documentation of "class" """
""" To read about decorators see here:
https://www.geeksforgeeks.org/decorators-in-python/#:~:text=Decorators%20are%20very%20powerful%20and%20useful%20tool%20in,behavior%20of%20wrapped%20function%2C%20without%20permanently%20modifying%20it.

and here:

https://www.typescriptlang.org/docs/handbook/decorators.html#:~:text=A%20Class%20Decorator%20is%20declared%20just%20before%20a,ambient%20context%20%28such%20as%20on%20a%20declare%20class%29.

to read about a multiple inheritance problem see
https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way

And to read about meta classes in python see:
https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
"""

"""
def f1(arg):
    print(1, "f1 is executed")
    return 1


def f2(arg):
    print("f2executed")


@f1
@f2
class A:
    print("V1class a entered")


class B:
    print("V2 class b entered")


B = f1(f2(B))
"""
# decorators from geeksforgeeks source

# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# # calling the function
# function_to_be_used()

"""   def __init__(self):
        print("Entering A")
        super(A, self).__init__()
        print("Leaving A")"""

"""
class B:
    def __init__(self):
        print("Entering B")
        super(B, self).__init__()
        print("Leaving B")


class C(A, B):
    def __init__(self):
        print("Entering C")
        #super().__init__()

        A.__init__(self)
        B.__init__(self) #uncomment one of them to see what will happen
        print("Leaving C")"""

if __name__ == '__main__':
    # y = []

    """print(type(A))
    print(type(B))"""



    # calling the function
    function_to_be_used()
