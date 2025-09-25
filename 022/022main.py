import turtle, time
from players import Rackets, Ball, Score
screen = turtle.Screen()
screen.setup(width= 800, height= 500)
screen.bgcolor("black")
screen.title("PONG GAME")

line = turtle.Turtle()
line.color("white")
line.hideturtle()
line.speed("fastest")
line.pensize(10)
line.penup()
line.goto(0, -300)
line.setheading(90)

screen.listen()

for _ in range(30):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

left_racket = Rackets((-395, 0))
right_racket = Rackets((390, 0))
ball = Ball()

score = Score()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()
    if ball.distance(right_racket.racket) < 30 and ball.xcor() > 360 or ball.distance(left_racket.racket) < 35 and ball.xcor() < -360:
        ball.bounce_x()
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            score.left_point()
        else:
            score.right_point()
        time.sleep(1)
        ball.reset_position()

    screen.onkey(left_racket.move_up, 'q')
    screen.onkey(left_racket.move_down, 'a')
    screen.onkey(right_racket.move_down, 'Down')
    screen.onkey(right_racket.move_up, 'Up')




screen.exitonclick()