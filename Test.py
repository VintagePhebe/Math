my_list = [75, 57, 16, 44, 91, 18, 69, 98, 32, 13, 81, 8, 88, 71, 60, 83, 64, 86, 100, 38, 70, 1, 63, 31, 90, 21, 52, 24, 17, 92, 27, 22, 67, 9, 3, 2, 93, 48, 66, 35, 68, 59, 19, 79, 80, 51, 62, 49, 40, 55, 72, 10, 33, 36, 87, 56, 25, 82, 14, 46, 5, 89, 28, 30, 76, 58, 84, 29, 97, 6, 77, 85, 96, 74, 4, 94, 15, 39, 73, 47, 37, 53, 61, 11, 42, 50, 78, 41, 20, 26, 34, 23, 65, 54, 95, 99, 45, 12, 7, 43]


def pad_numbers(input_list):
    if not input_list:
        return []

    # Find the maximum number of digits
    max_digits = max(len(str(num)) for num in input_list)

    # Format each number with leading zeros
    padded_list = [f"{num:0{max_digits}}" for num in input_list]

    return padded_list

complete_list = pad_numbers(my_list)

def sort(lst):
    max_digits = len(lst[0])
    buckets = [[] for _ in range(10)]

    for i in range(max_digits):
        for number in lst:
            digit = int(str(number)[i]) if i < len(str(number)) else 0
            buckets[digit].append(number)

        lst = [num for bucket in buckets for num in bucket]
        buckets = [[] for _ in range(10)]

    return lst

print(sort(complete_list))