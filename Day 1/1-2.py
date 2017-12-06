# in a sequence of digits, find the sum of all digits that match the digit halfway around the circle.
# EX: 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
# EX: 1221 produces 0, because every comparison is between a 1 and a 2.
# EX: 123425 produces 4, because both 2s match each other, but no other digit has a match.
# EX: 123123 produces 12.
# EX: 12131415 produces 4.

def RunCaptcha(data):
    first_number = data[0]
    steps = len(data)/2
    counter = 0;
    matching_number_list = list()
    past_half = 0

    for number in data:
        # if counter < len(data) - 1:
        #     if number == data[counter + 1]:
        #         matching_number_list.append(int(number))
        # else:
        #     print(number)
        #     if number == data[0]:
        #         matching_number_list.append(int(number))
        target_pos = counter + steps
        if target_pos < len(data):
            if number == data[target_pos]:
                matching_number_list.append(int(number))
        elif target_pos >= len(data):
            if number == data[past_half]:
                matching_number_list.append(int(number))
            past_half += 1
        counter += 1

    print("final result is: " +str(sum(matching_number_list)))

file_object = open("1.txt", "r")
data = file_object.read()

RunCaptcha(data);
