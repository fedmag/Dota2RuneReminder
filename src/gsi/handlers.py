def clock_handler(last_state, state):
    if states_are_usable(last_state, state):
        new_clock = state.get("map").get("clock_time")
        last_clock = last_state.get("map").get("clock_time")
        if last_clock != new_clock:
            return new_clock
    return None

def states_are_usable(last_state, state):
    return last_state is not None and state is not None and state.get("map") is not None and last_state.get("map") is not None