from parser import parseFile #COMMENT THIS LINE OUT IF YOU WANT TO RUN PARSER AS MAIN
from ncls import NCLS
from collections import defaultdict
import sys
import subprocess
import csv
import random
import numpy as np

def handle_csv(file):
    datafile = open(file, 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append(row)
    return data

def generate_empty_list():
    list = []
    list.append([])
    list.append([])
    return list

def handle_gtf(file):
    frequency_trees = defaultdict(generate_empty_list)
    gtf = open(file, 'r')
    for line in gtf:
        line = line.split('\t')
        try:
            chr = int(line[0])
            try:
                if (line[2] != 'transcript'):
                    frequency_trees[chr][0].append(int(line[3]))
                    frequency_trees[chr][1].append(int(line[4]))
            except:
                print("Lol we have a real problem")
        except:
            print("Chromosome was non-integer")
    for key in frequency_trees.keys():
        frequency_trees[key] = NCLS(np.array(frequency_trees[key][0]), np.array(frequency_trees[key][1]), np.array(frequency_trees[key][0]))
    return frequency_trees

def run_bowtie(contents, frequency_tree):
    reads_to_be_analized = 10000
    reads_per_random_index = 10000
    outputs = []
    for i in range(len(contents)):
        print("############# BEGINING SEQUENCING " + str(i + 1) + " OF " + str(len(contents)) + " #############", file = sys.stderr)

        number_of_spots = 1000#get_spots(contents[i][0])
        for j in range(reads_to_be_analized//reads_per_random_index):
            subprocess.call(["../bt2/bowtie2/bowtie2", "-x", "human","--skip", str(random.randint(0, number_of_spots)),"--mm", "--upto", str(reads_per_random_index), "--no-hd", "--sra-acc", contents[i][1], ">>", "temp.sam"])

        print("############# FINISHED SEQUENCING " + str(i + 1) + " OF " + str(len(contents)) + " #############", file = sys.stderr)
        data = parseFile("temp.sam", frequency_tree)
        outputs.append(data)
        subprocess.call("rm temp.sam", shell=True)
        for value in data:
            contents[i].append(value)
    return outputs

def get_spots(sra_label):
    print(sra_label)
    query_result = subprocess.check_output("esearch -db sra -query " +  sra_label  +  " | efetch -format runinfo", shell=True)
    return int((query_result.decode().split('\n')[1]).split(',')[3])
