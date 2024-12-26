import random


def walk_sat(formula, literals_symbols, max_flips=1000, p=0.5):
    """
    WalkSAT stochastic-local search Algorithm to determine SAT for a given CNF Formula.

    Parameters:
        - formula: List of clauses representing the CNF formula. Each clause is a list of integers.
        - clause_result: List of booleans representing the satisfaction status of each clause.
        - literals_symbols: List of booleans representing the truth values of the literals.
        - max_flips: Maximum number of flips to attempt before giving up.
        - p: Probability of making a random flip (0 < p <= 1).

    Returns:
         - literals_symbols: The satisfying assignment if the formula is satisfiable.
        - False: If no satisfying assignment is found within max_flips.
    """
    # STEP (1): Random initialization of literals.
    literals_symbols = [random.choice([True, False]) for literal in literals_symbols]

    for _ in range(max_flips):
        # Evaluate clauses result based on current assigment.
        clause_result = [
            any(literals_symbols[abs(literal) - 1] if literal > 0 else not literals_symbols[abs(literal) - 1]
                for literal in clause) for clause in formula]

        # If all clause are satisfied return the solution.
        if all(clause_result):
            return literals_symbols

        # STEP (2): Random pick a unsatisfied clause.
        unsatisfied_clause = [clause for clause_index, clause in enumerate(formula) if not clause_result[clause_index]]
        current_unsatisfied_clause = random.choice(unsatisfied_clause)

        # STEP (3): Probabilistic choice of literal in the chosen unsatisfied clause.
        if random.random() < p:
            # Random flip: Pick a random literal in the clause to flip.
            current_random_literal = random.choice(current_unsatisfied_clause)
            literals_symbols[abs(current_random_literal) - 1] = not literals_symbols[abs(current_random_literal) - 1]
        else:
            # Flip the literal that minimizes the number of unsatisfied clauses.
            best_literal = None
            min_unsatisfied_clauses = float('inf')
            for literal in current_unsatisfied_clause:
                # Flip the literal temporarily.
                literals_symbols[abs(literal) - 1] = not literals_symbols[abs(literal) - 1]

                # Count unsatisfied clauses after the flip.
                temp_clause_result = [
                    any(literals_symbols[abs(lit) - 1] if lit > 0 else not literals_symbols[abs(lit) - 1]
                        for lit in clause) for clause in formula]
                unsatisfied_count = sum(1 for satisfied in temp_clause_result if not satisfied)

                # Restore the literal to its original value.
                literals_symbols[abs(literal) - 1] = not literals_symbols[abs(literal) - 1]
                # Update best_literal if this flip minimizes unsatisfied clauses.
                if unsatisfied_count < min_unsatisfied_clauses:
                    min_unsatisfied_clauses = unsatisfied_count
                    best_literal = literal
            # Perform the best flip.
            if best_literal is not None:
                literals_symbols[abs(best_literal) - 1] = not literals_symbols[abs(best_literal) - 1]
    # If no satisfying assignment is found after max_flips, return False.
    return False


formula = [[1, -2, 3], [1, -3, -2], [1, 2, 3], [-1, -2, -3], [1, -3, -2]]
clause_result = [False, False, False, False, False]  # Initial clause satisfaction status
literals_symbols = [False, False, True]  # Initial truth assignment

solution = walk_sat(formula, literals_symbols)
if solution:
    print("Satisfying assignment found:", solution)
else:
    print("No satisfying assignment found.")
