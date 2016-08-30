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

print(reverse_list(["a", "b", "c"])) #['c', 'b', 'a']

def capitalize(given):
    """ (list of str) -> (list of str)
    Capitalizes a list of strings
    """
    for j in range(0, len(given)):
        given[j] = given[j].upper()
    return given

print(capitalize(["A", "B", "C"])) #['A', 'B', 'C']
print(capitalize(["a", "b", "c"])) #['A', 'B', 'C']
print(capitalize(["a", "B", "c"])) #['A', 'B', 'C']

def similar_count(given1, given2):
    """ (list, list) -> int
    Returns the number of identical elements occuring
    at the same points in both lists
    """
    count = 0
    for i in range(0, min(len(given1), len(given2))):
        if (given1[i] == given2[i]):
            count = count + 1
    return count

print(similar_count([1, 2, 4], [4, 5, 4])) #expect 1
print(similar_count([1, 2, 3], [1, 2, 3])) #expect 3
print(similar_count([1, 2, 3], [1, 2, 2])) #expect 2
print(similar_count([1, 2, 3], [5, 6, 7])) #expect 0
