def reverse_list(given):
    """ list -> (list of str)
    Returns the reverse of the given argument
    """
    base = given[0]
    for i in range(0, len(given) // 2):
        given[i] = given[-(i + 1)]
        given[-(i + 1)] = base
        base = given[i + 1]
    return given

print(reverse_list(["a", "b", "c"]))


def identical_elements(list_one, list_two):
    """ (list of any type, list of any type) -> (list of any type)
    Produces the list of identical elements in the two
    given lists
    """
    count = 0
    for i in list_one:
        for j in list_two:
            if (i == j):
                count = count + 1
    return count

print(identical_elements([1, 2, 3], [1, 2, 3]))
print(identical_elements([1, 2, 3], [1, 2, 9]))
print(identical_elements(["a", "n", "o"], ["b", "y", "i"]))
