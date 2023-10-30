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



def list_of_lists_to_dict(input_list):
    result_dict = {}
    for y, row in enumerate(input_list):
        for x, item in enumerate(row):
            result_dict[(x, y)] = item
    print(result_dict)
    return result_dict

def get_key(list):
    key = []
    for i in list:
        key.append(i)
    return tuple(key)

def findAdiacentValues(var1, var2):

    try:
        AdiacentValue = (coordinates[0] + var1, coordinates[1] + var2)
        return dic_grid[AdiacentValue]

    except KeyError:
        #print('something aint right')
        AdiacentValue = 0
    return AdiacentValue


list_of_coordinates = get_coordinates(grid)
dic_grid = list_of_lists_to_dict(grid)


for i in list_of_coordinates:

    coordinates = get_key(i)

    value1 = findAdiacentValues(-1, 0)
    value2 = findAdiacentValues(-1, -1)
    value3 = findAdiacentValues(-1, 1)
    value4 = findAdiacentValues(0, -1)
    value5 = findAdiacentValues(0, 1)
    value6 = findAdiacentValues(1, 0)
    value7 = findAdiacentValues(1, -1)
    value8 = findAdiacentValues(1, 1)

    totValues = value8 + value7 + value6 + value5 + value4 + value3 + value2 + value1

    if totValues == 2 or totValues == 3:
        dic_grid[coordinates] = 1
    else:
        dic_grid[coordinates] = 0

