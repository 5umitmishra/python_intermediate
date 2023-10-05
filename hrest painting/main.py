# import colorgram
#
# rgb_color =[]
# colors = colorgram.extract('537b6eca8c43b46982da4c2af786fb1124592d0a-1200x995.webp', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b, )
#     rgb_color.append(new_color)
# print(rgb_color)

import turtle as t
t.colormode(255)
import random
tim = t.Turtle()

color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40),
 (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143),
 (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92),
 (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187),
 (169, 206, 172), (219, 182, 169)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
total_dots = 100
tim.speed("fastest")
tim.hideturtle()


for dots_count in range (1,total_dots +1):
    tim.dot(20 , random.choice(color_list))
    tim.forward(50)

    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()

























