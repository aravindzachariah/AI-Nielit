#Q1 and Q2
library(caret)
library(e1071)
dS=iris
head(iris)
v=createDataPartition(dS$Species,p=0.8,list=FALSE)
trainSet=dS[v,]
testSet=dS[-v,]
fKNN=train(Species~.,data=trainSet,method="knn")
p=predict(fKNN,testSet)
confusionMatrix(testSet[,5],p)

#Q3
T=read.table(file.choose())
head(T)
T1=T[,-1]
T1
v=createDataPartition(T1$V9,p=0.9,list=FALSE)
train1=T1[v,]
test1=T1[-v,]
fKNN1=train(V9~.,data=train1,method="knn")
p1=predict(fKNN1,test1)
confusionMatrix(test1$V9,p1)

