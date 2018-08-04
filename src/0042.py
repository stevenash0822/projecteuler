import math
from functools import reduce


def read_sequence_from_file(filename):
    sequence = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            for name in line:
                name = name.strip('\"')
                sequence.append(name)

    return sequence


def judge_triangle_number(number):
    n = math.trunc(math.sqrt(number * 2))

    if n * (n + 1) == number * 2:
        return True
    else:
        return False


def count_triangle_words(sequence):
    alphabet_value_dict = {chr(ord('A') + i): i + 1 for i in range(26)}
    result = 0

    for word in sequence:
        total_value = 0
        for ch in word:
            total_value += alphabet_value_dict[ch]
        if judge_triangle_number(total_value):
            result += 1

    return result


if __name__ == '__main__':
    seq = read_sequence_from_file("../data/0042.txt")
    ans = count_triangle_words(seq)
    print(ans)
