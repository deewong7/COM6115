"""
USE: python <PROGNAME> (options) WORDLIST-FILE INPUT-FILE OUTPUT-FILE
OPTIONS:
    -h : print this help message and exit
"""
################################################################

import sys

################################################################

MAXWORDLEN = 5

################################################################
# Command line options handling, and help

def print_help():
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help_message = __doc__.replace('<PROGNAME>', progname, 1)
    print('-' * 60, help_message, '-' * 60, file=sys.stderr)
    sys.exit(0)
    
if '-h' in sys.argv or len(sys.argv) != 4:
    print_help()

word_list_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

################################################################

# PARTS TO COMPLETE: 

################################################################
# READ CHINESE WORD LIST
# Read words from Chinese word list file, and store in 
# a suitable data structure (e.g. a set)
chinese_dictions = set()

with open(word_list_file, "r", encoding="utf-8") as f:
    for line in f:
        chinese_dictions.add(line.strip())



################################################################
# FUNCTION TO PROCESS ONE SENTENCE
# Sentence provided as a string. Result returned as a list of strings 

DEBUG = False
def segment(sent :str, wordset):   # dummy definition provided, so can 
    # TODO: To apply greedy algorithm here
    sent = sent.strip()
    word_lst = list()

    i = 0
    while i < len(sent):
    # every outer iteration, to find a magical length 

        local_optim = []
        for j in range(i + 1, i + 1 + MAXWORDLEN):
            # print(range(i, j))

            item = sent[i:j].strip()

            remain = sent[j:len(sent)]

            if DEBUG:
                print(item, "^", remain)

            previous = ""
            if len(local_optim) != 0:
                previous = local_optim[-1]

            if (item in wordset or len(item) == 1) and item != previous:
                local_optim.append(item)
                # print(f"{item} in wordset = {item in wordset}")
                # print()
                # print(f"Returned: at {i}:", matched)
            
            # if the current right index is out of bound
            if j == len(sent):
                # if cannot find one till the last
                break
            
        if DEBUG:
            print(local_optim)
        word = local_optim.pop()
        word_lst.append(word)
        i += len(word)

    return word_lst         # write code for main loop first.



################################################################
# MAIN LOOP
# Read each line from input file, segment, and print to output file

# f_out = open(output_file, "w", encoding="utf-8")
sys.stdout = open(output_file, "w", encoding="utf-8")

with open(input_file, "r", encoding="utf-8") as f_in:
    for line in f_in:
        seg_lst = segment(line, chinese_dictions)
        print(" ".join(seg_lst))

        if DEBUG:
            break


sys.stdout.close()

################################################################

