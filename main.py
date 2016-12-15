import grid

def main():
	make_grid = grid.Grid()
	make_grid.make_grid()
	play_game = grid.PlayGame()
	play_game.start_the_game()


if __name__ == '__main__':
	main()