import sys
import csv

def main(file):
    datafile = open(file, 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    print(datareader)
    for i in datareader:
        print(i)
        data.append(i[1])

    with open("testerinoes.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv)
        csvWriter.writerows(data)

if __name__ == '__main__':
    main(sys.argv[1])
