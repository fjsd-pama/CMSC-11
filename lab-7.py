# number 1
# Create a function that returns the cube of the integer's initial value.

# stub
#def cubed(x):
#    """ (int) -> int
#
#    Returns the given integer raised to the power of 3.
#    """
#    return 0

# template
#def cubed(x):
#    """ (int) -> int
#
#    Returns the given integer raised to the power of 3.
#    """
#    return ... x

def cubed(x):
    """ (integer) -> integer

    Returns the given integer raised to the power of 3.
    """
    return (x ** 3)

#examples
cubed(-100) == (-100) ** 3
cubed(100) == (100) ** 3
cubed(8.9) == (8.9) ** 3
cubed(-8.9) == (-8.9) ** 3
cubed(0) == 0


# number 2
# Create a function that determines whether or not
# a given number is an even number.

# stub
#def is_even(y):
#    """ (num) -> bool
#
#    Returns True if the given number is even, else False.
#    """
#    return 0

# template
#def is_even(y):
#    """ (num) -> bool
#
#    Returns True if the given number is even, else False.
#    """
#    return ... y

def is_even(y):
    """ (num) -> bool

    Returns True if the given number is even, else False.
    """
    return (num % 2) == 0

#examples
is_even(2) #True
is_even(-2) #True
is_even(0) #True
is_even(1) #False
is_even(-1) #False


# number 3
# Create a function that removes the first character of an input.

# stub
#def string_rest(x):
#    """ (str) -> str
#
#    Produces a string like the given one with the first character removed.
#    """
#    return 0

# template
#def string_rest(x):
#    """ (str) -> str
#
#    Produces a string like the given one with the first character removed.
#    """
#    return ... x
>>> def string_rest(x):
    """ (str) -> str

    Produces a string like the given one with the first character removed.
    """
    return x[1:]

#examples
string_rest(" ") == ""
string_rest(0) #error
string_rest("123") == "23"
string_rest("str") == "tr"
string_rest("") == ""


# number 4
# Create a function that removes the last character of an input.

# stub
#def string_remove_last(y):
#    """ (str) -> str
#
#    Produces a string like the given one with the last character removed.
#    """
#    return 0

# template
#def string_remove_last(y):
#    """ (str) -> str
#
#    Produces a string like the given one with the last character removed.
#    """
#    return ... y
>>> def string_remove_last(y):
    """ (str) -> str

    Produces a string like the given one with the last character removed.
    """
    return y[:-1]

string_remove_last("") == ""[:-1]
string_remove_last(" ") == " "[:-1]
string_remove_last(0) #error
string_remove_last("str") == "st"
string_remove_last("123") == "12"

