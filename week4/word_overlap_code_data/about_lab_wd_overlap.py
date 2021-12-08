def about_stem_word():
    from nltk.stem import PorterStemmer

    stem = PorterStemmer().stem
    # print(type(stem))
    a = "happiest"
    a = "apptity"

    print(stem(a))


def about_set_operations():
    A = [0, 1, 2, 3, 4, 5]
    B = [1, 2, 3, 4, 5, 6]

    A = set(A)
    B = set(B)

    print(f"A intersection B = {A & B}")
    print(f"A union B = {A | B}")


def about_min():
    A = [12, 13]
    B = 13

    print(min(A))


if __name__ == "__main__":
    # about_stem_word()

    # about_set_operations()

    about_min()