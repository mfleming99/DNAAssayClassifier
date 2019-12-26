import argparse as ap
import pickle
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from handle_data import getMatrix
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
    #print(means)
    #print(std)
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
#    print(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#`    print(X_train.shape, y_train.shape)
#   print(X_test.shape, y_test.shape)
    print(y_test)
    forest = RandomForestClassifier(max_depth = 4)
    forest.fit(X_train, y_train)
#    knn = KNeighborsClassifier(n_neighbors=3)
#    knn.fit(X_train, y_train)
    scores = cross_val_score(forest, X_train, y_train, cv=10, scoring='accuracy')
    #pickle.dump(knn, open('first_knn', 'wb'))
    print(scores)
    pickle.dump(forest, open('third_forest', 'wb'))
    #prediction_score = knn.score(X_test, y_test)
    #predict(X_test,knn)
    prediction_score = forest.score(X_test, y_test)
    print(prediction_score)
    print(forest.feature_importances_)
#    print(forest.decision_path.feature_importances_)

if __name__ == '__main__':
    args = get_args()
    main(args)
