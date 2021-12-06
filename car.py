from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.goto(x=310 + (random.randint(1, 500)), y=random.randint(-150, 150))
        self.setheading(180)
        self.turtlesize(stretch_len=3)
        self.move_speed = 0

    def move(self):
        if self.xcor() < -360:
            self.goto(x=310, y=random.randint(-150, 150))
        else:
            self.forward(self.move_speed)
