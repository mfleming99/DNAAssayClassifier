import numpy as np
import matplotlib.pyplot as plt

def make_scatterplot(data, name):
    colors = ("red")
    groups = ("WGS", "poop")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="0")
    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    plt.title(name)
    plt.legend(loc=2)
    plt.savefig(name + '.png')

def make_each_scatterplot(data_list):
        data_names = []
        data_names.append("Gene Percent vs. Read Length")
        data_names.append("Gene Percent vs. Read Frequency")
        data_names.append("Gene Percent vs. Mean of PD STDs")
        data_names.append("Gene Percent vs. Mean of Position Difference")
        data_names.append("Gene Percent vs. Number of Chromosomes")
        data_names.append("Gene Percent vs. Max of PD STDs")
        data_names.append("Gene Percent vs. Min of PD STDs")
        data_names.append("Gene Percent vs. Max of Position Difference")
        data_names.append("Gene Percent vs. Min of Position Difference")
        for i in range(len(data_list)):
            make_scatterplot(data_list[i], data_names[i])
