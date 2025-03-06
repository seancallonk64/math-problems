import random
import math

def solve_math_problem(problem):
    # Check if problem is already solved
    if "solved" in problem:
        return problem["solution"]
    
    # Get the type of problem
    problem_type = problem["type"]
    
    # Generate a random solution
    if problem_type == "addition":
        solution = random.randint(problem["min"], problem["max"]) + random.randint(problem["min"], problem["max"])
    elif problem_type == "subtraction":
        solution = random.randint(problem["min"], problem["max"]) - random.randint(problem["min"], problem["max"])
    elif problem_type == "multiplication":
        solution = random.randint(problem["min"], problem["max"]) * random.randint(problem["min"], problem["max"])
    else: # problem_type == "division"
        solution = random.randint(problem["min"], problem["max"]) // random.randint(problem["min"], problem["max"])
    
    # Save the solution to the problem dictionary
    problem["solved"] = True
    problem["solution"] = solution
    
    return solution
