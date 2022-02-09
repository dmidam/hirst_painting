import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255)
color_list = [(35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8), (121, 221, 230), (23, 84, 93), (175, 188, 216), (102, 122, 172), (71, 71, 45)]

def random_color(list):
    random_color = random.choice(list)
    R = random_color[0]
    G = random_color[1]
    B = random_color[2]
    return R, G, B

def moving ():
    for _ in range(10):
        tim.color(random_color(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    for _ in range(10):
        tim.color(random_color(color_list))
        tim.forward(50)
        tim.dot(20)
        tim.penup()
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    # for _ in range(10):
    #     tim.color(random_color(color_list))
    #     tim.dot(20)
    #     tim.forward(50)
    #     tim.penup()
    # tim.left(90)
    # tim.forward(50)
    # tim.left(90)
    # for _ in range(10):
    #     tim.color(random_color(color_list))
    #     tim.forward(50)
    #     tim.dot(20)
    #     tim.penup()
    # tim.right(90)
    # tim.forward(50)
    # tim.right(90)
    # for _ in range(10):
    #     tim.color(random_color(color_list))
    #     tim.dot(20)
    #     tim.forward(50)
    #     tim.penup()

for _ in range(5):
    moving()
tim.hideturtle()



turtle.Screen()
turtle.exitonclick()