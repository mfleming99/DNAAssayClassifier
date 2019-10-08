import numpy as np
import matplotlib.pyplot as plt

def make_scatterplot(data_wgs, data_srna, data_mrna, name):
    colors = ("red", "green", "blue")
    groups = ("WGS", "SmallRNA", "RNA")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
    x_wgs = data_wgs[0]
    y_wgs = data_wgs[1]
    ax.scatter(x_wgs, y_wgs, alpha=0.8, c=colors[0], edgecolors='none', s=30, label=groups[0])
    x_srna = data_srna[0]
    y_srna = data_srna[1]
    ax.scatter(x_srna, y_srna, alpha=0.8, c=colors[1], edgecolors='none', s=30, label=groups[1])
    x_mrna = data_mrna[0]
    y_mrna = data_mrna[1]
    ax.scatter(x_mrna, y_mrna, alpha=0.8, c=colors[2], edgecolors='none', s=30, label=groups[2])
    plt.title(name)
    plt.legend()
    plt.savefig(name + '.png')

def make_each_scatterplot(data_list_wgs, data_list_srna, data_list_mrna):
        data_names = []
        data_names.append("GenePercent_ReadLength")
        data_names.append("GenePercent_ReadFrequency")
        data_names.append("GenePercent_MeanOfPDSTDs")
        data_names.append("GenePercent_MeanOfPositionDifference")
        data_names.append("GenePercent_NumberOfChromosomes")
        data_names.append("GenePercent_MaxOfPDSTDs")
        data_names.append("GenePercent_MinOfPDSTDs")
        data_names.append("GenePercent_MaxOfPositionDifference")
        data_names.append("GenePercent_MinOfPositionDifference")
        for i in range(len(data_list_wgs)):
            make_scatterplot(data_list_wgs[i], data_list_srna[i], data_list_mrna[i], data_names[i])
