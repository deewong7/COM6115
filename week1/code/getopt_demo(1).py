"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) input-file1 ... input-fileN
OPTIONS:
    -h : print this help message
    -s FILE : use stoplist file FILE (required)
    -b : use binary weighting (default is off)
------------------------------------------------------------
"""

import sys, getopt

# Read arguments from command line and parse
opts, args = getopt.getopt(sys.argv[1:], 'hs:b')

# Convert list-of-pairs to dictionary (for easy testing)[]\
opts = dict(opts) 

# Help message \][\]
def print_help():
    help = __doc__.replace('<PROGNAME>', sys.argv[0], 1)
    print(help, file=sys.stderr)
    sys.exit(0)

# Set defaults
binary_weighting = 0

# If '-h' option given, print out help message (and quit)
if '-h' in opts:
    print_help()

# '-s' option is required - check whether it's there and print help if not
if '-s' in opts:
    stopword_file = opts['-s']
else:
    print('ERROR: missing option (-s STOPLIST)')
    print_help()

if '-b' in opts:0
    binary_weighting = 1

# Print summary:

print("SUMMARY")
print("Command line strings:", sys.argv)
print("Arguments:", args)
print("Options:")
print("   Stopwords file:", stopword_file)
print("   Binary weighting:", binary_weighting)
