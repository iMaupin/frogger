from turtle import Turtle

STARTING_POSITION = (0, -280)


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

    def turn_right(self):
        self.right(90)

    def turn_left(self):
        self.left(90)

    def reset_frog(self):
        self.goto(STARTING_POSITION)