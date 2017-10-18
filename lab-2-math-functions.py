Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> def first(p):
	return math.sqrt((1 - p) ** 3)

>>> def second(n):
	return (n * (n - 1)) / 2

>>> def third(x, y):
	return math.sqrt(50 (x ** 3) * (y ** 5))

>>> def fourth():
        return (4 * math.sqrt(5)) + (3 * math.sqrt(125)) - (math.sqrt(20))

>>> def fifth(x):
	return (x * (x - 1)) / (x * (x + 1))

>>> def sixth(r):
	4 * math.pi * (r ** 2)

	
>>> def seventh(a, r):
	return (r * (math.cos(a) ** 2)) + (r * (math.sin(a) ** 2))

>>> def eight(a, x, b, c):
	first_term= a * ((x + (b / (2 * a))) ** 2)
	second_term= ((b ** 2) - (4 * a * c)) / (4 * a)
	return first_term - second_term

>>> def ninth(x):
	return (-2 * (x ** 2)) + x - 1

>>> def tenth(x):
	return x + abs(x - 2)
