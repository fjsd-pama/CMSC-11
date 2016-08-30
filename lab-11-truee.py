##def shortest_name(names_list):
##    """ (list of strings) -> str
##    Returns the shortest name within a given list
##    """
##    return ""
##
##def shortest_name(names_list):
##    """ (list of strings) -> str
##    Returns the shortest name within a given list
##    """
##    for name in names_list:
##        ...
##    return ...

def shortest_name(names_list):
    """ (list of strings) -> str
    Returns the shortest name within a given list
    """
    name = names_list[0]
    for sth in names_list:
        if (len(sth) < len(name)):
            return sth
    return name


print("This is a test for function shortest_name:")
print("Joe" == shortest_name(["Joe", "Pama"]))
print("Joe" == shortest_name(["Pama", "Joe"]))
print("An" == shortest_name(["Pama", "An", "Joe"]))
print("Ba" == shortest_name(["Ba", "An", "Cu"]))



##def is_letter(x):
##    """ str -> bool
##    Returns True when the given argument is a letter, otherwise returns False
##    """
##    return False
##
##def is_letter(x):
##    """ str -> bool
##    Returns True when the given argument is a letter, otherwise returns False
##    """
##    return ... x

alph_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
alph_2 = ["n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alph_3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
alph_4 = ["N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet = alph_1 + alph_2 + alph_3 + alph_4

def is_letter(x):
    """ str -> bool
    Returns True when the given argument is a letter, otherwise returns False
    """
    return (x in alphabet)

print("This is a test for function is_letter:")
print(False == is_letter(98))
print(False == is_letter("1"))
print(True == is_letter("y"))



##def word_count(string):
##    """ str -> int
##    Takes a string and returns the number of words in that string
##
##    NOTE: Words may be separated by multiple spaces.
##    But the string is guaranteed not to start or end with a space.
##    """
##    return 0
##
##def word_count(string):
##    """ str -> int
##    Takes a string and returns the number of words in that string
##
##    NOTE: Words may be separated by multiple spaces.
##    But the string is guaranteed not to start or end with a space.
##    """
##    count = 0
##    prev = " "
##    for var in string:
##        ...
##    return ...

def word_count(string):
    """ str -> int
    Takes a string and returns the number of words in that string

    NOTE: Words may be separated by multiple spaces.
    But the string is guaranteed not to start or end with a space.
    """
    count = 0
    prev = " "
    for var in string:
        if (is_letter(var) and (prev == " ")):
            count = count + 1
        prev = var
    return count

print("This is a test for function word_count:")
print(5 == word_count("this is       a sample      string"))   #expect 5
print(3 == word_count("never give up"))

##def LCM(a, b):
##    """ (int, int) -> int
##    Returns the least common multiple of a given pair of integers
##    """
##    return 0
##
##def LCM(a, b):
##    """ (int, int) -> int
##    Returns the least common multiple of a given pair of integers
##    """
##    result = (a * b)
##    for val in range(a, (a * b)):
##        ....
##    return ...

def LCM(a, b):
    """ (int, int) -> int
    Returns the least common multiple of a given pair of integers
    """
    result = (a * b)
    for val in range(a, (a * b)):
        if ((val % a == 0) or (val % b == 0)) and (val <= result):
            result = val
    return result


print("This is a test for function LCM:")
print(2 == LCM(2, 1))
print(4 == LCM(4, 2))
print(5 == LCM(5, 5))
print(0 == LCM(9, 0))
print(72 == LCM(72, 8))
print(LCM(4, 6))

##def is_smallest_to_highest(nums_list):
##    """ (list of numbers) -> bool
##    Determines if a list of numbers is sorted from
##    smallest to largest
##    """
##    return False
##
##def is_smallest_to_highest(nums_list):
##    """ (list of numbers) -> bool
##    Determines if a list of numbers is sorted from
##    smallest to largest
##    """
##    for num in nums_list:
##        ...
##    return ...

def is_smallest_to_highest(nums_list):
    """ (list of numbers) -> bool
    Determines if a list of numbers is sorted from
    smallest to largest
    """
    for num in nums_list:
        for sth in range(1, len(nums_list) + 1):
            if (num < nums_list[sth]):
                return True
            return False


print("This is a test for function is_smallest_to_highest:")
print(True == is_smallest_to_highest([1, 2, 3]))
print(True == is_smallest_to_highest([1, 2, 4]))
print(False == is_smallest_to_highest([2, 2, 1]))
print(False == is_smallest_to_highest([6, 2, 3, 67]))
print(True == is_smallest_to_highest([6, 8, 67, 67]))
print(False == is_smallest_to_highest([9, 8, 1, 56]))

##def first_n_cubes(n):
##    """ int -> (list of integers)
##
##    Creates a function that creates a list of the first n cubes
##    given a positive integer n
##    """
##    result []
##
##def first_n_cubes(n):
##    """ int -> (list of integers)
##
##    Creates a function that creates a list of the first n cubes
##    given a positive integer n
##    """
##    output = []
##    for i in range(1, (n + 1)):
##        ...
##    return ...

def first_n_cubes(n):
    """ int -> (list of integers)

    Creates a function that creates a list of the first n cubes
    given a positive integer n
    """
    output = []
    for i in range(1, (n + 1)):
        output = output + [i ** 3]
    return output

print("This is a test for function first_n_cubes:")
print([1, 8, 27, 64] == first_n_cubes(4))

