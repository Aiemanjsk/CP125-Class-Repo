import pandas as pd


def explore_data(filename):
    df = pd.read_csv(filename)
    total_students = len(df)
    subject = ["math", "science", "english"]
    average_math = df.loc["math"].mean()
    round_avg_math = round(average_math, 1)
    highest_mark_math = df.loc(["math"].idmax(), "name")
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }

result = explore_data("data/students.csv")
print(result)
    pass
