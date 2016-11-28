#create game w/ width 20 and height 20
class Grid(object):
	def __init__ (self, width = 20, height = 20):
		# create dictionary for grid
		self.grid = {}
		self.width = width
		self.height = height
		# pre-populate the grid w/ 2 nested for loops
		for x in range(width):
			for y in range(height):
				self.grid [(x,y)] = "no_move"
		print width 

	def get_width(self):
		return self.width

# Grid()


# ask player input for who is black and white


# write function to determine whose turn it is


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



class Gomoku(object):
	def __init__(self):
		self.grid = Grid()
		self.players = Players()
	def start_game(self):
		whose_turn = self.players.whose_turn()
		raw_input("It is %s's turn. Please enter a move: ")%whose_turn
		



# prompt player for move

turn_choice = raw_input("It's %s's turn") %black_player_name

# check if move is available and allowed

# insert move into dictionary

# write check_win function to see if a player has won 

# if no player has won, prompt next player for move


