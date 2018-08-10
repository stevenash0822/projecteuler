def cal_interval(index, property_name):
    try:
        if property_name == "triangle":
            return index
        elif property_name == "pentagonal":
            return 3 * index - 2
        elif property_name == "hexagonal":
            return 4 * index - 3
        else:
            raise NameError(property_name)
    except NameError as err:
        print("errors derived from wrong function parameter: {0}".format(err))


def gen_number_satisfy_three_properties(n):
    triangle_number, pentagonal_number, hexagonal_number = 1, 1, 1
    triangle_index, pentagonal_index, hexagonal_index = 1, 1, 1

    count_find = 0
    while count_find < n:
        hexagonal_index += 1
        hexagonal_number += cal_interval(hexagonal_index, "hexagonal")

        while hexagonal_number > pentagonal_number:
            pentagonal_index += 1
            pentagonal_number += cal_interval(pentagonal_index, "pentagonal")

        while hexagonal_number > triangle_number:
            triangle_index += 1
            triangle_number += cal_interval(triangle_index, "triangle")

        if (hexagonal_number == pentagonal_number) and (hexagonal_number == triangle_number):
            count_find += 1

    return hexagonal_number


if __name__ == '__main__':
    ans = gen_number_satisfy_three_properties(2)
    print(ans)
