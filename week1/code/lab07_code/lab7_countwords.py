def similarity(dict1: dict, dict2: dict, verbose=False):
    len1 = len(dict1)
    len2 = len(dict2)
    N = 0

    for key in dict1:
        if key in dict2:
            N += 1
    
    sim = float(N / (len1 + len2 - N))

    if verbose:
        print(f"The similarity between these two = {sim}.")

    return sim


def read_stopwords():
    words_lst = []
    with open("stopwords.txt", "r") as f:
        for each in f:
            words_lst.append(each.strip())

    return words_lst

def countWords(filename: str, use_stopwords=True) -> dict:

    word_count = {}

    if use_stopwords:
        stops = read_stopwords()
    else:
        stops = []

    with open(filename, "r") as f:
        for each in f:
            word_list = each.split()
            for word in word_list:

                if word in stops:
                    continue

                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word]= 1
    
    return word_count


def print_top20(word_dict: dict):
    word_dict = sorted(word_dict.items(), key=lambda k:k[1], reverse=True)
    word_dict_orderd = iter(word_dict)
    for i in range(20):
        print(next(word_dict_orderd))




if __name__ == "__main__":
    # word_count = countWords()
    pass
