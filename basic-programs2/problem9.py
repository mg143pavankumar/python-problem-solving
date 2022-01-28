# Python Program to Convert Celsius To Fahrenheit
'''
    (celsius * 9/5) + 32 = Fahrenheit
'''


def convert_celsius_to_fahrenheit(celsius):
    '''Converting celsius to fahrenheit'''

    fahrenheit = (celsius * 9/5) + 32
    print(f"Fahrenheit = {fahrenheit} F")


def convert_fahrenheit_to_celsius(fahrenheit):
    '''Converting fahrenheit to Celsius'''

    celsius = (fahrenheit - 32) * 5/9
    print(f"Celsius = {celsius} C")


print(convert_celsius_to_fahrenheit.__doc__)
convert_celsius_to_fahrenheit(21)

print("")
print(convert_fahrenheit_to_celsius.__doc__)
convert_fahrenheit_to_celsius(69.8)
