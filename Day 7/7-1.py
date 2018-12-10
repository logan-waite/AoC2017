def MainFunction(data):
    print(data)

file_object = open("7.txt", "r")
data = file_object.read()

MainFunction(data)