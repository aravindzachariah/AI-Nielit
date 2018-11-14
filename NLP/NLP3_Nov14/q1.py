from textblob .classifiers import NaiveBayesClassifier
trainData=[]
f=open('TrainSet.txt','r')
data=f.readline().strip()
while data:
	splitData=data.split(',')
	category=splitData[0]
	content=splitData[1]
	tuple=content,category
	trainData.append(tuple)
	data=f.readline().strip()
classifier=NaiveBayesClassifier(trainData)
print "Training Done"
f.close()
f1=open('TestSet.txt','r')
data=f1.read()
if classifier.classify(data)=='C01':
	print "Bacterial Infections and Mycoses"
else:
	print "Virus Diseases"    
