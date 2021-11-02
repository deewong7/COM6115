from pylab import plot, show, figure
from typing import List, Tuple


def fetch_data(filename) -> Tuple[List[float], List[float]]:
    Xs = []
    Ys = []

    with open(filename) as f:
        for each in f:
            (x, y) = each.split(' ')
            Xs.append(float(x))
            Ys.append(float(y))

    return (Xs, Ys)


def draw(X, Y):
    plot(Xs, Ys)
    show()


def get_moving_average(values, W = 20) -> List[float]:

    res = []
    for i in range(len(values)):
        left = int(i - W / 2)
        right = int(i + W / 2)

        if left < 0:
            left = 0
        if right > len(values):
            right = len(values)

        items = values[left:right]
        mv = sum(items) / W
        res.append(mv)

        # print("Calculating: ", "[" + str(left) + ":" + str(right) + "]", "=", mv)

    return res


def try_slice():
    numbers = [1, 2, 3, 4]
    print(numbers[-1:2])
    print(numbers[4:5])


def substract(mains, mv):
    for i in range(len(mv)):
        mains[i] -= mv[i]

    return mains


if __name__ == "__main__":
    pure_file = "pure_signal.txt"
    noisy_file = "noisy_signal.txt"
    mains_noise = "mains_noise.txt"
    random_noise = "random_noise.txt"

    # (X_noises, Y_noises) = fetch_data(noisy_file)
    # the original data
    (Xs, Ys) = fetch_data(noisy_file)

    # the blue one is the original one
    # plot(Xs, Ys, "b")
    plot(Xs, Ys)

    figure()
    # the red one is the fixed one
    mavrg = get_moving_average(Ys, 40)
    plot(Xs, mavrg, "r")

    # the green one is the correct one
    _, pures = fetch_data(pure_file)
    plot(Xs, pures, "g")

    show()
