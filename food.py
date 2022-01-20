from turtle import Turtle
from random import randint, choice

FOOD_LOOT_TABLE = [1, 1, 1, 1, 5]


class Food(Turtle):
    """Food that appears at a random location on the screen."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.9)
        self.color("turquoise")
        self.speed("fastest")
        self.loot = 1
        self.refresh()

    def refresh(self):
        self.loot = choice(FOOD_LOOT_TABLE)
        if self.loot == 5:
            self.shape("turtle")
            self.color("SeaGreen")
        else:
            self.shape("circle")
            self.color("turquoise")
        rand_x = randint(-13, 13) * 20
        rand_y = randint(-13, 13) * 20
        self.goto(rand_x, rand_y)
