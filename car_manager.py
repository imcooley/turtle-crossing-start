from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)

    def add_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randint(-250, 250)
        new_car.goto(320, random_y)
        self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
