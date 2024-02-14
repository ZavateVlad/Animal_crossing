
from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(False)
player = Player()
car = CarManager()



screen.listen()
screen.onkeypress(player.move_up, 'Up')

game_is_on = True



while game_is_on:
    time.sleep(0.1)
    screen.update()
    #screen.ontimer(car.create_car(), t =1)
    #screen.ontimer(car.movement(), t = 1)
    car.create_car()
    car.movement()






#create car
#move the car
#after a while
#create another car
#move the other car
#and so on
screen.exitonclick()
