import numpy as np
import math


def gen_number_sumOfDivisors_array(length):
    # construct the array from index 1, and the terminal is index (length - 1)
    d = np.ones(length, dtype=int)
    d[1] = 0

    for i in range(2, math.trunc(math.sqrt(length - 1)) + 1):
        for j in range(i, (length - 1) // i + 1):
            if i == j:
                d[i * j] += i
            else:
                d[i * j] += i + j

    return d


def gen_abundant_list(array):
    abundant_list = []

    for i in range(1, array.shape[0]):
        if array[i] > i:
            abundant_list.append(i)

    return abundant_list


def cal_sum_of_non_abundant_num(abundant_list, upper_bound):
    non_abundant_num_array = np.arange(upper_bound, dtype=int)

    for i in range(len(abundant_list)):
        for j in range(i, len(abundant_list)):
            if abundant_list[i] + abundant_list[j] < upper_bound:
                non_abundant_num_array[abundant_list[i] + abundant_list[j]] = 0

    return sum(non_abundant_num_array)


if __name__ == '__main__':
    arr = gen_number_sumOfDivisors_array(30000)
    ab_list = gen_abundant_list(arr)
    ans = cal_sum_of_non_abundant_num(ab_list, 30000)
    print(ans)