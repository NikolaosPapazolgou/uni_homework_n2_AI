import random


def dpll(formula, assignment, depth=0):
    """
    DPLL Algorithm to determine SAT for a given formula.

    Parameters:
        - formula: A CNF formula represented as a list of clauses.
        - assignment: A dictionary storing the current variable assignments.
        - depth: Recursion depth for debugging purposes.

    Returns:
        - True and a satisfying assignment if the formula is satisfiable.
        - False otherwise.
    """
    # Debugging print
    print(f"Recursion Depth: {depth}, Current Assignment: {assignment}")
    print("Formula:", formula)

    # Base case: Check if the formula is satisfied
    if all([any([(literal > 0 and literal in assignment and assignment[literal]) or
                 (literal < 0 and -literal in assignment and not assignment[-literal])
                 for literal in clausee]) for clausee in formula]):
        return True, assignment

    # Check for a conflict
    if any([all([(literal > 0 and literal in assignment and not assignment[literal]) or
                 (literal < 0 and -literal in assignment and assignment[-literal])
                 for literal in clausee]) for clausee in formula]):
        return False, None

    # Unit propagation
    for clausee in formula:
        unassigned_literals = [literal for literal in clausee if abs(literal) not in assignment]
        if len(unassigned_literals) == 1:
            unit = unassigned_literals[0]
            assignment[abs(unit)] = unit > 0  # Assign True if positive, False if negative
            return dpll(formula, assignment, depth + 1)

    # Pure literal elimination
    literals = {literal for clausee in formula for literal in clausee}
    for literal in literals:
        if -literal not in literals:
            assignment[abs(literal)] = literal > 0  # Assign True if positive, False if negative
            return dpll(formula, assignment, depth + 1)

    # Choose a variable to branch
    for clausee in formula:
        for literal in clausee:
            if abs(literal) not in assignment:
                variable = abs(literal)
                break
        else:
            continue
        break

    # Branch on the variable
    assignment[variable] = True
    resultt, final_assignment = dpll(formula, assignment, depth + 1)
    if resultt:
        return resultt, final_assignment

    # Backtrack
    assignment[variable] = False
    return dpll(formula, assignment, depth + 1)




def generate_formula(num_clauses, num_literals, num_symbols):
    """
    Generate a random CNF formula for testing.

    Parameters:
        - num_clauses: Number of clauses in the formula.
        - num_literals: Number of literals per clause.
        - num_symbols: Number of propositional symbols.

    Returns:
        - formula: A CNF formula as a list of clauses.
    """
    symbols = list(range(1, num_symbols + 1))  # Propositional symbols are integers 1, 2, ..., num_symbols
    formula = []

    for _ in range(num_clauses):
        clause = []
        for _ in range(num_literals):
            literal = random.choice(symbols)  # Pick a random symbol
            if random.random() < 0.5:  # Randomly negate the literal
                literal = -literal
            clause.append(literal)
        formula.append(clause)

    return formula


# Generate a random formula
random_formula = generate_formula(num_clauses=10, num_literals=5, num_symbols=5)

# Initialize an empty assignment
initial_assignment = {}

# Print the formula
print("Generated CNF Formula:")
for clause in random_formula:
    print(clause)

# Test the DPLL algorithm
result, satisfying_assignment = dpll(random_formula, initial_assignment)

# Output the results
if result:
    print("\nSatisfiable Formula")
    print("Satisfying Assignment:", satisfying_assignment)
else:
    print("\nUnsatisfiable Formula")

