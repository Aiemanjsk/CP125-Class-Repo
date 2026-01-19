
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    total_first_half = 0
    total_second_half = 0
    if len(times) % 2 == 0:
        first_half = len(times) // 2 
    else:
        first_half = len(times) // 2 + 1
    for i in range(first_half):
        total_first_half += times[i]
    average_first_half = total_first_half / (len(times)/2)
    for j in range(first_half ,len(times)):
        total_second_half += times[j]
    average_second_half = total_second_half / (len(times)/2)

    if average_first_half < average_second_half:
        return True
    else:
        return False
    
        

    pass


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
