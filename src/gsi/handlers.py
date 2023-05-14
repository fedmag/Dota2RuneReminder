def clock_handler(last_state, state):
    if last_state is not None and state is not None:
        new_clock = state.get("map").get("clock_time")
        last_clock = last_state.get("map").get("clock_time")
        if last_clock != new_clock:
            # print(last_clock, new_clock)
            # print(new_clock)
            return new_clock
    return None