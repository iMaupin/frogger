from turtle import Turtle


class LevelNumber(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=("Courier", 24, "normal"))

    def next_level(self):
        self.level += 1
        self.update_level()
        return self.level

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 36, "normal"))
