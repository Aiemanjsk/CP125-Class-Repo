import csv
def calculate_average_height(input_file):
    user_input = open(input_file, mode = 'r', newline = '')
    input_read = csv.reader(user_input)
    next(input_read)
    total_height = 0
    count = 0
    #use for loop for count average
    for height in input_read:
        total_height += float(height[1])
        count += 1
        print(height)
    average = total_height / count
    user_input.close()
    print(average)

def add_new_data(output_file, input_file):
    user_input = open(input_file, mode = 'r', newline = '')
    output = open(output_file, mode = 'a', newline = '')
    input_read = csv.reader(user_input)
    next(input_read)
    #enter input and append on the same file
    gender = input("gender is: ")
    height = input("height is ")
    weight = input("weight is: ")
    bmi_index = input("BMI index is: ")
    output.append("/n" + gender, height, weight, bmi_index)
    user_input.close()
    output.close()
    print(output_write)


calculate_average_height("labs/Lab_test/bmi.csv")
add_new_data("labs/Lab_test/bmi.csv", "labs/Lab_test/bmi.csv")