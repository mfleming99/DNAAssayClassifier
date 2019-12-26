from subprocess import call
for i in range(100):
    call(['dot', '-Tpng', 'third_forest_trees/tree' + str(i) + '.dot', '-o', 'third_forest_trees/tree' + str(i)+ '.png', '-Gdpi=600'])
