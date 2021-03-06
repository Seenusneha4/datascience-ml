from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn import tree
iris=load_iris()
x,y=iris.data,iris.target
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
print(tree.plot_tree(clf))
tree.plot_tree(clf)
plt.show()