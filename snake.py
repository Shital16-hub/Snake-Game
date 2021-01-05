from turtle import Turtle, Screen
import time

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()

    def creat_snake(self):
        for position in START_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # def new_segment(self):
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     self.segments.append(new_segment)

    def go_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    snake.creat_snake()
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        snake.go_snake()

    screen.exitonclick()
