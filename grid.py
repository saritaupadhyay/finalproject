import sys
sys.stdout.write('')

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
		return "(%s,%s)" % (format_number(x), format_number(y))
	elif grid[(x,y)] == "b":
		return "b"
	elif grid[(x,y)] == "w":
		return "w"
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
				

make_grid()
