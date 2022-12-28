import turtle as t
import random
import colorgram
t.colormode(255)


def color_extraction(image, number):
    extract_colors = colorgram.extract(image, number)
    colours = []
    for i in range(len(extract_colors)):
        color = extract_colors[i]
        rgb = color.rgb
        color_tuple = (rgb.r, rgb.g, rgb.b)
        colours.append(color_tuple)
    return colours


colors = color_extraction('img.jpg', 50)
tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(320)
tim.setheading(0)
for dot in range(1, 101):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
