import math
from itertools import permutations
from functools import reduce


def judge_prime(number):
    if number <= 1:
        return False

    for i in range(2, math.trunc(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def gen_largest_pandigital_prime():
    for sublist in list(permutations(range(1,8), 7))[::-1]:
        number = reduce(lambda x, y: x * 10 + y, sublist)
        if judge_prime(number):
            return number


if __name__ == '__main__':
    ans = gen_largest_pandigital_prime()
    print(ans)
