import time
import utils
import random


def state_to_tuple(state):
    """
    Converts a state into a tuple that can be added to a set for comparison.
    This function is essential for ensuring that states can be uniquely identified
    and checked for duplicates when traversing or exploring potential solutions.
    For example, we convert the 'symbols' list and 'divorce_result' to a tuple.
    """
    return tuple(state["symbols"]), tuple(state["divorce_result"])


def hill_climbing_with_exploration(initial_state, max_restarts=50, exploration_factor=0.1, time_limit=20):
    current_state = initial_state
    steps = 0
    restarts = 0
    visited_states = set()

    start_time = time.time()

    visited_states.add(state_to_tuple(current_state))

    if utils.goal_state(current_state):
        print("Goal state reached!")
        return current_state, steps, restarts

    while not utils.goal_state(current_state):
        neighbor_states = utils.possible_states(current_state)

        best_state = current_state
        best_heuristic = utils.heuristic_function(current_state)

        for neighbor in neighbor_states:
            neighbor_tuple = state_to_tuple(neighbor)

            if neighbor_tuple in visited_states:
                continue

            h = utils.heuristic_function(neighbor)

            if h > best_heuristic:
                best_heuristic = h
                best_state = neighbor
        # If no improvement is made, we restart with some exploration
        if best_state["symbols"] == current_state["symbols"]:
            restarts += 1
            print(f"No improvement found. Restarting... ({restarts}/{max_restarts})")

            if restarts >= max_restarts:
                print("Max restarts reached. Exiting.")
                break

            # Add exploration by adding some randomness to the current state
            if random.random() < exploration_factor:  # Chance to explore
                print("Exploring alternative state...")
                current_state = utils.random_initialize_symbols(current_state)
            else:
                current_state = utils.random_initialize_symbols(current_state)

            visited_states = set()
            visited_states.add(state_to_tuple(current_state))
            steps += 1
            continue

        # Otherwise, update current state to the best neighbor
        current_state = best_state
        visited_states.add(state_to_tuple(current_state))
        steps += 1

        if time.time() - start_time > time_limit:
            print("Time limit reached.")
            break

    if utils.goal_state(current_state):
        print("Goal state found!")
    else:
        print("Hill climbing stopped due to timeout or other reason.")

    print(f"Steps taken: {steps}, Restarts: {restarts}")
    return current_state, steps, restarts, time.time() - start_time


"""
    Returns:
        current_state (dict): The final state reached by the algorithm.
        steps (int): The total number of steps taken to reach the result.
        restarts (int): The number of times the algorithm restarted due to lack of progress.
        elapsed_time (float): The time elapsed during the algorithm execution.
"""
