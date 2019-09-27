#method to take in a string of sam data and output read length, read frequency, and lopsidedness
from collections import defaultdict
import numpy as np
import sys
import re

def parseFile(file, frequency_tree):
    print("############# OPENING SAM FILE", file=sys.stderr)
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text
        contents = myfile.read()
    return parseString(contents, frequency_tree)


def parseString(txt, frequency_tree):
    spliter = re.compile('\n+')
    readnumber = re.compile('[r]+\d+')
    line_spliter = re.compile('\t+')
    colon_spliter = re.compile(':')
    forward_reads = 0
    reverse_reads = 0
    unmatched_reads = 0
    read_positions = defaultdict(list)
    position_differences = []
    read_lengths_count = 0
    read_lengths_total = 0
    read_frequency = 0
    read_lengths_average = 0
    # tlen = []
    # read_quality_unpaired = [[]]
    # read_quality_first = [[]]
    # read_quality_second = [[]]
    # match_scores = []
    # mapq_scores = []

    lines = spliter.split(txt)
    #Itterating though everyline
    for i in range(len(lines) - 1):
        subline = line_spliter.split(lines[i])
        if (int(subline[1]) & 4 == 4):
            unmatched_reads += 1
        elif (int(subline[1]) & 16 == 16):
            reverse_reads += 1
        else:
            forward_reads += 1
        read = subline[9]
        read_lengths_count += 1
        read_lengths_total += len(read)
        chromosome = getChromosome(subline[2])
        if chromosome != -1:
            read_positions[chromosome].append(int(subline[3]))
    if read_lengths_count != 0:
        read_lengths_average = read_lengths_total / read_lengths_count
    if (forward_reads + reverse_reads + unmatched_reads) != 0:
        read_frequency = (forward_reads + reverse_reads) / (forward_reads + reverse_reads + unmatched_reads)
    # read_positions.sort()
    # for i in range(len(read_positions) - 1):
    #     position_differences.append(read_positions[i + 1] - read_positions[i])
    # std_dev_of_position_difference = np.std(position_differences)

    gene_annotation_match = 0
    gene_annotation_total = 0
    gene_annotation_percent = 0
    for key in read_positions.keys():
        for position in read_positions[key]:
            #TODO there is for sure a better way to do this than with a break
            for j in frequency_tree[key].find_overlap(position, position):
                gene_annotation_match += 1
                break
            gene_annotation_total += 1
    if gene_annotation_total != 0:
        gene_annotation_percent = gene_annotation_match / gene_annotation_total
    print("gene_annotation_percent = " + str(gene_annotation_percent))
    #return [read_frequency, read_lengths_average, std_dev_of_position_difference, gene_annotation_percent]
    return [read_frequency, read_lengths_average, gene_annotation_percent]

def getChromosome(str):
    if str == "*" or str[3:] == 'X':
        return -1
    try:
        return int(str[3:])
    except:
        return -1
