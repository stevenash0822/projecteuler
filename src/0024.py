import math


# sorted_digit_list contains all digits of an ascending order; pos = (real lexicographic position) - 1
def gen_permutation_of_certain_position(sorted_digit_list, pos):
    if len(sorted_digit_list) == 1:
        return str(sorted_digit_list[0])
    else:
        num_of_possible_sub_permutation = math.factorial(len(sorted_digit_list) - 1)
        current_index = pos // num_of_possible_sub_permutation
        pos %= num_of_possible_sub_permutation

        current_digit = sorted_digit_list.pop(current_index)
        return str(current_digit) + gen_permutation_of_certain_position(sorted_digit_list, pos)


if __name__ == '__main__':
    digit_list = [i for i in range(10)]
    ans = gen_permutation_of_certain_position(digit_list, 999999)
    print(ans)
