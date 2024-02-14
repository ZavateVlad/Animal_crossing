import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
random_speed = STARTING_MOVE_DISTANCE + random.choice(range(0,50))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        #self.create_car()
        #self.movement()

    def create_car(self):
        self.shape('square')
        #self.speed('fastest')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        random_y = random.choice(range(-250, 250))
        self.goto(280, random_y)




    def movement(self):
        self.forward(random_speed)


