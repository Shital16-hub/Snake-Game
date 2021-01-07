from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.go_snake()

    # Detect the collision between snake head and food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.refresh_score()

    # Detect the collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect the collision with wall
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
