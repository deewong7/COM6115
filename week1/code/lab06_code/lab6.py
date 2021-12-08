import itertools
import numpy as np
import pylab as plb


def section1():
    # it is a numpy.ndarray returned
    img = plb.imread('chick.png')
    # print(type(img))
    # print(img.shape)
    # print()

    def revert_img(img: np.ndarray):
        rows, cols, cha = img.shape

        for i, j, k in itertools.product(range(rows), range(cols), range(cha)):
            img[i][j][k] = 1 - img[i][j][k]

    def revert_img2(img: np.ndarray):
        rows, cols, cha = img.shape

        for i, j in itertools.product(range(rows), range(cols)):
            if sum(img[i, j]) < 1.5:
                img[i, j] = (0, 0, 0)

    # revert_img(img)
    revert_img2(img)

    plb.imshow(img)
    plb.show()


def section2():
    img = plb.imread("che.png")
    print(img.shape)
    rows, cols, dim = img.shape

    # set to black and white
    def task1():
        for i, j, k in itertools.product(range(rows), range(cols), range(dim)):
            if img[i][j][k] < 0.5:
                img[i][j][k] = 0.0
            else:
                img[i][j][k] = 1.0

    def task2():
        red = (1.0, 0.0, 0.0)
        for i, j in itertools.product(range(rows), range(cols)):
            if img[i, j].sum() > 2.99:
                img[i, j] = red

    def task3():

        for i in range(rows):
            for j in range(cols):
                if img[i, j, 0] < 0.5:
                    img[i, j] = (.0, .0, .0) # black
                elif 55 < i < 160 and 55 < j < 140:
                    img[i, j] = (1., 1., 1.) # white
                else:
                    img[i, j] = (1., .0, .0) # red

    def task4():
        for i, j in itertools.product(range(rows), range(cols)):
            if img[i, j].sum() > 0.66:
                img[i, j] = (1.0, 0.0, 0.0)
            elif img[i, j].sum() < 0.33:
                img[i, j] = (0.0, 0.0, 1.0)
            else:
                img[i, j] = (0.0, 1.0, 0.0)

    def task5():
        chick = plb.imread("chick.png")
        print(chick.shape)

        chick_row, chick_col, _ = chick.shape
        row_proportion = float(rows / chick_row)
        col_proportion = float(cols / chick_col)

        for i, j in itertools.product(range(chick.shape[0]), range(chick.shape[1])):
            idx = int(i * row_proportion)
            jdx = int(j * col_proportion)

            # img[idx, jdx] += chick[i, j]
            img[idx, jdx] = chick[i, j]


    plb.imshow(img)
    plb.show()

    # task1()
    # task2()
    # task3()
    # task4()
    task5()

    plb.imshow(img)
    plb.show()


if __name__ == "__main__":
    section2()
