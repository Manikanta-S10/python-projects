from turtle import *
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
              
    def add_segment(self,position):
        self.new_segment = Turtle('square')
        self.new_segment.penup()
        self.new_segment.color('white')
        self.new_segment.goto(position)
        self.segments.append(self.new_segment) 

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())    

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.new_x = self.segments[seg_num-1].xcor()
            self.new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(self.new_x,self.new_y)
        self.head.forward(MOVE_DISTANCE)     

    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)            
