from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()




screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")                        
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update() #it will work since its moving the whole segment
    time.sleep(0.1)
    snake.move()

    #Colission with FOOD
    if snake.head.distance(food) < 15:
    #print("Nom nom") #Testing colission
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Wall Colission
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            




screen.exitonclick()
