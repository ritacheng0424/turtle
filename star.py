import turtle

screen = turtle.Screen()
ted = turtle.Turtle()
sideLength = 300
for x in range(5):
	ted.forward(sideLength)
	ted.right(144)
screen.exitonclick()
