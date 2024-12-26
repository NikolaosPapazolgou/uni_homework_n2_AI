import copy
import random


def read_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        raw_data = file.readlines()
        for line in raw_data:
            data.append(line.strip('\n'))
    return data


def random_initialize_symbols(state):
    """
    Randomly initializes the 'symbols' list in the state to boolean values (True or False).

    Parameters:
    - state: The state dictionary containing the 'symbols' list to be initialized.

    Returns:
    - state: The updated state with the 'symbols' list randomly initialized.
    """
    # Randomly initialize the 'symbols' list with True or False for each element
    print(f"STATE BEFORE: {state}")
    state["symbols"] = [random.choice([True, False]) for _ in state["symbols"]]
    update_result_list(state)
    print(f"State AFTER: {state}")
    return state


def get_initial_state(data):
    number_symbols_divorces_terms = [int(char_num) for index, string_line in enumerate(data) for char_num in
                                     string_line.split() if index == 0]
    initial_state = []
    temp_list = []
    divorce_result = []
    temp_state = [int(char_num) for index, line_string in enumerate(data) for char_num in line_string.split() if
                  index != 0]
    # Initialize symbols list with True values.
    symbols = [random.choice([True, False]) for _ in range(number_symbols_divorces_terms[0])]

    for index, symbol_number in enumerate(temp_state):
        temp_list.append(symbol_number)
        if (index + 1) % number_symbols_divorces_terms[2] == 0:
            initial_state.append(temp_list)
            temp_list = []

    for divorce_index, divorce_proposition in enumerate(initial_state):
        false_divorce = True
        for term_index in divorce_proposition:
            if term_index < 0:
                false_divorce = False
                divorce_result.append(false_divorce)
                break
        if false_divorce:
            divorce_result.append(false_divorce)

    final_state = {"number": number_symbols_divorces_terms, "symbols": symbols, "initial_state": initial_state,
                   "divorce_result": divorce_result}
    return final_state


# INPUTS: The dictionary that contains (1) Symbols list (2) Divorces Propositions
# GOAL: Synchronizes the values of the divorce_result of a new propositional_symbols values corresponding
# to divorce_propositions
def update_result_list(current_state):
    """
    Synchronizes the values of `divorce_result` in `current_state`
    based on `symbols` and `divorces_state`.
    """
    symbols = current_state["symbols"]
    divorces_state = current_state["initial_state"]  # Assuming it's a list of divorce propositions

    # Ensure `divorce_result` is initialized to the correct size
    if "divorce_result" not in current_state or not isinstance(current_state["divorce_result"], list):
        current_state["divorce_result"] = [False] * len(divorces_state)

    # Process each divorce proposition
    for divorce_index, divorce_proposition in enumerate(divorces_state):
        boolean_result = True  # Initialize for each proposition

        for number in divorce_proposition:
            # Get the value of the corresponding symbol
            current_boolean_value = symbols[abs(number) - 1]

            # If the number is negative, invert the symbol's value
            if number < 0:
                current_boolean_value = not current_boolean_value

            # Apply AND logic
            boolean_result = boolean_result or current_boolean_value

            # Short-circuit evaluation for efficiency
            if not boolean_result:
                break

        # Update the divorce_result for this proposition
        current_state["divorce_result"][divorce_index] = boolean_result
    return current_state["divorce_result"]


def goal_state(current_state):
    return all(current_state["divorce_result"])  # If all divorce propositions are satisfied returns true else false.


def possible_states(current_state):
    neighbor_states = []  # List of all possible states (dictionaries of states)
    symbols = []
    state_list = []
    for symbol_index, symbol_value in enumerate(current_state["symbols"]):
        # STEP (1): Create a shallow copy of the symbols list
        copy_symbols = copy.copy(current_state["symbols"])
        # STEP (2): Modify the copy by toggling the current symbol
        copy_symbols[symbol_index] = not symbol_value
        # STEP (3): Create a new state with the modified symbols
        state = {
            "number": current_state["number"],
            "symbols": copy_symbols,
            "divorce_result": current_state["divorce_result"][:],
            "initial_state": current_state["initial_state"]
        }

        # STEP (4): Update the result and append to neighbor_states
        state["divorce_result"] = update_result_list(state)
        # print(f"State {state}")
        neighbor_states.append(state)
    return neighbor_states


def heuristic_function(state):
    count_true = 0  # Counter of true divorce propositions.
    for divorce_result in state["divorce_result"]:  # Checks what boolean result each divorce proposition returns.
        if divorce_result:
            count_true += 1
    return count_true


def print_results(final_state, time_executed):
    print("Final state: ")  # Output the final state reached by the algorithm.
    print(f"Symbols : {final_state["symbols"]}")
    print(f"Divorce results: {final_state["divorce_result"]}")
    print("Execution time: ", time_executed)  # Output the total execution time.
    print(f"M(Number of Divorce propositions): {final_state["number"][1]}")
    print(f"N(Number of propositional Symbols): {final_state["number"][0]}")
    print(f"K(Number of terms per proposition): {final_state["number"][2]}")
