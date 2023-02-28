def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for entry, exit in permanence_period:
            if entry <= target_time and exit >= target_time:
                counter += 1
    except (Exception):
        return None
    return counter
