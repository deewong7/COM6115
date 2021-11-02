from pylab import plot, show, xlabel, ylabel, title, savefig, figure
from typing import List

def sum_list(numbers) -> int:
    res = 0
    for each in numbers:
        res += each
    return res


def sum_triangular(n) -> int:
    res = 0
    while(n > 0):
        res += n
        n -= 1
    return res


def square_list(numbers) -> List[int]:
    res = []
    for each in numbers:
        res.append(pow(each, 2))
    
    return res


def triangular_list(numbers) -> List[int]:
    res = []
    for each in numbers:
        res.append(sum_triangular(each))

    return res


if __name__ == "__main__":

    SAMPLE = [1, 2, 3, 4, 5]

    # 2.1
    print(sum_list(SAMPLE))
    print(sum_triangular(4))

    # 2.2
    print(square_list(SAMPLE))
    # check original list
    print(SAMPLE)
    # copy a list:
    copied_sample = list(SAMPLE)

    print(triangular_list(SAMPLE))

    # 3
    plot(SAMPLE, triangular_list(SAMPLE), "r-o")
    xlabel("This is x")
    ylabel("This is y")
    title("This is title")
    # savefig("saved_figure")
    show()

