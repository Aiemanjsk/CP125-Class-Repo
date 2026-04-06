import pandas as pd
import matplotlib.pyplot as plt

def plot_subject_maximums(filename):
    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]
    max_scores = [0, 0, 0, 0, 0]
    student_count = 0

    with open(filename, 'r') as file:
        lines = file.readlines()

        # Skip header
        for line in lines[1:]:
            parts = line.strip().split(',')
            student_count += 1

            for i in range(len(subjects)):
                score = float(parts[i])
                if score > max_scores[i]:
                    max_scores[i] = score

    # Plot
    plt.figure()
    plt.plot(subjects, max_scores, marker='o')
    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    plt.show()
    return student_count

count = plot_subject_maximums("labs/labs09/data/students.csv")
# Chart window appears showing line plot of maximum scores
print(count)  # 25
pass
