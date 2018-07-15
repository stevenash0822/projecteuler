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


def cal_sum_of_name_scores(sequence):
    score = 0

    sequence.sort()
    for index, name in enumerate(sequence, 1):
        alphabetical_value = 0
        for ch in name:
            alphabetical_value += ord(ch) - ord('A') + 1
        score += alphabetical_value * index

    return score


if __name__ == '__main__':
    seq = read_sequence_from_file("../data/0022.txt")
    ans = cal_sum_of_name_scores(seq)
    print(ans)
