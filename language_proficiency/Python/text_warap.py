# Check Tutorial tab to know how to to solve.

# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to
# Returns

# string: a single string with newline characters ('\n') where the breaks should be
# Input Format

# The first line contains a string, string.
# The second line contains the width, max_width.

# Constraints

# 0 < len(string) < 1000
# 0 < len (max_width) < len(string)


# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import math
def wrap(string, max_width):
    alfa = []
    rows = []
    new_string = ''
    init = 0
    end = max_width
    alfa = [letter for letter in string]
    size = math.ceil(len(alfa)/max_width)
    for i in range(size):
        rows.append(alfa[init:end])
        rows.append('\n')
        init+=max_width
        end+=max_width
    for i in rows:
        for j in i:
            new_string+=''.join(j)
    return new_string