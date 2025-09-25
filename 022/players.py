import turtle
class Rackets:
    def __init__(self, position):
        self.racket = turtle.Turtle()
        self.racket.shape("square")
        self.racket.color("white")
        self.racket.shapesize(stretch_wid=5, stretch_len=1)
        self.racket.penup()
        self.racket.goto(position)

    def move_up(self):
        y = self.racket.ycor()
        if y < 200:
            self.racket.sety(y + 50)

    def move_down(self):
        y = self.racket.ycor()
        if y > -200:
            self.racket.sety(y - 50)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

class Score:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"{self.left_score}    {self.right_score}", align="center", font=("Courier", 26, "bold"))

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()