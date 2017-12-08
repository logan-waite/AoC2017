def MainFunction(data):
	numbers = map(int, data.split("\t"))
	print (numbers)

file_object = open("6.txt", "r")
data = file_object.read()

MainFunction(data)