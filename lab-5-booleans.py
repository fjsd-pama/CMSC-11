Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> # 1
>>> True and not False
True
>>> True and not false
  #this will not work
>>> True or True and False
True
>>> not True or not False
True
>>> 52 < 52.3
True
>>> 1 + 52 < 52.3
False
>>> 4 != 4.0
False
>>> 
>>> # 2
>>> def are_they_equal(a, b, c):
	return (a and (b or c)) == ((a and b) or (a and c))

>>> are_they_equal(True, True, True)
True
>>> are_they_equal(True, True, False)
True
>>> are_they_equal(True, False, True)
True
>>> are_they_equal(True, False, False)
True
>>> are_they_equal(False, True, True)
True
>>> are_they_equal(False, True, False)
True
>>> are_they_equal(False, False, True)
True
>>> are_they_equal(False, False, False)
True
>>> #"the two functions are equal"
#'the two functions are equal'
>>> 
>>> def are_they_also_equal(a, b):
	return (not(a or b)) == ((not a) or (not b))

>>> are_they_also_equal(True, True)
True
>>> are_they_also_equal(True, False)
False
>>> are_they_also_equal(False, True)
False
>>> are_they_also_equal(False, False)
True
>>> #"therefore, the two functions are not equal"
#'therefore, the two functions are not equal'
 
>>> # 3
>>> def is_retired(age):
	return age >= 65

>>> def is_acid(ph_level):
	return ph_level < 7

>>> def is_teenager(age):
	return 13 <= age <= 19

>>> def is_even(x):
	return x % 2 == 0

>>> def is_valid_url(url):
	return url[0:4] + url[-4:] == "www." + ".com"

>>> def is_multiple_of_10(x):
	x % 10 == 0

	
>>> def is_multiple_of_10(x):
	return x % 10 == 0

>>> def is_vowel(letter):
	return letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"

