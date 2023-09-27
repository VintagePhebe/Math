import re

iterations = -1
ram = 0
def split_equation(equation):
    # Utilizziamo espressioni regolari per suddividere l'equazione in numeri e segni
    pattern = r'(\d+\.?\d*|[A-Za-z]+|[\+\-\*/=])'
    tokens = re.findall(pattern, equation)

    # Rimuoviamo gli spazi vuoti dai token
    tokens = [token.strip() for token in tokens if not token.isspace()]

    # Convertiamo i token numerici in float
    for i, token in enumerate(tokens):
        if re.match(r'\d+(\.\d*)?$', token):
            tokens[i] = float(token)

    return tokens

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return True
def replace_and_remove_indices(lst, index, x):

    # Verifica se l'indice è valido
    if index >= 1 and index < len(lst):
        # Rimuove l'indice precedente
        del lst[index - 1]
        # Sostituisce l'indice specifico con x
        lst[index] = x
    return x
    #index -= 2

def remove_multiply_and_divide_indices(lst):
    lst[:] = [x for x in lst if x != '*' and x != '/']

def keep_last_element(lst):
    if len(lst) > 1:
        del lst[:-1]

def number_before():
    if is_float(tokens[iterations - 1]):
        x = tokens[iterations - 1]
    else:
        x = tokens[iterations - 2]
    return x
def number_after():
    if is_float(tokens[iterations + 1]):
        y = tokens[iterations + 1]
    else:
        y = tokens[iterations - 2]
    return y
def multi():
    x = number_before() * number_after()
    return replace_and_remove_indices(tokens, iterations, x)

def div():
    x = number_before() / number_after()
    return replace_and_remove_indices(tokens, iterations, x)
def sum():
    x = number_before() + number_after()
    return replace_and_remove_indices(tokens, iterations, x)
def sub():
    x = number_before() - number_after()
    return replace_and_remove_indices(tokens, iterations, x)

inp = input("Inserire l'espressione\t")

tokens = split_equation(inp)
#print(tokens)

for monomial in tokens:
    iterations += 1
    #print(ram)

    if monomial == '*':
        ram = multi()
    elif monomial == '/':
        ram = div()

remove_multiply_and_divide_indices(tokens)
iterations = -1

for monomial in tokens:
    iterations += 1
    #print(ram)

    if monomial == '+':
        ram = sum()
    elif monomial == '-':
        ram = sub()

keep_last_element(tokens)
result = tokens[0]

print(f'il risultato dell\'espressione è: {result}')
