import numpy as np


def cal_num_routes(height, width):
    num_routes_matrix = np.zeros((height + 1, width + 1), dtype=np.int64)
    num_routes_matrix[0, :] = 1
    num_routes_matrix[:, 0] = 1

    for i in range(1, num_routes_matrix.shape[0]):
        for j in range(1, num_routes_matrix.shape[1]):
            num_routes_matrix[i, j] = num_routes_matrix[i-1, j] + num_routes_matrix[i, j-1]

    return num_routes_matrix[height, width]


if __name__ == '__main__':
    ans = cal_num_routes(20, 20)
    print(ans)
