def count_letters_from_1_to_1000():
    givenNumber_letters_dict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
                                11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
                                20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8, 0: 0}
    conjunction_letters_dict = {'and': 3}

    count = 0
    for num in range(1, 1001):
        if num == 1000:
            count += givenNumber_letters_dict[1] + givenNumber_letters_dict[1000]
        else:
            if num >= 100:
                count += givenNumber_letters_dict[num // 100] + givenNumber_letters_dict[100]
                if num % 100 == 0:
                    pass
                else:
                    count += conjunction_letters_dict['and']
                    if num % 100 < 20:
                        count += givenNumber_letters_dict[num % 100]
                    else:
                        count += givenNumber_letters_dict[(num % 100) - (num % 10)] + givenNumber_letters_dict[num % 10]
            else:
                if num < 20:
                    count += givenNumber_letters_dict[num]
                else:
                    count += givenNumber_letters_dict[num - (num % 10)] + givenNumber_letters_dict[num % 10]

    return count


if __name__ == '__main__':
    ans = count_letters_from_1_to_1000()
    print(ans)
