def MainFunction(data):
	numbers = map(int, data.split("\t"))
	updated_nums = list(numbers)
	number_sets = list()
	number_sets.append(numbers)

	iteration_counter = 1
	while True:
		# print (iteration_counter)

		max_num = max(updated_nums)
		max_num_index = updated_nums.index(max_num)
		index_counter = max_num_index + 1
		updated_nums[max_num_index] = 0
		matched = False

		while max_num > 0:
			if index_counter >= len(updated_nums):
				index_counter = 0
			updated_nums[index_counter] += 1
			max_num -= 1
			index_counter += 1

		for num_list in number_sets:
			# print("***")
			# print(updated_nums)
			# print(num_list)
			if CheckEqual(updated_nums, num_list):
				print ("Found Match!")
				print(updated_nums)
				print(num_list)
				print("Iterations: " + str(iteration_counter))
				print((len(number_sets) ) - number_sets.index(num_list))
				matched = True

		if matched or iteration_counter > 10000:
			break
		else:
			number_sets.append(list(updated_nums))
			iteration_counter += 1

def CheckEqual(one, two):
	if (len(one) == len(two)):
		for i, x in enumerate(one):
			y = two[i]
			if x == y:
				continue
			return False
		return True
	return False


file_object = open("6.txt", "r")
data = file_object.read()

MainFunction(data)