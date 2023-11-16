from sympy import symbols, expand, collect


def get_monomials(equation):
    # Define symbols
    x, y, z = symbols('x y z')

    # Parse the equation
    expr = eval(equation)

    # Expand the expression to ensure all terms are explicitly written
    expanded_expr = expand(expr)

    # Collect terms to group them by powers of variables
    collected_expr = collect(expanded_expr, [x, y, z])

    # Extract individual monomials
    monomials = [str(term) for term in collected_expr.as_ordered_terms()]

    return monomials

def simplify_monomials(matrix):
    simplified_monomials = []

    for monomial in matrix:

        new_monomial = monomial 
        # Remove '*' signs and letters
        simplified_monomial = ''.join(char for char in monomial if char.isdigit())
        simplified_monomials.append(simplified_monomial)

    return simplified_monomials

# Example usage



# Example usage
equation = "x**2 + 2*x*y + y**2 + 3*z"
result = get_monomials(equation)
print(result)

new_monomial = simplify_monomials(result)

print(result)