from turtle import Turtle
FONT = ("Arial", 25, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_clear_write()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def score_clear_write(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.score_clear_write()
