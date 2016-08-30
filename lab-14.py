def YearsToReachTarget(current_balance, target_balance, interest_rate):
    """ (num, num, float) -> int
    Returns the number of years a starting bank account
    balance will reach a target balance given an
    interest rate
    """
    year = 0
    while (current_balance < target_balance):
        current_balance = current_balance + (current_balance * interest_rate)
        year = year + 1
    return year

print(YearsToReachTarget(400, 450, 0.02)) #expect 6

def is_even(number):
    """ (number) -> bool
    Returns True is the given number is even,
    otherwise returns False
    """
    if (number % 2 == 0):
        return True
    else:
        return False

def Syracuse_sequence(x):
    """ int -> (list of int)
    Returns a list containing the Syracuse sequence
    for a starting value

    e.g. The Syracuse sequence starting with 5 is:
    5, 16, 8, 4, 2, 1
    """
    base = x
    sequence = [base]
    while (base != 1):
        if (is_even(base)):
            base = int(base / 2)
        else:
            base = int((3 * base) + 1)
        sequence = sequence + [base]
    return sequence

print(Syracuse_sequence(5)) #expect [5, 16, 8, 4, 2, 1]

def decimal_to_binary(number):
    """ int -> int
    Converts a decimal number to its binary digits
    """
    decimal = number
    remainder = decimal % 2
    binary = str(remainder)
    while (decimal > 1):
        decimal = decimal // 2
        remainder = decimal % 2
        binary = str(remainder) + binary
    return "".join(binary)

print(decimal_to_binary(156)) #expect 10011100


