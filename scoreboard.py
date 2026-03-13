from turtle import Turtle 





class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.score_update()
        self.hideturtle()


    def score_update(self):
        self.clear()
        self.write(arg= f"Score: {self.score} High Score {self.high_score}", align="center", font=("Bookman Old Style",16,"bold", "underline"))

    def score_increase(self):
        self.score+=1
        self.score_update()
    
    def high_score_update(self):
        if self.score > self.high_score :
            self.high_score= self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
        self.score= 0
        self.score_update()
