import numpy as np

#make three different csv file, one for each assay type
#run data generatof three times on those three csv files, and keep the list of outputs from parser
#pass the three different lists of outputs from parser to data modifier
#for each list, construc the appropriate 15 pairings of data
#pass the three lists of 15 pairings into plot maker
# make the plots

def make_data_lists_for_assay_type(sra_outputs):
    gene_annotation_percent_list = []
    read_length_list = []
    frequency_list = []
    std_of_pos_diff_list = []
    mean_of_pos_diff_list = []
    num_of_chromosomes_list = []
    max_position_difference_list = []
    min_position_difference_list = []

    for output in sra_outputs:
        gene_annotation_percent_list.append(output[0])
        read_length_list.append(output[1])
        frequency_list.append(output[2])
        std_of_pos_diff_list.append(output[3])
        mean_of_pos_diff_list.append(output[4])
        num_of_chromosomes_list.append(output[5])
        max_position_difference_list.append(output[6])
        min_position_difference_list.append(output[7])
    return [gene_annotation_percent_list, read_length_list, frequency_list, std_of_pos_diff_list, mean_of_pos_diff_list, num_of_chromosomes_list, max_position_difference_list, min_position_difference_list]

def make_pairings_for_scatter(data_lists):
    gene_annotation_percent_list = data_lists[0]
    read_length_list = data_lists[1]
    frequency_list = data_lists[2]
    stdv_list = data_lists[3]
    mean_of_pos_diff_list = data_lists[4]
    num_of_chromosomes_list = data_lists[5]
    max_position_difference_list = data_lists[6]
    min_position_difference_list = data_lists[7]

    gene_length = (gene_annotation_percent_list, read_length_list)
    gene_freq = (gene_annotation_percent_list, frequency_list)
    gene_stdv = (gene_annotation_percent_list, stdv_list)
    gene_pdm = (gene_annotation_percent_list, mean_of_pos_diff_list)
    gene_chrom = (gene_annotation_percent_list, num_of_chromosomes_list)
    gene_max_posdiff = (gene_annotation_percent_list, max_position_difference_list)
    gene_min_posdiff = (gene_annotation_percent_list, min_position_difference_list)

    # length_freq = (read_length_list, frequency_list)
    # length_stdvm = (read_length_list, mean_of_stdv_list)
    # length_pdm = (read_length_list, mean_of_pos_diffs)
    # length_chrom = (read_length_list, num_chromosomes)
    #
    # freq_stdvm = (frequency_list, mean_of_stdv_list)
    # freq_pdm = (frequency_list, mean_of_pos_diffs)
    # freq_chrom = (frequency_list, num_chromosomes)
    #
    # stdvm_pdm = (mean_of_stdv_list, mean_of_pos_diffs)
    # stdvm_chrom = (mean_of_stdv_list, num_chromosomes)
    #
    # pdm_chrom = (mean_of_pos_diff_list, num_chromosomes)

    return [gene_length, gene_freq, gene_stdv, gene_pdm, gene_chrom, gene_max_posdiff, gene_min_posdiff]
