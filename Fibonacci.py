import math

x = int(input("scegliere quanti numeri si desidera\t"))
def primeFactors(n):
    buffer = ''

    while n % 2 == 0:
        buffer += '2 x '
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            buffer += f'{int(i)} x '
            n = n / i

    if n > 2:
        buffer += f'{int(n)} x '

    print(f'\033[93m{buffer[:-3]}')

fibonacci = x//2


def PrintFibonacci(fibonacci ):
    y = 0
    z = 1
    for i in range(fibonacci):
        y += z
        print(f"\033[94m{y}", end=' = ')
        primeFactors(y)

        z += y
        print(f"\033[94m{z}", end=' = ')
        primeFactors(z)

PrintFibonacci(fibonacci)
