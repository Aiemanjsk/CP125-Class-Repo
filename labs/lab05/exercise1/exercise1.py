
def was_backward_detected(waypoints):
    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """

    
    for i in range(1, len(waypoints)):
        currentX, currentY, currentZ = waypoints[i]
        previousX, previousY, previousZ = waypoints[i-1]
        
        if currentX < previousX or currentY < previousY:
            return True

    return False
    pass


# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
