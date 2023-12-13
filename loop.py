# objective: write this function:
# def sum(x):
#     result = 0
#     for i in x:
#         result += i
#     return result

# without for or while loops

myList = [1, 2, 3, 4, 5]

def sum(lst):
    searchable = str(lst)
    numbers = searchable.replace(' ', '+')
    numbers = numbers.replace('[', '')
    numbers = numbers.replace(']', '')
    numbers = numbers.replace(',', '')
    result = eval(numbers)
    return result


sum = sum(myList)

print(sum)