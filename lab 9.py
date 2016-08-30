#stub
#def max_of_2(x, y):
#    """ (int, int) -> int
	
#    Accepts 2 integers and returns the value of the 	    
#    largest integer
#    """
#    return 0


#template
#def max_of_2(x, y):
#    """ (int, int) -> int
	
#    Accepts 2 integers and returns the value of the 	    
#    largest integer
#    """
#    return ... x y

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
max_of_2(1, 2) #2


#stub
#def max_of_3(x, y, z):
#    """ (int, int, int) -> int

#    Accepts 3 integers and returns the value of the
#    largest integer
#    """
#    return 0

#def max_of_3(x, y, z):
#    """ (int, int, int) -> int

#    Accepts 3 integers and returns the value of the
#    largest integer
#    """
#    return ... x y z

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






quota_purchase = 1000
discount_value = 0.08

#stub
#def discount(purchase_amount):
#    """ (num) -> num

#    Calculates the discount given the amount of purchase
#    """
#    return 0

#template
#def discount(purchase_amount):
#    """ (num) -> num

#    Calculates the discount given the amount of purchase
#    """
#    return ... purchase_amount

def discount(purchase_amount):
    """ (num) -> num

    Calculates the discount given the amount paid
    """
    return (purchase_amount * discount_value)


#example
discount(1500) #120


#stub
#def total_cost(purchase_amount):
#    """ (num) -> num

#    Calculates the total cost of to be paid, given the amount
#    of purchase
#    """
#    return 0

#template
#def total_cost(purchase_amount):
#    """ (num) -> num

#    Calculates the total cost of to be paid, given the amount
#    of purchase
#    """
#    return ... purchase_amount quota_price discount_value discount(purchase_amount)

def total_cost(purchase_amount):
    """ (num) -> num

    Calculates the total cost to be paid, given amount of purchase
    """
    if (purchase_amount > quota_purchase):
        return purchase_amount - discount(purchase_amount)
    else:
        return purchase_amount


#examples
total_cost(1300) #1196
total_cost(1000) #1000

#stub
#def change(purchase_amount, amount_paid):
#    """ (num, num) -> num
#
#    Determines the change to be returned given the total cost of
#    purchase and the amount paid
#    """
#    return 0

#template
#def change(purchase_amount, amount_paid):
#    """ (num, num) -> num
#
#    Determines the change to be returned given the total cost of
#    purchase and the amount paid
#    """
#    return ... purchase_amount quota_price discount_value discount(purchase_amount) total_cost(purchase_amount)


def change(purchase_amount, amount_paid):
    """ (num, num) -> num

    Determines the change to be returned given the total cost of
    purchase and the amount paid
    """
    return amount_paid - total_cost(purchase_amount)

#examples
change(1000, 1500) #500
change(1300, 1500) #304







import math
radians_conversion_denominator = 180


#stub
#def angle_to_radians(degree_angle):
#    """ (num) -> num

#    Converts the given angle in degrees to radians
#    """
#    return 0

#template
#def angle_to_radians(degree_angle):
#    """ (num) -> num
#
#    Converts the given angle in degrees to radians
#    """
#    return ... degree_angle math_pi radians_conversion_denominator


def angle_to_radians(degree_angle):
    """ (num) -> num

    Converts the given angle in degrees to radians
    """
    return (math.pi / radians_conversion_denominator) * (degree_angle)

#example
angle_to_radians(180) #math.pi


#stub
#def length_of_ladder_required(height_reached, degree_angle):
#    """ (num, num) -> num
#
#    Accepts an angle in degrees, and calculates the length of ladder
#    required to reach a given height
#    """
#    return 0

#template
#def length_of_ladder_required(height_reached, degree_angle):
#    """ (num, num) -> num
#
#    Accepts an angle in degrees, and calculates the length of ladder
#    required to reach a given height
#    """
#    return ... degree_angle math_pi radians_conversion_denominator #height_reached


def length_of_ladder_required(height_reached, degree_angle):
    """ (num, num) -> num

    Accepts an angle in degrees, and calculates the length of ladder
    required to reach a given height
    """
    return height_reached / (math.sin(angle_to_radians(degree_angle)))

#examples
length_of_ladder_required(10, 90) #10
length_of_ladder_required(10, 30) == (10 / (math.sin(angle_to_radians(30))))
length_of_ladder_required(20, 45) == (20 / (math.sin(angle_to_radians(45))))





import math

#stub
#def radius(diameter):
#    """ (num) -> num
#
#    Computes for the radius given the diameter
#    """
#    return 0

#template
#def radius(diameter):
#    """ (num) -> num
#
#    Computes for the radius given the diameter
#    """
#    return ... diameter 2

def radius(diameter):
    """ (num) -> num

    Computes for the radius given the diameter
    """
    return diameter / 2

radius(4) #2


#stub
#def area_of_pizza(diameter):
#    """ (num) -> num
#
#    Computes for the area of a circular pizza given the diameter
#    """
#    return 0

#template
#def area_of_pizza(diameter):
#    """ (num) -> num
#
#    Computes for the area of a circular pizza given the diameter
#    """
#    return ... diameter math.pi

def area_of_pizza(diameter):
    """ (num) -> num

    Computes for the area of a circular pizza given the diameter
    """
    return math.pi * ((radius(diameter) ** 2))

area_of_pizza(4) == math.pi * ((radius(4) ** 2))

area_of_pizza(0) #0

#stub
#def cost_per_square_inch(diameter, price):
#    """ (num, num) -> num
#
#    Determines the cost per square inch of a circular pizza given
#    its diameter and price
#    """
#    return 0

#template
#def cost_per_square_inch(diameter, price):
#    """ (num, num) -> num
#
#    Determines the cost per square inch of a circular pizza given
#    its diameter and price
#    """
#    return ... diameter math_pi price

def cost_per_square_inch(diameter, price):
    """ (num, num) -> num

    Determines the cost per square inch of a circular pizza given
    its diameter and price
    """
    return price / (area_of_pizza(radius(diameter)))

cost_per_square_inch(100, 10) == 10 / (area_of_pizza(radius(100)))
cost_per_square_inch(200, 15) == 15 / (area_of_pizza(radius(200)))
cost_per_square_inch(300, 20) == 20 / (area_of_pizza(radius(300)))


