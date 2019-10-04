#method to take in a string of sam data and output read length, read frequency, and lopsidedness
from collections import defaultdict
# from data_generator import handle_gtf #UNCOMMENT THIS LINE IF YOU WANT TO RUN PARSER AS MAIN
import numpy as np
import sys
import re

def main(argv):
    sam_file = argv[0]
    gtf_file = argv[1]
    frequency_tree = handle_gtf(gtf_file)
    result = parseFile(sam_file, frequency_tree)
    print(result)


def parseFile(file, frequency_tree):
    print("############# OPENING SAM FILE", file=sys.stderr)
    with open(file, 'rt') as myfile:
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
    position_differences_stdv_list = []
    total_position_diffs = []
    read_lengths_count = 0
    read_lengths_total = 0
    read_frequency = 0
    read_lengths_average = 0
    num_chromosomes = 0
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

    for _, position_list in read_positions.items():
        position_list.sort()
        num_chromosomes += 1
        for i in range(len(position_list) - 1):
            position_differences.append(position_list[i + 1] - position_list[i])
            total_position_diffs.append(position_list[i + 1] - position_list[i])
        std_dev_of_position_difference = np.std(position_differences)
        position_differences_stdv_list.append(std_dev_of_position_difference)
        position_differences.clear()

    mean_of_stdv_per_chromosome = np.nanmean(position_differences_stdv_list)
    mean_of_pos_diffs = np.nanmean(total_position_diffs)
    max_stdv = np.nanmax(position_differences_stdv_list)
    min_stdv = np.nanmin(position_differences_stdv_list)
    max_position_difference = np.amax(total_position_diffs)
    min_position_difference = np.amin(total_position_diffs)
    return [gene_annotation_percent, read_lengths_average, read_frequency, mean_of_stdv_per_chromosome, mean_of_pos_diffs, num_chromosomes, max_stdv, min_stdv, max_position_difference, min_position_difference, position_differences_stdv_list]

def getChromosome(str):
    if str == "*" or str[3:] == 'X':
        return -1
    try:
        return int(str[3:])
    except:
        return -1

if __name__ == '__main__':
  main(sys.argv[1:])
