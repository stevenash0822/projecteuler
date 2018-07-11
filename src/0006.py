def calculate_difference(upper_bound):
    ans1, ans2 = 0, 0
    for i in range(1, upper_bound + 1):
        ans1 += i
        ans2 += i * i
    ans1 = ans1 * ans1

    return ans1 - ans2

if __name__ == '__main__':
    ans = calculate_difference(100)
    print(ans)
