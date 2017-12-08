def MainFunction(data):
	jumps = map(int, data.split("\n"))
	current_pos = 0
	steps = 1

	while True:
		jump = jumps[current_pos]
		jumps[current_pos] += 1
		current_pos += jump
		if current_pos >= len(jumps):
			print(steps)
			break
		steps += 1

file_object = open("5.txt", "r")
data = file_object.read()

MainFunction(data)