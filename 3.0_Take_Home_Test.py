'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Spencer Daves



1. Write a line of code that will print your name.
'''
print("Spencer Daves")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?

'''
name=(input("What's your name?"))
print(name)
'''
3. Predict the output of the following lines of code and then test them? Write down your prediction and the output.
print (17/9)   prediction: 1.88  result: 1.8888888888888888
print (17//9)  prediction: 1     result: 1
print (17%9)   prediction: 8     result: 8
'''


'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.

'''
base=int(input("Enter base length:"))
height=int(input("Enter the height:"))
area=base*height/2
print("Area:", area)
'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
a="May the force be with you!"
print(a)


'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''

side_length=int(input("Enter square's side length:"))
square_area=side_length**2
print("Area:", square_area)
'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
radius_a=int(input("Enter 1st radius length: "))
radius_b=int(input("Enter the 2nd radius length: "))
ellipse_area=radius_a*radius_b*3.14
print("Ellipse Area:", ellipse_area)

'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
moles=int(input("Enter amount of moles:"))
temp=int(input("Enter the temperature in celsius:"))
volume=int(input("Enter the volume in meters cubed: "))
gas_constant=8.3144
pressure= (moles*temp*gas_constant)/volume
print("Pressure: ", pressure, "atmospheres")
'''
9. Ask a user for an integer and then print the square root.
'''
integer=int(input("Enter the integer you want to find the square root of:"))
square_root=integer**0.5
print("Square Root:", square_root)
'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
mass=int(input("Enter mass: "))
acceleration=int(input("Enter acceleration: "))
force=mass*acceleration
print("Force:", force)
print("Get it?")