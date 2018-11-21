from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,train_test_split,KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import preprocessing
#from Tkinter import filedialog
import tkFileDialog as filedialog
from Tkinter import * 
import Tkinter as tk
wm = Tk()
L = tk.Listbox(wm,width=50,height=10)
t1=StringVar()
t2=StringVar()
global fl,data,il,ol
S=""
def fS():
	global fl,data
	wm.filename=filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
	fl=wm.filename
	data=pd.read_csv(fl)
	k=list(data)
	for i in k:
		S=str(i)
		L.insert(END,S)
def rI():
	global il
	il=t1.get()
def rO():
	global ol
	ol=t2.get()
def Comp():
	global il,ol,data
	le=preprocessing.LabelEncoder()
	for col in data.columns.values:
		if data[col].dtypes=='object':
			le.fit(data[col].values)
       			data[col]=le.transform(data[col])
	data=data.dropna(axis=0, how='any')
	data=data.as_matrix()
	il=il.split(",")
	il=[int(x) for x in il]
	ol=ol.split(",")
        ol=[int(x) for x in ol]
	X=data[:,il]
	y=data[:,ol]
	kfold=KFold(10,random_state=7)
	models=[]
	models.append(("KNN",KNeighborsClassifier()))
	models.append(("NB",GaussianNB()))
	models.append(("LG",LogisticRegression()))
	models.append(("CART",DecisionTreeClassifier()))
	#models.append(("SVM",SVC()))
	results=[]
	names=[]
	scoring='accuracy'
	for name,model in models:
		kfold=KFold(n_splits=10,random_state=7) 
		v=cross_val_score(model,X,y,cv=kfold,scoring="accuracy")
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
wm.title("Algorithm Selector ")
wm.geometry('800x600')
b1=Button(wm,text='Select Data File',command=fS)
b1.pack()
L.pack()
e1=Entry(wm,textvariable=t1)
e1.pack()
b2=Button(wm,text='Set Input',command=rI)
b2.pack()
e2=Entry(wm,textvariable=t2)  
e2.pack()
b3=Button(wm,text='Set Output',command=rO)
b3.pack()
b4=Button(wm,text='Test Algirithms',command=Comp)
b4.pack()
wm.mainloop()


