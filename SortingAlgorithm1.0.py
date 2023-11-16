import random
import time

iterations = 0
var = 10000
def generate_random_integers():
    lower_limit = 1
    upper_limit = var

    random_integers = random.sample(range(lower_limit, upper_limit + 1), upper_limit)

    return random_integers

my_list = generate_random_integers()

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



# Record the start time
start_time = time.time()


while not all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1)):
    my_list = sort(my_list)
    iterations += 1



# Record the end time
end_time = time.time()


elapsed_time = end_time - start_time

print(f"The process took {elapsed_time} seconds.")
print(f'it took {iterations} iterations of the algorithm')


