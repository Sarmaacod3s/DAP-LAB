def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:",round(celsius,3))

fahrenheit = float(input('enter fahrenheit'))
fahrenheit_to_celsius(fahrenheit) 
