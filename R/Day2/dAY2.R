V=c(seq(1,20,1),seq(19,1,-1))
x=c(4,6,3)
r1=rep(x,10)
r1
r2=rep(x,10,length.out=31)
r2
r3=c(rep(4,10),rep(6,20),rep(3,30))
r3

R <- c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
H <- c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
V=(1/3)*pi*R^2*H
V
round(V)
max(V)
min(V)

A=sample(0:999,250)
A
B=B[which(B>900)]
B
C=sort(B)
C
H=c(180, 165, 160, 193) 
W=c(87, 58, 65, 100)
H=H/100
BMI=W/H^2
BMI
ob=BMI[which(BMI>25)]
ob
avg=mean(BMI)
avg

dry <- c(77, 93, 92, 68, 88, 75, 100)
sum(dry)
length(dry)
mean(dry)
sum(dry)/length(dry) ## Equation for mean, cross check value with Mean above
sort(dry)
median(dry)
sd(dry)
var(dry)
##Variance
sd(dry)^2
min(dry)
max(dry)
summary(dry)

R=sample(1:20,10,replace=TRUE)
R
R2=R[which(R%%2==0)]
R2