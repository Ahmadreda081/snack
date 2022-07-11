from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(.4,.4)

        self.refresh()
    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)

        self.goto(random_x, random_y)
