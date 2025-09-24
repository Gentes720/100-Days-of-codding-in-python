import turtle, time


class ScoreBoaard(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.scorep = 0
        self.hscore = 0
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.Update_score()

    def increase(self):
        self.scorep += 1
        self.Update_score()

    def Update_score(self):
        self.clear()
        self.get_hscore()
        self.write(f"score = {self.scorep}, High score {self.hscore} ",False , align = "center", font = ("Arial", 15, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!",False , align = "center", font = ("Arial", 30, "bold"))
    #     time.sleep(3)
        
    def reset(self):
        self.get_hscore()
        if self.scorep > self.hscore:
            with open('data.txt', mode= 'w') as data:
                data.write(f'{self.scorep}')

        self.scorep = 0
        self.Update_score()

    def get_hscore(self):
        with open('data.txt', 'r') as data:
            self.hscore = int(data.read())
        