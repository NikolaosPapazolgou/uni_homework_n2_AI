import time
import sys
import os
import utils
import hill_climbing as hc
import depth_first as dp


def main():
    start = time.time()  # Record the start time of the program execution.
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen for a clean output.
    correct_number_input = False  # Flag to check the validity of input arguments.

    # Check if the correct number of input arguments is provided.
    if len(sys.argv) == 4:
        correct_number_input = True
        method = sys.argv[1]  # Method to use, either 'hill' for hill climbing or 'depth' for depth-first search.
        input_file = sys.argv[2]  # Name of the input file containing the problem description.
        output_file = sys.argv[3]  # Name of the output file to save the solution.
    else:
        # Print usage instructions and exit if arguments are incorrect.
        sys.stdout.buffer.write(b'How to use : \n'
                                b'Provide 3 arguments \n'
                                b"<method> is either 'hill' or 'depth' (without the quotes) \n"
                                b"<inputfile> is the name of the file with the problem description \n"
                                b"<outputfile> is the name of the output file with the solution")
        sys.exit()  # Exit the program due to incorrect input.

    # Read and parse the problem description from the input file.
    data = utils.read_file(input_file)
    initial_state = utils.get_initial_state(data)  # Extract the initial state from the input data.

    # Execute the hill climbing algorithm if specified.
    if method.lower() == 'hill':
        final_state, steps, restarts, time_executed = hc.hill_climbing_with_exploration(initial_state)
        utils.print_results(final_state, time_executed)

    # Execute the depth-first search algorithm if specified.
    elif method.lower() == 'depth':
        final_state, steps, time_executed = dp.depth_first_search(initial_state)
        utils.print_results(final_state, time_executed)


if __name__ == '__main__':
    main()  # Entry point of the program.
