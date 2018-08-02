import time
import math


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Total running time of Function %s(): %.4f seconds" % (func.__name__, end - start))
        return result

    return wrapper


def judge_prime(number):
    if number <= 1:
        return False

    for i in range(2, math.trunc(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def judge_truncatable(number):
    reverse_string = str(number)[::-1]
    temp = 0

    for i in range(len(reverse_string) - 1):
        temp += int(reverse_string[i]) * pow(10, i)
        if not judge_prime(temp):
            return False

    return True


@timeit
def cal_sum_of_truncatable_primes():
    top_digit = [2, 3, 5, 7]
    append_digit = [1, 3, 7, 9]
    possible_sequence = top_digit

    count_truncatable_primes = 0
    result = 0
    while (count_truncatable_primes < 11):
        last_possible_sequence = possible_sequence
        possible_sequence = []

        for i in range(len(last_possible_sequence)):
            for j in range(len(append_digit)):
                current_number = last_possible_sequence[i] * 10 + append_digit[j]
                if judge_prime(current_number):
                    possible_sequence.append(current_number)
                    if judge_truncatable(current_number):
                        result += current_number
                        count_truncatable_primes += 1

    return result


if __name__ == '__main__':
    ans = cal_sum_of_truncatable_primes()
    print(ans)
