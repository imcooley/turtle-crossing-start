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

screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    counter += 1
    print(counter)
    if counter == 6:
        counter = 0
        car_manager.add_cars()
        # for _ in random.randint(0, 10):
        #     car_manager.add_cars()
