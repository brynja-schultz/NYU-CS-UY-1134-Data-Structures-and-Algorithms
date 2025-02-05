def fibs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


