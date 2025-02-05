def factors(num):
    sqrt_num = int(num ** (1/2))
    compliment_lst = []

    for i in range(1, sqrt_num+1):
        if num % i == 0:
            c = num // i
            if c != i:
                compliment_lst.append(c)
            yield i
    while compliment_lst:
        yield compliment_lst.pop(-1)

