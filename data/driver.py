from argument_parser import get_args
from data_generator import handle_gtf, handle_csv, run_bowtie
from data_modifier import make_data_lists_for_assay_type, make_pairings_for_scatter
from plot_maker import make_each_scatterplot
import sys
import csv

def main(bowtie_index, csv_file_wgs, csv_file_srna, csv_file_mrna, gtf_file):
    frequency_trees = handle_gtf(gtf_file)
    data = handle_csv(csv_file_wgs)
    output_data_wgs = run_bowtie(bowtie_index, data, frequency_trees)
    with open("output/data_output_wgs.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerow(["Count", "SRA Accession", "Gene Annotation Percent", "Average Read Length", "Read Frequency", "STD of Position Difference", "Mean of Position Difference", "Number of Chromosoms", "Max Position Difference", "Min Position Difference", "Percent A", "Percent C", "Percent G", "Percent T"])
        csvWriter.writerows(map(lambda x: [x],output_data_wgs))
    my_csv.close()
    data = handle_csv(csv_file_srna)
    output_data_srna = run_bowtie(bowtie_index, data, frequency_trees)
    with open("output/data_output_srna.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerow(["Count", "SRA Accession", "Gene Annotation Percent", "Average Read Length", "Read Frequency", "STD of Position Difference", "Mean of Position Difference", "Number of Chromosoms", "Max Position Difference", "Min Position Difference", "Percent A", "Percent C", "Percent G", "Percent T"])
        csvWriter.writerows(map(lambda x: [x],output_data_srna))
    my_csv.close()
    data = handle_csv(csv_file_mrna)
    output_data_mrna = run_bowtie(bowtie_index, data, frequency_trees)
    with open("output/data_output_mrna.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerow(["Count", "SRA Accession", "Gene Annotation Percent", "Average Read Length", "Read Frequency", "STD of Position Difference", "Mean of Position Difference", "Number of Chromosoms", "Max Position Difference", "Min Position Difference", "Percent A", "Percent C", "Percent G", "Percent T"])
        csvWriter.writerows(map(lambda x: [x],output_data_mrna))
    my_csv.close()

if __name__ == '__main__':
    args = get_args()
    main(args.index, args.wgs, args.srna, args.mrna, args.gtf)
