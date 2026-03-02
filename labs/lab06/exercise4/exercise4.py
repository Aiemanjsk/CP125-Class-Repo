def synchronize_databases(legacy_list, modern_set, blacklist):
        # Step 1: Sanitize legacy data (remove blacklisted emails)
    sanitized_legacy_ids = {
        record_id
        for record_id, email in legacy_list
        if email not in blacklist
    }

    # Step 2: IDs in legacy but missing in modern → lost
    lost_set = sanitized_legacy_ids - modern_set

    # Step 3: IDs in modern but not in sanitized legacy → ghost
    ghost_set = modern_set - sanitized_legacy_ids

    return (lost_set, ghost_set)
    pass
