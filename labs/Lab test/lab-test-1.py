def determine_grade(students_mark):
    if students_mark >= 80:
        grade = "A"
    elif students_mark >= 60:
        grade = "B"
    elif students_mark >= 50:
        grade = "C"
    elif students_mark >= 40:
        grade = "D"
    elif students_mark >= 0:
        grade = "F"
    else:
        grade = "absent"
    return grade
    

print ("Mark: ", mark, "Grade:", determine_grade(float(input("Enter the student's mark: "))))