def MainFunction(data):
	phrases = data.split("\n")
	valid = 0

	for phrase in phrases:
		words = phrase.split(" ")
		if len(words) == len(set(words)):
			valid += 1

	print(valid)

file_object = open("4.txt", "r")
data = file_object.read()

MainFunction(data)