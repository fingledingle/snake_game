from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    """Snake for the game"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

        # idk weird way i did
        # x_value = -20
        # for _ in range(3):
        #     joe = Turtle("square")
        #     joe.color("white")
        #     joe.pensize(width=20)
        #     joe.goto(x_value, 0)
        #     x_value += 20


        # dumb way
        # joe1 = Turtle("square")
        # joe1.color("white")
        #
        #
        # joe2 = Turtle("square")
        # joe2.color("white")
        # joe2.goto(-20, 0)
        #
        # joe3 = Turtle("square")
        # joe3.color("white")
        # joe3.goto(-40, 0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): #example(1,2,3) start being 1 stop being 3 and step being 1 since it will jump 1 by 1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
