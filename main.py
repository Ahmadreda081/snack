from turtle import  Screen
from snack_body import Snack
import time
from food import Food
from sccorebord import ScoreBoard
screen = Screen()
screen.title('Snack Game')
screen.bgcolor('black')
Width = 600
Height = 600
screen.setup(width=Width, height=Height)
screen.tracer(0)
screen.listen()

snack = Snack()
food = Food()
score = ScoreBoard()
is_game_on = True
screen.onkey(snack.Right, 'd')
screen.onkey(snack.Left, 'a')
screen.onkey(snack.Up, 'w')
screen.onkey(snack.Down, 's')


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.xcor() >= Width/2  - 5 or snack.head.ycor() >=Height/2 - 5 \
            or snack.head.ycor() <= -Height/2 + 5or snack.head.xcor() <= -Width/2 + 5:
        score.reset()
        snack.rest()
    if snack.head.distance(food) < 15:
        food.refresh()
        score.incres_score()
        snack.extend()
    for segment in snack.segments[1:len(snack.segments) - 1]:
        if snack.head.distance(segment) < 15:
            score.reset()
            snack.rest()

screen.exitonclick()










