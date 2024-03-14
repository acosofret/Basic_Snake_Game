from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.speed("fastest")
		self.penup()
		self.goto(0, 280)
		self.hideturtle()
		self.score = 0
		with open("/Users/ACoso/Desktop/data.txt", mode="r") as data_file:
			self.high_score = int(data_file.read())
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open ("C:/Users/ACoso/Desktop/data.txt", mode="w") as data_file:
				data_file.write(f"{self.high_score}")
		self.score = 0
		self.update_scoreboard()



	# def game_over(self):
	# 	self.clear()
	# 	self.goto(0, 20)
	# 	self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)
	# 	self.goto(0, -20)
	# 	self.write(f"Your final score: {self.score}", align=ALIGNMENT, font=FONT)

