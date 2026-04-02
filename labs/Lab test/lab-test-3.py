import csv
def calculate_average_height(input_file):
    input = open(input_file, mode = 'r', newline = '')
    input.newline()
    print(input)
    input.close()

calculate_average_height("labs/Lab_test/bmi.csv")