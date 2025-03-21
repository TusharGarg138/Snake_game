from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}" ,False, "center", ("Arial", 15, "normal"))
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 15, "normal"))

    def reset(self):
        if self.score> self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", False, "center", ("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()