from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.color = 'brown'
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def change_score(self):
        self.score += 1
        self.clear()
        self.update_score()