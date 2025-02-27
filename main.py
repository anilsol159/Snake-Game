import time
from turtle import Screen
from food import Food
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w",fun=snake.up)
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="d",fun=snake.right)
screen.onkey(key="a",fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        scoreboard.reset()
        snake.reset()

    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()


    snake.move()



screen.exitonclick()