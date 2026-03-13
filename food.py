import turtle as t
import random 
class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed(0)
        self.egg_next_loctaion()


    def egg_next_loctaion(self):
        x_axis= random.randint(-280, 280)
        y_axis= random.randint(-280, 280)
        self.goto(x_axis,y_axis)
