import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player.reset_position()
car_manager = CarManager()
scoreboard = Scoreboard()

for pos in range(-250, 230, 50):
    car_manager.start_positions.append(pos)
    

screen.listen()
screen.onkey(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 270:
        time.sleep(4)
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()
        
screen.exitonclick()