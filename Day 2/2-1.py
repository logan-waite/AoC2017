def Checksum(data):
    rows = data.split("\n")
    num_diffs = list()
    for row in rows:
        numbers = map(int, row.split("\t"))

        num_diffs.append(max(numbers) - min(numbers))
    print(sum(num_diffs))


file_object = open("2.txt", "r")
data = file_object.read()

Checksum(data)