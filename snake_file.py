import turtle as t 
DOWN=270
UP=90
LEFT=180
RIGHT=0
POISITION= [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.body_list=[]
        self.create_snake()
        self.head = self.body_list[0]

    def snake_body_creator(self, position):
        kachua=t.Turtle("square") 
        kachua.penup()
        kachua.color("white")
        kachua.goto((position))
        self.body_list.append(kachua)


    def create_snake(self):
        for position in POISITION:
            self.snake_body_creator(position)


    def move(self):
        for i in range(len(self.body_list)-1,0,-1):
            x_axis= self.body_list[i-1].xcor()
            y_axis= self.body_list[i-1].ycor()
            self.body_list[i].goto(x_axis, y_axis)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def extend(self):
        self.snake_body_creator(self.body_list[-1].position())

    def restart(self):
        for sender in self.body_list:
         sender.goto(1000,1000)
        self.body_list.clear()
        self.create_snake()
        self.head = self.body_list[0]
