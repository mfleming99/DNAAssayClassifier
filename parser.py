#method to take in a string of sam data and output read length, read frequency, and lopsidedness
import numpy as np
import sys
import re

def parseFile(file):
    print("############# OPENING SAM FILE #############", file=sys.stderr)
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text
        contents = myfile.read()
    return parseString(contents)



def parseString(txt):
    spliter = re.compile('\n+')
    readnumber = re.compile('[r]+\d+')
    line_spliter = re.compile('\t+')
    colon_spliter = re.compile(':')
    forward_reads = 0
    reverse_reads = 0
    unmatched_reads = 0
    read_positions = []
    position_differences = []
    read_lengths_count = 0
    read_lengths_total = 0
    read_frequency = 0
    # tlen = []
    # read_quality_unpaired = [[]]
    # read_quality_first = [[]]
    # read_quality_second = [[]]
    # match_scores = []
    # mapq_scores = []

    lines = spliter.split(txt)
    #Itterating though everyline
    for i in range(len(lines) - 1):
        get_match_score = True
        subline = line_spliter.split(lines[i])
        if (int(subline[1]) & 4 == 4):
            unmatched_reads += 1
            get_match_score = False
        elif (int(subline[1]) & 16 == 16):
            reverse_reads += 1
        else:
            forward_reads += 1
        read = subline[9]
        read_lengths_count += 1
        read_lengths_total += len(read)
        read_positions.append(int(subline[3]))

    read_lengths_average = read_lengths_total / read_lengths_count
    read_positions.sort()
    read_frequency = (forward_reads + reverse_reads) / (forward_reads + reverse_reads + unmatched_reads)
    for i in range(len(read_positions) - 1):
        position_differences.append(read_positions[i + 1] - read_positions[i])
    std_dev_of_position_difference = np.std(position_differences)
    return [read_frequency, read_lengths_average, std_dev_of_position_difference]
