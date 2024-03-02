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
        # game_is_on = False
        # scoreboard.game_over()

    #Detect colission with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()












#idk weird way i did
# x_value = -20
# for _ in range(3):
#     joe = Turtle("square")
#     joe.color("white")
#     joe.pensize(width=20)
#     joe.goto(x_value, 0)
#     x_value += 20



#dumb way
# joe1 = Turtle("square")
# joe1.color("white")
#
#
# joe2 = Turtle("square")
# joe2.color("white")
# joe2.goto(-20, 0)
#
# joe3 = Turtle("square")
# joe3.color("white")
# joe3.goto(-40, 0)

screen.exitonclick()
