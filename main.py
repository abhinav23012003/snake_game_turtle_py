from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    line = Turtle()
    line.hideturtle()
    line.color("white")
    line.penup()
    line.goto(0, 270)
    line.write("____________________________________________", move=False, align="center", font=("Arial", 25, "normal"))
    # Detecting collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_update()
        snake.extend()
# Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

# Detect collision with tail
# If head collide with any segment in the tail
# trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()
