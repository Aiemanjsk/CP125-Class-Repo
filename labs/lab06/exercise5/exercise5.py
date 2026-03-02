def audit_zero_trust(baseline_set, current_log_list):
    # Step 1: Convert logs to a set
   current_set = set(current_log_list)

    # Step 2: Authorized logins (present in both)
   authorized = baseline_set & current_set

    # Step 3: Alerts (in logs but not baseline)
   alerts = current_set - baseline_set

    # Step 4: Inactive (in baseline but not logs)
   inactive = baseline_set - current_set

   return (authorized, alerts, inactive)

   pass