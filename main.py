from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
snake = Snake()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
food = Food()
score = Score()

screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    if snake.head.distance(food) < 15:
        score.puntuacion()
        food.refresh()
        snake.extend()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset()
        snake.reset()
        

    for any_seg in snake.snake_long[1:]:
        if snake.head.distance(any_seg) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()