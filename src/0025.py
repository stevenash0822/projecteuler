import numpy as np


def complicated_add(array1, array2):
    length1, length2 = array1.shape[0], array2.shape[0]

    if length1 > length2:
        array2 = np.hstack((np.zeros(length1 - length2, dtype=int), array2))
    elif length2 > length1:
        array1 = np.hstack((np.zeros(length2 - length1, dtype=int), array1))

    result = np.add(array1, array2)
    for i in range(result.shape[0] - 1, 0, -1):
        result[i - 1] += result[i] // 10
        result[i] %= 10
    if result[0] >= 10:
        top_digit = result[0] // 10
        result[0] %= 10
        result = np.concatenate(([top_digit], result))

    return result


def cal_certain_index_of_fibonacci_sequence(upper_bound_digits):
    a = np.array([1])
    b = np.array([1])

    index = 2
    while b.shape[0] < upper_bound_digits:
        a, b = b, complicated_add(a, b)
        index += 1

    return index


if __name__ == '__main__':
    ans = cal_certain_index_of_fibonacci_sequence(1000)
    print(ans)
