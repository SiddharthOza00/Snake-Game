from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Food Detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


    #Wall Collision Detection
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        print(f"Game Over! Your score is {score.Score}")
        score.reset()
        snake.reset()


    #Detect Collision with Tail
    #if head collides with any part of the tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
                pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()