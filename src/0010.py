import time
import numpy as np


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Total running time of Function %s(): %.4f seconds" % (func.__name__, end - start))
        return result

    return wrapper


def judge_prime(number, current_prime_list):
    for prime in current_prime_list:
        if number % prime == 0:
            return False

    current_prime_list.append(number)
    return True


@timeit
def gen_sum_value_of_prime(upper_bound):
    current_prime_list = []
    for current_number in range(2, upper_bound):
        judge_prime(current_number, current_prime_list)

    return sum(current_prime_list)


@timeit
def gen_sum_value_of_prime_method2(upper_bound):
    current_prime_list = []
    prime_flag_array = np.ones(upper_bound, dtype=int)

    for current_number in range(2, upper_bound):
        if prime_flag_array[current_number] == 1:
            current_prime_list.append(current_number)
            overwrite_number = current_number * 2
            while overwrite_number < upper_bound:
                prime_flag_array[overwrite_number] = 0
                overwrite_number += current_number
        else:
            continue

    return sum(current_prime_list)


if __name__ == '__main__':
    ans = gen_sum_value_of_prime(2000000)
    print(ans)
    ans2 = gen_sum_value_of_prime_method2(2000000)
    print(ans2)
