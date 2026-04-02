# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    # TODO: Implement this function
    import csv
    scores = open(input_file, mode = "r", newline = "")
    grades = open(output_file, mode = "w", newline = "")
    read_score = csv.reader(scores)
    write_grade = csv.writer(grades)
    next(read_score)
    total_score = 0
    total = 0
    write_grade.writerow(["student_id", "final_grade"])
    for grade in read_score:
        final_grade = (float(grade[1]) * 0.4) + (float(grade[2]) * 0.6)
        total += 1
        total_score += final_grade 
    write_grade.writerow([grade[0], format(final_grade, ".2f")])
    average = total_score / total
    
    scores.close()
    grades.close()
    return average

    

    pass


# Test your code here
result = calculate_final_grades("Labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
