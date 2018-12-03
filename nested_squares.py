import turtle
import math
import random

screen = turtle.Screen()
ted = turtle.Turtle()
sideLength = 50
colors = ["red","purple","blue","orange","pink","green","yellow","brown","grey","black"]
for x in range(7):
    for i in range(4):
    	ted.forward(sideLength)
    	ted.right(90)
    color = random.choice(colors)
    sideLength = sideLength+20
    ted.color(color)
screen.exitonclick()
