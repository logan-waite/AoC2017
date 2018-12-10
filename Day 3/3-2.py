def MainFunction(data):
	goal = int(data)
	x = y = dx = 0
	dy = -1
	grid = {}

	coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

	while True:
		total = 0
		print(total)
		for offset in coords:
			ox, oy = offset
			if (x+ox, y+oy) in grid:
				total += grid[(x+ox, y+oy)]
		if total > int(data):
			print( str(total) )
			return 1
		if (x, y) == (0, 0):
			grid[(0, 0)] = 1
		else:
			grid[(x, y)] = total
		if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
			dx, dy = -dy, dx
		x, y = x+dx, y+dy

file_object = open("3.txt", "r")
data = file_object.read()

MainFunction(data)