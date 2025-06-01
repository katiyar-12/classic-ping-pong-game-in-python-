from turtle import  Turtle

class Paddle(Turtle) :

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.speed("fastest")
        self.penup()
        # default size of every turtle is 20 by 20
        self.shapesize(stretch_len=5, stretch_wid=1)

        self.up()
        self.down()


    def set_position(self,x,y):
        self.setposition(x,y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


