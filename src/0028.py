# n: the n-th layer surrounding the center 1
# In the northeast direction, the general term is (2n + 1)^2
# In the southeast direction, the general term is (2n - 1) * 2n + 1
# In the northwest direction, the general term is (2n + 1) * 2n + 1
# In the southwest direction, the general term is (2n)^2 + 1
# So the sum of diagonals in n-th layer is 4 * [n * (4n + 1) + 1]


def cal_sum_of_diagonals(num_layers):
    result = 1

    for n in range(1, num_layers + 1):
        result += 4 * (n * (4 * n + 1) + 1)

    return result


if __name__ == '__main__':
    ans = cal_sum_of_diagonals((1001 - 1) // 2)
    print(ans)
