def Checksum(data):
	rows = data.split("\n")
	divided_list = list()

	for row in rows:
		numbers = map(int, row.split("\t"))

		for number in numbers:
			array = [number / x for x in numbers if (number % x == 0) and (number != x)]
			if len(array) > 0:
				divided_list.append(array[0])

	print(sum(divided_list))

file_object = open("2.txt", "r")
data = file_object.read()

Checksum(data)