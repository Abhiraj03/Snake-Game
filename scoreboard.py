from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('Snake-Game\data.txt') as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Snake-Game\data.txt', mode='w') as new_data:
                new_data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",move=False,align=ALIGN,font=FONT)

    
    def score_update(self):
        self.score += 1
        self.update_scoreboard()