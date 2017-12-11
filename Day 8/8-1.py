import operator

def MainFunction(data):
	lines = data.split("\n")
	registers = dict()
	for line in lines:
		items = line.split(" ")
		# item 0: variable being acted upon
		# item 1: operation (dec/inc) performed on item 0
		# item 2: amount applied to item 0
		# item 3: if
		# item 4: variable to check
		# item 5: boolean operation
		# item 6: number to check against item 4

		# Make sure both variables are in the dictionary.
		# If one isn't, put it in with a starting value of 0
		if items[0] not in registers:
			registers[items[0]] = 0

		if items[4] not in registers:
			registers[items[4]] = 0

		# now check the validity of the 
		# boolean statement present in items 4 - 6
		isTrue = CheckBoolean(registers[items[4]], int(items[6]), items[5])

		# if the statement is true, apply change to register
		if isTrue:
			if items[1] == "dec":
				registers[items[0]] -= int(items[2])
			elif items[1] == "inc":
				registers[items[0]] += int(items[2])
			else:
				print("I'm just broken at this point")

	max_key = max(registers, key=lambda key: registers[key])
	print(max_key, registers[max_key])


def CheckBoolean(a, b, op):
	if op == "==":
		return a == b
	elif op == "!=":
		return a != b
	elif op == "<":
		return a < b
	elif op == ">":
		return a > b
	elif op == "<=":
		return a <= b
	elif op == ">=":
		return a >= b
	else:
		print("i'm breaking here now")


file_object = open("8.txt", "r")
data = file_object.read()

MainFunction(data)