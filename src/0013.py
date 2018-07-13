import numpy as np


def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                single_row = []
                for ch in line:
                    single_row.append(ch)
                matrix.append(single_row)

    matrix = np.array(matrix, dtype=int)
    return matrix


def gen_first_ten_numbers_of_sum(matrix):
    sum_by_row = np.sum(matrix, axis=0)
    complementary_zeros_array = np.zeros(int(np.log10(matrix.shape[0])) + 5, dtype=int)
    sum_by_row = np.hstack((complementary_zeros_array, sum_by_row))
    length_digits = sum_by_row.shape[0]

    for i in range(length_digits - 1, -1, -1):
        if sum_by_row[i] != 0:
            sum_by_row[i - 1] += sum_by_row[i] // 10
            sum_by_row[i] %= 10
        else:
            break

    result = ''
    for digit in sum_by_row[np.nonzero(sum_by_row)[0][0] : np.nonzero(sum_by_row)[0][0] + 10]:
        result += str(digit)

    return result


if __name__ == '__main__':
    mat = read_matrix_from_file("../data/0013.txt")
    ans = gen_first_ten_numbers_of_sum(mat)
    print(ans)
