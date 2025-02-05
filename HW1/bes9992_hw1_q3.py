def sum_squares(n):
    sum_of_squares = 0
    for i in range(1, n):
        sum_of_squares += (i**i)

    sum_of_all_squares = sum([i**i for i in range(1, n)])

    return sum_of_squares


def sum_odd_squares(n):
    odd_sum = 0
    for i in range(1, n, 2):
        print(i)
        odd_sum += (i**i)

    sum_of_odd_squares = sum([i**i for i in range(1, n, 2)])

    return odd_sum



