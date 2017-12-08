def MainFunction(data):
	phrases = data.split("\n")
	valid = 0

	for phrase in phrases:
		words = phrase.split(" ")
		ordered_words = list()
		for word in words:
			letters = sorted(list(word))
			new_word = "".join(letters)
			ordered_words.append(new_word)
		if len(ordered_words) == len(set(ordered_words)):
				valid += 1


	print(valid)

file_object = open("4.txt", "r")
data = file_object.read()

MainFunction(data)