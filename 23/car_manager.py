import random
import turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.ht()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.start_positions = []
    
    def create_car(self):
        if random.randint(1, 6) == 1 :
            new_car = turtle.Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.choice(self.start_positions))
            self.all_cars.append(new_car)

    def move_cars(self):    
        for car in self.all_cars:
            car.backward(self.car_speed)
        

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
