from argument_parser import get_args
from data_generator import handle_gtf, handle_csv, run_bowtie
from data_modifier import make_data_lists_for_assay_type, make_pairings_for_scatter
from plot_maker import make_each_scatterplot
import sys
import csv

def main(bowtie_index, csv_file_wgs, csv_file_srna, csv_file_mrna, gtf_file):
    print("############# STARTING", file=sys.stderr)
    print("############# STARTING CONSTURCTING FREQUENCY TREE", file=sys.stderr)
    frequency_trees = handle_gtf(gtf_file)
    print("############# ENDING CONSTURCTING FREQUENCY TREE", file=sys.stderr)

    print("############# STARTING HANDLING CSV WGS", file=sys.stderr)
    data = handle_csv(csv_file_wgs)
    print("############# FINSHING HANDLING CSV WGS", file=sys.stderr)
    print("############# BEGINING SEQUENCING WGS", file=sys.stderr)
    output_data_wgs = run_bowtie(bowtie_index, data, frequency_trees)
    data_lists_wgs = make_data_lists_for_assay_type(output_data_wgs)
    pairings_wgs = make_pairings_for_scatter(data_lists_wgs)
    print("############# FINISHED SEQUENCING WGS", file=sys.stderr)
    print("############# FINSHING WGS", file=sys.stderr)
    with open("data_output_wgs.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)

    print("############# STARTING HANDLING CSV SMALL RNA", file=sys.stderr)
    data = handle_csv(csv_file_srna)
    print("############# FINSHING HANDLING CSV SMALL RNA", file=sys.stderr)
    print("############# BEGINING SEQUENCING SMALL RNA", file=sys.stderr)
    output_data_srna = run_bowtie(bowtie_index, data, frequency_trees)
    data_lists_srna = make_data_lists_for_assay_type(output_data_srna)
    pairings_srna = make_pairings_for_scatter(data_lists_srna)
    print("############# FINISHED SEQUENCING SMALL RNA", file=sys.stderr)
    print("############# FINSHING SMALL RNA", file=sys.stderr)
    with open("data_output_srna.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)

    print("############# STARTING HANDLING CSV mRNA", file=sys.stderr)
    data = handle_csv(csv_file_mrna)
    print("############# FINSHING HANDLING CSV mRNA", file=sys.stderr)
    print("############# BEGINING SEQUENCING mRNA", file=sys.stderr)
    output_data_mrna = run_bowtie(bowtie_index, data, frequency_trees)
    data_lists_mrna = make_data_lists_for_assay_type(output_data_mrna)
    pairings_mrna = make_pairings_for_scatter(data_lists_mrna)
    print("############# FINISHED SEQUENCING mRNA", file=sys.stderr)
    print("############# FINSHING mRNA", file=sys.stderr)
    with open("data_output_mrna.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)

#     print("############# MAKING SCATTERPLOTS")
#     make_each_scatterplot(pairings_wgs, pairings_srna, pairings_mrna)
#     print("DONE")

if __name__ == '__main__':
    args = get_args()
    main(args.index, args.wgs, args.srna, args.mrna, args.gtf)
