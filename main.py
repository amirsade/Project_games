from turtle import Screen
from scoreboard import ScoreBoard
from food import Food
from snake import Snake
from time import sleep

snake = Snake()
food = Food()
score = ScoreBoard()
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.title('Your Snake Game')
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
is_race_on = True
while is_race_on:
    screen.update()
    sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.change_score()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        is_race_on = False
        score.game_over()
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            is_race_on = False
            score.game_over()
screen.exitonclick()
