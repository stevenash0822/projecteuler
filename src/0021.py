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


def count_sum_of_amicable_numbers_of_array(d):
    count = 0

    for num in range(2, d.shape[0]):
        if d[num] < d.shape[0]:
            if (num == d[d[num]]) and (num != d[num]):
                count += num

    return count


if __name__ == '__main__':
    array = gen_number_sumOfDivisors_array(10000)
    ans = count_sum_of_amicable_numbers_of_array(array)
    print(ans)
