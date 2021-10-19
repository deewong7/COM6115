from sys import exit
import pylab


def use_pylab():
# dimensions & shape
    ndarray = pylab.zeros((3, 5))
    print(type(ndarray))
    print(list(ndarray))

    arranged_array = pylab.arange(0, 2, 0.5)

    print(len(arranged_array))
    print(arranged_array)

    for each in arranged_array:
        # print(each)
        print(type(each))

def use_lambda():
    # a = lambda x : (x * x) + 1
    # print(type(a(1)))
    # print(a(3))

    s = [3, 8, 7, 3]
    s2 = [4, 9, 8, 4]
    l = lambda a:a[1]
    print(type(l))
    print(l(s2))

def use_lambda2():
    # example with lambda: sorting list of pairs(tuple) by second value
    x = [('a', 3), ('c', 1), ('b', 5)]
    print(type(x))
    print(x)
    x.sort(key=lambda a:a[1])
    print(x)

# Sorting Dictionaries (labels) by Value
def use_lambda3():
    # use lambda function to sort labels from dictionary
    counts = {'a': 3, 'c': 1, 'b': 5}
    labels = counts.keys()
    print(type(labels))
    print(type(list(labels)))

    lables = list(labels)
    print(labels)
    lables.sort()
    print(lables)

    lables.sort(key=lambda item:counts[item], reverse=True)
    print(lables)

if __name__ == "__main__":
    # use_pylab()
    # use_lambda()
    # use_lambda2()
    use_lambda3()

    pass