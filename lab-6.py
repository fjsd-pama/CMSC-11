def max_of_2(x, y):
    if (x > y):
        return x
    else:
	   return y

def signal_no(windspeed):
    if (windspeed > 185):
	return 4
    elif (100 <= windspeed <= 185):
	return 3
    elif (60 <= windspeed < 100):
	return 2
    elif (30 <= windspeed < 60):
	return 1
    else:
	return 0

	
def daily_pay(hours):
    if (hours <= 8):
	return hours * 80
    else:
        return hours * 120

        
def max_of_3(x, y, z):
    if (x >= (y or z)) or (x >= (y and z)):
	return x
    elif (y >= (x or z)) or (y >= (x and z)):
	return y
    elif (z >= (x or y)) or (z >= (x and y)):
	return z
    else:
	return x

	
def motto(first, last):
    if (last == "Stark" and first != "Arya"):
	return "Winter is Coming"
    elif (first == "Jon" and last == "Snow"):
	return "Winter is Coming"
    elif (first == "Arya" and last == "Stark"):
	return "Valar Morghulis"
    elif (last == "Lannister"):
	return "Hear Me Roar"
    elif (last == "Baratheon"):
	return "Ours is the Fury"
    else:
	return "..."

	
def risk_level(bmi, age):
    if (bmi < 22.0 and age < 45):
	return "Low"
    elif (bmi >= 22.0 and age < 45)or (bmi < 22.0 and age >= 45):
	return "Medium"
    else:
	return "High"

 
