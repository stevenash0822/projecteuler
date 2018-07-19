def cal_num_of_distinct_terms(lower_bound_a, upper_bound_a, lower_bound_b, upper_bound_b):
    result_set = set()

    for a in range(lower_bound_a, upper_bound_a + 1):
        for b in range(lower_bound_b, upper_bound_b + 1):
            result_set.add(a ** b)

    return len(result_set)


if __name__ == '__main__':
    ans = cal_num_of_distinct_terms(2, 100, 2, 100)
    print(ans)
