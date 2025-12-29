
def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    # TODO: Implement this function
    usage = (15/100 * 10) * (distance/10)
    return usage
    pass

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    # TODO: Implement this function
    if is_sport_mode:
        current_battery = usage * 1.5
    else:
        current_battery = usage
    return current_battery
    pass

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    # TODO: Implement this function
    usage = (15/100 * 10) * (distance/10)
    if is_sport_mode:
        round_trip = (usage * 1.5) * 2
    else:
        round_trip = usage * 2
    if current_battery >= round_trip:
        return True
    else:
        return False
    pass
