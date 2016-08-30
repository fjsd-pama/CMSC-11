def characters(given_string):
    """ str -> (list of str)
    Returns the list of every character in the given string
    """
    list_chr = []
    for i in given_string:
        list_chr = list_chr + [i]
    return list_chr

def is_unique(letter, characters):
    """ (str, str) -> bool
    Returns True if the given letter does not appear
    in the second string
    """
    for j in characters:
        if (letter == j):
            return False
    return True

print("This is a test for function is_unique:")
print(is_unique("A", "BBB"))
print(is_unique("B", "BBB"))
print(is_unique("C", "BBC"))

def difference_count(first, second):
    """ (str, str) -> int
    Counts the number of unique characters in the first string
    """
    count = 0
    for i in first:
        if is_unique(i, characters(second)):
            count = count + 1
    return count

    
print("This is a test for function difference_count:")
print(difference_count("AAA", "CCC"))
print(difference_count("BBC", "CCC"))
print(difference_count("CCC", "CCC"))
print(difference_count("CCC", "BBC"))

flames =["F - Friendship", "L- Love", "A- Admiration", "M- Marriage", "E- Enemies", "S- Soulmate"]

def FLAMES(first_name, second_name):
    """ (str, str) -> str
    Determines the fortune of two given names
    """
    count = difference_count(first_name, second_name) + difference_count(second_name, first_name)

    if (count > 0):
        if (count <= 6):
            count = count
        else:
            count = (count % 6)

        return flames[count - 1]

    else:
        return "None"

print("This is a test for function FLAMES:")
print(FLAMES("CAT", "DOG"))
print(FLAMES("AAA", "CCC"))
print(FLAMES("BBC", "CCC"))
print(FLAMES("CCC", "CCC"))
print(FLAMES("jose arniel pama", "enarcisa po"))
