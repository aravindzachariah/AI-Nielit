from textblob.classifiers import NaiveBayesClassifier as NBC
import glob
import sys
f=glob.glob("/home/aravind/AI-Nielit/NLP/Day3_Nov14/A4/Data/*/*")
trainData=[]
for i in f:
	s=i.split('/')
	cls=s[-2]
	f=open(i,"r")
	f=f.read().strip()
	tup=f,cls
	trainData.append(tup)
print "Data Importing Completed"
classifier=NBC(trainData)
print "Training Complete"
f=open('Test',"r")
f1=f.read()
testData=[]
testData.append(f1)
print "Test Data\n-------------------------------------"
print f1
print "-------------------------------------"
c=classifier.classify(testData)
print c

