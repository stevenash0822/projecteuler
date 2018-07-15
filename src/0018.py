def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            line = [int(item) for item in line]
            if line:
                matrix.append(line)

    return matrix


def cal_maximum_total_of_all_routes(matrix):
    for i in range(1, len(matrix)):
        for j in range(i + 1):
            if j == 0:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j]
            elif j == i:
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - 1]) + matrix[i][j]

    maximum_total = 0
    for j in range(len(matrix)):
        maximum_total = max(matrix[len(matrix) - 1][j], maximum_total)

    return maximum_total


if __name__ == '__main__':
    mat = read_matrix_from_file("../data/0018.txt")
    ans = cal_maximum_total_of_all_routes(mat)
    print(ans)
