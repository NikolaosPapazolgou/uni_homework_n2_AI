def read_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        raw_data = file.readlines()
        for line in raw_data:
            data.append(line.strip('\n'))
    return data


def get_initial_state(data):
    number_symbols_divorces_terms = [int(char_num) for index, string_line in enumerate(data) for char_num in
                                     string_line.split() if index == 0]
    initial_state = []
    temp_list = []
    divorce_result = []
    temp_state = [int(char_num) for index, line_string in enumerate(data) for char_num in line_string.split() if
                  index != 0]
    # Initialize symbols list with True values.
    symbols = [True for i in range(number_symbols_divorces_terms[0])]

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
def update_result_list():
    # PROCESS:
    # STEP (1): Iterate by each divorce-proposition
    # STEP (2): Access the corresponding element of the ith divorce-proposition
    # STEP (3): Find the ith element in the symbols list and return each value
    # STEP (4): If the ith element has a negative value then return the opposite value
    # of the corresponding element in the symbols list.
    # STEP (5): Before you access a new divorce-proposition add the resulting boolean value (that was extracted
    # via the process above) to the ith corresponding element of the divorce_result list in the state dictionary.
    return None
