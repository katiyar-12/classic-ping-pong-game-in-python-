import time
from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


myScreen = Screen()

myScreen.tracer(0)


ball = Ball()

r_paddle = Paddle()
l_paddle = Paddle()
scoreboard = Scoreboard()




myScreen.setup(width=800,height=600)
myScreen.bgcolor("black")
myScreen.title(titlestring="My ping pong Game ")




r_paddle.setposition(350,0)
l_paddle.setposition(-350,0)






myScreen.listen()

myScreen.onkey(r_paddle.up, "Up")
myScreen.onkey(r_paddle.down, "Down")

myScreen.onkey(l_paddle.up , "w")
myScreen.onkey(l_paddle.down , "s")




game_is_on = True

while game_is_on :
    scoreboard.scoreboard()
    time.sleep(ball.move_speed)

    myScreen.update()
    ball.move_ball()

    # detection collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >  330 or ball.distance(l_paddle) < 50 and ball.xcor() > -330 :
        ball.bounce_x()
    # detect when  right paddle misses the ball
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    # detect when  left paddle misses the ball
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()





myScreen.exitonclick()

