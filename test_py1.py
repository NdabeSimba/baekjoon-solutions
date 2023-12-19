def solve_equation():
    equation = input("Enter an equation to solve (e.g., '2x + 5 = 10'): ")
    variable = input("Enter the variable to solve for: ")
    try:
        solution = eval(equation.replace(variable, "x"))
        print(f"The solution for {variable} is: {solution}")
    except (SyntaxError, NameError):
        print("Invalid equation or variable.")

solve_equation()