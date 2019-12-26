from sklearn.tree import export_graphviz
import pickle

def main():
    forest = pickle.load(open('third_forest', 'rb'))
    for i in range(len(forest.estimators_)):
        filename = 'tree' + str(i) + '.dot'
        export_graphviz(forest.estimators_[i], 
                out_file='third_forest_trees/tree' + str(i) + '.dot', 
                rounded = True, proportion = False, 
                precision = 2, filled = True)


if __name__ == '__main__':
    main()
