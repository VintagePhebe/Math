# objective transfoer a float to  a ratio ex. 1.5 = 3/2
from math import gcd
user_input = float(input('inserire il prprio numero:\t'))


def float_to_ratio(user_input):
    new_integer = 0
    def get_digits(flt):
        digits = []
        try:
            flt_str = str(flt)
        except:
            print('Error')
            return digits

        for char in flt_str:
            digits.append(char)
        return digits

    def find_decimal_point_position(digits):
        point_position = 0
        point_found = False
        for char in digits:
            if char == '.':
                point_found = True
            elif point_found:
                point_position += 1
        return point_position

    def calculate_divisor(point_position):
        divisor = 10 ** point_position
        return divisor

    def extract_integer_part(digits):
        integer_part = ''
        for char in digits:
            if char != '.':
                integer_part += char
        return integer_part

    def find_gcd(new_integer, divisor):
        greatest_common_divisor = gcd(new_integer, divisor)
        return greatest_common_divisor

    def calculate_ratio(integer_part, divisor, gcd_value):
        new_integer = int(integer_part) // gcd_value
        new_divisor = divisor // gcd_value
        return f'{new_integer}/{new_divisor}'

    digits = get_digits(user_input)
    decimal_point_position = find_decimal_point_position(digits)
    divisor = calculate_divisor(decimal_point_position)
    integer_part = extract_integer_part(digits)
    try:
        new_integer = int(integer_part)
    except:
        pass

    gcd_value = find_gcd(new_integer, divisor)
    ratio = calculate_ratio(integer_part, divisor, gcd_value)

    return gcd_value, ratio

gcd_value, ratio = float_to_ratio(user_input)

print(f'the GCD is :\t{gcd_value}')
print(f'The ratio of your float is: {ratio}')
