import colorama

def text_color(color="black"):
    if color == "red":
        style = colorama.Fore.RED
    elif color == "green":
        style = colorama.Fore.GREEN
    else:
        style = colorama.Fore.BLACK
    def wrap(func):
        def inner_wrap(*args):
            print(style, end='')
            print(func(*args))
            print(colorama.Style.RESET_ALL, end='')
            return
        return inner_wrap
    return wrap

@text_color()
def neutral_statement():
    return "Neither good nor bad"

@text_color("red")
def bad_statement():
    return "This indicates something bad"

@text_color("green")
def good_statement():
    return "This is a good thing!"

def non_decorated_statement():
    print("This is just to spice things up")

print()
non_decorated_statement()
bad_statement()
neutral_statement()
good_statement()
non_decorated_statement()
print()