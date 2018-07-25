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


def gen_prime_list(upper_bound):
    prime_list = []
    prime_flag_array = np.ones(upper_bound, dtype=int)

    for current_number in range(2, upper_bound):
        if prime_flag_array[current_number] == 1:
            prime_list.append(current_number)
            overwrite_number = current_number * 2
            while overwrite_number < upper_bound:
                prime_flag_array[overwrite_number] = 0
                overwrite_number += current_number
        else:
            continue

    return prime_list


def gen_all_order(number):
    all_order_set = set()
    string = str(number)

    while string not in all_order_set:
        all_order_set.add(string)
        string = string[-1] + string[:-1]

    return set(int(i) for i in all_order_set)


@timeit
def cal_num_of_circular_prime(upper_bound):
    prime_set = set(gen_prime_list(upper_bound))
    circular_prime_set = set()
    result = 0

    for number in prime_set:
        if number not in circular_prime_set:
            all_order_set = gen_all_order(number)
            circular_flag = True

            for related_number in all_order_set:
                if related_number not in prime_set:
                    circular_flag = False
                    break

            if circular_flag:
                circular_prime_set = circular_prime_set.union(all_order_set)
                result += len(all_order_set)

    return result


if __name__ == '__main__':
    ans = cal_num_of_circular_prime(1000000)
    print(ans)
