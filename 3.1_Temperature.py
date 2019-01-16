'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ???

'''

temp_fahrenheit = int(input("Enter Temperature Fahrenheit:"))
temp_celsius= (temp_fahrenheit-32)*5/9
print("Temperature Celsius:", temp_celsius)