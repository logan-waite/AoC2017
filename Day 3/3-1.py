import math

def MainFunction(data):
	num = int(data)
	print("num" + str(num))

	found = False
	n = 1
	square = 0;
	square_distance = math.floor(n % 2)

	while not found:
		# find closest square
		if num <= n**2:
			square = n**2
			found = True
		else:
			n += 2

	distance_from_sq = square - num;

	if num == square:
		print("Steps: " + str(square_distance * 2))
		return 1

	for i in range(1,4):
		x = (n-1) * i
		print(square - x)
		if num > square - x: # inside this side
			middle = (square - x) + square_distance
			distance_to_middle = math.fabs( num - middle );
			print("Steps: " + str(distance_to_middle + square_distance))
		elif num == square - x: # in the corner
			print("Steps: " + str(square_distance * 2))
			break
		else:
			print("Not side " + str(i));

	return 1

#--------------
file_object = open("3.txt", "r")
data = file_object.read()

MainFunction(data)