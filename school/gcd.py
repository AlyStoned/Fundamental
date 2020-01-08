""" Greatest common divisor """
from math import gcd


def gcd_1(a, b):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b
    return a


def gcd_2(m, n):
    return gcd(abs(m - n), min(m, n)) if (m - n) else n


if __name__ == '__main__':
    print('gcd python', '-' * 50)
    print(gcd(1, 5))
    print(gcd(1000, 3))
    print(gcd(4, 6))
    print(gcd(0, 2))
    print(gcd(0, 0))

    print('gcd_1', '-' * 50)
    print(gcd_1(1, 5))
    print(gcd_1(1000, 3))
    print(gcd_1(4, 6))
    print(gcd_1(0, 2))
    print(gcd_1(0, 0))

    print('gcd_2', '-' * 50)
    print(gcd_2(1, 5))
    print(gcd_2(1000, 3))
    print(gcd_2(4, 6))
    print(gcd_2(0, 2))
    print(gcd_2(0, 0))
