age=c(2,3,5,7,8) 
weight=c(14,20,32,42,44)
rel=lm(weight~age)
rel

plot(age,weight)
abline(rel)
a1=data.frame(age=6)
predict(rel,a1)

x=c(8,7,6,4,2,1)
y=c(15,19,25,23,34,40)
cor(x,y,method="pearson")
rel1=lm(x~y)
rel11=lm(y~x)
d1=data.frame(y=2)
d2=data.frame(x=5)
predict(rel1,d1)
predict(rel11,d2)

M=c(6,4,8,5,3.5)
C=c(6.5,4.5,7,5,4)
rel2=lm(C~M)
plot(M,C)
abline(rel2)
m1=data.frame(M=7.5)
predict(rel2,m1)

H=c(186,189,190,192,193,193,198,201,203,205)
W=c(85,85,86,90,87,91,93,103,100,101)
cc=cor(H,W,method="pearson")
cc
rel3=lm(W~H)
plot(H,W)
abline(rel3)
h1=data.frame(H=208)
predict(rel3,h1)

Hr=c(80,79,83,84,78,60,82,85,79,84,80,62)
Pr=c(300,302,315,330,300,250,300,340,315,330,310,240)
cc1=cor(Hr,Pr,method="pearson")
cc1
rel4=lm(Pr~Hr)
plot(Hr,Pr)
abline(rel4)

Ns=c(6,7,8,9,10)
Nt=c(4,3,3,2,1)
cc2=cor(x,y,method="pearson")
cc2
rel5=lm(Nt~Ns)
plot(Ns,Nt)
abline(rel5)
ns1=data.frame(Ns=8)
predict(rel5,ns1)


Ts=c(25,42,33,54,29,36)
Sl=c(42,72,50,90,45,48)
cc3=cor(Ts,Sl,method="pearson")
cc3
rel6=lm(Sl~Ts)
t1=data.frame(Ts=47)
predict(rel6,t1)