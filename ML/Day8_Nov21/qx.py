from sklearn.model_selection import cross_val_score,train_test_split,KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import preprocessing
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
#from Tkinter import filedialog
from PIL import ImageTk
import  PIL.Image as Im
import os
import tkFileDialog as filedialog
from Tkinter import * 
import Tkinter as tk
import ttk
wm = Tk()
L = tk.Listbox(wm,selectmode=MULTIPLE,width=20,height=10)
L.bind('<FocusOut>', lambda e: listbox.selection_clear(0, END))
Li= tk.Listbox(wm,width=20,height=10)
Lo= tk.Listbox(wm,width=20,height=10)
global fl,data,il,ol
#img = ImageTk.PhotoImage(Image.open("foo.png"))
image = Im.open("foo.png")
photo = ImageTk.PhotoImage(image)
t1=StringVar()
t2=StringVar()
t3=StringVar()
il=list()
ol=list()
S=""
D=dict()
def fS():
	global fl,data,D
	wm.filename=filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
	fl=wm.filename
	data=pd.read_csv(fl)
	k=list(data)
	j=0
	for i in k:
		D[i]=j
		j+=1
		S=str(i)
		L.insert(END,S)
	t3.set(fl)
def rI():
	return
def rO():
	return
def selecti():
	reslist = list()
	seleccion = L.curselection()
    	for i in seleccion:
        	ED = L.get(i)
        	reslist.append(ED)
    	for val in reslist:
		il.append(D[val])
        	Li.insert(END,str(val))
def selecto():
      	reslist = list()
        seleccion = L.curselection()
        for i in seleccion:
                ED = L.get(i)
                reslist.append(ED)
        for val in reslist:
                ol.append(D[val])
                Lo.insert(END,str(val))
def Comp():
	global il,ol,data,img
	le=preprocessing.LabelEncoder()
	for col in data.columns.values:
		if data[col].dtypes=='object':
			le.fit(data[col].values)
       			data[col]=le.transform(data[col])
	data=data.dropna(axis=0, how='any')
	data=data.as_matrix()
	#il=il.split(",")
	#il=[int(x) for x in il]
	#ol=ol.split(",")
        #ol=[int(x) for x in ol]
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
	#canvas = FigureCanvasTkAgg(fig1, master=wm)  
	#canvas.draw()
	#canvas.grid(column=0,row=12)
	ax.set_xticklabels(names)
	plt.savefig('foo.png')
	img = ImageTk.PhotoImage(Image.open("foo.png"))
	plt.show()
wm.title("Algorithm Selector ")
wm.geometry('800x400')
frame = ttk.Frame(wm, padding=(3, 3, 12, 12))
frame.grid(column=0, row=0, sticky="N, S, E, W")
L1=Entry(wm,textvariable=t3,width=60)
L1.grid(column=0,row=0,columnspan=2)
b1=Button(wm,text='Select Data File',command=fS)
b1.grid(column=2,row=0)
L.grid(column=0,row=5)
Li.grid(column=1,row=5)
Lo.grid(column=2,row=5)
b2=Button(wm,text='Set Input',command=selecti)
b2.grid(column=1,row=7)
b3=Button(wm,text='Set Output',command=selecto)
b3.grid(column=2,row=7)
b4=Button(wm,text='Test Algirithms',command=Comp)
b4.grid(column=3,row=10)
panel = Label(wm, image = photo)
panel.grid(column=3,row=12)
wm.mainloop()


