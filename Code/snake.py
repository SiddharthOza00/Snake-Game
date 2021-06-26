from turtle import Turtle


starting_position = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in starting_position:
            self.add_segment(position)


    def add_segment(self, position):
        segment = Turtle()
        segment.color("white")
        segment.penup()
        segment.shape("square")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1,0,-1):
            newy = self.segments[seg -1].ycor()
            newx = self.segments[seg-1].xcor()
            self.segments[seg].goto(newx, newy)
        self.head.forward(moving_distance)

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