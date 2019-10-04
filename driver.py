from data_generator import handle_gtf, handle_csv, run_bowtie
from data_modifier import make_data_lists_for_assay_type, make_pairings_for_scatter
from plot_maker import make_each_scatterplot
import sys
import csv

def main(csv_file, gtf_file):
    print("############# STARTING", file=sys.stderr)
    print("############# STARTING CONSTURCTING FREQUENCY TREE", file=sys.stderr)
    frequency_trees = handle_gtf(gtf_file)
    print("############# ENDING CONSTURCTING FREQUENCY TREE", file=sys.stderr)
    print("############# STARTING HANDLING CSV", file=sys.stderr)
    data = handle_csv(csv_file)
    print("############# FINSHING HANDLING CSV", file=sys.stderr)
    print("############# BEGINING SEQUENCING", file=sys.stderr)
    output_data = run_bowtie(data, frequency_trees)
    data_lists = make_data_lists_for_assay_type(output_data)
    pairings = make_pairings_for_scatter(data_lists)
    make_each_scatterplot(pairings)
    print("############# FINISHED SEQUENCING", file=sys.stderr)
    print("############# FINSHING", file=sys.stderr)
    with open("data_output.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
