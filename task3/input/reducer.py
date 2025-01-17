#!/usr/bin/python

import sys

word_count = 0
line_count = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    word_count_string, line_count_string = line.split("\t", 1)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    word_count += int(word_count_string)
    line_count += int(line_count_string)

print("{0}\t{1}".format(word_count, line_count))
