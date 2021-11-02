from pylab import plot, show

def f(x):
    return (pow(x, 2) + 20)


def g(x):
    return (pow(x/2.0, 3) - 100)


if __name__ == "__main__":
    
    X = []
    Y = []
    Y2 = []
    N = 20
    for i in range(-N, N):
        X.append(i)
        Y.append(f(i))
        Y2.append(g(i))

    # It is not necessary to specify the third parameter, it is still optional.
    # plot(X, Y, "r")
    # plot(X, Y2, "b")
    plot(X, Y)
    plot(X, Y2)
    show()
