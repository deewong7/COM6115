def MySqrt(A):
    # initial_value = 2
    initial_value = 1e-3
    E = 1e-3  # error tolerance

    def f(x):
        return (pow(x, 2) - A)

    def fdx(x):
        return (2 * x)

    def find_next(xi):
        return (xi - (f(xi) / fdx(xi)))

    x = find_next(initial_value)
    i = 0
    while (f(x) - 0 > E):
        # print(x)
        x = find_next(x)
        i += 1

    # print("Found it after", i, "times:", x)
    return x


print(MySqrt(4))
