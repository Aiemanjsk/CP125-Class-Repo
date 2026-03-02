
def find_largest_drop(readings):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.    
    """
    largest_drop_found = 0
    drop_found = 0
    for i in range(len(readings)):
        if i == 0:
            continue
        if readings[i-1] > readings[i]:
            drop_found = readings[i-1] - readings[i]
        if drop_found > largest_drop_found:
            largest_drop_found = drop_found
        
    if largest_drop_found > 0:    
        return largest_drop_found
    else:
        return 0.0
    pass


# Test
temps = (20.0, 21.0, 22.0, 23.0)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
