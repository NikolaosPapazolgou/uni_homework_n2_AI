import time
import sys
import os
import utils


def main():
    start = time.time()  #Start Time.
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear Terminal
    correct_number_input = False
    print(sys.argv)

    # Check if the input arguments from the terminal are correct.
    if len(sys.argv) == 4:
        correct_number_input = True
        method = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]
    else:
        sys.stdout.buffer.write(b'How to use : \n'
                                b'Provide 3 arguments \n'
                                b"<method> is either 'hill' or 'depth' (without the quotes) \n"
                                b"<inputfile> is the name of the file with the problem description \n"
                                b"<outputfile> is the name of the output file with the solution")
        sys.exit()
    # Loads the problem. (Reads the input file and returns the content in a list format.)
    data = utils.read_file(input_file)
    print(f"DATA: {data}")
    # Process the data list into an initial_state list
    initial_state = utils.get_initial_state(data)
    print(f"Number of symbols (N):{initial_state['number'][0]}")
    print(f"Number of divorces (M):{initial_state['number'][1]}")
    print(f"Number of terms (K):{initial_state['number'][2]}")
    print(f"INITIAL STATE: {initial_state['initial_state']}")
    print(f"RESULT: {initial_state['divorce_result']}")
    print(f"Symbols: {initial_state['symbols']}")


if __name__ == '__main__':
    main()