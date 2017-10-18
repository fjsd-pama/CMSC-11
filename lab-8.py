# number 1
# template
# def camera_switch_on(lux, temp):
# """(num, num) -> bool
#
# Determine whether to turn on the camera given the light level and
# the temperature
# """
# return 0


light_level = 0.01
freezing_pt = 0

# template
# def camera_switch_on(lux, temp):
# """(num, num) -> bool
#
# Determine whether to turn on the camera given the light level and
# the temperature
# """
# return... lux temp light_level freezing_pt

def camera_switch_on(lux, temp):
    """(num, num) -> bool

    Determines whether to turn on the camera given the light
    level and the temperature
    """
    return (lux < light_level) != (temp > freezing_pt)

#example
camera_switch_on(0, 0)#True
camera_switch_on(-1, 0) #True
camera_switch_on(0.01, 0) #True
camera_switch_on(0.2, 0) #False
camera_switch_on(-1, 1) #False
camera_switch_on(0.2, -2) #False
camera_switch_on(0.2, 2) #True

#stub
#def max_of_2(x, y):
# """ (int, int) -> int
# Accepts 2 integers and returns the value of the
# largest integer
# """
# return 0

#template
#def max_of_2(x, y):
# """ (int, int) -> int
# Accepts 2 integers and returns the value of the
# largest integer
# """
# return ... x y

def max_of_2(x, y):
    """ (int, int) -> int
    Accepts 2 integers and returns the value of the
    largest integer
    """
    if (x > y):
        return x
    else:
        return y

#examples
    max_of_2(2, 2) #2
    max_of_2(2, 1) #2
    max_of_2(1, 2) #1


#stub
#def max_of_3(x, y, z):
# """ (int, int, int) -> int
# Accepts 3 integers and returns the value of the
# largest integer
# """
# return 0

#template
#def max_of_3(x, y, z):
# """ (int, int, int) -> int
# Accepts 3 integers and returns the value of the
# largest integer
# """
# return ... x y z

def max_of_3(x, y, z):
    """ (int, int, int) -> int
    Accepts 3 integers and returns the value of the
    largest integer
    """
    return max_of_2(max_of_2(x, y), z)

#examples
max_of_3(3, 2, 1) # expect 3
max_of_3(3, 3, 1) # expect 3
max_of_3(3, 2, 3) # expect 3
max_of_3(2, 3, 1) # expect 3
max_of_3(3, 3, 1) # expect 3
max_of_3(2, 3, 3) # expect 3
max_of_3(1, 2, 3) # expect 3
max_of_3(1, 3, 3) # expect 3
max_of_3(3, 3, 3) # expect 3



age_constant = 45
BMI_constant = 22.0

#stub #def is_at_risk(age, BMI):
# """ (num, num) -> str
# Determines if someone is at risk for heart disease,
# given his age and BMI
# """
# return ""

#template
#def is_at_risk(age, BMI):
# """ (num, num) -> str
# Determines if someone is at risk for heart disease,
# given his age and BMI
# """
# return ... age BMI age_constant BMI_constant

def risk_level(age, BMI):
    """ (num, num) -> str
    Determines if someone is at risk for heart disease,
    given his age and BMI
    """
    if (BMI < BMI_constant and age < age_constant):
	    return "Low"
    elif (BMI >= BMI_constant and age < age_constant) or (BMI < BMI_constant and age >= age_constant):
	    return "Medium"
    else:
	    return "High"

#examples
risk_level(44, 21) # expect "low"
risk_level(44, 22) # expect "medium"
risk_level(44, 23) # expect "medium"
risk_level(45, 21) # expect "medium"
risk_level(45, 22) # expect "high"
risk_level(45, 23) # expect "high"
risk_level(46, 21) # expect "medium"
risk_level(46, 22) # expect "high"
risk_level(46, 23) # expect "high"


#stub
#def letter_grade(letter):
# """ (str) -> str
# Returns the next highest letter grade
# """
# return ""

#template
#def letter_grade(letter):
# """ (str) -> str
# Returns the next highest letter grade
# """
# return ... letter


def letter_grade(letter):
    """ (str) -> str

    Returns the next highest letter grade
    """
    if (letter == "A") or (letter == "B"):
        return "A"
    else:
        return "B"

#examples
letter_grade("A") == "A"
letter_grade("B") == "A"
letter_grade("C") == "B"


string_length_constant = 5
#stub
#def length_of_string(string):
# """ (str) -> num
#
# Returns the length of the given string
# """
# return 0

#template
#def length_of_string(string):
# """ (str) -> num
#
# Returns the length of the given string
# """
# return ... string

def length_of_string(string):
    """ (str) -> num

    Returns the length of the given string
    """
    return len(string)

#examples
length_of_string("String") #6
length_of_string("") #0
length_of_string(" ") #1
length_of_string("Yes") #3

#stub
#def length_is_less_than_five(string):
# """ (str) -> bool
#
# Checks if the length of a given string is less
# than 5
# """
# return 0

#template
#def length_is_less_than_five(string):
# """ (str) -> bool
#
# Checks if the length of a given string is less
# than 5
# """
# return ... string string_length_constant


def length_is_less_than_five(string):
    """ (str) -> bool

    Checks if the length of a given string is less than 5
    """
    return length_of_string(string) <= string_length_constant

#examples
length_is_less_than_five("String") #False
length_is_less_than_five("") #True
length_is_less_than_five("Mommy") #True



