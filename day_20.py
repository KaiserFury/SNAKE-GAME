import turtle as t
import time
from snake_file import Snake
from food import Food
from scoreboard import Score 



screen=t.Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True  

while game_is_on :

    screen.update()
    time.sleep(0.10)
    
    if snake.head.distance(food) < 15:
        food.egg_next_loctaion()
        score.score_increase()
        snake.extend()

#Game over condition :- Touching the wall
    if snake.head.xcor()>295 or snake.head.ycor()>295 or snake.head.xcor()<-295 or snake.head.ycor()<-295:
        score.high_score_update()
        snake.restart()


# Game over condition:- Touching the body 
    for cheker in snake.body_list[1:]:
        if snake.head.distance(cheker) <10:
            score.high_score_update()
            snake.restart()
        

    snake.move()



screen.exitonclick()