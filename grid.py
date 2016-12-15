import sys

num_cells = 18

class Grid(object):
	def __init__ (self, num_cells=18):
		self.num_cells = num_cells
		self.grid = {}
		# pre-populate the grid w/ 2 nested for loops
		for x in range(1, num_cells+1):
			for y in range(1, num_cells+1):
				self.grid[(x,y)] = " "

	def make_grid_line(self):
		line = ""
		for y in range(num_cells):
			line = line + "+---------" 
		return line + "+ \n"

	def get_coordinate_value(self,x, y):
		if self.grid[(x,y)] == " ":
			return "| (%s,%s) " % (self.format_number(x), self.format_number(y))
		elif self.grid[(x,y)] == "b":
			return "|    B    "
		elif self.grid[(x,y)] == "w":
			return "|    w    "
		else:
			return "error"


	def format_number(self,num):
		if num <10:
			return " %i" %num
		else:
			return num

	def make_grid(self):
		for y in range(1, num_cells+1):
			sys.stdout.write(self.make_grid_line())	
			for x in range(1, num_cells+1):
				sys.stdout.write (self.get_coordinate_value(x, y))
				if x == num_cells:
					sys.stdout.write("|\n")
		sys.stdout.write(self.make_grid_line())			

# make_grid = Grid()
# make_grid.make_grid()


class Players(Grid):
	def __init__(self):
		self.black_player = "Black Player"
		self.white_player = "White Player"
		self.turn_count = 0
		super(Players, self).__init__()

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
		if self.valid_move(move_input_x, move_input_y) == move_input_x:
			if self.grid[(move_input_x,move_input_y)] == " ":
				self.grid[(move_input_x, move_input_y)] = self.player_name_abbr()
				self.turn_count = self.turn_count + 1
			else:
				print "ERROR: There is already a piece in that location."
				self.make_grid()
		self.check_all_wins(move_input_x,move_input_y)
		self.make_grid()

	def parse_input(self, question):
		input = raw_input(question)
		if input.lower() == "exit":
			sys.exit()
		try:
			return int(input)
		except ValueError:
			print "ERROR: Not a valid input. Please type an integer that appears on the board."
			return self.parse_input(question)
		else:
			return int(input)
			

	def valid_move(self, x,y):
		try:
			self.grid[(x, y)]
			return x
		except KeyError:
			print "ERROR: Move must be within the grid"
			self.make_a_move()

	def check_all_wins(self,x,y):
		if self.check_win_horizontal(x,y) or self.check_win_vertical(x,y) or self.check_win_diagonal(x,y) or self.check_win_diagonal_downslope(x,y) == True:
			print "You won!"
			sys.exit()
		else:
			pass

	def check_win_horizontal(self,x,y):
		for x in range(1, num_cells-4):
			for y in range(1, num_cells-4):
				if(self.grid[(x,y)]!= " " and self.grid[(x,y)] == self.grid[(x+1, y)] == self.grid[(x+2, y)] == self.grid[(x+3,y)] == self.grid[(x+4,y)]):
					return x
				else:
					pass
					
	def check_win_vertical(self,x,y):
		for x in range(1, num_cells-4):
			for y in range(1, num_cells-4):
				if(self.grid[(x,y)]!= " " and self.grid[(x,y)] == self.grid[(x, y+1)] == self.grid[(x, y+2)] == self.grid[(x,y+3)] == self.grid[(x,y+4)]):
					return x
				else:
					pass

	def check_win_diagonal(self, x, y):
		for x in range(1, num_cells-4):
			for y in range(1, num_cells-4):
				if(self.grid[(x,y)]!= " " and self.grid[(x,y)] == self.grid[(x+1, y+1)] == self.grid[(x+2, y+2)] == self.grid[(x+3,y+3)] == self.grid[(x+4,y+4)]):
					return x
				else:
					pass

	def check_win_diagonal_downslope(self, x, y):
		for x in range(1, num_cells-4):
			for y in range(1, num_cells-4):
				if(self.grid[(x,y)]!= " " and self.grid[(x,y)] == self.grid[(x-1, y+1)] == self.grid[(x-2, y+2)] == self.grid[(x-3,y+3)] == self.grid[(x-4,y+4)]):
					return x
				else:
					pass						
# play_game = PlayGame()
# play_game.start_the_game()


