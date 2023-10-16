# objective transfoer a float to  a ratio ex. 1.5 = 3/2
from math import gcd
input = float(input('inserire il prprio numero:\t'))

def get_ciphers(flt):
    ciphers = []
    try:
        input = str(flt)
    except:
        print('error')

    for i in input:
        ciphers.append(i)
    return ciphers
def get_pointPosition(ciphers):
    point_position = 0
    check = False
    for i in ciphers:
        if i == '.':
            check = True
        elif check == True:
            point_position += 1
    return point_position
def get_divisor(pointPosition):
    divisor = 10 ** pointPosition
    return divisor
def get_intNumber(ciphers):
    intNumber = ''
    for i in ciphers:
        if i != '.':
            intNumber += i

    return intNumber


def get_GTD(intNUmber, Divisor):
    try:
        New_intNumber = int(intNUmber)
    except:
        pass
    GCD = gcd(New_intNumber,Divisor)
    return GCD
def get_ratio(intNumber, divisor, GCD):
    new_in = intNumber // GCD
    new_div = divisor // GCD
    return f'{new_in}/{new_div}'

ciphers = get_ciphers(input)
pointerPosition = get_pointPosition(ciphers)
divisor = get_divisor(pointerPosition)
intNumber = get_intNumber(ciphers)
try:
    New_intNumber = int(intNumber)
except:
    pass
GCD = get_GTD(New_intNumber, divisor)
ratio = get_ratio(New_intNumber, divisor, GCD)

#print(f'ciphers = \t{ciphers}\npointerPosition = \t{pointerPosition}\ndivisor = \t{divisor}\nintNumber = \t{intNumber}\nGCD = \t{GCD}\nratio = \t {ratio}')

print(f'the ratio of your float is:\t{ratio}')

