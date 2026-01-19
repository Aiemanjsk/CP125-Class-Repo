
def analyze_performance(lap_times):

    total_first_half = 0
    total_second_half = 0
    if len(lap_times) % 2 == 0:
        first_half = len(lap_times) // 2 
    else:
        first_half = len(lap_times) // 2 + 1
    for i in range(first_half):
        total_first_half += lap_times[i]
    average_first_half = total_first_half / (len(lap_times)/2)
    for j in range(first_half ,len(lap_times)):
        total_second_half += lap_times[j]
    average_second_half = total_second_half / (len(lap_times)/2)

    if average_first_half < average_second_half:
        return True
    else:
        return False
  
    pass


# Test
laps = [50, 55, 60, 65, 70]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
