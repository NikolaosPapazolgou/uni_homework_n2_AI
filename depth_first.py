import time
import utils


def state_to_tuple(state):
    """
    Converts a state into a tuple that can be added to a set for comparison.
    For example, we convert the 'symbols' list and 'divorce_result' to a tuple.
    """
    return tuple(state["symbols"]), tuple(state["divorce_result"])


def depth_first_search(initial_state, time_limit=20):
    """
    Performs a Depth-First Search (DFS) to find a goal state.

    Args:
        initial_state (dict): The starting state of the search.
        time_limit (int): Maximum time allowed for the search in seconds.

    Returns:
        tuple: (Final state, steps taken).
    """
    # Initialize variables
    stack = [initial_state]
    visited_states = set()
    steps = 0
    start_time = time.time()

    while stack:
        # Check for timeout
        if time.time() - start_time > time_limit:
            print("Search terminated due to timeout.")
            break

        # Pop the next state to explore from the stack
        current_state = stack.pop()
        steps += 1

        # Check if the current state is the goal state
        if utils.goal_state(current_state):
            print("Goal state reached!")
            return current_state, steps, time.time() - start_time

        # Mark the state as visited
        visited_states.add(state_to_tuple(current_state))

        # Get possible neighbor states
        neighbor_states = utils.possible_states(current_state)
        for neighbor in neighbor_states:
            # Add neighbors to the stack if not visited
            if state_to_tuple(neighbor) not in visited_states:
                stack.append(neighbor)

    print("Search completed without finding the goal state.")
