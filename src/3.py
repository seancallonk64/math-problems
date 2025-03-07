import random

def solve_math_problem(problem):
    """
    Solves a math problem using Python.

    Args:
        problem (str): The math problem to be solved.

    Returns:
        int: The solution to the math problem.
    """
    # Split the problem into individual operations
    operations = problem.split(" ")

    # Perform each operation and store the result in a variable
    for i, op in enumerate(operations):
        if op == "+":
            operations[i] = int(operations[i - 1]) + int(operations[i + 1])
        elif op == "-":
            operations[i] = int(operations[i - 1]) - int(operations[i + 1])
        elif op == "*":
            operations[i] = int(operations[i - 1]) * int(operations[i + 1])
        else:
            raise ValueError("Unsupported operation")

    # Return the final result of the problem
    return operations[-1]
