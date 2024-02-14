import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
random_speed = STARTING_MOVE_DISTANCE + random.choice(range(0,50))


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        for i in self.all_cars:
            if self.all_cars[i].distance:
                self.all_cars.pop(i)

    def create_car(self):
        new_car = Turtle('square')
        new_car.speed('fastest')
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.choice(range(-250, 250))
        new_car.goto(330, random_y)
        if new_car.ycor() % 4 == 0:
            self.all_cars.append(new_car)




    def movement(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


