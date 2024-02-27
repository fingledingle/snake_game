from turtle import Turtle
FONT = ('Courier', 14 , 'normal')
ALIGMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)

