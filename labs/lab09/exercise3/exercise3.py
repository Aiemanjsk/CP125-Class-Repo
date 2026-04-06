import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df = pd.read_csv(filename)
    math = df['Math']  
    x = df.index
    y = math
    plt.plot(x, y)              
    plt.xlabel("Student Index") 
    plt.ylabel("Math Score")     
    plt.title("Math Scores Trends")     
    plt.show()    
    return len(df)
count = show_math_trend("labs/lab09/data/students.csv")
# Chart window appears showing Math scores
print(count)      
pass
