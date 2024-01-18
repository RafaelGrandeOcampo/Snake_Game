from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT= 0
LEFT= 180

class Snake:
    def __init__(self):
        self.snake_long = []
        self.create_snake()
        self.head = self.snake_long[0]

    def move(self):
        for seg_num in range(len(self.snake_long) - 1, 0, -1):
            new_x = self.snake_long[seg_num - 1].xcor()
            new_y = self.snake_long[seg_num - 1].ycor()
            self.snake_long[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.setposition(position)
        self.snake_long.append(snake)

    def reset(self):
        for seg in self.snake_long:
            seg.goto(1000, 1000)
        self.snake_long.clear()
        self. create_snake()
        self.head = self.snake_long[0]

    def extend(self):
        self.add_segment(self.snake_long[-1].position())

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
