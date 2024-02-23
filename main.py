from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
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
