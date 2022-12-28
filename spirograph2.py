import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")


def square():
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)


for i in range(360//10):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.color((r, g, b))
    square()
    tim.setheading(tim.heading() + 10)
screen = turtle.Screen()
screen.exitonclick()
