Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> def pizza_cost_per_square_inch(diameter, price):
	area = math.pi * ((diameter / 2) ** 2)
	return price / area

>>> def to_conserve_pizza(no_of_friends, maximum_slices):
	return (no_of_friends * maximum_slices) // 8

>>> to_conserve_pizza(5, 4)
2
>>> def epact_calculation(year):
	C = year / 100
	epact = ((8 + (C / 4) - C + ((8 * C + 13) / 25)) + (11 * (year % 19))) % 30
	return epact

>>> epact_calculation(2015)
10.855500000000001
>>> epact_calculation(2014)
29.8598
>>> epact_calculation(2012)
6.868400000000008
>>> def total_cost_of_coffee_order(kilo_of_coffee_beans):
	price_of_beans = 850 * kilo_of_coffee_beans
	cost_of_shipping = (185 * kilo_of_coffee_beans) + 250
	return price_of_beans + cost_of_shipping

>>> total_cost_of_coffee_order(30)
31300
>>> total_cost_of_coffee_order(1)
1285
>>> def length_of_ladder_required(height_reached_by_ladder, angle_of_ladder):
	return (height_reached_by_ladder / (math.sin(math.radians(angle_of_ladder))))

>>> length_of_ladder_required(9, 34)
16.094624849742605
>>> length_of_ladder_required(24, 90)
24.0
>>> 
