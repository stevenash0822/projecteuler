import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Total running time of Function %s(): %.4f seconds" % (func.__name__, end - start))
        return result

    return wrapper


def judge_palindromic_string(string):
    last = len(string) - 1
    return all(string[i] == string[last - i] for i in range(0, last // 2 + 1))


@timeit
def cal_sum_of_all_palindromic_number_in_both_base(upper_bound):
    result = 0

    for i in range(1, upper_bound):
        if judge_palindromic_string(str(i)):
            if judge_palindromic_string(bin(i)[2:]):
                result += i

    return result


if __name__ == '__main__':
    ans = cal_sum_of_all_palindromic_number_in_both_base(1000000)
    print(ans)
