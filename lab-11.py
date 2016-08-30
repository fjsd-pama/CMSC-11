def min_of_2(x, y):
    """ (number, number) -> number

    Returns the smaller number
    """
    if (x < y):
        return x
    else:
        return y

#stub
#def shortest_name(x):
#    """ (list of strings) -> str
#
#    Returns the shortest name in a
#    list of names
#    """
#    return ""

#template
#def shortest_name(x):
#    """ (list of strings) -> str
#
#    Returns the shortest name in a
#    list of names
#    """
#    for i in x:
#        ...
#    return ...

def shortest_name(x):
    """ (list of strings) -> str

    Returns the shortest name in a
    list of names
    """
    for i in x:
        min = min_of_2(x[0], len(i))
    return min
        
        
print(shortest_name("Papa, Ate"))





def num_words_in(word):
    """ str -> number

    Returns the number of words in a
    given string
    """
    for i in word:
        ...
    return ...

def LCM(a, b):
    """ (int, int) -> number

    Determines the least common multiple
    a given pair of integers
    """
    for i in b:
        ...
    return ...

def is_smallest_to_highest(sth):
    """ (list of numbers) -> bool

    Determines if a list of numbers
    is sorted from smallest to largest
    values
    """
    for i in sth:
        for
    return 
def list_of_first_cubes(n):
    """ (int) -> (list of ints)

    Creates a list of the first n cubes,
    assuming 1 is the first cube
    """
    first_cubes = []
    for i in range(1, (n + 1)):
        for ch in i:
            cube = first_cubes + [ch ** 3]
    return cube

list_of_first_cubes(3)
list_of_first_cubes(4)

























