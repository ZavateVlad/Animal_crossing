
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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    car.create_car()
    car.movement()

    # Change level
    if player.ycor() > 250:
        scoreboard.increase_level()
        player.reset_position()
        car.increase_speed()

    # Detect player's collision with car
    for i in car.all_cars:
        if i.distance(player.position()) < 35:
            scoreboard.game_over()
            game_is_on = False






#create car
#move the car
#after a while
#create another car
#move the other car
#and so on
screen.exitonclick()
