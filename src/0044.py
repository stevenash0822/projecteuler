def cal_minimum_difference_for_pentagonal():
    pentagonal_set = set()
    sum_difference_dictionary = {}

    n = 0
    p = 0
    while True:
        p += 3 * n + 1
        if p in sum_difference_dictionary:
            return sum_difference_dictionary[p]

        for old in pentagonal_set:
            diff = p - old
            if diff in pentagonal_set:
                sum_difference_dictionary[p + old] = diff

        pentagonal_set.add(p)
        n += 1


if __name__ == '__main__':
    ans = cal_minimum_difference_for_pentagonal()
    print(ans)
