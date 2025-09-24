import turtle, random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed(10.5)
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.desapier()

    def desapier(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))