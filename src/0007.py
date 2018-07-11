def judge_prime(number, current_prime_list):
    for prime in current_prime_list:
        if number % prime == 0:
            return False

    current_prime_list.append(number)
    return True


def query_prime(query):
    current_prime_list = []
    current_number = 2
    while len(current_prime_list) < query:
        judge_prime(current_number, current_prime_list)
        current_number += 1

    return current_number - 1


if __name__ == '__main__':
    ans = query_prime(10001)
    print(ans)
