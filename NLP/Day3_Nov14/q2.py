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
	tup=f,s
	trainData.append(tup)
print "Data Importing Completed"
classifier=NBC(trainData)
print "Training Complete"
dir=sys.argv[1]
f=open(i,"r")
f1=f.read().strip()
testData=[]
testData.append(f1)
print "Test Data\n-------------------------------------"
print type(testData)
print "-------------------------------------"
c=classifier.classify(testData)
print c

