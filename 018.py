import turtle
import random
import colorgram
# def new_random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)
# t = turtle.Turtle()
# t.speed("fastest")
# t.pensize(5)
# turtle.colormode(255)


# colors = ["red", "green", "yellow", "brown","black"]
# moves = [0,45, 90, 135,225, 315, 180, 270]

# # for i in range(100000):
# #     t.color(new_random_colour())
# #     t.forward(5)
# #     t.setheading(random.randint(0, 360))
# for _ in range(360):
#     t.color(new_random_colour())
#     t.circle(100)
#     t.setheading(t.heading() + 0.1) 
t = turtle.Turtle()
turtle.colormode(255)
list_colors = []
colors = colorgram.extract('/home/gentes/Documents/My 100 days pycodes/image1.jpg', 20)
for i in range(20):
    list_colors.append(colors[i].rgb)
print(list_colors)

def new_line():
    for i in range(7):
        t.dot(20, random.choice(list_colors))
        t.penup()
        t.forward(30)
        t.pendown()
def turn(i):
    if i % 2 == 0:
        t.left(90)
        t.penup()
        t.forward(30)
        t.left(90)
        t.forward(30)
        t.pendown
    else:
        t.right(90)
        t.penup()
        t.forward(30)
        t.right(90)
        t.forward(30)
        t.pendown
for i in range(7):
    new_line()
    turn(i)


screen = turtle.Screen()
screen.exitonclick()

