import sys


grid ={}
for x in range(1, 11):
	for y in range(1, 11):
		grid[(x,y)] = " "

def make_grid_line():
	line = ""
	for y in range(10):
		line = line + "+---------" 
	return line + "+ \n"

def get_coordinate_value(x, y):
	if grid[(x,y)] == " ":
		return "| (%s,%s) " % (format_number(x), format_number(y))
	elif grid[(x,y)] == "b":
		return "|    b    "
	elif grid[(x,y)] == "w":
		return "|    w    "
	else:
		return "error"


def format_number(num):
	if num <10:
		return " %i" %num
	else:
		return num

def make_grid():
	for y in range(1, 11):
		sys.stdout.write(make_grid_line())	
		for x in range(1, 11):
			sys.stdout.write (get_coordinate_value(x, y))
			if x == 10:
				sys.stdout.write("|\n")
	sys.stdout.write(make_grid_line())			

make_grid()


class Players(object):
	def __init__(self):
		self.black_player = "Black Player"
		self.white_player = "White Player"
		self.turn_count = 0

	def get_black_player_name(self):
		return self.black_player

	def get_white_player_name(self):
		return self.white_player

	def whose_turn(self):
		if self.turn_count % 2 == 0:
			return self.black_player
		else:
			return self.white_player

	def player_name_abbr(self):
		return self.whose_turn()[0].lower()


class PlayGame(Players):
	def start_the_game(self):
		print "To exit the game, type 'exit.'"
		print "To read game instructions, write 'instructions.'"
		print "Decide who will be the black player and who will be the white player. Black always goes first."
		print "Please type in the x and y coordinate of the space where you would like to play."
		while True:
			self.make_a_move()

	def make_a_move(self):
		who_plays_now = self.whose_turn()
		print "It is now the %s's turn" % (who_plays_now) 
		move_input_x = self.parse_input("x coordinate: ")
		move_input_y = self.parse_input("y coordinate: ")
		print "You have chosen spot (%s,%s)" % (move_input_x, move_input_y)
		if valid_move(move_input_x, move_input_y) == 
			if grid[(move_input_x,move_input_y)] == " ":
				grid[(move_input_x, move_input_y)] = self.player_name_abbr()
				self.turn_count = self.turn_count + 1
			else:
				print "ERROR: There is already a piece in that location."
				make_grid()
		make_grid()

	def parse_input(self, question):
		input = raw_input(question)
		if input.lower() == "exit":
			sys.exit()
		try:
			return int(input)
		except ValueError:
			print "ERROR: Not a valid input. Please type an integer that appears on the board."
			self.parse.input(question)
		else:
			return int(input)
			

	def valid_move(x,y):
		try:
			grid[(move_input_x,move_input_y)]
		except KeyError:
			print "ERROR: Move must be within the grid"
			self.make_a_move()



play_game = PlayGame()
play_game.start_the_game()


