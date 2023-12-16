import random
import time

iterations = 0
var = 10000
def generate_random_integers():
    lower_limit = 1
    upper_limit = var

    random_integers = random.sample(range(lower_limit, upper_limit + 1), upper_limit)

    return random_integers

def pad_numbers(input_list):
    if not input_list:
        return []

    # Find the maximum number of digits
    max_digits = max(len(str(num)) for num in input_list)

    # Format each number with leading zeros
    padded_list = [f"{num:0{max_digits}}" for num in input_list]

    return padded_list

my_list = pad_numbers(generate_random_integers())


def sort2(lst):

    max_digits = len(lst[0])
    buckets = [[] for _ in range(10)]

    for i in range(max_digits):
        for number in lst:
            digit = int(str(number)[-i]) if i < len(str(number)) else 0
            buckets[digit].append(number)

        lst = [num for bucket in buckets for num in bucket]
        buckets = [[] for _ in range(10)]

    return lst

print(my_list)

# Record the start time
start_time = time.time()

print(sort2(my_list))



# Record the end time
end_time = time.time()


elapsed_time = end_time - start_time

print(f"The process took {elapsed_time} seconds.")

