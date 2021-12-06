from turtle import Screen
from frog import Frog
from car import Car
from levelnumber import LevelNumber
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Frogger")
frog = Frog()
level_label = LevelNumber()
level = level_label.level


def update_cars():
    cars = [
        Car() for _ in range(level * 5)
    ]
    for car in cars:
        car.move_speed += 10
    return cars


cars = update_cars()

screen.listen()
screen.onkey(key="Up", fun=frog.move_forward)
screen.onkey(key="Down", fun=frog.move_backward)
screen.onkey(key="Right", fun=frog.turn_right)
screen.onkey(key="Left", fun=frog.turn_left)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for car in cars:
        car.move()

    for car in cars:
        if car.distance(frog) < 27:
            level_label.game_over()
            game_is_on = False

    if frog.ycor() > 300:
        frog.reset_frog()
        level_label.next_level()
        level = level_label.level
        for car in cars:
            car.hideturtle()
        cars = update_cars()

screen.exitonclick()
