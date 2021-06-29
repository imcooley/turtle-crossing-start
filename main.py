import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    counter += 1
    if counter == 4:
        counter = 0
        car_manager.add_car()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.start()
        car_manager.level_up()



screen.exitonclick()