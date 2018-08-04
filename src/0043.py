# from d2d3d4 is divisible by 2, d4 = 0, 2, 4, 6, 8
# from d3d4d5 is divisible by 3, (d3 + d4 + d5) % 3 = 0
# from d4d5d6 is divisible by 5, d6 = 0, 5
# from d5d6d7 is divisible by 7, (10d5 + d6 - 2d7) % 7 = 0
# from d6d7d8 is divisible by 11, (d6 + d8 - d7) % 11 = 0, i.e., d6 + d8 - d7 = 0, 11
# from d7d8d9 is divisible by 13, (10d7 + d8 + 4d9) % 13 = 0
# from d8d9d710 is divisible by 17, (10d8 + d9 - 5d10) % 17 = 0

# from above, we can infer that d5d6d7d8d9d10 = 357289 or 952867


if __name__ == '__main__':
    ans = 1406357289 + 1460357289 + 4106357289 + 4160357289 + 1430952867 + 4130952867
    print(ans)
