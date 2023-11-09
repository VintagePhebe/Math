grid = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def get_coordinates(grid):
    x = -1
    y = -1
    container_list = []
    for list in grid:
        x += 1
        for value in list:
            y += 1
            if value == 1:
                container_list.append([y, x])
        y = -1
    print(container_list)
    return container_list
def findAdiacentValues(var1, var2, ncoordinates):

    try:
        AdiacentValue = grid[ncoordinates[0] + var1][ncoordinates[1] + var2]

    except KeyError:
        #print('something aint right')
        AdiacentValue = 0

    return AdiacentValue


coordinates = get_coordinates(grid)

print(grid)

itr = 0
for i in coordinates:


    value1 = findAdiacentValues(-1, 0, i)
    value2 = findAdiacentValues(-1, -1, i)
    value3 = findAdiacentValues(-1, 1, i)
    value4 = findAdiacentValues(0, -1, i)
    value5 = findAdiacentValues(0, 1, i)
    value6 = findAdiacentValues(1, 0, i)
    value7 = findAdiacentValues(1, -1, i)
    value8 = findAdiacentValues(1, 1, i)

    totValues = value8 + value7 + value6 + value5 + value4 + value3 + value2 + value1

    if totValues == 2 or totValues == 3:
        grid[coordinates[0]][coordinates[1]] = 1
    else:
        grid[coordinates[itr][0]][coordinates[itr][1]] = 0

    itr += 1

print(itr)
print(grid)
