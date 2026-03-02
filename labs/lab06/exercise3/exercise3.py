def audit_blocklists(list_a, list_b, list_c):
    universal = list_a & list_b & list_c

    # Redundant set: present in at least two lists
    redundant = (
        (list_a & list_b) |
        (list_a & list_c) |
        (list_b & list_c)
    )

    # Unique A set: present only in list A
    unique_a = list_a - list_b - list_c

    return (universal, redundant, unique_a)
    pass
