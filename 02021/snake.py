import turtle
SNAKE_POSITIONS = [(0,0),(-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in SNAKE_POSITIONS:
            self.add_segm(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
    
    def add_segm(self, position):
        segment = turtle.Turtle(shape= "square")
        segment.color("yellow")
        segment.penup() 
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        last_position = self.segments[-1].position()
        self.add_segm(last_position)
    def Up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(90)
    def Down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)
    def Right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.ht()
            
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]