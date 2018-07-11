def gen_maximum_consecutive_product(digit_sequence, sub_length):
    maximum_product = 0
    start_pos = 0

    while start_pos + sub_length - 1 < len(digit_sequence):
        product = 1
        jump_flag = False

        for i in range(sub_length):
            if digit_sequence[start_pos + i] == '0':
                start_pos = start_pos + i + 1
                jump_flag = True
                break
            else:
                product *= int(digit_sequence[start_pos + i])

        if not jump_flag:
            if product > maximum_product:
                maximum_product = product

            while start_pos + sub_length < len(digit_sequence):
                if digit_sequence[start_pos + sub_length] != '0':
                    product = product // int(digit_sequence[start_pos]) * int(digit_sequence[start_pos +sub_length])
                    start_pos += 1
                    if product > maximum_product:
                        maximum_product = product
                else:
                    start_pos = start_pos + sub_length + 1
                    break

    return maximum_product


def read_sequence_from_file(filename):
    import re

    with open(filename, 'r') as f:
        digit_seq = f.read()
        digit_seq = digit_seq.strip()
        digit_seq = re.sub(r'\D', '', digit_seq)

    return digit_seq


if __name__ == '__main__':
    digit_sequence = read_sequence_from_file("../data/0008.txt")
    ans = gen_maximum_consecutive_product(digit_sequence, 13)
    print(ans)
