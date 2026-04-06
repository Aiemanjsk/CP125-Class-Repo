import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    df = pd.read_csv(filename)
    score_science = df['Science']
    plt.hist(score_science, bins=10)  
    plt.xlabel("Score Range")
    plt.ylabel("Frequency")
    plt.title("Score Distribution")
    plt.show()
    return len(df)

count = show_science_distribution("labs/lab09/data/students.csv")
# Chart window appears showing Science score distribution
print(count)  # 25
pass
