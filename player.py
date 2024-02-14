from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def reset_position(self):
        self.goto(STARTING_POSITION)