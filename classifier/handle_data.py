import numpy as np
from numpy import genfromtxt

def getMatrix(wgs_file, mrna_file, srna_file):
    wgs = genfromtxt(wgs_file, delimiter=',', dtype=float)
    mrna = genfromtxt(mrna_file, delimiter=',', dtype=float)
    srna = genfromtxt(srna_file, delimiter=',', dtype=float)
    wgs_label = np.zeros((wgs.shape[0]), dtype='int')
    mrna_label = np.ones((mrna.shape[0]), dtype='int')
    srna_label = np.zeros((srna.shape[0]), dtype = 'int')
    srna_label.fill(2)
    X = np.vstack((wgs, mrna, srna))
    Y = np.hstack((wgs_label, mrna_label, srna_label))
    X = X * 1000
    return X,Y
