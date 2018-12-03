#Question1,2
sname=c("Alex","Lilly","Mark")
Age=c(25,31,23)
Height=c(177,163,190)
Weight=c(57,69,83)
Sex=c("F","F","M")
d1=data.frame(sname,Age,Height,Weight,Sex)
Working=c("Yes","No","No")
d2=data.frame(sname,Working)
d3=cbind(d1,d2)
mh=mean(d3$Height)
BMI=d3$Weight/(d3$Height/100)^2
d3=cbind(d3,BMI)
d3
Healthy=ifelse(d3$BMI<25,"True","False")
Healthy
d3=cbind(d3,Healthy)
d3

#Question3,4,5
t=read.table(file.choose(),head=TRUE)
t1=read.csv(file.choose(),head=TRUE)
r=c('r1','r2')
c=c('c1','c2','c3')
w=c('w1','w2','w3')
a=array(data=c(1:20),dim=c(2,3,3),dimnames = list(r,c,w))

#Question6
cars=data.frame(mtcars$mpg,mtcars$cyl,mtcars$hp)
cars
first=head(mtcars,5)
last=tail(mtcars,5)
cars1=rbind(first,last)
cars1

#Question7
sum=function(a,b)
{
  s=a+b
  print(s)
}
sum(2,5)
sum(b=5,a=2)
 

