import turtle, time, math
from snake import Snake
from food import Food
from score import ScoreBoaard


screen = turtle.Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("green")
screen.title("SNAKE GAME")
  
snake = Snake()
food = Food( )
score = ScoreBoaard()


screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.03)
    snake.move() 

    if snake.head.distance(food) < 15:
        snake.extend()
        food.desapier()
        score.increase()
       

    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        score.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
                score.reset()
                snake.reset()

     
screen.exitonclick() 