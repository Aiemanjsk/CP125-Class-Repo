def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """

    MAX_CAPACITY = 7
    MIN_THRESHOLD = 5

    # Step 1: Process drops
    for student in drop_requests:
        enrolled.discard(student)  # discard avoids errors if name not present

    # Step 2: If below minimum, refill from waitlist
    if len(enrolled) < MIN_THRESHOLD:
        while len(enrolled) < MAX_CAPACITY and waitlist:
            enrolled.add(waitlist.pop())  # random element from set

    # Step 3: Return final count
    return len(enrolled)
    pass
