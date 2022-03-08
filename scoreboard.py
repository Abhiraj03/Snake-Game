from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",move=False,align=ALIGN,font=FONT)

    
    def score_update(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()