import turtle
import math

user = int(input("Please enter the number of sides in a polygon:"))
if (user < 3 or user > 25):
	print("Please enter a correct number!")
screen = turtle.Screen()
ted = turtle.Turtle()
sideLength = 100
angle = 360/user
if (user >= 3 and user <= 25):
	for i in range(user):
		ted.forward(sideLength)
		ted.left(angle)

screen.exitonclick()