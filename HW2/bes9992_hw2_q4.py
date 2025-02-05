def e_approx(n):
    e = 1
    divisor = 1
    for i in range(1, n+1):
        divisor *= i
        e += (1/divisor)

    return e




