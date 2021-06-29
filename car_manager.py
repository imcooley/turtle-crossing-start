from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.add_cars()
        self.cars = []

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        print(new_x)
        self.goto(new_x, self.ycor())

    def add_cars(self):
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randint(-250, 250)
        starting_x = 300
        self.goto(starting_x, random_y)
        self.setheading(180)
        self.cars.append(new_car)
