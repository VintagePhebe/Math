import random
import time

def generate_random_integers():
    lower_limit = 1
    upper_limit = 10000000

    random_integers_as_strings = [str(num) for num in random.sample(range(lower_limit, upper_limit + 1), upper_limit)]

    return random_integers_as_strings

def pad_numbers(input_list):
    if not input_list:
        return []

    # Find the maximum number of digits
    max_digits = max(len(str(num)) for num in input_list)

    # Format each number with leading zeros
    padded_list = [f"{num:0{max_digits}}" for num in input_list]

    return padded_list

my_list = generate_random_integers()


def sort(lst):

    max_digits = max(len(num) for num in lst)
    buckets = [[] for _ in range(10)]

    for i in range(1, max_digits + 1):
        for number in lst:
            digit = int(number[-i]) if i <= len(number) else 0
            buckets[digit].append(number)

        lst = [num for bucket in buckets for num in bucket]
        buckets = [[] for _ in range(10)]

    return lst

print(my_list)

start_time = time.time()

###
sorted_list = sort(my_list)
#sorted_list = sorted(my_list)
###

end_time = time.time()


elapsed_time = end_time - start_time

print(sorted_list)
print(f"The process took {elapsed_time} seconds.")
