# in a sequence of digits, find the sum of all digits that match the following digit. The digit after the last digit is the first digit
# EX: 1122 produces 3 (1 + 2 = 3) because the first digit matches the second and the third matches the fourth
# EX: 1111 produces 4 because each digit matches the next one
# EX: 1234 produces 0 because no digit matches the next
# EX: 91212129 produces 9 because the only matching digit is the last one (to the first)

def RunCaptcha(data):
    first_number = data[0]
    counter = 0;
    matching_number_list = list()
    print(first_number)
    print(data[-1])
    print ("starting loop...")
    for number in data:
        if counter < len(data) - 1:
            if number == data[counter + 1]:
                matching_number_list.append(int(number))
        else:
            print(number)
            if number == data[0]:
                print("last matches first!" + str(number))
                matching_number_list.append(int(number))
        counter += 1

    print("final result is: " +str(sum(matching_number_list)))

file_object = open("1.txt", "r")
data = file_object.read()

RunCaptcha(data);
