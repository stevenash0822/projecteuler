import numpy as np


def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            if line:
                matrix.append(line)

    matrix = np.array(matrix, dtype=int)
    return matrix


def gen_greatest_product_of_four_adjacent_numbers(matrix):
    maximum_product = 0
    height, width = matrix.shape

    for i in range(height):
        for j in range(width):
            if j + 3 < width:
                product = matrix[i, j] * matrix[i, j + 1] * matrix[i, j + 2] * matrix[i, j + 3]
                maximum_product = max(product, maximum_product)
            if (i + 3 < height) and (j + 3 < width):
                product = matrix[i, j] * matrix[i + 1, j + 1] * matrix[i + 2, j + 2] * matrix[i + 3, j + 3]
                maximum_product = max(product, maximum_product)
            if i + 3 < height:
                product = matrix[i, j] * matrix[i + 1, j] * matrix[i + 2, j] * matrix[i + 3, j]
                maximum_product = max(product, maximum_product)
            if (i + 3 < height) and (j - 3 >= 0):
                product = matrix[i, j] * matrix[i + 1, j - 1] * matrix[i + 2, j - 2] * matrix[i + 3, j - 3]
                maximum_product = max(product, maximum_product)

    return maximum_product


if __name__ == '__main__':
    mat = read_matrix_from_file("../data/0011.txt")
    ans = gen_greatest_product_of_four_adjacent_numbers(mat)
    print(ans)
