from turtle import Turtle
ALIGN="center"
FONT=('Arial', 18, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-20,260)
        with open('high_score.txt', 'r') as data:
            self.high_score = int(data.read())


        self.update_screen()
        self.ht()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_screen()

    def incres_score(self):
        self.clear()
        self.score += 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f'Score: {self.score}  High score: {self.high_score}',  align=ALIGN, font=FONT)




