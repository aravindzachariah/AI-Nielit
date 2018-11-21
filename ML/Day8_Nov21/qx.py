from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,train_test_split,KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import pandas as pd
from Tkinter import *
from tkFileDialog import askDirectory
root=Tk()
root.filename=tkFileDilog.askopenfilename(initialdir ="/",title="Select File",filetypes=(("csv files","*.csv"),("all files","*.*")))
print root.filename
root.title('Algorithm Tester')
root.geometry('200x300')
data=load_iris()
X=data.data
y=data.target
kfold=KFold(10,random_state=7)
models=[]
models.append(("KNN",KNeighborsClassifier()))
models.append(("NB",GaussianNB()))
models.append(("LG",LogisticRegression()))
models.append(("CART",DecisionTreeClassifier()))
models.append(("SVM",SVC()))
results=[]
names=[]
scoring='accuracy'
for name,model in models:
	kfold=KFold(n_splits=10,random_state=7) 
	v=cross_val_score(model,X,y,cv=kfold,scoring=scoring)
	results.append(v)
	names.append(name)
	print(name)
	print(v)
fig=plt.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



