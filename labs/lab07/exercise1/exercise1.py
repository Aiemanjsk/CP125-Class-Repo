def process_actions(catalog, actions):
    # TODO: Your code here
    for action, isbn in actions:
        # Skip if ISBN not in catalog
        if isbn not in catalog:
            continue

        if action == "BORROW":
            # Only decrement if copies are available
            if catalog[isbn] > 0:
                catalog[isbn] -= 1

        elif action == "RETURN":
            catalog[isbn] += 1

    return catalog
    pass



catalog = {
    "978-A": 2,
    "978-B": 0,
    "978-C": 1,
}
actions = [
    ("BORROW", "978-A"),
    ("BORROW", "978-A"),
    ("BORROW", "978-B"),
    ("RETURN", "978-B"),
    ("BORROW", "978-Z"),
]
result = process_actions(catalog, actions)
print(result)
