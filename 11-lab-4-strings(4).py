Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> # 1
>>> def f():
	return "the quick brown fox jumps over the lazy dog"

>>> f()[0:3]
'the'
>>> f()[16] * 5
'fffff'
>>> f()[13]
'w'
>>> f()[37]
'z'
>>> f()[42]
'g'
>>> f()[21]
'u'
>>> f()[16:19]
'fox'
>>> f()[40:]
'dog'
>>> f()[20:30]
'jumps over'
>>> f()[10:26] * 3
'brown fox jumps brown fox jumps brown fox jumps '
>>> f()[31:]
'the lazy dog'
 
>>> # 2
>>> def up_email_add(first, middle, last):
	return first[0] + middle[0] + last + "@up.edu.ph"

>>> up_email_add("juan", "gonzales", "mendoza")
'jgmendoza@up.edu.ph'
>>> def initials(first, middle, last):
	return first[0] + middle[0] + last[0]

>>> initials("Juan", "Gonzales", "Mendoza")
'JGM'
>>> def name_ave(first, middle, last):
	return (len(first) + len(middle) + len(last)) / 3

>>> name_ave("Juan", "Gonzales", "Mendoza")
6.333333333333333
 
