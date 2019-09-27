from parser import parseFile
from ncls import NCLS
import sys
import subprocess
import csv
import random
import numpy as np
reads_to_be_analized = 10000
reads_per_random_index = 5

def main(cvs_file, gtf_file):

    print("############# STARTING #############", file=sys.stderr)

    frequency_tree = handle_gtf(gtf_file)
    data = handle_csv(cvs_file)
    run_bowtie(data)

    print("############# FINSHING #############", file=sys.stderr)

    with open("data_output.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)


def handle_csv(file):

    print("############# STARTING HANDLEING CSV #############", file=sys.stderr)

    datafile = open(file, 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append(row)

    print("############# FINSHING HANDLEING CSV #############", file=sys.stderr)

    return data

def handle_gtf(file):
    starts = np.array()
    ends = np.array()
    gtf = open(file, 'r')
    for line in gtf:
        line = line.split(' ')
        starts.append([int(line[3])])
        ends.append([int(line[4])])
    ids = starts
    ncls = NCLS(starts, ends, ids)

def run_bowtie(contents):

    print("############# BEGINING SEQUENCING #############", file=sys.stderr)

    for i in range(len(contents)):

        print("############# BEGINING SEQUENCING " + str(i + 1) + " OF " + str(len(contents)) + " #############", file=sys.stderr)

        number_of_spots = get_spots(contents[i][0])
        for j in range(reads_to_be_analized//reads_per_random_index):
            subprocess.call(["bowtie2", "-x", "human","--skip", str(random.randint(0, number_of_spots)),"--mm", "--upto", str(reads_per_random_index), "--no-hd", "--sra-acc", contents[i][0], ">>", "temp.sam"])

        print("############# FINISHED SEQUENCING " + str(i + 1) + " OF " + str(len(contents)) + " #############", file=sys.stderr)

        data = parseFile("temp.sam")
        subprocess.call("rm temp.sam")
        for value in data:
            contents[i].append(value)
            
    print("############# FINISHED SEQUENCING #############", file=sys.stderr)

def get_spots(sra_label):
    print(sra_label)
    query_result = subprocess.check_output("esearch -db sra -query " +  sra_label  +  " | efetch -format runinfo", shell=True)
    return int((query_result.decode().split('\n')[1]).split(',')[3])

main(sys.argv[1], sys.argv[2])
