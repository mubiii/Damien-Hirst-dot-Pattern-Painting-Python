import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")

for i in range(360//5):
    r = random.randint(1, 200)  # (1, 255)
    g = random.randint(1, 200)  # (1, 255)
    b = random.randint(1, 200)  # (1, 255)
    tim.color((r, g, b))
    tim.circle(100)
    tim.setheading(tim.heading() + 5)
screen = turtle.Screen()
screen.exitonclick()
