# This is an advanced example for decorators. Not only can we access information
# about the function and control its execution, but the decorator can take arguments
# so that it can be reused for multiple functions

from random import choice, randint

def add_description(operation = ""): # Contains details about the decorator parameters
    def wrap(func):                     # Contains the original function
        def inner_wrap(a,b):                # Contains the original function's arguments
            influence = choice(["angel on shoulder","devil on shoulder"])
            if influence == "devil on shoulder":
                modifier = randint(1,10)
            else:
                modifier = 0
                                            # We can call the original function, with arguments
                                            # (even customized ones), in here
            print(f"The {operation} of {a} and {b} is {func(a,b+modifier)}")
            return                          # Since we call the function inside the inner wrap
                                            # a blank return statement is fine
        return inner_wrap               # wrap() returns inner_wrap()
    return wrap                     # The decorator returns the wrap

@add_description(operation = "sum")
def add(a, b):
    return(a+b)

@add_description(operation="difference")
def subtract(a,b):
    return(a-b)

add(1,5)
subtract(6,3)