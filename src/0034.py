import time
import math


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Total running time of Function %s(): %.4f seconds" % (func.__name__, end - start))
        return result

    return wrapper


def cal_sum_of_factorial_of_digits(number, digit_factorial_dict):
    result = 0

    while number:
        result += digit_factorial_dict[number % 10]
        number //= 10

    return result


@timeit
def cal_sum_of_all_curious_numbers():
    digit_factorial_dict = {i: math.factorial(i) for i in range(10)}
    result = 0

    for number in range(10, 2999999):
        if number == cal_sum_of_factorial_of_digits(number, digit_factorial_dict):
            result += number

    return result


if __name__ == '__main__':
    ans = cal_sum_of_all_curious_numbers()
    print(ans)
