def get_legit_power_users(log_data, bot_ids, threshold):
    user_actions = {}

    # Process logs
    for timestamp, user_id, action_type in log_data:
        # Skip bots
        if user_id in bot_ids:
            continue

        # Initialize set for user if not already present
        if user_id not in user_actions:
            user_actions[user_id] = set()

        # Add action to user's set of unique actions
        user_actions[user_id].add(action_type)

    # Filter users exceeding the threshold
    power_users = [
        user_id
        for user_id, actions in user_actions.items()
        if len(actions) > threshold
    ]

    return sorted(power_users)
    pass
