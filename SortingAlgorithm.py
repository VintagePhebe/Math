import random
import time

iterations = 0
var = 100
def generate_random_integers():
    lower_limit = 1
    upper_limit = var

    random_integers = random.sample(range(lower_limit, upper_limit + 1), upper_limit)

    return random_integers

random_integer_list = generate_random_integers()

def sort(lst):
    i = 0
    for number in lst:
        try:
            i += 1
            test = lst[i]
            if number > lst[i]:

                ram = lst[i]

                lst[i] = number
                lst[i - 1] = ram
        except IndexError:
            pass
    return lst



print(random_integer_list)

# Record the start time
start_time = time.time()


while not all(random_integer_list[i] <= random_integer_list[i + 1] for i in range(len(random_integer_list) - 1)):
    random_integer_list = sort(random_integer_list)
    iterations += 1


# Record the end time
end_time = time.time()
print(random_integer_list)

elapsed_time = end_time - start_time

print(f"The process took {elapsed_time} seconds.")
print(f'it took {iterations} iterations of the algorithm')


