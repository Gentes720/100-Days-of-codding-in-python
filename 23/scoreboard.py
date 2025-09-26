import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"LEVEL: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.pen.goto(0, 0)
        self.pen.write("GAME OVER", align="center", font=FONT)
