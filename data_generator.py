from parser import parseFile
import sys
import subprocess
import csv

readsToBeAnalized = 10000

def main(file):
    print("############# STARTING #############", file=sys.stderr)
    data = handle_csv(file)
    run_bowtie(data)
    print("############# FINSHING #############", file=sys.stderr)
    print(data)
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

def run_bowtie(contents):
    print("############# BEGINING SEQUENCING #############", file=sys.stderr)
    for i in range(len(contents)):
        print("############# BEGINING SEQUENCING " + str(i + 1) + " OF " + str(len(contents)) + " #############", file=sys.stderr)
        subprocess.call(["bowtie2", "-x", "human","--upto", str(readsToBeAnalized), "--no-hd", "--sra-acc", contents[i][0], ">", "temp.sam"])
        print("############# FINISHED SEQUENCING " + str(i + 1) + " OF " + str(len(contents)) + " #############", file=sys.stderr)
        data = parseFile("temp.sam")
        for value in data:
            contents[i].append(value)
    print("############# FINISHED SEQUENCING #############", file=sys.stderr)

main(sys.argv[1])
