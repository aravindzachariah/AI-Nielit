from textblob .classifiers import NaiveBayesClassifier
import glob
f=glob.glob("/home/ai13/Codes/NLP/NLP3_Nov14/Assignment 3/*/*")
trainData=[]
for i in f:
	cls=i.split('/')[-2]
	data=open(i).read().replace('\n','')
	tupple=(data,cls)
	trainData.append(tupple)
len(f)
#classifier=NaiveBayesClassifier(trainData)
	
