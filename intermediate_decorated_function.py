# This is an intermediate case for decorators.
# We want to have access to control the execution
# of the decorated function

def add_description(func):  # We're passing the decorated function into here
    def wrap(*args):            # The args of the decorated function are passed into here, and this is a catch-all to accept them
                                # We could also accept the specific args `def wrap(a,b):`
                                # We must call the decorated function somewhere in this function
        print(f"The result is {func(args[0], args[1]+5)}") # <--- I'm really sneaky
        return                  # Normally, we would return the decorated function, but we're already calling it
    return wrap             # We must return the wrapper function

@add_description
def add(a, b):
    return(a+b)

add(1,5)