import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
#screen.tracer(0)
player = Player()
game_is_on = True
game = True

while game:
    car = CarManager()
    screen.ontimer(car.create_car(), t=10)
    while game_is_on:
        screen.ontimer(car.movement(), t=100)
    # while game_is_on:
    #     car.movement()




screen.listen()
screen.onkeypress(player.move_up, 'Up')

#game_is_on = True



# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     car.movement()





#create car
#move the car
#after a while
#create another car
#move the other car
#and so on
screen.exitonclick()
