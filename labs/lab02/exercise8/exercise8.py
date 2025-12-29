def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    # TODO: Implement this
    bounce_height = 80/100 * current_height
    return bounce_height
    
    pass


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    # TODO: Implement this
    if height < 1:
        return True
    else:
        return False

    pass


def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    # TODO: Implement this
    bounce_count = 0
    while initial_height < 1:
        initial_height = 80/100 * initial_height
        bounce_count += 1
    return bounce_count
    pass


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    # TODO: Implement this
    if initial_height == 1:
        distance = 0
        total_distance = 18
    e
    
    pass
