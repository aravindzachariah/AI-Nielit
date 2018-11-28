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
from PIL import ImageTk
import  PIL.Image as Im
import os
import tkFileDialog as filedialog
from Tkinter import * 
import Tkinter as tk
import ttk
import pickle as pk
wm = Tk()
wm.title("Kakka	 ")
wm.geometry('800x450')

tab_control = ttk.Notebook(wm)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

L = tk.Listbox(tab2,selectmode=MULTIPLE,width=20,height=10)
L.bind('<FocusOut>', lambda e: listbox.selection_clear(0, END))
Li= tk.Listbox(tab2,width=20,height=10)
Lo= tk.Listbox(tab2,width=20,height=10)

txt = Text(tab1,width=97,height=15,fg='BLUE') 

global fl,data,il,ol
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
	txt.insert(END,str(data.head())+"\n[Displaying]"+"\n\nTotal Size: \n"+str(data.shape))	
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
	ax.set_xticklabels(names)
	plt.savefig('foo.png')
	img = ImageTk.PhotoImage(Image.open("foo.png"))
	plt.show()


tab_control.add(tab1, text='Data Selection') 
L1=Entry(tab1,textvariable=t3,width=80)
b1=Button(tab1,text='Select Data File',command=fS)
L1.grid(row=0,column=0,padx=5,pady=5,columnspan=6)
b1.grid(row=0,column=6,padx=5,pady=5,columnspan=1)
txt.grid(row=1,column=0,rowspan=6,columnspan=8,padx=5,pady=5)
tab_control.pack(expand=1, fill='both')

tab_control.add(tab2, text='Preprocessing') 
tab_control.pack(expand=1, fill='both')
b2=Button(tab2,text='Set Input',command=selecti)
b3=Button(tab2,text='Set Output',command=selecto)
L.grid(row=0,column=0,padx=5,pady=5)
Li.grid(row=1,column=1,padx=5,pady=5)
Lo.grid(row=1,column=3,padx=5,pady=5)
b2.grid(row=1,column=0,padx=5,pady=5)
b3.grid(row=1,column=2,padx=5,pady=5)


tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Learning Algoritms') 
tab_control.pack(expand=1, fill='both')
rad1 = Radiobutton(tab3,text='KNeighbours', value=1)
rad2 = Radiobutton(tab3,text='Logistic Regression', value=2)
rad3 = Radiobutton(tab3,text='Decision Tree', value=3)
rad4 = Radiobutton(tab3,text='Naive Bayes', value=4)
rad5 = Radiobutton(tab3,text='All', value=5)
rad1.grid(row=0,column=0,padx=5,pady=5)
rad2.grid(row=0,column=1,padx=5,pady=5)
rad3.grid(row=0,column=2,padx=5,pady=5)
rad4.grid(row=0,column=3,padx=5,pady=5)
rad5.grid(row=0,column=4,padx=5,pady=5)
b4=Button(tab2,text='Test Algirithms',command=Comp)

wm.mainloop()


