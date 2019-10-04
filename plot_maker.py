import numpy as np
import matplotlib.pyplot as plt

def make_scatterplot(data, name):
    color = "red"
    group = "WGS"
    print(data)
    print(name)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
    x = data[0]
    y = data[1]
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    plt.title(name)
    plt.legend(loc=2)
    plt.savefig(name + '.png')

def make_each_scatterplot(data_list):
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
        for i in range(len(data_list)):
            make_scatterplot(data_list[i], data_names[i])
