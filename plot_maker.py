import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 60
    g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
    lengthVfreq(g1)

def lengthVfreq(wgs_data):
    colors = ("red")
    groups = ("WGS", "poop")
    data = []
    data.append(wgs_data)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    plt.title('Matplot scatter plot')
    plt.legend(loc=2)
    plt.show()

if __name__ == '__main__':
    main()
