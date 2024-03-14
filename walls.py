from turtle import Turtle


class Walls(Turtle):

	def __init__(self):
		super().__init__()
		self.pencolor("white")
		self.penup()
		self.speed("fastest")
		self.hideturtle()

	def draw_wall(self):
		self.goto(-280, -280)
		self.pendown()
		self.goto(280, -280)
		self.goto(280, 280)
		self.goto(-280, 280)
		self.goto(-280, -280)


