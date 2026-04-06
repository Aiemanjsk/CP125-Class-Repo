import pandas as pd


def high_performers(filename):
    df = pd.read_csv(filename)
    
    # Filter students scoring above 85 in all subjects
    filtered = df[
        (df["Math"] > 85) & 
        (df["Science"] > 85) & 
        (df["English"] > 85)
    ]
    
    # Extract names as a set
    names = set(filtered["Name"])
    
    # Count of high performers
    count = len(names)
    
    # Return result
    return {
        "count": count,
        "names": names
    }
    pass
