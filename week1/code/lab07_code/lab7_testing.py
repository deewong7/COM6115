from lab7_countwords import countWords, print_top20, similarity

# res = countWords("mobypara.txt")
# res = countWords("mobydick.txt")
# # print(res)
# print_top20(res)

res1 = countWords("george01.txt")
res2 = countWords("george03.txt")


similarity(res1, res2, verbose=True)

"""
I can see that the first and the third documents are quite similar because the similarity calculated are a relatively large number.
"""
