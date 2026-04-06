import pandas as pd


def compare_averages(filename):
    df = pd.read_csv(filename)
    subjects = ["Math", "Science", "English"]
    average_math = round(df['Math'].mean(), 1)
    average_science = round(df['Science'].mean(), 1)
    average_english = round(df['English'].mean(), 1)
    
    

    pass
