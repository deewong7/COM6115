def MyCubeRoot(A):

    initial_x = 2
    E = 1e-3

    def f(x):
        return (pow(x, 3) - A)

    def fdx(x):
        return (3 * pow(x, 2))

    def find_next(x):
        return (x - (f(x) / fdx(x)))

    i = 0

    x = find_next(initial_x)
    while(f(x) - 0 > E):
        print(x)
        x = find_next(x)
        i += 1
    
    return x

base = 8
A = pow(base, 3)
print(MyCubeRoot(A))
