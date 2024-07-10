"""
fibonacci series
"""
import turtle

screen = turtle.Screen()
screen.setup(1000, 800)
Turtle = turtle.Turtle()
Turtle.pensize(3)

def main():
    Num_One = 0
    Num_Two = 1
    sum_of_Nums = 1
    for i in range(8):
        Turtle.right(90)
        drawSq(sum_of_Nums * 20)
        sum_of_Nums = Num_One + Num_Two
        Num_One = Num_Two
        Num_Two = sum_of_Nums

def drawSq(sides):
    for n in range(6):
        Turtle.forward(sides)
        Turtle.left(90)

def spiral():
    r = 20
    angle = 90
    Turtle.right(90)
    Turtle.penup()
    Turtle.setpos(0, 0)
    Turtle.pendown()
    arc(20, angle)
    arc(20, angle)
    arc(40, angle)
    arc(60, angle)
    arc(100, angle)
    arc(160, angle)
    arc(260, angle)
    arc(420, angle)

def arcLine(n, length, angle):
    for i in range(n):
        Turtle.forward(length)
        Turtle.left(angle)

def arc(r, angle):
    arc_length = 2 * 3.14159 * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    Turtle.left(step_angle / 2)
    arcLine(n, step_length, step_angle)
    Turtle.right(step_angle / 2)

def fibonacci_series():
    main()
    spiral()
    screen.exitonclick()

fibonacci_series()