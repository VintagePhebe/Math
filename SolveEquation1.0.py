from sympy import *
import re

init_printing(use_unicode=True)

def solve_equation(input_equation):
    def extract_known_number(polynomial):
        # Regular expression pattern to extract known numbers (e.g., -5, +7, etc.)
        pattern = r"[yx]\s?([+\-]\s?\d+)"

        try:
            polynomial = str(polynomial)
        except:
            pass

        matches = re.findall(pattern, polynomial)
        if matches:
            # Return the last matched known number
            return matches[-1]
        else:
            return 'error'

    def invert_signs(number):
        # Function to invert the signs of a number (e.g., -5 becomes +5)
        inverted_number = number.replace('-', '+')
        inverted_number = inverted_number.replace('+', '-')
        return inverted_number

    def replace_known_number(equation, known_number):
        # Replace the right-hand side of the equation with the known_number
        known_number_inverted = invert_signs(known_number)
        pattern = "[-+]\s\d+"

        try:
            equation_str = str(equation)
        except:
            print('error')
            pass

        matches = re.findall(pattern, equation_str)
        if matches:
            last_match = matches[-1]
            equation_str = equation_str.replace(last_match, '')
            new_equation = f'{equation_str} = {known_number_inverted}'
            return new_equation
        else:
            print('error')

    def add_multiplication_signs(expression):
        # Remove unnecessary multiplication signs
        pattern = r"(\d+|\w)(\w|[\(\[\{])"
        modified_expression = re.sub(pattern, r'\1 * \2', expression)
        return modified_expression

    def normalize_equation(equation):
        # Normalize the equation by putting it in the form m - n = 0
        left_side, right_side = equation.split('=')
        return f'{left_side.strip()} - ({right_side.strip()})'

    def simplify_equation(equation):
        # Simplify the equation using SymPy
        result = add_multiplication_signs(equation)
        final_result = simplify(result)
        return final_result

    def split_equation(expression):
        # Split the equation into two sides separated by the equals sign
        sides = expression.split('=')
        return f'{simplify_equation(sides[0])} = {simplify_equation(sides[1])}'

    def remove_moltiplication(x):
        y = x.replace('*', '')
        return y

    normalized_equation = normalize_equation(split_equation(input_equation))
    simplified_equation = simplify_equation(normalized_equation)
    known_number = extract_known_number(simplified_equation)
    equation_with_known_number = replace_known_number(simplified_equation, known_number)
    simplified_equation = add_multiplication_signs(equation_with_known_number)
    final_equation = remove_moltiplication(simplified_equation)
    print(f'\033[93mthe simplification of your equation is:\t\033[92m{final_equation}')

x, y = symbols('x y')

equation_input = input('Enter your equation: ')
solve_equation(equation_input)

