import turtle

screen = turtle.Screen()
ted = turtle.Turtle()
ted.color("green")
ted.begin_fill()
ted.circle(50)
ted.end_fill()

ted.penup()
ted.setposition(-120,0)
ted.pendown()
ted.begin_fill()
ted.color("yellow")
ted.circle(50)
ted.end_fill()

ted.penup()
ted.setposition(60,60)
ted.pendown()
ted.begin_fill()
ted.color("red")
ted.circle(50)
ted.end_fill()
 
ted.penup()
ted.setposition(-60, 60)
ted.pendown()
ted.begin_fill()
ted.color("black")
ted.circle(50)
ted.end_fill()
 
ted.penup()
ted.setposition(-180, 60)
ted.pendown()
ted.begin_fill()
ted.color("blue")
ted.circle(50)
ted.end_fill()

screen.exitonclick()