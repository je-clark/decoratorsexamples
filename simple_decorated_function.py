# This is a very simple decorator case. We just preface the actual function with 
# a little message.

def add_description(func):  # We must accept the decorated function as an argument
                                # We can access meta-info about the function
    print(f'The result of function "{func.__name__}" is')
    return func                 # We must return the decorated function

@add_description
def add(a, b):
    return(a+b)

print(add(1,3))
#add(1,6)