passing_grade = 60
FE_total_pt = 150
perfect_class_standing = 100
final_exam_credit = 20
class_standing_credit = 80

#stub
#def final_exam_percentage(FE_score):
#    """ (num) -> num
#
#    Returns the final exam percentage given the
#    final exam score
#    """
#    return 0

#template
#def final_exam_percentage(FE_score):
#    """ (num) -> num
#
#    Returns the final exam percentage given the
#    final exam score
#    """
#    return ... FE_score FE_total_pt final_exam_credit

def final_exam_percentage(FE_score):
    """ (num) -> num

    Returns the final exam percentage given the
    final exam score
    """
    return ((FE_score / FE_total_pt)) * final_exam_credit

final_exam_percentage(150) #20
final_exam_percentage(75) #10

#stub
#def class_standing_percentage(class_standing):
#    """ (num) -> num
#
#    Calculates the class standing percentage given the class standing
#    """
#    return 0

#template
#def class_standing_percentage(class_standing):
#    """ (num) -> num
#
#    Calculates the class standing percentage given the current
#    class standing
#    """
#    return ... class_standing perfect_class_standing
#class_standing_credit

def class_standing_percentage(class_standing):
    """ (num) -> num

    Calculates the class standing percentage given the class standing
    """
    return (class_standing / perfect_class_standing) * class_standing_credit

class_standing_percentage(0) #0
class_standing_percentage(100) #80
class_standing_percentage(50) #40

#stub
#def is_passing(class_standing, FE_score):
#    """ (int, int) -> bool
#
#    Determines whether a student passes or fails a subject
#    given his current class standing and his final exam score
#    """
#    return 0

#template
#def is_passing(class_standing, FE_score):
#    """ (int, int) -> bool
#
#    Determines whether a student passes or fails a subject
#    given his current class standing and his final exam score
#    """
#    return class_standing_percentage class_standing final_exam_percentage FE_score passing_grade


def is_passing(class_standing, FE_score):
    """ (int, int) -> bool

    Determines whether a student passes or fails a subject
    given his current class standing and his final exam score
    """
    return ((class_standing_percentage(class_standing)) + (final_exam_percentage(FE_score))) >= passing_grade

is_passing(80, 0) #True
is_passing(0, 20) #False
is_passing(100, 150) #True
is_passing(0, 0) #False





fare_rate = 7.5
add_rate = 0.75
km_base = 5

#stub
#def pay_for_km_base(km):
#    """ (num, int) -> num
#    Returns amount to pay if the given number of kilometers
#    does not exceed km_base
#    """
#    return 0

#template
#def pay_for_km_base(km):
#    """ (num, int) -> num
#    Returns amount to pay if the given number of kilometers
#    does not exceed km_base
#    """
#    return … fare_rate km

def pay_for_km_base(km):
    """ (num, int) -> num
    Returns amount to pay if the given number of kilometers
    does not exceed km_base
    """
    return fare_rate * km

pay_for_km_base(5) ==  fare_rate * 5
pay_for_km_base(4) == fare_rate * 4


#stub
#def pay_for_km_exceeding(km):
#    """ (num, int) -> num
#
#    Returns the amount to pay if the given number of kilometers
#    exceeds km_base
#    """
#    return 0

#template
#def pay_for_km_exceeding(km):
#    """ (num, int) -> num
#
#    Returns the amount to pay if the given number of kilometers
#    exceeds km_base
#    """
#    return … km pay_for_km_base km_base add_rate


def pay_for_km_exceeding(km):
    """ (num, int) -> num

    Returns the amount to pay if the given number of kilometers
    exceeds km_base
    """
    return (pay_for_km_base(km) + ((km - km_base) * (add_rate)))

pay_for_km_exceeding(6) == (pay_for_km_base(km) + ((6 - km_base) * (add_rate)))


#stub
#def appropriate_fare(km, people):
#    """ (num, int) -> num
#
#    Calculates the appropriate fare for a group of people given
#    the number of kilometers travelled
#    """
#    return 0


#template
#def appropriate_fare(km, people):
#    """ (num, int) -> num
#
#    Calculates the appropriate fare for a group of people given
#    the number of kilometers travelled
#    """
#    return ... km fare_rate add_rate first_km people

def appropriate_fare(km, people):
    """ (num, int) -> num

    Calculates the appropriate fare for a group of people given
    the number of kilometers travelled
    """
    if (km <= km_base):
        return people * (pay_for_km_base(km))
    else:
        return people * (pay_for_km_exceeding(km))

#examples
pay_for_km_base(5, 0) == 0 * fare_rate * 5
pay_for_km_base(5, 1) == 1 * fare_rate * 5
pay_for_km_base(5, 2) == 2 * fare_rate * 5
pay_for_km_base(0, 0) == 0 * fare_rate * 0
pay_for_km_base(4, 1) == 1 * 4 * fare_rate
pay_for_km_base(4, 2) == 2 * 4 * fare_rate
pay_for_km_exceeding(6, 0) == 0
pay_for_km_exceeding(6, 1) == 1 *(pay_for_km_base(6) + ((6 - km_base) * (add_rate)))
pay_for_km_exceeding(6, 2) == 2 *(pay_for_km_base(6) + ((6 - km_base) * (add_rate)))




horizontal_line_slope = 0

#stub
#def slope(x1, y1, x2, y2):
#    """ (num, num, num, num) -> num
#
#    Computes the slope given 2 x-coordinates and 2 y-coordinates
#    from two distinct points
#    """
#    return 0


#template
#def slope(x1, y1, x2, y2):
#    """ (num, num, num, num) -> num
#
#    Computes the slope given 2 x-coordinates and 2 y-coordinates
#    from two distinct points
#    """
#    return …  rise y1 y2 run x1 x2

def slope(x1, y1, x2, y2):
    """ (num, num, num, num) -> num

    Computes the slope given 2 x-coordinates and 2 y-coordinates
    from two distinct points
    """
    return (y2 - y1) / (x2 - x1)

#examples
slope(0, 0, 0, 0) #error
slope(0, 0, 0, 1) #error
slope(0, 1, 0, 1) #error
slope(0, 1, 1, 1) #expect 0
slope(1, 1, 1, 1) #error
slope(1, 1, 1, 2) #error
slope(1, 1, 2, 2) #expect 1
slope(1, 2, 2, 2) #expect 0
slope(1, 2, 2, 3) #expect 1
slope(1, 3, 2, 2) #expect -1

#stub
#def is_horizontal(x1, y1, x2, y2):
#    """ (num, num, num, num) -> bool
#
#    Determines whether a line, denoted by two points (x1, y1) and (x2, y2)
#    is horizontal
#    """
#    return 0

#template
#def is_horizontal(x1, y1, x2, y2):
#    """ (num, num, num, num) -> bool
#
#    Determines whether a line, denoted by two points (x1, y1) and (x2, y2)
#    is horizontal
#    """
#    return slope x1 y1 x2 y2 horizontal_line_slope

def is_horizontal(x1, y1, x2, y2):
    """ (num, num, num, num) -> bool

    Determines whether a line, denoted by two points (x1, y1) and (x2, y2)
    is horizontal
    """
    return slope(x1, y1, x2, y2) == horizontal_line_slope

#examples
is_horizontal(0, 0, 0, 0) #error
is_horizontal(0, 0, 0, 1) #error
is_horizontal(0, 1, 0, 1) #error
is_horizontal(0, 1, 1, 1) #expect 0 #True
is_horizontal(1, 1, 1, 1) #error
is_horizontal(1, 1, 1, 2) #error
is_horizontal(1, 1, 2, 2) #expect 1 #False
is_horizontal(1, 2, 2, 2) #expect 0 #True
is_horizontal(1, 2, 2, 3) #expect 1 #False
is_horizontal(1, 3, 2, 2) #expect -1 #False

