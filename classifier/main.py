import argparse as ap
import pickle
import sklearn
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from handle_data import getMatrix
from sklearn.decomposition import PCA
import numpy as np

def standardize(X):
    features = np.zeros((X.shape[1], X.shape[0]), dtype = float)
    means = np.zeros(X.shape[1], dtype = float)
    std = np.zeros(X.shape[1], dtype = float)
    for i in range(X.shape[1]):
        features[i] = X[:, i]
    for i in range(X.shape[1]):
        std[i] = np.nanstd(features[i])
        means[i] = np.nanmean(features[i])
    for i in range(X.shape[1]):
        X[:, i] = np.subtract(X[:, i], means[i])
        if std[i] > 0:
            X[:, i] = np.divide(X[:, i], std[i])
    return X

def predict(X, model):
    predictions = model.predict(X)
#    print(predictions)

def get_args():
    p = ap.ArgumentParser()
    p.add_argument("--wgs", type=str, required=True,
        help="Where is the wgs csv")
    p.add_argument("--mrna", type=str, required=True,
        help="Where is the mrna csv")
    p.add_argument("--srna", type=str, required=True,
        help="Where is the srna")
    return p.parse_args()

def main(args):
    wgs = args.wgs
    mrna = args.mrna
    srna = args.srna
    X,y = getMatrix(wgs, srna, mrna)
    X = standardize(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    forest = RandomForestClassifier(max_depth = 3, n_estimators = 80)
    forest.fit(X_train, y_train)
    scores = cross_val_score(forest, X_train, y_train, cv=10, scoring='accuracy')
    pickle.dump(forest, open('forest', 'wb'))
    pickle.dump(scores, open('forest__scores', 'wb'))
    test_acc = forest.score(X_test, y_test)
    print(str(i) + ',' + str(test_acc))    
    pickle.dump(X_train, open('x_train', 'wb'))
    pickle.dump(X_test, open('x_test', 'wb'))
    pickle.dump(y_train, open('y_train', 'wb'))
    pickle.dump(y_test, open('y_test', 'wb'))
    class_names = ['wgs', 'mrna', 'srna']
    pca = PCA(n_components= i + 5)
    X_t = pca.fit_transform(X_test)
    X = pca.fit_transform(X_train)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y_train)
    pickle.dump(knn, open('knn', 'wb'))  
    test_acc = knn.score(X_t, y_test)

if __name__ == '__main__':
    args = get_args()
    main(args)
