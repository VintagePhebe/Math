# coso = '2x + 3y = 20'
# chese = '2x - 3y = 8'

# coso = '3x + 2y = 7'
# chese = '6x + 4x = 14'

coso = '6x - 2y = 5'
chese = '18x - 6y = -1'
def get_matrix(coefficents):
    matrix = []
    ram = ''
    for i in coefficents:
        if i != 'x' and i != 'y' and i != '=':
            ram += i
        elif i == 'x' or i == 'y':
            matrix.append(ram.replace(' ', ''))
            ram = ''
    else:
        matrix.append(ram.strip())
    print(matrix)
    return matrix

def transform_in_int(matrix):
    final_matrix = []
    for i in matrix:
        try:
            i = int(i)
            final_matrix.append(i)
        except:
            print('error')
    print(final_matrix)
    return final_matrix
def solve_system(m1, m2):
    check1 = m1[0]/m2[0]
    check2 = m1[1]/m2[1]
    check3 = m1[2]/m2[2]
    if check1 == check2 == check3:
        print('sistema indeterminato')

    elif check1 == check2 != check3:
        print('sistema impossibile')

    else:
        d = m1[0]*m2[1]-m2[0]*m1[1]
        dx = m1[2]*m2[1]-m2[2]*m1[1]
        dy = m1[0]*m2[2]-m2[0]*m1[2]

        x_value = dx / d
        y_value = dy / d

        print(f'd = {d}\ndx = {dx}\ndy = {dy}')
        print(f'x = {x_value}\ny = {y_value}')


matrix1 = transform_in_int(get_matrix(coso))
matrix2 = transform_in_int(get_matrix(chese))

solve_system(matrix1, matrix2)
