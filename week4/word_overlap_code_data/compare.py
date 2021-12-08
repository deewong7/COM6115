"""
Answer for task 8:
duplication: news02.txt and news08.txt
plagirism:  news07.txt copied from news04.txt and news06.txt
related topics: news 1 5 9
"""


"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) file1...fileN
OPTIONS:
    -h : print this help message
    -s FILE : use stoplist file FILE
    -p : use Porter stemming (default: no stemming)
    -b : use BINARY weights (default: count weighting)
------------------------------------------------------------\
"""

import sys, re, getopt
import glob
from nltk.stem import PorterStemmer

opts, args = getopt.getopt(sys.argv[1:], 'hs:pbI:')
opts = dict(opts)

##############################
# HELP option

if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print(help, file=sys.stderr)
    sys.exit()

##############################
# Identify input files, when "-I" option used

if '-I' in opts:
    filenames = glob.glob(opts['-I'])
else:
    filenames = args

# Check if filenames are being found 
# (comment out after checking)
print('INPUT-FILES:', filenames, file=sys.stderr)

##############################
# STOPLIST option

stops = set()
if '-s' in opts:
    with open(opts['-s'], 'r') as stop_fs:
        # Since every line is a individual word, so split() is not needed here
        for line in stop_fs :
            stops.add(line.strip())
            
##############################
# Stemming function

stemmer = PorterStemmer().stem

def stem_word(word):
    return stemmer(word)

##############################
# COUNT-WORDS function. 
# Takes 2 inputs: 1= FILE-NAME, 2= stoplist
# Returns a dictionary of word counts

def count_words(filename, stops):
    counts = {}
    with open(filename, "r") as f:
        for line in f:
            words_lst = line.split()
            for word in words_lst:
                word = word.strip()
                word = word.lower()
                # To check the stopwords set
                # If there is not a `-f` specified, then the set should be empty 
                if word not in stops:

                    if "-p" in opts:
                        word = stem_word(word)

                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1


    return counts

##############################
# Compute counts for individual documents

docs = [ ]

for infile in filenames:
    docs.append(count_words(infile, stops))

##############################
# Compute similarity score for document pair
# Inputs are dictionaries of counts for each doc
# Returns similarity score

def jaccard(doc1: dict, doc2: dict):
    sim = 0.0

    if "-b" in opts:
        # To perform binary count-insensitive metric
        words1 = set(doc1.keys())
        words2 = set(doc2.keys())

        sim = float(len(words1 & words2) / len(words1 | words2))
    
    else:
        # To perform count-sensitive
        w_min = 0
        w_max = 0

        for key in doc1:
            if key in doc2:
                # now that the word in both documents
                w_a = doc1[key]
                w_b = doc2[key]
                w_min += min(w_a, w_b)
                w_max += max(w_a, w_b)

        # To avoid divide by 0 
        if w_max == 0:
            return 0

        sim = float(w_min / w_max)

    return sim

##############################
# Compute scores for all document pairs

results = {}
for i in range(len(docs)-1):
    for j in range(i+1, len(docs)):        
        # pair_name = '%s <> %s' % (filenames[i], filenames[j])
        pair_name = f"{filenames[i]} <> {filenames[j]}"
        results[pair_name] = jaccard(docs[i], docs[j])
        continue

        print()
        print(set(docs[i]) & set(docs[j]))
        print()
        print(set(docs[i]) | set(docs[j]))
        print()
        inter = {'friday,', 'european', 'put'}
        for each in inter:
            print(f"{each} at doc[{i}]:", docs[i][each])
            print(f"{each} at doc[{j}]:", docs[j][each])
        exit()

##############################
# Sort, and print top N results

top_N = 20

# results = sorted(results.items(), key=lambda k:k[1], reverse=True)[0:top_N]
results = sorted(results.items(), key=lambda k:k[1], reverse=True)

# pairs = list(results) # DUMMY CODE LINE 
pairs = results # DUMMY CODE LINE 
# Replace with code to sort results based on scores.
# Have only results for highest "top_N" scores printed.

# Printing
c = 0
for pair in pairs:
    c += 1
    # print('[%d] %s = %.3f' % (c, pair, results[pair]), file=sys.stdout)
    print('[%2d] %s = %.3f' % (c, pair[0], pair[1]), file=sys.stdout)

##############################

