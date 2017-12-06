def Checksum(data):
    rows = data.split("\n")

file_object = open("2.txt", "r")
data = file_object.read()

Checksum(data)