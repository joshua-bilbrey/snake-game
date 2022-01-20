from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
TOP_POS = (0, 280)
BOTTOM_POS = (0, -280)


class Scoreboard(Turtle):
    """Scoreboard."""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(TOP_POS)
        self.update_scoreboard(self.score)

    def update_scoreboard(self, loot):
        self.clear()
        self.score += loot
        self.goto(BOTTOM_POS)
        self.write(arg=f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.goto(TOP_POS)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard(self.score)
